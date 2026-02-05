# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "RecordingStartRecordingsParams",
    "AudioConfig",
    "InteractiveConfig",
    "RealtimekitBucketConfig",
    "RtmpOutConfig",
    "StorageConfig",
    "VideoConfig",
    "VideoConfigWatermark",
    "VideoConfigWatermarkSize",
]


class RecordingStartRecordingsParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    allow_multiple_recordings: bool
    """By default, a meeting allows only one recording to run at a time.

    Enabling the `allow_multiple_recordings` parameter to true allows you to
    initiate multiple recordings concurrently in the same meeting. This allows you
    to record separate videos of the same meeting with different configurations,
    such as portrait mode or landscape mode.
    """

    audio_config: AudioConfig
    """Object containing configuration regarding the audio that is being recorded."""

    file_name_prefix: str
    """Update the recording file name."""

    interactive_config: InteractiveConfig
    """
    Allows you to add timed metadata to your recordings, which are digital markers
    inserted into a video file to provide contextual information at specific points
    in the content range. The ID3 tags containing this information are available to
    clients on the playback timeline in HLS format. The output files are generated
    in a compressed .tar format.
    """

    max_seconds: int
    """
    Specifies the maximum duration for recording in seconds, ranging from a minimum
    of 60 seconds to a maximum of 24 hours.
    """

    meeting_id: str
    """ID of the meeting to record."""

    realtimekit_bucket_config: RealtimekitBucketConfig

    rtmp_out_config: RtmpOutConfig

    storage_config: Optional[StorageConfig]

    url: str
    """Pass a custom url to record arbitary screen"""

    video_config: VideoConfig


class AudioConfig(TypedDict, total=False):
    """Object containing configuration regarding the audio that is being recorded."""

    channel: Literal["mono", "stereo"]
    """Audio signal pathway within an audio file that carries a specific sound source."""

    codec: Literal["MP3", "AAC"]
    """Codec using which the recording will be encoded.

    If VP8/VP9 is selected for videoConfig, changing audioConfig is not allowed. In
    this case, the codec in the audioConfig is automatically set to vorbis.
    """

    export_file: bool
    """Controls whether to export audio file seperately"""


class InteractiveConfig(TypedDict, total=False):
    """
    Allows you to add timed metadata to your recordings, which are digital markers inserted into a video file to provide contextual information at specific points in the content range. The ID3 tags containing this information are available to clients on the playback timeline in HLS format. The output files are generated in a compressed .tar format.
    """

    type: Literal["ID3"]
    """The metadata is presented in the form of ID3 tags."""


class RealtimekitBucketConfig(TypedDict, total=False):
    enabled: Required[bool]
    """Controls whether recordings are uploaded to RealtimeKit's bucket.

    If set to false, `download_url`, `audio_download_url`, `download_url_expiry`
    won't be generated for a recording.
    """


class RtmpOutConfig(TypedDict, total=False):
    rtmp_url: str
    """RTMP URL to stream to"""


class StorageConfig(TypedDict, total=False):
    type: Required[Literal["aws", "azure", "digitalocean", "gcs", "sftp"]]
    """Type of storage media."""

    access_key: str
    """Access key of the storage medium.

    Access key is not required for the `gcs` storage media type.

    Note that this field is not readable by clients, only writeable.
    """

    auth_method: Literal["KEY", "PASSWORD"]
    """Authentication method used for "sftp" type storage medium"""

    bucket: str
    """Name of the storage medium's bucket."""

    host: str
    """SSH destination server host for SFTP type storage medium"""

    password: str
    """
    SSH destination server password for SFTP type storage medium when auth_method is
    "PASSWORD". If auth_method is "KEY", this specifies the password for the ssh
    private key.
    """

    path: str
    """Path relative to the bucket root at which the recording will be placed."""

    port: float
    """SSH destination server port for SFTP type storage medium"""

    private_key: str
    """
    Private key used to login to destination SSH server for SFTP type storage
    medium, when auth_method used is "KEY"
    """

    region: str
    """Region of the storage medium."""

    secret: str
    """Secret key of the storage medium.

    Similar to `access_key`, it is only writeable by clients, not readable.
    """

    username: str
    """SSH destination server username for SFTP type storage medium"""


class VideoConfigWatermarkSize(TypedDict, total=False):
    """Size of the watermark"""

    height: int
    """Height of the watermark in px"""

    width: int
    """Width of the watermark in px"""


class VideoConfigWatermark(TypedDict, total=False):
    """Watermark to be added to the recording"""

    position: Literal["left top", "right top", "left bottom", "right bottom"]
    """Position of the watermark"""

    size: VideoConfigWatermarkSize
    """Size of the watermark"""

    url: str
    """URL of the watermark image"""


class VideoConfig(TypedDict, total=False):
    codec: Literal["H264", "VP8"]
    """Codec using which the recording will be encoded."""

    export_file: bool
    """Controls whether to export video file seperately"""

    height: int
    """Height of the recording video in pixels"""

    watermark: VideoConfigWatermark
    """Watermark to be added to the recording"""

    width: int
    """Width of the recording video in pixels"""
