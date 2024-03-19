# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AppUpdateParams", "DNS", "OriginDNS", "EdgeIPs", "EdgeIPsEyeballIPs", "EdgeIPsCustomerOwnedIPs"]


class AppUpdateParams(TypedDict, total=False):
    zone: Required[str]
    """Identifier"""

    dns: Required[DNS]
    """The name and type of DNS record for the Spectrum application."""

    origin_dns: Required[OriginDNS]
    """The name and type of DNS record for the Spectrum application."""

    origin_port: Required[Union[int, str]]
    """The destination port at the origin.

    Only specified in conjunction with origin_dns. May use an integer to specify a
    single origin port, for example `1000`, or a string to specify a range of origin
    ports, for example `"1000-2000"`. Notes: If specifying a port range, the number
    of ports in the range must match the number of ports specified in the "protocol"
    field.
    """

    protocol: Required[str]
    """The port configuration at Cloudflare’s edge.

    May specify a single port, for example `"tcp/1000"`, or a range of ports, for
    example `"tcp/1000-2000"`.
    """

    argo_smart_routing: bool
    """
    Enables Argo Smart Routing for this application. Notes: Only available for TCP
    applications with traffic_type set to "direct".
    """

    edge_ips: EdgeIPs
    """The anycast edge IP configuration for the hostname of this application."""

    ip_firewall: bool
    """
    Enables IP Access Rules for this application. Notes: Only available for TCP
    applications.
    """

    proxy_protocol: Literal["off", "v1", "v2", "simple"]
    """Enables Proxy Protocol to the origin.

    Refer to
    [Enable Proxy protocol](https://developers.cloudflare.com/spectrum/getting-started/proxy-protocol/)
    for implementation details on PROXY Protocol V1, PROXY Protocol V2, and Simple
    Proxy Protocol.
    """

    tls: Literal["off", "flexible", "full", "strict"]
    """The type of TLS termination associated with the application."""

    traffic_type: Literal["direct", "http", "https"]
    """Determines how data travels from the edge to your origin.

    When set to "direct", Spectrum will send traffic directly to your origin, and
    the application's type is derived from the `protocol`. When set to "http" or
    "https", Spectrum will apply Cloudflare's HTTP/HTTPS features as it sends
    traffic to your origin, and the application type matches this property exactly.
    """


class DNS(TypedDict, total=False):
    name: str
    """The name of the DNS record associated with the application."""

    type: Literal["CNAME", "ADDRESS"]
    """The type of DNS record associated with the application."""


class OriginDNS(TypedDict, total=False):
    name: str
    """The name of the DNS record associated with the origin."""

    ttl: int
    """The TTL of our resolution of your DNS record in seconds."""

    type: Literal["", "A", "AAAA", "SRV"]
    """The type of DNS record associated with the origin.

    "" is used to specify a combination of A/AAAA records.
    """


class EdgeIPsEyeballIPs(TypedDict, total=False):
    connectivity: Literal["all", "ipv4", "ipv6"]
    """The IP versions supported for inbound connections on Spectrum anycast IPs."""

    type: Literal["dynamic"]
    """The type of edge IP configuration specified.

    Dynamically allocated edge IPs use Spectrum anycast IPs in accordance with the
    connectivity you specify. Only valid with CNAME DNS names.
    """


class EdgeIPsCustomerOwnedIPs(TypedDict, total=False):
    ips: List[str]
    """
    The array of customer owned IPs we broadcast via anycast for this hostname and
    application.
    """

    type: Literal["static"]
    """The type of edge IP configuration specified.

    Statically allocated edge IPs use customer IPs in accordance with the ips array
    you specify. Only valid with ADDRESS DNS names.
    """


EdgeIPs = Union[EdgeIPsEyeballIPs, EdgeIPsCustomerOwnedIPs]
