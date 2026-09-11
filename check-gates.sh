#!/bin/bash
# check-gates.sh — a mechanical gate check, not a vibe check.
# Run this before /speckit-plan or /speckit-implement. If it exits 1, stop.

FAIL=0

check_file() {
  local file="$1"
  local gate="$2"

  if [ ! -f "$file" ]; then
    echo "BLOCKED — Gate $gate: $file does not exist."
    FAIL=1
    return
  fi

  # The heading may carry a section number once a gate file grows into a real
  # document ("## 9. Acceptance Criteria"). Anchoring on the bare string made
  # this awk match nothing and report a confident PASS — a false green, which is
  # worse than a false red. Caught 2026-09-11 when design.md gained §§1-8.
  local pat='/^## +([0-9]+\. +)?Acceptance Criteria/'
  unchecked=$(awk "$pat"'{flag=1; next} /^## /{flag=0} flag && /^- \[ \]/{c++} END{print c+0}' "$file")
  total=$(awk "$pat"'{flag=1; next} /^## /{flag=0} flag && /^- \[[ x]\]/{c++} END{print c+0}' "$file")

  if [ "$total" -eq 0 ]; then
    echo "BLOCKED — Gate $gate: $file has no parsable acceptance criteria."
    echo "         Expected a '## Acceptance Criteria' heading (a leading section"
    echo "         number is fine) followed by '- [ ]' / '- [x]' rows. Zero rows"
    echo "         is reported as a failure on purpose: an unparsable gate file"
    echo "         would otherwise pass silently."
    FAIL=1
    return
  fi

  if [ "$unchecked" -gt 0 ]; then
    echo "BLOCKED — Gate $gate: $file has $unchecked of $total acceptance criteria unchecked."
    FAIL=1
  else
    echo "PASS — Gate $gate: $file ($total of $total checked)."
  fi
}

check_file "ux.md" "1 (right problem)"
check_file "vision.md" "2 (right thing)"
check_file "design.md" "3 (right build)"

echo ""
if [ "$FAIL" -eq 1 ]; then
  echo "Blocked. Fix the unchecked boxes above before proceeding."
  exit 1
fi

echo "All three gates pass. Clear to proceed."
exit 0
