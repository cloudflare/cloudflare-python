# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import TypedDict

from .ipv6_network_param import IPV6NetworkParam

__all__ = ["IPV6EndpointParam"]


class IPV6EndpointParam(TypedDict, total=False):
    enabled: bool
    """Indicate whether the IPV6 endpoint is enabled for this location."""

    networks: Optional[Iterable[IPV6NetworkParam]]
    """Specify the list of allowed source IPv6 network ranges for this endpoint.

    When the list is empty, the endpoint allows all source IPs. The list takes
    effect only if the endpoint is enabled for this location.
    """
