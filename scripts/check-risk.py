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

Every hazard below is grounded in a specific file or a specific measured defect.
None are hypothetical. Sources are printed with each one.

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


def build(dest, nviol, nhuman):
    """Return the hazard list for this destination.

    exposure is per-destination on purpose: an Art. 9 hazard has exposure 0 at an
    internal demo with no real data, and 1.0 the moment a real person discloses.
    """
    D = DESTINATIONS.index(dest)  # 0 demo, 1 pilot, 2 production
    H = []

    H.append(dict(
        id="RSK-01", kind="CLAIM",
        what="The artifact is read as evidence the concept works. Its own numbers "
             "(70.37% / 70.97%) are evidence AGAINST it, and they sit on the page "
             "next to a working demo.",
        exposure=[0.8, 0.6, 0.4][D], severity=3, floor=False,
        source="prototypes/doodle-journal/SOURCES.md; README 'not a stand-alone "
               "deliverable'; MC-04. The repo names this as the foreseeable misuse.",
        mitigation="FidelityBadge above the fold, the red no-data panel, and never "
                   "forwarding the HTML without its brief. Partially mitigated; the "
                   "residual risk is a screenshot in a deck."))

    H.append(dict(
        id="RSK-02", kind="EXCLUSION",
        what=f"{nviol} live accessibility/design violations, including no focus "
             f"style anywhere and an unlabelled describe-input textarea. A "
             f"keyboard or screen-reader user cannot reliably complete the core "
             f"task.",
        exposure=[0.5, 1.0, 1.0][D], severity=3, floor=True,
        source="scripts/check-design.py (exit 6); T4 audit found the unlabelled "
               "textarea, which no design.md criterion names.",
        mitigation="FLOOR work. Not gated on problem validation. Fix before any "
                   "destination that includes a real user."))

    H.append(dict(
        id="RSK-03", kind="LEGAL",
        what="Inferring emotional state from a journal entry is GDPR Art. 9 "
             "special-category processing. The consent copy is a UI pattern, not a "
             "lawful Art. 9 disclosure, and no qualified reviewer has seen it.",
        exposure=[0.0, 1.0, 1.0][D], severity=4, floor=True,
        source="OPEN.md H-02; design.md G3-22; scout/05. Exposure is 0 at an "
               "internal demo because the pipeline is mocked — no inference occurs.",
        mitigation="Named reviewer sign-off, or descope inference. There is no "
                   "engineering fix for a consent defect."))

    H.append(dict(
        id="RSK-04", kind="LEGAL",
        what="No retention or deletion SLA exists for an entry, its doodle, or "
             "derived inference data. Nothing states how long anything is kept.",
        exposure=[0.0, 1.0, 1.0][D], severity=4, floor=True,
        source="OPEN.md H-03; design.md G3-23; spec.md FR-010 NEEDS CLARIFICATION.",
        mitigation="A specified, sourced timing. Blocks any real-data destination."))

    H.append(dict(
        id="RSK-05", kind="HARM",
        what="A generated image misrepresents a person's own emotional disclosure "
             "in a way they find unsettling. 70.97% used negative language; "
             "participants reported actively avoiding images they found grotesque.",
        exposure=[0.1, 0.9, 0.9][D], severity=3, floor=False,
        source="SRC-001 PMC9810434, fetched and read. n=54.",
        mitigation="Per-entry consent (UXI-10), one-tap discard (UXI-03), entry text "
                   "always primary (UXI-01). These reduce the cost of the failure; "
                   "they do not reduce its rate. Rate is R-01/R-02, untested."))

    H.append(dict(
        id="RSK-06", kind="INVESTMENT",
        what="The core mechanism may simply not work. The nearest primary study "
             "found 70.37% judged generated images irrelevant to their own "
             "narrative, and the predicted-most-likely test outcome is "
             "re-scope-or-kill.",
        exposure=[0.7, 0.7, 0.7][D], severity=2, floor=False,
        source="SRC-001; ux.md ds:6.3 kill criteria; OPEN.md R-01, R-02.",
        mitigation="Run the reaction test before funding a build. This hazard is "
                   "cheapest to retire and nothing is doing it — H-01 is unresolved."))

    H.append(dict(
        id="RSK-07", kind="DECISION",
        what=f"{nhuman} decisions only a person can make are standing open. An "
             f"agent or a team that proceeds past them has substituted a default "
             f"for a decision nobody made.",
        exposure=[0.6, 0.9, 1.0][D], severity=2, floor=False,
        source="./check-blocked.sh (exit 2); OPEN.md HUMAN rows.",
        mitigation="Answer them or record declining to. check-blocked.sh already "
                   "detects this; nothing enforces it outside a speckit hook."))

    H.append(dict(
        id="RSK-08", kind="EVIDENCE",
        what="58.6% of tagged claims are [A] or [?] — roughly twice the 30% "
             "readiness threshold. For eng this is a change-risk map: the consent "
             "string, the retention number and the whole generation pipeline are "
             "all likely to move.",
        exposure=[0.5, 0.8, 1.0][D], severity=2, floor=False,
        source="briefs/doodle-journal.brief.md tag ledger, 17 of 29, grep-verified.",
        mitigation="Build a seam wherever the evidence is thin. Do not hardcode a "
                   "value that rests on an [A] claim."))

    return H


def main():
    dest = sys.argv[1] if len(sys.argv) > 1 else None
    if dest not in DESTINATIONS:
        print("usage: check-risk.py <" + " | ".join(DESTINATIONS) + ">")
        print("\nThe destination is required. 'Risk of shipping' with no stated")
        print("destination is a number waiting to be quoted in the wrong context.")
        return 2

    nviol = live_violations()
    nhuman = human_rows()
    hz = build(dest, nviol, nhuman)

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
        print("\nBoth are legal, both are FLOOR, and neither has an engineering")
        print("fix. They need a named reviewer and a specified retention timing.")
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
