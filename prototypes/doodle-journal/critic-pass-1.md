# Critic Pass 1 — Doodle Journal (Pre-Build)
Reviewed: briefs/doodle-journal.brief.md, ux.md, vision.md, .specify/memory/constitution.md, scout/00-05.
No HTML exists yet — this is a pre-build brief/gate review only.

## Scorecard

| Dimension | Score | Reason |
|---|---|---|
| Source check | PASS | Sampled 15+ ledger locators (scout/01 L41,L46; scout/02 L4,L9-10,L19,L20; scout/03 L34,L35; scout/04 L12,L16,L18-19; scout/05 L4,L7,L11-16,L24) — every one resolves to the exact claim and framing cited. No fabricated locator, no invented stat, no persona/seed data yet (none built). |
| Gate 1 — Problem | PARTIAL, correctly red | Split framing (real abandonment problem / unsourced mechanism / contradicting primary finding) holds under scrutiny. All four checked boxes in ux.md verified true against their cited evidence. But the gate's own "one named unknown" (ledger #13) is narrower than the evidence it's meant to resolve — see FAIL below. |
| Gate 2 — Right thing | PARTIAL, correctly red, but reasoning has a hole | The probe-not-product distinction is stated and (so far) held to in every artifact. The hole: the probe as scoped can only ever speak to the "unsettling tone" half of StoryWriter's finding, not the "irrelevant to my narrative" half — see FAIL below. No falsifiability condition exists for ledger #13 either direction. |
| Gate 3 — Built right / testable | FAIL | SC-001 and SC-002 require measuring reaction to a participant's "own generated doodle." The brief's own Assumptions section permits Tier-1 doodles to be mocked/pre-generated rather than live-inferred. A mocked doodle cannot be "their own generated doodle" in the sense the SC requires. This is a direct contradiction inside one document, not a hypothetical. |
| Requirements shape (P1-P3 / FR / SC) | PARTIAL | Priorities are honestly justified (P2/P3 explicitly tied to the unfavorable finding, not treated as default features). SC-001/002/003 correctly refuse to invent target thresholds — that's honest, not evasive, given no benchmark exists to justify one. But SC-003 has no traceable link back to any user story's acceptance scenarios, and SC-001/002 inherit the Gate-3 contradiction above. FR-010 carries an open [NEEDS CLARIFICATION] that User Story 3's Acceptance Scenario 2 quietly depends on. |
| Design system compliance | N/A | No HTML exists at this stage — nothing to check against Apex Bridge tokens, typography, or rail structure yet. Flagging only so it isn't silently skipped: this dimension is owed at critic-pass-2, not before. |

## Punch list

**FAIL — Gate 3 contradicts itself on what "the doodle" is.**
Assumptions section: "Tier 1 fidelity means the doodle rendering itself may be mocked/pre-generated [TEST DATA], not necessarily live inference." SC-001/SC-002: measure whether participants describe "their own generated doodle" as irrelevant/unsettling, benchmarked against StoryWriter's real-inference numbers. A pre-baked image is not "their own generated doodle" — the comparison to StoryWriter's 70.37%/70.97% becomes meaningless if the build takes the mocked path the brief itself allows. This must be resolved — decide and state whether Tier 1 requires live generation for the reaction-test path, or drop SC-001/002 as unmeasurable at this fidelity — before build, not discovered after.

**FAIL — The "one named unknown" doesn't cover the evidence it's meant to resolve.**
StoryWriter's finding is two separate numbers with two different plausible causes: 70.37% irrelevant-to-narrative (a content/semantic-matching failure — the machine didn't render what they actually said) and 70.97% negative/unsettling language (plausibly a style/aesthetic failure — the machine's rendering felt creepy). Ledger #13 frames the whole probe as "does doodle style avoid the reaction," which at best addresses the second number. The brief, ux.md, and vision.md all treat this as one resolvable unknown. If the eventual test shows "still irrelevant, but less unsettling," nothing in Gate 2 says whether that counts as resolving ledger #13 or not — there is no stated falsifiability condition. Name what result, in either direction, actually moves Gate 2 off PARTIAL.

**RISK — "Research probe" framing has no hard control against becoming "we tested this."**
vision.md names this exact drift as the most likely failure mode and says it happens in a stakeholder readout, not the code — correct prediction, but nothing operationalizes it. FR-007 requires a Tier-1/Concept fidelity label on every screen; it does not require a distinct statement that no reaction data has been collected. A fidelity badge and a "this hasn't been tested" disclosure are different claims — only the first is currently an FR.

**RISK — FR-010's open clarification is load-bearing for a stated acceptance scenario.**
FR-010 flags "[NEEDS CLARIFICATION: retention/deletion SLA not sourced anywhere in this corpus]." User Story 3's Acceptance Scenario 2 requires confirming "no residual inferred-emotion data attached to the entry" after discard — that's untestable without a defined deletion/propagation timing. Fine to leave open at Tier 1; not fine if build proceeds and this scenario gets marked "passing" against an undefined target.

**RISK — SC-003 is untethered.**
Every other SC traces to a specific user story's independent test. SC-003 (time-to-completed-entry) doesn't map to any story's acceptance scenarios or independent test — it's a freestanding metric with nowhere it plugs in.

**MISSING — No falsifiability condition for Gate 2's central hypothesis** (restated from the FAIL above, listed separately because it's a missing artifact, not just a reasoning gap): there is no written statement of what evidence would move Gate 2 from PARTIAL to PASS versus PARTIAL to killed. Without it, the probe can run indefinitely without ever producing a decision.

**MISSING — design.md / Gate 3 acceptance criteria file.**
Not a defect at this pipeline stage — expected to arrive at build. Naming it so it isn't mistaken for already covered: constitution's check-gates.sh treats a missing file as an automatic non-pass, and Gate 3 has not been assessed here because its source document doesn't exist yet.

**PASS — StoryWriter evidence functions as a design driver, not a risk-section footnote.**
It shapes FR-002 (no ambient/automatic generation), FR-003 (text always shown alongside doodle, never replaced), FR-004 (immediate discard without altering the entry), and directly justifies User Story 3's P3 priority. Failure Mode #1 restates it as the primary risk. This is the opposite of quarantining — it earns a clean pass on the question you asked me to check hardest.

**PASS — No falsely-checked gate box found.**
Checked every box in ux.md (4 checked / 2 open) and vision.md (4 checked / 2 open) against its cited evidence. All eight checked boxes hold up; both pairs of open boxes are legitimately blocked on artifacts (build, commissioned test plan) that don't exist yet — not soft-pedaled into a pass. The 2-of-6 open count in each gate is the right call, not an undercount or overcount.

**PASS — No invented numbers, personas, or scores.**
`idea_score` left UNSCORED with a stated reason rather than backfilled. `okr_objective`/`okr_key_result`/`counter_metric` correctly marked `[?]` rather than invented. The "3-4x speaking vs typing" and other `[CS: LOW]`-flagged vendor stats are tagged `[A]` in the ledger and never surface as hard numbers in the requirements text itself.

**PASS — Constitution's honesty rules are operationalized, not left as prose.**
FR-007 (fidelity label), FR-008 (no clinical/therapeutic language), FR-009 (fictional `[TEST DATA]` flag) map directly onto the constitution's three "Honesty Rules For This Repo." Enforceable requirements, not aspirational statements.

**SINGLE-SOURCE — named correctly, flagging per contract, not as a hidden defect.**
The entire counter-evidence against the doodle mechanism rests on one qualitative study, n=54 (StoryWriter, PMC9810434, Study 2). The brief itself calls this "the only primary study located" rather than dressing it as consensus — this is the correct move, and the required flag is here for completeness, not because it was concealed.

**UNSOURCED — none found.** No claim, quote, or stat in brief.md, ux.md, or vision.md lacked a locatable source in this pass. The one item that would have been the most likely candidate — the "3-4x faster speaking" multiplier and the unverified JMIR/Frontiers citations in scout/02 — are correctly tagged `[CS: LOW]` at the source and never get carried into the brief as asserted fact.

## Bottom line

Don't build yet. The two FAILs are brief-level reasoning defects — a self-contradiction between Assumptions and Success Criteria, and an unstated falsifiability condition for the concept's one named unknown. Both are fixable at the document level in less time than a build takes, and both will get baked into HTML and then into a critic-pass-2 delta table as inherited defects if they cross into build unresolved. Everything else here — the gate honesty, the evidence-carrying, the absence of invented numbers — is functioning as designed and shouldn't be re-litigated at pass 2.

---

## Orchestrator note — pipeline sequencing violation, recorded 2026-09-11

This pass was launched as pipeline step 3 (pre-build critic), but the build agent (step 4) was launched before this pass returned. The two ran concurrently. That is a violation of the point of a pre-build critic: its two FAILs could not inform a build that was already in flight.

The build was allowed to land rather than aborted, and the brief was corrected against this punch list in the same turn this pass was received (see "Critic Pass 1 — resolutions" in `briefs/doodle-journal.brief.md`). Critic pass 2 therefore carries an extra duty it would not normally have: checking whether the shipped HTML inherited either FAIL from the pre-correction brief it was actually built against.

Recorded here rather than quietly fixed, because "the pre-build critic ran" and "the pre-build critic informed the build" are different claims, and only the first is true of this run.
