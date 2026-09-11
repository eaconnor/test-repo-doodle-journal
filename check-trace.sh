#!/bin/bash
# check-trace.sh — keeps the derived gate checklists honest against the canonical intent spec.
#
# ux.md / vision.md / design.md hold no reasoning: every criterion carries a
# `traces_to:` pointer into "Intent Specs/doodle-journal.md" (or OPEN.md), which is
# canonical. Derived files are only safe if drift is detectable, so this checks
# BOTH directions:
#
#   forward  — every traces_to target actually exists. A pointer into nothing means
#              a criterion is enforcing a requirement that has been renamed or deleted,
#              and it will sit there green forever.
#   backward — every UXI-## requirement in the intent spec is referenced by at least
#              one criterion. An unreferenced requirement is a stated UX intent that
#              nothing verifies, which is the more dangerous direction: it looks
#              covered because it is written down.
#
# Exit codes (distinct from the other scripts on purpose):
#   0  traces valid
#   4  broken or orphaned trace
#   5  canonical intent spec missing

INTENT="Intent Specs/doodle-journal.md"
REGISTER="OPEN.md"
DERIVED=("ux.md" "vision.md" "design.md")

if [ ! -f "$INTENT" ]; then
  echo "BROKEN — canonical intent spec not found at '$INTENT'."
  echo "Derived checklists cannot be validated without the document they derive from."
  exit 5
fi

fail=0

echo "=== forward: do all traces_to targets exist? ==="
for f in "${DERIVED[@]}"; do
  [ -f "$f" ] || { echo "  SKIP $f (not present)"; continue; }

  # UXI ids
  for id in $(grep -oE 'UXI-[0-9]+' "$f" | sort -u); do
    if grep -q "\*\*$id " "$INTENT" || grep -q "| $id |" "$INTENT"; then
      :
    else
      echo "  BROKEN  $f -> $id not defined in $INTENT"; fail=1
    fi
  done

  # section refs like §5 or §2.3 -> require '## N.' to exist
  for sec in $(grep -oE '§[0-9]+' "$f" | sed 's/§//' | sort -un); do
    if ! grep -qE "^## $sec\." "$INTENT"; then
      echo "  BROKEN  $f -> §$sec has no '## $sec.' section in $INTENT"; fail=1
    fi
  done

  # register rows like OPEN.md H-01
  for row in $(grep -oE '\b[HRA]-[0-9]+\b' "$f" | sort -u); do
    if [ -f "$REGISTER" ] && grep -q "| $row |" "$REGISTER"; then
      :
    else
      echo "  BROKEN  $f -> $row not found as a row in $REGISTER"; fail=1
    fi
  done
done
[ "$fail" -eq 0 ] && echo "  all forward traces resolve"

echo ""
echo "=== backward: is every UXI requirement enforced somewhere? ==="
defined=$(grep -oE 'UXI-[0-9]+' "$INTENT" | sort -u)
for id in $defined; do
  hits=0
  for f in "${DERIVED[@]}"; do
    [ -f "$f" ] || continue
    grep -q "$id" "$f" && hits=$((hits+1))
  done
  if [ "$hits" -eq 0 ]; then
    echo "  ORPHAN  $id is stated in the intent spec but no derived criterion enforces it"
    fail=1
  fi
done
[ "$fail" -eq 0 ] && echo "  every UXI requirement is referenced by at least one criterion"

echo ""
if [ "$fail" -eq 1 ]; then
  echo "TRACE CHECK FAILED. A derived checklist has drifted from the intent spec."
  echo "Fix the pointer, or add a criterion for the orphaned requirement. Do not"
  echo "delete the requirement to make this pass."
  exit 4
fi

total=$(echo "$defined" | wc -w | tr -d ' ')
echo "Trace check passed — $total UXI requirements, all defined and all enforced."
exit 0
