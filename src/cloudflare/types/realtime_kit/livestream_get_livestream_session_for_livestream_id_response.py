# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "LivestreamGetLivestreamSessionForLivestreamIDResponse",
    "Data",
    "DataLivestream",
    "DataPaging",
    "DataSession",
]


class DataLivestream(BaseModel):
    id: Optional[str] = None
    """ID of the livestream."""

    created_at: Optional[str] = None
    """Timestamp the object was created at. The time is returned in ISO format."""

    disabled: Optional[str] = None
    """Specifies if the livestream was disabled."""

    ingest_server: Optional[str] = None
    """The server URL to which the RTMP encoder sends the video and audio data."""

    meeting_id: Optional[str] = None
    """The ID of the meeting."""

    name: Optional[str] = None
    """Name of the livestream."""

    playback_url: Optional[str] = None
    """The web address that viewers can use to watch the livestream."""

    status: Optional[Literal["LIVE", "IDLE", "ERRORED", "INVOKED"]] = None

    stream_key: Optional[str] = None
    """Unique key for accessing each livestream."""

    updated_at: Optional[str] = None
    """Timestamp the object was updated at. The time is returned in ISO format."""


class DataPaging(BaseModel):
    end_offset: Optional[int] = None

    start_offset: Optional[int] = None

    total_count: Optional[int] = None


class DataSession(BaseModel):
    id: Optional[str] = None
    """ID of the session."""

    created_at: Optional[datetime] = None
    """Timestamp the object was created at. The time is returned in ISO format."""

    err_message: Optional[str] = None

    ingest_seconds: Optional[float] = None
    """The time duration for which the input was given or the meeting was streamed."""

    invoked_time: Optional[datetime] = None
    """Timestamp the object was invoked. The time is returned in ISO format."""

    livestream_id: Optional[str] = None

    started_time: Optional[datetime] = None
    """Timestamp the object was started. The time is returned in ISO format."""

    stopped_time: Optional[datetime] = None
    """Timestamp the object was stopped. The time is returned in ISO format."""

    updated_at: Optional[datetime] = None
    """Timestamp the object was updated at. The time is returned in ISO format."""

    viewer_seconds: Optional[float] = None
    """The total view time for which the viewers watched the stream."""


class Data(BaseModel):
    livestream: Optional[DataLivestream] = None

    paging: Optional[DataPaging] = None

    session: Optional[DataSession] = None


class LivestreamGetLivestreamSessionForLivestreamIDResponse(BaseModel):
    data: Optional[Data] = None

    success: Optional[bool] = None
