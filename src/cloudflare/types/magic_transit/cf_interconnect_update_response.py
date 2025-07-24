# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .health_check import HealthCheck

__all__ = ["CfInterconnectUpdateResponse", "ModifiedInterconnect", "ModifiedInterconnectGRE"]


class ModifiedInterconnectGRE(BaseModel):
    cloudflare_endpoint: Optional[str] = None
    """
    The IP address assigned to the Cloudflare side of the GRE tunnel created as part
    of the Interconnect.
    """


class ModifiedInterconnect(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    colo_name: Optional[str] = None
    """The name of the interconnect. The name cannot share a name with other tunnels."""

    created_on: Optional[datetime] = None
    """The date and time the tunnel was created."""

    description: Optional[str] = None
    """An optional description of the interconnect."""

    gre: Optional[ModifiedInterconnectGRE] = None
    """The configuration specific to GRE interconnects."""

    health_check: Optional[HealthCheck] = None

    interface_address: Optional[str] = None
    """
    A 31-bit prefix (/31 in CIDR notation) supporting two hosts, one for each side
    of the tunnel. Select the subnet from the following private IP space:
    10.0.0.0–10.255.255.255, 172.16.0.0–172.31.255.255, 192.168.0.0–192.168.255.255.
    """

    interface_address6: Optional[str] = None
    """
    A 127 bit IPV6 prefix from within the virtual_subnet6 prefix space with the
    address being the first IP of the subnet and not same as the address of
    virtual_subnet6. Eg if virtual_subnet6 is 2606:54c1:7:0:a9fe:12d2::/127 ,
    interface_address6 could be 2606:54c1:7:0:a9fe:12d2:1:200/127
    """

    modified_on: Optional[datetime] = None
    """The date and time the tunnel was last modified."""

    mtu: Optional[int] = None
    """The Maximum Transmission Unit (MTU) in bytes for the interconnect.

    The minimum value is 576.
    """

    name: Optional[str] = None
    """The name of the interconnect. The name cannot share a name with other tunnels."""


class CfInterconnectUpdateResponse(BaseModel):
    modified: Optional[bool] = None

    modified_interconnect: Optional[ModifiedInterconnect] = None
