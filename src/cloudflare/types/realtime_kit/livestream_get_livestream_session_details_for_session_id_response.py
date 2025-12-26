# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["LivestreamGetLivestreamSessionDetailsForSessionIDResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """The livestream ID."""

    created_at: Optional[datetime] = None
    """Timestamp the object was created at. The time is returned in ISO format."""

    err_message: Optional[str] = None
    """The server URL to which the RTMP encoder sends the video and audio data."""

    ingest_seconds: Optional[int] = None
    """Name of the livestream."""

    livestream_id: Optional[str] = None

    started_time: Optional[str] = None
    """Unique key for accessing each livestream."""

    stopped_time: Optional[str] = None
    """The web address that viewers can use to watch the livestream."""

    updated_at: Optional[str] = None
    """Timestamp the object was updated at. The time is returned in ISO format."""

    viewer_seconds: Optional[int] = None
    """Specifies if the livestream was disabled."""


class LivestreamGetLivestreamSessionDetailsForSessionIDResponse(BaseModel):
    data: Optional[Data] = None

    success: Optional[bool] = None
