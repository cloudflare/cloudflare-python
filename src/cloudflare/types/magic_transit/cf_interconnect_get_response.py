# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .health_check import HealthCheck

__all__ = ["CfInterconnectGetResponse", "Interconnect", "InterconnectGRE"]


class InterconnectGRE(BaseModel):
    cloudflare_endpoint: Optional[str] = None
    """
    The IP address assigned to the Cloudflare side of the GRE tunnel created as part
    of the Interconnect.
    """


class Interconnect(BaseModel):
    id: Optional[str] = None
    """Tunnel identifier tag."""

    colo_name: Optional[str] = None
    """The name of the interconnect. The name cannot share a name with other tunnels."""

    created_on: Optional[datetime] = None
    """The date and time the tunnel was created."""

    description: Optional[str] = None
    """An optional description of the interconnect."""

    gre: Optional[InterconnectGRE] = None
    """The configuration specific to GRE interconnects."""

    health_check: Optional[HealthCheck] = None

    interface_address: Optional[str] = None
    """
    A 31-bit prefix (/31 in CIDR notation) supporting two hosts, one for each side
    of the tunnel. Select the subnet from the following private IP space:
    10.0.0.0–10.255.255.255, 172.16.0.0–172.31.255.255, 192.168.0.0–192.168.255.255.
    """

    modified_on: Optional[datetime] = None
    """The date and time the tunnel was last modified."""

    mtu: Optional[int] = None
    """The Maximum Transmission Unit (MTU) in bytes for the interconnect.

    The minimum value is 576.
    """

    name: Optional[str] = None
    """The name of the interconnect. The name cannot share a name with other tunnels."""


class CfInterconnectGetResponse(BaseModel):
    interconnect: Optional[Interconnect] = None
