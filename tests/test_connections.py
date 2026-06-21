from unittest.mock import MagicMock

from one_composio_mcp.connections import format_auth_link, toolkit_status_lines


def test_format_auth_link():
    assert (
        "[Authorize gmail](https://auth.example)"
        == format_auth_link("gmail", "https://auth.example")
    )


def test_toolkit_status_lines():
    toolkit = MagicMock()
    toolkit.slug = "gmail"
    toolkit.connection.is_active = False
    assert "gmail: disconnected" in toolkit_status_lines([toolkit])[0]
