# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MonitorCreateParams"]


class MonitorCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    allow_insecure: bool
    """Do not validate the certificate when monitor use HTTPS.

    This parameter is currently only valid for HTTP and HTTPS monitors.
    """

    consecutive_down: int
    """
    To be marked unhealthy the monitored origin must fail this healthcheck N
    consecutive times.
    """

    consecutive_up: int
    """
    To be marked healthy the monitored origin must pass this healthcheck N
    consecutive times.
    """

    description: str
    """Object description."""

    expected_body: str
    """A case-insensitive sub-string to look for in the response body.

    If this string is not found, the origin will be marked as unhealthy. This
    parameter is only valid for HTTP and HTTPS monitors.
    """

    expected_codes: str
    """The expected HTTP response code or code range of the health check.

    This parameter is only valid for HTTP and HTTPS monitors.
    """

    follow_redirects: bool
    """Follow redirects if returned by the origin.

    This parameter is only valid for HTTP and HTTPS monitors.
    """

    header: Dict[str, List[str]]
    """The HTTP request headers to send in the health check.

    It is recommended you set a Host header by default. The User-Agent header cannot
    be overridden. This parameter is only valid for HTTP and HTTPS monitors.
    """

    interval: int
    """The interval between each health check.

    Shorter intervals may improve failover time, but will increase load on the
    origins as we check from multiple locations.
    """

    method: str
    """The method to use for the health check.

    This defaults to 'GET' for HTTP/HTTPS based checks and 'connection_established'
    for TCP based health checks.
    """

    path: str
    """The endpoint path you want to conduct a health check against.

    This parameter is only valid for HTTP and HTTPS monitors.
    """

    port: int
    """The port number to connect to for the health check.

    Required for TCP, UDP, and SMTP checks. HTTP and HTTPS checks should only define
    the port when using a non-standard port (HTTP: default 80, HTTPS: default 443).
    """

    probe_zone: str
    """Assign this monitor to emulate the specified zone while probing.

    This parameter is only valid for HTTP and HTTPS monitors.
    """

    retries: int
    """
    The number of retries to attempt in case of a timeout before marking the origin
    as unhealthy. Retries are attempted immediately.
    """

    load_balancer_monitor_timeout: Annotated[int, PropertyInfo(alias="timeout")]
    """The timeout (in seconds) before marking the health check as failed."""

    type: Literal["http", "https", "tcp", "udp_icmp", "icmp_ping", "smtp"]
    """The protocol to use for the health check.

    Currently supported protocols are 'HTTP','HTTPS', 'TCP', 'ICMP-PING',
    'UDP-ICMP', and 'SMTP'.
    """
