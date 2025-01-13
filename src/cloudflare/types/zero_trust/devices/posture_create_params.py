# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .device_input_param import DeviceInputParam
from .device_match_param import DeviceMatchParam

__all__ = ["PostureCreateParams"]


class PostureCreateParams(TypedDict, total=False):
    account_id: Required[str]

    name: Required[str]
    """The name of the device posture rule."""

    type: Required[
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
    ]
    """The type of device posture rule."""

    description: str
    """The description of the device posture rule."""

    expiration: str
    """Sets the expiration time for a posture check result.

    If empty, the result remains valid until it is overwritten by new data from the
    WARP client.
    """

    input: DeviceInputParam
    """The value to be checked against."""

    match: Iterable[DeviceMatchParam]
    """The conditions that the client must match to run the rule."""

    schedule: str
    """Polling frequency for the WARP client posture check.

    Default: `5m` (poll every five minutes). Minimum: `1m`.
    """
