# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .endpoint import Endpoint
from ...._models import BaseModel

__all__ = ["Location", "Network"]


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

    endpoints: Optional[Endpoint] = None
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