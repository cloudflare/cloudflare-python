# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .pools import (
    Pools,
    AsyncPools,
    PoolsWithRawResponse,
    AsyncPoolsWithRawResponse,
    PoolsWithStreamingResponse,
    AsyncPoolsWithStreamingResponse,
)
from .preview import (
    Preview,
    AsyncPreview,
    PreviewWithRawResponse,
    AsyncPreviewWithRawResponse,
    PreviewWithStreamingResponse,
    AsyncPreviewWithStreamingResponse,
)
from .monitors import (
    Monitors,
    AsyncMonitors,
    MonitorsWithRawResponse,
    AsyncMonitorsWithRawResponse,
    MonitorsWithStreamingResponse,
    AsyncMonitorsWithStreamingResponse,
)
from .analytics import (
    Analytics,
    AsyncAnalytics,
    AnalyticsWithRawResponse,
    AsyncAnalyticsWithRawResponse,
    AnalyticsWithStreamingResponse,
    AsyncAnalyticsWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .analytics.analytics import Analytics, AsyncAnalytics

__all__ = ["LoadBalancing", "AsyncLoadBalancing"]


class LoadBalancing(SyncAPIResource):
    @cached_property
    def monitors(self) -> Monitors:
        return Monitors(self._client)

    @cached_property
    def pools(self) -> Pools:
        return Pools(self._client)

    @cached_property
    def preview(self) -> Preview:
        return Preview(self._client)

    @cached_property
    def analytics(self) -> Analytics:
        return Analytics(self._client)

    @cached_property
    def with_raw_response(self) -> LoadBalancingWithRawResponse:
        return LoadBalancingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LoadBalancingWithStreamingResponse:
        return LoadBalancingWithStreamingResponse(self)


class AsyncLoadBalancing(AsyncAPIResource):
    @cached_property
    def monitors(self) -> AsyncMonitors:
        return AsyncMonitors(self._client)

    @cached_property
    def pools(self) -> AsyncPools:
        return AsyncPools(self._client)

    @cached_property
    def preview(self) -> AsyncPreview:
        return AsyncPreview(self._client)

    @cached_property
    def analytics(self) -> AsyncAnalytics:
        return AsyncAnalytics(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLoadBalancingWithRawResponse:
        return AsyncLoadBalancingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLoadBalancingWithStreamingResponse:
        return AsyncLoadBalancingWithStreamingResponse(self)


class LoadBalancingWithRawResponse:
    def __init__(self, load_balancing: LoadBalancing) -> None:
        self._load_balancing = load_balancing

    @cached_property
    def monitors(self) -> MonitorsWithRawResponse:
        return MonitorsWithRawResponse(self._load_balancing.monitors)

    @cached_property
    def pools(self) -> PoolsWithRawResponse:
        return PoolsWithRawResponse(self._load_balancing.pools)

    @cached_property
    def preview(self) -> PreviewWithRawResponse:
        return PreviewWithRawResponse(self._load_balancing.preview)

    @cached_property
    def analytics(self) -> AnalyticsWithRawResponse:
        return AnalyticsWithRawResponse(self._load_balancing.analytics)


class AsyncLoadBalancingWithRawResponse:
    def __init__(self, load_balancing: AsyncLoadBalancing) -> None:
        self._load_balancing = load_balancing

    @cached_property
    def monitors(self) -> AsyncMonitorsWithRawResponse:
        return AsyncMonitorsWithRawResponse(self._load_balancing.monitors)

    @cached_property
    def pools(self) -> AsyncPoolsWithRawResponse:
        return AsyncPoolsWithRawResponse(self._load_balancing.pools)

    @cached_property
    def preview(self) -> AsyncPreviewWithRawResponse:
        return AsyncPreviewWithRawResponse(self._load_balancing.preview)

    @cached_property
    def analytics(self) -> AsyncAnalyticsWithRawResponse:
        return AsyncAnalyticsWithRawResponse(self._load_balancing.analytics)


class LoadBalancingWithStreamingResponse:
    def __init__(self, load_balancing: LoadBalancing) -> None:
        self._load_balancing = load_balancing

    @cached_property
    def monitors(self) -> MonitorsWithStreamingResponse:
        return MonitorsWithStreamingResponse(self._load_balancing.monitors)

    @cached_property
    def pools(self) -> PoolsWithStreamingResponse:
        return PoolsWithStreamingResponse(self._load_balancing.pools)

    @cached_property
    def preview(self) -> PreviewWithStreamingResponse:
        return PreviewWithStreamingResponse(self._load_balancing.preview)

    @cached_property
    def analytics(self) -> AnalyticsWithStreamingResponse:
        return AnalyticsWithStreamingResponse(self._load_balancing.analytics)


class AsyncLoadBalancingWithStreamingResponse:
    def __init__(self, load_balancing: AsyncLoadBalancing) -> None:
        self._load_balancing = load_balancing

    @cached_property
    def monitors(self) -> AsyncMonitorsWithStreamingResponse:
        return AsyncMonitorsWithStreamingResponse(self._load_balancing.monitors)

    @cached_property
    def pools(self) -> AsyncPoolsWithStreamingResponse:
        return AsyncPoolsWithStreamingResponse(self._load_balancing.pools)

    @cached_property
    def preview(self) -> AsyncPreviewWithStreamingResponse:
        return AsyncPreviewWithStreamingResponse(self._load_balancing.preview)

    @cached_property
    def analytics(self) -> AsyncAnalyticsWithStreamingResponse:
        return AsyncAnalyticsWithStreamingResponse(self._load_balancing.analytics)
