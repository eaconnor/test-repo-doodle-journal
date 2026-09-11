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

  unchecked=$(awk '/^## Acceptance Criteria/{flag=1; next} /^## /{flag=0} flag && /^- \[ \]/{c++} END{print c+0}' "$file")

  if [ "$unchecked" -gt 0 ]; then
    echo "BLOCKED — Gate $gate: $file has $unchecked unchecked acceptance criteria."
    FAIL=1
  else
    echo "PASS — Gate $gate: $file."
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
