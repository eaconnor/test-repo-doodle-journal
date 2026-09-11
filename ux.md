---
scope: research-corpus + marketing + feature
gate: 1
canonical_for: "the research corpus, the positioning and message frame, the audience model, and the primary-research plan"
derived_from: "Intent Specs/doodle-journal.md §2 (context and rationale), §3 (users and affected parties), §13 (open questions)"
evidence_base: "scout/00-index.md .. scout/05 — web-only, no internal sources exist for this concept"
eval_loop: "./check-gates.sh (box state) + ./check-trace.sh (trace validity) + ./check-blocked.sh (human decisions)"
---

# ux.md — Research, Marketing, Audience, and Gate 1

Two halves:

- **§§1–8 — the corpus.** What is actually known about this concept, what is claimed about it by people selling it, who it is supposedly for, and what would have to be measured to find out. Canonical for research and positioning.
- **§9 Acceptance Criteria** — Gate 1 for this feature. Read by `check-gates.sh`.

**Reference syntax in `traces_to:`.** `§N` = a section of the canonical `Intent Specs/doodle-journal.md`. `ds:N.N` = a section of *this* file. `UXI-##` = an intent-spec §5 requirement. `H-##` / `R-##` / `A-##` = an `OPEN.md` row.

> ### Two standing warnings, before anything below is quoted
>
> **1. Everything invented here is tagged `[TEST DATA]`.** Personas, quotes, message-test copy, segment sizes, and the competitive positioning table are fictional. No internal user research exists for this concept and none is claimed. `[TEST DATA]` is not decoration — it is the only thing separating the invented parts of this document from the sourced parts, and it is checked by G1-11.
>
> **2. The strongest real evidence in this document argues against the concept.** ds:4.3 is load-bearing and it cuts the wrong way. Read it before reading the positioning in ds:1, so that the marketing frame lands as a claim under test rather than as a summary of findings.

---

## 1. Positioning and message frame

### 1.1 How this category is sold — the vendor frame

Assembled from the live market (ds:2), in the vendors' own register. `[CS: LOW]` on every line as a *truth claim* — these are marketing pages, not findings. `[CS: HIGH]` that this is genuinely how the category is sold, because the pages were read.

- "See how you felt."
- "Your week, as art."
- "Journaling without the blank page."
- "Speak for a minute. Get something beautiful."

The frame is consistent across MoodGallery, Life Note, Journalie, StoryWriter and MoodMirror: the generated image is presented as an unambiguous reward, the emotional payoff that makes journaling stick.

### 1.2 The honest frame

`[TEST DATA]` — this copy is drafted here, never tested with any audience.

**Positioning statement.** *For people who stop journaling because the blank page is too much work, doodle-journal turns a minute of talking into an entry you actually finished — with a rough drawing beside it that may or may not be right, and which you can throw away without losing a word of what you said.*

**The differences from ds:1.1, and each one is deliberate:**

| vendor frame | honest frame | why the change |
|---|---|---|
| the image is the reward | the finished **entry** is the reward; the image is a by-product | ds:4.3 — the one study that measured it found the benefit came from the writing, not the images |
| "see how you felt" | "here is a guess at how you felt" | ds:4.3 — 70.37% found the images irrelevant to their own narrative |
| beautiful | rough | a rough doodle promises less, so it disappoints less. Untested — this is the whole point of R-01 |
| art you keep and share | a drawing you can discard in one tap | UXI-03, UXI-05 — being wrong must be cheap, and nothing here is built for an audience |

**The line the honest frame rests on:** *the machine's picture never outranks the person's own words* (UXI-01). Everything in ds:1.2 is downstream of that.

### 1.3 Message test matrix — designed, never run

`[TEST DATA]`. Four messages against one audience, forced-choice plus open-ended on why. This exists so that "which message" stops being an opinion.

| id | message | the bet it encodes | falsified if |
|---|---|---|---|
| M-1 | "Journaling without the blank page." | friction is the barrier | people say the barrier was time or privacy, not the blank page |
| M-2 | "Speak for a minute. Get something beautiful." | the image is the draw | people pick it and then react to the actual images the way ds:4.3's participants did |
| M-3 | "Here's a guess at how that felt. Throw it away if it's wrong." | honesty about fallibility is itself the appeal | people find it underwhelming or read it as the product apologising for itself |
| M-4 | "Your words, kept. A drawing, optional." | the entry is the product | no lift over a plain voice-notes app, in which case the doodle is not the concept's value |

**M-4 is the control that can kill the concept.** If M-4 wins, the thing people want is a voice journal, and the doodle is decoration. That outcome must be reportable, which is why M-4 is in the set.

### 1.4 Claims we may not make

Load-bearing, and sourced. Violating any row is not a tone problem, it is a false claim or a regulatory one.

| # | forbidden claim | why | source |
|---|---|---|---|
| MC-01 | therapeutic · therapy · healing · treats · processes trauma · wellness outcome | art therapy is a licensed clinical profession and this literature was never validated on internal product staff at Tier 1 | ds:4.4 · SRC-005 scout/04 · `[CS: HIGH]` |
| MC-02 | "backed by 40 years of research" / "200+ studies" | the effect-size literature is in open methodological disagreement — d=0.47 fixed-effects vs r=.075 random-effects, roughly a fifth the size | ds:4.1 · Frattaroli 2006 · `[CS: HIGH]` |
| MC-03 | "people love seeing their mood as art" | the only located study that measured reaction found majority-negative reception | ds:4.3 · PMC9810434 · `[CS: VERIFIED]` |
| MC-04 | "validated" / "tested" / "proven" in any form | zero participants have used this prototype | §12 · G1-14 |
| MC-05 | "3–4× faster than typing" | widely repeated vendor claim; no primary source located | ds:4.6 · scout/02 · `[CS: LOW]` |
| MC-06 | "87% of journaling app users quit within a week" | traced to a single Medium personal essay, not a study | ds:4.6 · `[CS: LOW]` |
| MC-07 | any privacy claim about on-device processing | no independent audit of any vendor's architecture was located, including the ones that advertise it | ds:4.5 · scout/05 · `[CS: MEDIUM]` |

An escalation trigger already exists for the moment someone describes this as validated (§10). MC-04 is that trigger written as a copy rule.

---

## 2. Market landscape

`[CS: LOW]` on every product claim — these are marketing pages, read but not verified against the products. `[CS: HIGH]` that the pages say what is reported here.

| product | input | output | model of the user | note |
|---|---|---|---|---|
| **StoryWriter** | free writing task | AI text-to-image per passage | writing is the work, image is support | the app in PMC9810434. The study of it is the strongest counter-evidence in this corpus (ds:4.3) |
| **MoodGallery** | daily mood check-in | AI artwork, with sharing | mood is an aesthetic to curate and show | sharing is a direct tension with UXI-05, "a drawer, not a dashboard" |
| **Life Note** ("Inner Gallery") | written entries | weekly generated artwork, $10.99/mo | accumulation is the value | weekly batching sidesteps per-entry accuracy, which is exactly what ds:4.3 measured |
| **Journalie** | written entries | "visual stories" | the entry is raw material for a better artifact | inverts UXI-01 |
| **MoodMirror** (MoodMe) | check-in | "emotional intelligence journal" | self-knowledge as a trackable score | closest to the measurement framing this concept refuses |

### 2.1 The gap that defines the opportunity — and the risk

**Nobody in the market is selling a fallible doodle.** Every product above sells the image as a finished good. Nobody found offers a one-tap discard, and nobody frames the output as a guess.

That is either the opening or the reason the category looks like this. Two readings, and the corpus cannot choose between them:

- **Opening.** Vendors oversold the image, users found it irrelevant (ds:4.3), and a product honest about fallibility would land better.
- **Warning.** Vendors sell the image as finished because a product that admits it is guessing has no reason to exist. If the doodle can be wrong and discarded in one tap, a user may reasonably ask why it is generated at all — which is precisely message M-4's hypothesis (ds:1.3).

`[A] Assumed` — the opening reading is the one this concept bets on, and nothing in this corpus supports it over the warning reading. Named in `OPEN.md` R-09.

### 2.2 The marketing-evidence gap, stated plainly

Every vendor page found presents AI-generated mood art as a validated positive feature. The one primary study located that actually measured user reaction to the images found majority-negative reception on both relevance and tone. **Two data points in tension, on a topic with almost no independent academic replication.** `[WOBBLY]` — do not let repetition across vendor blogs read as corroboration. Nine blog posts repeating one framing is one framing.

---

## 3. Audience

### 3.1 Segments

`[TEST DATA]` — all three segments and every size figure below are invented. No segmentation research exists for this concept. Sizes are there to make the model legible, not to be quoted.

| id | segment | size `[TEST DATA]` | the real evidence anchor | the part that is assumed |
|---|---|---|---|---|
| S-1 | **Lapsed journallers** — started, stopped, still intend to | 55% | abandonment is real and large: median 70% of users gone within 100 days across 18 studies and 525,824 participants (SRC-002) | that *friction* is why, and that lower friction brings them back. Never tested head-to-head — `OPEN.md` R-06 |
| S-2 | **Voice-first capturers** — already talk to their phone | 30% | nothing. Not one primary source on voice-journaling behaviour was located | the entire segment. The 3–4× speed claim behind it is `[CS: LOW]` vendor copy (MC-05) |
| S-3 | **Visual thinkers** — reach for a sketch before a sentence | 15% | art-therapy tradition holds that image-making accesses pre-verbal affect — a disciplinary premise, not an empirical result (ds:4.4) | that this generalises to a *machine-made* image. ds:4.3 is direct evidence against it |

**The ranking is the finding.** S-1 has real evidence for the *problem* and none for the *mechanism*. S-2 has none at all. S-3 has tradition behind the human act of drawing and primary evidence against the machine doing it. Any roadmap that treats these as three equally-supported segments is reading the table wrong.

### 3.2 Personas

`[TEST DATA]` — fictional. Named for legibility, not drawn from any participant. No real person has seen this prototype.

**P-1 · "Nadia" — the lapsed journaller** `[TEST DATA]`
Four journalling apps in three years. The last one still has eleven entries and a 2-day streak she would rather not look at. Wants the record more than the ritual.
- **Job:** finish an entry on a day she has nothing composed to say.
- **Anti-goal:** be graded on consistency. A streak counter is the reason she deleted the last one.
- **Design consequence:** UXI-05 (unobserved — a drawer, not a dashboard) and UXI-07 (an entry is complete without a doodle).
- **Evidence anchor:** SRC-002 reason categories 3, 4 and 5 — poor experience, insufficient personalisation, burdensome data entry. `[D]` for the categories, `[A]` for Nadia.

**P-2 · "Tomas" — the voice-first capturer** `[TEST DATA]`
Talks into his phone while walking. Has 140 voice memos and has replayed four of them.
- **Job:** make spoken thoughts findable later.
- **Anti-goal:** having to listen to himself to find anything.
- **Design consequence:** UXI-06 (transcript reviewable and editable before saving) and UXI-08 (text always present alongside the doodle).
- **Evidence anchor:** **none, and this is the important part.** Whether a doodle is any more skimmable than a voice note is unresearched — `OPEN.md` R-04. Tomas encodes the concept's central unanswered question: does this solve "you can't skim audio," or relocate it?

**P-3 · "Ruth" — the visual thinker** `[TEST DATA]`
Keeps a paper sketchbook. Would not call it journalling.
- **Job:** keep the feeling of a day without flattening it into sentences.
- **Anti-goal:** a machine telling her what her day looked like.
- **Design consequence:** UXI-01 (her words outrank the picture), UXI-03 (discard is cheap), UXI-09 (discard leaves the entry intact).
- **Evidence anchor:** ds:4.3 is evidence *against* Ruth being served by this. 70.97% of participants describing generated images used negative language. Ruth is the persona most likely to reject the output, and she is in the set for that reason.

### 3.3 Anti-persona — who this is explicitly not for

`[TEST DATA]` as a persona; the boundary itself is a real constraint from §4 and ds:4.4.

**Anyone in distress, or using this in place of care.** Crisis detection is explicitly not attempted (§4). No clinical claim is made (MC-01). A journal that guesses at your emotional state and draws it is the wrong object for someone in crisis, and the correct response to that user is not a better doodle — it is a person. `[CS: HIGH]` on the constraint.

---

## 4. Secondary research — the evidence base

Web-only, single pass, 2026-09-11. Full dossier in `scout/`. Every figure below is traced; nothing is rounded or restated from memory.

### 4.1 Expressive writing — the ground, and it is softer than it is sold as

Pennebaker & Beall (1986) established that writing about difficult experience — 15–30 minutes, roughly four sessions over a month — produces measurable wellbeing benefit. `[CS: HIGH]` as an origin point; not re-verified against the 1986 original.

**The effect-size drift is the actual state of the evidence:**

| meta-analysis | studies | model | effect | `[CS:]` |
|---|---|---|---|---|
| Smyth (1998) | 13 RCTs | fixed-effects | **d = 0.47** | MEDIUM — not fetched from primary |
| **Frattaroli (2006)** | **146 RCTs** | random-effects | **r = .075** | **HIGH — largest and most methodologically current located** |
| Pavlacic et al. (2019), PTSD/PTG/QoL | not fetched | — | positive, small | MEDIUM |
| adolescent-specific review | not fetched | — | mean ES = **0.127** | MEDIUM — abstract only |

`[WOBBLY]` — "40+ years, 200+ RCTs, robustly replicated" papers over a live methodological fight. Frattaroli's own conclusion is that the effect is **real but small**, and that cost-effectiveness, not magnitude, is the strongest remaining argument. A further paper (PMC10300201) suggests effect sizes are highly sensitive to how the prompt is worded — small changes in instruction move the result.

**What this means here.** The concept inherits a real but modest ground effect that is sensitive to prompt wording. It cannot inherit a large one. MC-02 exists because of this row.

### 4.2 Abandonment — the problem, and it is real

**SRC-002** — "When and Why Adults Abandon Lifestyle Behavior and Mental Health Mobile Apps", PMC11694054. `[CS: VERIFIED — fetched and read directly]`

- **18 eligible studies · 525,824 participants · published 2014–2022**
- Median discontinuation: **70% of users within the first 100 days**
- Comparators cited within: 66% of health apps and 69% of fitness apps abandoned within 90 days
- By category: alcohol apps 95–97% · **mental health apps 89–92%** · physical activity apps 54–75%
- **Six reason categories, 22 sub-reasons:** technical/functional · **privacy** · **poor user experience** · **content and features (insufficient personalisation, no accountability)** · **time and financial cost (burdensome data entry)** · evolving needs

This is the strongest retention citation in the corpus and the evidential basis for the problem statement. **It does not test image-output journaling.** The link from "burdensome data entry" to "therefore a doodle helps" is inferential. `[A] Assumed`, named in `OPEN.md` R-06.

### 4.3 The counter-evidence — read this before anything else

**SRC-001** — "Exploring the use of AI text-to-image generation to downregulate negative emotions in an expressive writing application", PMC9810434. `[CS: VERIFIED — fetched and read in full]`

Two studies. Study 1: experimental, **n = 388** (131 men / 252 women / 4 other, mean age 30.1), between-subjects, negative vs. neutral induction, with-images vs. without. Study 2: qualitative remote survey, **n = 54** (30 women / 19 men / 5 non-binary, mean age 33.7).

**Emotion regulation — modest and partial.** Under negative induction, with-images reduced anger (**d = −0.40**) and sadness (**d = −0.63**) against control. **Anxiety and stress showed no significant difference.**

**Mechanism — the benefit was the writing.** Study 2 attributes the effect to the writing process itself, not to the generated images.

**Reaction to the images — the finding that matters here:**

| finding | figure |
|---|---|
| participants who found the generated images **irrelevant to their own narrative** | **70.37%** (38 of 54) |
| participants describing the images in **negative language** — "scary", "unsettling", "creepy" | **70.97%** |
| generated images rated **suitable** for the writing task | **26.63%** |

Participants reported **actively avoiding looking** at images they found grotesque.

This is direct, primary, fetched evidence that a machine attempting to visually represent a person's own emotional disclosure frequently gets it wrong in ways people find **unsettling, not merely inaccurate**. Those are different failures and they need different fixes, which is why unknown #13 is split:

- **#13a — semantic miss.** Can *any* generated image match what a person actually said? 70.37% said no. **Style changes do not plausibly fix this.** `OPEN.md` R-02.
- **#13b — affective miss.** Does a hand-drawn doodle avoid the *unsettling* register? 70.97% negative language was against photorealistic output. A doodle might do better. Untested anywhere reachable. `OPEN.md` R-01.

**The split is not a hedge, it is the kill criterion.** A result where #13b improves and #13a does not is **re-scope-or-kill**, not a partial win: a doodle that feels pleasant while still failing to represent what the person said is a nicer failure, not a success. This is recorded in the brief's falsifiability table and in §1's anti-success signals.

**Second source, weaker.** "A Portrait of Emotion: Empowering Self-Expression through AI-Generated Art" (CogSci 2023, arXiv 2304.13324) — `[CS: MEDIUM, abstract level only; full-text extraction failed, sample size unverified]`. Reports that participants preferred images generated from their **emotions** over images depicting the literal **events** of their narrative, and names visual cliché and stereotype as a specific failure mode. Its authors reach toward clinical framing; that framing is not imported here (MC-01).

**A-01 applies to this entire section.** All of the counter-evidence rests on **one** study, n=54 on the qualitative half. That is a real limitation of the counter-evidence and it is not fixable by editing — only by more research. It is carried visibly rather than discounted, and it does not license discounting the finding: one direct measurement outranks nine vendor pages asserting the opposite.

### 4.4 Art therapy precedent, and the line this concept may not cross

Visual journalling as practice predates formal art therapy. Cathy Malchiodi, PhD, has written specifically on visual journalling as art therapy and self-help — `[CS: MEDIUM]`, and **her specific claims are not verified here**: the PDF fetch returned undecoded binary, so what the corpus holds is secondary characterisation, not direct reading. Flagged rather than passed off.

The field's rationale — that some emotional content is pre-verbal and that image-making reaches affect resisting language — is a **disciplinary premise, not an empirical result**. `[TRADITION: expressive arts therapy]`.

**The one directly relevant comparative study could not be read.** "Emotional expression and psychological symptoms: A comparison of writing and drawing" (ScienceDirect S0197455605000699) returned **HTTP 403**. It is the single most on-point study located in the entire scout pass and it is unread. `[CS: UNKNOWN pending access]` — `OPEN.md` R-03, and the gap is not filled with a plausible summary. Pizarro (2004), reported secondhand as finding art-plus-writing beats writing alone, has no DOI captured and the original was never read — `[CS: LOW]`, `OPEN.md` R-08.

**The clinical line.** Everything in this section sits inside a licensed clinical profession's literature, validated on clinical populations, not on internal product staff at Tier 1. MC-01 is the operational form of this. The concept may be *informed by* the idea that images reach something words do not; it may not claim efficacy it has not tested.

`[THIN DOMAIN]` — visual journalling as lived practice long predates this literature and exists across cultures with no digitised, English-language record a web scout can reach. The corpus represents the Western clinical/academic strand only. Named, not filled. `OPEN.md` A-02.

### 4.5 Privacy, law, and breach precedent

**GDPR Article 9.** Beth works in the UK; GDPR applies. Emotional or mental-state data inferred from a journal entry is **special category data**. Processing it is **prohibited by default**, permitted only under listed exceptions, and valid consent must be **explicit** — naming the specific special-category processing, not a general ToS checkbox — and freely given, specific, informed, unambiguous, documented and withdrawable. `[CS: HIGH — settled regulatory interpretation]`

**The load-bearing implication.** "It is just generating a picture" undersells the exposure. **The inference step is the regulated act**, not the storage. A text-to-image pipeline over a journal entry inherently infers something about mood — the image has to represent *something*. `[CS: HIGH]` on the law; `[CS: MEDIUM]` that it applies this way here, because no DPA enforcement action naming AI-generated mood art specifically was located. UXI-02 and UXI-10 exist because of this.

**Breach precedent — real, recent, fetched.** Oversecured research, via BleepingComputer, summarised by TechRepublic. `[CS: HIGH — fetched and read; note Oversecured is a commercial security vendor, so read the framing as vendor-interested even though the technical findings are specific and datable]`

- **10 widely-downloaded Android mental health apps · 14.7 million combined installs · examined 22–23 Jan 2026**
- **1,575 security flaws**, dozens rated high severity
- Exposed categories: therapy transcripts, CBT exercises, mood histories, medication reminders, **self-harm indicators**, treatment progress scores
- Causes: insecure inter-app communication, plaintext storage, exposed API endpoints, hardcoded database credentials, weak encryption
- App identities withheld pending remediation — disclosed-but-anonymised, not a named list

**Journal-specific privacy expectations are unmeasured.** No study was located measuring what users *believe* about a journal app's privacy as a category. The GDPR analysis sets the legal floor; it says nothing about expectation. That a "journal" carries stronger implicit privacy expectations than an "app" is a **design hypothesis, not a finding** — `OPEN.md` R-05.

### 4.6 Trust ladder and the do-not-cite table

**Strongest — fetched, read in full, quotable with figures**
- SRC-001 · PMC9810434 · StoryWriter — the counter-evidence (ds:4.3)
- SRC-002 · PMC11694054 · abandonment scoping review (ds:4.2)
- Oversecured/TechRepublic breach reporting (ds:4.5)

**Strong but not fetched from primary**
- SRC-003 · Frattaroli (2006) — PDF located, figures traced; treat as HIGH, not VERIFIED
- GDPR Art. 9 interpretation — settled law, no single fetched citation

**Directional only — do not quote as findings**
- arXiv 2304.13324 — abstract level, sample size unverified
- Malchiodi visual-journalling material — fetch failed, secondary characterisation only
- Pizarro (2004) — secondhand, no DOI
- every vendor product claim in ds:2

**`[WOBBLY]` — the whole voice-capture theme.** Nine vendor blog posts plus two academic citations that surfaced only through search-engine synthesis and were never fetched. **There is no independently verified primary research on voice journalling in this corpus at all.** Read every claim in it as marketing copy that happens to be directionally plausible.

**🚫 Do not cite, under any circumstances**

| source | why |
|---|---|
| **`cambridgeanalytica.org`** — claimed Apple's on-device Journal app performs "behavioural profiling" | `[CS: FABRICATION RISK]`. The domain name and framing pattern signal an agenda-driven source masquerading as an outlet. Uncorroborated. Named explicitly rather than silently dropped, because it looks citable and is not |
| "87% of journaling app users abandon within 7 days" | traced to one Medium personal essay. MC-06 |
| "therapy records sell for $1,000+ per record on the dark web" | single founder quote inside the Oversecured reporting, no market data behind it. `[CS: LOW]` |
| "speaking is 3–4× faster than typing" | repeated across nine vendor blogs, no primary source located. MC-05 |
| "a 2024 JMIR study found audio reflection comparable to written" | surfaced only via an AI-generated search summary — no authors, no title, no DOI. **This is exactly the fluent-but-unsourced pattern the protocol exists to catch** |

### 4.7 The ratio

`[A]` + `[?]` = **58.6%** of tagged claims — 17 of 29, grep-verified — against a 30% threshold. Nearly double. Computed, never asserted:

```bash
grep -cE '^\| [0-9]+[a-z]? \| \[[A?]\] \|' briefs/doodle-journal.brief.md   # 17
grep -cE '^\| [0-9]+[a-z]? \| \[[RDA?]\] \|' briefs/doodle-journal.brief.md # 29
```

Carried knowingly at Tier 1 under `PROCEED-FLAGGED`, stated in every artifact. `OPEN.md` A-04.

---

## 5. The gap register — what the evidence does not say

Every row is a real absence in the corpus, not a to-do. Each maps to an `OPEN.md` row so nothing here can be quietly dropped.

| gap | why it matters | row |
|---|---|---|
| Does a hand-drawn style avoid the *unsettling* reaction? (#13b) | the only plausible design fix for 70.97% negative language | R-01 |
| Can **any** generated image match what a person said? (#13a) | the more damaging half. 70.37% said no. Style does not fix it | R-02 |
| The one direct writing-vs-drawing comparison study | HTTP 403, unread. The most on-point source located | R-03 |
| Do people revisit voice entries at all, and is a doodle more skimmable? | decides whether the concept solves the skim problem or relocates it | R-04 |
| Do users hold stronger privacy expectations for "a journal"? | design hypothesis, unsourced | R-05 |
| Does lower-friction non-text capture actually improve retention? | the entire S-1 bet. Extrapolated from abandonment categories, never tested | R-06 |
| Transcription error in emotionally loaded speech | no source addresses it | R-07 |
| Pizarro (2004) primary | "art + writing beats writing alone" is secondhand | R-08 |
| Is the ds:2.1 opening real, or is the market shaped that way for a reason? | decides whether an honest-fallibility product has a market at all | R-09 |
| Has any persona or message been put in front of a person? | no. Zero participants | R-10 |

**Six of the nine `[?]`-level questions are answerable by research nobody has been assigned.** They are `RESEARCH`-kind rows, so the machine may proceed flagged — but it may not claim validation. The one `HUMAN` decision that gates all of it is H-01: commission the reaction test, or decline it in writing. `./check-blocked.sh` exits 2 while it stands.

---

## 6. The primary research plan

Designed here so that "we should test it" stops being a sentiment. **Not run. Zero participants.** Gated on H-01.

### 6.1 The question, stated so it can fail

Does a **hand-drawn doodle** generated from a person's **own** voice or text journal entry avoid the semantic miss (#13a) and the affective miss (#13b) that PMC9810434 found for photorealistic images generated from a fiction-writing task?

### 6.2 Design

Method follows PMC9810434's Study 2 so results are comparable rather than merely new. `[CS: HIGH]` that the method is reproducible from the paper; ds:4.3 for what it measured.

| element | specification |
|---|---|
| **Design** | within-participants, three stimulus styles: hand-drawn doodle · photorealistic · abstract non-figurative |
| **Input** | the participant's **own** entry, not a supplied narrative. This is the material difference from PMC9810434, whose participants wrote a fiction task |
| **n** | 54 minimum, matching the study being compared against `[TEST DATA]` as a recruitment target |
| **Primary measure — #13a** | relevance of image to own narrative, forced-choice plus open-ended. Directly comparable to the 70.37% figure |
| **Primary measure — #13b** | affective register of the participant's own free description, coded for negative language. Directly comparable to 70.97% |
| **Secondary** | proportion rated suitable (comparable to 26.63%) · discard rate per style · avoidance behaviour, which PMC9810434 observed qualitatively |
| **Analysis** | pre-registered. Style as within-subject factor. **No subgroup analysis not declared in advance** |

### 6.3 The kill criteria, declared before the data exists

This is the part that makes it a test rather than a demo.

| result | consequence |
|---|---|
| #13a and #13b both improve materially | Gate 2 upgrades from PARTIAL. Proceed to Tier 2 |
| **#13b improves, #13a does not** | **re-scope or kill.** A pleasanter failure is not a success (ds:4.3) |
| #13a improves, #13b does not | style problem — keep the mechanism, redesign the output |
| neither improves | **kill.** The concept's core mechanism does not work |

**The predicted-most-likely outcome is row 2**, and it is a re-scope-or-kill. That prediction is written down before the test so that it cannot be reinterpreted as a partial win afterwards.

### 6.4 Why SC-001 and SC-002 cannot be measured on the current prototype

The Tier 1 build serves **pre-drawn** doodles. There is no model call. A pre-drawn doodle cannot semantically miss a specific entry, because it was never derived from one — so #13a is **structurally unmeasurable** on this artifact, not merely unmeasured. Deferred to Tier 2 and recorded as such (G3-16, G3-17). Reporting a favourable number from this prototype would be measuring the wrong thing and calling it evidence.

---

## 7. Research operations and ethics

Constraints, not aspirations.

- **All seed data fictional and `[TEST DATA]`-tagged.** No real internal staff journal content, ever, even anonymised. `[CS: HIGH]` — project rule plus ds:4.5.
- **Purpose limitation.** Data gathered for one research purpose stays in it. Interview quotes are not seed data.
- **Offered, not taken.** Publicly accessible is not the same as in scope.
- **IRB principles apply** whether or not a formal IRB is required — participant data used only for the consented purpose, never to identify individuals without explicit consent.
- **Art. 9 consent copy is not yet lawful.** The current FR-006 copy is a UI pattern, not an Art. 9 disclosure. Needs a named qualified reviewer — `OPEN.md` H-02, G2-11, G3-22.
- **No crisis detection is attempted** (§4), and the correct response to a user in distress is a person, not a feature (ds:3.3).
- **The prototype is not a stand-alone deliverable.** The figures on its face are evidence *against* the concept, not results, which is why it renders a red no-data panel above the fold. Sending the HTML onward without its brief is the specific foreseeable misuse.

---

## 8. Jobs, journey, and measurement

### 8.1 Jobs to be done

| id | job | evidence | status |
|---|---|---|---|
| J-1 | "When I have nothing composed to say, help me finish an entry anyway." | SRC-002 categories 4 and 5 | `[D]` for the problem, `[A]` for the mechanism |
| J-2 | "Let me find what I said later without listening to all of it." | none located | `[?]` — R-04 |
| J-3 | "Keep the feel of the day without flattening it into sentences." | art-therapy premise, ds:4.4 | `[A]` — and ds:4.3 is evidence against the machine doing it |
| J-4 | "Let me be wrong cheaply." | UXI-03 · derived from ds:4.3's avoidance behaviour | `[R]` — the design response is sourced even though the job is inferred |

**J-4 is the only job in the table whose design response is grounded in primary evidence.** The rest are inferred. That is worth saying out loud, because a jobs table with four confident rows reads like four findings.

### 8.2 Journey, with the failure points named

| stage | what happens | the risk, sourced |
|---|---|---|
| 1 · Open | no doodle on load, nothing generated yet | UXI-02. Pre-generation would make the inference unasked-for — an Art. 9 problem, not a UX preference (ds:4.5) |
| 2 · Capture | speak or type | transcription error in emotionally loaded speech is unresearched — R-07 |
| 3 · Review | transcript editable before saving | UXI-06. Skipping this makes the machine's transcription the record of what a person said |
| 4 · Consent | explicit, per entry | UXI-10. Not a ToS checkbox (ds:4.5) |
| 5 · Generate | doodle appears beside the text, labelled as a guess | **the failure point.** 70.37% irrelevant · 70.97% negative language (ds:4.3) |
| 6 · Keep or discard | one tap, entry text untouched | UXI-03, UXI-09. This is J-4 and it is the design's answer to stage 5 |
| 7 · Return | a drawer, not a dashboard | UXI-05. No streaks, counters, notifications. The anti-goal that made P-1 delete the last app |

**Stage 5 is where the concept lives or dies, and the corpus already predicts it fails there.** Stage 6 exists because stage 5 is expected to be wrong often.

### 8.3 Measurement

| id | measures | instrumented | state |
|---|---|---|---|
| SC-001 | #13a — semantic match | no | structurally unmeasurable at Tier 1 (ds:6.4). Deferred |
| SC-002 | #13b — affective register | no | deferred to Tier 2 |
| SC-003 | time to a completed entry | **yes** | returned **1.8s** on one live save. **n = 1. Not a finding** |
| SC-004 | discard rate per style `[TEST DATA]` | no | requires the ds:6 test |
| — | retention | **deliberately not measured at Tier 1** | measuring retention on a concept probe would invite exactly the validation claim MC-04 forbids |

**Anti-metrics — success signals this product refuses to chase:** entries per week, streak length, session duration, doodles shared. Each would be read as engagement and each contradicts UXI-05. A metric you refuse to optimise is a design decision, so it is recorded here rather than left implicit.

---

## 9. Acceptance Criteria — Gate 1: Do we understand the problem?

Each criterion is settleable by a grep, a count, or a file-state check. Unchecked means **not true**, not overlooked.

**Evidence discipline**
- [x] G1-01 — Every evidentiary claim in the brief carries an `[R]`/`[D]`/`[A]`/`[?]` tag · traces_to: §2 · verified_by: `grep -cE '^\| [0-9]+[a-z]? \| \[[RDA?]\] \|' briefs/doodle-journal.brief.md` = 29, zero untagged rows
- [x] G1-02 — The `[A]`+`[?]` ratio is computed, never asserted · traces_to: §1, ds:4.7 · verified_by: the two grep commands in ds:4.7, 17/29 = 58.6%, recorded with the commands used
- [x] G1-03 — SRC-001's three figures (70.37 / 70.97 / 26.63) appear verbatim in the built artifact · traces_to: UXI-04, ds:4.3 · verified_by: `grep -c` on `prototypes/doodle-journal/doodle-journal.html`, all three present
- [x] G1-04 — SRC-001 is cited by accession number wherever its figures appear · traces_to: §2, ds:4.3 · verified_by: `grep -c PMC9810434` ≥ 1
- [x] G1-06 — The problem statement distinguishes the sourced problem from the unsourced mechanism · traces_to: §2 · verified_by: brief `problem_statement` frontmatter contains both a `[D]` clause and an unsourced-mechanism clause
- [x] G1-07 — Every `source_material` entry carries an owner and a status · traces_to: §2 · verified_by: 7 of 7 entries have both fields
- [x] G1-08 — The single-source limitation on the counter-evidence is stated in the artifact, not only in the brief · traces_to: ds:4.3, A-01 · verified_by: `grep` for the n=54 statement in `SOURCES.md` and in ds:4.3
- [x] G1-12 — Every statistic in this file carries a source id or accession number and a `[CS:]` tag · traces_to: ds:4.6 · verified_by: no bare figure appears outside a table row that names its source
- [x] G1-13 — The do-not-cite table names `cambridgeanalytica.org` explicitly rather than dropping it silently · traces_to: ds:4.6 · verified_by: `grep -c 'cambridgeanalytica'` ≥ 1 in `ux.md` and `SOURCES.md`
- [x] G1-16 — The effect-size disagreement is stated wherever expressive writing is relied on · traces_to: ds:4.1 · verified_by: both d=0.47 and r=.075 appear, with their models named

**Honesty about what is invented**
- [x] G1-05 — No internal user research is claimed anywhere · traces_to: §3 · verified_by: all 7 `source_material` rows are web or self-authored; no Condens, Confluence or Jira citation in brief, ux, vision or design
- [x] G1-11 — Every persona, segment size, and message-test row is tagged `[TEST DATA]` · traces_to: §3, ds:3 · verified_by: `grep -c '\[TEST DATA\]'` in `ux.md` ≥ 1 per invented block; P-1, P-2, P-3, S-1..S-3 and ds:1.3 each carry the tag
- [x] G1-14 — No artifact claims validation, testing, or proof **of this concept** · traces_to: §10, ds:1.4 · verified_by: MC-04 stated. `grep -inE '\b(validated|proven)\b' ux.md` returns 8 hits on 6 lines, each read: 3 are the prohibition itself (MC-04 and its escalation note), 1 is MC-01's clinical line, **2 describe someone else's claim** — vendors presenting mood art as "a validated positive feature" (ds:2.2) and the art-therapy literature being "validated on clinical populations" (ds:4.4) — and 1 is this criterion. Zero assert validation of this concept
- [x] G1-15 — The marketing claims we may not make are enumerated with sources, including the clinical line · traces_to: ds:1.4, ds:4.4 · verified_by: MC-01..MC-07 present, each with a source column
- [x] G1-17 — Competitive claims are labelled marketing rather than evidence · traces_to: ds:2 · verified_by: `[CS: LOW]` stated across the ds:2 block and the marketing-evidence gap named at ds:2.2

**The research that would settle it — designed, not done**
- [x] G1-18 — Unknown #13 is split into #13a and #13b, with the split's consequence stated · traces_to: ds:4.3, ds:6.3 · verified_by: both appear, and row 2 of ds:6.3 reads re-scope-or-kill
- [x] G1-19 — A kill criterion is declared before any data exists · traces_to: ds:6.3 · verified_by: 4-row outcome table present, with the predicted-most-likely outcome named
- [x] G1-20 — Every gap in the corpus maps to an `OPEN.md` row · traces_to: §13, ds:5 · verified_by: all 10 ds:5 rows carry an R-## id that resolves in `OPEN.md`
- [ ] G1-09 — A reaction test measuring #13a and #13b separately has been commissioned · traces_to: H-01, ds:6 · verified_by: `OPEN.md` H-01 moved to the Resolved table — **currently open, owner Beth. Everything in ds:6 waits on this one decision**
- [ ] G1-10 — SRC-004 (the writing-vs-drawing comparison, the most on-point study located) has been read · traces_to: R-03, ds:4.4 · verified_by: `source_material` SRC-004 status changes from `BLOCKED` — **HTTP 403, never read**
- [ ] G1-21 — The ds:1.3 message test has been run · traces_to: R-09, ds:1.3 · verified_by: a result per message, including whether control M-4 won — **never run. The positioning in ds:1.2 is an untested draft**
- [ ] G1-22 — At least one persona has been put in front of a real person · traces_to: R-10, ds:3.2 · verified_by: participant count > 0 — **zero. P-1, P-2 and P-3 are fiction and remain fiction**
- [ ] G1-23 — The ds:2.1 opening-vs-warning question has been resolved · traces_to: R-09, ds:2.1 · verified_by: evidence that an honest-fallibility product has a market, or a decision to proceed without it — **open; the corpus cannot choose between the two readings**
- [ ] G1-24 — The retention mechanism has been tested head-to-head against text journalling · traces_to: R-06, ds:4.2 · verified_by: a comparison study exists — **never tested. The entire S-1 bet is an extrapolation from SRC-002's reason categories**

Count computed, never asserted:

```bash
awk '/^## 9\. Acceptance Criteria/{f=1;next} /^## /{f=0} f && /^- \[ \]/{c++} END{print c+0}' ux.md
```

### What adding the corpus did to this gate

Gate 1 went from **10 criteria, 2 open** to **24 criteria, 6 open**.

The two original open rows were both about work nobody had done. **Four of the new open rows are about claims this document now makes out loud.** Writing down a positioning statement (ds:1.2), three personas (ds:3.2), a market opening (ds:2.1) and a retention mechanism (ds:4.2) created four falsifiable assertions where previously there were four unstated assumptions. G1-21 through G1-24 are the cost of having said them.

That is the correct direction. An assumption that is not written down cannot be tested, cannot be assigned, and cannot be shown to be wrong — it just quietly steers the roadmap. **Naming an assumption makes the gate redder and the project more honest, and those are the same event.**
