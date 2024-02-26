# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["ProxyEndpointEditParams"]


class ProxyEndpointEditParams(TypedDict, total=False):
    account_id: Required[object]

    ips: List[str]
    """A list of CIDRs to restrict ingress connections."""

    name: str
    """The name of the proxy endpoint."""

    subdomain: str
    """The subdomain to be used as the destination in the proxy client."""
