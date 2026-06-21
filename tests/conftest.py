"""Shared pytest fixtures for one-composio-mcp tests."""

import os
from pathlib import Path

# Project-local temp avoids Windows %TEMP% permission errors (WinError 5).
_project_tmp = Path(__file__).resolve().parent.parent / ".pytest_basetemp"
_project_tmp.mkdir(parents=True, exist_ok=True)
for _var in ("TMP", "TEMP", "TMPDIR"):
    os.environ[_var] = str(_project_tmp)
