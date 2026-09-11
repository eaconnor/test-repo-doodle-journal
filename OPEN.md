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
| H-01 | HUMAN | Commission the moderated reaction test measuring #13a and #13b separately? **The "everything waits on this" framing in this row is wrong, and writing the protocol is what exposed it.** H-01 commissions `instruments/I-01`, the expensive moderated study (54 sessions, live generation, two coders). `instruments/I-02` — a message test — costs a screener and a form, needs no decision from this row, and **can retire I-01 entirely**: if control message M-4 ("your words, kept — a drawing, optional") wins, the doodle is not the value proposition and a reaction test measures a feature nobody chose the product for. The reverse is not true. Recommendation: run I-02, then decide this row with its result in hand. Still Beth's decision. | Beth | ux.md G1-09, vision.md G2-10, design.md G3-16/G3-17/G3-24 | Beth commissions it or declines it in writing |
| H-02 | HUMAN | Does the FR-006 consent copy get legal / usability review, and who does it? Current copy is a UI pattern, not a lawful Art. 9 disclosure. | Beth to route | vision.md G2-11, design.md G3-22 | A named reviewer signs off, or the requirement is descoped for Tier 1 |
| H-03 | HUMAN | What is the retention / deletion SLA for an entry, its doodle, and derived inference data? No source in this corpus sets one. | Beth + Eng | design.md G3-23, spec.md FR-010 `[NEEDS CLARIFICATION]`, User Story 3 AS-2 | A timing is specified and sourced |
| H-04 | HUMAN | Is this register a per-repo file or a Band Protocol-level artifact shared across projects? Raised 2026-09-11; the whole point was "everyone shares it." **Narrower duplication question now resolved** (see Resolved H-10): this file is the machine-readable index, intent spec §13 is the canonical pointer to it, no duplicated rows. What remains is purely the per-repo vs Band-level scope call. | Beth | whether this pattern propagates | Beth picks scope |
| H-05 | HUMAN | Fix `test-repo-nav-update`'s shape — hand-rolled `spec.md`, stub `plan.md`/`tasks.md` — now that it is public and read as a template? Previously "note, don't fix." | Beth | nav-update's credibility as an example | Beth says fix or leave |
| H-06 | HUMAN | Revoke the three read invitations now that both repos are public, or keep them for future write access? | Beth | nothing; housekeeping | Beth decides |
| H-07 | HUMAN | The `idea_score` rubric was never located. Supply it, or drop the field from brief frontmatter? | Beth | brief frontmatter completeness | Rubric provided or field removed |
| H-08 | HUMAN | Font loading resolved in favour of the design system over self-containment. Confirm that precedence holds generally, or is it case-by-case? (This row previously listed design.md G3-14 in its `blocks` column and tripped `check-never.sh` NE-1. G3-14 is settled by execution — the fonts either load or they do not — regardless of what the general policy turns out to be. The `blocks` column must mean "cannot be settled until you decide", not "is relevant to"; conflating those two produces false never events, and a false never event is how the whole mechanism gets switched off.) | Beth | all future single-file prototypes | Beth states the general rule |
| R-01 | RESEARCH | Does a hand-drawn doodle style avoid the *unsettling* reaction (#13b)? Untested anywhere reachable. | unassigned | vision.md G2-10; Gate 2 staying PARTIAL | A reaction test reports on #13b |
| R-02 | RESEARCH | Can *any* generated image match what a person actually said (#13a, 70.37% said no)? The more damaging half; style changes do not plausibly fix it. | unassigned | Gate 2; the concept's viability | A reaction test reports on #13a |
| R-03 | RESEARCH | Writing-vs-drawing comparison — now identified as **Chan, K.M. & Horneffer, K. (2006), "Emotional expression and psychological symptoms: A comparison of writing and drawing," The Arts in Psychotherapy 33(1), 26–36, DOI 10.1016/j.aip.2005.06.001**. Citation verified via PASCAL-FRANCIS and OpenAlex records (both fetched). Unpaywall confirms `is_oa: false`, no OA location anywhere; publisher, ResearchGate and proxy routes all 403/CAPTCHA; Semantic Scholar reports the abstract elided by the publisher. **Still never read — not even the abstract.** A retrieval pass produced plausible design/findings detail for this paper; it was rejected because it came from a search-engine synthesis that also produced a demonstrably wrong paraphrase on two other calls. Institutional access is the only route. | unassigned | ux.md G1-10, brief ledger #21 | The paper itself is read |
| R-04 | RESEARCH | Review/skim cost — do people revisit voice entries at all, and is a doodle any more skimmable? No research located. | unassigned | brief ledger #17, #18 | A source is found or a study run |
| R-05 | RESEARCH | Do users hold stronger privacy expectations for "a journal" than for apps generally? Design hypothesis, unsourced. | unassigned | brief ledger #26, #27 | A source is found or a study run |
| R-06 | RESEARCH | Does lower-friction non-text capture actually improve retention? Extrapolated from abandonment categories, never tested head-to-head. | unassigned | brief ledger #4, #5 | A head-to-head comparison exists |
| R-07 | RESEARCH | Transcription error in emotionally loaded journaling — no source addresses it. | unassigned | spec.md Edge Cases | A source is found |
| R-08 | RESEARCH | **RESOLVED — and the claim was backwards. See Resolved R-08 below.** | — | — | — |
| R-09 | RESEARCH | Is `ux.md` ds:2.1's "opening" reading right, or is the market shaped that way for a reason? Every vendor sells the generated image as a finished good; nobody sells a fallible doodle. That is either the gap or the answer. Covers the untested positioning (ds:1.2) and the four-message test (ds:1.3), including whether control M-4 — "the entry is the product, the doodle is optional" — wins and makes the doodle decoration. | unassigned | ux.md G1-21, G1-23 | The message test runs and reports per message, M-4 included |
| R-10 | RESEARCH | Personas P-1/P-2/P-3 and segments S-1..S-3 are `[TEST DATA]` fiction. No persona, journey, or message has been in front of a real person. | unassigned | ux.md G1-22 | Participant count > 0 |
| R-11 | RESEARCH | The design-system conformance audit has never been run against the prototype: the eight states (ds:3), composition rules C-01..C-12, the §4.1 response budgets, the SHD-05 pressed state, and CLR-01/CLR-02 colour-text conformance. Not defects found — checks never performed. | unassigned | design.md G3-27, G3-28, G3-29, G3-34, G3-35, G3-36 | An audit is run and each criterion settled true or false |
| R-12 | RESEARCH | The accessibility audit has never been run: contrast against the measured ds:1.1 table, keyboard operation, doodle text alternatives, colour-alone state, target size, focus visibility, reduced motion. `--ochre` at 2.10:1 and `--cadmium` at 1.49:1 on light ground mean a single misuse is an outright AA failure. | unassigned | design.md G3-18, G3-19, G3-20, G3-21, G3-30, G3-31, G3-32 | An audit is run and each criterion settled true or false |
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
| R-08 | RESEARCH | **The secondhand claim was contradicted by the primary source.** Located and read in full: Pizarro, J. (2004), "The Efficacy of Art and Writing Therapy: Increasing Positive Mental Health Outcomes and Participant Retention After Exposure to Traumatic Experience," *Art Therapy* 21(1), 5–12 — full text at `files.eric.ed.gov/fulltext/EJ683379.pdf`, independently re-verified against the PDF. **N=45, three conditions: write-stress, art-stress, art-control (drawing a still life). There was no combined art+writing condition** — the paper names a combined design as *future* work: "Future research could combine writing and art therapy to determine whether a mixed design would both improve health and maximize participant retention." On symptoms, **writing beat art**: "Participants in the writing condition, but not the art therapy condition, showed a decrease in social dysfunction." On the direct stress measure (GMPS) no condition differed significantly. **What art won was enjoyment and completion**: "participants who completed artwork reported more enjoyment, were more likely to c[omplete]…". Consequence: the register's old claim is `[CS: FABRICATION RISK — contradicted by primary source]` and must not be cited. A **new `[R]` claim** replaces it, and it is a better fit for this concept than the one it replaces: *the measured benefit of the drawing is retention and enjoyment, not a better outcome* — which lands directly on SRC-002's 70%-within-100-days abandonment problem. `ux.md` ds:1.2 and ds:4.4 need updating to the finding rather than the misreading. | 2026-09-11 |
| H-00 | HUMAN | Repo visibility — both repos made public; "nothing sensitive here" (Beth). MIT licence and spec-kit attribution added first. | 2026-09-11 |
| H-09 | HUMAN | Council pass — skipped by explicit decision. Gate 3 criteria therefore rest on one critic pass, recorded as a limitation not a dropped step. | 2026-09-11 |
| H-10 | HUMAN | OPEN.md vs intent spec §13 duplication — resolved: this file is the single machine-readable register (`check-blocked.sh` reads it); §13 is a canonical pointer holding no duplicate rows. One place to edit, one place to read. | 2026-09-11 |
| H-11 | HUMAN | ux.md / vision.md / design.md made DERIVED mechanical checklists; intent spec §5 (UXI-01..14), §1, §4, §7, §11, §12 canonical. Every criterion carries `traces_to:`; `check-trace.sh` validates both directions. **Partly superseded the same day by H-12.** | 2026-09-11 |
| H-12 | HUMAN | Scope of canonicity — **reversed part of H-11 on Beth's call.** `ux.md` is canonical for the research corpus, positioning, audience and research plan; `design.md` is canonical for the Itten design system, interaction canon and accessibility standard; the intent spec stays canonical for *this feature's* intent; `vision.md` stays a thin derived checklist. Reason: a design system and a research corpus are not derived from a feature spec — they outlive it and apply to the next prototype. Each enlarged file keeps its `## 9. Acceptance Criteria` block so the scripts still settle the gates. Apex 2.0 was considered as the design system and dropped: the real tokens were not in hand, inventing them would have been fabrication, and a genuine Apex spec is internal IP that does not belong in a public repo. Itten was substituted — real, locked, already implemented. | 2026-09-11 |
