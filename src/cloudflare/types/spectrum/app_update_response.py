# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AppUpdateResponse", "DNS", "EdgeIPs", "EdgeIPsEyeballIPs", "EdgeIPsCustomerOwnedIPs", "OriginDNS"]


class DNS(BaseModel):
    name: Optional[str] = None
    """The name of the DNS record associated with the application."""

    type: Optional[Literal["CNAME", "ADDRESS"]] = None
    """The type of DNS record associated with the application."""


class EdgeIPsEyeballIPs(BaseModel):
    connectivity: Optional[Literal["all", "ipv4", "ipv6"]] = None
    """The IP versions supported for inbound connections on Spectrum anycast IPs."""

    type: Optional[Literal["dynamic"]] = None
    """The type of edge IP configuration specified.

    Dynamically allocated edge IPs use Spectrum anycast IPs in accordance with the
    connectivity you specify. Only valid with CNAME DNS names.
    """


class EdgeIPsCustomerOwnedIPs(BaseModel):
    ips: Optional[List[str]] = None
    """
    The array of customer owned IPs we broadcast via anycast for this hostname and
    application.
    """

    type: Optional[Literal["static"]] = None
    """The type of edge IP configuration specified.

    Statically allocated edge IPs use customer IPs in accordance with the ips array
    you specify. Only valid with ADDRESS DNS names.
    """


EdgeIPs = Union[EdgeIPsEyeballIPs, EdgeIPsCustomerOwnedIPs]


class OriginDNS(BaseModel):
    name: Optional[str] = None
    """The name of the DNS record associated with the origin."""

    ttl: Optional[int] = None
    """The TTL of our resolution of your DNS record in seconds."""

    type: Optional[Literal["", "A", "AAAA", "SRV"]] = None
    """The type of DNS record associated with the origin.

    "" is used to specify a combination of A/AAAA records.
    """


class AppUpdateResponse(BaseModel):
    id: Optional[str] = None
    """Application identifier."""

    argo_smart_routing: Optional[bool] = None
    """
    Enables Argo Smart Routing for this application. Notes: Only available for TCP
    applications with traffic_type set to "direct".
    """

    created_on: Optional[datetime] = None
    """When the Application was created."""

    dns: Optional[DNS] = None
    """The name and type of DNS record for the Spectrum application."""

    edge_ips: Optional[EdgeIPs] = None
    """The anycast edge IP configuration for the hostname of this application."""

    ip_firewall: Optional[bool] = None
    """
    Enables IP Access Rules for this application. Notes: Only available for TCP
    applications.
    """

    modified_on: Optional[datetime] = None
    """When the Application was last modified."""

    origin_dns: Optional[OriginDNS] = None
    """The name and type of DNS record for the Spectrum application."""

    origin_port: Union[int, str, None] = None
    """The destination port at the origin.

    Only specified in conjunction with origin_dns. May use an integer to specify a
    single origin port, for example `1000`, or a string to specify a range of origin
    ports, for example `"1000-2000"`. Notes: If specifying a port range, the number
    of ports in the range must match the number of ports specified in the "protocol"
    field.
    """

    protocol: Optional[str] = None
    """The port configuration at Cloudflare’s edge.

    May specify a single port, for example `"tcp/1000"`, or a range of ports, for
    example `"tcp/1000-2000"`.
    """

    proxy_protocol: Optional[Literal["off", "v1", "v2", "simple"]] = None
    """Enables Proxy Protocol to the origin.

    Refer to
    [Enable Proxy protocol](https://developers.cloudflare.com/spectrum/getting-started/proxy-protocol/)
    for implementation details on PROXY Protocol V1, PROXY Protocol V2, and Simple
    Proxy Protocol.
    """

    tls: Optional[Literal["off", "flexible", "full", "strict"]] = None
    """The type of TLS termination associated with the application."""

    traffic_type: Optional[Literal["direct", "http", "https"]] = None
    """Determines how data travels from the edge to your origin.

    When set to "direct", Spectrum will send traffic directly to your origin, and
    the application's type is derived from the `protocol`. When set to "http" or
    "https", Spectrum will apply Cloudflare's HTTP/HTTPS features as it sends
    traffic to your origin, and the application type matches this property exactly.
    """
