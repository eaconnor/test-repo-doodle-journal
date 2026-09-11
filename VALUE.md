# VALUE.md — what research and design actually contributed

A register, not a case study. One row per time research or design **changed the outcome**, with the counterfactual stated and labelled.

Read by `./check-value.sh`, which is why the table format is strict.

## Why this exists

Design's value is normally asserted and unfalsifiable — "we made it more user-centered," "we de-risked it." Nobody can check that, which means nobody has to believe it, which is why the function gets cut first in a squeeze.

This register makes the claim auditable. It has three rules:

1. **The counterfactual is the value.** Not "we did research" — *what would have shipped without it*. A row with no counterfactual records activity, not value.
2. **Every row is `EVIDENCED` or `CLAIMED`.** `EVIDENCED` means the counterfactual is demonstrated by something a third party can check. `CLAIMED` means it is a reasonable inference. Both are legitimate; conflating them is not.
3. **Costs and zero-value rows are mandatory.** A value register with no negative rows is marketing. `check-value.sh` fails if there are none — that check exists to stop this file becoming what it was written to replace.

## The kinds

| kind | meaning |
|---|---|
| `EVIDENCE` | research found something that changed a decision |
| `DECISION` | design made a call that changed the artifact |
| `PREVENTION` | something harmful or wasteful did not happen |
| `CORRECTION` | an error already in the work was caught |
| `COST` | what this consumed, including mistakes made |
| `ZERO` | something we invested in that measurably did not work |

## Rows

| id | kind | what happened | what it changed | counterfactual — what would have shipped | status |
|---|---|---|---|---|---|
| V-01 | EVIDENCE | Scout located and read PMC9810434 in full: 70.37% of participants found AI-generated images of their own writing irrelevant, 70.97% used negative language, and the measured benefit came from the writing rather than the images | The whole concept was reframed from "doodles help you reflect" to "one half of one named unknown." UXI-01, UXI-03 and UXI-09 exist because of it | A brief asserting the mechanism works. All five vendor pages found frame AI mood art as a validated positive feature, and that framing was the only one available before this study was read | EVIDENCED — in a 12-agent test, all six control-arm agents asked for "the evidence this works" led with this finding, citing `scout/` and `SOURCES.md`. The corpus is demonstrably what carries it |
| V-02 | CORRECTION | Critic pass 2 re-scored the build and found 7 FAILs, 5 of them defects I had introduced while hand-patching pass 1's findings | All 7 fixed and re-verified before anything was shared | A prototype claiming "Saved ✓ — verbatim, timestamped" while the JS only toggled a `hidden` attribute; a stale 57.1% statistic; a `readonly` transcript contradicting its own aria-label | EVIDENCED — `prototypes/doodle-journal/critic-pass-2.md` records each with its delta |
| V-03 | PREVENTION | `check-gates.sh` fired during a live `/speckit-plan` run and blocked it | Planning stopped on a red gate instead of proceeding past it | A plan built on Gate 1 criteria that were never satisfied. Before this, the only thing connecting the script to the workflow was one sentence of constitution prose — a norm wearing a mechanism's hat | EVIDENCED — reproducible; the hook is in `.specify/extensions.yml` with `optional: false` |
| V-04 | CORRECTION | `check-trace.sh` found UXI-05 and UXI-07 orphaned on its first run | Two criteria added; both requirements now enforced | Two stated UX intents that nothing verified — the dangerous direction, because a written-down requirement *looks* covered | EVIDENCED — the script exits 4 on a reintroduced orphan; tested against a deliberately broken pointer |
| V-05 | CORRECTION | `check-design.py` found 10 live violations in a build that two critic passes and a 36-criterion gate file had cleared, and falsified two boxes that were **checked**: G3-12 (4 hardcoded `#1a1612` outside `:root`) and G3-20 (claimed "not implemented"; all four doodles do carry `aria-label`) | 7 FLOOR accessibility failures surfaced, including no focus style anywhere on the page | A prototype shipped to a pilot with contrast failures on every warning and destructive control, and no visible focus indicator | EVIDENCED — `python3 scripts/check-design.py`, exit 6 |
| V-06 | CORRECTION | A retrieval pass located Pizarro (2004) and read it in full; I re-verified against the ERIC PDF independently. The register's secondhand claim was **backwards** — no combined art+writing condition was ever run, and writing beat art on symptoms | R-08 reclassified `[CS: FABRICATION RISK — contradicted by primary source]`. A **new `[R]` claim** replaced it: the drawing's measured benefit is enjoyment and completion, not outcome | A brief citing "art + writing beats writing alone" as support for the concept — a claim the primary source contradicts. It had already survived one scout pass and one critic pass | EVIDENCED — `files.eric.ed.gov/fulltext/EJ683379.pdf`, verified twice from source text |
| V-07 | CORRECTION | `check-eng.sh` EG-2 found FR-005, FR-007, FR-008, FR-009 and FR-010 trace to no stated intent and no gate criterion | 5 of 11 requirements flagged off-roadmap | Five requirements built, maintained forever, and defended by nobody — the most expensive kind of scope | EVIDENCED — `./check-eng.sh`, exit 11 on the roadmap gate alone |
| V-08 | EVIDENCE | Scout identified that the **inference step**, not the storage, is the GDPR Art. 9 regulated act — "it's just generating a picture" undersells the exposure | UXI-02 and UXI-10: no generation on load, explicit per-entry consent. `check-risk.py` now blocks `pilot` and `production` | A pilot shipping with a ToS-style checkbox as its lawful basis for special-category processing | CLAIMED — no pilot was attempted, so the harm is averted-in-principle. The hazard itself is `[CS: HIGH]` settled law; the counterfactual is inference |
| V-09 | DECISION | Unknown #13 was split into #13a (semantic miss) and #13b (affective miss), with "#13b improves and #13a does not" declared **re-scope-or-kill** before any data exists | The falsifiability table, and the prediction that row 2 is the most likely outcome | A result where the doodle feels pleasanter but still misrepresents what the person said, read afterwards as a partial win. "Fails more pleasantly" is the specific failure this split makes unavailable | CLAIMED — but unusually strong, because the prediction is timestamped in the repo and cannot be revised after the data |
| V-10 | PREVENTION | Kill criteria and thresholds written before Tier 2 was funded | Tier 2 is scoped as a bounded reaction test with a pre-agreed proceed/re-scope/kill call | An open-ended Tier 2 build, with the decision to continue made after the money was spent and by whoever was most invested | CLAIMED — the largest single item here, and the one that most needs a real Tier 2 to confirm |
| V-11 | ZERO | `ux.md` and `design.md` were written as substantial documents — 866 lines, sourced, structured. A controlled test then ran 12 fresh agents on 6 trap tasks, half with the files present and half with them deleted | **Nothing.** 6 of 6 task pairs tied. Not one of the 12 agents cited either file. One agent holding `design.md` put an emoji in the markup, which SHD-06 forbids; another built a confirmation dialog while holding the section saying discard must never be confirmed | The same outcomes. What actually did the work: the prototype's existing patterns, `CLAUDE.md §11`, the intent spec's §0 agent summary, `SOURCES.md`, and the brief's tag ledger | EVIDENCED — 6 pairs, 12 agents, predictions registered before the run in `PREDICTIONS.md` |
| V-12 | COST | This session produced 866 lines of gate documentation and five scripts, and spent **zero minutes** in contact with a user | — | — | EVIDENCED — participant count is 0 across every instrument. The opportunity cost is real and belongs in this register, not a footnote |
| V-13 | COST | I introduced 5 defects while hand-patching critic pass 1's findings, and ran `build` before the pre-build critic returned, defeating the purpose of a pre-build gate | Both recorded permanently rather than fixed quietly | — | EVIDENCED — `critic-pass-1.md`, `critic-pass-2.md`, and `OPEN.md` A-03 |
| V-14 | COST | Four times this session I attached a `verified_by:` command that did not settle the claim beside it — the claim was true, the stated check was not. Caught each time, but only on re-reading | Each corrected inline with the command that actually settles it | — | EVIDENCED — G3-25, G3-12, G1-14 and the design.md box count, all corrected in place |

## What this register says, read honestly

**The measured value is in the machinery, not the documents.** Every `EVIDENCED` correction row is a *script* or a *critic pass* catching something. The one row for the documents themselves is `ZERO`, and it is the best-evidenced row in the table.

**The largest claimed value — V-10, a cheaper kill decision before Tier 2 — is unconfirmed**, and will stay unconfirmed until a Tier 2 either happens or is declined. It is the number worth quoting to leadership and the one most in need of a real test.

**Research's best row is V-01, and it argued against the project.** The most valuable single thing research did here was find the evidence that the concept probably does not work. That is what the function is for, and it is the hardest kind of value to get credit for.

## Counts

Computed, never asserted — run `./check-value.sh`.
