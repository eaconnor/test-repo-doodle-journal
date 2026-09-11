# HAZARDS.md — the hazard register, read by `scripts/check-risk.py`

What actually goes wrong, to whom, and how badly. **Not** a criteria count — `ux-score.py` does that. A project can be 90% conformant and carry a critical hazard, because conformance is measured against what you thought to write down and hazards are not.

`exposure` is per-destination on purpose and that is the load-bearing column. An Art. 9 hazard has exposure **0** at an internal demo with a mocked pipeline and **1.0** the moment a real person discloses. One number for "risk" is a number waiting to be quoted in the wrong room.

`severity`: 1 annoying · 2 harmful · 3 serious · 4 critical. **Any severity-4 hazard with non-zero exposure is ship-blocking regardless of the aggregate** — criticals do not average away, which is why the verdict is not a threshold on a total.

`floor` marks hazards that hold whether or not the concept is right (accessibility, lawfulness, data integrity). FLOOR is never gated on problem validation.

Every row must name a real source. A hypothetical hazard belongs in a risk workshop, not here.

## Hazards

| id | kind | severity | floor | exp_demo | exp_pilot | exp_prod | what | source | mitigation |
|---|---|---|---|---|---|---|---|---|---|
| RSK-01 | CLAIM | 3 | fit | 0.8 | 0.6 | 0.4 | The artifact is read as evidence the concept works. Its own numbers (70.37% / 70.97%) are evidence AGAINST it, and they sit on the page next to a working demo. | prototypes/doodle-journal/SOURCES.md; README 'not a stand-alone deliverable'; MC-04. The repo names this as the foreseeable misuse. | FidelityBadge above the fold, the red no-data panel, and never forwarding the HTML without its brief. Partially mitigated; the residual risk is a screenshot in a deck. |
| RSK-02 | EXCLUSION | 3 | FLOOR | 0.5 | 1.0 | 1.0 | Live accessibility and design violations, including no focus style anywhere and an unlabelled describe-input textarea. A keyboard or screen-reader user cannot reliably complete the core task. Live count: run `python3 scripts/check-design.py`. | scripts/check-design.py (exit 6); T4 audit found the unlabelled textarea, which no design.md criterion names. | FLOOR work. Not gated on problem validation. Fix before any destination that includes a real user. |
| RSK-03 | LEGAL | 4 | FLOOR | 0.0 | 1.0 | 1.0 | Inferring emotional state from a journal entry is GDPR Art. 9 special-category processing. The consent copy is a UI pattern, not a lawful Art. 9 disclosure, and no qualified reviewer has seen it. | OPEN.md H-02; design.md G3-22; scout/05. Exposure is 0 at an internal demo because the pipeline is mocked — no inference occurs. | Named reviewer sign-off, or descope inference. There is no engineering fix for a consent defect. |
| RSK-04 | LEGAL | 4 | FLOOR | 0.0 | 1.0 | 1.0 | No retention or deletion SLA exists for an entry, its doodle, or derived inference data. Nothing states how long anything is kept. | OPEN.md H-03; design.md G3-23; spec.md FR-010 NEEDS CLARIFICATION. | A specified, sourced timing. Blocks any real-data destination. |
| RSK-05 | HARM | 3 | fit | 0.1 | 0.9 | 0.9 | A generated image misrepresents a person's own emotional disclosure in a way they find unsettling. 70.97% used negative language; participants reported actively avoiding images they found grotesque. | SRC-001 PMC9810434, fetched and read. n=54. | Per-entry consent (UXI-10), one-tap discard (UXI-03), entry text always primary (UXI-01). These reduce the cost of the failure; they do not reduce its rate. Rate is R-01/R-02, untested. |
| RSK-06 | INVESTMENT | 2 | fit | 0.7 | 0.7 | 0.7 | The core mechanism may simply not work. The nearest primary study found 70.37% judged generated images irrelevant to their own narrative, and the predicted-most-likely test outcome is re-scope-or-kill. | SRC-001; ux.md ds:6.3 kill criteria; OPEN.md R-01, R-02. | Run the reaction test before funding a build. This hazard is cheapest to retire and nothing is doing it — H-01 is unresolved. |
| RSK-07 | DECISION | 2 | fit | 0.6 | 0.9 | 1.0 | Decisions only a person can make are standing open. An agent or a team that proceeds past them has substituted a default for a decision nobody made. Live count: run `./check-blocked.sh`. | ./check-blocked.sh (exit 2); OPEN.md HUMAN rows. | Answer them or record declining to. check-blocked.sh already detects this; nothing enforces it outside a speckit hook. |
| RSK-08 | EVIDENCE | 2 | fit | 0.5 | 0.8 | 1.0 | 58.6% of tagged claims are [A] or [?] — roughly twice the 30% readiness threshold. For eng this is a change-risk map: the consent string, the retention number and the whole generation pipeline are all likely to move. | briefs/doodle-journal.brief.md tag ledger, 17 of 29, grep-verified. | Build a seam wherever the evidence is thin. Do not hardcode a value that rests on an [A] claim. |

## Counts

Computed, never asserted — run `python3 scripts/check-risk.py <destination>`.
