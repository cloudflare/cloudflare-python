# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["Configuration", "WARPDevice"]


class WARPDevice(BaseModel):
    id: str
    """Unique identifier for the warp device."""

    name: str
    """Name of the warp device."""


class Configuration(BaseModel):
    default_sampling: float
    """Fallback sampling rate of flow messages being sent in packets per second.

    This should match the packet sampling rate configured on the router.
    """

    name: str
    """The account name."""

    router_ips: List[str]

    warp_devices: List[WARPDevice]
