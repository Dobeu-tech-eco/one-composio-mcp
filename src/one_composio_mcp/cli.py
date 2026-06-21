from __future__ import annotations

import typer

from one_composio_mcp.config import load_config
from one_composio_mcp.connections import (
    authorize_toolkit,
    format_auth_link,
    toolkit_status_lines,
)
from one_composio_mcp.mcp_emitter import emit_json
from one_composio_mcp.session_manager import SessionManager
from one_composio_mcp.state import load_active_session, save_active_session

app = typer.Typer(help="Unified Composio MCP bridge")
session_app = typer.Typer(help="Session management")
app.add_typer(session_app, name="session")


@session_app.command("create")
def session_create(profile: str | None = typer.Option(None, "--profile", "-p")) -> None:
    cfg = load_config()
    mgr = SessionManager(cfg)
    info = mgr.create_session(profile)
    save_active_session(info)
    typer.echo(f"Created session: {info.session_id} (profile={info.profile})")
    typer.echo(emit_json(info))


@session_app.command("status")
def session_status() -> None:
    info = load_active_session()
    typer.echo(f"Active session: {info.session_id} (profile={info.profile})")
    typer.echo(f"MCP URL: {info.mcp_url}")


@app.command("connections")
def connections_status() -> None:
    cfg = load_config()
    info = load_active_session()
    session = SessionManager(cfg).use_session(info.session_id)
    result = session.toolkits()
    for line in toolkit_status_lines(result.items):
        typer.echo(line)


@app.command("authorize")
def authorize(toolkit: str) -> None:
    cfg = load_config()
    info = load_active_session()
    session = SessionManager(cfg).use_session(info.session_id)
    url = authorize_toolkit(session, toolkit)
    typer.echo(format_auth_link(toolkit, url))
    typer.echo("Run: one-composio-mcp wait --toolkit " + toolkit)


@app.command("wait")
def wait_for(toolkit: str) -> None:
    cfg = load_config()
    info = load_active_session()
    session = SessionManager(cfg).use_session(info.session_id)
    request = session.authorize(toolkit)
    request.wait_for_connection()
    typer.echo(f"{toolkit}: connected")


@app.command("mcp-emit")
def mcp_emit(server_name: str = "composio-unified") -> None:
    info = load_active_session()
    typer.echo(emit_json(info, server_name=server_name))


if __name__ == "__main__":
    app()
