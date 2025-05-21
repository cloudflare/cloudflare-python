# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = [
    "SplitTunnelIncludeParam",
    "TeamsDevicesIncludeSplitTunnelWithAddress",
    "TeamsDevicesIncludeSplitTunnelWithHost",
]


class TeamsDevicesIncludeSplitTunnelWithAddress(TypedDict, total=False):
    address: Required[str]
    """The address in CIDR format to include in the tunnel.

    If `address` is present, `host` must not be present.
    """

    description: str
    """A description of the Split Tunnel item, displayed in the client UI."""


class TeamsDevicesIncludeSplitTunnelWithHost(TypedDict, total=False):
    host: Required[str]
    """The domain name to include in the tunnel.

    If `host` is present, `address` must not be present.
    """

    description: str
    """A description of the Split Tunnel item, displayed in the client UI."""


SplitTunnelIncludeParam: TypeAlias = Union[
    TeamsDevicesIncludeSplitTunnelWithAddress, TeamsDevicesIncludeSplitTunnelWithHost
]
