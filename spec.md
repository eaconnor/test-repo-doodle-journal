# Feature Specification: Doodle Journal — Voice/Text Entry Rendered as a Doodle

**Feature Branch**: `001-doodle-journal`

**Created**: 2026-09-11

**Status**: Draft — Tier 1 / Concept. Gates 1 and 2 PARTIAL, Gate 3 assessed in `design.md`.

**Build artifact**: `prototypes/doodle-journal/doodle-journal.html` — self-contained, pre-drawn `[TEST DATA]` doodles, no model call. Reviewed in `prototypes/doodle-journal/critic-pass-1.md` (pre-build) and `critic-pass-2.md` (post-build).

**Input**: User description: "a journal app that translates voice or text entries into doodles"

> **Shape note.** This file follows `.specify/templates/spec-template.md` deliberately — prioritized user stories, `FR-###` requirements, `SC-###` success criteria. The sibling test repo (`test-repo-nav-update/spec.md`) was hand-written with a `What / Why / Open Questions` shape that does not match the template, which is why `/speckit-*` commands had nothing they recognized to work with. Evidence and tagging live in `briefs/doodle-journal.brief.md`; this file is the spec-kit-shaped view of the same content, not a second source of truth.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Low-friction entry capture (Priority: P1)

A person wants to log a reflection on their day without the blank-page friction that drives journaling-app abandonment. They choose voice or text for the same entry, whichever is faster in the moment.

**Why this priority**: The only part of the concept resting on a sourced problem — `[D]` 70% median discontinuation within 100 days across 18 studies / 525,824 participants (PMC11694054), with "blank page / low personalization" and "burdensome data entry" among the named causes. Independently valuable with zero dependency on whether the doodle mechanism works.

**Independent Test**: Have a user create one entry, choosing voice or text, and complete it within a self-set time budget, with no image-generation step required to call the story done.

**Acceptance Scenarios**:

1. **Given** an empty entry screen, **When** the user chooses "speak" and talks for under a minute, **Then** the entry is saved as a transcript the user can review and edit before it is final.
2. **Given** an empty entry screen, **When** the user chooses "type" instead, **Then** the same entry structure is used — voice and text are equivalent inputs to one entry type, not two products.

---

### User Story 2 - Doodle rendered from an entry (Priority: P2)

A person completes an entry and is shown a small hand-drawn-feeling image generated from it, as a companion to re-reading their own text.

**Why this priority**: This is the concept's disputed core claim, not its sourced foundation. `[R]` The nearest primary analogue (StoryWriter, PMC9810434, n=54) found 70.37% judged generated images irrelevant to their own narrative and 70.97% described them in negative language. Framed as a hypothesis test of unknown #13b, not as a validated feature.

**Independent Test**: Generate a doodle for a completed entry and ask the user, in their own words, whether the image feels relevant to what they said — StoryWriter's own Study 2 question, applied to this style. **Requires live generation; not exercisable by the Tier 1 build**, which uses pre-drawn doodles.

**Acceptance Scenarios**:

1. **Given** a saved entry, **When** the user requests a doodle, **Then** the doodle is shown alongside — never in place of — the original text/transcript.
2. **Given** a generated doodle, **When** the user is asked to describe it in their own words, **Then** that description is captured verbatim as the measurement instrument, not as a cosmetic feedback box.

---

### User Story 3 - Discard or regenerate a doodle that misses (Priority: P3)

A person judges their doodle irrelevant, wrong, or unsettling and needs to dismiss it immediately without losing or distorting the underlying entry.

**Why this priority**: Direct mitigation for the majority-negative finding. At a 70%+ irrelevance rate on the nearest analogue, shipping *without* an easy discard path is the higher-risk default, not the safe one.

**Independent Test**: Generate a doodle, discard it, and confirm the original entry text/transcript is unchanged.

**Acceptance Scenarios**:

1. **Given** a doodle the user finds inaccurate or unsettling, **When** they select "discard," **Then** the doodle is removed immediately, with no confirmation friction that re-exposes the image.
2. **Given** a discarded doodle, **When** the user checks the entry later, **Then** the original text is intact and no residual inferred-emotion data remains attached. **MUST NOT be marked passing at Tier 1** — depends on FR-010's open clarification.

### Edge Cases

- The generated doodle is judged "creepy" or irrelevant (StoryWriter benchmark) → covered by User Story 3; dismissal must never require the user to explain why first.
- Voice capture mistranscribes a moment of emotional disclosure → `[?]` no source addresses transcription error in an emotionally loaded journaling context; named as a gap, not designed for.
- A user deletes an entry → does deletion propagate to the doodle and any derived inference data? Required by GDPR consent-withdrawal principles; not yet designed (FR-010).
- An entry contains crisis or self-harm language → **out of scope** for a non-clinical Tier 1 concept per the constitution. The prototype must not attempt to detect or respond, and the demo script must say so plainly rather than imply the system handles it.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow entry creation via typed text OR recorded voice, for the same entry, at the user's choice.
- **FR-002**: System MUST render at most one doodle per entry, only after an explicit per-entry user action — never automatic or ambient generation.
- **FR-003**: System MUST display the original text/transcript alongside any doodle; the doodle MUST NOT be the sole record of an entry.
- **FR-004**: System MUST let a user discard or regenerate a doodle without altering the underlying entry.
- **FR-005**: System MUST NOT auto-share or transmit a doodle outside the user's own view without a separate explicit share action.
- **FR-006**: System MUST capture explicit, specific consent for the inference step, distinct from general terms-of-service acceptance (GDPR Art. 9 — the inference is the regulated act, not just the storage).
- **FR-007**: System MUST visibly label its fidelity ("Tier 1 · Concept") on every screen a stakeholder can see.
- **FR-008**: System MUST NOT present clinical, therapeutic, diagnostic, or "processes trauma" language anywhere in copy.
- **FR-009**: All seed/demo entries and doodles MUST be fictional and visibly tagged `[TEST DATA]`.
- **FR-010**: System MUST allow deletion of an entry, its doodle, and derived inference data as one action, with propagation timing [NEEDS CLARIFICATION: retention/deletion SLA not sourced anywhere in this corpus].
- **FR-011**: System MUST state on every screen that no reaction data has been collected and no user testing has been run — a claim distinct from, and verified separately from, the FR-007 fidelity label.

### Key Entities

- **JournalEntry**: raw voice recording or typed text, plus transcript if voice; timestamp; owner.
- **Doodle**: image linked 1:1 to a JournalEntry; style parameters; discard/regenerate state; never produced without an explicit per-entry action.
- **ConsentRecord**: the explicit special-category consent required before generation; withdrawable.
- **DemoSeedEntry**: fictional entry+doodle pairs for stakeholder demos; always `[TEST DATA]`.

## Success Criteria *(mandatory)*

- **SC-001** — *deferred to Tier 2*: proportion of participants describing their own **live-generated** doodle as "irrelevant to what I said," addressing unknown #13a. No target set; StoryWriter's 70.37% is the only benchmark and it is unfavorable. Not satisfiable by a pre-drawn build.
- **SC-002** — *deferred to Tier 2*: proportion using negative/unsettling language, addressing unknown #13b, against StoryWriter's 70.97%. Same constraint.
- **SC-003**: Time from opening the app to a completed entry (voice or text) is measured — the independent test for User Story 1, and the only success criterion the Tier 1 build can exercise. No target set; no source establishes what "fast enough" means here.
- **SC-004**: Zero instances of clinical/therapeutic language in shipped copy, verified by manual review before any stakeholder demo.
- **SC-005**: 100% of demo/seed data confirmed fictional and `[TEST DATA]`-tagged before any stakeholder sees it.
- **SC-006**: Every screen states that no reaction data has been collected, verified separately from the fidelity label.

## Assumptions

- Tier 1 audience is internal design/product staff — not the general public, and not a clinical population the art-therapy literature was validated against.
- **Tier 1 doodles are pre-drawn `[TEST DATA]`, not live inference.** Decided, not left open. The consequence is that SC-001/SC-002 cannot be measured against this build.
- Beth, not this spec, decides whether the Tier 2 reaction test is commissioned, on whom, and when.
- `[A]`+`[?]` = 58.6% of tagged claims (17 of 29, grep-verified). Nearly 2× the 30% threshold — this spec is not ready to build past a concept-level probe, and says so rather than implying readiness by existing.
