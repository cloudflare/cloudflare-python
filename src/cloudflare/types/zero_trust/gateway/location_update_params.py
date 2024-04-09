# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .location_network_param import LocationNetworkParam

__all__ = ["LocationUpdateParams"]


class LocationUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    name: Required[str]
    """The name of the location."""

    client_default: bool
    """True if the location is the default location."""

    ecs_support: bool
    """True if the location needs to resolve EDNS queries."""

    networks: Iterable[LocationNetworkParam]
    """A list of network ranges that requests from this location would originate from."""
