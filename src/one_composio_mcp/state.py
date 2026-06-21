import json
from pathlib import Path

from one_composio_mcp.session_manager import SessionInfo

DEFAULT_STATE_PATH = Path(".one-composio-mcp/active-session.json")


def save_active_session(info: SessionInfo, path: Path = DEFAULT_STATE_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(
            {
                "session_id": info.session_id,
                "mcp_url": info.mcp_url,
                "mcp_headers": info.mcp_headers,
                "profile": info.profile,
            }
        ),
        encoding="utf-8",
    )


def load_active_session(path: Path = DEFAULT_STATE_PATH) -> SessionInfo:
    data = json.loads(path.read_text(encoding="utf-8"))
    return SessionInfo(**data)
