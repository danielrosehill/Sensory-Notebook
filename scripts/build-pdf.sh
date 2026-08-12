#!/usr/bin/env bash
# Build a consolidated PDF of the whole notebook.
#
#   scripts/build-pdf.sh              # today's date
#   scripts/build-pdf.sh 2026-08-12   # a specific date
#
# Produces outputs/consolidated-YYMMDD.md and outputs/consolidated-YYMMDD.pdf.
#
# Requires: python3, pandoc (>= 3.0, for the typst writer), typst.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO"

for tool in python3 pandoc typst; do
  command -v "$tool" >/dev/null || { echo "missing required tool: $tool" >&2; exit 1; }
done

DATE="${1:-$(date +%F)}"
STAMP="$(date -d "$DATE" +%y%m%d)"
MD="outputs/consolidated-${STAMP}.md"
PDF="outputs/consolidated-${STAMP}.pdf"

echo "==> assembling $MD"
python3 scripts/consolidate.py --date "$DATE" >/dev/null

echo "==> typesetting $PDF"
pandoc "$MD" \
  --from=markdown \
  --to=pdf \
  --pdf-engine=typst \
  --template=templates/notebook.typ \
  --output="$PDF"

echo "==> done: $PDF ($(du -h "$PDF" | cut -f1))"
