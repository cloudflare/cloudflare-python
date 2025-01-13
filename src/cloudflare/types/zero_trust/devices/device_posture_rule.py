# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel
from .device_input import DeviceInput
from .device_match import DeviceMatch

__all__ = ["DevicePostureRule"]


class DevicePostureRule(BaseModel):
    id: Optional[str] = None
    """API UUID."""

    description: Optional[str] = None
    """The description of the device posture rule."""

    expiration: Optional[str] = None
    """Sets the expiration time for a posture check result.

    If empty, the result remains valid until it is overwritten by new data from the
    WARP client.
    """

    input: Optional[DeviceInput] = None
    """The value to be checked against."""

    match: Optional[List[DeviceMatch]] = None
    """The conditions that the client must match to run the rule."""

    name: Optional[str] = None
    """The name of the device posture rule."""

    schedule: Optional[str] = None
    """Polling frequency for the WARP client posture check.

    Default: `5m` (poll every five minutes). Minimum: `1m`.
    """

    type: Optional[
        Literal[
            "file",
            "application",
            "tanium",
            "gateway",
            "warp",
            "disk_encryption",
            "sentinelone",
            "carbonblack",
            "firewall",
            "os_version",
            "domain_joined",
            "client_certificate",
            "client_certificate_v2",
            "unique_client_id",
            "kolide",
            "tanium_s2s",
            "crowdstrike_s2s",
            "intune",
            "workspace_one",
            "sentinelone_s2s",
            "custom_s2s",
        ]
    ] = None
    """The type of device posture rule."""
