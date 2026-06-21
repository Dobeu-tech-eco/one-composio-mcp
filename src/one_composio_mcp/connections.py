from __future__ import annotations


def format_auth_link(toolkit: str, redirect_url: str) -> str:
    return f"[Authorize {toolkit}]({redirect_url})"


def toolkit_status_lines(toolkits) -> list[str]:
    lines: list[str] = []
    for tk in toolkits:
        active = bool(getattr(getattr(tk, "connection", None), "is_active", False))
        state = "connected" if active else "disconnected"
        lines.append(f"{tk.slug}: {state}")
    return lines


def authorize_toolkit(session, toolkit: str) -> str:
    request = session.authorize(toolkit)
    return request.redirect_url
