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

__all__ = ["Teamnet", "AsyncTeamnet"]


class Teamnet(SyncAPIResource):
    @cached_property
    def routes(self) -> Routes:
        return Routes(self._client)

    @cached_property
    def virtual_networks(self) -> VirtualNetworks:
        return VirtualNetworks(self._client)

    @cached_property
    def with_raw_response(self) -> TeamnetWithRawResponse:
        return TeamnetWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TeamnetWithStreamingResponse:
        return TeamnetWithStreamingResponse(self)


class AsyncTeamnet(AsyncAPIResource):
    @cached_property
    def routes(self) -> AsyncRoutes:
        return AsyncRoutes(self._client)

    @cached_property
    def virtual_networks(self) -> AsyncVirtualNetworks:
        return AsyncVirtualNetworks(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTeamnetWithRawResponse:
        return AsyncTeamnetWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTeamnetWithStreamingResponse:
        return AsyncTeamnetWithStreamingResponse(self)


class TeamnetWithRawResponse:
    def __init__(self, teamnet: Teamnet) -> None:
        self._teamnet = teamnet

    @cached_property
    def routes(self) -> RoutesWithRawResponse:
        return RoutesWithRawResponse(self._teamnet.routes)

    @cached_property
    def virtual_networks(self) -> VirtualNetworksWithRawResponse:
        return VirtualNetworksWithRawResponse(self._teamnet.virtual_networks)


class AsyncTeamnetWithRawResponse:
    def __init__(self, teamnet: AsyncTeamnet) -> None:
        self._teamnet = teamnet

    @cached_property
    def routes(self) -> AsyncRoutesWithRawResponse:
        return AsyncRoutesWithRawResponse(self._teamnet.routes)

    @cached_property
    def virtual_networks(self) -> AsyncVirtualNetworksWithRawResponse:
        return AsyncVirtualNetworksWithRawResponse(self._teamnet.virtual_networks)


class TeamnetWithStreamingResponse:
    def __init__(self, teamnet: Teamnet) -> None:
        self._teamnet = teamnet

    @cached_property
    def routes(self) -> RoutesWithStreamingResponse:
        return RoutesWithStreamingResponse(self._teamnet.routes)

    @cached_property
    def virtual_networks(self) -> VirtualNetworksWithStreamingResponse:
        return VirtualNetworksWithStreamingResponse(self._teamnet.virtual_networks)


class AsyncTeamnetWithStreamingResponse:
    def __init__(self, teamnet: AsyncTeamnet) -> None:
        self._teamnet = teamnet

    @cached_property
    def routes(self) -> AsyncRoutesWithStreamingResponse:
        return AsyncRoutesWithStreamingResponse(self._teamnet.routes)

    @cached_property
    def virtual_networks(self) -> AsyncVirtualNetworksWithStreamingResponse:
        return AsyncVirtualNetworksWithStreamingResponse(self._teamnet.virtual_networks)
