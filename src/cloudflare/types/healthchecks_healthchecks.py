# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["HealthchecksHealthchecks", "HTTPConfig", "TcpConfig"]


class HTTPConfig(BaseModel):
    allow_insecure: Optional[bool] = None
    """Do not validate the certificate when the health check uses HTTPS."""

    expected_body: Optional[str] = None
    """A case-insensitive sub-string to look for in the response body.

    If this string is not found, the origin will be marked as unhealthy.
    """

    expected_codes: Optional[List[str]] = None
    """The expected HTTP response codes (e.g.

    "200") or code ranges (e.g. "2xx" for all codes starting with 2) of the health
    check.
    """

    follow_redirects: Optional[bool] = None
    """Follow redirects if the origin returns a 3xx status code."""

    header: Optional[object] = None
    """The HTTP request headers to send in the health check.

    It is recommended you set a Host header by default. The User-Agent header cannot
    be overridden.
    """

    method: Optional[Literal["GET", "HEAD"]] = None
    """The HTTP method to use for the health check."""

    path: Optional[str] = None
    """The endpoint path to health check against."""

    port: Optional[int] = None
    """Port number to connect to for the health check.

    Defaults to 80 if type is HTTP or 443 if type is HTTPS.
    """


class TcpConfig(BaseModel):
    method: Optional[Literal["connection_established"]] = None
    """The TCP connection method to use for the health check."""

    port: Optional[int] = None
    """Port number to connect to for the health check. Defaults to 80."""


class HealthchecksHealthchecks(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    address: Optional[str] = None
    """The hostname or IP address of the origin server to run health checks on."""

    check_regions: Optional[
        List[
            Literal[
                "WNAM",
                "ENAM",
                "WEU",
                "EEU",
                "NSAM",
                "SSAM",
                "OC",
                "ME",
                "NAF",
                "SAF",
                "IN",
                "SEAS",
                "NEAS",
                "ALL_REGIONS",
            ]
        ]
    ] = None
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

    http_config: Optional[HTTPConfig] = None
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

    tcp_config: Optional[TcpConfig] = None
    """Parameters specific to TCP health check."""

    timeout: Optional[int] = None
    """The timeout (in seconds) before marking the health check as failed."""

    type: Optional[str] = None
    """The protocol to use for the health check.

    Currently supported protocols are 'HTTP', 'HTTPS' and 'TCP'.
    """
