# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from .gateway_ips_item import GatewayIPsItem

__all__ = ["ProxyEndpointEditParams"]


class ProxyEndpointEditParams(TypedDict, total=False):
    account_id: Required[str]

    ips: List[GatewayIPsItem]
    """A list of CIDRs to restrict ingress connections."""

    name: str
    """The name of the proxy endpoint."""
