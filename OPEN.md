# OPEN.md — the register of everything unresolved

One index for every open question, riskiest assumption, and accepted risk in this repo. **If it is unresolved and it matters, it has a row here.** Anything `[?]`-tagged in a brief, any unchecked gate criterion, and any `[NEEDS CLARIFICATION]` marker in `spec.md` must trace to an id below.

Read by `./check-blocked.sh`, which is why the table format is strict.

## Why this file exists

Spec-kit already has the vocabulary for this — `[NEEDS CLARIFICATION]` markers, `/speckit-clarify`, `## Assumptions`, reviewer-owned checklists. What it does not have:

1. **An index.** Markers sit inline across `spec.md` and `plan.md`; nothing aggregates them, so nothing can tell you the total.
2. **A kind distinction.** `[NEEDS CLARIFICATION]` cannot say whether a human must decide, whether evidence is missing, or whether a risk is being knowingly carried. The confidence regime in the constitution draws that line (`BLOCKED` = decision uncertainty, `PROCEED-FLAGGED` = evidence uncertainty); spec-kit has no equivalent.
3. **Enforcement.** `/speckit-clarify` is *expected* to run before `/speckit-plan`. Expected is a norm. This repo already learned what happens to norms that aren't wired into `.specify/extensions.yml`.
4. **Reach.** Clarify only touches `spec.md`. Research unknowns, design decisions, and accepted risks live nowhere.

## The kinds — this is the load-bearing distinction

| kind | meaning | who unblocks it | machine behaviour |
|---|---|---|---|
| `HUMAN` | A **decision** only a person can make. No amount of research resolves it. | named owner | **Stop and ask.** Do not infer, do not pick a sensible default, do not proceed "provisionally." |
| `RESEARCH` | **Evidence** is missing. The question has a findable answer nobody has found. | anyone who can do the work | Proceed flagged. May build, must not claim validation. |
| `ACCEPTED` | A known weakness being **deliberately carried**. | already decided | Proceed. Must stay visible in the artifact; never silently dropped. |

An agent that hits a `HUMAN` row and guesses anyway has made the specific error this file exists to prevent.

## Open rows

| id | kind | question / assumption | owner | blocks | resolves_when |
|---|---|---|---|---|---|
| H-01 | HUMAN | Commission the moderated reaction test (StoryWriter Study 2 method) measuring #13a and #13b separately? Everything downstream waits on this one decision. | Beth | ux.md AC-05, vision.md AC-06, design.md SC-001/SC-002 + reaction-test criterion | Beth commissions it or declines it in writing |
| H-02 | HUMAN | Does the FR-006 consent copy get legal / usability review, and who does it? Current copy is a UI pattern, not a lawful Art. 9 disclosure. | Beth to route | design.md FR-006 | A named reviewer signs off, or the requirement is descoped for Tier 1 |
| H-03 | HUMAN | What is the retention / deletion SLA for an entry, its doodle, and derived inference data? No source in this corpus sets one. | Beth + Eng | design.md FR-010, spec.md FR-010 `[NEEDS CLARIFICATION]`, User Story 3 AS-2 | A timing is specified and sourced |
| H-04 | HUMAN | Is this register a per-repo file or a Band Protocol-level artifact shared across projects? Raised 2026-09-11; the whole point was "everyone shares it." | Beth | whether this pattern propagates | Beth picks scope |
| H-05 | HUMAN | Fix `test-repo-nav-update`'s shape — hand-rolled `spec.md`, stub `plan.md`/`tasks.md` — now that it is public and read as a template? Previously "note, don't fix." | Beth | nav-update's credibility as an example | Beth says fix or leave |
| H-06 | HUMAN | Revoke the three read invitations now that both repos are public, or keep them for future write access? | Beth | nothing; housekeeping | Beth decides |
| H-07 | HUMAN | The `idea_score` rubric was never located. Supply it, or drop the field from brief frontmatter? | Beth | brief frontmatter completeness | Rubric provided or field removed |
| H-08 | HUMAN | Font loading resolved in favour of the design system over self-containment. Confirm that precedence holds generally, or is it case-by-case? | Beth | design.md font criterion; all future single-file prototypes | Beth states the general rule |
| R-01 | RESEARCH | Does a hand-drawn doodle style avoid the *unsettling* reaction (#13b)? Untested anywhere reachable. | unassigned | Gate 2 staying PARTIAL | A reaction test reports on #13b |
| R-02 | RESEARCH | Can *any* generated image match what a person actually said (#13a, 70.37% said no)? The more damaging half; style changes do not plausibly fix it. | unassigned | Gate 2; the concept's viability | A reaction test reports on #13a |
| R-03 | RESEARCH | Writing-vs-drawing comparison study (ScienceDirect S0197455605000699) — the single most relevant study found, HTTP 403, never read. | unassigned | brief ledger #21 | Institutional access obtained and the paper read |
| R-04 | RESEARCH | Review/skim cost — do people revisit voice entries at all, and is a doodle any more skimmable? No research located. | unassigned | brief ledger #17, #18 | A source is found or a study run |
| R-05 | RESEARCH | Do users hold stronger privacy expectations for "a journal" than for apps generally? Design hypothesis, unsourced. | unassigned | brief ledger #26, #27 | A source is found or a study run |
| R-06 | RESEARCH | Does lower-friction non-text capture actually improve retention? Extrapolated from abandonment categories, never tested head-to-head. | unassigned | brief ledger #4, #5 | A head-to-head comparison exists |
| R-07 | RESEARCH | Transcription error in emotionally loaded journaling — no source addresses it. | unassigned | spec.md Edge Cases | A source is found |
| R-08 | RESEARCH | Pizarro (2004), "art + writing beats writing alone" — secondhand, no DOI, original never read. | unassigned | brief ledger #20 | Primary located and read |
| A-01 | ACCEPTED | All counter-evidence rests on **one** qualitative study, n=54. Not fixable by editing — only by more research. | — | nothing; must stay visible | n/a — carried, not resolved |
| A-02 | ACCEPTED | `[THIN DOMAIN]` — the entire corpus is Western, English-language, academic. Non-Western and oral visual-journaling practice is absent. | — | nothing; must stay visible | n/a — named, not filled |
| A-03 | ACCEPTED | `design.md` was authored *from* the finished build by critic pass 2, so Gate 3 grades the artifact on its own terms. Provenance inversion. | — | nothing; recorded as a finding | n/a — fix by authoring Gate 3 before build next time |
| A-04 | ACCEPTED | `[A]`+`[?]` = 58.6% of 29 tagged claims, ~2× the 30% threshold. Built anyway, at Tier 1 only, under `PROCEED-FLAGGED`. | — | nothing; stated in every artifact | n/a — resolved only by R-01…R-08 |

## Counts

Computed, never asserted — run `./check-blocked.sh`.

## Resolved

Rows move here with a date and an outcome. Nothing is deleted; a register you can rewrite silently is not a record.

| id | kind | outcome | date |
|---|---|---|---|
| H-00 | HUMAN | Repo visibility — both repos made public; "nothing sensitive here" (Beth). MIT licence and spec-kit attribution added first. | 2026-09-11 |
| H-09 | HUMAN | Council pass — skipped by explicit decision. Gate 3 criteria therefore rest on one critic pass, recorded as a limitation not a dropped step. | 2026-09-11 |
