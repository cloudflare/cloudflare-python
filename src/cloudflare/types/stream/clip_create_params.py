# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .allowed_origins import AllowedOrigins

__all__ = ["ClipCreateParams", "Watermark"]


class ClipCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    clipped_from_video_uid: Required[Annotated[str, PropertyInfo(alias="clippedFromVideoUID")]]
    """The unique video identifier (UID)."""

    end_time_seconds: Required[Annotated[int, PropertyInfo(alias="endTimeSeconds")]]
    """Specifies the end time for the video clip in seconds."""

    start_time_seconds: Required[Annotated[int, PropertyInfo(alias="startTimeSeconds")]]
    """Specifies the start time for the video clip in seconds."""

    allowed_origins: Annotated[List[AllowedOrigins], PropertyInfo(alias="allowedOrigins")]
    """Lists the origins allowed to display the video.

    Enter allowed origin domains in an array and use `*` for wildcard subdomains.
    Empty arrays allow the video to be viewed on any origin.
    """

    creator: str
    """A user-defined identifier for the media creator."""

    max_duration_seconds: Annotated[int, PropertyInfo(alias="maxDurationSeconds")]
    """The maximum duration in seconds for a video upload.

    Can be set for a video that is not yet uploaded to limit its duration. Uploads
    that exceed the specified duration will fail during processing. A value of `-1`
    means the value is unknown.
    """

    require_signed_urls: Annotated[bool, PropertyInfo(alias="requireSignedURLs")]
    """Indicates whether the video can be a accessed using the UID.

    When set to `true`, a signed token must be generated with a signing key to view
    the video.
    """

    thumbnail_timestamp_pct: Annotated[float, PropertyInfo(alias="thumbnailTimestampPct")]
    """
    The timestamp for a thumbnail image calculated as a percentage value of the
    video's duration. To convert from a second-wise timestamp to a percentage,
    divide the desired timestamp by the total duration of the video. If this value
    is not set, the default thumbnail image is taken from 0s of the video.
    """

    watermark: Watermark


class Watermark(TypedDict, total=False):
    uid: str
    """The unique identifier for the watermark profile."""
