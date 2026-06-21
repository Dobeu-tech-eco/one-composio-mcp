from __future__ import annotations

import os
import socket
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True)
class ProfileConfig:
    toolkits: list[str]
    tags: list[str] = field(default_factory=list)
    connected_accounts: dict[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class BridgeConfig:
    api_key: str
    user_id: str
    default_profile: str
    profiles: dict[str, ProfileConfig]
    connected_account_aliases: dict[str, str] = field(default_factory=dict)


def _resolve_user_id(raw: dict[str, Any]) -> str:
    env_name = raw.get("user_id_env", "COMPOSIO_USER_ID")
    return os.environ.get(env_name) or socket.gethostname()


def load_config(path: Path | None = None) -> BridgeConfig:
    config_path = path or Path("config.yaml")
    raw: dict[str, Any] = {}
    if config_path.exists():
        raw = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}

    composio_raw = raw.get("composio", {})
    api_key_env = composio_raw.get("api_key_env", "COMPOSIO_API_KEY")
    api_key = os.environ.get(api_key_env)
    if not api_key:
        raise ValueError(
            f"{api_key_env} is required; never store ak_* keys in config.yaml"
        )

    profiles_raw = raw.get("profiles", {})
    profiles: dict[str, ProfileConfig] = {}
    for name, pdata in profiles_raw.items():
        profiles[name] = ProfileConfig(
            toolkits=list(pdata.get("toolkits", [])),
            tags=list(pdata.get("tags", [])),
            connected_accounts=dict(pdata.get("connected_accounts", {})),
        )

    return BridgeConfig(
        api_key=api_key,
        user_id=_resolve_user_id(composio_raw),
        default_profile=composio_raw.get("default_profile", "phase0_smoke"),
        profiles=profiles,
        connected_account_aliases=dict(composio_raw.get("connected_accounts", {})),
    )
