# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .smart_routing import (
    SmartRoutingResource,
    AsyncSmartRoutingResource,
    SmartRoutingResourceWithRawResponse,
    AsyncSmartRoutingResourceWithRawResponse,
    SmartRoutingResourceWithStreamingResponse,
    AsyncSmartRoutingResourceWithStreamingResponse,
)
from .tiered_caching import (
    TieredCachingResource,
    AsyncTieredCachingResource,
    TieredCachingResourceWithRawResponse,
    AsyncTieredCachingResourceWithRawResponse,
    TieredCachingResourceWithStreamingResponse,
    AsyncTieredCachingResourceWithStreamingResponse,
)

__all__ = ["ArgoResource", "AsyncArgoResource"]


class ArgoResource(SyncAPIResource):
    @cached_property
    def smart_routing(self) -> SmartRoutingResource:
        return SmartRoutingResource(self._client)

    @cached_property
    def tiered_caching(self) -> TieredCachingResource:
        return TieredCachingResource(self._client)

    @cached_property
    def with_raw_response(self) -> ArgoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ArgoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ArgoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ArgoResourceWithStreamingResponse(self)


class AsyncArgoResource(AsyncAPIResource):
    @cached_property
    def smart_routing(self) -> AsyncSmartRoutingResource:
        return AsyncSmartRoutingResource(self._client)

    @cached_property
    def tiered_caching(self) -> AsyncTieredCachingResource:
        return AsyncTieredCachingResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncArgoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncArgoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncArgoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncArgoResourceWithStreamingResponse(self)


class ArgoResourceWithRawResponse:
    def __init__(self, argo: ArgoResource) -> None:
        self._argo = argo

    @cached_property
    def smart_routing(self) -> SmartRoutingResourceWithRawResponse:
        return SmartRoutingResourceWithRawResponse(self._argo.smart_routing)

    @cached_property
    def tiered_caching(self) -> TieredCachingResourceWithRawResponse:
        return TieredCachingResourceWithRawResponse(self._argo.tiered_caching)


class AsyncArgoResourceWithRawResponse:
    def __init__(self, argo: AsyncArgoResource) -> None:
        self._argo = argo

    @cached_property
    def smart_routing(self) -> AsyncSmartRoutingResourceWithRawResponse:
        return AsyncSmartRoutingResourceWithRawResponse(self._argo.smart_routing)

    @cached_property
    def tiered_caching(self) -> AsyncTieredCachingResourceWithRawResponse:
        return AsyncTieredCachingResourceWithRawResponse(self._argo.tiered_caching)


class ArgoResourceWithStreamingResponse:
    def __init__(self, argo: ArgoResource) -> None:
        self._argo = argo

    @cached_property
    def smart_routing(self) -> SmartRoutingResourceWithStreamingResponse:
        return SmartRoutingResourceWithStreamingResponse(self._argo.smart_routing)

    @cached_property
    def tiered_caching(self) -> TieredCachingResourceWithStreamingResponse:
        return TieredCachingResourceWithStreamingResponse(self._argo.tiered_caching)


class AsyncArgoResourceWithStreamingResponse:
    def __init__(self, argo: AsyncArgoResource) -> None:
        self._argo = argo

    @cached_property
    def smart_routing(self) -> AsyncSmartRoutingResourceWithStreamingResponse:
        return AsyncSmartRoutingResourceWithStreamingResponse(self._argo.smart_routing)

    @cached_property
    def tiered_caching(self) -> AsyncTieredCachingResourceWithStreamingResponse:
        return AsyncTieredCachingResourceWithStreamingResponse(self._argo.tiered_caching)
