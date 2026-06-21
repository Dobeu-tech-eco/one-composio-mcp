"""Shared pytest fixtures for one-composio-mcp tests."""

import os
from pathlib import Path

# Project-local basetemp avoids Windows %TEMP% permission errors (WinError 5).
_project_tmp = Path(__file__).resolve().parent.parent / ".pytest-tmp"
_project_tmp.mkdir(parents=True, exist_ok=True)
for _var in ("TMP", "TEMP", "TMPDIR"):
    os.environ[_var] = str(_project_tmp)


def pytest_configure(config) -> None:
    config.option.basetemp = str(_project_tmp)
