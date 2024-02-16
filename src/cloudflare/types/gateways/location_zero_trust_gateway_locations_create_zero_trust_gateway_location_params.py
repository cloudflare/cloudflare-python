# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import Iterable

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["LocationZeroTrustGatewayLocationsCreateZeroTrustGatewayLocationParams", "Network"]


class LocationZeroTrustGatewayLocationsCreateZeroTrustGatewayLocationParams(TypedDict, total=False):
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
