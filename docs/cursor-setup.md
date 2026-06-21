# Cursor MCP Integration

This guide shows how to wire the unified Composio MCP bridge into Cursor via HTTP MCP config emission.

## Prerequisites

- Python 3.10+
- `COMPOSIO_API_KEY` exported in your shell (never commit `ak_*` keys)
- Optional: `COMPOSIO_USER_ID` (defaults to machine hostname)

## Setup

```bash
export COMPOSIO_API_KEY=ak_...          # shell only, never in git
cp config.example.yaml config.yaml
pip install -e ".[dev]"
one-composio-mcp session create --profile phase0_smoke
one-composio-mcp mcp-emit > .cursor/mcp.fragment.json
```

## Merge into Cursor

Copy the `mcpServers` block from the emitted fragment into `~/.cursor/mcp.json` (or your project `.cursor/mcp.json`).

Example emitted config:

```json
{
  "mcpServers": {
    "composio-unified": {
      "url": "https://backend.composio.dev/mcp/sess_...",
      "headers": {
        "x-api-key": "ak_..."
      }
    }
  }
}
```

See also `examples/cursor-mcp.json.example`.

## Commands

| Command | Purpose |
|---------|---------|
| `one-composio-mcp session create` | Create Tool Router session, save state |
| `one-composio-mcp session status` | Show active session |
| `one-composio-mcp mcp-emit` | Print Cursor-compatible MCP JSON |
| `one-composio-mcp connections` | List toolkit connection status |
| `one-composio-mcp authorize <toolkit>` | Start OAuth for a toolkit |
| `one-composio-mcp wait --toolkit <toolkit>` | Block until connection completes |

## Security

- API keys live only in environment variables.
- `config.yaml` is gitignored; use `config.example.yaml` as a template.
- Session state is stored locally in `.one-composio-mcp/active-session.json`.
