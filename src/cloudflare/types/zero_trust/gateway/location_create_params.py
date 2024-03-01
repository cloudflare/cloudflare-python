# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["LocationCreateParams", "Network"]


class LocationCreateParams(TypedDict, total=False):
    account_id: Required[object]

    name: Required[str]
    """The name of the location."""

    client_default: bool
    """True if the location is the default location."""

    ecs_support: bool
    """True if the location needs to resolve EDNS queries."""

    networks: Iterable[Network]
    """A list of network ranges that requests from this location would originate from."""


class Network(TypedDict, total=False):
    network: Required[str]
    """The IPv4 address or IPv4 CIDR. IPv4 CIDRs are limited to a maximum of /24."""
