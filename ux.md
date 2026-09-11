---
scope: feature
parent_vision: vision.md
canonical_spec: spec.md
brief: briefs/doodle-journal.brief.md
gate: 1
eval_loop: built-in — see "Acceptance Criteria" below
evidence: scout/ (6 files, web-only) · briefs/doodle-journal.brief.md (28 tagged claims)
---

# ux.md — Doodle Journal (Test Concept)

Gate 1 spine. Everything here traces to `scout/` or to `briefs/doodle-journal.brief.md`. Nothing on this page is real user research, because none exists for this concept — that absence is a finding, not a gap to fill.

## Who

- `[?]` **No sourced persona exists.** No interviews, no Condens sessions, no survey, no Jira/Confluence ticket — confirmed absent by design, not searched-and-missed (brief ledger #28).
- Tier 1 build audience, per the task framing: internal design/product staff. This is who will *look at the prototype*, not a validated user segment. `[A]`

## The Problem — split, because it does not hold together as one claim

**The sourced half.** `[D]` People abandon journaling and mental-health apps at scale: 18 studies, 525,824 participants, median 70% discontinuation within the first 100 days; mental-health apps specifically 89–92%. Source: PMC11694054, fetched directly (brief ledger #1, #2). Two of its six abandonment-reason categories are on point — "blank page / low personalization" and "burdensome data entry" (ledger #3).

**The unsourced half.** `[A]` That a *doodle* reduces that friction is an extrapolation, not a finding (ledger #4). `[?]` No study compares non-verbal/visual capture retention against text journaling head-to-head (ledger #5).

**The half that argues the other way.** `[R]` StoryWriter (PMC9810434, fetched and read in full) is the only primary study located that measured how people react to AI-generated imagery of their own emotional disclosure. In its qualitative study, n=54:
- **70.37% (38/54)** judged the generated images **irrelevant to their own narrative** (ledger #9)
- **70.97%** described the images in **negative language** — "scary," "unsettling," "creepy" (ledger #10)
- only **26.63%** of images were rated suitable for the task (ledger #11)
- its own mechanism finding: the modest benefit it measured (anger d=−0.40, sadness d=−0.63) came from **the writing, not the images** (ledger #12)

These numbers stay at full strength wherever this concept is discussed. Softening them into "some users found the images imperfect" is the specific failure this gate exists to prevent.

## Top Tasks (provisional — no voting has occurred)

Derived from the brief's prioritized user stories, not from user research. `[A]` on all three.

1. Capture a reflection with minimal friction — voice or text, user's choice (brief User Story 1, P1 — the only story resting on a sourced problem)
2. See the entry rendered as a doodle, alongside the original text (User Story 2, P2 — the disputed core claim)
3. Dismiss a doodle that misses, without damaging the entry (User Story 3, P3 — direct mitigation for ledger #9-#10)

## Atomic Insights

- `[D]` Abandonment is driven partly by data-entry burden and blank-page friction — PMC11694054 (ledger #3). This is the strongest ground the concept stands on.
- `[R]` A machine rendering a person's own disclosure back to them gets it wrong, in ways users find unsettling, a majority of the time — PMC9810434 (ledger #9-#11).
- `[?]` Whether a *hand-drawn doodle* style avoids that reaction is **the single most decision-relevant unknown** and is untested anywhere reachable (ledger #13).
- `[?]` Nobody has measured whether a doodle can be skimmed or revisited more easily than a voice note. The concept's implicit "text is hard to revisit" premise is unexamined (ledger #17, #18).
- `[R]` Emotion inferred from a journal entry is GDPR Article 9 special-category data, and the *inference step* is the regulated act — not merely the storage (ledger #23, #24).
- `[THIN DOMAIN]` The entire evidence base is Western, English-language, academic-institutional. Visual/reflective journaling practices outside that strand are absent from what a web scout can reach — named, not filled (scout/00-index).

## Acceptance Criteria — Gate 1: Do we understand the problem?

Written as literal checkboxes because `check-gates.sh` reads them literally. Unchecked means unchecked — these are not aspirational.

- [x] The general abandonment problem is sourced to PMC11694054 wherever it is cited, not asserted — holds in this file and in the brief
- [x] The claim "a doodle solves the abandonment problem" is nowhere presented as sourced — it is `[A]`/`[?]` in this file and in the brief, and has not been upgraded
- [ ] The StoryWriter finding (70.37% irrelevant / 70.97% negative language) is carried with its exact numbers into the **build** and the **post-build critic** — cannot be checked until those stages exist
- [x] No internal user research exists for this concept, confirmed absent by design rather than unsearched — scout/00-index line 2
- [ ] A named test plan exists for the doodle-style unknown (ledger #13) before Gate 2 is upgraded from PARTIAL — does not exist yet; Beth's call to commission
- [x] The `[A]`+`[?]` share of tagged claims is **recomputed, not estimated** — grep-verified 2026-09-11 after Critic Pass 1 split ledger #13 into #13a/#13b: **29 rows, 8 `[R]` / 4 `[D]` / 8 `[A]` / 9 `[?]` → 58.6%**. *(Superseded, not deleted: 28 rows / 57.1% before the split.)*

**Two boxes are open, on purpose.** 58.6% `[A]`+`[?]` is nearly double the 30% threshold. Gate 1 is red and should be.

## Critic Pass 1 — what it changed here

The pre-build critic split this concept's central unknown in two, and the distinction matters more than anything else on this page:

- **#13a — semantic match.** 70.37% found the image irrelevant to their own narrative. A doodle style change does **not** plausibly fix this. It is the more damaging half.
- **#13b — affective register.** 70.97% found the image unsettling. A hand-drawn style is a plausible mitigation — and this is the *only* half the concept's bet actually addresses.

The original framing collapsed both into "does doodle style avoid the reaction," which could only ever speak to #13b. Anyone reading this concept as "we have a hypothesis that fixes the StoryWriter problem" is reading it wrong: at best it addresses half, and the more forgiving half.

## Mini Docs

- `scout/03-text-to-image-reflective-surface.md` — read first, it is the load-bearing file
- `briefs/doodle-journal.brief.md` — full tag ledger and the arithmetic
- `prototypes/doodle-journal/doodle-journal.html` — the Tier 1 build. It carries the StoryWriter numbers on its own face and a red "no data has been collected" panel, because this file's Gate 1 findings are the ones most likely to get lost when the HTML travels without its brief
- `prototypes/doodle-journal/critic-pass-1.md` · `critic-pass-2.md` — the review record, including the #13a/#13b split that changed what this gate claims
