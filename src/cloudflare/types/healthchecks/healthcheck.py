# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .check_region import CheckRegion
from .tcp_configuration import TCPConfiguration
from .http_configuration import HTTPConfiguration

__all__ = ["Healthcheck"]


class Healthcheck(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    address: Optional[str] = None
    """The hostname or IP address of the origin server to run health checks on."""

    check_regions: Optional[List[CheckRegion]] = None
    """A list of regions from which to run health checks.

    Null means Cloudflare will pick a default region.
    """

    consecutive_fails: Optional[int] = None
    """
    The number of consecutive fails required from a health check before changing the
    health to unhealthy.
    """

    consecutive_successes: Optional[int] = None
    """
    The number of consecutive successes required from a health check before changing
    the health to healthy.
    """

    created_on: Optional[datetime] = None

    description: Optional[str] = None
    """A human-readable description of the health check."""

    failure_reason: Optional[str] = None
    """The current failure reason if status is unhealthy."""

    http_config: Optional[HTTPConfiguration] = None
    """Parameters specific to an HTTP or HTTPS health check."""

    interval: Optional[int] = None
    """The interval between each health check.

    Shorter intervals may give quicker notifications if the origin status changes,
    but will increase load on the origin as we check from multiple locations.
    """

    modified_on: Optional[datetime] = None

    name: Optional[str] = None
    """A short name to identify the health check.

    Only alphanumeric characters, hyphens and underscores are allowed.
    """

    retries: Optional[int] = None
    """
    The number of retries to attempt in case of a timeout before marking the origin
    as unhealthy. Retries are attempted immediately.
    """

    status: Optional[Literal["unknown", "healthy", "unhealthy", "suspended"]] = None
    """The current status of the origin server according to the health check."""

    suspended: Optional[bool] = None
    """If suspended, no health checks are sent to the origin."""

    tcp_config: Optional[TCPConfiguration] = None
    """Parameters specific to TCP health check."""

    timeout: Optional[int] = None
    """The timeout (in seconds) before marking the health check as failed."""

    type: Optional[str] = None
    """The protocol to use for the health check.

    Currently supported protocols are 'HTTP', 'HTTPS' and 'TCP'.
    """
