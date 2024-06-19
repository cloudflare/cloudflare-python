# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .allowed_origins import AllowedOrigins

__all__ = ["CopyCreateParams", "Watermark"]


class CopyCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    url: Required[str]
    """A video's URL.

    The server must be publicly routable and support `HTTP HEAD` requests and
    `HTTP GET` range requests. The server should respond to `HTTP HEAD` requests
    with a `content-range` header that includes the size of the file.
    """

    allowed_origins: Annotated[List[AllowedOrigins], PropertyInfo(alias="allowedOrigins")]
    """Lists the origins allowed to display the video.

    Enter allowed origin domains in an array and use `*` for wildcard subdomains.
    Empty arrays allow the video to be viewed on any origin.
    """

    creator: str
    """A user-defined identifier for the media creator."""

    meta: object
    """
    A user modifiable key-value store used to reference other systems of record for
    managing videos.
    """

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

    watermark: Watermark

    upload_creator: Annotated[str, PropertyInfo(alias="Upload-Creator")]
    """A user-defined identifier for the media creator."""

    upload_metadata: Annotated[str, PropertyInfo(alias="Upload-Metadata")]
    """Comma-separated key-value pairs following the TUS protocol specification.

    Values are Base-64 encoded. Supported keys: `name`, `requiresignedurls`,
    `allowedorigins`, `thumbnailtimestamppct`, `watermark`, `scheduleddeletion`.
    """


class Watermark(TypedDict, total=False):
    uid: str
    """The unique identifier for the watermark profile."""
