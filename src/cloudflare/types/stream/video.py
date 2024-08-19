# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .watermark import Watermark
from .allowed_origins import AllowedOrigins

__all__ = ["Video", "Input", "Playback", "Status"]


class Input(BaseModel):
    height: Optional[int] = None
    """The video height in pixels.

    A value of `-1` means the height is unknown. The value becomes available after
    the upload and before the video is ready.
    """

    width: Optional[int] = None
    """The video width in pixels.

    A value of `-1` means the width is unknown. The value becomes available after
    the upload and before the video is ready.
    """


class Playback(BaseModel):
    dash: Optional[str] = None
    """DASH Media Presentation Description for the video."""

    hls: Optional[str] = None
    """The HLS manifest for the video."""


class Status(BaseModel):
    error_reason_code: Optional[str] = FieldInfo(alias="errorReasonCode", default=None)
    """Specifies why the video failed to encode.

    This field is empty if the video is not in an `error` state. Preferred for
    programmatic use.
    """

    error_reason_text: Optional[str] = FieldInfo(alias="errorReasonText", default=None)
    """
    Specifies why the video failed to encode using a human readable error message in
    English. This field is empty if the video is not in an `error` state.
    """

    pct_complete: Optional[str] = FieldInfo(alias="pctComplete", default=None)
    """Indicates the size of the entire upload in bytes.

    The value must be a non-negative integer.
    """

    state: Optional[Literal["pendingupload", "downloading", "queued", "inprogress", "ready", "error"]] = None
    """Specifies the processing status for all quality levels for a video."""


class Video(BaseModel):
    allowed_origins: Optional[List[AllowedOrigins]] = FieldInfo(alias="allowedOrigins", default=None)
    """Lists the origins allowed to display the video.

    Enter allowed origin domains in an array and use `*` for wildcard subdomains.
    Empty arrays allow the video to be viewed on any origin.
    """

    created: Optional[datetime] = None
    """The date and time the media item was created."""

    creator: Optional[str] = None
    """A user-defined identifier for the media creator."""

    duration: Optional[float] = None
    """The duration of the video in seconds.

    A value of `-1` means the duration is unknown. The duration becomes available
    after the upload and before the video is ready.
    """

    input: Optional[Input] = None

    live_input: Optional[str] = FieldInfo(alias="liveInput", default=None)
    """The live input ID used to upload a video with Stream Live."""

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
    """The date and time the media item was last modified."""

    playback: Optional[Playback] = None

    preview: Optional[str] = None
    """The video's preview page URI. This field is omitted until encoding is complete."""

    ready_to_stream: Optional[bool] = FieldInfo(alias="readyToStream", default=None)
    """Indicates whether the video is playable.

    The field is empty if the video is not ready for viewing or the live stream is
    still in progress.
    """

    ready_to_stream_at: Optional[datetime] = FieldInfo(alias="readyToStreamAt", default=None)
    """Indicates the time at which the video became playable.

    The field is empty if the video is not ready for viewing or the live stream is
    still in progress.
    """

    require_signed_urls: Optional[bool] = FieldInfo(alias="requireSignedURLs", default=None)
    """Indicates whether the video can be a accessed using the UID.

    When set to `true`, a signed token must be generated with a signing key to view
    the video.
    """

    scheduled_deletion: Optional[datetime] = FieldInfo(alias="scheduledDeletion", default=None)
    """Indicates the date and time at which the video will be deleted.

    Omit the field to indicate no change, or include with a `null` value to remove
    an existing scheduled deletion. If specified, must be at least 30 days from
    upload time.
    """

    size: Optional[float] = None
    """The size of the media item in bytes."""

    status: Optional[Status] = None
    """Specifies a detailed status for a video.

    If the `state` is `inprogress` or `error`, the `step` field returns `encoding`
    or `manifest`. If the `state` is `inprogress`, `pctComplete` returns a number
    between 0 and 100 to indicate the approximate percent of completion. If the
    `state` is `error`, `errorReasonCode` and `errorReasonText` provide additional
    details.
    """

    thumbnail: Optional[str] = None
    """The media item's thumbnail URI.

    This field is omitted until encoding is complete.
    """

    thumbnail_timestamp_pct: Optional[float] = FieldInfo(alias="thumbnailTimestampPct", default=None)
    """
    The timestamp for a thumbnail image calculated as a percentage value of the
    video's duration. To convert from a second-wise timestamp to a percentage,
    divide the desired timestamp by the total duration of the video. If this value
    is not set, the default thumbnail image is taken from 0s of the video.
    """

    uid: Optional[str] = None
    """A Cloudflare-generated unique identifier for a media item."""

    uploaded: Optional[datetime] = None
    """The date and time the media item was uploaded."""

    upload_expiry: Optional[datetime] = FieldInfo(alias="uploadExpiry", default=None)
    """
    The date and time when the video upload URL is no longer valid for direct user
    uploads.
    """

    watermark: Optional[Watermark] = None
