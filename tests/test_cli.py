from unittest.mock import MagicMock, patch

from typer.testing import CliRunner

from one_composio_mcp.cli import app

runner = CliRunner()


@patch("one_composio_mcp.cli.SessionManager")
@patch("one_composio_mcp.cli.load_config")
@patch("one_composio_mcp.cli.save_active_session")
def test_session_create_prints_json(mock_save, mock_load, mock_mgr_cls):
    mock_cfg = MagicMock()
    mock_load.return_value = mock_cfg
    mock_mgr_cls.return_value.create_session.return_value = MagicMock(
        session_id="sess_x",
        mcp_url="https://u",
        mcp_headers={"x-api-key": "ak"},
        profile="phase0_smoke",
    )
    result = runner.invoke(app, ["session", "create", "--profile", "phase0_smoke"])
    assert result.exit_code == 0
    assert "sess_x" in result.stdout
    assert "mcpServers" in result.stdout
    assert "https://u" in result.stdout
    assert "x-api-key" in result.stdout
    mock_save.assert_called_once()
