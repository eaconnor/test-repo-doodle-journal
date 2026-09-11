# Critic Pass 2 — Doodle Journal (Post-Build)
Reviewed: `prototypes/doodle-journal/doodle-journal.html` (full read, incl. `<style>` and `<script>` blocks), `critic-pass-1.md`, `briefs/doodle-journal.brief.md`, `ux.md`, `vision.md`, `spec.md`, `.specify/memory/constitution.md`, `scout/03`.

**Council pass:** explicitly skipped by Beth's decision for this run. Not a dropped step — noted per instruction. Gate 3's acceptance criteria therefore rest on this single critic pass, not a multi-voice council; weighted accordingly, and named as a limitation rather than hidden.

**Pipeline sequencing violation, inherited:** the build agent ran before Pass 1 returned, against the pre-correction brief. The document-level FAILs from Pass 1 were resolved in the brief/ux/vision *afterward* by the orchestrator, then hand-patched into the already-built HTML. This pass's job is to check whether those patches actually closed the gap or just covered it.

## Scorecard — Pass 2

| Dimension | Score | Reason |
|---|---|---|
| Source check | **FAIL** | StoryWriter numbers (70.37%/70.97%/26.63%) verified correct against scout/03 and carried at full strength — good. But the Bradley rail quotes **57.1%** as the brief's [A]/[?] share; every source document (brief.md, ux.md, vision.md) recomputed this to **58.6%** after the #13 split and explicitly marked 57.1% "superseded, not deleted." [CS: VERIFIED — recounted the 29-row tag ledger myself] The 47% rule exists precisely to catch a stale stat like this before it ships. |
| Gate 1 — Problem | PARTIAL, red, correctly — but a new build-level gap | The #13a/#13b split (the finding that "one named unknown" was really two) now appears on-screen, in the header subtitle — satisfying ux.md's previously-blocked checkbox. But it is not present in the rail, which is the higher-traffic summary surface for a stakeholder skim. |
| Gate 2 — Right thing | PARTIAL, red, correctly — same hole, relocated | vision.md's condition was that on-screen framing keep "testing an unknown" and "validating the concept" distinct everywhere. The rail's blurb, "what will hurt you" block, and Product routed card all still cite the undifferentiated "ledger #13," not the split — so the exact drift vision.md predicted ("happens in a stakeholder readout") has a live, unpatched vector: reading only the rail. |
| Gate 3 — Built right / testable | **FAIL, same shape as Pass 1, relocated not resolved** | Pass 1's FAIL was: a mocked doodle cannot be "their own generated doodle" that SC-001/SC-002 require. The brief resolved this at the document level (SC-001/SC-002 explicitly deferred, and the build's own disclosure box says so). But the per-entry "describe-box" recreates the identical contradiction inside the build itself: it is labeled "Measurement instrument... captured verbatim for the reaction-test record" and confirms "Saved ✓ — verbatim, timestamped" on a pre-drawn doodle — the JS does not persist or timestamp anything. [CS: VERIFIED — read `saveDescBtn` handler in full] The document-level fix did not reach the UI copy that recreates the same false claim. |
| Requirements shape (FR/SC) | PARTIAL, with new defects found at build | FR-002/003/004/009 verified correctly implemented in the JS. FR-011 and SC-006 exist as required text. New defects found only visible at build: FR-001's voice transcript (`#voiceTranscript`) carries a permanent `readonly` attribute never removed by any code path, contradicting its own aria-label ("editable after mock recording") and Acceptance Scenario 1. SC-003 — named as "the only success criterion the Tier 1 build can actually exercise" — has zero instrumentation; no elapsed-time code exists anywhere in the script. FR-010 is honestly self-flagged in the rail as unverified, which is correct. |
| Design system compliance | N/A → **PARTIAL** | First assessment. Itten tokens (`#D8472B`/`#1F3C96`/`#C99A2E`/`#efe7d6`/`#f7f0df`), 28px grid, hard `Npx Npx 0` offset shadows, no rounded corners, no emoji: present and consistent through the main stylesheet — real compliance, not decoration. Two gaps: (1) no Google Fonts `<link>`/`@import` found anywhere in `<head>` — Space Mono and Kalam are declared in `font-family` but never loaded, silently falling back to system fonts for essentially every reader; (2) the hand-patched FR-011 disclosure block hardcodes `#D8472B` and a translucent `rgba(26,22,18,.18)` shadow instead of `var(--vermillion)` and the page's established opaque hard-shadow convention — token drift, specifically in the block that was patched outside the normal build step, exactly where the task asked to look. |

## Delta table vs. Pass 1

| Dimension | Pass 1 | Pass 2 | What changed |
|---|---|---|---|
| Source check | PASS | FAIL | Stale 57.1% figure shipped in the rail; every source doc moved to 58.6% after the #13 split. New defect, introduced at the hand-patch stage, not present in Pass 1 (no HTML existed then). |
| Gate 1 — Problem | PARTIAL, correctly red | PARTIAL, correctly red | The #13a/#13b split closed ux.md's open checkbox in one place (header) but not in the rail — hole narrowed, not closed. |
| Gate 2 — Right thing | PARTIAL, correctly red, w/ hole | PARTIAL, correctly red, hole reopened elsewhere | Same split-propagation gap as Gate 1, from the Gate 2 angle: the rail and Product routed card still read as if the unknown is singular and untested-full-stop, not "half-addressed at best." |
| Gate 3 — Built right/testable | FAIL (mocked doodle vs. "own generated doodle" contradiction) | FAIL, same shape, relocated into the build | Document-level contradiction resolved (brief/vision/spec now correctly defer SC-001/SC-002). Build-level contradiction reintroduced via the describe-box's "measurement instrument... timestamped" copy, which the code does not back up. |
| Requirements shape | PARTIAL | PARTIAL, two new build-only defects | FR-011/SC-006 added as required. New: FR-001 transcript not actually editable; SC-003 not instrumented anywhere despite being the one SC this build was supposed to be able to exercise. |
| Design system compliance | N/A | PARTIAL | First-ever assessment. Tokens/grid/shadows/no-rounded-corners/no-emoji hold through the main stylesheet. Fonts never loaded via Google Fonts. Hand-patched block drifts from tokens into hardcoded hex + soft shadow. |

## Verdict on the two post-build patches — adversarial read

**FR-011 disclosure ("no reaction data collected"):** Adequate in isolation — well-placed (above the fold, before the StoryWriter card), visually distinct from the FR-007 fidelity banner (separate vermillion-bordered card, different color and position), and specific (names SC-001/SC-002 by number and explains why they're unmeasurable). **Inadequate as a system-wide guarantee.** It is directly contradicted a few hundred pixels down by the describe-box's "Measurement instrument... captured verbatim for the reaction-test record" / "Saved ✓ — verbatim, timestamped" — language that claims exactly the kind of reaction-data capture the disclosure just said doesn't exist, on data (pre-drawn doodles) the brief itself says cannot support that measurement. This is a label slapped over a defect: the disclosure text is correct, but the interactive part of the page was never brought into line with it.

**#13a/#13b split:** Adequate where it appears — the header subtitle states the split correctly and names which half a doodle style plausibly addresses. **Inadequate as delivered**, because it appears in exactly one location and in low-visual-weight text (13px, opacity .8) directly beside a 26px bold vermillion stats card that carries no such nuance. The rail — the artifact's own executive-summary surface, designed to be read by someone deciding whether to keep going — still frames the unknown as singular and cites the pre-split, superseded percentage. A reader who skims the rail alone (a realistic reading pattern for a Bradley rail) walks away with the exact pre-Critic-Pass-1 misreading this patch was meant to prevent.

**Net answer to the adversarial question:** the artifact does not yet genuinely prevent a stakeholder from walking away thinking the concept was tested (the describe-box invites that reading directly), and it does not consistently prevent the "doodle style answers the whole StoryWriter problem" misreading (the split exists in one place and is undermined by its own visual hierarchy, and is absent from the rail).

## Punch list

**FAIL — describe-box contradicts FR-011.** "Measurement instrument... captured verbatim for the reaction-test record, not a feedback nicety" and "Saved ✓ — verbatim, timestamped" appear on every entry card's doodle-description field. [CS: VERIFIED] `saveDescBtn`'s click handler only toggles a `hidden` attribute — no `Date.now()`, no storage, no export, nothing "timestamped." This directly undermines the disclosure box's claim that zero reaction data has been collected, on the exact pre-drawn doodles the disclosure names as structurally incapable of producing that data.

**FAIL — `#voiceTranscript` is permanently readonly.** [CS: VERIFIED — no code path in the script removes the attribute] Its own `aria-label` claims "editable after mock recording"; Acceptance Scenario 1 (spec.md, brief.md) requires the transcript be reviewable *and editable*. Neither is true as shipped.

**FAIL — SC-003 has zero instrumentation.** [CS: VERIFIED] No elapsed-time / `Date.now()` timing code exists anywhere in the script. SC-003 is named in spec.md as "the only success criterion the Tier 1 build can actually exercise" — the build does not exercise it.

**FAIL — stale statistic shipped in the Bradley rail.** Rail blurb states "57.1% of this brief's tagged claims are [A]/[?]." [CS: VERIFIED — recounted the 29-row tag ledger: 8 [R] + 4 [D] + 8 [A] + 9 [?], (8+9)/29 = 58.6%] All three source documents carry the corrected 58.6% and explicitly flag 57.1% as superseded. This is a 47%-rule violation shipped into the artifact itself.

**FAIL — #13a/#13b split not propagated to the rail.** The rail blurb, the "what will hurt you" dual-block, and the Product routed card all still reference undifferentiated "ledger #13," not the split that names doodle style as addressing at most the affective-register half (#13b), never the semantic-match half (#13a). Only the page header carries the split.

**RISK — visual hierarchy inverts the intended emphasis.** The #13a/#13b distinction sits in 13px/opacity-.8 subtitle text; the StoryWriter numbers sit in a 26px bold vermillion stats card three sections later. The more decision-critical claim (this can only ever answer half the problem) is the least visually prominent claim on the page.

**FAIL (design system) — no font loading.** [CS: VERIFIED — full `<head>` read, no `<link>`/`@import` to fonts.googleapis.com or any font source] Space Mono and Kalam are declared in `font-family` stacks but never fetched. Both fall back to Comic Sans MS / Courier New for effectively every reader who doesn't happen to have these fonts installed locally.

**FAIL (design system) — hand-patched block drifts from tokens.** The FR-011 disclosure box hardcodes `border:2px solid #D8472B; border-left:10px solid #D8472B;` instead of `var(--vermillion)`, and uses `box-shadow:6px 6px 0 rgba(26,22,18,.18)` — a translucent shadow — where every other card on the page uses the opaque `var(--line)` hard-shadow convention. This is drift specifically in the block that was patched outside the normal build step.

**RISK — consent checkbox doesn't gate after the fact.** Unchecking consent after a render doesn't hide or retract the already-rendered doodle. Minor; not central to this pass's mandate but worth naming.

**PASS — StoryWriter numbers at full strength, correctly sourced.** 70.37%/70.97%/26.63%, the mechanism finding (benefit from writing not images), and the PMC9810434 citation all match scout/03 exactly. [CS: VERIFIED]

**PASS — FR-002/FR-003/FR-004 correctly implemented.** Doodle render is consent-gated and requires an explicit click (no ambient generation); original entry text is never touched by render/discard/again handlers; verified directly in the JS.

**PASS — seed data fictional, clearly tagged, over-labeled.** All three seed entries and all composer-generated entries carry `[TEST DATA]` plus an explicit "(fabricated, not a real person)" — exceeds the bare FR-009 requirement.

**PASS — no clinical/therapeutic language found.** Manual scan of all copy found no violations. The footer's "no clinical or therapeutic claim is made" sentence is compliance, correctly not flagged as a violation.

**PASS — Itten token palette, 28px grid, hard shadows, no rounded corners, no emoji hold through the main stylesheet.** `:root` block matches CLAUDE.md's locked palette exactly; consistent 28px spacing; every shadow in the primary stylesheet uses the opaque `Npx Npx 0 var(--line)` form; no `border-radius` found; no emoji glyphs found (the "✓" is a Unicode checkmark, not a decorative emoji).

**PASS — honest self-flagging survives into the rail.** The "what will hurt you" block correctly names the consent checkbox as UI-pattern-only (not legal review) and FR-010's deletion as a UI gesture without a verified propagation guarantee. This is the rail doing exactly what it's for.

**SINGLE-SOURCE — carried forward, correctly unresolved.** All counter-evidence against the doodle mechanism still rests on one qualitative study, n=54 (StoryWriter, PMC9810434, Study 2). Named as such in the brief and not dressed as consensus anywhere in the build. Not a new defect — flagged per contract.

**MISSING — SOURCES.md / handoff packet.** *(Resolved after this pass was written: `SOURCES.md` now exists in this folder.)*

## Bottom line

Two of Pass 1's FAILs were genuinely resolved at the document level and one new document-level improvement (the falsifiability table) landed cleanly. But because the build ran against the pre-correction brief, both fixes had to be hand-patched into already-shipped HTML rather than built in — and neither patch reached every place the underlying misreading lives. The result is an artifact where the *correct* framing exists but is inconsistently applied (present in the header, absent or stale in the rail) and, in one case, actively undercut by unrelated UI copy that was never updated to match (the describe-box). A stakeholder who reads the whole page carefully gets the honest picture. A stakeholder who skims the rail, or who clicks through the interactive part, does not. That gap — between "the honest text exists somewhere on this page" and "the page as a whole cannot be misread" — is the load-bearing finding of this pass.

---

## Orchestrator response — what was fixed after this pass, 2026-09-11

Five of the seven FAILs above were introduced by the orchestrator's own hand-patches, not by the build agent. All were fixed after this pass and re-verified; see the "post-pass-2 remediation" note in `design.md` for which Gate 3 boxes flipped as a result.

One FAIL is **not** a build defect and is recorded here as a constraint conflict rather than fixed: **font loading.** The build agent was explicitly instructed to ship with no external dependencies, no CDN links, and no network calls — so it could not load Space Mono or Kalam, and correctly used fallback stacks instead. "Self-contained, zero network" and "webfonts loaded" cannot both be true for a single-file offline artifact. The design-system rule and the no-external-refs rule are in genuine conflict here; naming it as a decision Beth owns rather than silently resolving it in either direction.
