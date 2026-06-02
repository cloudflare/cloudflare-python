# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._utils import PropertyInfo

__all__ = [
    "CommandCreateParams",
    "Command",
    "CommandArgs",
    "CommandArgsWARPDiagArgs",
    "CommandArgsPCAPArgs",
    "CommandArgsSpeedTestArgs",
]


class CommandCreateParams(TypedDict, total=False):
    account_id: Required[str]

    commands: Required[Iterable[Command]]
    """List of device-level commands to execute"""


class CommandArgsWARPDiagArgs(TypedDict, total=False):
    test_all_routes: Annotated[bool, PropertyInfo(alias="test-all-routes")]
    """Test an IP address from all included or excluded ranges.

    Essentially the same as running 'route get <ip>' and collecting the results.
    This option may increase the time taken to collect the warp-diag.
    """


class CommandArgsPCAPArgs(TypedDict, total=False):
    max_file_size_mb: Annotated[float, PropertyInfo(alias="max-file-size-mb")]
    """Maximum file size (in MB) for the capture file.

    If the capture artifact exceeds the specified max file size, it will NOT be
    uploaded.
    """

    packet_size_bytes: Annotated[float, PropertyInfo(alias="packet-size-bytes")]
    """Maximum number of bytes to save for each packet"""

    time_limit_min: Annotated[float, PropertyInfo(alias="time-limit-min")]
    """Limit on capture duration (in minutes)"""


class CommandArgsSpeedTestArgs(TypedDict, total=False):
    interfaces: List[Literal["default", "tunnel"]]
    """List of interfaces to run the speed test on"""


CommandArgs: TypeAlias = Union[CommandArgsWARPDiagArgs, CommandArgsPCAPArgs, CommandArgsSpeedTestArgs]


class Command(TypedDict, total=False):
    device_id: Required[str]
    """Unique identifier for the physical device"""

    type: Required[Literal["pcap", "speed-test", "warp-diag"]]
    """Type of command to execute on the device"""

    user_email: Required[str]
    """Email tied to the device"""

    args: CommandArgs
    """Command arguments. Allowed fields depend on `type`."""

    registration_id: str
    """Unique identifier for the device registration.

    Required for multi-user devices to target the correct user session.
    """
