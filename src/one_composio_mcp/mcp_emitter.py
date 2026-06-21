from __future__ import annotations

import json

from one_composio_mcp.session_manager import SessionInfo


def emit_cursor_config(info: SessionInfo, server_name: str = "composio-unified") -> dict:
    return {
        "mcpServers": {
            server_name: {
                "url": info.mcp_url,
                "headers": info.mcp_headers,
            }
        }
    }


def emit_json(info: SessionInfo, server_name: str = "composio-unified") -> str:
    return json.dumps(emit_cursor_config(info, server_name), indent=2)
