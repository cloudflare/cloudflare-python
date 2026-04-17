# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["StreamListParams"]


class StreamListParams(TypedDict, total=False):
    account_id: str
    """The account identifier tag."""

    id: str
    """Filter by video ID(s). Can be a single ID or a comma-separated list of IDs."""

    after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Alias for 'start'.

    Returns videos created after this date/time (RFC 3339 format).
    """

    asc: bool
    """Lists videos in ascending order of creation."""

    before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Alias for 'end'.

    Returns videos created before this date/time (RFC 3339 format).
    """

    creator: str
    """A user-defined identifier for the media creator."""

    end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Lists videos created before the specified date."""

    include_counts: bool
    """
    Includes the total number of videos associated with the submitted query
    parameters.
    """

    limit: int
    """Maximum number of videos to return (default 1000, max 1000)."""

    live_input_id: str
    """Filter by live input ID to find videos associated with a specific live stream."""

    name: str
    """Filter by video name/UID(s). Can be a single name or a comma-separated list."""

    search: str
    """Provides a partial word match of the `name` key in the `meta` field.

    Slow for medium to large video libraries. May be unavailable for very large
    libraries.
    """

    start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Lists videos created after the specified date."""

    status: Literal["pendingupload", "downloading", "queued", "inprogress", "ready", "error", "live-inprogress"]
    """Specifies the processing status for all quality levels for a video."""

    type: str
    """Specifies whether the video is `vod` or `live`."""

    video_name: str
    """Provides a fast, exact string match on the `name` key in the `meta` field."""
