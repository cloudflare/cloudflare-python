# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PreviewCreateParams", "HTTPConfig", "TcpConfig"]


class PreviewCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    address: Required[str]
    """The hostname or IP address of the origin server to run health checks on."""

    name: Required[str]
    """A short name to identify the health check.

    Only alphanumeric characters, hyphens and underscores are allowed.
    """

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
    ]
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

    http_config: Optional[HTTPConfig]
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

    tcp_config: Optional[TcpConfig]
    """Parameters specific to TCP health check."""

    healthcheck_timeout: Annotated[int, PropertyInfo(alias="timeout")]
    """The timeout (in seconds) before marking the health check as failed."""

    type: str
    """The protocol to use for the health check.

    Currently supported protocols are 'HTTP', 'HTTPS' and 'TCP'.
    """


class HTTPConfig(TypedDict, total=False):
    allow_insecure: bool
    """Do not validate the certificate when the health check uses HTTPS."""

    expected_body: str
    """A case-insensitive sub-string to look for in the response body.

    If this string is not found, the origin will be marked as unhealthy.
    """

    expected_codes: Optional[List[str]]
    """The expected HTTP response codes (e.g.

    "200") or code ranges (e.g. "2xx" for all codes starting with 2) of the health
    check.
    """

    follow_redirects: bool
    """Follow redirects if the origin returns a 3xx status code."""

    header: Optional[object]
    """The HTTP request headers to send in the health check.

    It is recommended you set a Host header by default. The User-Agent header cannot
    be overridden.
    """

    method: Literal["GET", "HEAD"]
    """The HTTP method to use for the health check."""

    path: str
    """The endpoint path to health check against."""

    port: int
    """Port number to connect to for the health check.

    Defaults to 80 if type is HTTP or 443 if type is HTTPS.
    """


class TcpConfig(TypedDict, total=False):
    method: Literal["connection_established"]
    """The TCP connection method to use for the health check."""

    port: int
    """Port number to connect to for the health check. Defaults to 80."""
