# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .endpoint_param import EndpointParam

__all__ = ["LocationUpdateParams", "Network"]


class LocationUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    name: Required[str]
    """The name of the location."""

    client_default: bool
    """True if the location is the default location."""

    dns_destination_ips_id: str
    """The identifier of the pair of IPv4 addresses assigned to this location.

    When creating a location, if this field is absent or set with null, the pair of
    shared IPv4 addresses (0e4a32c6-6fb8-4858-9296-98f51631e8e6) is auto-assigned.
    When updating a location, if the field is absent or set with null, the
    pre-assigned pair remains unchanged.
    """

    ecs_support: bool
    """True if the location needs to resolve EDNS queries."""

    endpoints: EndpointParam
    """The destination endpoints configured for this location.

    When updating a location, if this field is absent or set with null, the
    endpoints configuration remains unchanged.
    """

    networks: Iterable[Network]
    """A list of network ranges that requests from this location would originate from.

    A non-empty list is only effective if the ipv4 endpoint is enabled for this
    location.
    """


class Network(TypedDict, total=False):
    network: Required[str]
    """The IPv4 address or IPv4 CIDR. IPv4 CIDRs are limited to a maximum of /24."""
