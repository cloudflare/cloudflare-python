# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DNSResolverSettingsV6Param"]


class DNSResolverSettingsV6Param(TypedDict, total=False):
    ip: Required[str]
    """IPv6 address of upstream resolver."""

    port: int
    """A port number to use for upstream resolver. Defaults to 53 if unspecified."""

    route_through_private_network: bool
    """Whether to connect to this resolver over a private network.

    Must be set when vnet_id is set.
    """

    vnet_id: str
    """Optionally specify a virtual network for this resolver.

    Uses default virtual network id if omitted.
    """
