from __future__ import annotations

from one_composio_mcp.config import BridgeConfig


def resolve_session_options(cfg: BridgeConfig, profile_name: str | None = None) -> dict:
    name = profile_name or cfg.default_profile
    if name not in cfg.profiles:
        raise KeyError(f"Unknown profile: {name}")

    profile = cfg.profiles[name]
    connected: dict[str, str] = {}
    for toolkit, alias in profile.connected_accounts.items():
        account_id = cfg.connected_account_aliases.get(alias)
        if not account_id:
            raise ValueError(
                f"Missing connected account alias '{alias}' for toolkit '{toolkit}'"
            )
        connected[toolkit] = account_id

    options: dict = {"toolkits": profile.toolkits}
    if profile.tags:
        options["tags"] = profile.tags
    if connected:
        options["connected_accounts"] = connected
    options["manage_connections"] = True
    return options
