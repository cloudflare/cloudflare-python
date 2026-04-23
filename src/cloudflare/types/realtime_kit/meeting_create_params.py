# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "MeetingCreateParams",
    "AIConfig",
    "AIConfigSummarization",
    "AIConfigTranscription",
    "RecordingConfig",
    "RecordingConfigAudioConfig",
    "RecordingConfigLiveStreamingConfig",
    "RecordingConfigRealtimekitBucketConfig",
    "RecordingConfigStorageConfig",
    "RecordingConfigVideoConfig",
    "RecordingConfigVideoConfigWatermark",
    "RecordingConfigVideoConfigWatermarkSize",
]


class MeetingCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    ai_config: AIConfig
    """
    The AI Config allows you to customize the behavior of meeting transcriptions and
    summaries
    """

    live_stream_on_start: Optional[bool]
    """Specifies if the meeting should start getting livestreamed on start."""

    persist_chat: bool
    """
    If a meeting is set to persist_chat, meeting chat would remain for a week within
    the meeting space.
    """

    record_on_start: Optional[bool]
    """
    Specifies if the meeting should start getting recorded as soon as someone joins
    the meeting.
    """

    recording_config: RecordingConfig
    """Recording Configurations to be used for this meeting.

    This level of configs takes higher preference over App level configs on the
    RealtimeKit developer portal.
    """

    session_keep_alive_time_in_secs: float
    """
    Time in seconds, for which a session remains active, after the last participant
    has left the meeting.
    """

    summarize_on_end: bool
    """Automatically generate summary of meetings using transcripts.

    Requires Transcriptions to be enabled, and can be retrieved via Webhooks or
    summary API.
    """

    title: Optional[str]
    """Title of the meeting"""


class AIConfigSummarization(TypedDict, total=False):
    """Summary Config"""

    summary_type: Literal[
        "general",
        "team_meeting",
        "sales_call",
        "client_check_in",
        "interview",
        "daily_standup",
        "one_on_one_meeting",
        "lecture",
        "code_review",
    ]
    """Defines the style of the summary, such as general, team meeting, or sales call."""

    text_format: Literal["plain_text", "markdown"]
    """Determines the text format of the summary, such as plain text or markdown."""

    word_limit: int
    """Sets the maximum number of words in the meeting summary."""


class AIConfigTranscription(TypedDict, total=False):
    """Transcription Configurations"""

    keywords: SequenceNotStr[str]
    """Adds specific terms to improve accurate detection during transcription."""

    language: Literal["en-US", "en-IN", "de", "hi", "sv", "ru", "pl", "el", "fr", "nl"]
    """Specifies the language code for transcription to ensure accurate results."""

    profanity_filter: bool
    """Control the inclusion of offensive language in transcriptions."""


class AIConfig(TypedDict, total=False):
    """
    The AI Config allows you to customize the behavior of meeting transcriptions and summaries
    """

    summarization: AIConfigSummarization
    """Summary Config"""

    transcription: AIConfigTranscription
    """Transcription Configurations"""


class RecordingConfigAudioConfig(TypedDict, total=False):
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


class RecordingConfigLiveStreamingConfig(TypedDict, total=False):
    rtmp_url: str
    """RTMP URL to stream to"""


class RecordingConfigRealtimekitBucketConfig(TypedDict, total=False):
    enabled: Required[bool]
    """Controls whether recordings are uploaded to RealtimeKit's bucket.

    If set to false, `download_url`, `audio_download_url`, `download_url_expiry`
    won't be generated for a recording.
    """


class RecordingConfigStorageConfig(TypedDict, total=False):
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


class RecordingConfigVideoConfigWatermarkSize(TypedDict, total=False):
    """Size of the watermark"""

    height: int
    """Height of the watermark in px"""

    width: int
    """Width of the watermark in px"""


class RecordingConfigVideoConfigWatermark(TypedDict, total=False):
    """Watermark to be added to the recording"""

    position: Literal["left top", "right top", "left bottom", "right bottom"]
    """Position of the watermark"""

    size: RecordingConfigVideoConfigWatermarkSize
    """Size of the watermark"""

    url: str
    """URL of the watermark image"""


class RecordingConfigVideoConfig(TypedDict, total=False):
    codec: Literal["H264", "VP8"]
    """Codec using which the recording will be encoded."""

    export_file: bool
    """Controls whether to export video file seperately"""

    height: int
    """Height of the recording video in pixels"""

    watermark: RecordingConfigVideoConfigWatermark
    """Watermark to be added to the recording"""

    width: int
    """Width of the recording video in pixels"""


class RecordingConfig(TypedDict, total=False):
    """Recording Configurations to be used for this meeting.

    This level of configs takes higher preference over App level configs on the RealtimeKit developer portal.
    """

    audio_config: RecordingConfigAudioConfig
    """Object containing configuration regarding the audio that is being recorded."""

    file_name_prefix: str
    """Adds a prefix to the beginning of the file name of the recording."""

    live_streaming_config: RecordingConfigLiveStreamingConfig

    max_seconds: float
    """
    Specifies the maximum duration for recording in seconds, ranging from a minimum
    of 60 seconds to a maximum of 24 hours.
    """

    realtimekit_bucket_config: RecordingConfigRealtimekitBucketConfig

    storage_config: Optional[RecordingConfigStorageConfig]

    video_config: RecordingConfigVideoConfig
