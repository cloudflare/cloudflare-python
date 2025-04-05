# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = [
    "SplitTunnelExcludeParam",
    "TeamsDevicesExcludeSplitTunnelWithAddress",
    "TeamsDevicesExcludeSplitTunnelWithHost",
]


class TeamsDevicesExcludeSplitTunnelWithAddress(TypedDict, total=False):
    address: Required[str]
    """The address in CIDR format to exclude from the tunnel.

    If `address` is present, `host` must not be present.
    """

    description: str
    """A description of the Split Tunnel item, displayed in the client UI."""


class TeamsDevicesExcludeSplitTunnelWithHost(TypedDict, total=False):
    host: Required[str]
    """The domain name to exclude from the tunnel.

    If `host` is present, `address` must not be present.
    """

    description: str
    """A description of the Split Tunnel item, displayed in the client UI."""


SplitTunnelExcludeParam: TypeAlias = Union[
    TeamsDevicesExcludeSplitTunnelWithAddress, TeamsDevicesExcludeSplitTunnelWithHost
]
