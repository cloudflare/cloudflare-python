# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["LivestreamStartLivestreamingAMeetingResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """The livestream ID."""

    ingest_server: Optional[str] = None
    """The server URL to which the RTMP encoder sends the video and audio data."""

    playback_url: Optional[str] = None
    """The web address that viewers can use to watch the livestream."""

    status: Optional[Literal["LIVE", "IDLE", "ERRORED", "INVOKED"]] = None

    stream_key: Optional[str] = None
    """Unique key for accessing each livestream."""


class LivestreamStartLivestreamingAMeetingResponse(BaseModel):
    data: Optional[Data] = None

    success: Optional[bool] = None
