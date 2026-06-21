#!/usr/bin/env bash
# validate-python.sh
# Run pytest and basic Python validation for one-composio-mcp.
# Usage: ./scripts/validate-python.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$ROOT_DIR"

echo "one-composio-mcp Python Validation"
echo "==================================="
echo

if ! python3 -m pytest --version >/dev/null 2>&1; then
    echo "pytest not found — install dev deps: pip install -e \".[dev]\""
    exit 1
fi

echo "Running pytest..."
python3 -m pytest -q
PASS_COUNT=$(python3 -m pytest -q 2>&1 | tail -1)
echo
echo "Result: $PASS_COUNT"
echo
echo "Validation complete."
