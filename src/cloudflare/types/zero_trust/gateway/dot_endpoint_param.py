# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import TypedDict

from .ip_network_param import IPNetworkParam

__all__ = ["DOTEndpointParam"]


class DOTEndpointParam(TypedDict, total=False):
    enabled: bool
    """Indicate whether the DOT endpoint is enabled for this location."""

    networks: Optional[Iterable[IPNetworkParam]]
    """Specify the list of allowed source IP network ranges for this endpoint.

    When the list is empty, the endpoint allows all source IPs. The list takes
    effect only if the endpoint is enabled for this location.
    """
