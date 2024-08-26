# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .dns_param import DNSParam
from .edge_ips_param import EdgeIPsParam
from .origin_dns_param import OriginDNSParam
from .origin_port_param import OriginPortParam

__all__ = ["AppCreateParams", "SpectrumConfigAppConfig", "SpectrumConfigPaygoAppConfig"]


class SpectrumConfigAppConfig(TypedDict, total=False):
    zone_id: Required[str]
    """Zone identifier."""

    dns: Required[DNSParam]
    """The name and type of DNS record for the Spectrum application."""

    ip_firewall: Required[bool]
    """
    Enables IP Access Rules for this application. Notes: Only available for TCP
    applications.
    """

    protocol: Required[str]
    """The port configuration at Cloudflare's edge.

    May specify a single port, for example `"tcp/1000"`, or a range of ports, for
    example `"tcp/1000-2000"`.
    """

    proxy_protocol: Required[Literal["off", "v1", "v2", "simple"]]
    """Enables Proxy Protocol to the origin.

    Refer to
    [Enable Proxy protocol](https://developers.cloudflare.com/spectrum/getting-started/proxy-protocol/)
    for implementation details on PROXY Protocol V1, PROXY Protocol V2, and Simple
    Proxy Protocol.
    """

    tls: Required[Literal["off", "flexible", "full", "strict"]]
    """The type of TLS termination associated with the application."""

    traffic_type: Required[Literal["direct", "http", "https"]]
    """Determines how data travels from the edge to your origin.

    When set to "direct", Spectrum will send traffic directly to your origin, and
    the application's type is derived from the `protocol`. When set to "http" or
    "https", Spectrum will apply Cloudflare's HTTP/HTTPS features as it sends
    traffic to your origin, and the application type matches this property exactly.
    """

    argo_smart_routing: bool
    """
    Enables Argo Smart Routing for this application. Notes: Only available for TCP
    applications with traffic_type set to "direct".
    """

    edge_ips: EdgeIPsParam
    """The anycast edge IP configuration for the hostname of this application."""

    origin_direct: List[str]
    """List of origin IP addresses.

    Array may contain multiple IP addresses for load balancing.
    """

    origin_dns: OriginDNSParam
    """The name and type of DNS record for the Spectrum application."""

    origin_port: OriginPortParam
    """The destination port at the origin.

    Only specified in conjunction with origin_dns. May use an integer to specify a
    single origin port, for example `1000`, or a string to specify a range of origin
    ports, for example `"1000-2000"`. Notes: If specifying a port range, the number
    of ports in the range must match the number of ports specified in the "protocol"
    field.
    """


class SpectrumConfigPaygoAppConfig(TypedDict, total=False):
    zone_id: Required[str]
    """Zone identifier."""

    dns: Required[DNSParam]
    """The name and type of DNS record for the Spectrum application."""

    protocol: Required[str]
    """The port configuration at Cloudflare's edge.

    May specify a single port, for example `"tcp/1000"`, or a range of ports, for
    example `"tcp/1000-2000"`.
    """

    origin_direct: List[str]
    """List of origin IP addresses.

    Array may contain multiple IP addresses for load balancing.
    """


AppCreateParams: TypeAlias = Union[SpectrumConfigAppConfig, SpectrumConfigPaygoAppConfig]
