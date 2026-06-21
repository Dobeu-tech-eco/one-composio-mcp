from pathlib import Path

import os
import pytest

from one_composio_mcp.config import BridgeConfig, load_config


def test_pyproject_declares_package():
    text = Path("pyproject.toml").read_text(encoding="utf-8")
    assert "[project]" in text
    assert "one-composio-mcp" in text
    assert "composio>=" in text


def test_load_config_reads_api_key_from_env(tmp_path, monkeypatch):
    cfg_file = tmp_path / "config.yaml"
    cfg_file.write_text(
        "composio:\n  api_key_env: COMPOSIO_API_KEY\n  default_profile: phase0_smoke\n"
        "profiles:\n  phase0_smoke:\n    toolkits: [composio_search]\n",
        encoding="utf-8",
    )
    monkeypatch.setenv("COMPOSIO_API_KEY", "ak_test_key")
    cfg = load_config(cfg_file)
    assert cfg.api_key == "ak_test_key"
    assert cfg.default_profile == "phase0_smoke"


def test_load_config_raises_without_api_key(tmp_path, monkeypatch):
    cfg_file = tmp_path / "config.yaml"
    cfg_file.write_text(
        "composio:\n  api_key_env: COMPOSIO_API_KEY\nprofiles: {}\n",
        encoding="utf-8",
    )
    monkeypatch.delenv("COMPOSIO_API_KEY", raising=False)
    with pytest.raises(ValueError, match="COMPOSIO_API_KEY"):
        load_config(cfg_file)
