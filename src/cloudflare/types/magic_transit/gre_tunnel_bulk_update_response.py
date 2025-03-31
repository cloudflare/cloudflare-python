# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .health_check_rate import HealthCheckRate
from .health_check_type import HealthCheckType

__all__ = [
    "GRETunnelBulkUpdateResponse",
    "ModifiedGRETunnel",
    "ModifiedGRETunnelHealthCheck",
    "ModifiedGRETunnelHealthCheckTarget",
    "ModifiedGRETunnelHealthCheckTargetMagicHealthCheckTarget",
]


class ModifiedGRETunnelHealthCheckTargetMagicHealthCheckTarget(BaseModel):
    effective: Optional[str] = None
    """The effective health check target.

    If 'saved' is empty, then this field will be populated with the calculated
    default value on GET requests. Ignored in POST, PUT, and PATCH requests.
    """

    saved: Optional[str] = None
    """The saved health check target.

    Setting the value to the empty string indicates that the calculated default
    value will be used.
    """


ModifiedGRETunnelHealthCheckTarget: TypeAlias = Union[ModifiedGRETunnelHealthCheckTargetMagicHealthCheckTarget, str]


class ModifiedGRETunnelHealthCheck(BaseModel):
    direction: Optional[Literal["unidirectional", "bidirectional"]] = None
    """The direction of the flow of the healthcheck.

    Either unidirectional, where the probe comes to you via the tunnel and the
    result comes back to Cloudflare via the open Internet, or bidirectional where
    both the probe and result come and go via the tunnel.
    """

    enabled: Optional[bool] = None
    """Determines whether to run healthchecks for a tunnel."""

    rate: Optional[HealthCheckRate] = None
    """How frequent the health check is run. The default value is `mid`."""

    target: Optional[ModifiedGRETunnelHealthCheckTarget] = None
    """The destination address in a request type health check.

    After the healthcheck is decapsulated at the customer end of the tunnel, the
    ICMP echo will be forwarded to this address. This field defaults to
    `customer_gre_endpoint address`. This field is ignored for bidirectional
    healthchecks as the interface_address (not assigned to the Cloudflare side of
    the tunnel) is used as the target. Must be in object form if the
    x-magic-new-hc-target header is set to true and string form if
    x-magic-new-hc-target is absent or set to false.
    """

    type: Optional[HealthCheckType] = None
    """The type of healthcheck to run, reply or request. The default value is `reply`."""


class ModifiedGRETunnel(BaseModel):
    cloudflare_gre_endpoint: str
    """The IP address assigned to the Cloudflare side of the GRE tunnel."""

    customer_gre_endpoint: str
    """The IP address assigned to the customer side of the GRE tunnel."""

    interface_address: str
    """
    A 31-bit prefix (/31 in CIDR notation) supporting two hosts, one for each side
    of the tunnel. Select the subnet from the following private IP space:
    10.0.0.0–10.255.255.255, 172.16.0.0–172.31.255.255, 192.168.0.0–192.168.255.255.
    """

    name: str
    """The name of the tunnel.

    The name cannot contain spaces or special characters, must be 15 characters or
    less, and cannot share a name with another GRE tunnel.
    """

    id: Optional[str] = None
    """Tunnel identifier tag."""

    created_on: Optional[datetime] = None
    """The date and time the tunnel was created."""

    description: Optional[str] = None
    """An optional description of the GRE tunnel."""

    health_check: Optional[ModifiedGRETunnelHealthCheck] = None

    modified_on: Optional[datetime] = None
    """The date and time the tunnel was last modified."""

    mtu: Optional[int] = None
    """Maximum Transmission Unit (MTU) in bytes for the GRE tunnel.

    The minimum value is 576.
    """

    ttl: Optional[int] = None
    """Time To Live (TTL) in number of hops of the GRE tunnel."""


class GRETunnelBulkUpdateResponse(BaseModel):
    modified: Optional[bool] = None

    modified_gre_tunnels: Optional[List[ModifiedGRETunnel]] = None
