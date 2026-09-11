# Constitution — Doodle Journal (Test Repo)

Second wiring test for the three-gate framework. Trimmed on purpose: gate rubric and enforcement only.

## Gates

- **Gate 1 — Understanding.** Do we understand the problem? Checked against `ux.md`'s Acceptance Criteria.
- **Gate 2 — Right Thing.** Does this advance the vision? Checked against `vision.md`'s Acceptance Criteria.
- **Gate 3 — Right Build.** Is it usable, accessible, and honest about its fidelity? Checked against `design.md`'s Acceptance Criteria.

A spec does not move to "Ready to Build" without all three gates showing PASS, or an override explicitly logged in `vision.md`'s Decision Log by a human.

## Enforcement

`./check-gates.sh` reads the Acceptance Criteria checkboxes in `ux.md`, `vision.md`, and `design.md` and exits non-zero if any gate has an unchecked box or a missing file. No file, no pass, no proceeding.

It is wired in mechanically, by this chain — all five links required:

1. `.specify/extensions.yml` registers `check-gates` under `hooks.before_plan`, `hooks.before_tasks`, and `hooks.before_implement` with `optional: false`, and with **no** `condition:` field (the skills skip conditioned hooks and defer to a HookExecutor that does not exist here, so a condition silently disables the gate).
2. Each `speckit-*` skill reads `.specify/extensions.yml` in its Pre-Execution Checks and is instructed to `EXECUTE_COMMAND` every mandatory hook and wait for the result.
3. `/check-gates` (`.claude/skills/check-gates/SKILL.md`) runs the script from the repo root and hard-stops on non-zero exit.
4. A resolvable feature context exists — `.specify/feature.json`. Without it `setup-plan.sh` exits 1 and `/speckit-plan` dies at step 1 of its Outline, before it ever reads this file. A gate that is never reached is not a gate.
5. `.claude/` is **tracked in git, not ignored.** In the nav-update test repo `.gitignore` was `.claude/`, so the skills that read `extensions.yml` did not exist in the pushed repo and enforcement was machine-local by accident. Verified 2026-09-11.

The gate is a stop, not a consideration. Not proceeding "provisionally," not downgrading a red gate to an assumption.

## Honesty Rules For This Repo

- **All seed data is fictional and tagged `[TEST DATA]`.** No real people, no real entries, no invented statistics presented as research findings. An ungrounded claim is `[CS: UNKNOWN]` or it does not ship.
- **No therapeutic or clinical claims.** This concept borders art therapy and expressive-writing research. The prototype may not claim mental-health benefit, diagnose mood, or imply clinical validation. Cite the tradition; do not inherit its authority.
- **Fidelity is stated on the artifact.** Tier 1 / Concept means the prototype says so on its face.

## No Giant Repo Rule

Every file here stays small and networked. If a section outgrows a screen, it becomes a linked mini-doc.
