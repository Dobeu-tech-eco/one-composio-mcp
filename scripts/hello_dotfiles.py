#!/usr/bin/env python3
"""Hello Dotfiles - Sample Python utility for dobeutech dotfiles demo.

This module demonstrates clean, PEP 8 compliant code with type hints,
docstrings, and defensive practices. It serves as a template and
validation target for the pep8-code-reviewer skill.

Usage:
    python scripts/hello_dotfiles.py [name]
"""

from __future__ import annotations

import sys
from typing import Optional


def greet(name: Optional[str] = None) -> str:
    """Return a friendly greeting.

    Args:
        name: Optional name to greet. Defaults to 'world'.

    Returns:
        A greeting string.
    """
    target: str = name or "world"
    return f"Hello, {target}! Welcome to dobeutech dotfiles."


def main() -> int:
    """Entry point for the hello_dotfiles utility.

    Returns:
        Exit code (0 for success).
    """
    name: Optional[str] = sys.argv[1] if len(sys.argv) > 1 else None
    message: str = greet(name)
    print(message)
    return 0


if __name__ == "__main__":
    sys.exit(main())