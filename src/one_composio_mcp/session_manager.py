from __future__ import annotations

from dataclasses import dataclass

from one_composio_mcp.composio_client import build_composio_client
from one_composio_mcp.config import BridgeConfig
from one_composio_mcp.profiles import resolve_session_options


@dataclass(frozen=True)
class SessionInfo:
    session_id: str
    mcp_url: str
    mcp_headers: dict[str, str]
    profile: str


class SessionManager:
    def __init__(self, cfg: BridgeConfig) -> None:
        self._cfg = cfg
        self._client = build_composio_client(api_key=cfg.api_key)

    def create_session(self, profile_name: str | None = None) -> SessionInfo:
        profile = profile_name or self._cfg.default_profile
        options = resolve_session_options(self._cfg, profile)
        session = self._client.create(user_id=self._cfg.user_id, **options)
        headers = {
            k: v for k, v in (session.mcp.headers or {}).items() if v is not None
        }
        return SessionInfo(
            session_id=session.session_id,
            mcp_url=session.mcp.url,
            mcp_headers=headers,
            profile=profile,
        )

    def use_session(self, session_id: str):
        return self._client.use(session_id)
