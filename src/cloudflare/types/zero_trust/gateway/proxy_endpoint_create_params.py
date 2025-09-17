# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr
from .gateway_ips import GatewayIPs

__all__ = ["ProxyEndpointCreateParams"]


class ProxyEndpointCreateParams(TypedDict, total=False):
    account_id: Required[str]

    ips: Required[SequenceNotStr[GatewayIPs]]
    """Specify the list of CIDRs to restrict ingress connections."""

    name: Required[str]
    """Specify the name of the proxy endpoint."""
