# SOURCES.md — Doodle Journal

Provenance for everything claimed in `doodle-journal.html`, `briefs/doodle-journal.brief.md`, `ux.md`, `vision.md`, and `spec.md`. Carried **in** the artifact so the next reader can check the argument without re-doing the scout pass.

**Scout type:** web-only, 2026-09-11. No Confluence, no Jira, no Condens, no interviews — none exist for this concept. That absence is confirmed by design, not searched-and-missed, and it is the single most important thing to know before quoting anything here.

---

## ⭐ Start here — the five sources that carry the whole argument

| # | Source | What it carries | Trust |
|---|---|---|---|
| 1 | **StoryWriter** — "Exploring the use of AI text-to-image generation to downregulate negative emotions in an expressive writing application", [PMC9810434](https://pmc.ncbi.nlm.nih.gov/articles/PMC9810434/) | **The load-bearing source.** The only primary study located that measured how people react to AI-generated imagery of their *own* emotional disclosure. n=54 qualitative: **70.37%** judged images irrelevant to their narrative, **70.97%** used negative language ("scary," "unsettling," "creepy"), **26.63%** rated suitable. Study 1 (n=388): anger d=−0.40, sadness d=−0.63, no effect on anxiety/stress. Its own mechanism finding: benefit came from **the writing, not the images** | `[CS: VERIFIED]` — fetched and read in full |
| 2 | **App abandonment scoping review** — "When and Why Adults Abandon Lifestyle Behavior and Mental Health Mobile Apps", [PMC11694054](https://pmc.ncbi.nlm.nih.gov/articles/PMC11694054/) | The only sourced problem this concept has. 18 studies, **525,824 participants**, 2014–2022. Median **70% discontinuation within 100 days**; mental-health apps **89–92%**. Six reason categories — "blank page / low personalization" and "burdensome data entry" are the two on point | `[CS: VERIFIED]` — fetched directly |
| 3 | **Frattaroli (2006)** — "Experimental Disclosure and Its Moderators: A Meta-Analysis", [PDF](https://bpb-us-e2.wpmucdn.com/faculty.sites.uci.edu/dist/c/602/files/2019/08/Frattaroli-psych-bulletin-2006.pdf) | The honest state of expressive-writing evidence: **146 RCTs, random-effects, r = .075** — small but significant. Use this to deflate any "expressive writing is robustly proven" framing | `[CS: HIGH]` — fetched directly |
| 4 | **GDPR Article 9** (via `scout/05`) | Emotion inferred from a journal entry is **special-category data**, processing prohibited by default, consent must be **explicit**. The **inference step is the regulated act** — not merely the storage. Drives FR-006 | `[CS: HIGH]` — settled regulatory interpretation |
| 5 | **Oversecured / BleepingComputer / TechRepublic** (via `scout/05`) | This app category is a live target, not a theoretical risk: **10 Android mental-health apps, 14.7M installs, 1,575 flaws**, Jan 22–23 2026. Exposed therapy transcripts, mood histories, self-harm indicators | `[CS: HIGH]` on the technical findings — vendor-interested framing; Oversecured sells security |

---

## Read-for-the-question map

| If you need to answer… | Read | Live link |
|---|---|---|
| "Is there evidence people want this?" | `scout/01` — and the answer is no, not for the *mechanism* | [PMC11694054](https://pmc.ncbi.nlm.nih.gov/articles/PMC11694054/) |
| "Will the doodle feel accurate to the person?" | `scout/03` — the one study that measured it says no, a majority of the time | [PMC9810434](https://pmc.ncbi.nlm.nih.gov/articles/PMC9810434/) |
| "Is voice actually lower-friction?" | `scout/02` — entirely vendor marketing, no verified primary source | *(see do-not-cite below)* |
| "What does drawing do that writing doesn't?" | `scout/04` — the directly-titled comparative study is **paywalled and was never read** | [S0197455605000699](https://www.sciencedirect.com/science/article/abs/pii/S0197455605000699) — HTTP 403 |
| "What are we legally on the hook for?" | `scout/05` | GDPR Art. 9 |
| "Can we call this therapeutic?" | `scout/04` — **no.** Licensed profession, clinical protocols, never validated on this population | [REPAT protocol PMC10343444](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10343444/) |
| "How ready is this to build?" | `briefs/doodle-journal.brief.md` — 58.6% `[A]`+`[?]`, ~2× the 30% threshold | — |

---

## Trust ladder

### Strongest — fetched, read in full, quote directly
- **PMC9810434** (StoryWriter) — all four numbers and the mechanism finding
- **PMC11694054** (abandonment) — the 70%/100-day and 89–92% figures
- **Frattaroli 2006** — r = .075 across 146 RCTs

### Directional only — real, but don't build a number on it
- **Smyth (1998)**, d = 0.47 — `[CS: MEDIUM]`, not fetched from primary. Cite *only* alongside Frattaroli, because the gap between them is the methodological fight, and quoting d=0.47 alone overstates the field by roughly 5×
- **"A Portrait of Emotion"** (CogSci 2023, arXiv 2304.13324) — `[CS: MEDIUM]`, abstract only; PDF extraction failed. Its "people prefer emotion-images over event-images" finding is suggestive, not verified. Also note its authors reach toward therapeutic framing we must not inherit
- **REPAT** (PMC10343444) — a clinical *protocol* paper, i.e. a planned intervention design, **not an outcomes study**

### `[WOBBLY]` — synthesis presented as consensus somewhere in the wild
- The **"40+ years, 200+ RCTs, robustly replicated"** framing of expressive writing (e.g. Mindsera's "200+ Studies Reviewed"). Papers over the fixed-vs-random-effects fight. `scout/01`
- **The entire voice-input theme** (`scout/02`) rests on nine vendor blog posts plus two academic citations that were never fetched. There is no independently verified primary research in that file
- **Every vendor page** on AI mood art (MoodGallery, Life Note, Journalie, StoryWriter-as-product, MoodMirror) frames generated imagery as an unambiguous positive. The only primary study that measured user reaction found majority-negative. Repetition across blogs is **not** independent corroboration
- **Art therapy's "some emotional content is pre-verbal"** — a disciplinary premise, not an empirical result. `scout/04`
- **`[THIN DOMAIN]`** across all five scout files: every tradition here is Western, English-language, academic-institutional. Non-Western, oral, and pre-colonial visual/reflective journaling practice is absent from what a web scout can reach. Named, not filled

### 🚫 Do not cite — the traps, named explicitly
These look citable and are not. Listed so nobody re-finds them and quotes them in good faith.

| Claim | Why not |
|---|---|
| Apple's Journal app performs "behavioral profiling" | Sourced to a domain calling itself **cambridgeanalytica.org**. `[CS: FABRICATION RISK]`. Uncorroborated, agenda-shaped, masquerading as an outlet. Do not repeat in any form |
| **"87% of journaling app users abandon within 7 days"** | A Medium personal essay, not a study. `[CS: LOW]`. The real, sourced figure is 70% within 100 days (PMC11694054) — use that |
| **"Therapy records sell for $1,000+ per record on the dark web"** | Single quote from a security vendor's founder, no market data behind it. `[CS: LOW]` |
| **"Speaking is 3–4× faster than typing"** | Repeated across nine vendor blogs, no primary cognitive-science source verified in a journaling context. `[CS: LOW]`. Tagged `[A]` in the brief, never load-bearing |
| **"2024 JMIR study: audio reflection comparable to written"** | Surfaced only via an AI-generated search summary. No authors, no title, no DOI, never fetched. `[CS: LOW]`. This is precisely the fluent-but-unsourced pattern the `[CS:]` apparatus exists to catch |
| **"Frontiers in Psychology" on vocal prosody** | Prosody-as-emotion-signal is a real field (`[CS: HIGH]` as a field claim), but **this specific attribution was never verified** `[CS: LOW]`. Don't cite the journal; cite the field or nothing |
| **Malchiodi's visual-journaling PDF** | Fetch returned undecoded binary. Her specific claims were **never read directly** — what the brief carries is secondary characterization. `[CS: MEDIUM]` at best. Do not quote her |
| **Pizarro (2004)**, "art + writing beats writing alone" | Secondhand citation, original never read, no journal or DOI captured. `[CS: LOW]`. Tempting because it supports the concept — which is exactly why it needs the flag |

---

## Verified arithmetic

Per the 47% rule, every ratio in this packet is grep-computed, never asserted:

- Tag ledger: **29 rows** — 8 `[R]` · 4 `[D]` · 8 `[A]` · 9 `[?]`
- `[R]`+`[D]` = 12/29 = **41.4%**
- `[A]`+`[?]` = 17/29 = **58.6%** — nearly 2× the 30% readiness threshold
- Verified 2026-09-11 by regex count over the ledger table plus `python3` division. *Superseded, not deleted: 28 rows / 57.1%, correct before critic pass 1 split ledger #13 into #13a/#13b.*

## Single-source warning

All counter-evidence against this concept's mechanism rests on **one qualitative study, n=54** (StoryWriter, Study 2). The brief states this rather than dressing it as consensus. It is not fixable by editing — only by finding or running more research, starting with the paywalled writing-vs-drawing comparison above that this pipeline could not read.

Nothing in this packet was validated with users. No seed entry, name, or doodle is real.
