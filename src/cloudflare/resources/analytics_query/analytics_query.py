# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, Iterable, cast
from datetime import datetime

import httpx

from ...types import analytics_query_top_n_params, analytics_query_summary_params, analytics_query_timeseries_params
from ..._types import Body, Query, Headers, NotGiven, SequenceNotStr, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options
from .data_security.data_security import (
    DataSecurityResource,
    AsyncDataSecurityResource,
    DataSecurityResourceWithRawResponse,
    AsyncDataSecurityResourceWithRawResponse,
    DataSecurityResourceWithStreamingResponse,
    AsyncDataSecurityResourceWithStreamingResponse,
)
from ...types.analytics_query_top_n_response import AnalyticsQueryTopNResponse
from ...types.analytics_query_summary_response import AnalyticsQuerySummaryResponse
from ...types.analytics_query_timeseries_response import AnalyticsQueryTimeseriesResponse

__all__ = ["AnalyticsQueryResource", "AsyncAnalyticsQueryResource"]


class AnalyticsQueryResource(SyncAPIResource):
    @cached_property
    def data_security(self) -> DataSecurityResource:
        return DataSecurityResource(self._client)

    @cached_property
    def with_raw_response(self) -> AnalyticsQueryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AnalyticsQueryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalyticsQueryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AnalyticsQueryResourceWithStreamingResponse(self)

    def summary(
        self,
        dataset: str,
        *,
        account_id: str,
        filters: Iterable[analytics_query_summary_params.Filter],
        from_: Union[str, datetime],
        group_by: SequenceNotStr[str],
        stats: SequenceNotStr[str],
        to: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsQuerySummaryResponse:
        """Returns aggregate summary stats for a dataset.

        Includes current-period and
        previous-period totals for trend comparison.

        Args:
          filters: Filters to apply before aggregating results.

          from_: The start of the query time range (inclusive). RFC3339 format with timezone is
              required (e.g. `2024-11-05T00:00:00Z`).

          group_by: Specifies the column names to group results by. Requires valid columns for the
              target dataset.

          stats: Specifies the stat names to include in results. Requires valid stats for the
              target dataset (e.g. `attemptsTotal`, `bytesTotal`).

          to: Specifies the end of the query time range (exclusive). Requires RFC3339 format
              with timezone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dataset:
            raise ValueError(f"Expected a non-empty value for `dataset` but received {dataset!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/analytics/query/{dataset}/summary", account_id=account_id, dataset=dataset
            ),
            body=maybe_transform(
                {
                    "filters": filters,
                    "from_": from_,
                    "group_by": group_by,
                    "stats": stats,
                    "to": to,
                },
                analytics_query_summary_params.AnalyticsQuerySummaryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AnalyticsQuerySummaryResponse]._unwrapper,
            ),
            cast_to=cast(Type[AnalyticsQuerySummaryResponse], ResultWrapper[AnalyticsQuerySummaryResponse]),
        )

    def timeseries(
        self,
        dataset: str,
        *,
        account_id: str,
        filters: Iterable[analytics_query_timeseries_params.Filter],
        from_: Union[str, datetime],
        group_by: SequenceNotStr[str],
        resolution: str,
        stats: SequenceNotStr[str],
        to: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsQueryTimeseriesResponse:
        """Returns time-bucketed analytics data for a dataset.

        Includes time slots, each
        containing the requested stats, group-by dimensions, and resolution-controlled
        bucket size (e.g. `hour`, `day`).

        Args:
          filters: Filters to apply before aggregating results.

          from_: The start of the query time range (inclusive). RFC3339 format with timezone is
              required (e.g. `2024-11-05T00:00:00Z`).

          group_by: Specifies the column names to group results by. Requires valid columns for the
              target dataset.

          resolution: Time bucket size for grouping results. Controls the granularity of the returned
              time slots.

          stats: Specifies the stat names to include in results. Requires valid stats for the
              target dataset (e.g. `attemptsTotal`, `bytesTotal`).

          to: Specifies the end of the query time range (exclusive). Requires RFC3339 format
              with timezone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dataset:
            raise ValueError(f"Expected a non-empty value for `dataset` but received {dataset!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/analytics/query/{dataset}/timeseries", account_id=account_id, dataset=dataset
            ),
            body=maybe_transform(
                {
                    "filters": filters,
                    "from_": from_,
                    "group_by": group_by,
                    "resolution": resolution,
                    "stats": stats,
                    "to": to,
                },
                analytics_query_timeseries_params.AnalyticsQueryTimeseriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AnalyticsQueryTimeseriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[AnalyticsQueryTimeseriesResponse], ResultWrapper[AnalyticsQueryTimeseriesResponse]),
        )

    def top_n(
        self,
        dataset: str,
        *,
        account_id: str,
        filters: Iterable[analytics_query_top_n_params.Filter],
        from_: Union[str, datetime],
        group_by: SequenceNotStr[str],
        n: int,
        order_by: str,
        stats: SequenceNotStr[str],
        to: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[AnalyticsQueryTopNResponse]:
        """Returns the top N results for a dataset by a specified stat.

        Includes an array
        of result rows, each containing the requested stats and group-by dimensions.

        Args:
          filters: Filters to apply before aggregating results.

          from_: The start of the query time range (inclusive). RFC3339 format with timezone is
              required (e.g. `2024-11-05T00:00:00Z`).

          group_by: Specifies the column names to group results by. Requires valid columns for the
              target dataset.

          n: Maximum number of results to return.

          order_by: Specifies the stat name for sorting results in descending order. Requires a
              valid stat for the target dataset.

          stats: Specifies the stat names to include in results. Requires valid stats for the
              target dataset (e.g. `attemptsTotal`, `bytesTotal`).

          to: Specifies the end of the query time range (exclusive). Requires RFC3339 format
              with timezone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dataset:
            raise ValueError(f"Expected a non-empty value for `dataset` but received {dataset!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/analytics/query/{dataset}/top-n", account_id=account_id, dataset=dataset
            ),
            page=SyncSinglePage[AnalyticsQueryTopNResponse],
            body=maybe_transform(
                {
                    "filters": filters,
                    "from_": from_,
                    "group_by": group_by,
                    "n": n,
                    "order_by": order_by,
                    "stats": stats,
                    "to": to,
                },
                analytics_query_top_n_params.AnalyticsQueryTopNParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=AnalyticsQueryTopNResponse,
            method="post",
        )


class AsyncAnalyticsQueryResource(AsyncAPIResource):
    @cached_property
    def data_security(self) -> AsyncDataSecurityResource:
        return AsyncDataSecurityResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAnalyticsQueryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAnalyticsQueryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalyticsQueryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAnalyticsQueryResourceWithStreamingResponse(self)

    async def summary(
        self,
        dataset: str,
        *,
        account_id: str,
        filters: Iterable[analytics_query_summary_params.Filter],
        from_: Union[str, datetime],
        group_by: SequenceNotStr[str],
        stats: SequenceNotStr[str],
        to: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsQuerySummaryResponse:
        """Returns aggregate summary stats for a dataset.

        Includes current-period and
        previous-period totals for trend comparison.

        Args:
          filters: Filters to apply before aggregating results.

          from_: The start of the query time range (inclusive). RFC3339 format with timezone is
              required (e.g. `2024-11-05T00:00:00Z`).

          group_by: Specifies the column names to group results by. Requires valid columns for the
              target dataset.

          stats: Specifies the stat names to include in results. Requires valid stats for the
              target dataset (e.g. `attemptsTotal`, `bytesTotal`).

          to: Specifies the end of the query time range (exclusive). Requires RFC3339 format
              with timezone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dataset:
            raise ValueError(f"Expected a non-empty value for `dataset` but received {dataset!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/analytics/query/{dataset}/summary", account_id=account_id, dataset=dataset
            ),
            body=await async_maybe_transform(
                {
                    "filters": filters,
                    "from_": from_,
                    "group_by": group_by,
                    "stats": stats,
                    "to": to,
                },
                analytics_query_summary_params.AnalyticsQuerySummaryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AnalyticsQuerySummaryResponse]._unwrapper,
            ),
            cast_to=cast(Type[AnalyticsQuerySummaryResponse], ResultWrapper[AnalyticsQuerySummaryResponse]),
        )

    async def timeseries(
        self,
        dataset: str,
        *,
        account_id: str,
        filters: Iterable[analytics_query_timeseries_params.Filter],
        from_: Union[str, datetime],
        group_by: SequenceNotStr[str],
        resolution: str,
        stats: SequenceNotStr[str],
        to: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsQueryTimeseriesResponse:
        """Returns time-bucketed analytics data for a dataset.

        Includes time slots, each
        containing the requested stats, group-by dimensions, and resolution-controlled
        bucket size (e.g. `hour`, `day`).

        Args:
          filters: Filters to apply before aggregating results.

          from_: The start of the query time range (inclusive). RFC3339 format with timezone is
              required (e.g. `2024-11-05T00:00:00Z`).

          group_by: Specifies the column names to group results by. Requires valid columns for the
              target dataset.

          resolution: Time bucket size for grouping results. Controls the granularity of the returned
              time slots.

          stats: Specifies the stat names to include in results. Requires valid stats for the
              target dataset (e.g. `attemptsTotal`, `bytesTotal`).

          to: Specifies the end of the query time range (exclusive). Requires RFC3339 format
              with timezone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dataset:
            raise ValueError(f"Expected a non-empty value for `dataset` but received {dataset!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/analytics/query/{dataset}/timeseries", account_id=account_id, dataset=dataset
            ),
            body=await async_maybe_transform(
                {
                    "filters": filters,
                    "from_": from_,
                    "group_by": group_by,
                    "resolution": resolution,
                    "stats": stats,
                    "to": to,
                },
                analytics_query_timeseries_params.AnalyticsQueryTimeseriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AnalyticsQueryTimeseriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[AnalyticsQueryTimeseriesResponse], ResultWrapper[AnalyticsQueryTimeseriesResponse]),
        )

    def top_n(
        self,
        dataset: str,
        *,
        account_id: str,
        filters: Iterable[analytics_query_top_n_params.Filter],
        from_: Union[str, datetime],
        group_by: SequenceNotStr[str],
        n: int,
        order_by: str,
        stats: SequenceNotStr[str],
        to: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AnalyticsQueryTopNResponse, AsyncSinglePage[AnalyticsQueryTopNResponse]]:
        """Returns the top N results for a dataset by a specified stat.

        Includes an array
        of result rows, each containing the requested stats and group-by dimensions.

        Args:
          filters: Filters to apply before aggregating results.

          from_: The start of the query time range (inclusive). RFC3339 format with timezone is
              required (e.g. `2024-11-05T00:00:00Z`).

          group_by: Specifies the column names to group results by. Requires valid columns for the
              target dataset.

          n: Maximum number of results to return.

          order_by: Specifies the stat name for sorting results in descending order. Requires a
              valid stat for the target dataset.

          stats: Specifies the stat names to include in results. Requires valid stats for the
              target dataset (e.g. `attemptsTotal`, `bytesTotal`).

          to: Specifies the end of the query time range (exclusive). Requires RFC3339 format
              with timezone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dataset:
            raise ValueError(f"Expected a non-empty value for `dataset` but received {dataset!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/analytics/query/{dataset}/top-n", account_id=account_id, dataset=dataset
            ),
            page=AsyncSinglePage[AnalyticsQueryTopNResponse],
            body=maybe_transform(
                {
                    "filters": filters,
                    "from_": from_,
                    "group_by": group_by,
                    "n": n,
                    "order_by": order_by,
                    "stats": stats,
                    "to": to,
                },
                analytics_query_top_n_params.AnalyticsQueryTopNParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=AnalyticsQueryTopNResponse,
            method="post",
        )


class AnalyticsQueryResourceWithRawResponse:
    def __init__(self, analytics_query: AnalyticsQueryResource) -> None:
        self._analytics_query = analytics_query

        self.summary = to_raw_response_wrapper(
            analytics_query.summary,
        )
        self.timeseries = to_raw_response_wrapper(
            analytics_query.timeseries,
        )
        self.top_n = to_raw_response_wrapper(
            analytics_query.top_n,
        )

    @cached_property
    def data_security(self) -> DataSecurityResourceWithRawResponse:
        return DataSecurityResourceWithRawResponse(self._analytics_query.data_security)


class AsyncAnalyticsQueryResourceWithRawResponse:
    def __init__(self, analytics_query: AsyncAnalyticsQueryResource) -> None:
        self._analytics_query = analytics_query

        self.summary = async_to_raw_response_wrapper(
            analytics_query.summary,
        )
        self.timeseries = async_to_raw_response_wrapper(
            analytics_query.timeseries,
        )
        self.top_n = async_to_raw_response_wrapper(
            analytics_query.top_n,
        )

    @cached_property
    def data_security(self) -> AsyncDataSecurityResourceWithRawResponse:
        return AsyncDataSecurityResourceWithRawResponse(self._analytics_query.data_security)


class AnalyticsQueryResourceWithStreamingResponse:
    def __init__(self, analytics_query: AnalyticsQueryResource) -> None:
        self._analytics_query = analytics_query

        self.summary = to_streamed_response_wrapper(
            analytics_query.summary,
        )
        self.timeseries = to_streamed_response_wrapper(
            analytics_query.timeseries,
        )
        self.top_n = to_streamed_response_wrapper(
            analytics_query.top_n,
        )

    @cached_property
    def data_security(self) -> DataSecurityResourceWithStreamingResponse:
        return DataSecurityResourceWithStreamingResponse(self._analytics_query.data_security)


class AsyncAnalyticsQueryResourceWithStreamingResponse:
    def __init__(self, analytics_query: AsyncAnalyticsQueryResource) -> None:
        self._analytics_query = analytics_query

        self.summary = async_to_streamed_response_wrapper(
            analytics_query.summary,
        )
        self.timeseries = async_to_streamed_response_wrapper(
            analytics_query.timeseries,
        )
        self.top_n = async_to_streamed_response_wrapper(
            analytics_query.top_n,
        )

    @cached_property
    def data_security(self) -> AsyncDataSecurityResourceWithStreamingResponse:
        return AsyncDataSecurityResourceWithStreamingResponse(self._analytics_query.data_security)
