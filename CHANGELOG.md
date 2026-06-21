# Changelog

All notable changes to one-composio-mcp are documented here.

## [0.1.0] - 2026-06-20

### Added

- Env-only config loader (`config.py`) with YAML profile support
- Phased toolkit profiles (`phase0_smoke` through `phase3_gmail`)
- Tool Router session manager via `composio.create()` / `composio.use()`
- Active session persistence (`.one-composio-mcp/active-session.json`)
- Cursor-compatible HTTP MCP JSON emitter
- Connection helpers: authorize, wait, status
- Typer CLI (`one-composio-mcp`) with session, mcp-emit, and connections commands
- pytest suite with mocked SDK calls
- Documentation: architecture, cursor-setup, FAQ, glossary, AEO schema

### Security

- API keys read from environment only; `config.yaml` is gitignored
- Emitted MCP headers sourced from SDK session, not hand-rolled Connect headers

[0.1.0]: https://github.com/dobeutech/composio-one-mcp-bridge/releases/tag/v0.1.0
