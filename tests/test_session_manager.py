from unittest.mock import MagicMock, patch

from one_composio_mcp.config import BridgeConfig, ProfileConfig
from one_composio_mcp.session_manager import SessionInfo, SessionManager


@patch("one_composio_mcp.session_manager.build_composio_client")
def test_create_session_calls_composio_create(mock_build_client):
    mock_session = MagicMock()
    mock_session.session_id = "sess_abc"
    mock_session.mcp.url = "https://backend.composio.dev/mcp/sess_abc"
    mock_session.mcp.headers = {"x-api-key": "ak_test"}
    mock_client = MagicMock()
    mock_client.create.return_value = mock_session
    mock_build_client.return_value = mock_client

    cfg = BridgeConfig(
        api_key="ak_test",
        user_id="user-1",
        default_profile="phase0_smoke",
        profiles={"phase0_smoke": ProfileConfig(toolkits=["composio_search"])},
    )
    mgr = SessionManager(cfg)
    result = mgr.create_session()

    mock_build_client.assert_called_once_with(api_key="ak_test")
    mock_client.create.assert_called_once()
    assert result.session_id == "sess_abc"
    assert result.mcp_url == "https://backend.composio.dev/mcp/sess_abc"


def test_save_and_load_active_session(tmp_path):
    from one_composio_mcp.state import load_active_session, save_active_session

    info = SessionInfo(
        "sess_1", "https://example/mcp", {"x-api-key": "ak"}, "phase0_smoke"
    )
    path = tmp_path / "state.json"
    save_active_session(info, path)
    loaded = load_active_session(path)
    assert loaded.session_id == "sess_1"
