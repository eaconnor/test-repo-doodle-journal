# WAIVERS.md — the override ledger

**Gates here do not stop work. They require a signature.**

Any gate, check or never event can be bypassed. What cannot happen is bypassing one *silently*. A waiver records who proceeded, past what, why, and **what they predicted it would cost if they were wrong** — and later, what it actually cost.

Read by `./check-waivers.sh`.

## Why it works this way

A gate that idles an engineer for six weeks gets removed, and it deserves to be. Design and engineering must be able to work on other things while research runs. The problem was never people proceeding — it was people proceeding **without knowing what they were accepting**, and nobody being able to tell afterwards whether the gate was right.

So this ledger does three jobs:

1. **Informed consent.** The risk is named at the moment of the decision, by the person taking it.
2. **Attribution.** A bypass has a name and a date on it. Not to blame anyone — so that the reasoning survives the person leaving.
3. **Calibration, which is the real prize.** Every waiver predicts a cost. Later, the actual cost gets recorded. Over time that produces evidence about whether the gate is worth obeying — and **a gate whose authority comes from evidence is worth more than one whose authority comes from policy.** If nine waivers out of twelve turn out fine, the gate is too strict and should be loosened. That is a finding, not an embarrassment.

**A waiver is not a failure.** Most should be vindicated. If none ever are, the gates are theatre.

## Status values

| status | meaning |
|---|---|
| `PENDING` | proceeded; outcome not yet known |
| `VINDICATED` | the bypass was fine. Cost ≈ 0. **Evidence the gate was too strict here** |
| `COSTLY` | it bit. Actual cost recorded. Evidence the gate was right |
| `FATAL` | it caused a never event or shipped harm. Investigate, do not score |

## Waivers

| id | date | who | bypassed | why | risk accepted | predicted cost | actual cost | status |
|---|---|---|---|---|---|---|---|---|
| W-01 | 2026-09-11 | Claude | pre-build critic gate (pipeline step 3 before step 4) | Started `build` before the pre-build critic returned. No reason — a sequencing error, not a decision | Building against an unreviewed brief | Not predicted. No waiver was taken at the time; this row is retrospective | **Both of critic pass 1's FAILs had to be hand-patched into finished HTML. Those patches introduced 5 new defects, caught only by critic pass 2, each needing its own fix and re-verification.** Roughly a third of the build effort spent twice | `COSTLY` |
| W-02 | 2026-09-11 | Claude | Gate 3 authored before the artifact | `design.md` v0.1 was written *from* the finished build by critic pass 2, so Gate 3 graded the artifact on its own terms | A gate that cannot fail the thing it grades | Not predicted | **When real design-system content was added later, 9 previously invisible criteria opened at once** — none of them new defects, all of them always true. The gate had been scoped to what the build already did well | `COSTLY` |
| W-03 | 2026-09-11 | Beth | `[A]`+`[?]` = 58.6%, ~2× the 30% readiness threshold | Build at Tier 1 anyway under `PROCEED-FLAGGED`, to have something concrete to argue about | Proceeding on thin evidence, with outputs marked provisional | Wasted build effort if the concept dies | Not yet known. The prototype has already changed the argument twice — it is what made #13a/#13b separable | `PENDING` |
| W-04 | 2026-09-11 | Beth | council pass (pipeline step 5b) | Skipped by explicit decision | Gate 3 criteria rest on a single critic pass | One analytical lens instead of five | Not yet known. Recorded as a limitation in `OPEN.md` H-09, not as a dropped step | `PENDING` |
| W-05 | 2026-09-11 | Claude | evidence-verification discipline, 4× | Attached a `verified_by:` command that did not settle the claim beside it. The claim was true each time; the stated check was not | A criterion that looks verified and is not | Not predicted | Four re-verifications, and it is the **least visible defect class in the apparatus** — both halves look fine in isolation. Logged as `check-never.sh` RD-3 | `COSTLY` |
| W-06 | 2026-09-11 | Claude | "write it down and it will be followed" | Wrote 866 lines of sourced gate documentation in `ux.md` and `design.md` on the assumption that stated rules change behaviour | That documentation alone would be read and obeyed | Assumed near-zero — the whole point was that it would work | **Zero behaviour change, measured.** 12 agents, 6 controlled pairs, 6 ties, no citations of either file. One agent violated the no-emoji rule while holding the file stating it. See `VALUE.md` V-11 | `COSTLY` |

## What this ledger already shows

**Four of six waivers are `COSTLY`, and all four were taken by me without a waiver being recorded at the time.** Three of the four are the same shape: *proceeding past a verification step because the work looked finished.* That is the pattern this ledger exists to make visible, and it took a retrospective reconstruction to see it — which is the argument for logging waivers at the moment of the bypass rather than afterwards.

**Both `PENDING` rows are Beth's, both were deliberate, and both were cheap to state.** A deliberate waiver with a named risk is not the problem. An undeclared one is.

## Counts

Computed, never asserted — run `./check-waivers.sh`.
