# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LiveInput", "Recording", "Rtmps", "RtmpsPlayback", "Srt", "SrtPlayback", "WebRtc", "WebRtcPlayback"]


class Recording(BaseModel):
    allowed_origins: Optional[List[str]] = FieldInfo(alias="allowedOrigins", default=None)
    """Lists the origins allowed to display videos created with this input.

    Enter allowed origin domains in an array and use `*` for wildcard subdomains. An
    empty array allows videos to be viewed on any origin.
    """

    hide_live_viewer_count: Optional[bool] = FieldInfo(alias="hideLiveViewerCount", default=None)
    """
    Disables reporting the number of live viewers when this property is set to
    `true`.
    """

    mode: Optional[Literal["off", "automatic"]] = None
    """Specifies the recording behavior for the live input.

    Set this value to `off` to prevent a recording. Set the value to `automatic` to
    begin a recording and transition to on-demand after Stream Live stops receiving
    input.
    """

    require_signed_urls: Optional[bool] = FieldInfo(alias="requireSignedURLs", default=None)
    """
    Indicates if a video using the live input has the `requireSignedURLs` property
    set. Also enforces access controls on any video recording of the livestream with
    the live input.
    """

    timeout_seconds: Optional[int] = FieldInfo(alias="timeoutSeconds", default=None)
    """
    Determines the amount of time a live input configured in `automatic` mode should
    wait before a recording transitions from live to on-demand. `0` is recommended
    for most use cases and indicates the platform default should be used.
    """


class Rtmps(BaseModel):
    stream_key: Optional[str] = FieldInfo(alias="streamKey", default=None)
    """The secret key to use when streaming via RTMPS to a live input."""

    url: Optional[str] = None
    """The RTMPS URL you provide to the broadcaster, which they stream live video to."""


class RtmpsPlayback(BaseModel):
    stream_key: Optional[str] = FieldInfo(alias="streamKey", default=None)
    """The secret key to use for playback via RTMPS."""

    url: Optional[str] = None
    """The URL used to play live video over RTMPS."""


class Srt(BaseModel):
    passphrase: Optional[str] = None
    """The secret key to use when streaming via SRT to a live input."""

    stream_id: Optional[str] = FieldInfo(alias="streamId", default=None)
    """The identifier of the live input to use when streaming via SRT."""

    url: Optional[str] = None
    """The SRT URL you provide to the broadcaster, which they stream live video to."""


class SrtPlayback(BaseModel):
    passphrase: Optional[str] = None
    """The secret key to use for playback via SRT."""

    stream_id: Optional[str] = FieldInfo(alias="streamId", default=None)
    """The identifier of the live input to use for playback via SRT."""

    url: Optional[str] = None
    """The URL used to play live video over SRT."""


class WebRtc(BaseModel):
    url: Optional[str] = None
    """The WebRTC URL you provide to the broadcaster, which they stream live video to."""


class WebRtcPlayback(BaseModel):
    url: Optional[str] = None
    """The URL used to play live video over WebRTC."""


class LiveInput(BaseModel):
    created: Optional[datetime] = None
    """The date and time the live input was created."""

    delete_recording_after_days: Optional[float] = FieldInfo(alias="deleteRecordingAfterDays", default=None)
    """
    Indicates the number of days after which the live inputs recordings will be
    deleted. When a stream completes and the recording is ready, the value is used
    to calculate a scheduled deletion date for that recording. Omit the field to
    indicate no change, or include with a `null` value to remove an existing
    scheduled deletion.
    """

    meta: Optional[object] = None
    """
    A user modifiable key-value store used to reference other systems of record for
    managing live inputs.
    """

    modified: Optional[datetime] = None
    """The date and time the live input was last modified."""

    recording: Optional[Recording] = None
    """Records the input to a Cloudflare Stream video.

    Behavior depends on the mode. In most cases, the video will initially be
    viewable as a live video and transition to on-demand after a condition is
    satisfied.
    """

    rtmps: Optional[Rtmps] = None
    """Details for streaming to an live input using RTMPS."""

    rtmps_playback: Optional[RtmpsPlayback] = FieldInfo(alias="rtmpsPlayback", default=None)
    """Details for playback from an live input using RTMPS."""

    srt: Optional[Srt] = None
    """Details for streaming to a live input using SRT."""

    srt_playback: Optional[SrtPlayback] = FieldInfo(alias="srtPlayback", default=None)
    """Details for playback from an live input using SRT."""

    status: Optional[
        Literal[
            "connected",
            "reconnected",
            "reconnecting",
            "client_disconnect",
            "ttl_exceeded",
            "failed_to_connect",
            "failed_to_reconnect",
            "new_configuration_accepted",
        ]
    ] = None
    """The connection status of a live input."""

    uid: Optional[str] = None
    """A unique identifier for a live input."""

    web_rtc: Optional[WebRtc] = FieldInfo(alias="webRTC", default=None)
    """Details for streaming to a live input using WebRTC."""

    web_rtc_playback: Optional[WebRtcPlayback] = FieldInfo(alias="webRTCPlayback", default=None)
    """Details for playback from a live input using WebRTC."""
