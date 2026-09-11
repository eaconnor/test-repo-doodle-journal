# Test Repo — Doodle Journal

Second wiring test for the three-gate framework (`ux.md` / `vision.md` / `design.md` + constitution + `check-gates.sh`), this time driven end-to-end by the Band Protocol prototyping pipeline instead of hand-written content.

**Concept under test:** a journaling app that turns a voice or text entry into a doodle. Tier 1 / lo-fi, internal audience, no real source docs — web-only scout, all seed data fictional and `[TEST DATA]`.

**What is actually being tested here is the plumbing, not the concept.** Two questions: does the gate script get invoked by a real `/speckit-plan` run, and does pipeline output fit the gate template or fight it.

## How this is structured — read this first

Each document is canonical for one domain. Three scripts check the joins.

```
Intent Specs/doodle-journal.md   ← CANONICAL for this feature's intent. 16 sections.
                                    §5 UX intent = UXI-01..UXI-14
                                    §13 open questions -> points at OPEN.md
                                    §14 decision log = the single record of decisions

ux.md       ← CANONICAL for the research corpus, positioning, audience, research plan.
              §§1-8 content, §9 = Gate 1 acceptance criteria.

design.md   ← CANONICAL for the design system (Itten), the interaction canon, and the
              usability/accessibility standard. §§1-8 content, §9 = Gate 3 criteria.

vision.md   ← DERIVED checklist only. Gate 2. Direction and scope stay in the intent spec.

OPEN.md     ← the register: every open question, typed HUMAN / RESEARCH / ACCEPTED
```

**Why this shape, after two passes at it.** The first pass made all three gate files thin derived checklists, on the reasoning that judgment belongs in one canonical place. That was right about *this feature's* intent and wrong about everything else: a design system and a research corpus are not derived from a feature spec — they outlive it, and they apply to the next prototype too. So they are canonical in their own right, and each still ends in the `## 9. Acceptance Criteria` block the scripts read. Different domains, not duplication.

| script | question it answers | exit |
|---|---|---|
| `./check-gates.sh` | are the gate boxes ticked? | 1 if any open, or if a gate file has no parsable criteria |
| `./check-blocked.sh` | are we waiting on a *person*? | 2 if a HUMAN row stands |
| `./check-trace.sh` | have the criteria drifted from what they claim to enforce? | 4 on a broken or orphaned trace |
| `python3 scripts/check-design.py` | does the **build** actually obey the design system? | 6 on a violation · 7 if only unresolved pairs remain |
| `python3 scripts/check-risk.py <dest>` | what is the risk of shipping **to a named destination**? | 9 on a ship-blocking hazard · 2 if no destination given |
| `./check-eng.sh` | the five gates eng owns | 10 if the build can harm a user · 11 if something is off-roadmap |
| `./check-value.sh` | is the contribution register well-formed and honest? | 13 if malformed or if it records no costs |
| `python3 scripts/ux-score.py` | conformance baseline, ceiling, and the work list | 0 — reports, never blocks |

Every exit code is distinct on purpose, so a caller can tell "a box is unticked" from "a person owes us an answer" from "a criterion points at nothing" from "this build can hurt someone." A single pass/fail would collapse all of those into one number and lose the only information that tells you what to do next.

**The split that makes this usable by engineering.** `check-eng.sh` divides Gate 3 into **FLOOR** — accessibility, data integrity, lawfulness, security, never gated on problem validation — and **FIT** — polish that only pays off if the concept survives. "Don't build until Gate 1 passes" is right for FIT and dangerously wrong for FLOOR; you do not wait for a reaction test to label a form field. Eng gets a hard CI failure on FLOOR (exit 10) and a visible warning on everything else.

**`VALUE.md`** is the register of what research and design actually contributed, with the counterfactual stated for every row and each one labelled `EVIDENCED` or `CLAIMED`. `check-value.sh` fails the register if it contains **no cost or zero-value rows** — because a value register with only wins in it is a case study, and a case study is what the file exists to replace.

`scripts/contrast.py` is not a gate script — it computes the WCAG contrast table in `design.md` ds:1.1, so those ratios are reproducible rather than asserted.

**Two silent failures this restructure caused, both caught by the scripts and worth knowing about:**

1. `check-gates.sh` anchored on `/^## Acceptance Criteria/`. Once the heading became `## 9. Acceptance Criteria` the awk matched nothing, counted zero unchecked boxes, and printed a confident **PASS**. A false green is worse than a false red. The script now accepts an optional section number and **fails when a gate file yields zero parsable criteria**, rather than treating "I found nothing" as "nothing is wrong."
2. `check-trace.sh` resolved every `§N` against the intent spec. Once `ux.md` and `design.md` had their own §1–§8, `§5` was ambiguous — and it resolved against the intent spec either way, so a wrong pointer would have passed. Local references are now `ds:N.N` and cannot collide. Both directions are validated, and the checks were tested against deliberately broken pointers before being trusted.

**Reference syntax**, used in every `traces_to:` field: `§N` = intent spec · `ds:N.N` = a section of the file itself · `UXI-##` = an intent spec §5 requirement · `CLR-##` / `C-##` / `SHD-##` = a design-system rule · `H-##` / `R-##` / `A-##` = an `OPEN.md` row.

## Reading order

1. `Intent Specs/doodle-journal.md` — **canonical.** Start at §0 agent summary, then §5 UX intent
2. `.specify/memory/constitution.md` — the three gates and the five-link enforcement chain
3. `scout/00-index.md` — evidence index; **read `scout/03` first**, it is load-bearing and it cuts against the concept
4. `briefs/doodle-journal.brief.md` — 29 tagged claims, the falsifiability table, the Critic Pass 1 resolutions
5. `OPEN.md` — every unresolved thing, typed HUMAN / RESEARCH / ACCEPTED
6. `ux.md` — the research corpus, positioning, audience and research plan; Gate 1 at §9 (18 of 24 checked). **ds:4.3 is the load-bearing section and it argues against the concept**
7. `vision.md` — Gate 2 derived checklist (9 of 11 checked)
8. `design.md` — the Itten design system, interaction canon and accessibility standard; Gate 3 at §9 (18 of 36 checked)
9. `spec.md` — the spec-kit-shaped view: prioritized stories, `FR-###`, `SC-###`
10. `prototypes/doodle-journal/critic-pass-1.md` → `critic-pass-2.md` — the review record
11. `prototypes/doodle-journal/doodle-journal.html` — the Tier 1 prototype. Open it directly in a browser. No model call and no backend; it does load Space Mono and Kalam from Google Fonts, which is its only external request

## Prototype location

Everything for this prototype lives in one folder, `prototypes/doodle-journal/`, matching the `prototypes/<concept-name>/` convention:

```
prototypes/doodle-journal/
  doodle-journal.html    ← the build (self-contained, open in any browser)
  critic-pass-1.md       ← pre-build scorecard + punch list
  critic-pass-2.md       ← post-build re-score + delta table vs. pass 1
  SOURCES.md             ← provenance: what carries the argument, what not to cite
```

The prototype is **not** a stand-alone deliverable and should not be sent onward by itself. It renders a red "No data has been collected" panel above the fold precisely because the HTML is the artifact most likely to be forwarded without its brief, and the numbers on it are evidence *against* the concept — not results.

## What's ours and what isn't

- `.specify/` and `.claude/skills/speckit-*` are **vendored from [github/spec-kit](https://github.com/github/spec-kit)** — not original work here. They are committed rather than gitignored on purpose: the `speckit-*` skills are the layer that reads `.specify/extensions.yml`, so enforcement only travels with the repo if they do.
- `.claude/skills/check-gates/`, `check-gates.sh`, the gate files (`ux.md` / `vision.md` / `design.md`), the constitution, the brief, the scout corpus, the critic passes and the prototype are original.
- Licensed MIT — see `LICENSE`. Fork it, teach it, build on it.

## Setup on a fresh clone — one required step

`.specify/feature.json` is **not in this repo**, and cannot be: spec-kit's own `.specify/.gitignore` treats it as machine-local state. Without it, `get_feature_paths` hard-errors, `setup-plan.sh` exits 1, and `/speckit-plan` dies at step 1 of its Outline — before it ever reaches the constitution or the gate. So after cloning, run one of:

```bash
printf '{\n  "feature_directory": "."\n}\n' > .specify/feature.json
```

or set it per-shell instead:

```bash
export SPECIFY_FEATURE_DIRECTORY=.
```

Either points spec-kit at the repo root as the feature directory, which is where this project's `spec.md` / `plan.md` / `tasks.md` would live. Then:

```bash
./check-gates.sh          # exits 1 — gates are red on purpose
```

This is worth understanding rather than just running, because it is the subtlest of the five failures this repo exists to document: **a gate that is never reached is not a gate.** The gate check can be perfectly configured and still never fire, because the workflow dies upstream of it. Nothing about that failure looks like a gate failure — it looks like a path error.

## Gate state

Red, for real reasons. `./check-gates.sh` exits 1 — **6 open in Gate 1, 2 in Gate 2, 18 in Gate 3.** `[A]`+`[?]` = **58.6%** of tagged claims (17 of 29, grep-verified) — nearly twice the 30% threshold. Nothing here is checked to make the script go green.

The open count went **up** when `ux.md` and `design.md` gained real content: Gate 1 from 2 open to 6, Gate 3 from 9 to 18. None of those are new defects. Writing down a measured contrast table surfaced that two palette colours fail AA on the light ground (2.10:1 and 1.49:1) and that nothing had ever checked. Writing down a positioning statement and three personas turned four unstated assumptions into four testable claims nobody has tested. **A gate can only catch what it names**, so naming more made it redder — and those are the same event.

## How this repo deliberately differs from `test-repo-nav-update`

Each difference is a fix for something that broke over there:

| Difference | Why |
|---|---|
| `.claude/` is **tracked**, not gitignored | In nav-update `.gitignore` was `.claude/`, so the `speckit-*` skills — the layer that reads `extensions.yml` and runs the gate check — weren't in the pushed repo at all. Enforcement has to travel with the repo or it isn't enforcement. Tracking it is also what made the skills auto-discoverable to a live session. |
| `.specify/extensions.yml` exists | The only mechanical `before_plan` hook slot `speckit-plan` actually reads. In nav-update it was missing, so nothing connected the script to the workflow except one line of constitution prose. |
| `.specify/feature.json` exists | Without it `setup-plan.sh` exits 1 and `/speckit-plan` dies at step 1 of its Outline — before it ever reads the constitution. A gate that is never reached is not a gate. |
| `/check-gates` skill resolves the root by walking up for `.specify/` + `check-gates.sh` | Not via `git rev-parse --show-toplevel`, which returns the *parent* repo when this folder has no `.git` of its own — the script then runs in the wrong directory and exits with a confident code either way. Caught during a live run, 2026-09-11. |
| `spec.md` matches `.specify/templates/spec-template.md` | nav-update's `spec.md` was hand-written as `What / Why / Open Questions`, a shape no `/speckit-*` command recognizes. |
| No `plan.md` / `tasks.md` stubs | They exist in nav-update as two-line stubs saying "blocked." `/speckit-plan` and `/speckit-tasks` generate these; hand-stubbing them adds nothing and makes `setup-plan.sh` skip its own template copy. |

## What to break

Check the six open boxes in `ux.md` without doing the work they describe, then run `./check-gates.sh` and `/speckit-plan`. The script will go green and planning will proceed. That is the honest limit of this design: the gate is only as good as the honesty of whoever ticks the box. The script checks that a box is ticked — it cannot check that the claim beside it is true. Only a human reading the evidence can do that, which is the finding, not a bug to fix.
