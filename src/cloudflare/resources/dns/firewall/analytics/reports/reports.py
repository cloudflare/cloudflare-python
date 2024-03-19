# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, cast
from datetime import datetime

import httpx

from .bytimes import (
    Bytimes,
    AsyncBytimes,
    BytimesWithRawResponse,
    AsyncBytimesWithRawResponse,
    BytimesWithStreamingResponse,
    AsyncBytimesWithStreamingResponse,
)
from ......_types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ......_utils import (
    maybe_transform,
    async_maybe_transform,
)
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_wrappers import ResultWrapper
from ......_base_client import (
    make_request_options,
)
from ......types.dns.analytics import DNSDNSAnalyticsAPIReport
from ......types.dns.firewall.analytics import report_get_params

__all__ = ["Reports", "AsyncReports"]


class Reports(SyncAPIResource):
    @cached_property
    def bytimes(self) -> Bytimes:
        return Bytimes(self._client)

    @cached_property
    def with_raw_response(self) -> ReportsWithRawResponse:
        return ReportsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportsWithStreamingResponse:
        return ReportsWithStreamingResponse(self)

    def get(
        self,
        dns_firewall_id: str,
        *,
        account_id: str,
        dimensions: str | NotGiven = NOT_GIVEN,
        filters: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        metrics: str | NotGiven = NOT_GIVEN,
        since: Union[str, datetime] | NotGiven = NOT_GIVEN,
        sort: str | NotGiven = NOT_GIVEN,
        until: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSDNSAnalyticsAPIReport:
        """
        Retrieves a list of summarised aggregate metrics over a given time period.

        See
        [Analytics API properties](https://developers.cloudflare.com/dns/reference/analytics-api-properties/)
        for detailed information about the available query parameters.

        Args:
          account_id: Identifier

          dns_firewall_id: Identifier

          dimensions: A comma-separated list of dimensions to group results by.

          filters: Segmentation filter in 'attribute operator value' format.

          limit: Limit number of returned metrics.

          metrics: A comma-separated list of metrics to query.

          since: Start date and time of requesting data period in ISO 8601 format.

          sort: A comma-separated list of dimensions to sort by, where each dimension may be
              prefixed by - (descending) or + (ascending).

          until: End date and time of requesting data period in ISO 8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dns_firewall_id:
            raise ValueError(f"Expected a non-empty value for `dns_firewall_id` but received {dns_firewall_id!r}")
        return self._get(
            f"/accounts/{account_id}/dns_firewall/{dns_firewall_id}/dns_analytics/report",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dimensions": dimensions,
                        "filters": filters,
                        "limit": limit,
                        "metrics": metrics,
                        "since": since,
                        "sort": sort,
                        "until": until,
                    },
                    report_get_params.ReportGetParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DNSDNSAnalyticsAPIReport], ResultWrapper[DNSDNSAnalyticsAPIReport]),
        )


class AsyncReports(AsyncAPIResource):
    @cached_property
    def bytimes(self) -> AsyncBytimes:
        return AsyncBytimes(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReportsWithRawResponse:
        return AsyncReportsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportsWithStreamingResponse:
        return AsyncReportsWithStreamingResponse(self)

    async def get(
        self,
        dns_firewall_id: str,
        *,
        account_id: str,
        dimensions: str | NotGiven = NOT_GIVEN,
        filters: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        metrics: str | NotGiven = NOT_GIVEN,
        since: Union[str, datetime] | NotGiven = NOT_GIVEN,
        sort: str | NotGiven = NOT_GIVEN,
        until: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSDNSAnalyticsAPIReport:
        """
        Retrieves a list of summarised aggregate metrics over a given time period.

        See
        [Analytics API properties](https://developers.cloudflare.com/dns/reference/analytics-api-properties/)
        for detailed information about the available query parameters.

        Args:
          account_id: Identifier

          dns_firewall_id: Identifier

          dimensions: A comma-separated list of dimensions to group results by.

          filters: Segmentation filter in 'attribute operator value' format.

          limit: Limit number of returned metrics.

          metrics: A comma-separated list of metrics to query.

          since: Start date and time of requesting data period in ISO 8601 format.

          sort: A comma-separated list of dimensions to sort by, where each dimension may be
              prefixed by - (descending) or + (ascending).

          until: End date and time of requesting data period in ISO 8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dns_firewall_id:
            raise ValueError(f"Expected a non-empty value for `dns_firewall_id` but received {dns_firewall_id!r}")
        return await self._get(
            f"/accounts/{account_id}/dns_firewall/{dns_firewall_id}/dns_analytics/report",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "dimensions": dimensions,
                        "filters": filters,
                        "limit": limit,
                        "metrics": metrics,
                        "since": since,
                        "sort": sort,
                        "until": until,
                    },
                    report_get_params.ReportGetParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DNSDNSAnalyticsAPIReport], ResultWrapper[DNSDNSAnalyticsAPIReport]),
        )


class ReportsWithRawResponse:
    def __init__(self, reports: Reports) -> None:
        self._reports = reports

        self.get = to_raw_response_wrapper(
            reports.get,
        )

    @cached_property
    def bytimes(self) -> BytimesWithRawResponse:
        return BytimesWithRawResponse(self._reports.bytimes)


class AsyncReportsWithRawResponse:
    def __init__(self, reports: AsyncReports) -> None:
        self._reports = reports

        self.get = async_to_raw_response_wrapper(
            reports.get,
        )

    @cached_property
    def bytimes(self) -> AsyncBytimesWithRawResponse:
        return AsyncBytimesWithRawResponse(self._reports.bytimes)


class ReportsWithStreamingResponse:
    def __init__(self, reports: Reports) -> None:
        self._reports = reports

        self.get = to_streamed_response_wrapper(
            reports.get,
        )

    @cached_property
    def bytimes(self) -> BytimesWithStreamingResponse:
        return BytimesWithStreamingResponse(self._reports.bytimes)


class AsyncReportsWithStreamingResponse:
    def __init__(self, reports: AsyncReports) -> None:
        self._reports = reports

        self.get = async_to_streamed_response_wrapper(
            reports.get,
        )

    @cached_property
    def bytimes(self) -> AsyncBytimesWithStreamingResponse:
        return AsyncBytimesWithStreamingResponse(self._reports.bytimes)
