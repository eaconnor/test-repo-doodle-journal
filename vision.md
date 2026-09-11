---
scope: product
gate: 2
derived_from: "Intent Specs/doodle-journal.md §1 (desired outcome), §4 (scope and non-goals), §10 (escalation triggers), §14 (decision log)"
role: "DERIVED MECHANICAL CHECKLIST — holds no reasoning. Judgment lives in the intent spec."
eval_loop: "./check-gates.sh (box state) + ./check-trace.sh (trace validity)"
---

# vision.md — Gate 2 (derived checklist)

**Do not write reasoning here.** The direction, the scope boundaries, the anti-success signals and the decision log are all canonical in `Intent Specs/doodle-journal.md`. This file only holds criteria a script can settle.

**The decision log moved.** It now lives at intent spec **§14**, as a single canonical record. It is not duplicated here — a decision recorded in two places drifts, and today's session shipped a stale statistic for exactly that reason.

## Acceptance Criteria — Gate 2: Are we making the right thing?

- [x] G2-01 — Scope is recorded as a Tier 1 concept probe, not a product bet · traces_to: §14 row 1 · verified_by: `grep` for the decision row in the intent spec
- [x] G2-02 — Anti-success signals are stated, including the predicted-most-likely outcome · traces_to: §1 anti-success · verified_by: §1 contains the "fails more pleasantly" re-scope-or-kill condition
- [x] G2-03 — A falsifiability table exists giving a Gate 2 consequence for each test result · traces_to: §1, brief falsifiability table · verified_by: 4-row outcome table present in the brief
- [x] G2-04 — Unknown #13 is split into #13a and #13b everywhere it appears · traces_to: §1 anti-success · verified_by: `grep -c '#13a'` = `grep -c '#13b'` = 8 in the built artifact, both non-zero
- [x] G2-05 — No clinical, therapeutic, or diagnostic claim appears in any artifact · traces_to: §4 non-goals, §10 · verified_by: `grep -iE 'therap|diagnos|heal|wellness'` returns only the disclaimer sentence
- [x] G2-06 — GDPR Art. 9 exposure is named as a live obligation, with the inference step identified as the regulated act · traces_to: §8 · verified_by: `grep` for the Art. 9 statement in the intent spec and brief FR-006
- [x] G2-07 — Out-of-scope items are enumerated, including crisis detection as explicitly not attempted · traces_to: §4 out of scope · verified_by: §4 lists it
- [x] G2-08 — Escalation triggers are written down and include "anyone describes this as validated" · traces_to: §10 · verified_by: §10 contains that trigger
- [x] G2-09 — Every decision in the log carries a date and a reason · traces_to: §14 · verified_by: 10 of 10 rows have both columns populated
- [ ] G2-10 — Gate 2 upgraded from PARTIAL: a reaction test has been run and its result mapped through the falsifiability table · traces_to: `OPEN.md` H-01 · verified_by: H-01 resolved and a result row added to §14 — **currently open, owner Beth**
- [ ] G2-11 — The Art. 9 consent copy has been reviewed by someone qualified · traces_to: §8, `OPEN.md` H-02 · verified_by: H-02 resolved with a named reviewer — **currently open, owner Beth to route**

**2 of 11 open.** Both blocked on human decisions, tracked as `HUMAN` rows. `./check-blocked.sh` exits 2 while they stand.
