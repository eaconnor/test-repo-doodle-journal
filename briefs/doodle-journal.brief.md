---
feature: "Doodle Journal — Voice/Text-to-Sketch Reflective Journaling (Tier 1 Concept)"
gate: 10
owner: "Beth"
problem_statement: "Journaling-app abandonment is real and documented in general [D] (see ledger #1-#3), but the specific problem this concept proposes to solve — that translating a reflective entry into a generated image increases engagement, retention, or emotional processing — is not sourced. The one primary study that tested the closest analogous mechanism found a majority-negative user reaction to it [R] (ledger #9-#11)."
okr_objective: "[?] Unknown — no OKR exists for this concept. Task framing names this explicitly as a pipeline-wiring test, not a funded initiative. Not invented here."
okr_key_result: "[?] Unknown — same reason as above."
counter_metric: "[?] Unknown — same reason as above. If this proceeds past Tier 1, a candidate counter-metric worth naming later: rate of users who report the doodle as inaccurate/unsettling, benchmarked against StoryWriter's 70.97% (ledger #10) — not a target, a tripwire."
idea_score: "UNSCORED — the scoring rubric text was not located in this session's available files (referenced by the spec agent's operating instructions but not present in any file read for this brief). A number was not invented to fill the gap. If the rubric exists elsewhere, re-run scoring against it explicitly rather than backfilling this field."
evidence_sources:
  - "test-repo-doodle-journal/scout/00-index.md"
  - "test-repo-doodle-journal/scout/01-expressive-non-textual-journaling.md"
  - "test-repo-doodle-journal/scout/02-voice-capture-journaling-input.md"
  - "test-repo-doodle-journal/scout/03-text-to-image-reflective-surface.md (load-bearing)"
  - "test-repo-doodle-journal/scout/04-art-therapy-visual-journaling-precedent.md"
  - "test-repo-doodle-journal/scout/05-failure-modes-ethics-privacy.md"
  - "PMC11694054 — journaling/mental-health app abandonment scoping review (fetched directly)"
  - "PMC9810434 — StoryWriter, AI text-to-image + expressive writing (fetched directly)"
  - "Frattaroli 2006 meta-analysis PDF (fetched directly)"
build_artifact: "prototypes/doodle-journal/doodle-journal.html — Tier 1 / Concept, self-contained, pre-drawn [TEST DATA] doodles, no model call"
review_record:
  - "prototypes/doodle-journal/critic-pass-1.md — pre-build, returned DON'T BUILD YET with 2 FAILs"
  - "prototypes/doodle-journal/critic-pass-2.md — post-build re-score + delta table"
council_pass: "NOT RUN — Beth's explicit decision, 2026-09-11. Gate 3 acceptance criteria therefore derive from critic pass 2 alone, not from critic + council. Recorded as a decision, not a dropped step."
confidence_regime: PROCEED-FLAGGED
proceed_because: "Beth asked for this as a Tier-1/lo-fi internal wiring-test concept, not a funded product decision, and this is evidence uncertainty (do we have enough research on the mechanism) not decision uncertainty (Beth has already decided to run a concept-level pipeline test) — producing an honest brief that carries the negative primary finding forward is worth more than withholding, on condition no [A]/[?] claim is upgraded to validated along the way."
machine_behavior: "build Tier 1 / Concept fidelity only, surface [R]/[D]/[A]/[?] tags visibly inside the prototype's own framing (not just this brief), carry the StoryWriter 70.37%/70.97% finding into the build rather than softening it, no clinical/therapeutic language anywhere per constitution, all seed data [TEST DATA] and fictional, do not claim the doodle mechanism improves retention/emotional processing since that claim is [A]/[?] not [R]/[D], Gate 2 stays PARTIAL until a doodle-style-specific reaction test exists"
status: "draft"
---

## Confidence regime — stated plainly

This is **evidence uncertainty**, not decision uncertainty. Beth has already decided to run a Tier‑1/lo‑fi concept test through the pipeline — that decision isn't in question here. What's in question is whether the *mechanism* (voice/text entry → generated doodle) has any sourced basis, and it mostly doesn't: 57.1% of the claims tagged in this brief are `[A]` or `[?]` (raw counts and math below). `PROCEED-FLAGGED` means: build the lo-fi concept, but the artifact must carry its own uncertainty on its face, not launder it. If this were instead a question of "should we build a real product here," the honest regime would be `BLOCKED` — it isn't that question, yet.

---

## Gate 1 — Do we understand the customer problem? Real and sourced, or assumed?

**Split answer, stated exactly:**

The *general* problem — people abandon journaling and mental-health apps — is real and sourced. `[D]` A scoping review of 18 studies and 525,824 participants (PMC11694054, fetched directly) found median discontinuation of 70% within the first 100 days, with mental-health apps specifically at 89–92% abandonment (ledger #1, #2). Two of the six named abandonment-reason categories are directly relevant: "poor UX / blank page / low personalization" and "burdensome data entry" (ledger #3).

The *specific* problem this concept proposes to solve — that rendering an entry as an image reduces that friction, or does something writing alone doesn't — is **not sourced**. `[A]` The bridge from "friction causes abandonment" to "a doodle reduces friction" is a scout-named extrapolation, not a finding (ledger #4). `[?]` No study was located that directly compares non-verbal/visual capture retention against text-journal retention head-to-head (ledger #5).

Worse than merely unsourced: the closest primary analogue **argues against the mechanism**. `[R]` StoryWriter (PMC9810434, fetched and read in full) is the only primary research located that measured how people react to AI-generated images of their own emotional disclosure. In its qualitative study (n=54): **70.37% (38/54) judged the generated images irrelevant to their own narrative**, **70.97% described the images in negative language ("scary," "unsettling," "creepy")**, and only 26.63% of images were rated suitable for the task (ledger #9, #10, #11). Its own mechanism finding is that the modest emotion-regulation benefit it did measure (anger d=−0.40, sadness d=−0.63) is attributable to the *writing process*, not the images (ledger #12).

`[?]` No source tests this concept's actual proposed mechanism — voice/text journal entry, specifically, rendered as a *doodle* specifically. StoryWriter is a fiction-writing task; mood-slider apps (MoodGallery, Life Note) are check-in inputs, not free reflection. Both are adjacent, not equivalent (ledger #14). Whether a hand-drawn/doodle *style* specifically avoids the "grotesque/unsettling" reaction found with StoryWriter's imagery is untested anywhere this scout could reach (ledger #13).

**Gate 1 verdict: problem is partially real (the abandonment problem), but the concept's specific solution mechanism has no supporting evidence and one directly-contradicting primary finding. This gate does not pass on the solution as framed.**

### Gate 1 — Acceptance Criteria

- [ ] The general journaling-app abandonment problem (friction, blank page, low personalization) is sourced to PMC11694054 in every downstream artifact that cites it — confirmed here, must not be dropped downstream.
- [ ] The claim "translating an entry into a doodle solves the abandonment problem" is never presented as sourced in any downstream artifact (critic, build, handoff) — it remains `[A]`/`[?]`, not upgraded.
- [ ] The StoryWriter finding (70.37% irrelevant / 70.97% negative language, ledger #9-#10) is carried into the build and critic stages with its exact numbers, not summarized into a softer paraphrase.
- [ ] No internal user interview, survey, Condens session, or Jira/Confluence ticket exists for this concept — confirmed absent by design (scout index, line 2), not merely unsearched — this stays true before any build proceeds.
- [ ] A named test plan for the doodle-style-specific unknown (ledger #13) exists before Gate 2 is ever upgraded from PARTIAL to PASS.
- [ ] The `[A]`+`[?]` percentage of tagged claims (57.1%, see math below) is recalculated, not re-estimated, if any new source is added to this brief.

---

## Gate 2 — Are we making the right thing?

No OKR or mission linkage exists for this concept — it is named in the task itself as a pipeline-wiring test, not a funded initiative. That's stated in frontmatter as `[?]` rather than backfilled.

Setting mission-linkage aside, the narrower Gate 2 question is: given the evidence, is building *this* — even at Tier 1 — the right next move? The honest answer is conditional, not clean:

- Building a full "voice/text-to-doodle journal" as a product bet is **not supported**. The one primary study on the nearest analogous mechanism found majority-negative reception (ledger #9-#11), and the "friction reduction" argument that would justify the mechanism is itself unevidenced (ledger #4, #5).
- Building a **narrow, low-fidelity concept probe** — specifically to test the one named unknown that isn't yet foreclosed by evidence, whether a *doodle* style (simple, hand-drawn-feeling, non-photorealistic) avoids the "grotesque/unsettling" reaction that a more literal/generic AI-art style produced (ledger #13) — is a defensible research move. It is not the same claim as "this concept works," and the brief must not let it become that claim by drift.

`[A]` A second reason for caution not yet named above: `[A]` "it's just generating a picture" undersells the regulatory exposure. `[R]` Mood/emotional-state data inferred from a journal entry qualifies as special-category data under GDPR Article 9 — a settled regulatory interpretation (ledger #23) — and the *inference step*, not just storage, is what's regulated (ledger #24). Any version of this that ships past Tier 1 concept demo carries that obligation whether or not the team frames it as "just an image."

**Gate 2 verdict: PARTIAL / CONDITIONAL. Not yet "the right thing" as a product; defensible as a narrowly-scoped research probe if and only if the brief, build, and any stakeholder-facing framing keep the distinction between "testing a named unknown" and "validating a concept" explicit and don't collapse it.**

---

## Gate 3 — Are we making the thing right? Tested how, by whom?

`[?]` No test plan exists yet. No user testing — internal or external — has been run on this specific concept. This is the honest state, not a placeholder to be filled with invented numbers.

If Beth decides to test the Tier 1 build, the one directly relevant methodological precedent in the corpus is StoryWriter's own Study 2 design: a small qualitative reaction survey after use, asking participants to describe the generated image in their own words and rate its relevance/suitability (ledger #9-#11's source method). That's named here as the *closest available precedent*, not as a decision already made — Beth chooses the actual method, participants, and n.

**Definition of done for Tier 1, stated plainly:** a working lo-fi prototype that (a) discloses its own fidelity on its face, (b) never claims the doodle mechanism is validated, (c) carries the StoryWriter finding into its own framing rather than hiding it in an appendix, and (d) uses only fictional `[TEST DATA]`. Nothing about "does this work for real people" is answered by shipping the Tier 1 build — that's a separate, not-yet-run test.

---

## Failure modes

1. **The core mechanism repeats StoryWriter's finding at doodle scale.** Users generate a doodle from a real (or in Tier 1, fictional-but-realistic-feeling) entry, judge it irrelevant or unsettling, and disengage *faster* than they would have with plain text — the opposite of the friction-reduction theory this concept implicitly relies on (ledger #9-#11).
2. **Evidence laundering.** The team conflates the sourced abandonment problem (`[D]`, real) with the unsourced solution mechanism (`[A]`/`[?]`, unproven) and reports internally that "the concept is validated by research" — it isn't; the research that exists on the closest analogue is unfavorable.
3. **Regulatory exposure via inference, not storage.** A team member assumes "we're not storing sensitive data, we're just generating a picture" and skips explicit Article 9 consent design, because the image-generation step itself (not the text storage) is the regulated inference (ledger #23-#24). Compounded risk: the nearest adjacent app category (mental-health apps) has a recent, dated breach precedent — 10 apps, 14.7M installs, 1,575 flaws (ledger #25) — showing this category is a live target, not a theoretical one.
4. **Clinical-claims drift.** Marketing or internal stakeholder language slides from "informed by the idea that images access something words don't" (a disciplinary premise of art therapy, `[A]`, ledger #22) into "helps you process your day" — a claim this literature was never validated against for this population, and one the constitution explicitly prohibits.

---

## What's missing (unknowns, named not filled)

- `[?]` Whether a hand-drawn/doodle style specifically avoids the negative reaction StoryWriter measured with its (non-doodle-style) generated imagery — the single most decision-relevant unknown, and untested.
- `[?]` Whether people can review/skim a doodle any more efficiently than they could skim or re-listen to a voice entry — no research located on review/skim cost of either input mode (ledger #17, #18).
- `[?]` The directly-titled comparative study — "Emotional expression and psychological symptoms: a comparison of writing and drawing" — exists and is the single most relevant comparative study found, and it is paywalled (HTTP 403). It was never read (ledger #21).
- `[?]` Whether "journal" as an app category carries stronger implicit privacy expectations than apps generally — no study located; this is a design hypothesis, not a finding (ledger #26-#27).
- `[A]` No internal user research exists at all for this concept — no interviews, no Condens sessions, no Jira/Confluence tickets — confirmed absent by design, not a search failure (ledger #28). Everything in Gate 1 rests on secondary web research, much of it vendor marketing the scout explicitly flagged as weak.
- No rubric was available in this session to compute `idea_score` — named in frontmatter rather than backfilled with an invented number.

---

## Critic Pass 1 — resolutions

Critic Pass 1 (`prototypes/doodle-journal/critic-pass-1.md`) returned **"don't build yet"** with two FAILs. Both are resolved here. Recorded rather than silently patched, because the corrections change what this brief claims.

### FAIL #1 — mocked vs. live doodle contradiction → **resolved by deciding**

The Assumptions section permitted mocked/pre-generated doodles at Tier 1 while SC-001/SC-002 required measuring reaction to a participant's "own generated doodle." Those cannot both hold. **Decision: Tier 1 is pre-drawn `[TEST DATA]`, and SC-001/SC-002 are therefore deferred to Tier 2.** The Tier 1 build can exercise exactly one success criterion (SC-003, entry-completion time) plus the two compliance checks (SC-004, SC-005) and the new SC-006. Anything the Tier 1 build appears to say about whether the doodle *lands* with a person is not evidence.

### FAIL #2 — the "one named unknown" was really two → **split, with falsifiability stated**

StoryWriter's finding is two numbers with two different plausible causes, and the original ledger #13 collapsed them into one hypothesis that only addressed the smaller-sounding half. Split:

- **#13a — semantic match.** 70.37% judged the image **irrelevant to their own narrative** (ledger #9). Cause is plausibly content/comprehension: the machine did not render what they actually said. **A doodle style change does not plausibly fix this.** This is the more damaging half and the probe as originally scoped could not speak to it at all.
- **#13b — affective register.** 70.97% described the image in **negative language** — "scary," "unsettling," "creepy" (ledger #10). Cause is plausibly style/aesthetic: uncanny, over-literal rendering. **A hand-drawn doodle style is a plausible mitigation for this half**, and this is the only half the concept's core bet actually addresses.

**Falsifiability condition — what moves Gate 2 off PARTIAL, in either direction:**

| Tier 2 reaction-test result | Gate 2 consequence |
|---|---|
| #13b improves materially **and** #13a improves | PARTIAL → candidate PASS; the mechanism has a real basis and the concept is worth scoping as a product question |
| #13b improves but **#13a does not** (still "irrelevant to what I said") | **Gate 2 stays PARTIAL and the concept is re-scoped or killed.** A prettier image that still misrepresents the person is a worse product, not a better one — it fails more pleasantly. This is the most likely outcome on current evidence and the brief predicts it |
| Neither improves | Gate 2 → **FAIL.** Concept killed; the mechanism does not survive its own nearest analogue |
| #13a improves but #13b does not | Ambiguous; the doodle-style bet specifically is disconfirmed even though the concept's problem-framing survives. Re-run with a different visual register before any Gate 2 call |

Without this table the probe could have run indefinitely without producing a decision — which was the substance of Critic Pass 1's MISSING finding.

### RISK items also resolved
- **FR-011** added — the "no reaction data collected" disclosure, distinct from the fidelity label.
- **SC-003** tethered explicitly to User Story 1's independent test; it was previously freestanding.
- **SC-006** added — verification that the no-testing disclosure is present.
- **FR-010** now states outright that User Story 3's Acceptance Scenario 2 must not be marked passing while its clarification is open.

### Not resolved, deliberately
The **single-source** flag stands: all counter-evidence rests on one qualitative study, n=54. That is not fixable by editing; it is fixable only by finding or running more research, including the paywalled writing-vs-drawing comparison (ledger #21) that this pipeline could not read.

---

## Requirements

### User Scenarios & Testing

#### User Story 1 — Low-friction entry capture (Priority: P1)

A person wants to log a reflection on their day without the blank-page friction that drives journaling-app abandonment (ledger #1-#3, `[D]`). They choose voice or text for the same entry, whichever is faster for them in the moment.

**Why this priority**: This is the only part of the concept resting on a sourced problem. It is independently valuable — and independently testable — with zero dependency on whether the doodle mechanism works at all.

**Independent Test**: Can be fully tested by having a user create one entry, choosing voice or text, and completing it in under a self-set time budget, with no image-generation step required to call the story done.

**Acceptance Scenarios**:
1. **Given** an empty entry screen, **When** the user chooses "speak" and talks for under a minute, **Then** the entry is saved as a transcript the user can review and edit before it's final.
2. **Given** an empty entry screen, **When** the user chooses "type" instead, **Then** the same entry structure is used — voice and text are equivalent inputs to one entry type, not two products.

---

#### User Story 2 — Doodle rendered from an entry (Priority: P2)

A person completes an entry and is shown a small hand-drawn-feeling image generated from it, as an alternative or companion to re-reading their own text.

**Why this priority**: This is the concept's disputed core claim, not its sourced foundation. It is framed here explicitly as a hypothesis test of the one named unknown (ledger #13) — whether doodle style avoids the reaction StoryWriter measured (ledger #9-#11) — not as a validated feature.

**Independent Test**: Can be tested by generating a doodle for a completed entry and directly asking the user, in their own words, whether the image feels relevant to what they said — the same question StoryWriter's Study 2 asked, applied to this style specifically.

**Acceptance Scenarios**:
1. **Given** a saved entry, **When** the user requests a doodle, **Then** the doodle is shown alongside — never in place of — the original text/transcript (per Gate 2's mitigation for ledger #9-#11).
2. **Given** a generated doodle, **When** the user is asked to describe it in their own words, **Then** that description is captured verbatim for the reaction-test record — this is the measurement instrument, not a cosmetic feedback box.

---

#### User Story 3 — Discard or regenerate a doodle that misses (Priority: P3)

A person judges their generated doodle irrelevant, wrong, or unsettling and needs an immediate way to dismiss it without losing or distorting their underlying entry.

**Why this priority**: Direct mitigation for the majority-negative finding (70.37% irrelevant, 70.97% negative language — ledger #9-#10). Given that finding, shipping *without* an easy discard/regenerate path is the higher-risk default, not the safe one.

**Independent Test**: Can be tested by generating a doodle, discarding it, and confirming the original entry (text/transcript) is unchanged and undamaged by the discard action.

**Acceptance Scenarios**:
1. **Given** a doodle the user finds inaccurate or unsettling, **When** they select "discard," **Then** the doodle is removed from view immediately, with no confirmation friction re-exposing the image.
2. **Given** a discarded doodle, **When** the user checks their entry later, **Then** the original text/transcript is intact and the discard action left no residual inferred-emotion data attached to the entry (ledger #23-#24).

---

### Edge Cases

- What happens when the generated doodle is judged "creepy" or irrelevant by the user, per the StoryWriter benchmark (ledger #9-#10)? → Covered by User Story 3; must not require the user to explain why before dismissing.
- What happens when voice capture mishears or mistranscribes a moment of emotional disclosure? → `[?]` No source addresses transcription-error handling in an emotionally loaded journaling context specifically; named as a gap.
- What happens when a user deletes an entry — does deletion propagate to the generated doodle and any inferred-emotion data used to produce it? → Required by GDPR consent/withdrawal principles (ledger #23), not yet designed.
- What happens if a user's entry contains crisis or self-harm language? → Out of scope for a non-clinical Tier 1 concept per the constitution's clinical-claims prohibition; the prototype must not attempt to detect or respond to this, and the demo script must say so plainly rather than imply the system handles it.

### Functional Requirements

*(Requirements below are design decisions, not evidentiary claims — they are not `[R]/[D]/[A]/[?]`-tagged individually; the rationale sentences that justify them, above, carry the tags.)*

- **FR-001**: System MUST allow entry creation via typed text OR recorded voice, for the same entry, at the user's choice.
- **FR-002**: System MUST render at most one doodle per entry, generated only after an explicit per-entry user action — never automatic or ambient generation.
- **FR-003**: System MUST display the original text/transcript alongside any generated doodle; the doodle MUST NOT be the sole record of an entry.
- **FR-004**: System MUST let a user discard or request regeneration of a doodle without altering or deleting the underlying entry.
- **FR-005**: System MUST NOT auto-share, auto-post, or otherwise transmit a generated doodle outside the user's own view without a separate, explicit share action.
- **FR-006**: System MUST capture explicit, specific consent for the inference step used to generate a doodle, distinct from general app terms-of-service acceptance (GDPR Art. 9, ledger #23-#24).
- **FR-007**: System MUST visibly label its fidelity ("Tier 1 / Concept") on every screen a stakeholder can see.
- **FR-008**: System MUST NOT present clinical, therapeutic, diagnostic, or "processes trauma" language anywhere in copy, per constitution.
- **FR-009**: All seed/demo entries and doodles MUST be fictional and visibly tagged `[TEST DATA]`.
- **FR-010**: System MUST allow deletion of an entry, its doodle, and any derived inference data as one action, with propagation timing [NEEDS CLARIFICATION: retention/deletion SLA not sourced anywhere in this corpus]. **User Story 3's Acceptance Scenario 2 depends on this open clarification** and therefore MUST NOT be marked passing at Tier 1 — there is no defined target to test against (Critic Pass 1, RISK).
- **FR-011** *(added per Critic Pass 1)*: System MUST state, on every screen, that **no reaction data has been collected and no user testing has been run** — separately and visibly distinct from the FR-007 fidelity label. A fidelity badge says "this is a concept"; it does not say "nobody has tested this." The drift `vision.md` predicts — probe becoming "we tested this" in a stakeholder readout — is operationalized against here rather than merely warned about.

### Key Entities

- **JournalEntry**: raw voice recording or typed text, plus transcript if voice; timestamp; owner.
- **Doodle**: generated image linked 1:1 to a JournalEntry; style parameters; discard/regenerate state; never generated without an explicit per-entry action (FR-002).
- **ConsentRecord**: captures the explicit special-category consent required before doodle generation (FR-006); withdrawable.
- **DemoSeedEntry**: fictional entry+doodle pairs used for any stakeholder demo; always carries the `[TEST DATA]` flag (FR-009).

### Success Criteria

- **SC-001** — **DEFERRED TO TIER 2, not measurable against this build.** `[?]` Of internal participants completing a moderated reaction test, the proportion who describe their own **live-generated** doodle as "irrelevant to what I said" is measured and reported, addressing unknown **#13a** (semantic match). No target threshold is set — the only comparable benchmark found is StoryWriter's 70.37% (ledger #9), and it is unfavorable, not a bar to clear casually. Requires live generation per the Assumptions section; the Tier 1 build uses pre-drawn doodles and therefore **cannot satisfy or fail this criterion**. Claiming otherwise off a mocked build is the defect Critic Pass 1 caught.
- **SC-002** — **DEFERRED TO TIER 2, same reason.** `[?]` Of the same participants, the proportion using negative/unsettling language to describe the doodle is measured and reported against StoryWriter's 70.97% benchmark (ledger #10), addressing unknown **#13b** (style/affect). No target set for the same reason.
- **SC-003**: `[?]` Time from opening the app to a completed entry (voice or text) is measured — this is the independent test for **User Story 1 (P1)**, whose acceptance is "completes an entry within a self-set time budget," and it is the only success criterion the Tier 1 build can actually exercise. No target set — no source in this corpus establishes what "fast enough" means for this population or this task.
- **SC-006** *(added per Critic Pass 1)*: Every screen states that **no reaction data has been collected** — a claim distinct from the Tier 1 fidelity label, and verified separately from it, because "this is a concept" and "nobody has tested this" are two different disclosures and only the first was previously required.
- **SC-004**: Zero instances of clinical/therapeutic language in shipped copy, verified by manual review before any stakeholder demo. (Direct compliance check against the constitution — not evidence-dependent, not tagged.)
- **SC-005**: 100% of demo/seed data confirmed fictional and tagged `[TEST DATA]` before any stakeholder sees the prototype. (Same — compliance check, not an empirical claim.)

### Assumptions

- Audience for the Tier 1 build is internal design/product staff, per the task's framing — not general public, and not a clinical population art-therapy literature was validated against (File 04).
- **Tier 1 doodles are pre-drawn `[TEST DATA]`, not live inference. Decided, not left open** (resolves Critic Pass 1 FAIL #1). No production-grade image-generation model or hosting decision is implied by this brief. The direct consequence, stated rather than buried: **the reaction test SC-001/SC-002 describe cannot be run against this build**, because a pre-drawn doodle is not "their own generated doodle." Those two criteria are deferred to a Tier 2 build with live generation. The demo script must say plainly that the doodles are pre-drawn (per scout File 05's explicit instruction).
- Beth, not this brief, decides whether the Gate 3 test plan gets run, on whom, and when.

---

## Tag ledger — every ratified claim, counted once

| # | Tag | Claim | Locator |
|---|-----|-------|---------|
| 1 | [D] | Journaling/mental-health app abandonment: 18 studies, 525,824 participants, median 70% discontinuation within 100 days | PMC11694054 |
| 2 | [D] | Mental health apps abandonment range 89–92% within window | PMC11694054 |
| 3 | [D] | Abandonment reason categories include "blank page/low personalization" and "burdensome data entry" | PMC11694054 |
| 4 | [A] | "Lower-friction, non-text capture increases retention" — extrapolation, not tested | scout/01, line 41 |
| 5 | [?] | No study compares non-verbal/visual capture retention vs. text-journal retention head-to-head | scout/01, line 46 |
| 6 | [R] | Frattaroli (2006) meta-analysis, 146 RCTs, r=.075 (small, significant) expressive-writing effect | Frattaroli 2006 PDF |
| 7 | [R] | Smyth (1998) fixed-effects meta-analysis, 13 studies, d=0.47 — methodological tension w/ #6, [WOBBLY] | scout/01, line 14-20 |
| 8 | [R] | StoryWriter Study 1: 388 participants; images reduced anger d=−0.40, sadness d=−0.63; no effect on anxiety/stress | PMC9810434 |
| 9 | [R] | StoryWriter Study 2: 70.37% (38/54) found generated images irrelevant to their own narrative | PMC9810434 |
| 10 | [R] | StoryWriter Study 2: 70.97% described images in negative language ("scary," "unsettling," "creepy") | PMC9810434 |
| 11 | [R] | StoryWriter Study 2: only 26.63% of images rated suitable for the writing task | PMC9810434 |
| 12 | [R] | StoryWriter mechanism finding: benefit attributable to writing process itself, not images | PMC9810434 |
| 13a | [?] | **Semantic match** — whether any generated image can render what the person actually said; 70.37% said irrelevant. Doodle style does not plausibly fix this half | scout/03, line 35 + Critic Pass 1 |
| 13b | [?] | **Affective register** — whether a hand-drawn doodle style avoids the grotesque/unsettling reaction; untested. The only half the concept's bet addresses | scout/03, line 35 + Critic Pass 1 |
| 14 | [?] | No source tests the specific mechanism (voice/text entry → doodle); analogues are adjacent, not equivalent | scout/03, line 34 |
| 15 | [A] | "Portrait of Emotion" (CogSci 2023) — people prefer emotion-images over event-images — abstract-only, unverified | arXiv 2304.13324 |
| 16 | [A] | "Speaking is 3-4x faster than typing" — vendor-marketing claim, no primary source verified | scout/02, line 4 |
| 17 | [?] | No research on review/skim cost of voice journal entries | scout/02, line 19 |
| 18 | [?] | No research on self-consciousness speaking aloud in a private-but-recorded journaling context | scout/02, line 20 |
| 19 | [A] | Vocal prosody carries emotion info text cannot — field claim plausible, specific attribution unverified | scout/02, line 9-10 |
| 20 | [?] | Pizarro (2004) combined art+writing > writing alone — secondhand, original not read, no DOI | scout/04, line 16 |
| 21 | [?] | Direct writing-vs-drawing comparison study — most relevant found, blocked HTTP 403, never read | scout/04, line 18-19 |
| 22 | [A] | "Some emotional content is pre-verbal" — disciplinary premise of art therapy, not an empirical finding | scout/04, line 12 |
| 23 | [R] | GDPR: emotional-state data inferred from an entry qualifies as special-category data (Art. 9), settled interpretation | scout/05, line 4 |
| 24 | [A] | "It's just generating a picture" undersells GDPR exposure — inference itself is the regulated act | scout/05, line 7 |
| 25 | [D] | Oversecured/BleepingComputer/TechRepublic: 10 Android mental-health apps, 14.7M installs, 1,575 flaws (Jan 2026) | scout/05, line 11-16 |
| 26 | [?] | No study measures user privacy expectations for "journal" as a category specifically | scout/05, line 24 |
| 27 | [A] | "Journal" category may carry stronger implicit privacy expectations than apps generally — hypothesis, not sourced | scout/05, line 24 |
| 28 | [A] | No internal user research exists for this concept — confirmed absent by design, not unsearched | scout/00-index, line 2, 18 |

### The arithmetic (grep-checkable against the table above, not estimated)

**Recomputed after Critic Pass 1 split ledger #13 into #13a and #13b.** Total rises 28 → 29 and the ratio moves; both re-derived by grep and `python3`, not adjusted by hand.

- Total tagged claims: **29**
- `[R]`: **8** (#6, #7, #8, #9, #10, #11, #12, #23)
- `[D]`: **4** (#1, #2, #3, #25)
- `[A]`: **8** (#4, #15, #16, #19, #22, #24, #27, #28)
- `[?]`: **9** (#5, #13a, #13b, #14, #17, #18, #20, #21, #26)
- `[R]` + `[D]` = 12/29 = **41.4%**
- `[A]` + `[?]` = 17/29 = **58.6%**

*Prior figures, superseded not deleted: 28 claims, 42.9% / 57.1% — correct before the #13 split.*

**58.6% exceeds the 30% threshold.** Per protocol, this brief is named explicitly as not ready to build past a Tier 1 concept-level probe. It should not move to critic as if it were a validated concept — it should move to critic as what it is: a brief that surfaces a real general problem (`[D]`, 4 claims), a disputed core mechanism with one directly unfavorable primary finding (`[R]`, 8 claims, including the load-bearing StoryWriter numbers), and a majority of open or assumed ground (16 of 28 claims) that no amount of build polish resolves.
