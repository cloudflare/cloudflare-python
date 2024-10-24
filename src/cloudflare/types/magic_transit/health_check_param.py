# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias, TypedDict

from .health_check_rate import HealthCheckRate
from .health_check_type import HealthCheckType

__all__ = ["HealthCheckParam", "Target", "TargetMagicHealthCheckTarget"]


class TargetMagicHealthCheckTarget(TypedDict, total=False):
    saved: str
    """The saved health check target.

    Setting the value to the empty string indicates that the calculated default
    value will be used.
    """


Target: TypeAlias = Union[TargetMagicHealthCheckTarget, str]


class HealthCheckParam(TypedDict, total=False):
    enabled: bool
    """Determines whether to run healthchecks for a tunnel."""

    rate: HealthCheckRate
    """How frequent the health check is run. The default value is `mid`."""

    target: Target
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
