# FAQ

## What is one-composio-mcp?

**one-composio-mcp** is a CLI bridge that creates Composio Tool Router sessions with scoped toolkit profiles and emits HTTP MCP configuration for Cursor, Claude Desktop, and other MCP clients that support remote HTTP servers.

## How is this different from Rube?

**Rube** is Composio's hosted MCP proxy with a broad default toolkit set. **one-composio-mcp** gives you explicit, phased profiles (`phase0_smoke` through `phase3_gmail`), local session state, and reproducible `mcp.json` fragments you control. Use Rube for quick exploration; use this bridge when you need scoped rollouts and shared connected accounts across agents.

## Where do I put my Composio API key?

Export `COMPOSIO_API_KEY` in your shell only. Never commit `ak_*` keys to `config.yaml` or git. Copy `config.example.yaml` to `config.yaml` and set `api_key_env: COMPOSIO_API_KEY` — the loader reads the key from the environment at runtime.

## What are phased profiles?

Profiles in `config.example.yaml` control which toolkits each session includes:

| Profile | Toolkits | When to use |
|---------|----------|-------------|
| `phase0_smoke` | composio_search | First live smoke test |
| `phase1_cloud` | googledrive, outlook | Cloud file + mail rollout |
| `phase2_onedrive` | + one_drive | Microsoft OneDrive |
| `phase3_gmail` | + gmail | Full mail (enable after mailbox cost review) |

## Why HTTP MCP instead of stdio?

Tool Router sessions expose an HTTP/SSE MCP endpoint with SDK-provided headers (`session.mcp.headers`). This bridge emits that URL directly — no local stdio proxy. Clients must support HTTP MCP (Cursor does).

## How do connected accounts work?

OAuth bindings attach to a stable `user_id` (from `COMPOSIO_USER_ID` or your hostname), not to individual sessions. Recreate sessions without losing connections. Map aliases in `config.yaml` under `composio.connected_accounts` and reference them per profile.

## What does `session create` output?

It prints a Cursor-ready `mcpServers` JSON block and saves session metadata to `.one-composio-mcp/active-session.json`. Run `mcp-emit` later to re-print the same fragment without calling the API again.

## How do I authorize a toolkit?

```bash
one-composio-mcp authorize googledrive
one-composio-mcp wait --toolkit googledrive
one-composio-mcp connections
```

## Can I run tests without a live API key?

Yes. The pytest suite mocks Composio SDK calls. Live smoke requires `COMPOSIO_API_KEY` — see [smoke-test-log.md](smoke-test-log.md).
