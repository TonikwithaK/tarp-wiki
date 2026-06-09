#!/usr/bin/env bash
set -euo pipefail

QUARTZ_DIR="$HOME/tarp-quartz"
CANON_DIR="$HOME/tarp-wiki/vault/canon"
PAGE_SLUG="${1:-}"

cd "$QUARTZ_DIR"

echo "Syncing Canon → content/..."
rsync -av --delete "$CANON_DIR/" content/

echo "Generating llms.txt..."
python3 scripts/generate_llms_txt.py

if git diff --quiet && git diff --cached --quiet; then
  echo "No changes detected — nothing to deploy."
  exit 0
fi

COMMIT_MSG="canon: promote"
[[ -n "$PAGE_SLUG" ]] && COMMIT_MSG="$COMMIT_MSG [[$PAGE_SLUG]]"

git add -A
git commit -m "$COMMIT_MSG"
git push origin main

echo "Deployed. GitHub Actions will publish in ~60 seconds."
