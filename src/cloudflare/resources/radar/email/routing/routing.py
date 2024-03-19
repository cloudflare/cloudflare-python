# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .summary import (
    Summary,
    AsyncSummary,
    SummaryWithRawResponse,
    AsyncSummaryWithRawResponse,
    SummaryWithStreamingResponse,
    AsyncSummaryWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from .timeseries_groups import (
    TimeseriesGroups,
    AsyncTimeseriesGroups,
    TimeseriesGroupsWithRawResponse,
    AsyncTimeseriesGroupsWithRawResponse,
    TimeseriesGroupsWithStreamingResponse,
    AsyncTimeseriesGroupsWithStreamingResponse,
)

__all__ = ["Routing", "AsyncRouting"]


class Routing(SyncAPIResource):
    @cached_property
    def summary(self) -> Summary:
        return Summary(self._client)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroups:
        return TimeseriesGroups(self._client)

    @cached_property
    def with_raw_response(self) -> RoutingWithRawResponse:
        return RoutingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoutingWithStreamingResponse:
        return RoutingWithStreamingResponse(self)


class AsyncRouting(AsyncAPIResource):
    @cached_property
    def summary(self) -> AsyncSummary:
        return AsyncSummary(self._client)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroups:
        return AsyncTimeseriesGroups(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRoutingWithRawResponse:
        return AsyncRoutingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoutingWithStreamingResponse:
        return AsyncRoutingWithStreamingResponse(self)


class RoutingWithRawResponse:
    def __init__(self, routing: Routing) -> None:
        self._routing = routing

    @cached_property
    def summary(self) -> SummaryWithRawResponse:
        return SummaryWithRawResponse(self._routing.summary)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsWithRawResponse:
        return TimeseriesGroupsWithRawResponse(self._routing.timeseries_groups)


class AsyncRoutingWithRawResponse:
    def __init__(self, routing: AsyncRouting) -> None:
        self._routing = routing

    @cached_property
    def summary(self) -> AsyncSummaryWithRawResponse:
        return AsyncSummaryWithRawResponse(self._routing.summary)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsWithRawResponse:
        return AsyncTimeseriesGroupsWithRawResponse(self._routing.timeseries_groups)


class RoutingWithStreamingResponse:
    def __init__(self, routing: Routing) -> None:
        self._routing = routing

    @cached_property
    def summary(self) -> SummaryWithStreamingResponse:
        return SummaryWithStreamingResponse(self._routing.summary)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsWithStreamingResponse:
        return TimeseriesGroupsWithStreamingResponse(self._routing.timeseries_groups)


class AsyncRoutingWithStreamingResponse:
    def __init__(self, routing: AsyncRouting) -> None:
        self._routing = routing

    @cached_property
    def summary(self) -> AsyncSummaryWithStreamingResponse:
        return AsyncSummaryWithStreamingResponse(self._routing.summary)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsWithStreamingResponse:
        return AsyncTimeseriesGroupsWithStreamingResponse(self._routing.timeseries_groups)
