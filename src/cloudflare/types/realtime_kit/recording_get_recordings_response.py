# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RecordingGetRecordingsResponse", "Data", "DataMeeting", "DataStorageConfig", "Paging"]


class DataMeeting(BaseModel):
    id: str
    """ID of the meeting."""

    created_at: datetime
    """Timestamp the object was created at. The time is returned in ISO format."""

    updated_at: datetime
    """Timestamp the object was updated at. The time is returned in ISO format."""

    live_stream_on_start: Optional[bool] = None
    """Specifies if the meeting should start getting livestreamed on start."""

    persist_chat: Optional[bool] = None
    """Specifies if Chat within a meeting should persist for a week."""

    record_on_start: Optional[bool] = None
    """
    Specifies if the meeting should start getting recorded as soon as someone joins
    the meeting.
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


class DataStorageConfig(BaseModel):
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


class Data(BaseModel):
    id: str
    """ID of the recording"""

    audio_download_url: Optional[str] = None
    """
    If the audio_config is passed, the URL for downloading the audio recording is
    returned.
    """

    download_url: Optional[str] = None
    """URL where the recording can be downloaded."""

    download_url_expiry: Optional[datetime] = None
    """Timestamp when the download URL expires."""

    file_size: Optional[float] = None
    """File size of the recording, in bytes."""

    invoked_time: datetime
    """Timestamp when this recording was invoked."""

    output_file_name: str
    """File name of the recording."""

    session_id: Optional[str] = None
    """ID of the meeting session this recording is for."""

    started_time: Optional[datetime] = None
    """Timestamp when this recording actually started after being invoked.

    Usually a few seconds after `invoked_time`.
    """

    status: Literal["INVOKED", "RECORDING", "UPLOADING", "UPLOADED", "ERRORED", "PAUSED"]
    """Current status of the recording."""

    stopped_time: Optional[datetime] = None
    """Timestamp when this recording was stopped.

    Optional; is present only when the recording has actually been stopped.
    """

    meeting: Optional[DataMeeting] = None

    recording_duration: Optional[int] = None
    """Total recording time in seconds."""

    storage_config: Optional[DataStorageConfig] = None


class Paging(BaseModel):
    end_offset: float

    start_offset: float

    total_count: float


class RecordingGetRecordingsResponse(BaseModel):
    data: List[Data]

    paging: Paging

    success: bool
