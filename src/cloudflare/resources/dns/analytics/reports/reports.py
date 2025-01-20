# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, Optional, cast
from datetime import datetime

import httpx

from .bytimes import (
    BytimesResource,
    AsyncBytimesResource,
    BytimesResourceWithRawResponse,
    AsyncBytimesResourceWithRawResponse,
    BytimesResourceWithStreamingResponse,
    AsyncBytimesResourceWithStreamingResponse,
)
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
from .....types.dns.analytics import report_get_params
from .....types.dns.analytics.report import Report

__all__ = ["ReportsResource", "AsyncReportsResource"]


class ReportsResource(SyncAPIResource):
    @cached_property
    def bytimes(self) -> BytimesResource:
        return BytimesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ReportsResourceWithStreamingResponse(self)

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
        until: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Report]:
        """
        Retrieves a list of summarised aggregate metrics over a given time period.

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

          until: End date and time of requesting data period in ISO 8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/dns_analytics/report",
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
                post_parser=ResultWrapper[Optional[Report]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Report]], ResultWrapper[Report]),
        )


class AsyncReportsResource(AsyncAPIResource):
    @cached_property
    def bytimes(self) -> AsyncBytimesResource:
        return AsyncBytimesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncReportsResourceWithStreamingResponse(self)

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
        until: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Report]:
        """
        Retrieves a list of summarised aggregate metrics over a given time period.

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

          until: End date and time of requesting data period in ISO 8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/dns_analytics/report",
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
                post_parser=ResultWrapper[Optional[Report]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Report]], ResultWrapper[Report]),
        )


class ReportsResourceWithRawResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

        self.get = to_raw_response_wrapper(
            reports.get,
        )

    @cached_property
    def bytimes(self) -> BytimesResourceWithRawResponse:
        return BytimesResourceWithRawResponse(self._reports.bytimes)


class AsyncReportsResourceWithRawResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

        self.get = async_to_raw_response_wrapper(
            reports.get,
        )

    @cached_property
    def bytimes(self) -> AsyncBytimesResourceWithRawResponse:
        return AsyncBytimesResourceWithRawResponse(self._reports.bytimes)


class ReportsResourceWithStreamingResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

        self.get = to_streamed_response_wrapper(
            reports.get,
        )

    @cached_property
    def bytimes(self) -> BytimesResourceWithStreamingResponse:
        return BytimesResourceWithStreamingResponse(self._reports.bytimes)


class AsyncReportsResourceWithStreamingResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

        self.get = async_to_streamed_response_wrapper(
            reports.get,
        )

    @cached_property
    def bytimes(self) -> AsyncBytimesResourceWithStreamingResponse:
        return AsyncBytimesResourceWithStreamingResponse(self._reports.bytimes)
