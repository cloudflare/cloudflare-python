# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MeetingGetResponse", "Data", "Paging"]


class Data(BaseModel):
    id: str
    """ID of the meeting."""

    created_at: datetime
    """Timestamp the object was created at. The time is returned in ISO format."""

    updated_at: datetime
    """Timestamp the object was updated at. The time is returned in ISO format."""

    live_stream_on_start: Optional[bool] = None
    """Specifies if the meeting should start getting livestreamed on start."""

    persist_chat: Optional[bool] = None
    """Specifies if Chat within a meeting should persist for a week."""

    record_on_start: Optional[bool] = None
    """
    Specifies if the meeting should start getting recorded as soon as someone joins
    the meeting.
    """

    session_keep_alive_time_in_secs: Optional[float] = None
    """
    Time in seconds, for which a session remains active, after the last participant
    has left the meeting.
    """

    status: Optional[Literal["ACTIVE", "INACTIVE"]] = None
    """Whether the meeting is `ACTIVE` or `INACTIVE`.

    Users will not be able to join an `INACTIVE` meeting.
    """

    summarize_on_end: Optional[bool] = None
    """Automatically generate summary of meetings using transcripts.

    Requires Transcriptions to be enabled, and can be retrieved via Webhooks or
    summary API.
    """

    title: Optional[str] = None
    """Title of the meeting."""


class Paging(BaseModel):
    end_offset: float

    start_offset: float

    total_count: float


class MeetingGetResponse(BaseModel):
    data: List[Data]

    paging: Paging

    success: bool
