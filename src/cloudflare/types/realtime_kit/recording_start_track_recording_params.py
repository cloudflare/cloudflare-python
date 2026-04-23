# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RecordingStartTrackRecordingParams", "Layers", "LayersOutput", "LayersOutputStorageConfig"]


class RecordingStartTrackRecordingParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    layers: Required[Dict[str, Layers]]

    meeting_id: Required[str]
    """ID of the meeting to record."""

    max_seconds: float
    """Maximum seconds this recording should be active for (beta)"""


class LayersOutputStorageConfig(TypedDict, total=False):
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


class LayersOutput(TypedDict, total=False):
    storage_config: Optional[LayersOutputStorageConfig]

    type: Literal["REALTIMEKIT_BUCKET", "STORAGE_CONFIG"]
    """The type of output destination this layer is being exported to."""


class Layers(TypedDict, total=False):
    file_name_prefix: str
    """A file name prefix to apply for files generated from this layer"""

    outputs: Iterable[LayersOutput]
