#!/usr/bin/env python3
"""
check-tier.py — who has to sign to proceed past each open gate criterion.

THE PRINCIPLE: the signature level matches WHO BEARS THE CONSEQUENCE, not who has
seniority. Escalating by rank is what makes sign-off processes hated and routed
around. Escalating by who gets hurt is defensible to the person being asked, and
it produces a tier assignment nobody has to argue about.

    consequence lands on...          ->  tier  ->  who signs
    the person doing the work            T0        themselves (self-serve)
    the team or the roadmap              T1        one peer, not the author
    a USER                               T2        the accountable owner
    the COMPANY (legal / regulatory)     T3        accountable owner + risk function
    unbounded or irreversible            T4        nobody. This is an incident.

NON-BLOCKING IS ABOUT PEOPLE, NOT ACTIONS. A pending T2 signature never idles an
engineer — they move to other work. What waits is the specific risky action, or
shipping it to that destination. The person is never blocked; the risk is.

THE ANTI-BUREAUCRACY RULES, because this is where such systems die:

  1. DEFAULT IS T0. Most work is self-serve. If tiering pushes routine work to
     T2, the tiering is wrong and this script says so (see the integrity check).
  2. TIER IS A PROPERTY OF THE CRITERION, derived mechanically below — never
     negotiated per instance. Otherwise every waiver opens with an argument about
     what tier it is, and that argument costs more than the gate saves.
  3. NOTHING REVERSIBLE GOES ABOVE T2. If you can undo it, it does not need a
     company-level signature.
  4. ONE SIGNATURE PER TIER, TWO AT MOST (T3). A third signature adds delay and
     zero information.
  5. SILENCE IS NOT CONSENT. An unsigned T2 is not auto-approved by time passing.
  6. ESCALATION IS BY CONSEQUENCE, NOT BY DISAGREEMENT. You do not escalate
     because someone said no. A "no" at T2 means the FLOOR item gets fixed.

Exit codes:
    0   tiering reported
    17  integrity check failed — too much routine work requires a senior signature
"""

import re
import os
import sys

def conf(key, default=""):
    """Read a value from project.conf. The only project-specific input."""
    try:
        for line in open("project.conf", encoding="utf-8"):
            m = re.match(rf'\s*{key}\s*=\s*"?([^"#\n]*)"?', line)
            if m:
                return m.group(1).strip()
    except FileNotFoundError:
        pass
    return default


ACCOUNTABLE_OWNER = conf("ACCOUNTABLE_OWNER", "UNSET — set it in project.conf")
RISK_FUNCTION = conf("RISK_FUNCTION", "UNSET — set it in project.conf")

GATES = [(conf("GATE_1", "ux.md"), 1), (conf("GATE_2", "vision.md"), 2),
         (conf("GATE_3", "design.md"), 3)]
CRIT = re.compile(r"^- \[([ x])\] (\S+) — (.*)$")

# --- tier derivation. Order matters: first match wins, highest consequence first.
RULES = [
    # NOTE on "retention": the word is ambiguous and it mis-tiered G1-24 on the
    # first run. DATA retention (how long an entry is kept) is regulatory -> T3.
    # USER retention (do people keep journalling) is a product question -> T1.
    # Requiring an adjacent data word avoids reading one as the other.
    ("T3", re.compile(
        r"art\.? ?9|special[- ]category|lawful|consent copy|gdpr|legal|"
        r"(retention|deletion)\s*(/|or)?\s*(deletion)?\s*sla|"
        r"retention.{0,20}(data|entry|doodle|inference)|"
        r"(data|entry|doodle|inference).{0,20}retention", re.I),
     "consequence lands on the company — regulatory exposure"),

    ("T2", re.compile(
        r"wcag|contrast|keyboard|focus|aria|alt|text alternative|target size|"
        r"colour alone|color alone|reduced.motion|accessib|UXI-1[1234]|"
        r"data loss|participant|real person|segment has primary evidence|"
        # CLR-01/CLR-02 are contrast rules that never say "contrast" in the
        # criterion body. Missing them put two AA failures in the self-serve
        # bucket on the first run — the exact error that makes a tiering unsafe.
        r"CLR-0[12]|--ochre|--cadmium|--vermillion|colour pair|color pair", re.I),
     "consequence lands on a user — exclusion, harm, or an unvalidated audience"),

    ("T1", re.compile(
        r"traces_to nothing|off.roadmap|hardcod|composition|eight states|"
        r"response.time|budget|instrument|test run|reviewed|read|"
        # commissioning or running a study spends money and moves the roadmap
        r"commission|has been run|measured|retention mechanism", re.I),
     "consequence lands on the team or the roadmap"),
]

T_SIGNER = {
    "T0": "the person doing the work (self-serve)",
    "T1": "one peer who is not the author",
    "T2": f"the accountable owner — {ACCOUNTABLE_OWNER}. NOT self-signable by the builder",
    "T3": f"{ACCOUNTABLE_OWNER} AND {RISK_FUNCTION} — two named signatures",
    "T4": "nobody. No signature exists for a never event; it is an incident.",
}


def tier_of(body):
    for t, rx, why in RULES:
        if rx.search(body):
            return t, why
    return "T0", "consequence lands on the person doing the work"


def parse(path):
    out = []
    if not os.path.isfile(path):
        return out
    inb = False
    for line in open(path, encoding="utf-8"):
        if re.match(r"^#{2}\s+(\d+\.\s+)?Acceptance Criteria", line):
            inb = True
            continue
        if inb and line.startswith("## "):
            inb = False
        if not inb:
            continue
        m = CRIT.match(line.rstrip())
        if m:
            out.append({"checked": m.group(1) == "x", "id": m.group(2),
                        "body": m.group(3)})
    return out


def main():
    buckets = {t: [] for t in ("T0", "T1", "T2", "T3", "T4")}
    total_open = 0

    for path, gate in GATES:
        for c in parse(path):
            if c["checked"]:
                continue
            total_open += 1
            t, why = tier_of(c["body"])
            buckets[t].append((gate, c["id"], why, c["body"][:88]))

    # A MISSING gate file must fail loudly. Summing parsed criteria across all
    # three gates hid this: with GATE_1 typo'd, gates 2 and 3 still parsed, the
    # total was non-zero, and the script reported a clean tiering with a whole
    # gate silently absent. Same false-green class as the two fixed above —
    # found by testing the guard instead of trusting it.
    missing = [p for p, _ in GATES if not os.path.isfile(p)]
    if missing:
        print("BROKEN — gate file(s) not found: " + ", ".join(missing))
        print("Check GATE_1/GATE_2/GATE_3 in project.conf. A missing gate file is")
        print("a failure, not a gate with nothing in it: tiering the two that do")
        print("exist would report a confident answer with a third of the criteria")
        print("silently absent.")
        return 5

    n_parsed = sum(len(parse(p)) for p, _ in GATES)
    if n_parsed == 0:
        print("BROKEN — zero parsable acceptance criteria across all three gates.")
        print("Expected: '- [x] G1-01 — <claim> · verified_by: <how>' under a")
        print("'## Acceptance Criteria' heading. Reporting '0 open criteria, all")
        print("clear' when nothing could be read is a false green, so this fails")
        print("instead. Check GATE_1/2/3 in project.conf point at the right files.")
        return 5

    print("=" * 74)
    print("TIERED SIGNATURE AUTHORITY — who signs to proceed past each open gate")
    print("=" * 74)
    print(f"\n{total_open} open criteria across three gates.\n")

    for t in ("T3", "T2", "T1", "T0"):
        rows = buckets[t]
        print("-" * 74)
        print(f"{t}  ({len(rows)} criteria)   signs: {T_SIGNER[t]}")
        if not rows:
            print("     none")
            continue
        for gate, cid, why, body in rows:
            print(f"     G{gate} {cid:8s} {body}")
        print(f"     why: {rows[0][2]}")

    print("-" * 74)
    print(f"T4  signs: {T_SIGNER['T4']}")
    print("     Derived from ./check-never.sh, not from the gate files. Run it.")

    # ---- integrity check. Same shape as check-value.sh rule 3: the script has to
    # be able to tell you the design is wrong, or it is decoration.
    senior = len(buckets["T2"]) + len(buckets["T3"])
    pct = 100 * senior / total_open if total_open else 0

    print("\n" + "=" * 74)
    print("INTEGRITY CHECK — is the tiering itself wrong?")
    print("=" * 74)
    print(f"\n  {senior} of {total_open} open criteria ({pct:.0f}%) need a senior signature.")
    # Rule 1 ("default is T0") must be tested over ALL criteria, not just open
    # ones. Open criteria are survivorship: the self-serve work is the work that
    # already got done, so T0 looks tiny in the open list by construction.
    allb = {t: 0 for t in ("T0", "T1", "T2", "T3")}
    n_all = 0
    for path, gate in GATES:
        for c in parse(path):
            t, _ = tier_of(c["body"])
            allb[t] += 1
            n_all += 1
    t0pct = 100 * allb["T0"] / n_all if n_all else 0
    print(f"  Across ALL {n_all} criteria: T0 {allb['T0']} · T1 {allb['T1']} · "
          f"T2 {allb['T2']} · T3 {allb['T3']}  ({t0pct:.0f}% self-serve)")
    print("  Rule 1 is tested on this line, not the one above. The open list is")
    print("  survivorship — self-serve work is the work that already got done.")
    print()
    if pct > 60:
        print("  FAIL — most open work needs the accountable owner. That is not a")
        print("  governance model, it is a bottleneck with a diagram. Either the")
        print("  tier rules over-assign, or this project genuinely has a")
        print("  user-safety problem across the board. Check which before")
        print("  accepting it: if the T2 list is mostly accessibility, the honest")
        print("  reading is the second one — and the fix is to FIX them, not to")
        print("  re-tier them.")
        print()
        print("  Do not resolve a failed integrity check by lowering tiers.")
        return 17
    if pct < 10:
        print("  WARN — almost everything is self-serve. Check that FLOOR items")
        print("  are being detected; a tiering that never escalates is the same as")
        print("  no tiering.")
    else:
        print("  PASS — the distribution is plausible: most work self-serve, a")
        print("  minority escalated on user or company consequence.")

    print("\n  Non-blocking reminder: a pending signature never idles a person.")
    print("  They move to other work. What waits is the risky action, or shipping")
    print("  it to that destination — never the human.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
