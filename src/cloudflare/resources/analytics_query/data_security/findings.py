# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, Iterable, cast
from datetime import datetime

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.analytics_query.data_security import finding_summary_params, finding_timeseries_params
from ....types.analytics_query.data_security.finding_summary_response import FindingSummaryResponse
from ....types.analytics_query.data_security.finding_timeseries_response import FindingTimeseriesResponse

__all__ = ["FindingsResource", "AsyncFindingsResource"]


class FindingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FindingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return FindingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FindingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return FindingsResourceWithStreamingResponse(self)

    def summary(
        self,
        *,
        account_id: str,
        filters: Iterable[finding_summary_params.Filter],
        from_: Union[str, datetime],
        to: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindingSummaryResponse:
        """
        Returns aggregate current-period and previous-period totals for CASB findings.

        Args:
          filters: Filters to apply.

          from_: Start of the query time range (inclusive). RFC3339.

          to: End of the query time range (exclusive). RFC3339.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/analytics/query/data-security/findings/summary", account_id=account_id
            ),
            body=maybe_transform(
                {
                    "filters": filters,
                    "from_": from_,
                    "to": to,
                },
                finding_summary_params.FindingSummaryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[FindingSummaryResponse]._unwrapper,
            ),
            cast_to=cast(Type[FindingSummaryResponse], ResultWrapper[FindingSummaryResponse]),
        )

    def timeseries(
        self,
        *,
        account_id: str,
        filters: Iterable[finding_timeseries_params.Filter],
        from_: Union[str, datetime],
        to: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindingTimeseriesResponse:
        """
        Returns merged time-bucketed CASB findings.

        Args:
          filters: Filters to apply.

          from_: Start of the query time range (inclusive). RFC3339.

          to: End of the query time range (exclusive). RFC3339.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/analytics/query/data-security/findings/timeseries", account_id=account_id
            ),
            body=maybe_transform(
                {
                    "filters": filters,
                    "from_": from_,
                    "to": to,
                },
                finding_timeseries_params.FindingTimeseriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[FindingTimeseriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[FindingTimeseriesResponse], ResultWrapper[FindingTimeseriesResponse]),
        )


class AsyncFindingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFindingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFindingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFindingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncFindingsResourceWithStreamingResponse(self)

    async def summary(
        self,
        *,
        account_id: str,
        filters: Iterable[finding_summary_params.Filter],
        from_: Union[str, datetime],
        to: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindingSummaryResponse:
        """
        Returns aggregate current-period and previous-period totals for CASB findings.

        Args:
          filters: Filters to apply.

          from_: Start of the query time range (inclusive). RFC3339.

          to: End of the query time range (exclusive). RFC3339.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/analytics/query/data-security/findings/summary", account_id=account_id
            ),
            body=await async_maybe_transform(
                {
                    "filters": filters,
                    "from_": from_,
                    "to": to,
                },
                finding_summary_params.FindingSummaryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[FindingSummaryResponse]._unwrapper,
            ),
            cast_to=cast(Type[FindingSummaryResponse], ResultWrapper[FindingSummaryResponse]),
        )

    async def timeseries(
        self,
        *,
        account_id: str,
        filters: Iterable[finding_timeseries_params.Filter],
        from_: Union[str, datetime],
        to: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindingTimeseriesResponse:
        """
        Returns merged time-bucketed CASB findings.

        Args:
          filters: Filters to apply.

          from_: Start of the query time range (inclusive). RFC3339.

          to: End of the query time range (exclusive). RFC3339.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/analytics/query/data-security/findings/timeseries", account_id=account_id
            ),
            body=await async_maybe_transform(
                {
                    "filters": filters,
                    "from_": from_,
                    "to": to,
                },
                finding_timeseries_params.FindingTimeseriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[FindingTimeseriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[FindingTimeseriesResponse], ResultWrapper[FindingTimeseriesResponse]),
        )


class FindingsResourceWithRawResponse:
    def __init__(self, findings: FindingsResource) -> None:
        self._findings = findings

        self.summary = to_raw_response_wrapper(
            findings.summary,
        )
        self.timeseries = to_raw_response_wrapper(
            findings.timeseries,
        )


class AsyncFindingsResourceWithRawResponse:
    def __init__(self, findings: AsyncFindingsResource) -> None:
        self._findings = findings

        self.summary = async_to_raw_response_wrapper(
            findings.summary,
        )
        self.timeseries = async_to_raw_response_wrapper(
            findings.timeseries,
        )


class FindingsResourceWithStreamingResponse:
    def __init__(self, findings: FindingsResource) -> None:
        self._findings = findings

        self.summary = to_streamed_response_wrapper(
            findings.summary,
        )
        self.timeseries = to_streamed_response_wrapper(
            findings.timeseries,
        )


class AsyncFindingsResourceWithStreamingResponse:
    def __init__(self, findings: AsyncFindingsResource) -> None:
        self._findings = findings

        self.summary = async_to_streamed_response_wrapper(
            findings.summary,
        )
        self.timeseries = async_to_streamed_response_wrapper(
            findings.timeseries,
        )
