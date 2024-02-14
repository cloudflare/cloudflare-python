# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VirtualNetworkTunnelVirtualNetworkListVirtualNetworksParams"]


class VirtualNetworkTunnelVirtualNetworkListVirtualNetworksParams(TypedDict, total=False):
    is_default: object
    """If `true`, only include the default virtual network.

    If `false`, exclude the default virtual network. If empty, all virtual networks
    will be included.
    """

    is_deleted: object
    """If `true`, only include deleted virtual networks.

    If `false`, exclude deleted virtual networks. If empty, all virtual networks
    will be included.
    """

    name: str
    """A user-friendly name for the virtual network."""

    vnet_name: str
    """A user-friendly name for the virtual network."""
