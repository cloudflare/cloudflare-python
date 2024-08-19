# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .dns import DNS
from .edge_ips import EdgeIPs
from ..._models import BaseModel
from .origin_dns import OriginDNS
from .origin_port import OriginPort

__all__ = ["AppGetResponse", "SpectrumConfigAppConfig", "SpectrumConfigPaygoAppConfig"]


class SpectrumConfigAppConfig(BaseModel):
    id: str
    """App identifier."""

    created_on: datetime
    """When the Application was created."""

    dns: DNS
    """The name and type of DNS record for the Spectrum application."""

    ip_firewall: bool
    """
    Enables IP Access Rules for this application. Notes: Only available for TCP
    applications.
    """

    modified_on: datetime
    """When the Application was last modified."""

    protocol: str
    """The port configuration at Cloudflare's edge.

    May specify a single port, for example `"tcp/1000"`, or a range of ports, for
    example `"tcp/1000-2000"`.
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

    argo_smart_routing: Optional[bool] = None
    """
    Enables Argo Smart Routing for this application. Notes: Only available for TCP
    applications with traffic_type set to "direct".
    """

    edge_ips: Optional[EdgeIPs] = None
    """The anycast edge IP configuration for the hostname of this application."""

    origin_direct: Optional[List[str]] = None
    """List of origin IP addresses.

    Array may contain multiple IP addresses for load balancing.
    """

    origin_dns: Optional[OriginDNS] = None
    """The name and type of DNS record for the Spectrum application."""

    origin_port: Optional[OriginPort] = None
    """The destination port at the origin.

    Only specified in conjunction with origin_dns. May use an integer to specify a
    single origin port, for example `1000`, or a string to specify a range of origin
    ports, for example `"1000-2000"`. Notes: If specifying a port range, the number
    of ports in the range must match the number of ports specified in the "protocol"
    field.
    """


class SpectrumConfigPaygoAppConfig(BaseModel):
    id: str
    """App identifier."""

    created_on: datetime
    """When the Application was created."""

    dns: DNS
    """The name and type of DNS record for the Spectrum application."""

    modified_on: datetime
    """When the Application was last modified."""

    protocol: str
    """The port configuration at Cloudflare's edge.

    May specify a single port, for example `"tcp/1000"`, or a range of ports, for
    example `"tcp/1000-2000"`.
    """

    origin_direct: Optional[List[str]] = None
    """List of origin IP addresses.

    Array may contain multiple IP addresses for load balancing.
    """


AppGetResponse: TypeAlias = Union[SpectrumConfigAppConfig, SpectrumConfigPaygoAppConfig]
