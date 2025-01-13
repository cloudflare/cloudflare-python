# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .ipv6_network_param import IPV6NetworkParam

__all__ = ["IPV6EndpointParam"]


class IPV6EndpointParam(TypedDict, total=False):
    enabled: bool
    """True if the endpoint is enabled for this location."""

    networks: Iterable[IPV6NetworkParam]
    """A list of allowed source IPv6 network ranges for this endpoint.

    When empty, all source IPs are allowed. A non-empty list is only effective if
    the endpoint is enabled for this location.
    """
