# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .check_region import CheckRegion
from .tcp_configuration_param import TCPConfigurationParam
from .http_configuration_param import HTTPConfigurationParam

__all__ = ["HealthcheckCreateParams"]


class HealthcheckCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    address: Required[str]
    """The hostname or IP address of the origin server to run health checks on."""

    name: Required[str]
    """A short name to identify the health check.

    Only alphanumeric characters, hyphens and underscores are allowed.
    """

    check_regions: Optional[List[CheckRegion]]
    """A list of regions from which to run health checks.

    Null means Cloudflare will pick a default region.
    """

    consecutive_fails: int
    """
    The number of consecutive fails required from a health check before changing the
    health to unhealthy.
    """

    consecutive_successes: int
    """
    The number of consecutive successes required from a health check before changing
    the health to healthy.
    """

    description: str
    """A human-readable description of the health check."""

    http_config: Optional[HTTPConfigurationParam]
    """Parameters specific to an HTTP or HTTPS health check."""

    interval: int
    """The interval between each health check.

    Shorter intervals may give quicker notifications if the origin status changes,
    but will increase load on the origin as we check from multiple locations.
    """

    retries: int
    """
    The number of retries to attempt in case of a timeout before marking the origin
    as unhealthy. Retries are attempted immediately.
    """

    suspended: bool
    """If suspended, no health checks are sent to the origin."""

    tcp_config: Optional[TCPConfigurationParam]
    """Parameters specific to TCP health check."""

    healthcheck_timeout: Annotated[int, PropertyInfo(alias="timeout")]
    """The timeout (in seconds) before marking the health check as failed."""

    type: str
    """The protocol to use for the health check.

    Currently supported protocols are 'HTTP', 'HTTPS' and 'TCP'.
    """
