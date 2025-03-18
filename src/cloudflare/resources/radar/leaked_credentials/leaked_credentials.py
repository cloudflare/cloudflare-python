# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .summary import (
    SummaryResource,
    AsyncSummaryResource,
    SummaryResourceWithRawResponse,
    AsyncSummaryResourceWithRawResponse,
    SummaryResourceWithStreamingResponse,
    AsyncSummaryResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .timeseries_groups import (
    TimeseriesGroupsResource,
    AsyncTimeseriesGroupsResource,
    TimeseriesGroupsResourceWithRawResponse,
    AsyncTimeseriesGroupsResourceWithRawResponse,
    TimeseriesGroupsResourceWithStreamingResponse,
    AsyncTimeseriesGroupsResourceWithStreamingResponse,
)

__all__ = ["LeakedCredentialsResource", "AsyncLeakedCredentialsResource"]


class LeakedCredentialsResource(SyncAPIResource):
    @cached_property
    def summary(self) -> SummaryResource:
        return SummaryResource(self._client)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResource:
        return TimeseriesGroupsResource(self._client)

    @cached_property
    def with_raw_response(self) -> LeakedCredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return LeakedCredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LeakedCredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return LeakedCredentialsResourceWithStreamingResponse(self)


class AsyncLeakedCredentialsResource(AsyncAPIResource):
    @cached_property
    def summary(self) -> AsyncSummaryResource:
        return AsyncSummaryResource(self._client)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResource:
        return AsyncTimeseriesGroupsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLeakedCredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLeakedCredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLeakedCredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncLeakedCredentialsResourceWithStreamingResponse(self)


class LeakedCredentialsResourceWithRawResponse:
    def __init__(self, leaked_credentials: LeakedCredentialsResource) -> None:
        self._leaked_credentials = leaked_credentials

    @cached_property
    def summary(self) -> SummaryResourceWithRawResponse:
        return SummaryResourceWithRawResponse(self._leaked_credentials.summary)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResourceWithRawResponse:
        return TimeseriesGroupsResourceWithRawResponse(self._leaked_credentials.timeseries_groups)


class AsyncLeakedCredentialsResourceWithRawResponse:
    def __init__(self, leaked_credentials: AsyncLeakedCredentialsResource) -> None:
        self._leaked_credentials = leaked_credentials

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithRawResponse:
        return AsyncSummaryResourceWithRawResponse(self._leaked_credentials.summary)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResourceWithRawResponse:
        return AsyncTimeseriesGroupsResourceWithRawResponse(self._leaked_credentials.timeseries_groups)


class LeakedCredentialsResourceWithStreamingResponse:
    def __init__(self, leaked_credentials: LeakedCredentialsResource) -> None:
        self._leaked_credentials = leaked_credentials

    @cached_property
    def summary(self) -> SummaryResourceWithStreamingResponse:
        return SummaryResourceWithStreamingResponse(self._leaked_credentials.summary)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResourceWithStreamingResponse:
        return TimeseriesGroupsResourceWithStreamingResponse(self._leaked_credentials.timeseries_groups)


class AsyncLeakedCredentialsResourceWithStreamingResponse:
    def __init__(self, leaked_credentials: AsyncLeakedCredentialsResource) -> None:
        self._leaked_credentials = leaked_credentials

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithStreamingResponse:
        return AsyncSummaryResourceWithStreamingResponse(self._leaked_credentials.summary)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResourceWithStreamingResponse:
        return AsyncTimeseriesGroupsResourceWithStreamingResponse(self._leaked_credentials.timeseries_groups)
