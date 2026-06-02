# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .endpoint import Endpoint
from ...._models import BaseModel

__all__ = ["Location", "Network"]


class Network(BaseModel):
    network: str
    """Specify the IPv4 address or IPv4 CIDR. Limit IPv4 CIDRs to a maximum of /24."""


class Location(BaseModel):
    id: Optional[str] = None

    client_default: Optional[bool] = None
    """Indicate whether this location is the default location."""

    created_at: Optional[datetime] = None

    dns_destination_ips_id: Optional[str] = None
    """
    Indicate the identifier of the pair of IPv4 addresses assigned to this location.
    """

    dns_destination_ipv6_block_id: Optional[str] = None
    """
    Specify the UUID of the IPv6 block brought to the gateway so that this
    location's IPv6 address is allocated from the Bring Your Own IPv6 (BYOIPv6)
    block rather than the standard Cloudflare IPv6 block.
    """

    doh_subdomain: Optional[str] = None
    """Specify the DNS over HTTPS domain that receives DNS requests.

    Gateway automatically generates this value.
    """

    ecs_support: Optional[bool] = None
    """Indicate whether the location must resolve EDNS queries."""

    endpoints: Optional[Endpoint] = None
    """Configure the destination endpoints for this location."""

    ip: Optional[str] = None
    """
    Defines the automatically generated IPv6 destination IP assigned to this
    location. Gateway counts all DNS requests sent to this IP as requests under this
    location.
    """

    ipv4_destination: Optional[str] = None
    """
    Show the primary destination IPv4 address from the pair identified
    dns_destination_ips_id. This field read-only.
    """

    ipv4_destination_backup: Optional[str] = None
    """
    Show the backup destination IPv4 address from the pair identified
    dns_destination_ips_id. This field read-only.
    """

    name: Optional[str] = None
    """Specify the location name."""

    networks: Optional[List[Network]] = None
    """
    Specify the list of network ranges from which requests at this location
    originate. The list takes effect only if it is non-empty and the IPv4 endpoint
    is enabled for this location.
    """

    updated_at: Optional[datetime] = None
