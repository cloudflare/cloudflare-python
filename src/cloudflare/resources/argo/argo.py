# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .smart_routing import (
    SmartRouting,
    AsyncSmartRouting,
    SmartRoutingWithRawResponse,
    AsyncSmartRoutingWithRawResponse,
    SmartRoutingWithStreamingResponse,
    AsyncSmartRoutingWithStreamingResponse,
)
from .tiered_caching import (
    TieredCaching,
    AsyncTieredCaching,
    TieredCachingWithRawResponse,
    AsyncTieredCachingWithRawResponse,
    TieredCachingWithStreamingResponse,
    AsyncTieredCachingWithStreamingResponse,
)

__all__ = ["Argo", "AsyncArgo"]


class Argo(SyncAPIResource):
    @cached_property
    def smart_routing(self) -> SmartRouting:
        return SmartRouting(self._client)

    @cached_property
    def tiered_caching(self) -> TieredCaching:
        return TieredCaching(self._client)

    @cached_property
    def with_raw_response(self) -> ArgoWithRawResponse:
        return ArgoWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ArgoWithStreamingResponse:
        return ArgoWithStreamingResponse(self)


class AsyncArgo(AsyncAPIResource):
    @cached_property
    def smart_routing(self) -> AsyncSmartRouting:
        return AsyncSmartRouting(self._client)

    @cached_property
    def tiered_caching(self) -> AsyncTieredCaching:
        return AsyncTieredCaching(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncArgoWithRawResponse:
        return AsyncArgoWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncArgoWithStreamingResponse:
        return AsyncArgoWithStreamingResponse(self)


class ArgoWithRawResponse:
    def __init__(self, argo: Argo) -> None:
        self._argo = argo

    @cached_property
    def smart_routing(self) -> SmartRoutingWithRawResponse:
        return SmartRoutingWithRawResponse(self._argo.smart_routing)

    @cached_property
    def tiered_caching(self) -> TieredCachingWithRawResponse:
        return TieredCachingWithRawResponse(self._argo.tiered_caching)


class AsyncArgoWithRawResponse:
    def __init__(self, argo: AsyncArgo) -> None:
        self._argo = argo

    @cached_property
    def smart_routing(self) -> AsyncSmartRoutingWithRawResponse:
        return AsyncSmartRoutingWithRawResponse(self._argo.smart_routing)

    @cached_property
    def tiered_caching(self) -> AsyncTieredCachingWithRawResponse:
        return AsyncTieredCachingWithRawResponse(self._argo.tiered_caching)


class ArgoWithStreamingResponse:
    def __init__(self, argo: Argo) -> None:
        self._argo = argo

    @cached_property
    def smart_routing(self) -> SmartRoutingWithStreamingResponse:
        return SmartRoutingWithStreamingResponse(self._argo.smart_routing)

    @cached_property
    def tiered_caching(self) -> TieredCachingWithStreamingResponse:
        return TieredCachingWithStreamingResponse(self._argo.tiered_caching)


class AsyncArgoWithStreamingResponse:
    def __init__(self, argo: AsyncArgo) -> None:
        self._argo = argo

    @cached_property
    def smart_routing(self) -> AsyncSmartRoutingWithStreamingResponse:
        return AsyncSmartRoutingWithStreamingResponse(self._argo.smart_routing)

    @cached_property
    def tiered_caching(self) -> AsyncTieredCachingWithStreamingResponse:
        return AsyncTieredCachingWithStreamingResponse(self._argo.tiered_caching)
