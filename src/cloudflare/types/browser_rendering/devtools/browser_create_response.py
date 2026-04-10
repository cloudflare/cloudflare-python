# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["BrowserCreateResponse"]


class BrowserCreateResponse(BaseModel):
    session_id: str = FieldInfo(alias="sessionId")
    """Browser session ID."""

    web_socket_debugger_url: Optional[str] = FieldInfo(alias="webSocketDebuggerUrl", default=None)
    """WebSocket URL for the session."""
