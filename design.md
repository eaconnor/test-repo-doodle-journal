---
scope: feature
gate: 3
derived_from: "Intent Specs/doodle-journal.md §5 (UX intent, UXI-01..UXI-14), §7 (invariants), §11 (definition of done), §12 (testing)"
role: "DERIVED MECHANICAL CHECKLIST — holds no reasoning. Judgment lives in the intent spec."
eval_loop: "./check-gates.sh (box state) + ./check-trace.sh (trace validity)"
---

# design.md — Gate 3 (derived checklist)

**Do not write reasoning here.** Experience principles, desired feeling, key user states and accessibility requirements are canonical at intent spec **§5** as `UXI-01`–`UXI-14`. This file only enforces them.

Every criterion was settled by reading the shipped `<style>`/`<script>` or by executing the interaction in a browser — not by reading the brief's intent. Unchecked means the condition is **not true**, never that it was overlooked.

> **Provenance note, kept as a finding.** Version 0.1 of this file was authored *from* the finished build by critic pass 2 — a gate written after the artifact, grading it on its own terms. It has since been rewritten as a checklist derived from intent authored upstream, which is the correct direction. The original inversion is recorded at `OPEN.md` A-03.

## Acceptance Criteria — Gate 3: Are we making the thing right?

**Invariants — verified by execution**
- [x] G3-01 — Original entry text is displayed alongside every rendered doodle and is never the sole record · traces_to: UXI-01, UXI-08 · verified_by: DOM check after render; entry text present
- [x] G3-02 — No doodle exists on load; generation fires only on an explicit per-entry action · traces_to: UXI-02 · verified_by: `svgsOnLoad` = 0, 1 SVG only after click
- [x] G3-03 — Render is unavailable until per-entry consent is given · traces_to: UXI-10 · verified_by: render button `disabled` = true pre-consent, false post-consent
- [x] G3-04 — Discard removes the doodle immediately and leaves the entry text intact · traces_to: UXI-03, UXI-09 · verified_by: post-discard SVG count 0, entry text unchanged
- [x] G3-05 — The voice transcript is reviewable and editable before saving · traces_to: UXI-06 · verified_by: `readOnly` = false in DOM

**Self-disclosure — verified by grep**
- [x] G3-06 — A "Tier 1 · Concept" fidelity label is visible · traces_to: UXI-04 · verified_by: `grep -c 'Tier 1'` ≥ 1
- [x] G3-07 — A "no reaction data collected / no user testing run" statement exists, visually distinct from the fidelity label · traces_to: UXI-04 · verified_by: separate bordered block, own heading, distinct position
- [x] G3-08 — No on-screen copy contradicts G3-07 by claiming data is captured, saved, or timestamped · traces_to: UXI-04 · verified_by: `grep -c 'verbatim, timestamped'` = 0
- [x] G3-09 — Every ratio printed on the artifact matches its source document · traces_to: §1 success metrics · verified_by: 58.6% present, stale 57.1% present only as an explicitly superseded reference
- [x] G3-10 — All seed data is fictional and visibly `[TEST DATA]` tagged · traces_to: §11 · verified_by: `grep -c '\[TEST DATA\]'` = 7, every entry card tagged
- [x] G3-11 — No clinical, therapeutic, or diagnostic language in shipped copy · traces_to: §4 non-goals · verified_by: regex returns only the disclaimer sentence

**Design system — verified by grep**
- [x] G3-12 — Itten palette defined once in `:root`; no ad-hoc hex outside the token block · traces_to: §8 constraints · verified_by: `grep -n '#D8472B'` returns only the `:root` definition
- [x] G3-13 — 28px grid, opaque hard `Npx Npx 0` shadows, no `border-radius`, no emoji · traces_to: §8 · verified_by: `grep -c 'border-radius'` = 0; emoji scan clean
- [x] G3-14 — Space Mono and Kalam are actually loaded, not merely declared · traces_to: §8, §9 tradeoff 3 · verified_by: `document.fonts.check()` true for both families

**Measurement**
- [x] G3-15 — SC-003 (time to completed entry) is instrumented in the build · traces_to: §12 · verified_by: timer returned 1.8s on a live save; labelled on-screen as n=1 and not a finding
- [ ] G3-16 — SC-001 measured: proportion describing their live-generated doodle as irrelevant (#13a) · traces_to: §12, `OPEN.md` H-01 · verified_by: test run — **DEFERRED to Tier 2; structurally unmeasurable on pre-drawn doodles**
- [ ] G3-17 — SC-002 measured: proportion using negative/unsettling language (#13b) · traces_to: §12, `OPEN.md` H-01 · verified_by: test run — **DEFERRED to Tier 2**

**Accessibility — UXI-11..14, none verified**
- [ ] G3-18 — WCAG AA contrast audited · traces_to: UXI-11 · verified_by: a contrast audit — **never run**
- [ ] G3-19 — Full keyboard operation of capture, consent, render, discard · traces_to: UXI-12 · verified_by: a keyboard pass — **never run**
- [ ] G3-20 — Every doodle carries a text alternative · traces_to: UXI-13 · verified_by: `alt`/`aria-label` on every doodle SVG — **not implemented**
- [ ] G3-21 — No state conveyed by colour alone · traces_to: UXI-14 · verified_by: a review — **never run**

**Feels-like-a-drawer — added when `check-trace.sh` caught these as orphaned intents**
- [x] G3-25 — No engagement mechanics: no streaks, no day counters, no notifications or reminders, no share or social affordance · traces_to: UXI-05 · verified_by: `grep -icE 'streak|day [0-9]+ of|notification|reminder'` = 0 **and** `grep -icE '>[^<]*\b(share|post|publish|send to)\b'` = 0. *(Corrected: the first version of this criterion included `badge` in the pattern and claimed 0. It returns 4 — all of them the Tier-1 fidelity badge, not gamification. The claim was true, the stated command was not. Third instance today of writing a command-and-expected-result without running it.)*
- [x] G3-26 — An entry saves and remains complete without a doodle; nothing blocks or nags toward generation · traces_to: UXI-07 · verified_by: save path requires only non-empty text; no modal, prompt, or disabled state pushes the user to render

**Open obligations**
- [ ] G3-22 — Art. 9 consent copy reviewed by someone qualified · traces_to: §8, `OPEN.md` H-02 · verified_by: named reviewer — **open**
- [ ] G3-23 — Retention/deletion SLA defined and sourced · traces_to: §8, `OPEN.md` H-03 · verified_by: a specified timing — **open; User Story 3 AS-2 must not be marked passing until then**
- [ ] G3-24 — Any usability or accessibility testing run with a real person · traces_to: §12 · verified_by: participant count > 0 — **zero participants**

**15 of 24 checked, 9 open.** Count computed, not asserted:
`awk '/^## Acceptance Criteria/{f=1;next} /^## /{f=0} f && /^- \[ \]/{c++} END{print c+0}' design.md`

The nine open split into three kinds, and the distinction is the useful output: **four accessibility requirements nobody has verified** (G3-18..21 — the most fixable of the three, and the most quietly skipped), **two deferred metrics** that a pre-drawn build structurally cannot measure (G3-16/17), and **three human-owned obligations** (G3-22..24). No amount of build polish closes any of them.
