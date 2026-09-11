#!/bin/bash
# check-waivers.sh — reads the override ledger and reports calibration.
#
# THE POINT OF THIS SCRIPT IS NOT TO ENFORCE ANYTHING.
#
# Gates here do not stop work. Engineering and design must be able to work on
# other things while research runs, and a gate that idles people for six weeks
# gets removed — deservedly. What this measures instead is whether the gates are
# WORTH OBEYING, using the ledger's own record:
#
#   VINDICATED waiver  -> the bypass was fine  -> evidence the gate is TOO STRICT
#   COSTLY waiver      -> the bypass bit       -> evidence the gate is RIGHT
#
# A gate whose authority comes from evidence outranks one whose authority comes
# from policy. If most waivers are vindicated, loosen the gate — that is a
# finding, not an embarrassment. If none ever are, the gates are theatre.
#
# Exit codes:
#   0   ledger well-formed
#   15  a never event was waived (FATAL row) — that is not a waiver, it is an incident
#   16  ledger malformed, or a bypass has no predicted cost recorded

FILE="WAIVERS.md"
[ -f "$FILE" ] || { echo "BROKEN — $FILE not found. No record of who bypassed what."; exit 16; }

rows=$(awk '/^## Waivers/{f=1;next} /^## /{f=0} f && /^\| W-[0-9]+ \|/' "$FILE")
total=$(echo "$rows" | grep -c '^|')
[ "$total" -eq 0 ] && { echo "BROKEN — no W-## rows found."; exit 16; }

col() { echo "$1" | awk -F'|' -v n="$2" '{print $n}' | sed 's/^ *//; s/ *$//'; }

nvind=$(echo "$rows" | grep -c 'VINDICATED')
ncost=$(echo "$rows" | grep -c 'COSTLY')
npend=$(echo "$rows" | grep -c 'PENDING')
nfatal=$(echo "$rows" | grep -c 'FATAL')
settled=$((nvind + ncost))

echo "=== WAIVERS.md — override ledger ==="
echo
printf "  total waivers   %s\n" "$total"
printf "  VINDICATED      %s   (bypass was fine — gate may be too strict here)\n" "$nvind"
printf "  COSTLY          %s   (bypass bit — gate was right)\n" "$ncost"
printf "  PENDING         %s   (outcome not yet known)\n" "$npend"
printf "  FATAL           %s\n" "$nfatal"
echo

# --- every bypass must name a predicted cost. That is the whole discipline.
echo "=== does every waiver name a risk it accepted? ==="
bad=0
while IFS= read -r r; do
  [ -z "$r" ] && continue
  id=$(col "$r" 2); risk=$(col "$r" 7)
  if [ -z "$risk" ] || [ "$risk" = "—" ]; then
    echo "  MISSING  $id records no accepted risk. That is an undeclared bypass."
    bad=1
  fi
done <<< "$rows"
[ "$bad" -eq 0 ] && echo "  every waiver names the risk it accepted"

# --- calibration, the reason this file exists
echo
echo "=== calibration ==="
if [ "$settled" -eq 0 ]; then
  echo "  No waiver has settled yet. Nothing can be said about whether these"
  echo "  gates are worth obeying. Come back when an outcome is known."
else
  pct=$(( 100 * ncost / settled ))
  echo "  $settled of $total waivers have settled. $pct% were COSTLY."
  echo
  if [ "$pct" -ge 70 ]; then
    echo "  READING: the gates are earning their keep. Most bypasses cost"
    echo "  something real, so the block is carrying information rather than"
    echo "  process. Keep them, and keep logging."
  elif [ "$pct" -le 30 ]; then
    echo "  READING: most bypasses were fine. The gates are too strict and should"
    echo "  be loosened — this is a finding about the gates, not about the people"
    echo "  who went around them. Loosen the specific criteria that keep getting"
    echo "  waived without cost."
  else
    echo "  READING: mixed. Not enough signal to loosen or tighten. Look at WHICH"
    echo "  gates get waived costlessly rather than the aggregate."
  fi
fi

# --- the pattern check: repeated bypasses of the same gate
echo
echo "=== is the same gate being waived repeatedly? ==="
echo "$rows" | awk -F'|' '{g=$5; gsub(/^ *| *$/,"",g); print g}' | sort | uniq -c \
  | sort -rn | awk '$1>1{print "  x" $1 "  " substr($0, index($0,$2))}' | head
echo "  (a gate waived repeatedly is either wrong, or badly placed in the"
echo "   workflow. Either way it is a design problem, not a compliance problem.)"

# --- who
echo
echo "=== attribution ==="
echo "$rows" | awk -F'|' '{w=$4; gsub(/^ *| *$/,"",w); print w}' | sort | uniq -c \
  | sort -rn | sed 's/^/  /'
echo "  Attribution exists so the reasoning survives the person leaving, not to"
echo "  assign blame. A waiver is a legitimate act."

echo
if [ "$nfatal" -gt 0 ]; then
  echo "FATAL row present. A never event was waived — that is an incident, not a"
  echo "waiver. Stop and investigate the mechanism, per check-never.sh."
  exit 15
fi
if [ "$bad" -eq 1 ]; then
  echo "LEDGER MALFORMED — a bypass with no declared risk is the thing this file exists to prevent."
  exit 16
fi
echo "Ledger well-formed. $npend waiver(s) still pending an outcome."
exit 0
