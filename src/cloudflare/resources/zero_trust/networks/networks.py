# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .routes import (
    Routes,
    AsyncRoutes,
    RoutesWithRawResponse,
    AsyncRoutesWithRawResponse,
    RoutesWithStreamingResponse,
    AsyncRoutesWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .routes.routes import Routes, AsyncRoutes
from .virtual_networks import (
    VirtualNetworks,
    AsyncVirtualNetworks,
    VirtualNetworksWithRawResponse,
    AsyncVirtualNetworksWithRawResponse,
    VirtualNetworksWithStreamingResponse,
    AsyncVirtualNetworksWithStreamingResponse,
)

__all__ = ["Networks", "AsyncNetworks"]


class Networks(SyncAPIResource):
    @cached_property
    def routes(self) -> Routes:
        return Routes(self._client)

    @cached_property
    def virtual_networks(self) -> VirtualNetworks:
        return VirtualNetworks(self._client)

    @cached_property
    def with_raw_response(self) -> NetworksWithRawResponse:
        return NetworksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NetworksWithStreamingResponse:
        return NetworksWithStreamingResponse(self)


class AsyncNetworks(AsyncAPIResource):
    @cached_property
    def routes(self) -> AsyncRoutes:
        return AsyncRoutes(self._client)

    @cached_property
    def virtual_networks(self) -> AsyncVirtualNetworks:
        return AsyncVirtualNetworks(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNetworksWithRawResponse:
        return AsyncNetworksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNetworksWithStreamingResponse:
        return AsyncNetworksWithStreamingResponse(self)


class NetworksWithRawResponse:
    def __init__(self, networks: Networks) -> None:
        self._networks = networks

    @cached_property
    def routes(self) -> RoutesWithRawResponse:
        return RoutesWithRawResponse(self._networks.routes)

    @cached_property
    def virtual_networks(self) -> VirtualNetworksWithRawResponse:
        return VirtualNetworksWithRawResponse(self._networks.virtual_networks)


class AsyncNetworksWithRawResponse:
    def __init__(self, networks: AsyncNetworks) -> None:
        self._networks = networks

    @cached_property
    def routes(self) -> AsyncRoutesWithRawResponse:
        return AsyncRoutesWithRawResponse(self._networks.routes)

    @cached_property
    def virtual_networks(self) -> AsyncVirtualNetworksWithRawResponse:
        return AsyncVirtualNetworksWithRawResponse(self._networks.virtual_networks)


class NetworksWithStreamingResponse:
    def __init__(self, networks: Networks) -> None:
        self._networks = networks

    @cached_property
    def routes(self) -> RoutesWithStreamingResponse:
        return RoutesWithStreamingResponse(self._networks.routes)

    @cached_property
    def virtual_networks(self) -> VirtualNetworksWithStreamingResponse:
        return VirtualNetworksWithStreamingResponse(self._networks.virtual_networks)


class AsyncNetworksWithStreamingResponse:
    def __init__(self, networks: AsyncNetworks) -> None:
        self._networks = networks

    @cached_property
    def routes(self) -> AsyncRoutesWithStreamingResponse:
        return AsyncRoutesWithStreamingResponse(self._networks.routes)

    @cached_property
    def virtual_networks(self) -> AsyncVirtualNetworksWithStreamingResponse:
        return AsyncVirtualNetworksWithStreamingResponse(self._networks.virtual_networks)
