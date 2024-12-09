# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CommandCreateParams", "Command", "CommandCommandArgs"]


class CommandCreateParams(TypedDict, total=False):
    account_id: Required[str]

    commands: Required[Iterable[Command]]
    """List of device-level commands to execute"""


class CommandCommandArgs(TypedDict, total=False):
    interfaces: List[Literal["default", "tunnel"]]
    """List of interfaces to capture packets on"""

    max_file_size_mb: Annotated[float, PropertyInfo(alias="max-file-size-mb")]
    """Maximum file size (in MB) for the capture file.

    Specifies the maximum file size of the warp-diag zip artifact that can be
    uploaded. If the zip artifact exceeds the specified max file size, it will NOT
    be uploaded
    """

    packet_size_bytes: Annotated[float, PropertyInfo(alias="packet-size-bytes")]
    """Maximum number of bytes to save for each packet"""

    test_all_routes: Annotated[bool, PropertyInfo(alias="test-all-routes")]
    """Test an IP address from all included or excluded ranges.

    Tests an IP address from all included or excluded ranges. Essentially the same
    as running 'route get <ip>'' and collecting the results. This option may
    increase the time taken to collect the warp-diag
    """

    time_limit_min: Annotated[float, PropertyInfo(alias="time-limit-min")]
    """Limit on capture duration (in minutes)"""


class Command(TypedDict, total=False):
    command_type: Required[Literal["pcap", "warp-diag"]]
    """Type of command to execute on the device"""

    device_id: Required[str]
    """Unique identifier for the device"""

    user_email: Required[str]
    """Email tied to the device"""

    command_args: CommandCommandArgs
