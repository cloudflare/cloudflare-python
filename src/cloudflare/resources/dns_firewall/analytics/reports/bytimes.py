# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, Optional, cast
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
from ....._base_client import make_request_options
from .....types.dns.analytics.reports.by_time import ByTime
from .....types.dns_firewall.analytics.reports import bytime_get_params

__all__ = ["BytimesResource", "AsyncBytimesResource"]


class BytimesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BytimesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return BytimesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BytimesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return BytimesResourceWithStreamingResponse(self)

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
        time_delta: Literal["all", "auto", "year", "quarter", "month", "week", "day", "hour", "dekaminute", "minute"]
        | NotGiven = NOT_GIVEN,
        until: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ByTime]:
        """
        Retrieves a list of aggregate metrics grouped by time interval.

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

          time_delta: Unit of time to group data by.

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
            f"/accounts/{account_id}/dns_firewall/{dns_firewall_id}/dns_analytics/report/bytime",
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
                post_parser=ResultWrapper[Optional[ByTime]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ByTime]], ResultWrapper[ByTime]),
        )


class AsyncBytimesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBytimesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBytimesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBytimesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncBytimesResourceWithStreamingResponse(self)

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
        time_delta: Literal["all", "auto", "year", "quarter", "month", "week", "day", "hour", "dekaminute", "minute"]
        | NotGiven = NOT_GIVEN,
        until: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ByTime]:
        """
        Retrieves a list of aggregate metrics grouped by time interval.

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

          time_delta: Unit of time to group data by.

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
            f"/accounts/{account_id}/dns_firewall/{dns_firewall_id}/dns_analytics/report/bytime",
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
                post_parser=ResultWrapper[Optional[ByTime]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ByTime]], ResultWrapper[ByTime]),
        )


class BytimesResourceWithRawResponse:
    def __init__(self, bytimes: BytimesResource) -> None:
        self._bytimes = bytimes

        self.get = to_raw_response_wrapper(
            bytimes.get,
        )


class AsyncBytimesResourceWithRawResponse:
    def __init__(self, bytimes: AsyncBytimesResource) -> None:
        self._bytimes = bytimes

        self.get = async_to_raw_response_wrapper(
            bytimes.get,
        )


class BytimesResourceWithStreamingResponse:
    def __init__(self, bytimes: BytimesResource) -> None:
        self._bytimes = bytimes

        self.get = to_streamed_response_wrapper(
            bytimes.get,
        )


class AsyncBytimesResourceWithStreamingResponse:
    def __init__(self, bytimes: AsyncBytimesResource) -> None:
        self._bytimes = bytimes

        self.get = async_to_streamed_response_wrapper(
            bytimes.get,
        )
