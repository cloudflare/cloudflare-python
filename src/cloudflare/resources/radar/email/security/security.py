# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .top import (
    TopResource,
    AsyncTopResource,
    TopResourceWithRawResponse,
    AsyncTopResourceWithRawResponse,
    TopResourceWithStreamingResponse,
    AsyncTopResourceWithStreamingResponse,
)
from .summary import (
    SummaryResource,
    AsyncSummaryResource,
    SummaryResourceWithRawResponse,
    AsyncSummaryResourceWithRawResponse,
    SummaryResourceWithStreamingResponse,
    AsyncSummaryResourceWithStreamingResponse,
)
from .top.top import TopResource, AsyncTopResource
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from .timeseries_groups import (
    TimeseriesGroupsResource,
    AsyncTimeseriesGroupsResource,
    TimeseriesGroupsResourceWithRawResponse,
    AsyncTimeseriesGroupsResourceWithRawResponse,
    TimeseriesGroupsResourceWithStreamingResponse,
    AsyncTimeseriesGroupsResourceWithStreamingResponse,
)

__all__ = ["SecurityResource", "AsyncSecurityResource"]


class SecurityResource(SyncAPIResource):
    @cached_property
    def top(self) -> TopResource:
        return TopResource(self._client)

    @cached_property
    def summary(self) -> SummaryResource:
        return SummaryResource(self._client)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResource:
        return TimeseriesGroupsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SecurityResourceWithRawResponse:
        return SecurityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecurityResourceWithStreamingResponse:
        return SecurityResourceWithStreamingResponse(self)


class AsyncSecurityResource(AsyncAPIResource):
    @cached_property
    def top(self) -> AsyncTopResource:
        return AsyncTopResource(self._client)

    @cached_property
    def summary(self) -> AsyncSummaryResource:
        return AsyncSummaryResource(self._client)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResource:
        return AsyncTimeseriesGroupsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSecurityResourceWithRawResponse:
        return AsyncSecurityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecurityResourceWithStreamingResponse:
        return AsyncSecurityResourceWithStreamingResponse(self)


class SecurityResourceWithRawResponse:
    def __init__(self, security: SecurityResource) -> None:
        self._security = security

    @cached_property
    def top(self) -> TopResourceWithRawResponse:
        return TopResourceWithRawResponse(self._security.top)

    @cached_property
    def summary(self) -> SummaryResourceWithRawResponse:
        return SummaryResourceWithRawResponse(self._security.summary)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResourceWithRawResponse:
        return TimeseriesGroupsResourceWithRawResponse(self._security.timeseries_groups)


class AsyncSecurityResourceWithRawResponse:
    def __init__(self, security: AsyncSecurityResource) -> None:
        self._security = security

    @cached_property
    def top(self) -> AsyncTopResourceWithRawResponse:
        return AsyncTopResourceWithRawResponse(self._security.top)

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithRawResponse:
        return AsyncSummaryResourceWithRawResponse(self._security.summary)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResourceWithRawResponse:
        return AsyncTimeseriesGroupsResourceWithRawResponse(self._security.timeseries_groups)


class SecurityResourceWithStreamingResponse:
    def __init__(self, security: SecurityResource) -> None:
        self._security = security

    @cached_property
    def top(self) -> TopResourceWithStreamingResponse:
        return TopResourceWithStreamingResponse(self._security.top)

    @cached_property
    def summary(self) -> SummaryResourceWithStreamingResponse:
        return SummaryResourceWithStreamingResponse(self._security.summary)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResourceWithStreamingResponse:
        return TimeseriesGroupsResourceWithStreamingResponse(self._security.timeseries_groups)


class AsyncSecurityResourceWithStreamingResponse:
    def __init__(self, security: AsyncSecurityResource) -> None:
        self._security = security

    @cached_property
    def top(self) -> AsyncTopResourceWithStreamingResponse:
        return AsyncTopResourceWithStreamingResponse(self._security.top)

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithStreamingResponse:
        return AsyncSummaryResourceWithStreamingResponse(self._security.summary)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResourceWithStreamingResponse:
        return AsyncTimeseriesGroupsResourceWithStreamingResponse(self._security.timeseries_groups)
