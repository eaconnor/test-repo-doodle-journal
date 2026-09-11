---
name: "check-gates"
description: "Mechanical three-gate check. Runs ./check-gates.sh and hard-stops if Gate 1 (ux.md), Gate 2 (vision.md), or Gate 3 (design.md) has unchecked acceptance criteria. Registered as a mandatory before_plan / before_tasks / before_implement hook in .specify/extensions.yml."
user-invocable: true
disable-model-invocation: false
---

# check-gates

Run the script. Report its output verbatim. Obey its exit code.

## Steps

1. Resolve the project root as **the nearest ancestor directory containing both `.specify/` and `check-gates.sh`**, starting from the current directory and walking up.

   Do **not** use `git rev-parse --show-toplevel` as the primary method. If this project sits inside a larger git repository — which it does whenever the project folder has no `.git` of its own — `git rev-parse` returns the *parent* repo root, and the script then runs from the wrong directory against files that are not this project's gates. Verified 2026-09-11: in `test-repo-doodle-journal`, `git rev-parse --show-toplevel` returned `/…/Bethproto`, the parent.

   A gate check that runs in the wrong directory is worse than no gate check, because it exits with a confident code either way.

2. Verify `check-gates.sh` exists in the resolved root before running it. If it does not, report that as a BLOCKED condition — a missing gate script is a failed gate, never a skipped one.

3. From that directory run `./check-gates.sh`. The script reads `ux.md`, `vision.md`, and `design.md` by relative path, so it reports nonsense from anywhere else.
3. Report the script's stdout verbatim. Do not paraphrase it and do not re-derive the verdict by reading the markdown yourself.

## The exit code is the verdict, not your judgment

- **Exit 0** — all three gates pass. Say so and continue the calling workflow.
- **Exit non-zero** — emit exactly this, then stop:

```
BLOCKED — three-gate check failed.
[verbatim script output]
Fix the unchecked acceptance criteria above and re-run. Not proceeding to plan, tasks, or implement.
```

There is no discretion here. A red gate is not a consideration to note and design around. Do not offer to proceed anyway, do not plan "provisionally," do not downgrade the failure to an assumption and carry on. The only ways past a red gate are checked boxes or an override a human has logged in `vision.md`'s Decision Log.

## Why this is a hook and not a norm

The constitution used to carry the sentence "run `./check-gates.sh` before `/speckit-plan`." Prose in a constitution is something an agent may read and may act on. A hook in `.specify/extensions.yml` with `optional: false` is something `speckit-plan` is instructed to execute and block on. That difference is the entire finding.
