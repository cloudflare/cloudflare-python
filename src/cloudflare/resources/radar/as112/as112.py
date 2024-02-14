# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .timeseries_groups import (
    TimeseriesGroups,
    AsyncTimeseriesGroups,
    TimeseriesGroupsWithRawResponse,
    AsyncTimeseriesGroupsWithRawResponse,
    TimeseriesGroupsWithStreamingResponse,
    AsyncTimeseriesGroupsWithStreamingResponse,
)
from .timeseries_groups.timeseries_groups import TimeseriesGroups, AsyncTimeseriesGroups

__all__ = ["As112", "AsyncAs112"]


class As112(SyncAPIResource):
    @cached_property
    def timeseries_groups(self) -> TimeseriesGroups:
        return TimeseriesGroups(self._client)

    @cached_property
    def with_raw_response(self) -> As112WithRawResponse:
        return As112WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> As112WithStreamingResponse:
        return As112WithStreamingResponse(self)


class AsyncAs112(AsyncAPIResource):
    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroups:
        return AsyncTimeseriesGroups(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAs112WithRawResponse:
        return AsyncAs112WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAs112WithStreamingResponse:
        return AsyncAs112WithStreamingResponse(self)


class As112WithRawResponse:
    def __init__(self, as112: As112) -> None:
        self._as112 = as112

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsWithRawResponse:
        return TimeseriesGroupsWithRawResponse(self._as112.timeseries_groups)


class AsyncAs112WithRawResponse:
    def __init__(self, as112: AsyncAs112) -> None:
        self._as112 = as112

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsWithRawResponse:
        return AsyncTimeseriesGroupsWithRawResponse(self._as112.timeseries_groups)


class As112WithStreamingResponse:
    def __init__(self, as112: As112) -> None:
        self._as112 = as112

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsWithStreamingResponse:
        return TimeseriesGroupsWithStreamingResponse(self._as112.timeseries_groups)


class AsyncAs112WithStreamingResponse:
    def __init__(self, as112: AsyncAs112) -> None:
        self._as112 = as112

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsWithStreamingResponse:
        return AsyncTimeseriesGroupsWithStreamingResponse(self._as112.timeseries_groups)
