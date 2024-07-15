# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = [
    "Location",
    "Endpoints",
    "EndpointsDoh",
    "EndpointsDohNetwork",
    "EndpointsDot",
    "EndpointsDotNetwork",
    "EndpointsIPV4",
    "EndpointsIPV6",
    "EndpointsIPV6Network",
    "Network",
]


class EndpointsDohNetwork(BaseModel):
    network: str
    """The IP address or IP CIDR."""


class EndpointsDoh(BaseModel):
    enabled: Optional[bool] = None
    """True if the endpoint is enabled for this location."""

    networks: Optional[List[EndpointsDohNetwork]] = None
    """A list of allowed source IP network ranges for this endpoint.

    When empty, all source IPs are allowed. A non-empty list is only effective if
    the endpoint is enabled for this location.
    """

    require_token: Optional[bool] = None
    """
    True if the endpoint requires
    [user identity](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/agentless/dns/dns-over-https/#filter-doh-requests-by-user)
    authentication.
    """


class EndpointsDotNetwork(BaseModel):
    network: str
    """The IP address or IP CIDR."""


class EndpointsDot(BaseModel):
    enabled: Optional[bool] = None
    """True if the endpoint is enabled for this location."""

    networks: Optional[List[EndpointsDotNetwork]] = None
    """A list of allowed source IP network ranges for this endpoint.

    When empty, all source IPs are allowed. A non-empty list is only effective if
    the endpoint is enabled for this location.
    """


class EndpointsIPV4(BaseModel):
    enabled: Optional[bool] = None
    """True if the endpoint is enabled for this location."""


class EndpointsIPV6Network(BaseModel):
    network: str
    """The IPv6 address or IPv6 CIDR."""


class EndpointsIPV6(BaseModel):
    enabled: Optional[bool] = None
    """True if the endpoint is enabled for this location."""

    networks: Optional[List[EndpointsIPV6Network]] = None
    """A list of allowed source IPv6 network ranges for this endpoint.

    When empty, all source IPs are allowed. A non-empty list is only effective if
    the endpoint is enabled for this location.
    """


class Endpoints(BaseModel):
    doh: Optional[EndpointsDoh] = None

    dot: Optional[EndpointsDot] = None

    ipv4: Optional[EndpointsIPV4] = None

    ipv6: Optional[EndpointsIPV6] = None


class Network(BaseModel):
    network: str
    """The IPv4 address or IPv4 CIDR. IPv4 CIDRs are limited to a maximum of /24."""


class Location(BaseModel):
    id: Optional[str] = None

    client_default: Optional[bool] = None
    """True if the location is the default location."""

    created_at: Optional[datetime] = None

    dns_destination_ips_id: Optional[str] = None
    """The identifier of the pair of IPv4 addresses assigned to this location."""

    doh_subdomain: Optional[str] = None
    """The DNS over HTTPS domain to send DNS requests to.

    This field is auto-generated by Gateway.
    """

    ecs_support: Optional[bool] = None
    """True if the location needs to resolve EDNS queries."""

    endpoints: Optional[Endpoints] = None
    """The destination endpoints configured for this location.

    When updating a location, if this field is absent or set with null, the
    endpoints configuration remains unchanged.
    """

    ip: Optional[str] = None
    """IPV6 destination ip assigned to this location.

    DNS requests sent to this IP will counted as the request under this location.
    This field is auto-generated by Gateway.
    """

    ipv4_destination: Optional[str] = None
    """
    The primary destination IPv4 address from the pair identified by the
    dns_destination_ips_id. This field is read-only.
    """

    ipv4_destination_backup: Optional[str] = None
    """
    The backup destination IPv4 address from the pair identified by the
    dns_destination_ips_id. This field is read-only.
    """

    name: Optional[str] = None
    """The name of the location."""

    networks: Optional[List[Network]] = None
    """A list of network ranges that requests from this location would originate from.

    A non-empty list is only effective if the ipv4 endpoint is enabled for this
    location.
    """

    updated_at: Optional[datetime] = None
