# Phase 0 Smoke Test Log

**Date:** 2026-06-20  
**Status:** Ready for user — unit tests pass; live API verification pending

## Prerequisites

- Python 3.10+ with editable install: `pip install -e ".[dev]"`
- Composio API key with Tool Router access
- Cursor (or other HTTP MCP client)

## User Action Required

Run these steps in PowerShell or bash. Replace the placeholder with your real key — **never commit it**.

### 1. Set environment

**PowerShell:**

```powershell
$env:COMPOSIO_API_KEY = "YOUR_KEY_HERE"
cd C:\Users\jswil\repos\composio-one-mcp-bridge\one-composio-mcp
```

**bash:**

```bash
export COMPOSIO_API_KEY=YOUR_KEY_HERE
cd one-composio-mcp
```

### 2. Create local config

```bash
cp config.example.yaml config.yaml
```

### 3. Create smoke session

```bash
one-composio-mcp session create --profile phase0_smoke
```

Expected: JSON with `mcpServers.composio-unified.url` and `headers.x-api-key`.

### 4. Emit MCP config (optional re-print)

```bash
one-composio-mcp mcp-emit
```

### 5. Merge into Cursor

Copy the `mcpServers` block into `%USERPROFILE%\.cursor\mcp.json` (Windows) or `~/.cursor/mcp.json`. See [cursor-setup.md](cursor-setup.md).

### 6. Verify in Cursor

Restart Cursor or reload MCP servers. Confirm Composio tools appear in the MCP tools list.

### 7. Record results below

| Step | Pass/Fail | Notes |
|------|-----------|-------|
| session create | | |
| mcp-emit | | |
| Cursor MCP load | | |
| composio_search tool | | |

## Automated Test Baseline

Unit tests (mock-only, no live API):

```bash
python -m pytest -q
```

All tests must pass before running live smoke.

## Results

_Not yet run against live Composio API. Complete the checklist above and fill in the results table._
