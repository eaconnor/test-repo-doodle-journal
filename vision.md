---
scope: product
product: "Doodle Journal (test concept)"
gate: 2
brief: briefs/doodle-journal.brief.md
eval_loop: built-in — see "Acceptance Criteria" below
confidence_regime: PROCEED-FLAGGED
---

# Vision — Doodle Journal (Test Concept)

## Direction

A person should be able to put down how their day went without the blank page winning. If we render that entry as an image, the image serves the person's own recollection — it is not the product's party trick, and it is never the only record of what they said.

## What This Is Not

- **Not a product bet.** `[R]` The one primary study on the nearest analogous mechanism found majority-negative reception (70.37% irrelevant, 70.97% negative language — brief ledger #9-#10). Building this as a funded direction is not supported by the evidence that exists.
- **Not a therapeutic tool.** The concept borrows a premise from art therapy — that images reach what words don't — without inheriting that field's clinical validation. No "processes your day," no "heals," no mood diagnosis. Constitutional, not stylistic.
- **Not a validation exercise.** The Tier 1 build tests one named unknown. Shipping it answers nothing about whether the concept works for real people.

## The Gate 2 call, stated plainly

**PARTIAL / CONDITIONAL.** Defensible as a narrowly-scoped research probe into a single open question — whether a hand-drawn *doodle* style avoids the "grotesque / unsettling" reaction that more literal generated imagery produced (brief ledger #13, the one unknown the evidence has not already foreclosed). Not defensible as "we are building a doodle journal."

The condition is the whole thing: if the framing drifts from *testing a named unknown* to *validating a concept*, Gate 2 fails retroactively. That drift is the most likely way this goes wrong, and it happens in a stakeholder readout, not in the code.

## Acceptance Criteria — Gate 2: Are we making the right thing?

- [x] Scope is logged as a research probe testing one named unknown, not a product bet — Decision Log below
- [x] The distinction between "testing a named unknown" and "validating the concept" is explicit in the brief and in this file
- [ ] The prototype's own on-screen framing carries that distinction plus the StoryWriter numbers — not checkable until the build exists
- [x] No clinical, therapeutic, or diagnostic claim appears in any artifact — verified across brief, `ux.md`, this file
- [x] GDPR Article 9 exposure is named as a live design obligation, not deferred — brief FR-006, `ux.md` Atomic Insights
- [ ] Gate 2 is not upgraded from PARTIAL until a doodle-style reaction test has actually been run — no such test exists; Beth's call to commission

## Decision Log

| Date | Decision | Why |
|---|---|---|
| 2026-09-11 | Build at Tier 1 / Concept fidelity as a research probe only; explicitly not a product bet | Brief Gate 2 verdict PARTIAL/CONDITIONAL. `[A]`+`[?]` = **58.6%** of tagged claims (29 rows), grep-verified after Critic Pass 1's #13 split — nearly 2× the 30% threshold. *(Was 57.1%/28 rows pre-split; superseded, not deleted)* |
| 2026-09-11 | Tier 1 doodles are pre-drawn `[TEST DATA]`, **not** live inference — and SC-001/SC-002 are therefore deferred to Tier 2 | Critic Pass 1 FAIL #1: the brief permitted mocked doodles while requiring measurement of "their own generated doodle." Resolved by deciding, so the build cannot appear to answer a question it structurally cannot answer |
| 2026-09-11 | Falsifiability table added to the brief — what moves Gate 2 in either direction | Critic Pass 1 MISSING: without it the probe could run indefinitely without producing a decision. The predicted outcome ("prettier but still irrelevant") is written down in advance as a re-scope-or-kill, not a partial win |
| 2026-09-11 | The doodle is shown **alongside** the original text/transcript, never instead of it | Direct mitigation for ledger #9-#11: if the image misses, the person still has what they actually said |
| 2026-09-11 | An immediate discard/regenerate path is a P3 requirement, not a polish item | At a 70%+ irrelevance rate on the nearest analogue, easy dismissal is the safe default, not a nice-to-have |
| 2026-09-11 | Doodle generation requires an explicit per-entry action — never automatic or ambient | Ambient inference on intimate disclosure is both a GDPR Art. 9 problem (ledger #23-#24) and a trust problem |
| 2026-09-11 | No clinical or therapeutic framing anywhere, including internal stakeholder copy | Constitution. The art-therapy literature was never validated on this population or this artifact |
| 2026-09-11 | `idea_score` left UNSCORED in the brief rather than estimated | The scoring rubric was not located; a plausible-looking number was not invented to fill the field |
| 2026-09-11 | `[TEST DATA]` seed entries only — fictional, visibly flagged | Real journal content is special-category data; the publicity test forbids it in a prototype |

**No override has been logged.** Gates 1 and 2 both carry open boxes for real reasons; the only routes past them are satisfied criteria or an override Beth writes here herself.
