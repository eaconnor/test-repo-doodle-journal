#!/bin/bash
# check-value.sh — keeps VALUE.md from rotting into marketing.
#
# A register of design's contribution is only worth anything if it can embarrass
# the function that wrote it. So this script checks the register against itself:
#
#   1. Every row must state a counterfactual. A row without one records activity,
#      not value, and activity is what design is already assumed to be doing.
#   2. Every row must be EVIDENCED or CLAIMED, never unlabelled. The distinction
#      is the whole integrity of the file.
#   3. There must be at least one COST or ZERO row. THIS IS THE LOAD-BEARING
#      CHECK. A value register with no negative rows is a case study, and a case
#      study is what this file exists to replace. If design only ever records its
#      wins, nobody outside design has a reason to believe the wins.
#
# Exit codes, distinct from the other scripts on purpose:
#   0   register is well-formed
#   13  a row is malformed, or the register has no negative rows
#   14  VALUE.md missing

FILE="VALUE.md"

if [ ! -f "$FILE" ]; then
  echo "BROKEN — $FILE not found."
  echo "There is no record of what research or design contributed to this project."
  exit 14
fi

rows=$(awk '/^## Rows/{f=1;next} /^## /{f=0} f && /^\| V-[0-9]+ \|/' "$FILE")
total=$(echo "$rows" | grep -c '^|')

if [ "$total" -eq 0 ]; then
  echo "BROKEN — no V-## rows found between '## Rows' and the next heading."
  exit 13
fi

fail=0

echo "=== VALUE.md — register of research and design contribution ==="
echo

# --- counts by kind
printf "%-12s %s\n" "kind" "rows"
for k in EVIDENCE DECISION PREVENTION CORRECTION COST ZERO; do
  n=$(echo "$rows" | awk -F'|' -v k=" $k " '$3==k{c++} END{print c+0}')
  printf "%-12s %s\n" "$k" "$n"
done

ncost=$(echo "$rows" | awk -F'|' '$3==" COST "||$3==" ZERO "{c++} END{print c+0}')
nevid=$(echo "$rows" | grep -c 'EVIDENCED')
nclaim=$(echo "$rows" | grep -cE '\| CLAIMED')

echo
echo "total rows        $total"
echo "EVIDENCED         $nevid"
echo "CLAIMED           $nclaim"
echo "COST + ZERO       $ncost"
echo

# --- rule 1: every row has a counterfactual
echo "=== rule 1: does every row state a counterfactual? ==="
missing=0
while IFS= read -r line; do
  [ -z "$line" ] && continue
  id=$(echo "$line" | awk -F'|' '{gsub(/ /,"",$2); print $2}')
  kind=$(echo "$line" | awk -F'|' '{gsub(/ /,"",$3); print $3}')
  cf=$(echo "$line" | awk -F'|' '{print $6}' | tr -d ' ')
  # COST rows legitimately have no counterfactual — the cost IS the content
  if [ "$kind" = "COST" ]; then continue; fi
  if [ -z "$cf" ] || [ "$cf" = "—" ] || [ "$cf" = "-" ]; then
    echo "  MISSING  $id has no counterfactual. It records activity, not value."
    missing=$((missing+1))
  fi
done <<< "$rows"
[ "$missing" -eq 0 ] && echo "  all non-COST rows state a counterfactual"
[ "$missing" -gt 0 ] && fail=1

# --- rule 2: every row labelled
echo
echo "=== rule 2: is every row labelled EVIDENCED or CLAIMED? ==="
unlabelled=$(echo "$rows" | grep -vcE 'EVIDENCED|CLAIMED')
if [ "$unlabelled" -gt 0 ]; then
  echo "  $unlabelled row(s) carry neither label:"
  echo "$rows" | grep -vE 'EVIDENCED|CLAIMED' | awk -F'|' '{print "    " $2}'
  fail=1
else
  echo "  every row is labelled"
fi

# --- rule 3: the load-bearing one
echo
echo "=== rule 3: does the register record costs as well as wins? ==="
if [ "$ncost" -eq 0 ]; then
  echo "  FAIL  zero COST or ZERO rows."
  echo
  echo "  A value register with no negative rows is a case study, and a case"
  echo "  study is what this file exists to replace. Design that only records"
  echo "  its wins gives nobody outside design a reason to believe them."
  echo "  Add what this cost, and what did not work."
  fail=1
else
  echo "  $ncost negative row(s) present — the register can embarrass its author"
fi

# --- the ratio, reported not enforced
echo
if [ "$total" -gt 0 ]; then
  pct=$(( 100 * nevid / total ))
  echo "$pct% of rows are EVIDENCED ($nevid of $total)."
  echo "No threshold is enforced on this. CLAIMED rows are legitimate — a"
  echo "prevented harm often cannot be evidenced, because the point is that it"
  echo "did not happen. What matters is that the two are never conflated, which"
  echo "is rule 2."
fi

echo
if [ "$fail" -eq 1 ]; then
  echo "REGISTER MALFORMED. Fix the rows above."
  exit 13
fi
echo "Register well-formed."
exit 0
