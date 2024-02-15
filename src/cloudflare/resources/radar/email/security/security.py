# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .summaries import (
    Summaries,
    AsyncSummaries,
    SummariesWithRawResponse,
    AsyncSummariesWithRawResponse,
    SummariesWithStreamingResponse,
    AsyncSummariesWithStreamingResponse,
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
from .summaries.summaries import Summaries, AsyncSummaries
from .timeseries_groups.timeseries_groups import TimeseriesGroups, AsyncTimeseriesGroups

__all__ = ["Security", "AsyncSecurity"]


class Security(SyncAPIResource):
    @cached_property
    def summaries(self) -> Summaries:
        return Summaries(self._client)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroups:
        return TimeseriesGroups(self._client)

    @cached_property
    def with_raw_response(self) -> SecurityWithRawResponse:
        return SecurityWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecurityWithStreamingResponse:
        return SecurityWithStreamingResponse(self)


class AsyncSecurity(AsyncAPIResource):
    @cached_property
    def summaries(self) -> AsyncSummaries:
        return AsyncSummaries(self._client)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroups:
        return AsyncTimeseriesGroups(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSecurityWithRawResponse:
        return AsyncSecurityWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecurityWithStreamingResponse:
        return AsyncSecurityWithStreamingResponse(self)


class SecurityWithRawResponse:
    def __init__(self, security: Security) -> None:
        self._security = security

    @cached_property
    def summaries(self) -> SummariesWithRawResponse:
        return SummariesWithRawResponse(self._security.summaries)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsWithRawResponse:
        return TimeseriesGroupsWithRawResponse(self._security.timeseries_groups)


class AsyncSecurityWithRawResponse:
    def __init__(self, security: AsyncSecurity) -> None:
        self._security = security

    @cached_property
    def summaries(self) -> AsyncSummariesWithRawResponse:
        return AsyncSummariesWithRawResponse(self._security.summaries)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsWithRawResponse:
        return AsyncTimeseriesGroupsWithRawResponse(self._security.timeseries_groups)


class SecurityWithStreamingResponse:
    def __init__(self, security: Security) -> None:
        self._security = security

    @cached_property
    def summaries(self) -> SummariesWithStreamingResponse:
        return SummariesWithStreamingResponse(self._security.summaries)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsWithStreamingResponse:
        return TimeseriesGroupsWithStreamingResponse(self._security.timeseries_groups)


class AsyncSecurityWithStreamingResponse:
    def __init__(self, security: AsyncSecurity) -> None:
        self._security = security

    @cached_property
    def summaries(self) -> AsyncSummariesWithStreamingResponse:
        return AsyncSummariesWithStreamingResponse(self._security.summaries)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsWithStreamingResponse:
        return AsyncTimeseriesGroupsWithStreamingResponse(self._security.timeseries_groups)
