---
id: I-02
gate: 2
status: DESIGNED — never run. Zero participants.
settles: ux.md G1-21, G1-23 · OPEN.md R-09
blocks_nothing: this instrument does not require H-01
runs_before: I-01
---

# I-02 — Message test

**Run this before I-01.** It is roughly an order of magnitude cheaper, it is asynchronous, and **it can make I-01 unnecessary.** See "Why this goes first" below — that is the load-bearing part of this document.

## The question

Which of four positionings do people choose, and **does the control win?**

## Stimuli — the four messages, already fixed in `ux.md` ds:1.3

| id | message | the bet it encodes |
|---|---|---|
| M-1 | "Journaling without the blank page." | friction is the barrier |
| M-2 | "Speak for a minute. Get something beautiful." | the image is the draw |
| M-3 | "Here's a guess at how that felt. Throw it away if it's wrong." | honesty about fallibility is itself the appeal |
| **M-4** | **"Your words, kept. A drawing, optional."** | **the entry is the product — the control** |

Order randomised per participant. No product name, no visual, no doodle shown — this tests the proposition, not the execution.

## Method

| element | specification |
|---|---|
| Design | within-participants forced choice, then open-ended "why that one?" |
| Recruitment | people who have started and stopped a journalling app — screener below |
| n | **15 minimum.** Not a significance target; a preference-share and reason-code target |
| Mode | asynchronous, unmoderated. No facilitator time |
| Effort | ~10 min per participant. Screener + 4 messages + 3 questions |
| Analysis | preference share per message, plus reason codes from the open-ended, coded by two people independently |

**Screener (must pass all three):** has used a journalling or diary app · stopped using it · did not stop because they achieved what they wanted. The third item matters — someone who stopped because they finished is not the S-1 segment.

## Questions, in order

1. *(forced choice)* "Four apps describe themselves like this. Which would you be most likely to try?"
2. *(open)* "Why that one?"
3. *(open)* "What do you expect it would actually do?" — catches a message that wins by being misunderstood
4. *(forced choice)* "Which would you be **least** likely to try?" — the negative signal is often cleaner than the positive

## Thresholds — declared now, before any data exists

| result | reading | consequence |
|---|---|---|
| **M-4 takes the largest share** | the entry is the product; the doodle is decoration | **Gate 2 fails. Re-scope to a voice journal, and do not run I-01.** The doodle is not the value proposition and there is nothing left for a reaction test to save |
| M-2 largest | the image is the draw | run I-01 — and expect trouble, because this is the framing PMC9810434's participants reacted against |
| M-3 largest | fallibility is the appeal | run I-01. This is the framing `ux.md` ds:1.2 bets on, and would be the first evidence for it |
| M-1 largest | friction is the story, doodle incidental | run I-01, but the doodle is a feature not a proposition — re-scope the pitch |
| No message above ~40% | nothing resonates | re-scope before spending on I-01 |

**Predicted most likely: M-4 or M-1.** Written down before the data, so it cannot be reinterpreted afterwards.

## Why this goes first — and it contradicts how the register reads

`OPEN.md` H-01 is written as the decision everything waits on, and it commissions **I-01**, the expensive moderated study. That ordering is wrong on cost grounds:

- I-01 needs a facilitator, live stimulus generation, and per-session coding. I-02 needs a screener and a form.
- **I-02 can retire I-01 entirely.** If M-4 wins, the doodle is not the proposition, and a reaction test measuring how people feel about doodles is measuring a feature nobody chose the product for.
- The reverse is not true. Running I-01 first tells you nothing about whether anyone wanted the thing.

So the honest recommendation is: **run I-02, then decide H-01 with its result in hand.** H-01 stays open and Beth still owns it — this changes what it costs to answer, not who answers it.

## What this instrument cannot answer

- Whether the doodle is *accurate* (#13a) or *unsettling* (#13b). That is I-01. A stated preference for a message is not a reaction to an artifact.
- Whether anyone would keep using it. Preference is not retention, and treating it as retention is the oldest error in concept testing.
- Anything about the build. This is Gate 2.

## Ethics and data handling

Consented for this purpose only. Reason-code text is research data — it does not become seed data, persona quotes, or marketing copy (purpose limitation). No participant identifiers in any artifact. `purpose_tag: gate-2-positioning-only`.
