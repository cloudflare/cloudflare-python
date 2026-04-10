# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["SessionGetResponse"]


class SessionGetResponse(BaseModel):
    session_id: str = FieldInfo(alias="sessionId")
    """Session ID."""

    close_reason: Optional[str] = FieldInfo(alias="closeReason", default=None)
    """Reason for session closure."""

    close_reason_text: Optional[str] = FieldInfo(alias="closeReasonText", default=None)
    """Human-readable close reason."""

    connection_end_time: Optional[float] = FieldInfo(alias="connectionEndTime", default=None)
    """Connection end time."""

    connection_id: Optional[str] = FieldInfo(alias="connectionId", default=None)
    """Connection ID."""

    connection_start_time: Optional[float] = FieldInfo(alias="connectionStartTime", default=None)
    """Connection start time."""

    devtools_frontend_url: Optional[str] = FieldInfo(alias="devtoolsFrontendUrl", default=None)
    """DevTools frontend URL."""

    end_time: Optional[float] = FieldInfo(alias="endTime", default=None)
    """Session end time."""

    last_updated: Optional[float] = FieldInfo(alias="lastUpdated", default=None)
    """Last updated timestamp."""

    start_time: Optional[float] = FieldInfo(alias="startTime", default=None)
    """Session start time."""

    web_socket_debugger_url: Optional[str] = FieldInfo(alias="webSocketDebuggerUrl", default=None)
    """WebSocket URL for debugging this target."""
