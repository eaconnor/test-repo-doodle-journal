#!/bin/bash
# check-trace.sh — keeps the gate checklists honest against the canonical intent spec.
#
# Judgment lives in "Intent Specs/doodle-journal.md". Each acceptance criterion in
# ux.md / vision.md / design.md carries a `traces_to:` pointer, and those pointers are
# only safe if drift is detectable. So this checks BOTH directions:
#
#   forward  — every traces_to target actually exists. A pointer into nothing means a
#              criterion is enforcing a requirement that has been renamed or deleted,
#              and it will sit there green forever.
#   backward — every UXI-## requirement in the intent spec is referenced by at least one
#              criterion. An unreferenced requirement is a stated UX intent that nothing
#              verifies, which is the more dangerous direction: it looks covered because
#              it is written down.
#
# Reference syntax inside a `traces_to:` field:
#   UXI-##          a requirement in intent spec §5
#   §N              a section of the canonical intent spec
#   ds:N / ds:N.N   a section of the *local* file (ux.md / design.md now carry their own
#                   research corpus and design system, so they have sections of their own)
#   H-## R-## A-##  a row in OPEN.md
#
# Why the ds: prefix exists. ux.md and design.md used to be thin checklists with no
# sections, so a bare `§5` could only mean the intent spec. Once they grew real content
# they each gained a §5 of their own, and this script resolved `§5` against the intent
# spec regardless — it would have passed a pointer that meant something else entirely.
# The ambiguity was silent, and a silent pass is the failure mode this repo exists to
# document. Local refs are now `ds:` and cannot collide.
#
# Only the traces_to segment of a criterion line is scanned. Prose may say "§4.1" freely.
#
# Exit codes (distinct from the other scripts on purpose):
#   0  traces valid
#   4  broken or orphaned trace
#   5  canonical intent spec missing

# --- project.conf is the single source of project-specific paths. Nothing in
# --- this script is hardcoded to one project; see project.conf.
[ -f ./project.conf ] && . ./project.conf
INTENT="${INTENT_SPEC:-}"
REGISTER="OPEN.md"
DERIVED=("${GATE_1:-ux.md}" "${GATE_2:-vision.md}" "${GATE_3:-design.md}")

if [ -z "$INTENT" ]; then
  echo "BROKEN — no INTENT_SPEC set in project.conf."
  echo "Criteria carry traces_to: pointers; with no canonical document to point"
  echo "at, none of them can be validated. That is a finding, not a skip."
  exit 5
fi

if [ ! -f "$INTENT" ]; then
  echo "BROKEN — canonical intent spec not found at '$INTENT'."
  echo "Gate checklists cannot be validated without the document they trace to."
  exit 5
fi

fail=0

# Pull just the traces_to segment from every acceptance-criterion line in a file.
traces_of() {
  grep -E '^- \[[ x]\] ' "$1" | grep -oE 'traces_to:[^·]*'
}

echo "=== forward: do all traces_to targets exist? ==="
for f in "${DERIVED[@]}"; do
  [ -f "$f" ] || { echo "  SKIP $f (not present)"; continue; }

  t=$(traces_of "$f")
  if [ -z "$t" ]; then
    echo "  BROKEN  $f has acceptance criteria but none carry a traces_to: field"
    fail=1
    continue
  fi

  # UXI ids -> must be defined in the intent spec
  for id in $(echo "$t" | grep -oE 'UXI-[0-9]+' | sort -u); do
    if ! grep -qE "(\*\*$id |\| $id \|)" "$INTENT"; then
      echo "  BROKEN  $f -> $id not defined in $INTENT"; fail=1
    fi
  done

  # §N -> must be a top-level section of the intent spec
  for sec in $(echo "$t" | grep -oE '§[0-9]+' | sed 's/§//' | sort -un); do
    if ! grep -qE "^## $sec\." "$INTENT"; then
      echo "  BROKEN  $f -> §$sec has no '## $sec.' section in $INTENT"; fail=1
    fi
  done

  # ds:N / ds:N.N -> must be a section of THIS file
  for sec in $(echo "$t" | grep -oE 'ds:[0-9]+(\.[0-9]+)?' | sed 's/ds://' | sort -u); do
    if ! grep -qE "^#{2,4} $sec[. ]" "$f"; then
      echo "  BROKEN  $f -> ds:$sec has no matching section heading in $f"; fail=1
    fi
  done

  # rule ids defined locally (CLR-## / C-## / SHD-##) -> must appear in a rule table
  for id in $(echo "$t" | grep -oE '\b(CLR|SHD)-[0-9]+\b' | sort -u); do
    if ! grep -qE "^\| $id \|" "$f"; then
      echo "  BROKEN  $f -> $id is referenced but not defined as a rule row in $f"; fail=1
    fi
  done

  # register rows -> must be a row in OPEN.md (open or resolved)
  for row in $(echo "$t" | grep -oE '\b[HRA]-[0-9]+\b' | sort -u); do
    if ! { [ -f "$REGISTER" ] && grep -q "| $row |" "$REGISTER"; }; then
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
    traces_of "$f" | grep -q "$id" && hits=$((hits+1))
  done
  if [ "$hits" -eq 0 ]; then
    echo "  ORPHAN  $id is stated in the intent spec but no criterion's traces_to enforces it"
    fail=1
  fi
done
[ "$fail" -eq 0 ] && echo "  every UXI requirement is referenced by at least one criterion"

echo ""
if [ "$fail" -eq 1 ]; then
  echo "TRACE CHECK FAILED. A gate checklist has drifted from the intent spec."
  echo "Fix the pointer, or add a criterion for the orphaned requirement. Do not"
  echo "delete the requirement to make this pass."
  exit 4
fi

total=$(echo "$defined" | wc -w | tr -d ' ')
echo "Trace check passed — $total UXI requirements, all defined and all enforced."
exit 0
