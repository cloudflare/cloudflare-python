# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .endpoint_param import EndpointParam

__all__ = ["LocationUpdateParams", "Network"]


class LocationUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    name: Required[str]
    """Specify the location name."""

    client_default: bool
    """Indicate whether this location is the default location."""

    dns_destination_ips_id: str
    """Specify the identifier of the pair of IPv4 addresses assigned to this location.

    When creating a location, if this field is absent or set to null, the pair of
    shared IPv4 addresses (0e4a32c6-6fb8-4858-9296-98f51631e8e6) is auto-assigned.
    When updating a location, if this field is absent or set to null, the
    pre-assigned pair remains unchanged.
    """

    ecs_support: bool
    """Indicate whether the location must resolve EDNS queries."""

    endpoints: Optional[EndpointParam]
    """Configure the destination endpoints for this location."""

    networks: Optional[Iterable[Network]]
    """
    Specify the list of network ranges from which requests at this location
    originate. The list takes effect only if it is non-empty and the IPv4 endpoint
    is enabled for this location.
    """


class Network(TypedDict, total=False):
    network: Required[str]
    """Specify the IPv4 address or IPv4 CIDR. Limit IPv4 CIDRs to a maximum of /24."""
