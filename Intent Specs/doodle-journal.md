---
intent_spec_id: TEST-DJ-001
title: "Doodle Journal — Voice/Text Entry Rendered as a Doodle"
version: "0.1.0"
status: "Draft"
created_at: 2026-09-11T00:00:00Z
updated_at: 2026-09-11T00:00:00Z
target_release: "none — Tier 1 concept probe, not scheduled"

owners:
  product: "TBD — no product owner assigned; this is a pipeline wiring test"
  ux: "Beth Connor"
  engineering: "TBD"
  architecture: "TBD"
  qa: "TBD"
  data_analytics: "N/A"
  security_privacy_compliance: "TBD — GDPR Art. 9 exposure is live and unreviewed, see §8"

agent_context:
  canonical_source: true
  default_context_profile: "planning"
  summary_generated_at: null
  summary_source_version: null
  summary_source_hash: null

source_material:
  - id: SRC-001
    type: "Research"
    title: "StoryWriter — AI text-to-image in expressive writing (PMC9810434)"
    link: "https://pmc.ncbi.nlm.nih.gov/articles/PMC9810434/"
    owner: "scout, 2026-09-11"
    status: "Current — LOAD-BEARING, and it argues against this concept"
  - id: SRC-002
    type: "Research"
    title: "When and Why Adults Abandon Lifestyle Behavior and Mental Health Mobile Apps (PMC11694054)"
    link: "https://pmc.ncbi.nlm.nih.gov/articles/PMC11694054/"
    owner: "scout, 2026-09-11"
    status: "Current — the only sourced problem this concept has"
  - id: SRC-003
    type: "Research"
    title: "Frattaroli (2006) — Experimental Disclosure and Its Moderators: A Meta-Analysis"
    link: "https://bpb-us-e2.wpmucdn.com/faculty.sites.uci.edu/dist/c/602/files/2019/08/Frattaroli-psych-bulletin-2006.pdf"
    owner: "scout, 2026-09-11"
    status: "Current — deflates any 'expressive writing is proven' framing"
  - id: SRC-004
    type: "Research"
    title: "Emotional expression and psychological symptoms: writing vs drawing"
    link: "https://www.sciencedirect.com/science/article/abs/pii/S0197455605000699"
    owner: "unassigned"
    status: "BLOCKED — HTTP 403, paywalled, never read. Most relevant study found."
  - id: SRC-005
    type: "Scout corpus"
    title: "Full 6-file web-only scout dossier"
    link: "scout/00-index.md"
    owner: "scout, 2026-09-11"
    status: "Current"
  - id: SRC-006
    type: "Brief"
    title: "Three-gate brief, 29 tagged claims, falsifiability table"
    link: "briefs/doodle-journal.brief.md"
    owner: "spec, 2026-09-11"
    status: "Current"
  - id: SRC-007
    type: "Review"
    title: "Critic pass 1 (pre-build) and pass 2 (post-build)"
    link: "prototypes/doodle-journal/critic-pass-1.md"
    owner: "critic, 2026-09-11"
    status: "Current"

tags:
  product_area: ["journaling", "generative-image", "test-concept"]
  surfaces: ["web"]
  systems: ["none — mocked, no backend, no model call"]
  risk_level: "high"
  user_impact: "unknown — zero participants"
---

# Intent Spec: Doodle Journal — Voice/Text Entry Rendered as a Doodle

> **Fidelity: Tier 1 · Concept.** No user testing has been run. All seed data is fictional and `[TEST DATA]`. Doodles are pre-drawn, not generated. This document exists to test whether the Band pipeline's output fits the intent-spec shape — the concept itself is a vehicle.

## 0. Agent summary

### Compact build intent

Build a lo-fi web surface where a person records or types how their day went and can explicitly request a hand-drawn doodle rendered from it, shown *alongside* their own words, never instead of them. Ship the evidence against the mechanism on the face of the artifact.

### Most important rules

1. The doodle is **never** the sole record of an entry. Original text always visible.
2. Generation happens **only** on an explicit per-entry action. No ambient, automatic, or on-load generation.
3. Emotional-state inference from a journal entry is **GDPR Art. 9 special-category data**. The inference is the regulated act, not just the storage.
4. **No clinical, therapeutic, or diagnostic language anywhere.** This borders art therapy without inheriting its validation.
5. All seed data fictional and visibly `[TEST DATA]`.
6. The artifact must state that **no reaction data has been collected** — a separate claim from its fidelity label.

### Required agent behavior

Do not claim this concept is validated. Do not soften SRC-001's numbers. Do not upgrade an `[A]` or `[?]` claim to sourced. On any `HUMAN` row in `OPEN.md`, stop and ask the named owner — `./check-blocked.sh` exits 2 for exactly this.

## 1. Desired outcome

### Outcome statement

A person who would otherwise abandon a journal keeps one, because the capture step is cheap and the artifact it produces is worth returning to. **Currently unevidenced** — see §1 anti-success.

### Success looks like

- A person completes an entry without stalling on a blank page.
- They recognise something true about their day in the returned doodle.
- They come back.

### Success metrics

| id | metric | target | status |
|---|---|---|---|
| SC-003 | Time from first keystroke to saved entry | none set — no source establishes "fast enough" | **measurable now**; instrumented in the build, local only, n=1 |
| SC-001 | Proportion describing their own live-generated doodle as "irrelevant to what I said" (#13a) | none set; SRC-001's 70.37% is the only benchmark and it is unfavourable | **DEFERRED to Tier 2** — unmeasurable on pre-drawn doodles |
| SC-002 | Proportion using negative/unsettling language (#13b) | none set; SRC-001 benchmark 70.97% | **DEFERRED to Tier 2** |
| SC-004 | Clinical/therapeutic language instances in shipped copy | zero | passing, manual review |
| SC-005 | Seed data fictional and tagged | 100% | passing |
| SC-006 | Every screen states no reaction data collected | 100% | passing |

### Anti-success / failure signals

The failure mode is **not** low engagement. It is this:

- A person reads the doodle as a claim about their inner state, and it is **wrong about them**. SRC-001: 70.37% judged such images irrelevant to their own narrative; 70.97% described them as "scary," "unsettling," "creepy."
- The doodle is prettier but still misrepresents — **it fails more pleasantly.** Per the brief's falsifiability table this is a re-scope-or-kill, not a partial win, and it is the most likely outcome on current evidence.
- Someone reports internally that "research validates this." SRC-001 is the closest primary evidence and it points the other way.
- The mechanism's benefit turns out to come from the writing, not the image — which is what SRC-001 concluded.

## 2. Context and rationale

### Why this work exists

As a wiring test for the prototyping pipeline against the three-gate framework, using a concept with no internal source material so the pipeline's honesty apparatus is load-bearing rather than decorative. It is not a funded initiative and has no OKR.

### Relevant background

Journaling and mental-health app abandonment is real and large: SRC-002, 18 studies, 525,824 participants, median 70% discontinuation within 100 days, mental-health apps 89–92%. Two of its six named causes are on point — blank-page friction and burdensome data entry.

### Source evidence

See `source_material` in frontmatter and `prototypes/doodle-journal/SOURCES.md` for the trust ladder, including an explicit **do-not-cite** list of eight sources that look citable and aren't.

**Single-source warning:** all counter-evidence rests on one qualitative study, n=54 (SRC-001, Study 2). Stated, not dressed as consensus.

## 3. Users and affected parties

### Primary user

`[?]` **No sourced persona exists.** No interviews, no Condens sessions, no survey, no ticket — confirmed absent by design, not searched-and-missed.

Tier 1 audience is internal design/product staff looking at a prototype. That is who will *view* it, not a validated segment.

### Primary user journey

1. Opens the surface, chooses speak or type.
2. Records or types one entry about their day.
3. Ticks consent for image generation from that entry.
4. Requests a doodle. It appears beside their text.
5. Either keeps it, regenerates, or discards it as not matching — without damaging the entry.

### Affected secondary parties

Anyone whose name, mood, or circumstances appear in someone else's journal entry, and who never consented to inference being run over it. **Unaddressed at Tier 1 and not in scope** — named so it is not mistaken for handled.

## 4. Scope and non-goals

### In scope

Entry capture (voice mocked, text real), explicit consent gate, pre-drawn doodle render alongside text, discard/regenerate, delete-entry gesture, the honesty apparatus.

### Out of scope / non-goals

- Live image generation or any model call.
- Live speech-to-text.
- Any crisis or self-harm detection. **The prototype must not attempt this**, and the demo script must say so rather than imply it is handled.
- Sharing, social features, streaks, or gamification.
- Any therapeutic positioning.

### Scope boundary rules

If a change would make the artifact appear *tested*, it is out of scope regardless of merit.

## 5. UX intent

**This section is canonical.** `ux.md` and `design.md` are *derived* mechanical checklists that enforce it — they hold no reasoning of their own, and every criterion in them carries a `traces_to:` pointer to an id below. If this section changes and a checklist does not, `./check-trace.sh` fails. Judgment lives here; verification lives there.

### Experience principles

- **UXI-01 — The person's own words outrank the machine's picture.** Text is primary; the doodle is a companion to it.
- **UXI-02 — Nothing happens to a disclosure without being asked.** No ambient, automatic, or on-load inference.
- **UXI-03 — Being wrong must be cheap.** Dismissing a bad doodle takes one action and costs nothing.
- **UXI-04 — The artifact tells the truth about itself**, including the evidence against it.

### Desired user feeling

- **UXI-05 — Unobserved.** A journal should feel like a drawer, not a dashboard. The specific feeling to avoid is the one SRC-001 measured: *being interpreted, inaccurately, by something that was not asked to interpret.*

### Key user states

| id | state | treatment |
|---|---|---|
| UXI-06 | Empty / blank page | Two equal affordances, speak or type. No prompt-of-the-day, no coaching. |
| UXI-07 | Captured, no doodle | Complete and valid. The entry is the deliverable; the doodle is optional. |
| UXI-08 | Doodle rendered | Side by side with the text, never replacing it. |
| UXI-09 | Doodle rejected | Immediate removal, no confirmation friction re-exposing the image, entry untouched. |
| UXI-10 | Consent withheld | Render unavailable until consent is given. |

### Accessibility requirements

- **UXI-11 — WCAG AA contrast** across all text and state indicators.
- **UXI-12 — Full keyboard operation** of capture, consent, render, and discard.
- **UXI-13 — Every doodle carries a text alternative.** An image of your own feelings is useless to a screen reader without one.
- **UXI-14 — No reliance on colour alone** to convey state.

**UXI-11 through UXI-14 are unverified.** Zero accessibility testing has been run. These are requirements, not claims — and `design.md` records them as open, not ticked.

## 6. Functional behavior

Full numbered requirements live in `spec.md` as `FR-001`–`FR-011`. Summary of the load-bearing ones:

- **FR-002** at most one doodle per entry, only on explicit action.
- **FR-003** original text always displayed alongside.
- **FR-004** discard/regenerate never alters the entry.
- **FR-006** explicit Art. 9 consent, distinct from general ToS.
- **FR-011** every screen states no reaction data collected, distinct from the fidelity label.

## 7. Invariants

1. An entry's text is never mutated by any doodle operation.
2. A doodle never exists without a consent record for that entry.
3. No doodle is generated without an explicit user action in the same interaction.
4. No screen shows the artifact as tested.
5. No seed datum is real.

## 8. Constraints and dependencies

- **GDPR Art. 9.** Emotion inferred from an entry is special-category data; processing is prohibited by default; consent must be explicit, specific, documented, withdrawable. **The inference step is the regulated act.** Unreviewed by anyone qualified — `OPEN.md` H-02.
- **Retention/deletion SLA is undefined** — no source in this corpus sets one. `OPEN.md` H-03. User Story 3's second acceptance scenario cannot be marked passing without it.
- **Breach precedent is live, not theoretical:** 10 Android mental-health apps, 14.7M installs, 1,575 flaws, Jan 2026.
- Design system: Band palette, Space Mono + Kalam, 28px grid, hard shadows, no rounded corners.

## 9. Tradeoffs and priority rules

1. **Honesty over polish.** If a choice makes the artifact more persuasive but less accurate about its own status, accuracy wins.
2. **Text over image.** Any conflict between showing the doodle well and keeping the words visible resolves to the words.
3. **Design system over self-containment.** Resolved 2026-09-11: the locked typography outranks a zero-network constraint. Generalisation is `OPEN.md` H-08.
4. **Deferring a metric over faking it.** SC-001/SC-002 deferred rather than measured badly against pre-drawn doodles.

## 10. Escalation triggers

Stop and escalate to the named owner when:

- Anyone asks to remove or soften SRC-001's numbers from the artifact.
- Anyone describes this concept as validated, tested, or research-backed.
- A build is proposed with live generation before H-01's reaction test is commissioned.
- Any therapeutic or clinical framing appears in copy.
- Real journal content is proposed as seed data.
- Any `HUMAN` row in `OPEN.md` is about to be resolved by inference rather than by its owner. `./check-blocked.sh` exits 2 here.

## 11. Canonical Definition of Done

Tier 1 is done when the artifact: discloses its fidelity; states no reaction data collected; carries SRC-001 at full strength; shows text alongside every doodle; gates generation behind explicit consent; allows costless discard; uses only `[TEST DATA]`; and contains no clinical language. **All eight hold as of 2026-09-11.**

Tier 1 being done answers **nothing** about whether the concept works.

## 12. Testing, evaluation, and observability

- **Run:** SC-003 timing, instrumented locally, n=1, not stored, not a finding.
- **Not run:** SC-001, SC-002, any reaction test, any usability test, any accessibility audit. Zero participants.
- **Method precedent when H-01 is commissioned:** SRC-001's own Study 2 design — post-use qualitative survey asking participants to describe the image in their own words and rate relevance — measuring **#13a and #13b separately**, because a single combined result cannot distinguish the half a style change can fix from the half it can't.
- **Gate state:** `./check-gates.sh` exits 1 — Gate 1 has 2 open criteria, Gate 2 has 2, Gate 3 has 6.

## 13. Open questions

Indexed in **`OPEN.md`** — 20 rows: 8 `HUMAN`, 8 `RESEARCH`, 4 `ACCEPTED`, read by `./check-blocked.sh` (exit 2 = a person owes an answer).

*Note on duplication: `OPEN.md` was built before this intent spec existed. In acp-core's pattern this section holds the questions directly. Whether to fold `OPEN.md` into §13 or keep it as a machine-readable index this section points at is `OPEN.md` H-04.*

Highest-priority human decisions: **H-01** commission the reaction test · **H-02** route the Art. 9 consent copy for review · **H-03** define the retention SLA.

## 14. Decision log

| date | decision | why |
|---|---|---|
| 2026-09-11 | Tier 1 concept probe only; explicitly not a product bet | `[A]`+`[?]` = 58.6% of 29 tagged claims, ~2× the 30% threshold |
| 2026-09-11 | Doodle shown alongside text, never instead of it | If the image misses, the person still has what they actually said |
| 2026-09-11 | Costless discard is a requirement, not polish | At SRC-001's 70%+ irrelevance rate, easy dismissal is the safe default |
| 2026-09-11 | Generation requires explicit per-entry action | Ambient inference on intimate disclosure is both an Art. 9 problem and a trust problem |
| 2026-09-11 | Tier 1 doodles pre-drawn; SC-001/SC-002 deferred to Tier 2 | Resolves critic pass 1 FAIL: a mocked doodle cannot be "their own generated doodle" |
| 2026-09-11 | Unknown #13 split into #13a (semantic match) and #13b (affective register) | Critic pass 1: one hypothesis was addressing only the more forgiving half |
| 2026-09-11 | Falsifiability table added | Without it the probe could run indefinitely without producing a decision |
| 2026-09-11 | Design system beats self-containment on fonts | Locked typography is Beth's spec; zero-network was an instruction I invented |
| 2026-09-11 | `idea_score` left UNSCORED | Rubric never located; a plausible number was not invented |
| 2026-09-11 | Council pass skipped | Beth's explicit decision. Gate 3 rests on one critic pass — a limitation, not a dropped step |

## 15. Change log

| version | date | change |
|---|---|---|
| 0.1.0 | 2026-09-11 | Initial intent spec, written *after* the pipeline had already produced brief, gates, build, and two critic passes — i.e. reverse-engineered from downstream artifacts rather than authored upstream as the canonical source. That inversion is itself a finding: see `design.md`'s provenance caveat and `OPEN.md` A-03. |
