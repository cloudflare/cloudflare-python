# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["LivestreamGetAllLivestreamsResponse", "Data", "DataPaging"]


class DataPaging(BaseModel):
    end_offset: Optional[int] = None

    start_offset: Optional[int] = None

    total_count: Optional[int] = None


class Data(BaseModel):
    id: Optional[str] = None
    """The ID of the livestream."""

    created_at: Optional[datetime] = None
    """Timestamp the object was created at. The time is returned in ISO format."""

    disabled: Optional[str] = None
    """Specifies if the livestream was disabled."""

    ingest_server: Optional[str] = None
    """The server URL to which the RTMP encoder sends the video and audio data."""

    meeting_id: Optional[str] = None
    """ID of the meeting."""

    name: Optional[str] = None
    """Name of the livestream."""

    paging: Optional[DataPaging] = None

    playback_url: Optional[str] = None
    """The web address that viewers can use to watch the livestream."""

    status: Optional[Literal["LIVE", "IDLE", "ERRORED", "INVOKED"]] = None

    stream_key: Optional[str] = None
    """Unique key for accessing each livestream."""

    updated_at: Optional[datetime] = None
    """Timestamp the object was updated at. The time is returned in ISO format."""


class LivestreamGetAllLivestreamsResponse(BaseModel):
    data: Optional[Data] = None

    success: Optional[bool] = None
