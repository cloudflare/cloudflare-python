# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .health_check_rate import HealthCheckRate
from .health_check_type import HealthCheckType

__all__ = ["CfInterconnectListResponse", "Interconnect", "InterconnectGRE", "InterconnectHealthCheck"]


class InterconnectGRE(BaseModel):
    cloudflare_endpoint: Optional[str] = None
    """
    The IP address assigned to the Cloudflare side of the GRE tunnel created as part
    of the Interconnect.
    """


class InterconnectHealthCheck(BaseModel):
    enabled: Optional[bool] = None
    """Determines whether to run healthchecks for a tunnel."""

    rate: Optional[HealthCheckRate] = None
    """How frequent the health check is run. The default value is `mid`."""

    target: Optional[str] = None
    """The destination address in a request type health check.

    After the healthcheck is decapsulated at the customer end of the tunnel, the
    ICMP echo will be forwarded to this address. This field defaults to
    `customer_gre_endpoint address`.
    """

    type: Optional[HealthCheckType] = None
    """The type of healthcheck to run, reply or request. The default value is `reply`."""


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

    health_check: Optional[InterconnectHealthCheck] = None

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


class CfInterconnectListResponse(BaseModel):
    interconnects: Optional[List[Interconnect]] = None
