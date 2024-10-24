# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Monitor"]


class Monitor(BaseModel):
    id: Optional[str] = None

    allow_insecure: Optional[bool] = None
    """Do not validate the certificate when monitor use HTTPS.

    This parameter is currently only valid for HTTP and HTTPS monitors.
    """

    consecutive_down: Optional[int] = None
    """
    To be marked unhealthy the monitored origin must fail this healthcheck N
    consecutive times.
    """

    consecutive_up: Optional[int] = None
    """
    To be marked healthy the monitored origin must pass this healthcheck N
    consecutive times.
    """

    created_on: Optional[str] = None

    description: Optional[str] = None
    """Object description."""

    expected_body: Optional[str] = None
    """A case-insensitive sub-string to look for in the response body.

    If this string is not found, the origin will be marked as unhealthy. This
    parameter is only valid for HTTP and HTTPS monitors.
    """

    expected_codes: Optional[str] = None
    """The expected HTTP response code or code range of the health check.

    This parameter is only valid for HTTP and HTTPS monitors.
    """

    follow_redirects: Optional[bool] = None
    """Follow redirects if returned by the origin.

    This parameter is only valid for HTTP and HTTPS monitors.
    """

    header: Optional[Dict[str, List[str]]] = None
    """The HTTP request headers to send in the health check.

    It is recommended you set a Host header by default. The User-Agent header cannot
    be overridden. This parameter is only valid for HTTP and HTTPS monitors.
    """

    interval: Optional[int] = None
    """The interval between each health check.

    Shorter intervals may improve failover time, but will increase load on the
    origins as we check from multiple locations.
    """

    method: Optional[str] = None
    """The method to use for the health check.

    This defaults to 'GET' for HTTP/HTTPS based checks and 'connection_established'
    for TCP based health checks.
    """

    modified_on: Optional[str] = None

    path: Optional[str] = None
    """The endpoint path you want to conduct a health check against.

    This parameter is only valid for HTTP and HTTPS monitors.
    """

    port: Optional[int] = None
    """The port number to connect to for the health check.

    Required for TCP, UDP, and SMTP checks. HTTP and HTTPS checks should only define
    the port when using a non-standard port (HTTP: default 80, HTTPS: default 443).
    """

    probe_zone: Optional[str] = None
    """Assign this monitor to emulate the specified zone while probing.

    This parameter is only valid for HTTP and HTTPS monitors.
    """

    retries: Optional[int] = None
    """
    The number of retries to attempt in case of a timeout before marking the origin
    as unhealthy. Retries are attempted immediately.
    """

    timeout: Optional[int] = None
    """The timeout (in seconds) before marking the health check as failed."""

    type: Optional[Literal["http", "https", "tcp", "udp_icmp", "icmp_ping", "smtp"]] = None
    """The protocol to use for the health check.

    Currently supported protocols are 'HTTP','HTTPS', 'TCP', 'ICMP-PING',
    'UDP-ICMP', and 'SMTP'.
    """
