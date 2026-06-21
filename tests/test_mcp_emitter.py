import json

from one_composio_mcp.mcp_emitter import emit_cursor_config
from one_composio_mcp.session_manager import SessionInfo


def test_emit_cursor_config():
    info = SessionInfo(
        "sess_1",
        "https://backend/mcp/sess_1",
        {"x-api-key": "ak_test"},
        "phase0_smoke",
    )
    payload = emit_cursor_config(info, server_name="composio-unified")
    assert (
        payload["mcpServers"]["composio-unified"]["url"]
        == "https://backend/mcp/sess_1"
    )
    assert (
        payload["mcpServers"]["composio-unified"]["headers"]["x-api-key"] == "ak_test"
    )
    json.dumps(payload)
