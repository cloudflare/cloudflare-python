# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .events import (
    Events,
    AsyncEvents,
    EventsWithRawResponse,
    AsyncEventsWithRawResponse,
    EventsWithStreamingResponse,
    AsyncEventsWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["LoadBalancingAnalytics", "AsyncLoadBalancingAnalytics"]


class LoadBalancingAnalytics(SyncAPIResource):
    @cached_property
    def events(self) -> Events:
        return Events(self._client)

    @cached_property
    def with_raw_response(self) -> LoadBalancingAnalyticsWithRawResponse:
        return LoadBalancingAnalyticsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LoadBalancingAnalyticsWithStreamingResponse:
        return LoadBalancingAnalyticsWithStreamingResponse(self)


class AsyncLoadBalancingAnalytics(AsyncAPIResource):
    @cached_property
    def events(self) -> AsyncEvents:
        return AsyncEvents(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLoadBalancingAnalyticsWithRawResponse:
        return AsyncLoadBalancingAnalyticsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLoadBalancingAnalyticsWithStreamingResponse:
        return AsyncLoadBalancingAnalyticsWithStreamingResponse(self)


class LoadBalancingAnalyticsWithRawResponse:
    def __init__(self, load_balancing_analytics: LoadBalancingAnalytics) -> None:
        self._load_balancing_analytics = load_balancing_analytics

    @cached_property
    def events(self) -> EventsWithRawResponse:
        return EventsWithRawResponse(self._load_balancing_analytics.events)


class AsyncLoadBalancingAnalyticsWithRawResponse:
    def __init__(self, load_balancing_analytics: AsyncLoadBalancingAnalytics) -> None:
        self._load_balancing_analytics = load_balancing_analytics

    @cached_property
    def events(self) -> AsyncEventsWithRawResponse:
        return AsyncEventsWithRawResponse(self._load_balancing_analytics.events)


class LoadBalancingAnalyticsWithStreamingResponse:
    def __init__(self, load_balancing_analytics: LoadBalancingAnalytics) -> None:
        self._load_balancing_analytics = load_balancing_analytics

    @cached_property
    def events(self) -> EventsWithStreamingResponse:
        return EventsWithStreamingResponse(self._load_balancing_analytics.events)


class AsyncLoadBalancingAnalyticsWithStreamingResponse:
    def __init__(self, load_balancing_analytics: AsyncLoadBalancingAnalytics) -> None:
        self._load_balancing_analytics = load_balancing_analytics

    @cached_property
    def events(self) -> AsyncEventsWithStreamingResponse:
        return AsyncEventsWithStreamingResponse(self._load_balancing_analytics.events)
