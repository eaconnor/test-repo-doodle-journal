# Theme 2 — Voice Capture as Journaling Input: Friction, Privacy, Self-Consciousness, Review Cost

## Speed/friction claim
"Speaking is roughly three to four times faster than typing" — cited across voice-journaling vendor blogs (Reflection.app, Spokenly, Audionotes, June, Empath) as the core friction-reduction argument. [CS: LOW] — this is a widely repeated content-marketing claim; no primary cognitive-science source was surfaced or fetched to verify the 3–4x multiplier specifically in a journaling/reflective-writing context (typing-speed vs. speaking-speed research exists generally in HCI but wasn't independently checked here). Do not carry the specific multiplier into a deliverable without a real citation.

## Claimed comparability of audio vs. written reflection
A "2024 study published in the Journal of Medical Internet Research" is cited (via search-engine synthesis, not fetched) as finding audio-based reflection produces "comparable improvements in emotional awareness" to written journaling with less perceived effort. [CS: LOW — outside training window / not independently verified]. This claim surfaced only through an AI-generated search summary, not a direct citation with authors/title/DOI. **Treat as unconfirmed** until the actual JMIR paper is located and read. Flag explicitly to spec: this is exactly the "fluent but unsourced" pattern the protocol exists to catch.

## Vocal prosody argument
"Vocal prosody carries information about emotional state that pure text cannot represent" — attributed to "Frontiers in Psychology" research, again surfaced via search summary rather than a specific fetched paper. [CS: LOW] — plausible and consistent with general affective-computing literature (prosody-as-emotion-signal is a real, well-established sub-field), but the specific citation was not verified. Prosody-emotion research broadly is [CS: HIGH] as a field claim; this specific attribution is [CS: LOW].

## Privacy structure — where voice fails
"Privacy depends on three separate decisions: where audio is captured, where text is created, and where the journal is stored or synced" — framing from Spokenly blog. [CS: MEDIUM] — useful analytical frame, vendor-sourced, not independently validated, but internally coherent and matches general mobile-privacy architecture logic.
- Ambient/self-consciousness friction ("tools that feel surveilled make people less honest") — stated as a design claim in vendor content, not tied to a specific study. [CS: LOW].
- On-device processing example named: "Whisper Notes processes entirely on-device" (OpenAI Whisper model run locally) — [CS: MEDIUM, product claim, not independently verified against Whisper Notes' actual architecture].
- Encryption example named: "Reflection [app] uses AES-256 encryption" — [CS: MEDIUM, vendor claim].

## What was NOT found
- No research located on review/skim cost specifically — i.e., whether people actually go back and re-read/re-listen to voice journal entries, and how that compares to skimming text. This is a real gap for this concept, since voice-to-doodle removes even the option of skimming text later. **Name this gap directly to spec as [?] Unknown** — it is central to whether the doodle-output idea solves a real problem (can't skim audio) or just relocates it (can you skim a doodle any better?).
- No research located on self-consciousness/embarrassment speaking aloud about one's day in a private-but-recorded context specifically for journaling (as opposed to general voice-assistant literature).

## [WOBBLY]
This entire theme's evidence base is nine vendor blog posts (Reflection, Spokenly, Audionotes, Empath, June, JournalingHabit, VoiceScriber, SpeakWise) plus two unfetched academic citations surfaced by search-engine synthesis. There is no independently verified primary research in this file. Every vendor claim above should be read as marketing copy that happens to be directionally plausible, not evidence.
