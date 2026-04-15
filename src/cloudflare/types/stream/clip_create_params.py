# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .allowed_origins import AllowedOrigins

__all__ = ["ClipCreateParams", "Watermark"]


class ClipCreateParams(TypedDict, total=False):
    account_id: str
    """The account identifier tag."""

    clipped_from_video_uid: Required[Annotated[str, PropertyInfo(alias="clippedFromVideoUID")]]
    """The unique video identifier (UID)."""

    end_time_seconds: Required[Annotated[int, PropertyInfo(alias="endTimeSeconds")]]
    """Specifies the end time for the video clip in seconds."""

    start_time_seconds: Required[Annotated[int, PropertyInfo(alias="startTimeSeconds")]]
    """Specifies the start time for the video clip in seconds."""

    allowed_origins: Annotated[SequenceNotStr[AllowedOrigins], PropertyInfo(alias="allowedOrigins")]
    """Lists the origins allowed to display the video.

    Enter allowed origin domains in an array and use `*` for wildcard subdomains.
    Empty arrays allow the video to be viewed on any origin.
    """

    creator: str
    """A user-defined identifier for the media creator."""

    input: str
    """A video's URL. Preferred over 'url'."""

    meta: object
    """
    A user modifiable key-value store used to reference other systems of record for
    managing videos.
    """

    name: str
    """A name for the video."""

    require_signed_urls: Annotated[bool, PropertyInfo(alias="requireSignedURLs")]
    """Indicates whether the video can be a accessed using the UID.

    When set to `true`, a signed token must be generated with a signing key to view
    the video.
    """

    scheduled_deletion: Annotated[Union[str, datetime], PropertyInfo(alias="scheduledDeletion", format="iso8601")]
    """Indicates the date and time at which the video will be deleted.

    Omit the field to indicate no change, or include with a `null` value to remove
    an existing scheduled deletion. If specified, must be at least 30 days from
    upload time.
    """

    thumbnail_timestamp_pct: Annotated[float, PropertyInfo(alias="thumbnailTimestampPct")]
    """
    The timestamp for a thumbnail image calculated as a percentage value of the
    video's duration. To convert from a second-wise timestamp to a percentage,
    divide the desired timestamp by the total duration of the video. If this value
    is not set, the default thumbnail image is taken from 0s of the video.
    """

    url: str
    """A video's URL (legacy field, use 'input' instead)."""

    watermark: Watermark


class Watermark(TypedDict, total=False):
    uid: str
    """The unique identifier for the watermark profile."""
