# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "RecordingStartRecordingsResponse",
    "Data",
    "DataStartReason",
    "DataStartReasonCaller",
    "DataStopReason",
    "DataStopReasonCaller",
    "DataStorageConfig",
    "DataStorageConfigUnionMember0",
    "DataStorageConfigUnionMember1",
    "DataStorageConfigUnionMember2",
    "DataStorageConfigUnionMember3",
]


class DataStartReasonCaller(BaseModel):
    name: Optional[str] = None
    """Name of the user who started the recording."""

    type: Optional[Literal["ORGANIZATION", "USER"]] = None
    """The type can be an App or a user.

    If the type is `user`, then only the `user_Id` and `name` are returned.
    """

    user_id: Optional[str] = FieldInfo(alias="user_Id", default=None)
    """The user ID of the person who started the recording."""


class DataStartReason(BaseModel):
    caller: Optional[DataStartReasonCaller] = None

    reason: Optional[Literal["API_CALL", "RECORD_ON_START"]] = None
    """
    Specifies if the recording was started using the "Start a Recording"API or using
    the parameter RECORD_ON_START in the "Create a meeting" API.

    If the recording is initiated using the "RECORD_ON_START" parameter, the user
    details will not be populated.
    """


class DataStopReasonCaller(BaseModel):
    name: Optional[str] = None
    """Name of the user who stopped the recording."""

    type: Optional[Literal["ORGANIZATION", "USER"]] = None
    """The type can be an App or a user.

    If the type is `user`, then only the `user_Id` and `name` are returned.
    """

    user_id: Optional[str] = FieldInfo(alias="user_Id", default=None)
    """The user ID of the person who stopped the recording."""


class DataStopReason(BaseModel):
    caller: Optional[DataStopReasonCaller] = None

    reason: Optional[Literal["API_CALL", "INTERNAL_ERROR", "ALL_PEERS_LEFT"]] = None
    """Specifies the reason why the recording stopped."""


class DataStorageConfigUnionMember0(BaseModel):
    auth_method: Optional[Literal["KEY", "PASSWORD"]] = None
    """Authentication method used for "sftp" type storage medium"""

    bucket: Optional[str] = None
    """Name of the storage medium's bucket."""

    host: Optional[str] = None
    """SSH destination server host for SFTP type storage medium"""

    path: Optional[str] = None
    """Path relative to the bucket root at which the recording will be placed."""

    port: Optional[float] = None
    """SSH destination server port for SFTP type storage medium"""

    region: Optional[str] = None
    """Region of the storage medium."""

    type: Optional[Literal["gcs"]] = None

    username: Optional[str] = None
    """SSH destination server username for SFTP type storage medium"""


class DataStorageConfigUnionMember1(BaseModel):
    access_key: object

    region: object

    auth_method: Optional[Literal["KEY", "PASSWORD"]] = None
    """Authentication method used for "sftp" type storage medium"""

    bucket: Optional[str] = None
    """Name of the storage medium's bucket."""

    host: Optional[str] = None
    """SSH destination server host for SFTP type storage medium"""

    path: Optional[str] = None
    """Path relative to the bucket root at which the recording will be placed."""

    port: Optional[float] = None
    """SSH destination server port for SFTP type storage medium"""

    type: Optional[Literal["aws", "azure", "digitalocean"]] = None

    username: Optional[str] = None
    """SSH destination server username for SFTP type storage medium"""


class DataStorageConfigUnionMember2(BaseModel):
    auth_method: Optional[Literal["KEY"]] = None

    bucket: Optional[str] = None
    """Name of the storage medium's bucket."""

    host: Optional[str] = None
    """SSH destination server host for SFTP type storage medium"""

    path: Optional[str] = None
    """Path relative to the bucket root at which the recording will be placed."""

    port: Optional[float] = None
    """SSH destination server port for SFTP type storage medium"""

    region: Optional[str] = None
    """Region of the storage medium."""

    type: Optional[Literal["aws", "azure", "digitalocean", "gcs", "sftp"]] = None
    """Type of storage media."""

    username: Optional[str] = None
    """SSH destination server username for SFTP type storage medium"""


class DataStorageConfigUnionMember3(BaseModel):
    auth_method: Optional[Literal["PASSWORD"]] = None

    bucket: Optional[str] = None
    """Name of the storage medium's bucket."""

    host: Optional[str] = None
    """SSH destination server host for SFTP type storage medium"""

    path: Optional[str] = None
    """Path relative to the bucket root at which the recording will be placed."""

    port: Optional[float] = None
    """SSH destination server port for SFTP type storage medium"""

    region: Optional[str] = None
    """Region of the storage medium."""

    type: Optional[Literal["aws", "azure", "digitalocean", "gcs", "sftp"]] = None
    """Type of storage media."""

    username: Optional[str] = None
    """SSH destination server username for SFTP type storage medium"""


DataStorageConfig: TypeAlias = Union[
    DataStorageConfigUnionMember0,
    DataStorageConfigUnionMember1,
    DataStorageConfigUnionMember2,
    DataStorageConfigUnionMember3,
    None,
]


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

    start_reason: Optional[DataStartReason] = None

    stop_reason: Optional[DataStopReason] = None

    storage_config: Optional[DataStorageConfig] = None


class RecordingStartRecordingsResponse(BaseModel):
    success: bool
    """Success status of the operation"""

    data: Optional[Data] = None
    """Data returned by the operation"""
