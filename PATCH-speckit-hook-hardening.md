# PATCH — two hook-hardening fixes for `acp-core-main-3`'s `speckit-*` skills

**Status: proposed, not applied.** Nothing in this file has touched `acp-core-main-3`.
This is the deliverable from testing the hook mechanism in this repo — the whole point of
using doodle-journal as the test loop — and it names exactly what to change, where, so
someone with authority over that repo can decide whether to apply it.

## Why this exists

`acp-core-main-3`'s `.claude/skills/speckit-{plan,tasks,implement}/SKILL.md` files are the
mechanism that actually fires (or doesn't fire) any mandatory gate — including the
Research-Gate check named in the constitution's Principle VII. This repo's copies of the
same three files were hardened against two failure modes found while building the
three-gate framework here. Those fixes were never carried back. Diffed directly,
2026-09-17 — `[CS: VERIFIED]`.

## Bug 1 — a YAML typo silently deletes every mandatory gate

**Current (`acp-core-main-3`), identical at all 6 sites:**
> If the YAML cannot be parsed or is invalid, skip hook checking silently and continue normally.

A malformed `.specify/extensions.yml` — one bad indent, one stray character — makes every
hook disappear with no warning, mandatory ones included. The failure looks like nothing
happened, because nothing did.

**Fixed (this repo):**
> If the YAML cannot be parsed or is invalid, do not skip silently: tell the user that
> `.specify/extensions.yml` could not be read (include the parser error) and that no hooks
> were checked, including any mandatory (`optional: false`) hooks registered there, then
> continue [normally | to the Completion Report].

## Bug 2 — nothing requires the mandatory hook to actually run

**Current (`acp-core-main-3`):** the mandatory-hook block ends right after the
`EXECUTE_COMMAND:` line. Nothing tells the agent it must wait for a result — emitting the
text block satisfies the instruction on its face, whether or not the command was ever run.

**Fixed (this repo):** one line added after the closing fence:
> After emitting the block above you MUST actually invoke the hook and wait for it to
> finish before continuing. Run it the same way you would run the command yourself in this
> agent/session (the invocation may differ from the literal `{command}` id shown above,
> e.g. a skills-mode agent runs it as `/skill:speckit-...` or `$speckit-...`). Emitting the
> block alone does not run the hook.

This is the same failure class the 12-agent controlled test found (test-repo-nav-update's
README) — prose stated is not prose obeyed — except here it is one layer down, inside the
tool that is supposed to be the enforcement mechanism itself.

## The six sites, exact

Both bugs appear at every `before_*`/`after_*` hook-check pair in all three skills. Bug 1
patches a single existing line; Bug 2 inserts one new line after the mandatory-hook code
fence. Line numbers are `acp-core-main-3`'s current file as of this diff.

| file | block | bug 1 — line to replace | bug 2 — insert after |
|---|---|---|---|
| `speckit-plan/SKILL.md` | `before_plan` | line 27 | the fence closing the `before_plan` mandatory-hook block (~line 52) |
| `speckit-plan/SKILL.md` | `after_plan` | line 87 | the fence closing the `after_plan` mandatory-hook block (~line 101) |
| `speckit-tasks/SKILL.md` | `before_tasks` | line 27 | the fence closing the `before_tasks` mandatory-hook block (~line 52) |
| `speckit-tasks/SKILL.md` | `after_tasks` | line 98 | the fence closing the `after_tasks` mandatory-hook block (~line 112) |
| `speckit-implement/SKILL.md` | `before_implement` | line 27 | the fence closing the `before_implement` mandatory-hook block (~line 52) |
| `speckit-implement/SKILL.md` | `after_implement` | line 188 | the fence closing the `after_implement` mandatory-hook block (~line 202) |

**Bug 1 replacement, `before_*` sites (line 27 in all three files):**
```diff
- If the YAML cannot be parsed or is invalid, skip hook checking silently and continue normally.
+ If the YAML cannot be parsed or is invalid, do not skip silently: tell the user that `.specify/extensions.yml` could not be read (include the parser error) and that no hooks were checked, including any mandatory (`optional: false`) hooks registered there, then continue normally.
```

**Bug 1 replacement, `after_*` sites (lines 87 / 98 / 188 respectively):**
```diff
- If the YAML cannot be parsed or is invalid, skip hook checking silently and continue to the Completion Report.
+ If the YAML cannot be parsed or is invalid, do not skip silently: tell the user that `.specify/extensions.yml` could not be read (include the parser error) and that no hooks were checked, including any mandatory (`optional: false`) hooks registered there, then continue to the Completion Report.
```

**Bug 2 insertion, all 6 sites** — directly after the closing ` ``` ` of the mandatory-hook
block, before the next `- **Optional hook**` bullet:
```diff
      EXECUTE_COMMAND: {command}
      ```
+     After emitting the block above you MUST actually invoke the hook and wait for it to finish before continuing. Run it the same way you would run the command yourself in this agent/session (the invocation may differ from the literal `{command}` id shown above, e.g. a skills-mode agent runs it as `/skill:speckit-...` or `$speckit-...`). Emitting the block alone does not run the hook.
    - **Optional hook** (`optional: true`):
```

## How to verify the patch, once applied

1. `diff` the three patched files against this repo's copies — the `before_*`/`after_*`
   blocks should now match exactly (the `Automatic Pre-Hook` vs `Automatic Hook` label
   difference between the two `before`/`after` variants is pre-existing and not part of
   this patch).
2. Deliberately corrupt `.specify/extensions.yml` (one bad indent) and run `/speckit-plan`.
   **Before the patch:** it proceeds silently. **After:** it reports the parse error and
   names which mandatory hooks went unchecked.
3. Register a mandatory hook whose command is a script that writes a sentinel file, run the
   workflow stage, and confirm the sentinel file exists — not just that the hook text was
   printed.

## What this does not do

Does not touch `acp-core-main-3`. Does not submit anything upstream. Does not resolve
whether Principle VII's two named pending TODOs (`plan-template.md`'s Constitution Check,
`speckit-specify/SKILL.md`'s clarification guidance) get actioned — that is a separate,
larger piece of work this patch does not attempt.
