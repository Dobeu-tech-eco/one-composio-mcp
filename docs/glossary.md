# Glossary — Composio v1 → v3 Term Mapping

Terms evolved across Composio SDK versions. This bridge targets the **v3 Tool Router** API via `composio>=0.10.5`.

| Legacy / informal term | Current term (v3) | In this bridge |
|------------------------|-------------------|----------------|
| Composio API key | `COMPOSIO_API_KEY` env var | Loaded by `config.load_config()`; never in YAML |
| Entity ID | `user_id` | Stable identity for connected accounts; defaults to hostname |
| Connected account ID (`ca_*`) | Connected account | Mapped via `composio.connected_accounts` aliases in config |
| Integration / app | Toolkit | Listed in profile `toolkits` (e.g. `googledrive`, `gmail`) |
| Action | Tool | Exposed through Tool Router MCP session |
| Connect URL / MCP Connect | Tool Router session MCP URL | `session.mcp.url` from `composio.create()` |
| Connect headers | Session MCP headers | `session.mcp.headers` (includes `x-api-key`) |
| OAuth link | Authorization redirect | `session.authorize(toolkit).redirect_url` |
| Rube MCP | Hosted Composio MCP proxy | Alternative; this bridge is self-managed profiles |
| Trigger | Webhook / event (platform) | Not used in v0.1.0 bridge scope |
| Composio.dev dashboard | Composio platform | Where API keys and connected accounts are managed |

## Profile-specific aliases

| Config key | Meaning |
|------------|---------|
| `profiles.<name>.toolkits` | Toolkit slugs passed to `composio.create()` |
| `profiles.<name>.connected_accounts` | Maps toolkit → alias defined under `composio.connected_accounts` |
| `profiles.<name>.tags` | Optional Tool Router tags (e.g. `readOnlyHint`) |
| `default_profile` | Used when `--profile` is omitted |

## File artifacts

| Path | Purpose |
|------|---------|
| `config.yaml` | Local profiles and account aliases (gitignored) |
| `.one-composio-mcp/active-session.json` | Last created session (gitignored) |
| `examples/cursor-mcp.json.example` | Sample emitted MCP fragment |
