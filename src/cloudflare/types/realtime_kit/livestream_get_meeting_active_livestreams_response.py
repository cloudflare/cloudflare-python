# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["LivestreamGetMeetingActiveLivestreamsResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """The livestream ID."""

    created_at: Optional[datetime] = None
    """Timestamp the object was created at. The time is returned in ISO format."""

    disabled: Optional[str] = None
    """Specifies if the livestream was disabled."""

    ingest_server: Optional[str] = None
    """The server URL to which the RTMP encoder sends the video and audio data."""

    meeting_id: Optional[str] = None

    name: Optional[str] = None
    """Name of the livestream."""

    playback_url: Optional[str] = None
    """The web address that viewers can use to watch the livestream."""

    status: Optional[Literal["LIVE", "IDLE", "ERRORED", "INVOKED"]] = None

    stream_key: Optional[str] = None
    """Unique key for accessing each livestream."""

    updated_at: Optional[datetime] = None
    """Timestamp the object was updated at. The time is returned in ISO format."""


class LivestreamGetMeetingActiveLivestreamsResponse(BaseModel):
    data: Optional[Data] = None

    success: Optional[bool] = None
