---
id: I-01
gate: 2
status: DESIGNED — never run. Zero participants.
settles: ux.md G1-09 · vision.md G2-10 · design.md G3-16, G3-17 · OPEN.md R-01, R-02, H-01
requires: H-01 (Beth's decision to commission)
runs_after: I-02 — and I-02 may make this unnecessary. Read I-02 first.
benchmark: PMC9810434 Study 2 (n=54) — this instrument is built to be comparable, not merely new
---

# I-01 — Reaction test

## The question, stated so it can fail

Does a **hand-drawn doodle** generated from a person's **own** journal entry avoid the semantic miss (#13a) and the affective miss (#13b) that PMC9810434 measured for photorealistic images generated from a fiction-writing task?

## Why it must be the person's own entry

PMC9810434's participants wrote a **fiction task**. Its 70.37% irrelevance figure is therefore a weaker test than this concept needs: being told a picture doesn't match a story you invented is not the same as being told it doesn't match your own Tuesday. **This is the one material methodological difference from the benchmark**, and it makes the result harder, not easier. Anyone reading a favourable outcome should know that.

## Method

| element | specification |
|---|---|
| Design | within-participants, three stimulus styles: **hand-drawn doodle · photorealistic · abstract non-figurative** |
| Input | the participant's **own** entry, written or spoken in-session |
| Generation | **live.** Not pre-drawn. See "Why the current prototype cannot run this" |
| n | **54 minimum**, matching the benchmark so the figures are directly comparable |
| Mode | moderated, 1:1, ~45 min |
| Coding | #13b affective register coded from the participant's own unprompted description, two coders independent, disagreements recorded not averaged |
| Analysis | **pre-registered.** Style as within-subject factor. No subgroup analysis that was not declared in advance |

## Measures, each mapped to its benchmark figure

| id | measure | benchmark to beat |
|---|---|---|
| SC-001 | #13a — relevance of the image to the participant's own narrative | **70.37%** said irrelevant |
| SC-002 | #13b — proportion whose unprompted description uses negative language | **70.97%** used negative language |
| — | proportion rated suitable for the task | **26.63%** |
| — | **discard rate per style** — a behavioural measure, not an opinion | no benchmark; this is the better measure and it is new |
| — | avoidance behaviour (looking away, closing, minimising) | observed qualitatively in the benchmark |

The discard rate is the measure to trust most. It is a choice, not a rating, and this concept already ships a one-tap discard for other reasons (UXI-03), so it is free to instrument.

## Thresholds and kill criteria — declared before any data exists

| result | consequence |
|---|---|
| **#13a and #13b both improve materially** | Gate 2 upgrades from PARTIAL. Proceed to Tier 2 |
| **#13b improves, #13a does not** | **RE-SCOPE OR KILL.** A pleasanter failure is not a success. A doodle that feels fine while still misrepresenting what the person said is a worse product, not a better one — it fails more pleasantly |
| #13a improves, #13b does not | style problem. Keep the mechanism, redesign the output |
| **neither improves** | **KILL.** The core mechanism does not work |

**Predicted most likely outcome: row 2 — re-scope or kill.** Recorded before the test so it cannot be reread as a partial win afterwards. This prediction is the single most important line in this file.

## Why the current prototype cannot run this

The Tier 1 build serves **pre-drawn** doodles with no model call. A pre-drawn doodle cannot semantically miss a specific entry, because it was never derived from one. **#13a is structurally unmeasurable on the current artifact** — not merely unmeasured. Reporting a favourable number from it would be measuring the wrong thing and calling it evidence.

So I-01 has a build dependency: live generation behind the interface EG-3 already says to keep seamed. That is real cost, and it is why I-02 goes first.

## Cost

Stated in effort, not currency — I have no recruitment rates for this population and will not invent them.

- 54 moderated sessions at ~45 min, plus scheduling and no-show margin
- live generation wired into a build (see above)
- two coders on #13b, independently, across 54 transcripts
- pre-registration written and locked before the first session

**This is the expensive instrument.** I-02 costs a screener and a form. That asymmetry is the whole argument for running I-02 first.

## What this instrument cannot answer

- Retention. Reaction is not retention, and no measure here touches it. R-06 stays open.
- Whether anyone wanted the product (that is I-02).
- Anything at Tier 3 scale — n=54 moderated is a direction, not a launch signal.

## Ethics and data handling

Participants disclose real emotional content, so: explicit consent naming the specific processing, right to stop at any point without giving a reason, no retention of entry text beyond coding, and **no crisis detection is attempted** — a distressed participant is routed to a person, not a feature. Entry text and transcripts are consented for this analysis only and never become seed data, persona quotes, or marketing copy. `purpose_tag: gate-2-reaction-only`.

Art. 9 applies to the generation step in-session. **H-02 (consent copy reviewed by someone qualified) must be resolved before this instrument runs**, not alongside it.
