#!/usr/bin/env python3
"""
check-risk.py — risk of shipping, scored against a named destination.

"Risk of shipping" is meaningless without saying SHIPPING TO WHOM. The same
artifact carries three different risk profiles:

    internal-demo  shown to colleagues, no real user data, no real inference
    pilot          real people, real disclosures, small n, consented
    production     general availability

So the destination is a required argument. A tool that returns one number for
"risk" invites the number to be quoted in the wrong context, which is the exact
failure this repo exists to document.

HOW THIS DIFFERS FROM ux-score.py:
    ux-score counts criteria. This counts HAZARDS — what actually goes wrong, to
    whom, and how badly. A project can be 90% conformant and carry a critical
    hazard, because conformance is measured against what you thought to write
    down and hazards are not.

SCORING:
    exposure   0.0-1.0  how likely this hazard is reached at this destination
    severity   1-4      1 annoying · 2 harmful · 3 serious · 4 critical
    risk       exposure x severity, and any severity-4 hazard with exposure > 0
               sets a BLOCKING verdict regardless of the total. Critical hazards
               do not average away.

Hazards are READ FROM HAZARDS.md, not hardcoded here — the register is data a
team can edit without touching a checker. Every row must name a real source; a
hypothetical hazard belongs in a risk workshop, not in the register.

Exit codes:
    0  ship-acceptable at this destination
    9  ship-blocking hazard present at this destination
"""

import sys
import os
import re
import subprocess

DESTINATIONS = ("internal-demo", "pilot", "production")


def live_violations():
    exe = os.path.join("scripts", "check-design.py")
    if not os.path.isfile(exe):
        return 0
    try:
        r = subprocess.run([sys.executable, exe], capture_output=True,
                           text=True, timeout=60)
        m = re.search(r"=== (\d+) VIOLATION", r.stdout)
        return int(m.group(1)) if m else 0
    except Exception:
        return 0


def human_rows():
    """Count standing HUMAN rows in OPEN.md."""
    if not os.path.isfile("OPEN.md"):
        return 0
    n, inblock = 0, False
    for line in open("OPEN.md", encoding="utf-8"):
        if line.startswith("## Open rows"):
            inblock = True
            continue
        if inblock and line.startswith("## "):
            break
        if inblock and re.match(r"^\|\s*H-\d+\s*\|\s*HUMAN\s*\|", line):
            n += 1
    return n


def load_hazards(dest):
    """Read HAZARDS.md. The register is data, not code.

    The hazards used to be a literal list inside this script, which made it
    unportable — every project would have had to edit the source — and it put
    project content in a place nobody reviews. A hazard register is exactly the
    kind of thing a team should be able to edit without touching a checker.
    """
    if not os.path.isfile("HAZARDS.md"):
        return None
    col = {"internal-demo": 5, "pilot": 6, "production": 7}[dest]
    out, inb = [], False
    for line in open("HAZARDS.md", encoding="utf-8"):
        if line.startswith("## Hazards"):
            inb = True
            continue
        if inb and line.startswith("## "):
            break
        if not inb or not line.startswith("|"):
            continue
        f = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(f) < 10 or f[0] in ("id",) or set(f[0]) <= set("-"):
            continue
        try:
            sev = int(f[2])
            exp = float(f[col - 1])
        except ValueError:
            continue
        out.append(dict(id=f[0], kind=f[1], severity=sev,
                        floor=f[3].upper() == "FLOOR", exposure=exp,
                        what=f[7], source=f[8], mitigation=f[9]))
    return out


def main():
    dest = sys.argv[1] if len(sys.argv) > 1 else None
    if dest not in DESTINATIONS:
        print("usage: check-risk.py <" + " | ".join(DESTINATIONS) + ">")
        print("\nThe destination is required. 'Risk of shipping' with no stated")
        print("destination is a number waiting to be quoted in the wrong context.")
        return 2

    hz = load_hazards(dest)
    if hz is None:
        print("BROKEN — HAZARDS.md not found.")
        print("The hazard register is data, not code. Create it with the strict")
        print("table format, or this script has nothing to evaluate. An empty")
        print("hazard register is a claim that nothing can go wrong.")
        return 3
    if not hz:
        print("BROKEN — HAZARDS.md has no parsable rows.")
        print("Zero hazards is reported as a failure on purpose.")
        return 3
    print(f"  {len(hz)} hazard(s) in the register · "
          f"live checks: check-design.py reports {live_violations()} violation(s), "
          f"check-blocked.sh reports {human_rows()} open HUMAN row(s)\n")

    print("=" * 74)
    print(f"RISK OF SHIPPING — destination: {dest.upper()}")
    print("=" * 74)

    blocking = [h for h in hz if h["severity"] == 4 and h["exposure"] > 0]
    scored = sorted(hz, key=lambda h: -(h["exposure"] * h["severity"]))

    for h in scored:
        r = h["exposure"] * h["severity"]
        sev = {1: "annoying", 2: "harmful", 3: "serious", 4: "CRITICAL"}[h["severity"]]
        flag = "  <-- SHIP-BLOCKING" if h in blocking else ""
        tag = "FLOOR" if h["floor"] else "fit"
        if h["exposure"] == 0:
            band = "not reached at this destination"
        else:
            band = f"risk {r:.1f}  (exposure {h['exposure']:.0%} x {sev})"
        print(f"\n[{h['id']}] {h['kind']:11s} {tag:5s}  {band}{flag}")
        print(f"   what       {h['what']}")
        print(f"   source     {h['source']}")
        print(f"   mitigation {h['mitigation']}")

    reached = [h for h in hz if h["exposure"] > 0]
    total = sum(h["exposure"] * h["severity"] for h in reached)
    worst = max((h["exposure"] * h["severity"] for h in reached), default=0)

    print("\n" + "=" * 74)
    print(f"  hazards reached at this destination : {len(reached)} of {len(hz)}")
    print(f"  aggregate risk                     : {total:.1f}")
    print(f"  worst single hazard                : {worst:.1f}")
    print(f"  FLOOR hazards reached              : "
          f"{sum(1 for h in reached if h['floor'])}")

    print("\n  Aggregate is for tracking movement over time, not for comparing")
    print("  across destinations — the hazard set changes. A single CRITICAL")
    print("  hazard blocks regardless of the aggregate. Criticals do not average")
    print("  away, which is why the verdict is not a threshold on the total.")

    if blocking:
        print(f"\nVERDICT: SHIP-BLOCKING at {dest} — "
              f"{len(blocking)} critical hazard(s) reached:")
        for h in blocking:
            print(f"  {h['id']}  {h['kind']}")
        nfloor = sum(1 for h in blocking if h["floor"])
        if nfloor:
            print(f"\n{nfloor} of them are FLOOR — they hold whether or not the concept")
            print("is right, and they are not gated on problem validation. Read each")
            print("mitigation above: a hazard whose mitigation names a reviewer or a")
            print("decision has no engineering fix at all.")
        return 9

    print(f"\nVERDICT: no critical hazard reached at {dest}.")
    if any(h["floor"] for h in reached):
        print("FLOOR hazards are present and are not gated on problem validation —")
        print("fix them regardless of what the reaction test says.")
    print("This is not an approval. It is the absence of a critical hazard at one")
    print("named destination.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
