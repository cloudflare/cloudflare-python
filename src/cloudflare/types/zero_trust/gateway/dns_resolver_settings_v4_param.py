# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DNSResolverSettingsV4Param"]


class DNSResolverSettingsV4Param(TypedDict, total=False):
    ip: Required[str]
    """Specify the IPv4 address of the upstream resolver."""

    port: int
    """Specify a port number to use for the upstream resolver.

    Defaults to 53 if unspecified.
    """

    route_through_private_network: bool
    """Indicate whether to connect to this resolver over a private network.

    Must set when vnet_id set.
    """

    vnet_id: str
    """Specify an optional virtual network for this resolver.

    Uses default virtual network id if omitted.
    """
