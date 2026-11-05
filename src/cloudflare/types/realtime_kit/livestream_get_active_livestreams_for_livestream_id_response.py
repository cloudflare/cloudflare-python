# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["LivestreamGetActiveLivestreamsForLivestreamIDResponse", "Data", "DataLivestream", "DataSession"]


class DataLivestream(BaseModel):
    id: str
    """ID of the livestream."""

    created_at: datetime
    """Timestamp the livestream was created at, in ISO format."""

    disabled: bool
    """Specifies if the livestream is disabled."""

    external_id: str
    """ID of the underlying Cloudflare Stream live input."""

    ingest_server: str
    """The server URL to which the RTMP encoder sends the video and audio data."""

    manual_ingest: bool
    """Specifies if the livestream is ingested manually by an RTMP encoder."""

    meeting_id: Optional[str] = None
    """ID of the meeting being livestreamed, if any."""

    name: Optional[str] = None
    """Name of the livestream."""

    playback_url: str
    """The web address that viewers can use to watch the livestream."""

    status: Literal["LIVE", "IDLE", "ERRORED", "INVOKED", "METRICS_READY"]
    """Status of the livestream."""

    stream_key: str
    """Unique key for accessing each livestream. Empty if the livestream is disabled."""

    updated_at: datetime
    """Timestamp the livestream was last updated at, in ISO format."""


class DataSession(BaseModel):
    id: str
    """ID of the livestream session."""

    created_at: datetime
    """Timestamp the livestream session was created at, in ISO format."""

    err_message: Optional[str] = None
    """Error message, if the livestream session failed."""

    ingest_seconds: float
    """The time duration for which the input was given or the meeting was streamed."""

    invoked_time: Optional[datetime] = None
    """Timestamp the livestream session was invoked at, in ISO format."""

    livestream_id: str
    """ID of the livestream."""

    started_time: Optional[datetime] = None
    """Timestamp the livestream session started at, in ISO format."""

    stopped_time: Optional[datetime] = None
    """Timestamp the livestream session stopped at, in ISO format."""

    updated_at: datetime
    """Timestamp the livestream session was last updated at, in ISO format."""

    viewer_seconds: float
    """The total view time for which the viewers watched the stream."""


class Data(BaseModel):
    livestream: DataLivestream

    session: DataSession


class LivestreamGetActiveLivestreamsForLivestreamIDResponse(BaseModel):
    data: Data

    success: bool
