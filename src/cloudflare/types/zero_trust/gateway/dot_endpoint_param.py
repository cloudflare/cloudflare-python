# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .ip_network_param import IPNetworkParam

__all__ = ["DOTEndpointParam"]


class DOTEndpointParam(TypedDict, total=False):
    enabled: bool
    """True if the endpoint is enabled for this location."""

    networks: Iterable[IPNetworkParam]
    """A list of allowed source IP network ranges for this endpoint.

    When empty, all source IPs are allowed. A non-empty list is only effective if
    the endpoint is enabled for this location.
    """
