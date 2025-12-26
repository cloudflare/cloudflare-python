# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RecordingGetActiveRecordingsResponse", "Data"]


class Data(BaseModel):
    """Data returned by the operation"""

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

    recording_duration: Optional[int] = None
    """Total recording time in seconds."""


class RecordingGetActiveRecordingsResponse(BaseModel):
    data: Data
    """Data returned by the operation"""

    success: bool
    """Success status of the operation"""
