# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["LivestreamCreateIndependentLivestreamResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """The livestream ID."""

    disabled: Optional[bool] = None
    """Specifies if the livestream was disabled."""

    ingest_server: Optional[str] = None
    """The server URL to which the RTMP encoder should send the video and audio data."""

    meeting_id: Optional[str] = None

    name: Optional[str] = None

    playback_url: Optional[str] = None
    """The web address that viewers can use to watch the livestream."""

    status: Optional[Literal["LIVE", "IDLE", "ERRORED", "INVOKED"]] = None

    stream_key: Optional[str] = None
    """Unique key for accessing each livestream."""


class LivestreamCreateIndependentLivestreamResponse(BaseModel):
    data: Optional[Data] = None

    success: Optional[bool] = None
