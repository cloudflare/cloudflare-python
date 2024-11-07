# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["Configuration", "WARPDevice"]


class WARPDevice(BaseModel):
    id: str
    """Unique identifier for the warp device."""

    name: str
    """Name of the warp device."""

    router_ip: str
    """IPv4 CIDR of the router sourcing flow data associated with this warp device.

    Only /32 addresses are currently supported.
    """


class Configuration(BaseModel):
    default_sampling: float
    """Fallback sampling rate of flow messages being sent in packets per second.

    This should match the packet sampling rate configured on the router.
    """

    name: str
    """The account name."""

    router_ips: List[str]

    warp_devices: List[WARPDevice]
