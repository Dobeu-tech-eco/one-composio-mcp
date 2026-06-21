# one-composio-mcp

Unified Composio MCP bridge via Tool Router sessions. Creates scoped sessions, manages connections, and emits HTTP MCP config for Cursor and other agents.

## Problem

Composio offers multiple integration paths (Connect URL, Tool Router sessions, Rube). Agents need a reproducible, profile-scoped MCP setup that shares connected accounts across clients without duplicating OAuth or hardcoding toolkit lists.

## Solution

This bridge uses `composio.create(user_id, ...)` to create Tool Router sessions with phased toolkit profiles, persists session state locally, and emits `mcpServers` JSON compatible with Cursor's HTTP MCP support.

## Prerequisites

- Python 3.10+
- Composio API key (`COMPOSIO_API_KEY`, export in shell only)
- Optional: `COMPOSIO_USER_ID` (defaults to machine hostname)

## Quick Start

```bash
export COMPOSIO_API_KEY=ak_...
cp config.example.yaml config.yaml
pip install -e ".[dev]"
one-composio-mcp session create --profile phase0_smoke
one-composio-mcp mcp-emit
```

Merge the emitted `mcpServers` block into `~/.cursor/mcp.json`. See [docs/cursor-setup.md](docs/cursor-setup.md).

## Security

- Never store `ak_*` API keys in `config.yaml` or git.
- `config.yaml` is gitignored; copy from `config.example.yaml`.
- Session headers come from the SDK (`session.mcp.headers`), not hand-rolled Connect headers.

## Phased Rollout

Profiles in `config.example.yaml`:

| Profile | Toolkits |
|---------|----------|
| `phase0_smoke` | composio_search |
| `phase1_cloud` | googledrive, outlook |
| `phase2_onedrive` | + one_drive |
| `phase3_gmail` | + gmail (enable after mailbox cost review) |

## CLI Commands

```bash
one-composio-mcp session create [--profile NAME]
one-composio-mcp session status
one-composio-mcp mcp-emit [--server-name composio-unified]
one-composio-mcp connections
one-composio-mcp authorize <toolkit>
one-composio-mcp wait --toolkit <toolkit>
```

## Development

```bash
pip install -e ".[dev]"
python -m pytest -q
```

## Documentation

- [Architecture](docs/architecture.md)
- [Cursor setup](docs/cursor-setup.md)
- [FAQ](docs/faq.md)
- [Glossary](docs/glossary.md) — Composio v1→v3 term mapping
- [Smoke test log](docs/smoke-test-log.md)
- [CHANGELOG](CHANGELOG.md)
- [AEO schema](docs/aeo/schema.json) — JSON-LD for search engines
- [Composio Tool Router docs](https://docs.composio.dev)

## License

See repository root for license terms.

