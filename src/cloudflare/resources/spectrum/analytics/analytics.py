# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .events.events import (
    EventsResource,
    AsyncEventsResource,
    EventsResourceWithRawResponse,
    AsyncEventsResourceWithRawResponse,
    EventsResourceWithStreamingResponse,
    AsyncEventsResourceWithStreamingResponse,
)
from .aggregates.aggregates import (
    AggregatesResource,
    AsyncAggregatesResource,
    AggregatesResourceWithRawResponse,
    AsyncAggregatesResourceWithRawResponse,
    AggregatesResourceWithStreamingResponse,
    AsyncAggregatesResourceWithStreamingResponse,
)

__all__ = ["AnalyticsResource", "AsyncAnalyticsResource"]


class AnalyticsResource(SyncAPIResource):
    @cached_property
    def aggregates(self) -> AggregatesResource:
        return AggregatesResource(self._client)

    @cached_property
    def events(self) -> EventsResource:
        return EventsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AnalyticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalyticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AnalyticsResourceWithStreamingResponse(self)


class AsyncAnalyticsResource(AsyncAPIResource):
    @cached_property
    def aggregates(self) -> AsyncAggregatesResource:
        return AsyncAggregatesResource(self._client)

    @cached_property
    def events(self) -> AsyncEventsResource:
        return AsyncEventsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAnalyticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalyticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAnalyticsResourceWithStreamingResponse(self)


class AnalyticsResourceWithRawResponse:
    def __init__(self, analytics: AnalyticsResource) -> None:
        self._analytics = analytics

    @cached_property
    def aggregates(self) -> AggregatesResourceWithRawResponse:
        return AggregatesResourceWithRawResponse(self._analytics.aggregates)

    @cached_property
    def events(self) -> EventsResourceWithRawResponse:
        return EventsResourceWithRawResponse(self._analytics.events)


class AsyncAnalyticsResourceWithRawResponse:
    def __init__(self, analytics: AsyncAnalyticsResource) -> None:
        self._analytics = analytics

    @cached_property
    def aggregates(self) -> AsyncAggregatesResourceWithRawResponse:
        return AsyncAggregatesResourceWithRawResponse(self._analytics.aggregates)

    @cached_property
    def events(self) -> AsyncEventsResourceWithRawResponse:
        return AsyncEventsResourceWithRawResponse(self._analytics.events)


class AnalyticsResourceWithStreamingResponse:
    def __init__(self, analytics: AnalyticsResource) -> None:
        self._analytics = analytics

    @cached_property
    def aggregates(self) -> AggregatesResourceWithStreamingResponse:
        return AggregatesResourceWithStreamingResponse(self._analytics.aggregates)

    @cached_property
    def events(self) -> EventsResourceWithStreamingResponse:
        return EventsResourceWithStreamingResponse(self._analytics.events)


class AsyncAnalyticsResourceWithStreamingResponse:
    def __init__(self, analytics: AsyncAnalyticsResource) -> None:
        self._analytics = analytics

    @cached_property
    def aggregates(self) -> AsyncAggregatesResourceWithStreamingResponse:
        return AsyncAggregatesResourceWithStreamingResponse(self._analytics.aggregates)

    @cached_property
    def events(self) -> AsyncEventsResourceWithStreamingResponse:
        return AsyncEventsResourceWithStreamingResponse(self._analytics.events)
