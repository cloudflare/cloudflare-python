# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["BrowserVersionResponse"]


class BrowserVersionResponse(BaseModel):
    browser: str = FieldInfo(alias="Browser")
    """Browser name and version."""

    protocol_version: str = FieldInfo(alias="Protocol-Version")
    """Chrome DevTools Protocol version."""

    user_agent: str = FieldInfo(alias="User-Agent")
    """User agent string."""

    v8_version: str = FieldInfo(alias="V8-Version")
    """V8 JavaScript engine version."""

    web_kit_version: str = FieldInfo(alias="WebKit-Version")
    """WebKit version."""

    web_socket_debugger_url: str = FieldInfo(alias="webSocketDebuggerUrl")
    """WebSocket URL for debugging the browser."""
