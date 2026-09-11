# Test Repo — Doodle Journal

Second wiring test for the three-gate framework (`ux.md` / `vision.md` / `design.md` + constitution + `check-gates.sh`), this time driven end-to-end by the Band Protocol prototyping pipeline instead of hand-written content.

**Concept under test:** a journaling app that turns a voice or text entry into a doodle. Tier 1 / lo-fi, internal audience, no real source docs — web-only scout, all seed data fictional and `[TEST DATA]`.

**What is actually being tested here is the plumbing, not the concept.** Two questions: does the gate script get invoked by a real `/speckit-plan` run, and does pipeline output fit the gate template or fight it.

## Reading order

1. `.specify/memory/constitution.md` — the three gates, the five-link enforcement chain, and this repo's honesty rules
2. `scout/00-index.md` — evidence index; **read `scout/03` first**, it is load-bearing and it cuts against the concept
3. `briefs/doodle-journal.brief.md` — the three-gate brief, 29 tagged claims, the falsifiability table, and the Critic Pass 1 resolutions
4. `ux.md` — Gate 1 (2 of 6 boxes open, on purpose)
5. `vision.md` — Gate 2 (2 of 6 boxes open) + Decision Log
6. `design.md` — Gate 3 (written from the post-build critic)
7. `spec.md` — the spec-kit-shaped view: prioritized stories, `FR-###`, `SC-###`
8. `prototypes/doodle-journal/critic-pass-1.md` → `critic-pass-2.md` — the review record
9. `prototypes/doodle-journal/doodle-journal.html` — the Tier 1 prototype. Open it directly in a browser; it is self-contained, with no network calls, no CDN links, and no model calls

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

Red, for real reasons. `./check-gates.sh` exits 1. `[A]`+`[?]` = **58.6%** of tagged claims (17 of 29, grep-verified) — nearly twice the 30% threshold. Nothing here is checked to make the script go green.

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

Check the two open boxes in `ux.md` without doing the work they describe, then run `./check-gates.sh` and `/speckit-plan`. The script will go green and planning will proceed. That is the honest limit of this design: the gate is only as good as the honesty of whoever ticks the box. The script checks that a box is ticked — it cannot check that the claim beside it is true. Only a human reading the evidence can do that, which is the finding, not a bug to fix.
