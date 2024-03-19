# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import (
    make_request_options,
)
from .....types.dns.analytics.reports import DNSDNSAnalyticsAPIReportBytime, bytime_get_params

__all__ = ["Bytimes", "AsyncBytimes"]


class Bytimes(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BytimesWithRawResponse:
        return BytimesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BytimesWithStreamingResponse:
        return BytimesWithStreamingResponse(self)

    def get(
        self,
        *,
        zone_id: str,
        dimensions: str | NotGiven = NOT_GIVEN,
        filters: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        metrics: str | NotGiven = NOT_GIVEN,
        since: Union[str, datetime] | NotGiven = NOT_GIVEN,
        sort: str | NotGiven = NOT_GIVEN,
        time_delta: Literal["all", "auto", "year", "quarter", "month", "week", "day", "hour", "dekaminute", "minute"]
        | NotGiven = NOT_GIVEN,
        until: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSDNSAnalyticsAPIReportBytime:
        """
        Retrieves a list of aggregate metrics grouped by time interval.

        See
        [Analytics API properties](https://developers.cloudflare.com/dns/reference/analytics-api-properties/)
        for detailed information about the available query parameters.

        Args:
          zone_id: Identifier

          dimensions: A comma-separated list of dimensions to group results by.

          filters: Segmentation filter in 'attribute operator value' format.

          limit: Limit number of returned metrics.

          metrics: A comma-separated list of metrics to query.

          since: Start date and time of requesting data period in ISO 8601 format.

          sort: A comma-separated list of dimensions to sort by, where each dimension may be
              prefixed by - (descending) or + (ascending).

          time_delta: Unit of time to group data by.

          until: End date and time of requesting data period in ISO 8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/dns_analytics/report/bytime",
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
                        "time_delta": time_delta,
                        "until": until,
                    },
                    bytime_get_params.BytimeGetParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DNSDNSAnalyticsAPIReportBytime], ResultWrapper[DNSDNSAnalyticsAPIReportBytime]),
        )


class AsyncBytimes(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBytimesWithRawResponse:
        return AsyncBytimesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBytimesWithStreamingResponse:
        return AsyncBytimesWithStreamingResponse(self)

    async def get(
        self,
        *,
        zone_id: str,
        dimensions: str | NotGiven = NOT_GIVEN,
        filters: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        metrics: str | NotGiven = NOT_GIVEN,
        since: Union[str, datetime] | NotGiven = NOT_GIVEN,
        sort: str | NotGiven = NOT_GIVEN,
        time_delta: Literal["all", "auto", "year", "quarter", "month", "week", "day", "hour", "dekaminute", "minute"]
        | NotGiven = NOT_GIVEN,
        until: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSDNSAnalyticsAPIReportBytime:
        """
        Retrieves a list of aggregate metrics grouped by time interval.

        See
        [Analytics API properties](https://developers.cloudflare.com/dns/reference/analytics-api-properties/)
        for detailed information about the available query parameters.

        Args:
          zone_id: Identifier

          dimensions: A comma-separated list of dimensions to group results by.

          filters: Segmentation filter in 'attribute operator value' format.

          limit: Limit number of returned metrics.

          metrics: A comma-separated list of metrics to query.

          since: Start date and time of requesting data period in ISO 8601 format.

          sort: A comma-separated list of dimensions to sort by, where each dimension may be
              prefixed by - (descending) or + (ascending).

          time_delta: Unit of time to group data by.

          until: End date and time of requesting data period in ISO 8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/dns_analytics/report/bytime",
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
                        "time_delta": time_delta,
                        "until": until,
                    },
                    bytime_get_params.BytimeGetParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DNSDNSAnalyticsAPIReportBytime], ResultWrapper[DNSDNSAnalyticsAPIReportBytime]),
        )


class BytimesWithRawResponse:
    def __init__(self, bytimes: Bytimes) -> None:
        self._bytimes = bytimes

        self.get = to_raw_response_wrapper(
            bytimes.get,
        )


class AsyncBytimesWithRawResponse:
    def __init__(self, bytimes: AsyncBytimes) -> None:
        self._bytimes = bytimes

        self.get = async_to_raw_response_wrapper(
            bytimes.get,
        )


class BytimesWithStreamingResponse:
    def __init__(self, bytimes: Bytimes) -> None:
        self._bytimes = bytimes

        self.get = to_streamed_response_wrapper(
            bytimes.get,
        )


class AsyncBytimesWithStreamingResponse:
    def __init__(self, bytimes: AsyncBytimes) -> None:
        self._bytimes = bytimes

        self.get = async_to_streamed_response_wrapper(
            bytimes.get,
        )
