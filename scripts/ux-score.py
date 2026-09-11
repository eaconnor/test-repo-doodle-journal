#!/usr/bin/env python3
"""
ux-score.py — conformance index and ceiling across ux.md, vision.md, design.md.

WHAT THIS IS NOT, and read this before quoting any number it prints:

    This is NOT a measured UX score. It is NOT a predicted SUS score. No user has
    touched this artifact. Nothing here is validated against human behaviour.

    It is a CONFORMANCE INDEX: of the criteria this project declared for itself,
    how many are settled true, how many are settled false, and how many cannot be
    settled at all without people. Conformance is a necessary condition for
    quality and nowhere near a sufficient one. A product can be 100% conformant
    and solve a problem nobody has.

WHY THE CEILING MATTERS MORE THAN THE BASELINE:

    The useful question is not "what do we score" but "what is the best score
    reachable by working, and what does the rest cost?" So this reports three
    numbers:

      BASELINE  — settled true today
      CEILING   — the best reachable with code alone, no users
      HARD CAP  — why 100% is unreachable without human data, itemised

    The gap between BASELINE and CEILING is a work list, ranked. The gap between
    CEILING and 100% is a research budget. They are different kinds of problem and
    conflating them is how teams polish an artifact instead of validating it.

THE ORDERING RULE, which is the opinionated part:

    Gate 3 conformance is CAPPED while Gate 1 has open criteria. Build quality on
    an unvalidated problem is not quality — a high polish score on something
    nobody needs is an expensive false positive. The cap is stated, not hidden in
    a multiplier.

Exit codes:
    0  reported
    5  a gate file is missing
"""

import re
import os
import sys
import subprocess

GATES = [
    ("ux.md", 1, "Are we solving the right problem?"),
    ("vision.md", 2, "Are we making the right thing?"),
    ("design.md", 3, "Are we making the thing right?"),
]

CRIT_RE = re.compile(r"^- \[([ x])\] (\S+) — (.*)$")

# A criterion is HUMAN-REQUIRED if its verified_by names something only a person
# can produce. Keyword matching is crude but it is mechanical and auditable —
# better than me deciding case by case, which is how the earlier false-green
# claims got in.
HUMAN_MARKERS = [
    "participant", "reviewer", "named reviewer", "test run", "a test run",
    "audit", "keyboard pass", "instrument", "signs off", "commission",
    "in front of a real person", "moved to the Resolved", "a comparison study",
    "measurement", "a review", "a result per message", "evidence that",
    "a state audit", "a composition audit", "a contrast audit", "a focus audit",
    "institutional access", "decision to proceed",
]

# Effort estimate for machine-fixable items, used only to rank the work list.
# Deliberately coarse: S / M / L. A fake precision here would be worse than none.
EFFORT_HINTS = [
    (re.compile(r"prefers-reduced-motion|border-radius|hardcoded hex|emoji|"
                r"aria-label|role=\"img\"|focus ring|:focus", re.I), "S"),
    (re.compile(r"eight states|composition|pressed state|determinate", re.I), "M"),
    (re.compile(r"contrast|CLR-0", re.I), "M"),
]


def parse(path):
    out = []
    if not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8") as f:
        in_block = False
        for line in f:
            if re.match(r"^#{2}\s+(\d+\.\s+)?Acceptance Criteria", line):
                in_block = True
                continue
            if in_block and line.startswith("## "):
                in_block = False
            if not in_block:
                continue
            m = CRIT_RE.match(line.rstrip())
            if m:
                checked = m.group(1) == "x"
                cid = m.group(2)
                body = m.group(3)
                verified = ""
                vm = re.search(r"verified_by:\s*(.*)$", body)
                if vm:
                    verified = vm.group(1)
                human = any(k.lower() in verified.lower() for k in HUMAN_MARKERS)
                out.append({
                    "id": cid, "checked": checked, "body": body,
                    "verified": verified, "human": human,
                })
    return out


def effort(text):
    for rx, e in EFFORT_HINTS:
        if rx.search(text):
            return e
    return "M"


def linter_violations():
    """Machine-found defects that are true today regardless of box state."""
    exe = os.path.join("scripts", "check-design.py")
    if not os.path.isfile(exe):
        return None
    try:
        r = subprocess.run([sys.executable, exe], capture_output=True,
                           text=True, timeout=60)
    except Exception:
        return None
    m = re.search(r"=== (\d+) VIOLATION", r.stdout)
    u = re.search(r"=== (\d+) UNRESOLVED", r.stdout)
    return (int(m.group(1)) if m else 0, int(u.group(1)) if u else 0)


def bar(pct, width=32):
    filled = int(round(pct / 100 * width))
    return "#" * filled + "." * (width - filled)


def main():
    rows = {}
    for path, gate, question in GATES:
        parsed = parse(path)
        if parsed is None:
            print(f"BROKEN — {path} not found. Run from the repo root.")
            return 5
        rows[path] = (gate, question, parsed)

    print("=" * 74)
    print("CONFORMANCE INDEX — not a UX score, not a SUS score.")
    print("Zero users have touched this artifact. Read the header of this file.")
    print("=" * 74)

    tot_all = tot_true = tot_fixable = tot_human = 0
    worklist = []
    gate1_open = 0

    for path, (gate, question, crits) in rows.items():
        n = len(crits)
        true_ = sum(1 for c in crits if c["checked"])
        open_human = [c for c in crits if not c["checked"] and c["human"]]
        open_mach = [c for c in crits if not c["checked"] and not c["human"]]

        baseline = 100 * true_ / n if n else 0
        ceiling = 100 * (true_ + len(open_mach)) / n if n else 0

        if gate == 1:
            gate1_open = len(open_human) + len(open_mach)

        print(f"\nGATE {gate} — {question}")
        print(f"  file        {path}   ({n} criteria)")
        print(f"  baseline    {baseline:5.1f}%  {bar(baseline)}   {true_}/{n} settled true")
        print(f"  ceiling     {ceiling:5.1f}%  {bar(ceiling)}   "
              f"+{len(open_mach)} fixable with code alone")
        print(f"  human-gated {len(open_human):2d} criteria cannot close without people")

        for c in open_mach:
            worklist.append((gate, c["id"], effort(c["body"]), c["body"][:96]))

        tot_all += n
        tot_true += true_
        tot_fixable += len(open_mach)
        tot_human += len(open_human)

    base = 100 * tot_true / tot_all
    ceil = 100 * (tot_true + tot_fixable) / tot_all

    print("\n" + "=" * 74)
    print("OVERALL")
    print(f"  BASELINE  {base:5.1f}%  {bar(base)}   {tot_true}/{tot_all}")
    print(f"  CEILING   {ceil:5.1f}%  {bar(ceil)}   "
          f"reachable with code alone (+{tot_fixable})")
    print(f"  HARD CAP  {ceil:5.1f}%  — {tot_human} criteria are human-gated. "
          f"No amount of\n            engineering moves them. They need sessions, "
          f"reviewers, or a decision.")

    lv = linter_violations()
    if lv:
        v, u = lv
        print(f"\n  check-design.py independently finds {v} live violation(s) and "
              f"{u} unresolved")
        print( "  pair(s) in the shipped build. Note these are defects in code that "
               "the box")
        print( "  state does not reflect — two design.md boxes were checked while "
               "false.")
        print( "  Treat the baseline above as an UPPER bound on conformance, not a "
               "measurement.")

    if gate1_open:
        print("\n" + "-" * 74)
        print(f"  CAP RULE IN FORCE — Gate 1 has {gate1_open} open criteria.")
        print( "  Gate 3 polish is capped until the problem is validated. A high build")
        print( "  score on an unvalidated problem is an expensive false positive, and")
        print( "  the cheapest available action is not on the work list below — it is")
        print( "  Gate 1's human instrument.")
        print("-" * 74)

    if worklist:
        print(f"\nWORK LIST — {len(worklist)} items closable without users, "
              f"ranked S then M then L")
        order = {"S": 0, "M": 1, "L": 2}
        worklist.sort(key=lambda r: (order[r[2]], r[0]))
        each = 100 / tot_all
        for gate, cid, eff, body in worklist:
            print(f"  [{eff}] G{gate} {cid:8s} +{each:.1f}%  {body}")

    print(f"\nEach criterion is worth {100/tot_all:.1f}% of the index. "
          f"That is the honest\nresolution of this instrument — it cannot tell you "
          f"that one is more\nimportant than another, because the criteria carry no "
          f"weights. If you want\nweights, they are a judgement call and they belong "
          f"in the gate files, not here.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
