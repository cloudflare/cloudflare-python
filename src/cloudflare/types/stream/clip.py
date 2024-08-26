# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .allowed_origins import AllowedOrigins

__all__ = ["Clip", "Playback", "Watermark"]


class Playback(BaseModel):
    dash: Optional[str] = None
    """DASH Media Presentation Description for the video."""

    hls: Optional[str] = None
    """The HLS manifest for the video."""


class Watermark(BaseModel):
    uid: Optional[str] = None
    """The unique identifier for the watermark profile."""


class Clip(BaseModel):
    allowed_origins: Optional[List[AllowedOrigins]] = FieldInfo(alias="allowedOrigins", default=None)
    """Lists the origins allowed to display the video.

    Enter allowed origin domains in an array and use `*` for wildcard subdomains.
    Empty arrays allow the video to be viewed on any origin.
    """

    clipped_from_video_uid: Optional[str] = FieldInfo(alias="clippedFromVideoUID", default=None)
    """The unique video identifier (UID)."""

    created: Optional[datetime] = None
    """The date and time the clip was created."""

    creator: Optional[str] = None
    """A user-defined identifier for the media creator."""

    end_time_seconds: Optional[int] = FieldInfo(alias="endTimeSeconds", default=None)
    """Specifies the end time for the video clip in seconds."""

    max_duration_seconds: Optional[int] = FieldInfo(alias="maxDurationSeconds", default=None)
    """The maximum duration in seconds for a video upload.

    Can be set for a video that is not yet uploaded to limit its duration. Uploads
    that exceed the specified duration will fail during processing. A value of `-1`
    means the value is unknown.
    """

    meta: Optional[object] = None
    """
    A user modifiable key-value store used to reference other systems of record for
    managing videos.
    """

    modified: Optional[datetime] = None
    """The date and time the live input was last modified."""

    playback: Optional[Playback] = None

    preview: Optional[str] = None
    """The video's preview page URI. This field is omitted until encoding is complete."""

    require_signed_urls: Optional[bool] = FieldInfo(alias="requireSignedURLs", default=None)
    """Indicates whether the video can be a accessed using the UID.

    When set to `true`, a signed token must be generated with a signing key to view
    the video.
    """

    start_time_seconds: Optional[int] = FieldInfo(alias="startTimeSeconds", default=None)
    """Specifies the start time for the video clip in seconds."""

    status: Optional[Literal["pendingupload", "downloading", "queued", "inprogress", "ready", "error"]] = None
    """Specifies the processing status for all quality levels for a video."""

    thumbnail_timestamp_pct: Optional[float] = FieldInfo(alias="thumbnailTimestampPct", default=None)
    """
    The timestamp for a thumbnail image calculated as a percentage value of the
    video's duration. To convert from a second-wise timestamp to a percentage,
    divide the desired timestamp by the total duration of the video. If this value
    is not set, the default thumbnail image is taken from 0s of the video.
    """

    watermark: Optional[Watermark] = None
