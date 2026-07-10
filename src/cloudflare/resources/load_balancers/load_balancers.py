# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .regions import (
    RegionsResource,
    AsyncRegionsResource,
    RegionsResourceWithRawResponse,
    AsyncRegionsResourceWithRawResponse,
    RegionsResourceWithStreamingResponse,
    AsyncRegionsResourceWithStreamingResponse,
)
from .previews import (
    PreviewsResource,
    AsyncPreviewsResource,
    PreviewsResourceWithRawResponse,
    AsyncPreviewsResourceWithRawResponse,
    PreviewsResourceWithStreamingResponse,
    AsyncPreviewsResourceWithStreamingResponse,
)
from .searches import (
    SearchesResource,
    AsyncSearchesResource,
    SearchesResourceWithRawResponse,
    AsyncSearchesResourceWithRawResponse,
    SearchesResourceWithStreamingResponse,
    AsyncSearchesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .pools.pools import (
    PoolsResource,
    AsyncPoolsResource,
    PoolsResourceWithRawResponse,
    AsyncPoolsResourceWithRawResponse,
    PoolsResourceWithStreamingResponse,
    AsyncPoolsResourceWithStreamingResponse,
)
from .monitors.monitors import (
    MonitorsResource,
    AsyncMonitorsResource,
    MonitorsResourceWithRawResponse,
    AsyncMonitorsResourceWithRawResponse,
    MonitorsResourceWithStreamingResponse,
    AsyncMonitorsResourceWithStreamingResponse,
)
from .monitor_groups.monitor_groups import (
    MonitorGroupsResource,
    AsyncMonitorGroupsResource,
    MonitorGroupsResourceWithRawResponse,
    AsyncMonitorGroupsResourceWithRawResponse,
    MonitorGroupsResourceWithStreamingResponse,
    AsyncMonitorGroupsResourceWithStreamingResponse,
)

__all__ = ["LoadBalancersResource", "AsyncLoadBalancersResource"]


class LoadBalancersResource(SyncAPIResource):
    @cached_property
    def monitors(self) -> MonitorsResource:
        return MonitorsResource(self._client)

    @cached_property
    def monitor_groups(self) -> MonitorGroupsResource:
        return MonitorGroupsResource(self._client)

    @cached_property
    def pools(self) -> PoolsResource:
        return PoolsResource(self._client)

    @cached_property
    def previews(self) -> PreviewsResource:
        return PreviewsResource(self._client)

    @cached_property
    def regions(self) -> RegionsResource:
        return RegionsResource(self._client)

    @cached_property
    def searches(self) -> SearchesResource:
        return SearchesResource(self._client)

    @cached_property
    def with_raw_response(self) -> LoadBalancersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return LoadBalancersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LoadBalancersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return LoadBalancersResourceWithStreamingResponse(self)


class AsyncLoadBalancersResource(AsyncAPIResource):
    @cached_property
    def monitors(self) -> AsyncMonitorsResource:
        return AsyncMonitorsResource(self._client)

    @cached_property
    def monitor_groups(self) -> AsyncMonitorGroupsResource:
        return AsyncMonitorGroupsResource(self._client)

    @cached_property
    def pools(self) -> AsyncPoolsResource:
        return AsyncPoolsResource(self._client)

    @cached_property
    def previews(self) -> AsyncPreviewsResource:
        return AsyncPreviewsResource(self._client)

    @cached_property
    def regions(self) -> AsyncRegionsResource:
        return AsyncRegionsResource(self._client)

    @cached_property
    def searches(self) -> AsyncSearchesResource:
        return AsyncSearchesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLoadBalancersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLoadBalancersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLoadBalancersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncLoadBalancersResourceWithStreamingResponse(self)


class LoadBalancersResourceWithRawResponse:
    def __init__(self, load_balancers: LoadBalancersResource) -> None:
        self._load_balancers = load_balancers

    @cached_property
    def monitors(self) -> MonitorsResourceWithRawResponse:
        return MonitorsResourceWithRawResponse(self._load_balancers.monitors)

    @cached_property
    def monitor_groups(self) -> MonitorGroupsResourceWithRawResponse:
        return MonitorGroupsResourceWithRawResponse(self._load_balancers.monitor_groups)

    @cached_property
    def pools(self) -> PoolsResourceWithRawResponse:
        return PoolsResourceWithRawResponse(self._load_balancers.pools)

    @cached_property
    def previews(self) -> PreviewsResourceWithRawResponse:
        return PreviewsResourceWithRawResponse(self._load_balancers.previews)

    @cached_property
    def regions(self) -> RegionsResourceWithRawResponse:
        return RegionsResourceWithRawResponse(self._load_balancers.regions)

    @cached_property
    def searches(self) -> SearchesResourceWithRawResponse:
        return SearchesResourceWithRawResponse(self._load_balancers.searches)


class AsyncLoadBalancersResourceWithRawResponse:
    def __init__(self, load_balancers: AsyncLoadBalancersResource) -> None:
        self._load_balancers = load_balancers

    @cached_property
    def monitors(self) -> AsyncMonitorsResourceWithRawResponse:
        return AsyncMonitorsResourceWithRawResponse(self._load_balancers.monitors)

    @cached_property
    def monitor_groups(self) -> AsyncMonitorGroupsResourceWithRawResponse:
        return AsyncMonitorGroupsResourceWithRawResponse(self._load_balancers.monitor_groups)

    @cached_property
    def pools(self) -> AsyncPoolsResourceWithRawResponse:
        return AsyncPoolsResourceWithRawResponse(self._load_balancers.pools)

    @cached_property
    def previews(self) -> AsyncPreviewsResourceWithRawResponse:
        return AsyncPreviewsResourceWithRawResponse(self._load_balancers.previews)

    @cached_property
    def regions(self) -> AsyncRegionsResourceWithRawResponse:
        return AsyncRegionsResourceWithRawResponse(self._load_balancers.regions)

    @cached_property
    def searches(self) -> AsyncSearchesResourceWithRawResponse:
        return AsyncSearchesResourceWithRawResponse(self._load_balancers.searches)


class LoadBalancersResourceWithStreamingResponse:
    def __init__(self, load_balancers: LoadBalancersResource) -> None:
        self._load_balancers = load_balancers

    @cached_property
    def monitors(self) -> MonitorsResourceWithStreamingResponse:
        return MonitorsResourceWithStreamingResponse(self._load_balancers.monitors)

    @cached_property
    def monitor_groups(self) -> MonitorGroupsResourceWithStreamingResponse:
        return MonitorGroupsResourceWithStreamingResponse(self._load_balancers.monitor_groups)

    @cached_property
    def pools(self) -> PoolsResourceWithStreamingResponse:
        return PoolsResourceWithStreamingResponse(self._load_balancers.pools)

    @cached_property
    def previews(self) -> PreviewsResourceWithStreamingResponse:
        return PreviewsResourceWithStreamingResponse(self._load_balancers.previews)

    @cached_property
    def regions(self) -> RegionsResourceWithStreamingResponse:
        return RegionsResourceWithStreamingResponse(self._load_balancers.regions)

    @cached_property
    def searches(self) -> SearchesResourceWithStreamingResponse:
        return SearchesResourceWithStreamingResponse(self._load_balancers.searches)


class AsyncLoadBalancersResourceWithStreamingResponse:
    def __init__(self, load_balancers: AsyncLoadBalancersResource) -> None:
        self._load_balancers = load_balancers

    @cached_property
    def monitors(self) -> AsyncMonitorsResourceWithStreamingResponse:
        return AsyncMonitorsResourceWithStreamingResponse(self._load_balancers.monitors)

    @cached_property
    def monitor_groups(self) -> AsyncMonitorGroupsResourceWithStreamingResponse:
        return AsyncMonitorGroupsResourceWithStreamingResponse(self._load_balancers.monitor_groups)

    @cached_property
    def pools(self) -> AsyncPoolsResourceWithStreamingResponse:
        return AsyncPoolsResourceWithStreamingResponse(self._load_balancers.pools)

    @cached_property
    def previews(self) -> AsyncPreviewsResourceWithStreamingResponse:
        return AsyncPreviewsResourceWithStreamingResponse(self._load_balancers.previews)

    @cached_property
    def regions(self) -> AsyncRegionsResourceWithStreamingResponse:
        return AsyncRegionsResourceWithStreamingResponse(self._load_balancers.regions)

    @cached_property
    def searches(self) -> AsyncSearchesResourceWithStreamingResponse:
        return AsyncSearchesResourceWithStreamingResponse(self._load_balancers.searches)
