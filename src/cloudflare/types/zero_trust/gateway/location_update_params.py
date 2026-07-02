# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .endpoint_param import EndpointParam

__all__ = ["LocationUpdateParams", "MaxTTL", "Network"]


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

    max_ttl: Optional[MaxTTL]
    """
    Controls how DNS response TTLs are capped for this location relative to the
    account `max_ttl_secs` setting. Omitting `max_ttl` on update resets it to
    `inherit`.
    """

    networks: Optional[Iterable[Network]]
    """
    Specify the list of network ranges from which requests at this location
    originate. The list takes effect only if it is non-empty and the IPv4 endpoint
    is enabled for this location.
    """


class MaxTTL(TypedDict, total=False):
    """
    Controls how DNS response TTLs are capped for this location relative to the account `max_ttl_secs` setting. Omitting `max_ttl` on update resets it to `inherit`.
    """

    mode: Required[Literal["inherit", "override", "disabled"]]
    """`inherit` uses the account `max_ttl_secs`.

    `override` uses this location's `ttl_secs`. `disabled` leaves returned TTLs
    unchanged.
    """

    ttl_secs: Optional[int]
    """Location-specific cap on DNS response TTLs, in seconds.

    Required when `mode` is `override`. Must be omitted when `mode` is `inherit` or
    `disabled`.
    """


class Network(TypedDict, total=False):
    network: Required[str]
    """Specify the IPv4 address or IPv4 CIDR. Limit IPv4 CIDRs to a maximum of /24."""
