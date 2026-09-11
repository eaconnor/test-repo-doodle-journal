---
scope: feature
gate: 1
derived_from: "Intent Specs/doodle-journal.md §2 (context and rationale), §3 (users and affected parties)"
role: "DERIVED MECHANICAL CHECKLIST — holds no reasoning. Judgment lives in the intent spec."
eval_loop: "./check-gates.sh (box state) + ./check-trace.sh (trace validity)"
---

# ux.md — Gate 1 (derived checklist)

**Do not write reasoning here.** This file exists so a script can settle Gate 1. Every criterion below is a claim a `grep`, a count, or a file-state check can decide — nothing requiring interpretation. The *why* for each lives at the `traces_to` target in `Intent Specs/doodle-journal.md`, which is canonical.

If a criterion here cannot be settled without a human forming a judgement, it is in the wrong file and belongs in the intent spec.

## Acceptance Criteria — Gate 1: Do we understand the problem?

- [x] G1-01 — Every evidentiary claim in the brief carries an `[R]`/`[D]`/`[A]`/`[?]` tag · traces_to: §2.3 · verified_by: `grep -cE '^\| [0-9]+[a-z]? \| \[[RDA?]\] \|' briefs/doodle-journal.brief.md` = 29, zero untagged rows
- [x] G1-02 — The `[A]`+`[?]` ratio is computed, never asserted · traces_to: §1 success metrics · verified_by: regex count + `python3` division, 17/29 = 58.6%, recorded with the command used
- [x] G1-03 — SRC-001's three figures (70.37 / 70.97 / 26.63) appear verbatim in the built artifact · traces_to: UXI-04 · verified_by: `grep -c` on `prototypes/doodle-journal/doodle-journal.html`, all three present
- [x] G1-04 — SRC-001 is cited by accession number wherever its figures appear · traces_to: §2.3 · verified_by: `grep -c PMC9810434` ≥ 1
- [x] G1-05 — No internal user research is claimed anywhere · traces_to: §3 · verified_by: absence of interview/Condens/Jira citation in brief, ux, vision, design
- [x] G1-06 — The problem statement distinguishes the sourced problem from the unsourced mechanism · traces_to: §2.1 · verified_by: brief `problem_statement` frontmatter contains both a `[D]` and an unsourced-mechanism clause
- [x] G1-07 — Every `source_material` entry carries an owner and a status · traces_to: frontmatter `source_material` · verified_by: 7 of 7 entries have both fields
- [x] G1-08 — The single-source limitation on counter-evidence is stated in the artifact, not only in the brief · traces_to: §2.3 · verified_by: `grep` for the n=54 statement in `SOURCES.md`
- [ ] G1-09 — A reaction test measuring #13a and #13b separately has been commissioned · traces_to: `OPEN.md` H-01 · verified_by: `OPEN.md` H-01 moved to the Resolved table — **currently open, owner Beth**
- [ ] G1-10 — SRC-004 (writing-vs-drawing comparison, the most relevant study found) has been read · traces_to: `OPEN.md` R-03 · verified_by: `source_material` SRC-004 status changes from `BLOCKED` — **currently HTTP 403, never read**

**2 of 10 open.** Both are blocked on work nobody has done, not on defects. Neither closes by editing a file.
