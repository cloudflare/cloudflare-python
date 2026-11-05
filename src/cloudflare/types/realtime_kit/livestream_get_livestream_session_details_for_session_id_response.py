# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["LivestreamGetLivestreamSessionDetailsForSessionIDResponse", "Data"]


class Data(BaseModel):
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


class LivestreamGetLivestreamSessionDetailsForSessionIDResponse(BaseModel):
    data: Data

    success: bool
