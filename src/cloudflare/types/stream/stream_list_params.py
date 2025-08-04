# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["StreamListParams"]


class StreamListParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    asc: bool
    """Lists videos in ascending order of creation."""

    creator: str
    """A user-defined identifier for the media creator."""

    end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Lists videos created before the specified date."""

    include_counts: bool
    """
    Includes the total number of videos associated with the submitted query
    parameters.
    """

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
