---
scope: design-system + feature
gate: 3
design_system: "Itten / Band Protocol — real, locked, in use by the prototype"
canonical_for: "the design system, the interaction canon, and the usability/accessibility standard"
derived_from: "Intent Specs/doodle-journal.md §5 (UXI-01..UXI-14), §7 (invariants), §11 (definition of done), §12 (testing)"
eval_loop: "./check-gates.sh (box state) + ./check-trace.sh (trace validity)"
standards: ["WCAG 2.2 AA", "Nielsen 10 usability heuristics", "WAI-ARIA 1.2 patterns"]
---

# design.md — Design System, Interaction Canon, and Gate 3

The design system here is **Itten / Band Protocol** — the palette, type, grid and shadow rules locked in `CLAUDE.md §11` and already implemented in `prototypes/doodle-journal/doodle-journal.html`. Every value below is real and in use. Nothing is a placeholder.

Two halves:

- **§§1–8 — the system.** Canonical, reusable across any Band Protocol prototype, not specific to this feature.
- **§9 Acceptance Criteria** — Gate 3 for *this* feature. Read by `check-gates.sh`.

**Reference syntax in `traces_to:`, because this file now has sections of its own.** `§N` means a section of the canonical `Intent Specs/doodle-journal.md`. `ds:N.N` means a section of *this* file's design system. `UXI-##` is an intent-spec §5 requirement; `CLR-##`, `C-##`, `SHD-##` are rules defined below; `H-##` / `R-##` / `A-##` are `OPEN.md` rows. Before this split, `§5` in a gate file was ambiguous between intent-spec §5 and design.md §5 — and `check-trace.sh` resolved it against the intent spec either way, so it would have passed a wrong pointer without complaint.

---

## 1. Foundations

### 1.1 Colour — the Itten palette

Johannes Itten's colour theory as taught at the Bauhaus: a small set of saturated pigment hues held against a warm neutral ground. Locked. Not a starting point to riff on.

| token | hex | role |
|---|---|---|
| `--vermillion` | `#D8472B` | George · primary accent · emphasis |
| `--ultramarine` | `#1F3C96` | Bradley · information · the rail |
| `--ochre` | `#C99A2E` | Paul / Juliet warmth |
| `--violet` | `#5B3A7E` | Juliet · private / reflective |
| `--green-earth` | `#5E7A3F` | Tech · success |
| `--cadmium` | `#E8B93A` | warning |
| `--ink` | `#1a1612` | all body text, all borders |
| `--paper` | `#efe7d6` | page ground |
| `--card` | `#f7f0df` | raised surface |
| `--grid` | `rgba(26,22,18,.055)` | the 28px grid wash |

**Two grounds, one ink.** `--paper` is the page; `--card` is anything lifted off it. `--ink` is the only text colour for body copy — the hues are for *marks*, not for prose.

#### Measured contrast — the constraint, not a footnote

Computed, not asserted. WCAG relative-luminance formula, every pair:

| foreground | on `--paper` | on `--card` | on `--ink` |
|---|---|---|---|
| `--ink` | **14.62** ✅ AA | **15.83** ✅ AA | 1.00 ✗ |
| `--ultramarine` | **7.96** ✅ AA | **8.62** ✅ AA | 1.84 ✗ |
| `--violet` | **7.26** ✅ AA | **7.86** ✅ AA | 2.01 ✗ |
| `--green-earth` | 3.94 ⚠️ large only | 4.27 ⚠️ large only | 3.71 ⚠️ large only |
| `--vermillion` | 3.52 ⚠️ large only | 3.81 ⚠️ large only | 4.16 ⚠️ large only |
| `--ochre` | 2.10 ✗ **FAIL** | 2.27 ✗ **FAIL** | **6.98** ✅ AA |
| `--cadmium` | 1.49 ✗ **FAIL** | 1.62 ✗ **FAIL** | **9.79** ✅ AA |

Reproduce with `scripts/contrast.py`. ✅ = ≥4.5:1 · ⚠️ = ≥3:1, large text and UI boundaries only · ✗ = below 3:1.

**The rules that fall out of that table. They are not negotiable.**

| # | rule |
|---|---|
| CLR-01 | **`--ochre` and `--cadmium` may never carry text on `--paper` or `--card`.** 2.10:1 and 1.49:1. On light ground they are fill-and-border colours, or they take `--ink` text on top of themselves. This is the easiest way to break accessibility in this palette, and it looks fine to a sighted designer on a good monitor. |
| CLR-02 | `--vermillion` and `--green-earth` clear 3:1 but not 4.5:1. Permitted for **headings ≥24px**, ≥18.66px bold, icons, borders and rules. **Not permitted for body copy** at 16px. |
| CLR-03 | `--ink`, `--ultramarine` and `--violet` are the only body-text colours on a light ground. |
| CLR-04 | On `--ink` ground the polarity inverts: `--cadmium` (9.79) and `--ochre` (6.98) become the *safe* choices while `--ultramarine` (1.84) and `--violet` (2.01) become unusable. A dark panel is not the light panel with colours swapped — it is a separate pairing decision. |
| CLR-05 | Status is **never** colour alone (WCAG 1.4.1). Every status carries an icon, a text label, or a border-weight change as well. With four status hues and two of them failing on light ground, colour-alone would fail twice over. |

### 1.2 Grid and spacing — 28px

One number. The page is a 28px grid, visible as a `--grid` wash, and every spacing value is a multiple of it or a clean division.

| token | value | use |
|---|---|---|
| `--space-quarter` | 7px | inline nudge, icon-to-label |
| `--space-half` | 14px | within a component |
| `--space-1` | 28px | default component padding, between related components |
| `--space-2` | 56px | between groups |
| `--space-3` | 84px | between sections |
| `--space-4` | 112px | page-level rhythm |

**Rules:**
- Nothing is spaced by a value outside this set. An off-grid value is a bug, not a judgement call.
- **Margin belongs to the parent layout, not the child component.** A component never sets its own outer margin — otherwise spacing becomes unpredictable the moment it is reused. This is the most commonly violated rule in any design system and the cause of most "why is this misaligned" tickets.
- The grid wash stays visible. It is how a viewer can see that the system is a system.

### 1.3 Type — Space Mono and Kalam

Two faces, each with one job. **Space Mono** for anything the *machine* says: headers, UI chrome, labels, ids, values. **Kalam** for anything a *person* says: body copy, entries, notes. The split is semantic, not decorative — a mono label above a handwritten body tells the reader which voice they are reading.

| token | size / line-height | face | weight | use |
|---|---|---|---|---|
| `--type-display` | 34 / 42 | Space Mono | 700 | page title, one per page |
| `--type-h1` | 24 / 28 | Space Mono | 700 | section heading |
| `--type-h2` | 19 / 28 | Space Mono | 700 | subsection |
| `--type-label` | 11 / 14 | Space Mono | 700, `letter-spacing: .08em`, uppercase | rail labels, badges, field labels |
| `--type-mono` | 13 / 21 | Space Mono | 400 | ids, values, code |
| `--type-body` | 16 / 28 | Kalam | 400 | body copy, journal entries |
| `--type-body-lg` | 19 / 28 | Kalam | 400 | the entry itself, lead paragraphs |
| `--type-caption` | 13 / 14 | Space Mono | 400 | metadata, provenance, timestamps |

Line-heights land on the 28px grid or half of it, so text blocks stack on the grid rather than fighting it.

**Rules:** never skip more than one heading level. Kalam never carries a number a reader must read precisely — handwritten `7` and `1` are too close. Font size never indicates state; that is weight, border, or a label.

### 1.4 Shadow, border, radius

| token | value |
|---|---|
| `--shadow` | `6px 6px 0 var(--ink)` |
| `--shadow-sm` | `3px 3px 0 var(--ink)` |
| `--shadow-pressed` | `2px 2px 0 var(--ink)` |
| `--border` | `2px solid var(--ink)` |
| `--border-strong` | `3px solid var(--ink)` |
| `--radius` | `0` — always |

These are the rules that make it read as Itten rather than as generic flat design.

| # | rule |
|---|---|
| SHD-01 | **The shadow is hard and fully opaque.** `6px 6px 0 var(--ink)` — no blur radius, no alpha. A translucent or blurred shadow reads as Material and breaks the Bauhaus register immediately. This has been shipped wrong once in this repo; see `critic-pass-2.md`. |
| SHD-02 | Offset is always down-and-right, always equal on both axes, always a multiple of 3. One light source, never reconsidered per component. |
| SHD-03 | **`border-radius` is 0 everywhere.** No exceptions, including avatars, badges and inputs. `grep -c 'border-radius'` over any Band prototype must return 0. |
| SHD-04 | A shadowed element always has a border. The shadow is the border's cast, so a borderless shadow floats wrong. |
| SHD-05 | Pressed state shifts the element 4px down-and-right and shortens the shadow to `--shadow-pressed`, so the total silhouette stays constant. The thing physically depresses; nothing reflows. |
| SHD-06 | **No emoji, anywhere.** Not in UI copy, not in headings, not in markdown deliverables. Shapes, rules and text labels do that work. |

### 1.5 Motion

| token | value | use |
|---|---|---|
| `--motion-fast` | 90ms | hover, focus, press |
| `--motion-base` | 180ms | reveal, expand |
| `--motion-slow` | 300ms | route / view change |
| easing | `steps(3, end)` for reveals · `ease-out` for position | — |

**Rules:** nothing exceeds 300ms for a user-initiated action — past that it reads as lag, not polish. Reveals use a **stepped** easing rather than a smooth fade; the system is built from hard edges and a soft cross-fade contradicts it. Nothing animates on load except a loading indicator. `prefers-reduced-motion: reduce` **removes** transform and opacity animation — it does not merely shorten it.

---

## 2. Component inventory and composition

### 2.1 Inventory

**Primitives** — Button · IconButton · Input · Textarea · Select · Checkbox · Radio · Toggle · Link · Badge · Tag · Rule
**Containers** — Card · Panel · Rail · Modal · Drawer · Disclosure · Tabs
**Data** — Table · KeyValue · List · EmptyState
**Feedback** — InlineAlert · Banner · Toast · Progress · Skeleton
**Navigation** — TopBar · Breadcrumb · Stepper
**Band-specific** — **FidelityBadge** (Tier 1/2/3) · **BradleyRail** (readiness + nailed/hurt + routed cards) · **ProvenanceNote** (a `[CS:]` tag rendered in place)

The last three are not generic. They exist because every Band artifact must state its own fidelity and provenance on its face (UXI-04), and a component that does that is more reliable than a convention everyone has to remember.

### 2.2 Composition rules — what may contain what

The part most design systems leave implicit, which is why they drift. A system is defined as much by the **relationships** between the pieces as by the pieces.

| # | rule | why |
|---|---|---|
| C-01 | A **Modal** may not contain a Modal. Sequential decisions use a Stepper inside one Modal. | stacked modals have no coherent escape behaviour |
| C-02 | A **Tooltip** contains text only. No interactive children, ever. | a control you must hover to reach is unreachable by keyboard and by touch |
| C-03 | A **Disclosure** may contain interactive children but not a Table. | nested scroll regions inside collapsing containers break focus order |
| C-04 | A **Card** may not contain a Card. | nested grouping means the layout is wrong, not that you need another Card — and two stacked `6px 6px 0` shadows read as a rendering artefact |
| C-05 | A **Table** row may contain IconButtons, Badges and Tags. It may not contain an Input. Editing happens in a Drawer, a Modal, or a dedicated inline-edit row state. | inputs in rows destroy keyboard navigation of the table |
| C-06 | A **Banner** is page-scoped and appears once, at the top of the content area. An **InlineAlert** is section-scoped and may repeat. A **Toast** is transient and never carries information available nowhere else. | three feedback components with one job each; conflating them is how a failure gets missed |
| C-07 | A **Drawer** and a **Modal** never coexist on screen. | two competing escape targets |
| C-08 | Exactly one **primary** Button per view region. | two primaries mean the hierarchy is undecided |
| C-09 | **Tabs** switch views of the same object; they never change route-level context. Changing object is navigation. | tabs that navigate break the meaning of the back button |
| C-10 | A **destructive** action is never the default focus target and never sits flush against the primary action — minimum `--space-1` (28px) separation. | Fitts's law cuts both ways: easy to hit is easy to hit by accident |
| C-11 | The **BradleyRail** is always present on a prototype and always last in DOM order, never floated over content. | it must be readable with CSS off, and it must not obscure the thing it is grading |
| C-12 | A **FidelityBadge** appears above the fold and is never inside a dismissible container. | a fidelity claim that can be closed is a fidelity claim that will be |

### 2.3 Component contract — the eight requirements

Every component must define **all** of:

1. **Anatomy** — named parts.
2. **API** — props with types and defaults; boolean props default to the safe value.
3. **All eight states** (§3).
4. **Accessible name and role** — how assistive tech announces it.
5. **Keyboard contract** — every key it responds to.
6. **Content rules** — max length, truncation, zero-content behaviour.
7. **Do / Don't pair** — one of each.
8. **Responsive behaviour** — what it does below 768px.

A component missing any of the eight is not in the system yet, regardless of whether it is in the codebase.

---

## 3. State canon — all eight, non-negotiable

"We didn't design that state" is how production surfaces end up blank or stuck.

| state | requirement | Itten expression |
|---|---|---|
| **Default** | resting | `--border` + `--shadow` |
| **Hover** | pointer only; never the sole indicator of anything | shadow grows to `8px 8px 0` |
| **Focus** | always visible, never removed, never obscured (WCAG 2.4.7, 2.4.11) | `3px` `--ultramarine` outline at `2px` offset — 7.96:1 on paper, clears the 3:1 non-text minimum with room |
| **Active / pressed** | acknowledged under 100ms | translate 4px down-right, shadow to `--shadow-pressed` (SHD-05) |
| **Disabled** | explains **why**, via adjacent helper text | 40% opacity plus a stated reason; a disabled control with no reason is a dead end |
| **Loading** | preserves layout height so nothing shifts | Skeleton at `--grid` fill for content; stepped Progress for actions |
| **Error** | what happened, in plain language, and what to do next | `--vermillion` `3px` left border with `--ink` text. Never `--vermillion` text at body size — CLR-02 |
| **Empty** | says what goes here and offers the action that creates it | `--grid` wash, `--ink` text, one primary action |

**Empty and error are design work, not fallbacks.** They are the states users hit when they are most confused, and the ones most often left to whatever the framework does by default.

---

## 4. Interaction canon

### 4.1 Response-time budgets

| budget | required behaviour |
|---|---|
| **<100ms** | feels instantaneous — no feedback needed |
| **100ms–1s** | feels connected — no spinner, but state must change immediately on input |
| **1s–10s** | attention wanders — **determinate** progress indicator required |
| **>10s** | user switches task — background the work, notify on completion |

`[CS: HIGH — long-established HCI findings: Miller 1968; Card, Robertson & Mackinlay 1991; popularised by Nielsen.]`

**Rule:** a control acknowledges input within 100ms *even when the result takes longer*. Acknowledgement and result are separate obligations. The doodle render in this prototype is mocked at ~1.6s, which lands in the 1s–10s band and therefore **requires** a determinate indicator — see G3-29, currently open.

### 4.2 Destructive and reversible actions

- Confirmation only when the action is **irreversible**. Reversible actions get **undo** instead — undo beats a confirm dialog, because confirms earn click-through blindness.
- A confirm names the specific object — "Discard *Tuesday's doodle*?" — never "this item".
- The confirm button carries the verb, "Discard", never "OK".
- Discarding a doodle in this feature is deliberately **not** confirmed, because being wrong must be cheap (UXI-03). A confirm dialog would defeat the design.

### 4.3 Disclosure

- Progressive disclosure beats a modal. A modal interrupts; disclosure defers.
- Nothing hidden behind disclosure may be required in order to understand what is visible.
- A validation error is never hidden behind collapsed disclosure.

### 4.4 Feedback routing

| situation | pattern |
|---|---|
| Field validation | InlineAlert beside the field, **on blur** — not per keystroke |
| Form-level failure | summary at the top, focus moved to it, each error linked to its field |
| Background success | Toast, auto-dismiss |
| Background **failure** | InlineAlert or Banner — **never** an auto-dismissing Toast. A failure the user might miss must persist |
| System-wide condition | Banner |
| Provenance / confidence | ProvenanceNote, inline, never a tooltip |

### 4.5 Selection and bulk action

- Selection lives on the row **and** in a persistent count ("3 selected"), never only on the row.
- The bulk-action bar does not cover content and does not shift layout when it appears.
- Select-all applies to the **filtered** set, and says so.

### 4.6 Navigation and state

- Filter, sort and pagination state survive back-navigation.
- Anything that changes what the user sees is reflected in the URL.
- Lossy navigation warns before discarding unsaved input.

---

## 5. Accessibility standard — WCAG 2.2 AA

`[CS: HIGH — W3C WCAG 2.2 normative success criteria.]`

| criterion | requirement | Itten note |
|---|---|---|
| 1.4.3 Contrast (Min) | 4.5:1 body · 3:1 large (≥24px, or ≥18.66px bold) | the §1.1 table is the authority; ochre and cadmium fail on light ground |
| 1.4.11 Non-text Contrast | 3:1 for component boundaries, focus rings, meaningful graphics | `--ink` borders are 14.62:1 — no risk here |
| 1.4.1 Use of Colour | never the only means of conveying information | CLR-05 |
| 2.1.1 Keyboard | all functionality keyboard-reachable | |
| 2.1.2 No Keyboard Trap | focus can always leave | |
| 2.4.7 Focus Visible | indicator always visible | `--ultramarine` ring, §3 |
| 2.4.11 Focus Not Obscured | focused element not hidden by sticky chrome — **new in 2.2** | |
| 2.5.8 Target Size (Min) | **24×24 CSS px** minimum, or adequate spacing — **new in 2.2** | house floor is higher, below |
| 2.5.7 Dragging Movements | every drag has a single-pointer alternative — **new in 2.2** | |
| 1.4.10 Reflow | usable at 320px equivalent (400% zoom), no two-dimensional scrolling | |
| 1.4.12 Text Spacing | no content loss at increased line / letter / word spacing | Kalam at 28px line-height has headroom |
| 1.4.13 Content on Hover/Focus | dismissable, hoverable, persistent | |
| 3.3.1 / 3.3.3 Error Identification & Suggestion | errors named in text, with a correction suggested | |
| 3.3.7 Redundant Entry | never ask twice for the same information in one process — **new in 2.2** | |
| 4.1.2 Name, Role, Value | every control exposes all three | |

**House rules above the standard:**

- Primary touch targets **44×44px** minimum (Apple HIG; Material uses 48dp), not the 24px AA floor. On the 28px grid that is 28 + 2×7 padding, so it composes cleanly and there is no excuse.
- Every icon-only control has a visible tooltip **and** an accessible name.
- Every meaningful image has a text alternative; decorative images are explicitly `alt=""`.
- **A generated doodle is never decorative.** It is an interpretation of what a person said, so it always carries a text alternative naming what it is and what it was derived from (UXI-13).

---

## 6. Usability heuristics — Nielsen's 10, as system checks

`[CS: HIGH — Nielsen 1994.]`

| # | heuristic | the check here |
|---|---|---|
| 1 | Visibility of system status | every async action shows state within 100ms (§4.1) |
| 2 | Match to the real world | labels use the user's words, not internal system names |
| 3 | User control and freedom | undo over confirm (§4.2); every modal has a visible escape |
| 4 | Consistency and standards | one pattern per job; a second pattern needs a written reason |
| 5 | Error prevention | constrain input rather than validate after; keep destructive actions distinct (C-10) |
| 6 | Recognition over recall | show current filters and selection rather than expecting memory |
| 7 | Flexibility and efficiency | a keyboard path for every frequent action |
| 8 | Aesthetic and minimalist design | nothing on screen that does not serve the task |
| 9 | Help users recover | errors say what happened and what to do next (§3) |
| 10 | Help and documentation | contextual help at the point of difficulty |

---

## 7. Content and voice

- Sentence case for all UI text. Title Case only for proper nouns.
- Buttons are verbs: "Save entry", not "Submit" or "OK".
- No "please". No exclamation marks. No apologising for the system's behaviour. No emoji (SHD-06).
- Errors: what happened → why → what to do. Never a bare error code.
- Dates unambiguous — `11 Sep 2026`, never `09/11/26`.
- Numbers set in Space Mono, never Kalam (§1.3).
- Empty states: what goes here, plus the action that creates it.
- **Machine output is labelled as machine output.** A generated doodle, a transcription, an inference — each says so in `--type-label`. This is UXI-04 expressed as a copy rule.

---

## 8. Responsive and density

| breakpoint | width | behaviour |
|---|---|---|
| `--bp-sm` | <768px | single column · BradleyRail moves below content, still last in DOM (C-11) · Table becomes stacked KeyValue · grid wash to 14px |
| `--bp-md` | 768–1199px | two column · rail narrows, does not collapse |
| `--bp-lg` | ≥1200px | full layout · content plus a 320px rail |

**Rules:** a Table never scrolls horizontally below 768px — it changes representation. Horizontal scroll on a data table is a failure of the responsive design, not a feature of it. The 28px grid does not scale with the viewport; only the wash density changes, so the rhythm is identical at every size.

---

## 9. Acceptance Criteria — Gate 3: Are we making the thing right?

Settled by reading the shipped `<style>` / `<script>` or by executing the interaction. Unchecked means **not true**, not overlooked.

**Feature invariants — verified by execution**
- [x] G3-01 — Entry text displays alongside every doodle and is never the sole record · traces_to: UXI-01, UXI-08 · verified_by: DOM check post-render
- [x] G3-02 — No doodle on load; generation only on explicit per-entry action · traces_to: UXI-02 · verified_by: `svgsOnLoad` = 0, 1 after click
- [x] G3-03 — Render unavailable until per-entry consent given · traces_to: UXI-10 · verified_by: `disabled` true pre-consent, false post
- [x] G3-04 — Discard removes the doodle and leaves entry text intact, with no confirm dialog · traces_to: UXI-03, UXI-09, ds:4.2 · verified_by: post-discard SVG count 0, text unchanged
- [x] G3-05 — Voice transcript reviewable and editable before saving · traces_to: UXI-06 · verified_by: `readOnly` = false
- [x] G3-25 — No engagement mechanics: no streaks, counters, notifications, reminders, share · traces_to: UXI-05 · verified_by: `grep -icE 'streak|day [0-9]+ of|notification|reminder'` = 0 and `grep -icE '>[^<]*\b(share|post|publish|send to)\b'` = 0
- [x] G3-26 — An entry saves and stays complete without a doodle; nothing nags toward generation · traces_to: UXI-07 · verified_by: the save path requires only non-empty text

**Self-disclosure — verified by grep**
- [x] G3-06 — FidelityBadge "Tier 1 · Concept" visible above the fold and not dismissible · traces_to: UXI-04, ds:2.2 C-12 · verified_by: `grep -c 'Tier 1'` ≥ 1, no dismiss control in that block
- [x] G3-07 — "No reaction data collected" statement exists, visually distinct from the fidelity label · traces_to: UXI-04 · verified_by: a separate bordered block with its own heading
- [x] G3-08 — No copy contradicts G3-07 by claiming data is saved or timestamped · traces_to: UXI-04 · verified_by: `grep -c 'verbatim, timestamped'` = 0
- [x] G3-09 — Every ratio printed matches its source document · traces_to: §1 success metrics · verified_by: 58.6% present; 57.1% appears only as explicitly superseded
- [x] G3-10 — All seed data fictional and `[TEST DATA]` tagged · traces_to: §11 · verified_by: `grep -c '\[TEST DATA\]'` = 7
- [x] G3-11 — No clinical / therapeutic / diagnostic language · traces_to: §4 non-goals · verified_by: the regex returns only the disclaimer sentence
- [x] G3-33 — Machine-generated output is labelled as machine output wherever it appears · traces_to: UXI-04, ds:7 · verified_by: the doodle block carries a `--type-label` provenance line

**Design-system conformance — §§1–8**
- [x] G3-12 — Palette defined once in `:root`; no ad-hoc hex anywhere else · traces_to: ds:1.1 · verified_by: `grep -n '#D8472B'` returns only the `:root` definition
- [x] G3-13 — 28px grid, hard opaque shadows, zero border-radius, no emoji · traces_to: ds:1.2, ds:1.4 · verified_by: `grep -c 'border-radius'` = 0; shadow declarations carry no blur and no alpha; emoji scan clean
- [x] G3-14 — Space Mono and Kalam actually load · traces_to: ds:1.3 · verified_by: `document.fonts.check()` true for both families
- [ ] G3-34 — **CLR-01 holds: no `--ochre` or `--cadmium` text on `--paper` or `--card`** · traces_to: ds:1.1, `OPEN.md` R-11 · verified_by: a per-declaration audit of every colour / background pair — **never run. The measured ratios are 2.10:1 and 1.49:1, so a single violation is an outright AA failure, and nothing has checked.**
- [ ] G3-35 — CLR-02 holds: `--vermillion` and `--green-earth` carry no text below 24px / 18.66px-bold · traces_to: ds:1.1, `OPEN.md` R-11 · verified_by: the same audit — **never run**
- [ ] G3-27 — Every interactive component defines all eight states of §3 · traces_to: ds:3, `OPEN.md` R-11 · verified_by: a state audit per component — **never done; the prototype has no loading, error or disabled states designed at all**
- [ ] G3-28 — Composition rules C-01…C-12 hold · traces_to: ds:2.2, `OPEN.md` R-11 · verified_by: a composition audit — **not run. The prototype is too small to violate most of them, which is not the same as conforming.**
- [ ] G3-29 — §4.1 budgets met, with acknowledgement inside 100ms and a determinate indicator above 1s · traces_to: ds:4.1, `OPEN.md` R-11 · verified_by: instrumentation — **not measured; the mocked ~1.6s render has no progress indicator, which §4.1 requires**
- [ ] G3-36 — SHD-05 pressed state implemented: 4px shift plus shortened shadow, constant silhouette · traces_to: ds:1.4, ds:3, `OPEN.md` R-11 · verified_by: an `:active` rule — **not implemented**

**Accessibility — UXI-11..14 and §5**
- [ ] G3-18 — Every shipped colour pair audited against §1.1 at 4.5:1 / 3:1 · traces_to: UXI-11, ds:5, `OPEN.md` R-12 · verified_by: the audit in G3-34 / G3-35 — **never run**
- [ ] G3-19 — Full keyboard operation of capture, consent, render, discard (WCAG 2.1.1) · traces_to: UXI-12, ds:5, `OPEN.md` R-12 · verified_by: a keyboard pass — **never run**
- [ ] G3-20 — Every doodle carries a text alternative naming what it is and what it derives from · traces_to: UXI-13, ds:5, `OPEN.md` R-12 · verified_by: `alt` / `aria-label` on every doodle SVG — **not implemented**
- [ ] G3-21 — No state conveyed by colour alone (WCAG 1.4.1, CLR-05) · traces_to: UXI-14, ds:1.1, `OPEN.md` R-12 · verified_by: a review — **never run**
- [ ] G3-30 — Targets ≥24×24px (WCAG 2.5.8); house floor 44×44px · traces_to: ds:5, `OPEN.md` R-12 · verified_by: measurement — **never run**
- [ ] G3-31 — Focus ring visible and not obscured (WCAG 2.4.7, 2.4.11) · traces_to: ds:5, ds:3, `OPEN.md` R-12 · verified_by: a focus audit — **never run; no `--ultramarine` focus ring is defined, so the browser default is doing this job by accident**
- [ ] G3-32 — `prefers-reduced-motion` respected by removing, not shortening, animation · traces_to: ds:1.5, `OPEN.md` R-12 · verified_by: `grep -c 'prefers-reduced-motion'` = 0 — **not implemented**

**Measurement and open obligations**
- [x] G3-15 — SC-003 (time to completed entry) instrumented · traces_to: §12 · verified_by: returned 1.8s on a live save; labelled n=1, not a finding
- [ ] G3-16 — SC-001 measured (#13a semantic match) · traces_to: §12, `OPEN.md` H-01 · verified_by: a test run — **DEFERRED to Tier 2; structurally unmeasurable on pre-drawn doodles**
- [ ] G3-17 — SC-002 measured (#13b affective register) · traces_to: §12, `OPEN.md` H-01 · verified_by: a test run — **DEFERRED to Tier 2**
- [ ] G3-22 — Art. 9 consent copy reviewed by someone qualified · traces_to: §8 constraints, `OPEN.md` H-02 · verified_by: a named reviewer — **open**
- [ ] G3-23 — Retention / deletion SLA defined and sourced · traces_to: §8, `OPEN.md` H-03 · verified_by: a specified timing — **open**
- [ ] G3-24 — Any usability or accessibility testing run with a real person · traces_to: §12 · verified_by: participant count > 0 — **zero participants**

Count computed, never asserted:

```bash
awk '/^## 9\. Acceptance Criteria/{f=1;next} /^## /{f=0} f && /^- \[ \]/{c++} END{print c+0}' design.md
```

### What adding the real system did to this gate

It made it **substantially redder**, and that is the point.

Before: **26 criteria, 17 checked, 9 open.** After: **36 criteria, 18 checked, 18 open** — the open count doubled. Ten criteria exist now that did not exist an hour ago (G3-27…G3-36: CLR-01 and CLR-02 conformance, the eight states, composition, response budgets, the pressed state, target size, focus visibility, reduced motion, machine-output labelling), and nine of the ten are open.

**None of them are new defects.** Every one was already true of this prototype. They were invisible while `design.md` only tested the things the build happened to do well.

`G3-34` is the sharpest example. The Itten palette contains two colours that fail AA on the light ground by a wide margin — 2.10:1 and 1.49:1 — and a designer looking at ochre on paper sees a perfectly pleasant warm label. Nothing in the previous version of this file could have caught that, because the previous version did not know the numbers. **The number is what turns a preference into a rule.**

A gate can only catch what it names.
