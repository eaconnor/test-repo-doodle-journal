#!/bin/bash
# check-never.sh — never events, and the reason there are only seven.
#
# BORROWED FROM PATIENT SAFETY, DELIBERATELY. A "never event" in healthcare is an
# incident that should never occur: wrong-site surgery, a retained instrument. The
# discipline works because of four properties, and all four matter here:
#
#   1. The list is SHORT. NHS England runs about fifteen for an entire health
#      service. Seven is right for a project.
#   2. Each is UNAMBIGUOUS. You do not convene a meeting to decide whether the
#      wrong site was operated on.
#   3. There is NO ACCEPTABLE RATE. Not "reduce by half" — zero. A never event is
#      never averaged into a metric, because averaging is how a serious rare
#      failure disappears behind a good aggregate.
#   4. Every occurrence is INVESTIGATED, not scored.
#
# IS THIS TOO STRICT? That was the right question to ask, and the answer is: a
# never-event list is only too strict when the list is wrong. The failure mode is
# INFLATION. Declare forty never events and people route around all forty, and the
# concept is dead — worse than never having had it, because now the word means
# nothing. So every candidate below had to pass three tests:
#
#     (a) unambiguous — no judgement call about whether it happened
#     (b) detectable — by a script, or by a named person on a named artifact
#     (c) genuinely never acceptable — NO legitimate exception exists
#
# Things that FAILED those tests, and are deliberately NOT never events:
#
#   "Building before Gate 1 passes"        — has a legitimate exception. Tier 1
#                                            builds to LEARN. That is the point of
#                                            the tier system. This is a FIT cap
#                                            (check-eng.sh EG-3), not a never event.
#   "Shipping with open OPEN.md rows"      — would fire permanently and therefore
#                                            teach everyone to ignore the script.
#   "Running a pipeline step out of order" — bad, and it happened in this repo, but
#                                            it is recoverable and occasionally
#                                            justified. That makes it a REPORTABLE
#                                            DEVIATION, tier 2 below.
#
# The two-tier split is what keeps tier 1 credible. Without somewhere to put
# "serious but excusable," everything migrates into tier 1 and tier 1 dies.
#
# Exit codes:
#   0   no never event detected
#   20  a never event has occurred — stop and investigate, do not score
#
# Optional argument: destination (internal-demo | pilot | production). Some never
# events are scoped to a real user being present. Defaults to internal-demo.

DEST="${1:-internal-demo}"
FIRED=0
REPORTED=0

hr() { printf '%.0s='  {1..72}; echo; }

hr
echo "NEVER EVENTS — zero acceptable rate, investigate every occurrence"
echo "destination: $DEST"
hr

# ---------------------------------------------------------------- NE-1
# The most important one, and the only one that is fully mechanical.
echo
echo "NE-1  A gate criterion was ticked while the HUMAN decision it waits on is"
echo "      still open."
echo "      Why never: this is inferring a decision that belongs to a person. It"
echo "      is the single failure the HUMAN/RESEARCH split exists to prevent, and"
echo "      it is invisible afterwards — the box looks the same either way."
echo
if [ -f OPEN.md ]; then
  openh=$(awk '/^## Open rows/{f=1;next} /^## /{f=0} f && /^\| H-[0-9]+ \| HUMAN \|/' OPEN.md)
  hit=0
  while IFS= read -r row; do
    [ -z "$row" ] && continue
    hid=$(echo "$row" | awk -F'|' '{gsub(/ /,"",$2); print $2}')
    blocks=$(echo "$row" | awk -F'|' '{print $6}')
    for crit in $(echo "$blocks" | grep -oE 'G[123]-[0-9]+'); do
      for f in ux.md vision.md design.md; do
        [ -f "$f" ] || continue
        if grep -qE "^- \[x\] $crit " "$f"; then
          echo "  FIRED  $crit is ticked in $f, but $hid is unresolved."
          hit=1; FIRED=1
        fi
      done
    done
  done <<< "$openh"
  [ "$hit" -eq 0 ] && echo "  clear — no criterion blocked by an open HUMAN row is ticked"
fi

# ---------------------------------------------------------------- NE-2
echo
echo "NE-2  A criterion is ticked while a script reports the rule it asserts is"
echo "      violated in the build."
echo "      Why never: a false green is worse than a red. A red gate stops work;"
echo "      a false green certifies a defect and every downstream artifact"
echo "      inherits the certification. This repo committed it twice in one day."
echo
if [ -f scripts/check-design.py ] && [ -f design.md ]; then
  out=$(python3 scripts/check-design.py 2>/dev/null)
  vblock=$(echo "$out" | awk '/^=== [0-9]+ VIOLATION/{f=1;next} /^=== /{f=0} f')
  hit=0
  # Any rule id named inside a live violation, cross-checked against ticked boxes
  for rule in $(echo "$vblock" | grep -oE '\b(G3-[0-9]+|CLR-0[12]|SHD-0[0-9]|UXI-[0-9]+)\b' | sort -u); do
    ticked=$(grep -E "^- \[x\] .*(traces_to|verified_by).*$rule" design.md | head -1)
    if [ -n "$ticked" ]; then
      cid=$(echo "$ticked" | awk '{print $3}')
      echo "  FIRED  $cid is ticked, but check-design.py reports a live $rule violation."
      hit=1; FIRED=1
    fi
  done
  [ "$hit" -eq 0 ] && echo "  clear — no ticked criterion contradicts a live linter violation"
fi

# ---------------------------------------------------------------- NE-3
echo
echo "NE-3  A claim contradicted by its own primary source is still cited as"
echo "      support."
echo "      Why never: this is not a confidence problem, it is a false statement"
echo "      with a citation attached, which is more persuasive than an uncited one."
echo
if [ -f OPEN.md ]; then
  hit=0
  if grep -q 'FABRICATION RISK' OPEN.md; then
    # Pizarro is the live instance. Check it is not still cited as support.
    if grep -rqE 'art \+ writing beats writing alone|art and writing produced larger' \
        ux.md briefs/*.md 2>/dev/null; then
      echo "  FIRED  a claim marked FABRICATION RISK in OPEN.md is still cited as support."
      hit=1; FIRED=1
    fi
  fi
  [ "$hit" -eq 0 ] && echo "  clear — no FABRICATION RISK claim is still being used as support"
fi

# ---------------------------------------------------------------- NE-4
echo
echo "NE-4  The work claims validation while the participant count is zero."
echo "      Why never: it converts an untested concept into a licence to spend,"
echo "      and it is unrecoverable — nobody unhears 'it tested well'."
echo
hit=0
for f in ux.md vision.md design.md README.md; do
  [ -f "$f" ] || continue
  # assertions, not prohibitions and not descriptions of other people's claims
  bad=$(grep -inE '\b(we|this|it) (have |has )?(validated|proven|tested)\b' "$f" \
        | grep -viE 'not |never |zero |forbid|prohibit|may not|must not')
  if [ -n "$bad" ]; then
    echo "  FIRED  $f asserts validation:"
    echo "$bad" | sed 's/^/         /'
    hit=1; FIRED=1
  fi
done
[ "$hit" -eq 0 ] && echo "  clear — no artifact asserts validation of this concept"

# ---------------------------------------------------------------- NE-5
echo
echo "NE-5  A FLOOR accessibility failure reaches a real user."
echo "      Why never: it is exclusion, not a defect. Scoped to a destination —"
echo "      an internal demo with known FLOOR failures is a choice, shipping them"
echo "      to a person is not."
echo
if [ "$DEST" = "internal-demo" ]; then
  echo "  not applicable at internal-demo (no real user). Re-run with pilot."
elif [ -f check-eng.sh ]; then
  ./check-eng.sh >/dev/null 2>&1
  if [ $? -eq 10 ]; then
    echo "  FIRED  check-eng.sh EG-1 fails and destination is '$DEST'."
    FIRED=1
  else
    echo "  clear"
  fi
fi

# ---------------------------------------------------------------- NE-6
echo
echo "NE-6  Special-category data is processed without a reviewed lawful basis."
echo "      Why never: it is unlawful, not risky. There is no engineering fix and"
echo "      no internal justification that makes it acceptable."
echo
if [ "$DEST" = "internal-demo" ]; then
  echo "  not applicable at internal-demo — the pipeline is mocked, no inference"
  echo "  occurs, so no Art. 9 processing happens."
elif grep -qE '^\| H-02 \| HUMAN \|' OPEN.md 2>/dev/null; then
  echo "  FIRED  H-02 (Art. 9 consent copy reviewed) is unresolved and destination"
  echo "         is '$DEST'. The inference step is the regulated act."
  FIRED=1
else
  echo "  clear"
fi

# ---------------------------------------------------------------- NE-7
echo
echo "NE-7  Real user data is used as seed data, or participant data is reused"
echo "      outside its consented purpose."
echo "      Why never: purpose limitation is not a preference, and consent cannot"
echo "      be granted retroactively by the team that wants the data."
echo
if [ -f prototypes/doodle-journal/doodle-journal.html ]; then
  n=$(grep -c '\[TEST DATA\]' prototypes/doodle-journal/doodle-journal.html)
  echo "  $n [TEST DATA] tags present in the build."
  echo "  PARTIAL DETECTION ONLY. A script can confirm the tags exist; it cannot"
  echo "  confirm the content behind them is fictional. This never event is"
  echo "  human-attested, and saying so is better than implying coverage that"
  echo "  does not exist."
fi

# ================================================================ tier 2
echo
hr
echo "REPORTABLE DEVIATIONS — tier 2. Log with a reason; do not stop the line."
hr
echo
echo "These exist so tier 1 stays short. Each is serious and each has a"
echo "legitimate exception, so none belongs above. All four have occurred in this"
echo "repo and are recorded rather than tidied away."
echo
echo "  RD-1  A pipeline step ran out of order."
echo "        Occurred: build was started before the pre-build critic returned,"
echo "        defeating the purpose of a pre-build gate. Both of that critic's"
echo "        FAILs then had to be hand-patched into a finished artifact."
echo
echo "  RD-2  A gate was authored after the artifact it grades."
echo "        Occurred: design.md v0.1 was written FROM the finished build by"
echo "        critic pass 2, so Gate 3 graded the artifact on its own terms."
echo "        Recorded as OPEN.md A-03, not fixed retroactively."
echo
echo "  RD-3  A verified_by command does not settle the claim beside it."
echo "        Occurred four times in one session. The claim was true each time;"
echo "        the stated check was not. This is the most common defect in the"
echo "        whole apparatus and the least visible, because both halves look"
echo "        fine in isolation."
echo
echo "  RD-4  A fix was applied where the requirement pointed, not everywhere the"
echo "        misreading lived."
echo "        Occurred: five defects introduced while hand-patching, caught by a"
echo "        later critic pass."
echo
if [ -f OPEN.md ] && grep -q 'A-03' OPEN.md; then
  REPORTED=$((REPORTED+1))
fi

# ================================================================ verdict
echo
hr
if [ "$FIRED" -eq 1 ]; then
  echo "NEVER EVENT DETECTED at destination '$DEST'."
  echo
  echo "Do not score this, do not average it, and do not add it to a backlog."
  echo "Stop, establish how it happened, and fix the mechanism that allowed it —"
  echo "not just the instance. A never event that gets triaged is a never event"
  echo "that will recur."
  exit 20
fi
echo "No never event detected at destination '$DEST'."
echo
echo "This is a narrow statement. Seven never events is a floor, not a quality"
echo "bar — NE-7 is only partially detectable and NE-3 checks one known instance."
echo "Passing here means nothing catastrophic was caught. It does not mean the"
echo "work is good; that is what the other eight scripts are for."
exit 0
