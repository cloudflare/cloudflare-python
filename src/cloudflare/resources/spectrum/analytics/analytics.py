# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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
from .aggregates import (
    Aggregates,
    AsyncAggregates,
    AggregatesWithRawResponse,
    AsyncAggregatesWithRawResponse,
    AggregatesWithStreamingResponse,
    AsyncAggregatesWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from .events.events import Events, AsyncEvents
from .aggregates.aggregates import Aggregates, AsyncAggregates

__all__ = ["Analytics", "AsyncAnalytics"]


class Analytics(SyncAPIResource):
    @cached_property
    def aggregates(self) -> Aggregates:
        return Aggregates(self._client)

    @cached_property
    def events(self) -> Events:
        return Events(self._client)

    @cached_property
    def with_raw_response(self) -> AnalyticsWithRawResponse:
        return AnalyticsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalyticsWithStreamingResponse:
        return AnalyticsWithStreamingResponse(self)


class AsyncAnalytics(AsyncAPIResource):
    @cached_property
    def aggregates(self) -> AsyncAggregates:
        return AsyncAggregates(self._client)

    @cached_property
    def events(self) -> AsyncEvents:
        return AsyncEvents(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAnalyticsWithRawResponse:
        return AsyncAnalyticsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalyticsWithStreamingResponse:
        return AsyncAnalyticsWithStreamingResponse(self)


class AnalyticsWithRawResponse:
    def __init__(self, analytics: Analytics) -> None:
        self._analytics = analytics

    @cached_property
    def aggregates(self) -> AggregatesWithRawResponse:
        return AggregatesWithRawResponse(self._analytics.aggregates)

    @cached_property
    def events(self) -> EventsWithRawResponse:
        return EventsWithRawResponse(self._analytics.events)


class AsyncAnalyticsWithRawResponse:
    def __init__(self, analytics: AsyncAnalytics) -> None:
        self._analytics = analytics

    @cached_property
    def aggregates(self) -> AsyncAggregatesWithRawResponse:
        return AsyncAggregatesWithRawResponse(self._analytics.aggregates)

    @cached_property
    def events(self) -> AsyncEventsWithRawResponse:
        return AsyncEventsWithRawResponse(self._analytics.events)


class AnalyticsWithStreamingResponse:
    def __init__(self, analytics: Analytics) -> None:
        self._analytics = analytics

    @cached_property
    def aggregates(self) -> AggregatesWithStreamingResponse:
        return AggregatesWithStreamingResponse(self._analytics.aggregates)

    @cached_property
    def events(self) -> EventsWithStreamingResponse:
        return EventsWithStreamingResponse(self._analytics.events)


class AsyncAnalyticsWithStreamingResponse:
    def __init__(self, analytics: AsyncAnalytics) -> None:
        self._analytics = analytics

    @cached_property
    def aggregates(self) -> AsyncAggregatesWithStreamingResponse:
        return AsyncAggregatesWithStreamingResponse(self._analytics.aggregates)

    @cached_property
    def events(self) -> AsyncEventsWithStreamingResponse:
        return AsyncEventsWithStreamingResponse(self._analytics.events)
