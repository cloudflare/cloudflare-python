# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .health_check_rate import HealthCheckRate
from .health_check_type import HealthCheckType

__all__ = [
    "CfInterconnectUpdateParams",
    "GRE",
    "HealthCheck",
    "HealthCheckTarget",
    "HealthCheckTargetMagicHealthCheckTarget",
]


class CfInterconnectUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    description: str
    """An optional description of the interconnect."""

    gre: GRE
    """The configuration specific to GRE interconnects."""

    health_check: HealthCheck

    interface_address: str
    """
    A 31-bit prefix (/31 in CIDR notation) supporting two hosts, one for each side
    of the tunnel. Select the subnet from the following private IP space:
    10.0.0.0–10.255.255.255, 172.16.0.0–172.31.255.255, 192.168.0.0–192.168.255.255.
    """

    mtu: int
    """The Maximum Transmission Unit (MTU) in bytes for the interconnect.

    The minimum value is 576.
    """

    x_magic_new_hc_target: Annotated[bool, PropertyInfo(alias="x-magic-new-hc-target")]


class GRE(TypedDict, total=False):
    cloudflare_endpoint: str
    """
    The IP address assigned to the Cloudflare side of the GRE tunnel created as part
    of the Interconnect.
    """


class HealthCheckTargetMagicHealthCheckTarget(TypedDict, total=False):
    saved: str
    """The saved health check target.

    Setting the value to the empty string indicates that the calculated default
    value will be used.
    """


HealthCheckTarget: TypeAlias = Union[HealthCheckTargetMagicHealthCheckTarget, str]


class HealthCheck(TypedDict, total=False):
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
