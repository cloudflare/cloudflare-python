# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "MeetingUpdateMeetingByIDResponse",
    "Data",
    "DataAIConfig",
    "DataAIConfigSummarization",
    "DataAIConfigTranscription",
    "DataRecordingConfig",
    "DataRecordingConfigAudioConfig",
    "DataRecordingConfigLiveStreamingConfig",
    "DataRecordingConfigRealtimekitBucketConfig",
    "DataRecordingConfigStorageConfig",
    "DataRecordingConfigVideoConfig",
    "DataRecordingConfigVideoConfigWatermark",
    "DataRecordingConfigVideoConfigWatermarkSize",
]


class DataAIConfigSummarization(BaseModel):
    """Summary Config"""

    summary_type: Optional[
        Literal[
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
    ] = None
    """Defines the style of the summary, such as general, team meeting, or sales call."""

    text_format: Optional[Literal["plain_text", "markdown"]] = None
    """Determines the text format of the summary, such as plain text or markdown."""

    word_limit: Optional[int] = None
    """Sets the maximum number of words in the meeting summary."""


class DataAIConfigTranscription(BaseModel):
    """Transcription Configurations"""

    keywords: Optional[List[str]] = None
    """Adds specific terms to improve accurate detection during transcription."""

    language: Optional[Literal["en-US", "en-IN", "de", "hi", "sv", "ru", "pl", "el", "fr", "nl"]] = None
    """Specifies the language code for transcription to ensure accurate results."""

    profanity_filter: Optional[bool] = None
    """Control the inclusion of offensive language in transcriptions."""


class DataAIConfig(BaseModel):
    """
    The AI Config allows you to customize the behavior of meeting transcriptions and summaries
    """

    summarization: Optional[DataAIConfigSummarization] = None
    """Summary Config"""

    transcription: Optional[DataAIConfigTranscription] = None
    """Transcription Configurations"""


class DataRecordingConfigAudioConfig(BaseModel):
    """Object containing configuration regarding the audio that is being recorded."""

    channel: Optional[Literal["mono", "stereo"]] = None
    """Audio signal pathway within an audio file that carries a specific sound source."""

    codec: Optional[Literal["MP3", "AAC"]] = None
    """Codec using which the recording will be encoded.

    If VP8/VP9 is selected for videoConfig, changing audioConfig is not allowed. In
    this case, the codec in the audioConfig is automatically set to vorbis.
    """

    export_file: Optional[bool] = None
    """Controls whether to export audio file seperately"""


class DataRecordingConfigLiveStreamingConfig(BaseModel):
    rtmp_url: Optional[str] = None
    """RTMP URL to stream to"""


class DataRecordingConfigRealtimekitBucketConfig(BaseModel):
    enabled: bool
    """Controls whether recordings are uploaded to RealtimeKit's bucket.

    If set to false, `download_url`, `audio_download_url`, `download_url_expiry`
    won't be generated for a recording.
    """


class DataRecordingConfigStorageConfig(BaseModel):
    type: Literal["aws", "azure", "digitalocean", "gcs", "sftp"]
    """Type of storage media."""

    auth_method: Optional[Literal["KEY", "PASSWORD"]] = None
    """Authentication method used for "sftp" type storage medium"""

    bucket: Optional[str] = None
    """Name of the storage medium's bucket."""

    host: Optional[str] = None
    """SSH destination server host for SFTP type storage medium"""

    password: Optional[str] = None
    """
    SSH destination server password for SFTP type storage medium when auth_method is
    "PASSWORD". If auth_method is "KEY", this specifies the password for the ssh
    private key.
    """

    path: Optional[str] = None
    """Path relative to the bucket root at which the recording will be placed."""

    port: Optional[float] = None
    """SSH destination server port for SFTP type storage medium"""

    private_key: Optional[str] = None
    """
    Private key used to login to destination SSH server for SFTP type storage
    medium, when auth_method used is "KEY"
    """

    region: Optional[str] = None
    """Region of the storage medium."""

    secret: Optional[str] = None
    """Secret key of the storage medium.

    Similar to `access_key`, it is only writeable by clients, not readable.
    """

    username: Optional[str] = None
    """SSH destination server username for SFTP type storage medium"""


class DataRecordingConfigVideoConfigWatermarkSize(BaseModel):
    """Size of the watermark"""

    height: Optional[int] = None
    """Height of the watermark in px"""

    width: Optional[int] = None
    """Width of the watermark in px"""


class DataRecordingConfigVideoConfigWatermark(BaseModel):
    """Watermark to be added to the recording"""

    position: Optional[Literal["left top", "right top", "left bottom", "right bottom"]] = None
    """Position of the watermark"""

    size: Optional[DataRecordingConfigVideoConfigWatermarkSize] = None
    """Size of the watermark"""

    url: Optional[str] = None
    """URL of the watermark image"""


class DataRecordingConfigVideoConfig(BaseModel):
    codec: Optional[Literal["H264", "VP8"]] = None
    """Codec using which the recording will be encoded."""

    export_file: Optional[bool] = None
    """Controls whether to export video file seperately"""

    height: Optional[int] = None
    """Height of the recording video in pixels"""

    watermark: Optional[DataRecordingConfigVideoConfigWatermark] = None
    """Watermark to be added to the recording"""

    width: Optional[int] = None
    """Width of the recording video in pixels"""


class DataRecordingConfig(BaseModel):
    """Recording Configurations to be used for this meeting.

    This level of configs takes higher preference over App level configs on the RealtimeKit developer portal.
    """

    audio_config: Optional[DataRecordingConfigAudioConfig] = None
    """Object containing configuration regarding the audio that is being recorded."""

    file_name_prefix: Optional[str] = None
    """Adds a prefix to the beginning of the file name of the recording."""

    live_streaming_config: Optional[DataRecordingConfigLiveStreamingConfig] = None

    max_seconds: Optional[float] = None
    """
    Specifies the maximum duration for recording in seconds, ranging from a minimum
    of 60 seconds to a maximum of 24 hours.
    """

    realtimekit_bucket_config: Optional[DataRecordingConfigRealtimekitBucketConfig] = None

    storage_config: Optional[DataRecordingConfigStorageConfig] = None

    video_config: Optional[DataRecordingConfigVideoConfig] = None


class Data(BaseModel):
    """Data returned by the operation"""

    id: str
    """ID of the meeting."""

    created_at: datetime
    """Timestamp the object was created at. The time is returned in ISO format."""

    updated_at: datetime
    """Timestamp the object was updated at. The time is returned in ISO format."""

    ai_config: Optional[DataAIConfig] = None
    """
    The AI Config allows you to customize the behavior of meeting transcriptions and
    summaries
    """

    live_stream_on_start: Optional[bool] = None
    """Specifies if the meeting should start getting livestreamed on start."""

    persist_chat: Optional[bool] = None
    """Specifies if Chat within a meeting should persist for a week."""

    record_on_start: Optional[bool] = None
    """
    Specifies if the meeting should start getting recorded as soon as someone joins
    the meeting.
    """

    recording_config: Optional[DataRecordingConfig] = None
    """Recording Configurations to be used for this meeting.

    This level of configs takes higher preference over App level configs on the
    RealtimeKit developer portal.
    """

    session_keep_alive_time_in_secs: Optional[float] = None
    """
    Time in seconds, for which a session remains active, after the last participant
    has left the meeting.
    """

    status: Optional[Literal["ACTIVE", "INACTIVE"]] = None
    """Whether the meeting is `ACTIVE` or `INACTIVE`.

    Users will not be able to join an `INACTIVE` meeting.
    """

    summarize_on_end: Optional[bool] = None
    """Automatically generate summary of meetings using transcripts.

    Requires Transcriptions to be enabled, and can be retrieved via Webhooks or
    summary API.
    """

    title: Optional[str] = None
    """Title of the meeting."""


class MeetingUpdateMeetingByIDResponse(BaseModel):
    success: bool
    """Success status of the operation"""

    data: Optional[Data] = None
    """Data returned by the operation"""
