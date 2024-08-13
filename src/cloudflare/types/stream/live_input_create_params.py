# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["LiveInputCreateParams", "Recording"]


class LiveInputCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    default_creator: Annotated[str, PropertyInfo(alias="defaultCreator")]
    """Sets the creator ID asssociated with this live input."""

    delete_recording_after_days: Annotated[float, PropertyInfo(alias="deleteRecordingAfterDays")]
    """
    Indicates the number of days after which the live inputs recordings will be
    deleted. When a stream completes and the recording is ready, the value is used
    to calculate a scheduled deletion date for that recording. Omit the field to
    indicate no change, or include with a `null` value to remove an existing
    scheduled deletion.
    """

    meta: object
    """
    A user modifiable key-value store used to reference other systems of record for
    managing live inputs.
    """

    recording: Recording
    """Records the input to a Cloudflare Stream video.

    Behavior depends on the mode. In most cases, the video will initially be
    viewable as a live video and transition to on-demand after a condition is
    satisfied.
    """


class Recording(TypedDict, total=False):
    allowed_origins: Annotated[List[str], PropertyInfo(alias="allowedOrigins")]
    """Lists the origins allowed to display videos created with this input.

    Enter allowed origin domains in an array and use `*` for wildcard subdomains. An
    empty array allows videos to be viewed on any origin.
    """

    hide_live_viewer_count: Annotated[bool, PropertyInfo(alias="hideLiveViewerCount")]
    """
    Disables reporting the number of live viewers when this property is set to
    `true`.
    """

    mode: Literal["off", "automatic"]
    """Specifies the recording behavior for the live input.

    Set this value to `off` to prevent a recording. Set the value to `automatic` to
    begin a recording and transition to on-demand after Stream Live stops receiving
    input.
    """

    require_signed_urls: Annotated[bool, PropertyInfo(alias="requireSignedURLs")]
    """
    Indicates if a video using the live input has the `requireSignedURLs` property
    set. Also enforces access controls on any video recording of the livestream with
    the live input.
    """

    timeout_seconds: Annotated[int, PropertyInfo(alias="timeoutSeconds")]
    """
    Determines the amount of time a live input configured in `automatic` mode should
    wait before a recording transitions from live to on-demand. `0` is recommended
    for most use cases and indicates the platform default should be used.
    """
