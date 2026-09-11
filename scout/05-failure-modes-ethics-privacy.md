# Theme 5 — Failure Modes and Ethics: Mood Inference, On-Device vs. Cloud, Journal Privacy Expectations

## GDPR — the actual legal floor (relevant: Beth works in the UK, GDPR applies per project instructions)
- Mental/emotional-state data inferred from a journal entry qualifies as **special category data** under GDPR Article 9 (health data). [CS: HIGH — this is settled regulatory interpretation, not a contested claim]
- Processing special category data is **prohibited by default**; only specific listed exceptions permit it. [CS: HIGH]
- Valid consent for this category must be **explicit** — referencing the specific special-category processing, not a general ToS checkbox — and meet six conditions: freely given, specific, informed, unambiguous, documented, withdrawable. [CS: HIGH]
- **Direct implication for this concept:** if the doodle-generation pipeline involves any inference about the user's emotional state (which text-to-image-from-journal-entry inherently does — the image has to represent *something* about mood), that inference itself is special-category processing, even if the raw journal text is stored securely. **[ASSUMPTION to name to spec]: "it's just generating a picture" undersells the GDPR exposure — the inference step is the regulated act, not just the storage.**
- No specific primary EU regulatory guidance or DPA (Data Protection Authority) enforcement action naming AI-generated mood art specifically was located. This is an inference from general special-category-data law, not a case directly on point. [CS: MEDIUM]

## Breach / security precedent — real, recent, fetched directly
**Oversecured research, reported via BleepingComputer, summarized by TechRepublic** — [CS: HIGH — fetched and read directly; note Oversecured is a commercial security vendor, so treat the framing as vendor-interested even though the technical findings are specific and datable]
- **10 widely-downloaded Android mental health apps, 14.7 million combined installs**, examined Jan 22–23, 2026.
- **1,575 security flaws found**, "dozens" rated high severity.
- Exposed data categories: therapy session transcripts, CBT exercises, mood tracking histories, medication reminders, **self-harm indicators**, treatment progress scores.
- Technical causes named: insecure inter-app communication, plaintext storage of sensitive data, exposed API endpoints, hardcoded database credentials, weak/cryptographically-insecure encryption.
- App identities withheld pending vendor remediation — i.e., this is disclosed-but-anonymized, not a named-and-shamed list. [CS: HIGH, this specific detail]
- **Unverified figure carried within the same reporting, do not treat as confirmed:** "therapy records sell for $1,000+ per record on the dark web" — single quote attributed to Oversecured's founder, no independent market data behind it in what was fetched. [CS: LOW]

## On-device vs. cloud processing
- No independently-verified primary research located comparing user trust or actual privacy outcomes for on-device vs. cloud-processed journaling specifically. What exists is vendor claims about their own architecture (e.g., "Whisper Notes processes entirely on-device" — a product claim, not independently audited) — see File 02.
- One search result surfaced a claim that Apple's on-device Journal app nonetheless performs "behavioral profiling," sourced to a domain calling itself "cambridgeanalytica.org." **[CS: FABRICATION RISK / do-not-cite]** — this domain name and framing pattern is a strong signal of an unreliable or agenda-driven source masquerading as a credible outlet; it was not independently corroborated and should not be carried into any deliverable. Flagging explicitly rather than silently dropping, per protocol — this is the kind of source that looks citable and isn't.

## Journal-specific privacy expectations
No academic study was located that specifically measures user privacy *expectations* for a journal app as a category (as distinct from mental-health apps generally, or messaging apps generally). This is a real gap. The GDPR analysis above establishes the *legal* floor; it does not establish what users actually *believe* about a journal's privacy when they open one. **Name to spec as [?] Unknown**: "journal" as a category may carry stronger implicit privacy expectations than "app" generally (a paper diary has a lock; a journaling app's private-feeling UI may create expectations the architecture doesn't back up) — this is a reasonable design hypothesis, not a sourced finding.

## Direct implications for a Tier-1 internal prototype
- Because this is internal, non-clinical, and Tier 1/lo-fi: real user emotional/journal data must never be used as seed data. All seed entries, moods, and generated doodles used to demo this concept must be **[TEST DATA]** and fictional, per project rules — no real internal staff journal content, ever, even anonymized.
- If any part of the prototype demo implies real inference-from-text (even mocked), the demo script should say so plainly rather than let a stakeholder assume it's live inference on their own words.
