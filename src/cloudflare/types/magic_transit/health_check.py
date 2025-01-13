# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel
from .health_check_rate import HealthCheckRate
from .health_check_type import HealthCheckType

__all__ = ["HealthCheck", "Target", "TargetMagicHealthCheckTarget"]


class TargetMagicHealthCheckTarget(BaseModel):
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


Target: TypeAlias = Union[TargetMagicHealthCheckTarget, str]


class HealthCheck(BaseModel):
    enabled: Optional[bool] = None
    """Determines whether to run healthchecks for a tunnel."""

    rate: Optional[HealthCheckRate] = None
    """How frequent the health check is run. The default value is `mid`."""

    target: Optional[Target] = None
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
