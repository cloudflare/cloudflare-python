# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .health_check_rate import HealthCheckRate
from .health_check_type import HealthCheckType

__all__ = ["GRETunnelUpdateParams", "HealthCheck", "HealthCheckTarget", "HealthCheckTargetMagicHealthCheckTarget"]


class GRETunnelUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    cloudflare_gre_endpoint: Required[str]
    """The IP address assigned to the Cloudflare side of the GRE tunnel."""

    customer_gre_endpoint: Required[str]
    """The IP address assigned to the customer side of the GRE tunnel."""

    interface_address: Required[str]
    """
    A 31-bit prefix (/31 in CIDR notation) supporting two hosts, one for each side
    of the tunnel. Select the subnet from the following private IP space:
    10.0.0.0–10.255.255.255, 172.16.0.0–172.31.255.255, 192.168.0.0–192.168.255.255.
    """

    name: Required[str]
    """The name of the tunnel.

    The name cannot contain spaces or special characters, must be 15 characters or
    less, and cannot share a name with another GRE tunnel.
    """

    description: str
    """An optional description of the GRE tunnel."""

    health_check: HealthCheck

    mtu: int
    """Maximum Transmission Unit (MTU) in bytes for the GRE tunnel.

    The minimum value is 576.
    """

    ttl: int
    """Time To Live (TTL) in number of hops of the GRE tunnel."""

    x_magic_new_hc_target: Annotated[bool, PropertyInfo(alias="x-magic-new-hc-target")]


class HealthCheckTargetMagicHealthCheckTarget(TypedDict, total=False):
    saved: str
    """The saved health check target.

    Setting the value to the empty string indicates that the calculated default
    value will be used.
    """


HealthCheckTarget: TypeAlias = Union[HealthCheckTargetMagicHealthCheckTarget, str]


class HealthCheck(TypedDict, total=False):
    direction: Literal["unidirectional", "bidirectional"]
    """The direction of the flow of the healthcheck.

    Either unidirectional, where the probe comes to you via the tunnel and the
    result comes back to Cloudflare via the open Internet, or bidirectional where
    both the probe and result come and go via the tunnel.
    """

    enabled: bool
    """Determines whether to run healthchecks for a tunnel."""

    rate: HealthCheckRate
    """How frequent the health check is run. The default value is `mid`."""

    target: HealthCheckTarget
    """The destination address in a request type health check.

    After the healthcheck is decapsulated at the customer end of the tunnel, the
    ICMP echo will be forwarded to this address. This field defaults to
    `customer_gre_endpoint address`. This field is ignored for bidirectional
    healthchecks as the interface_address (not assigned to the Cloudflare side of
    the tunnel) is used as the target. Must be in object form if the
    x-magic-new-hc-target header is set to true and string form if
    x-magic-new-hc-target is absent or set to false.
    """

    type: HealthCheckType
    """The type of healthcheck to run, reply or request. The default value is `reply`."""
