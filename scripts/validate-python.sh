#!/usr/bin/env bash
# validate-python.sh
# Portable validation script for Python files in dobeutech dotfiles.
# Checks syntax and provides guidance for PEP 8 / style.
# Usage: ./scripts/validate-python.sh [path/to/file.py or dir]
# Part of dobeutech dotfiles - aligns with Ona and pep8-code-reviewer skill

set -euo pipefail

TARGET="${1:-.}"

echo "🐍 dobeutech Python Validation"
echo "=============================="
echo "Target: $TARGET"
echo

# Find Python files (simple portable method for demo)
PY_FILES=()
for file in $(find "$TARGET" -type f -name "*.py" ! -path "*/.*" 2>/dev/null | head -20); do
    PY_FILES+=("$file")
done

if [ ${#PY_FILES[@]} -eq 0 ]; then
    echo "No Python files found in $TARGET"
    exit 0
fi

echo "Found ${#PY_FILES[@]} Python file(s) to check..."
echo

for file in "${PY_FILES[@]}"; do
    echo "🔍 Checking: $file"
    
    # Syntax check
    if python3 -m py_compile "$file" 2>/dev/null; then
        echo "  ✅ Syntax OK"
    else
        echo "  ❌ Syntax error - run: python3 -m py_compile $file"
        python3 -m py_compile "$file" || true
        continue
    fi
    
    # Basic line length hint (PEP 8 recommends 79, black uses 88)
    LONG_LINES=$(awk 'length > 88 {print NR": "length" chars"}' "$file" | head -3)
    if [ -n "$LONG_LINES" ]; then
        echo "  ⚠️  Lines over 88 chars (consider black formatter):"
        echo "$LONG_LINES" | sed 's/^/     /'
    fi
    
    echo
done

echo "✅ Basic validation complete."
echo

echo "For full PEP 8 review, use the pep8-code-reviewer skill (structured feedback)."
echo "Recommended tools (install once):"
echo "  pip install black isort flake8"
echo "  black . && isort . && flake8 ."
echo

echo "Pre-commit hook recommended for automatic checks."