---
name: "check-open"
description: "Reads OPEN.md and reports whether we are blocked on a human decision, short on research, or clear. Hard-stops on human-owned decisions. Registered as a mandatory before_plan / before_tasks / before_implement hook in .specify/extensions.yml."
user-invocable: true
disable-model-invocation: false
---

# check-open

Run the script. Obey its exit code. Report the human questions verbatim to the user.

## Steps

1. Resolve the project root as the nearest ancestor directory containing both `.specify/` and `OPEN.md`, walking up from the current directory. Do **not** use `git rev-parse --show-toplevel` — it returns the parent repo whenever this project has no `.git` of its own, and the script would then read the wrong register.
2. Verify `check-blocked.sh` and `OPEN.md` exist in that root. If either is missing, that is a BLOCKED condition, not a skip — a missing register is not an empty register.
3. Run `./check-blocked.sh` from that root.

## Exit codes are the interface

| exit | meaning | what you do |
|---|---|---|
| `0` | No human blockers. Research gaps may remain. | Say so, note the research-gap count, continue the calling workflow. |
| `2` | **Blocked on a human decision.** | **Stop.** Report the listed questions and their owners verbatim. Do not continue. |
| `3` | `OPEN.md` missing or unparsable. | Stop. Report it as a failure of the register, not as an absence of risk. |

## On exit 2, emit exactly this and stop

```
BLOCKED ON A HUMAN DECISION.
[verbatim script output]
These are not questions I can answer by researching harder. Each one needs the
named owner. Not proceeding to plan, tasks, or implement.
```

## The rule this exists to enforce

There are two completely different kinds of stuck, and conflating them is how an agent causes real damage:

- **Evidence uncertainty** — the answer exists, nobody has found it. Legitimate to proceed flagged, build at low fidelity, and refuse to claim validation.
- **Decision uncertainty** — the answer does not exist anywhere; a person has to *choose*. There is no research that resolves it, and no default that is safe to assume.

A `HUMAN` row means someone owes an answer. Picking a sensible-looking default on a `HUMAN` row is not helpfulness — it is quietly making someone else's decision and then building on it, which is far harder to unwind than simply having asked. If the owner field says `UNASSIGNED`, the first question is who owns it.

Do not "note it and carry on." Do not resolve it by inference from surrounding context. Do not treat a long-open row as tacit approval; age is not consent.
