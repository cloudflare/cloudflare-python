# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ConfigUpdateParams", "WARPDevice"]


class ConfigUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    default_sampling: Required[float]
    """Fallback sampling rate of flow messages being sent in packets per second.

    This should match the packet sampling rate configured on the router.
    """

    name: Required[str]
    """The account name."""

    router_ips: List[str]

    warp_devices: Iterable[WARPDevice]


class WARPDevice(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the warp device."""

    name: Required[str]
    """Name of the warp device."""

    router_ip: Required[str]
    """IPv4 CIDR of the router sourcing flow data associated with this warp device.

    Only /32 addresses are currently supported.
    """
