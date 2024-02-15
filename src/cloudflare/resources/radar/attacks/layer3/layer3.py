# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .top import (
    Top,
    AsyncTop,
    TopWithRawResponse,
    AsyncTopWithRawResponse,
    TopWithStreamingResponse,
    AsyncTopWithStreamingResponse,
)
from .top.top import Top, AsyncTop
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
from .timeseries_groups.timeseries_groups import TimeseriesGroups, AsyncTimeseriesGroups

__all__ = ["Layer3", "AsyncLayer3"]


class Layer3(SyncAPIResource):
    @cached_property
    def timeseries_groups(self) -> TimeseriesGroups:
        return TimeseriesGroups(self._client)

    @cached_property
    def top(self) -> Top:
        return Top(self._client)

    @cached_property
    def with_raw_response(self) -> Layer3WithRawResponse:
        return Layer3WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> Layer3WithStreamingResponse:
        return Layer3WithStreamingResponse(self)


class AsyncLayer3(AsyncAPIResource):
    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroups:
        return AsyncTimeseriesGroups(self._client)

    @cached_property
    def top(self) -> AsyncTop:
        return AsyncTop(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLayer3WithRawResponse:
        return AsyncLayer3WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLayer3WithStreamingResponse:
        return AsyncLayer3WithStreamingResponse(self)


class Layer3WithRawResponse:
    def __init__(self, layer3: Layer3) -> None:
        self._layer3 = layer3

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsWithRawResponse:
        return TimeseriesGroupsWithRawResponse(self._layer3.timeseries_groups)

    @cached_property
    def top(self) -> TopWithRawResponse:
        return TopWithRawResponse(self._layer3.top)


class AsyncLayer3WithRawResponse:
    def __init__(self, layer3: AsyncLayer3) -> None:
        self._layer3 = layer3

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsWithRawResponse:
        return AsyncTimeseriesGroupsWithRawResponse(self._layer3.timeseries_groups)

    @cached_property
    def top(self) -> AsyncTopWithRawResponse:
        return AsyncTopWithRawResponse(self._layer3.top)


class Layer3WithStreamingResponse:
    def __init__(self, layer3: Layer3) -> None:
        self._layer3 = layer3

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsWithStreamingResponse:
        return TimeseriesGroupsWithStreamingResponse(self._layer3.timeseries_groups)

    @cached_property
    def top(self) -> TopWithStreamingResponse:
        return TopWithStreamingResponse(self._layer3.top)


class AsyncLayer3WithStreamingResponse:
    def __init__(self, layer3: AsyncLayer3) -> None:
        self._layer3 = layer3

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsWithStreamingResponse:
        return AsyncTimeseriesGroupsWithStreamingResponse(self._layer3.timeseries_groups)

    @cached_property
    def top(self) -> AsyncTopWithStreamingResponse:
        return AsyncTopWithStreamingResponse(self._layer3.top)
