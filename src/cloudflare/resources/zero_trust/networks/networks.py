# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .routes import (
    RoutesResource,
    AsyncRoutesResource,
    RoutesResourceWithRawResponse,
    AsyncRoutesResourceWithRawResponse,
    RoutesResourceWithStreamingResponse,
    AsyncRoutesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .routes.routes import RoutesResource, AsyncRoutesResource
from .virtual_networks import (
    VirtualNetworksResource,
    AsyncVirtualNetworksResource,
    VirtualNetworksResourceWithRawResponse,
    AsyncVirtualNetworksResourceWithRawResponse,
    VirtualNetworksResourceWithStreamingResponse,
    AsyncVirtualNetworksResourceWithStreamingResponse,
)

__all__ = ["NetworksResource", "AsyncNetworksResource"]


class NetworksResource(SyncAPIResource):
    @cached_property
    def routes(self) -> RoutesResource:
        return RoutesResource(self._client)

    @cached_property
    def virtual_networks(self) -> VirtualNetworksResource:
        return VirtualNetworksResource(self._client)

    @cached_property
    def with_raw_response(self) -> NetworksResourceWithRawResponse:
        return NetworksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NetworksResourceWithStreamingResponse:
        return NetworksResourceWithStreamingResponse(self)


class AsyncNetworksResource(AsyncAPIResource):
    @cached_property
    def routes(self) -> AsyncRoutesResource:
        return AsyncRoutesResource(self._client)

    @cached_property
    def virtual_networks(self) -> AsyncVirtualNetworksResource:
        return AsyncVirtualNetworksResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNetworksResourceWithRawResponse:
        return AsyncNetworksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNetworksResourceWithStreamingResponse:
        return AsyncNetworksResourceWithStreamingResponse(self)


class NetworksResourceWithRawResponse:
    def __init__(self, networks: NetworksResource) -> None:
        self._networks = networks

    @cached_property
    def routes(self) -> RoutesResourceWithRawResponse:
        return RoutesResourceWithRawResponse(self._networks.routes)

    @cached_property
    def virtual_networks(self) -> VirtualNetworksResourceWithRawResponse:
        return VirtualNetworksResourceWithRawResponse(self._networks.virtual_networks)


class AsyncNetworksResourceWithRawResponse:
    def __init__(self, networks: AsyncNetworksResource) -> None:
        self._networks = networks

    @cached_property
    def routes(self) -> AsyncRoutesResourceWithRawResponse:
        return AsyncRoutesResourceWithRawResponse(self._networks.routes)

    @cached_property
    def virtual_networks(self) -> AsyncVirtualNetworksResourceWithRawResponse:
        return AsyncVirtualNetworksResourceWithRawResponse(self._networks.virtual_networks)


class NetworksResourceWithStreamingResponse:
    def __init__(self, networks: NetworksResource) -> None:
        self._networks = networks

    @cached_property
    def routes(self) -> RoutesResourceWithStreamingResponse:
        return RoutesResourceWithStreamingResponse(self._networks.routes)

    @cached_property
    def virtual_networks(self) -> VirtualNetworksResourceWithStreamingResponse:
        return VirtualNetworksResourceWithStreamingResponse(self._networks.virtual_networks)


class AsyncNetworksResourceWithStreamingResponse:
    def __init__(self, networks: AsyncNetworksResource) -> None:
        self._networks = networks

    @cached_property
    def routes(self) -> AsyncRoutesResourceWithStreamingResponse:
        return AsyncRoutesResourceWithStreamingResponse(self._networks.routes)

    @cached_property
    def virtual_networks(self) -> AsyncVirtualNetworksResourceWithStreamingResponse:
        return AsyncVirtualNetworksResourceWithStreamingResponse(self._networks.virtual_networks)
