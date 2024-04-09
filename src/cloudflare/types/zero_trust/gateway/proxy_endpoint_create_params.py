# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from .gateway_ips import GatewayIPs

__all__ = ["ProxyEndpointCreateParams"]


class ProxyEndpointCreateParams(TypedDict, total=False):
    account_id: Required[str]

    ips: Required[List[GatewayIPs]]
    """A list of CIDRs to restrict ingress connections."""

    name: Required[str]
    """The name of the proxy endpoint."""
