# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .routes import (
    Routes,
    AsyncRoutes,
    RoutesWithRawResponse,
    AsyncRoutesWithRawResponse,
    RoutesWithStreamingResponse,
    AsyncRoutesWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .routes.routes import Routes, AsyncRoutes
from .virtual_networks import (
    VirtualNetworks,
    AsyncVirtualNetworks,
    VirtualNetworksWithRawResponse,
    AsyncVirtualNetworksWithRawResponse,
    VirtualNetworksWithStreamingResponse,
    AsyncVirtualNetworksWithStreamingResponse,
)

__all__ = ["Teamnets", "AsyncTeamnets"]


class Teamnets(SyncAPIResource):
    @cached_property
    def routes(self) -> Routes:
        return Routes(self._client)

    @cached_property
    def virtual_networks(self) -> VirtualNetworks:
        return VirtualNetworks(self._client)

    @cached_property
    def with_raw_response(self) -> TeamnetsWithRawResponse:
        return TeamnetsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TeamnetsWithStreamingResponse:
        return TeamnetsWithStreamingResponse(self)


class AsyncTeamnets(AsyncAPIResource):
    @cached_property
    def routes(self) -> AsyncRoutes:
        return AsyncRoutes(self._client)

    @cached_property
    def virtual_networks(self) -> AsyncVirtualNetworks:
        return AsyncVirtualNetworks(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTeamnetsWithRawResponse:
        return AsyncTeamnetsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTeamnetsWithStreamingResponse:
        return AsyncTeamnetsWithStreamingResponse(self)


class TeamnetsWithRawResponse:
    def __init__(self, teamnets: Teamnets) -> None:
        self._teamnets = teamnets

    @cached_property
    def routes(self) -> RoutesWithRawResponse:
        return RoutesWithRawResponse(self._teamnets.routes)

    @cached_property
    def virtual_networks(self) -> VirtualNetworksWithRawResponse:
        return VirtualNetworksWithRawResponse(self._teamnets.virtual_networks)


class AsyncTeamnetsWithRawResponse:
    def __init__(self, teamnets: AsyncTeamnets) -> None:
        self._teamnets = teamnets

    @cached_property
    def routes(self) -> AsyncRoutesWithRawResponse:
        return AsyncRoutesWithRawResponse(self._teamnets.routes)

    @cached_property
    def virtual_networks(self) -> AsyncVirtualNetworksWithRawResponse:
        return AsyncVirtualNetworksWithRawResponse(self._teamnets.virtual_networks)


class TeamnetsWithStreamingResponse:
    def __init__(self, teamnets: Teamnets) -> None:
        self._teamnets = teamnets

    @cached_property
    def routes(self) -> RoutesWithStreamingResponse:
        return RoutesWithStreamingResponse(self._teamnets.routes)

    @cached_property
    def virtual_networks(self) -> VirtualNetworksWithStreamingResponse:
        return VirtualNetworksWithStreamingResponse(self._teamnets.virtual_networks)


class AsyncTeamnetsWithStreamingResponse:
    def __init__(self, teamnets: AsyncTeamnets) -> None:
        self._teamnets = teamnets

    @cached_property
    def routes(self) -> AsyncRoutesWithStreamingResponse:
        return AsyncRoutesWithStreamingResponse(self._teamnets.routes)

    @cached_property
    def virtual_networks(self) -> AsyncVirtualNetworksWithStreamingResponse:
        return AsyncVirtualNetworksWithStreamingResponse(self._teamnets.virtual_networks)
