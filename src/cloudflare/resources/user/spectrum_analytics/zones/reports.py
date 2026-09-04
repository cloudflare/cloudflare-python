# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, cast
from datetime import datetime

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
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
from .....types.user.spectrum_analytics.zones import report_get_params
from .....types.user.spectrum_analytics.zones.report_get_response import ReportGetResponse

__all__ = ["ReportsResource", "AsyncReportsResource"]


class ReportsResource(SyncAPIResource):
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
        cdn_traffic: bool | Omit = omit,
        since: Union[str, datetime] | Omit = omit,
        until: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportGetResponse:
        """
        Retrieves a list of total bandwidth by zone over a given time period.

        Args:
          cdn_traffic: Include CDN traffic in the bandwidth aggregation.

          since: Start of time interval to query, defaults to `until` - 6 hours. Timestamp must
              be in RFC3339 format and uses UTC unless otherwise specified.

          until: End of time interval to query, defaults to current time. Timestamp must be in
              RFC3339 format and uses UTC unless otherwise specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/user/spectrum_analytics/zones/report",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cdn_traffic": cdn_traffic,
                        "since": since,
                        "until": until,
                    },
                    report_get_params.ReportGetParams,
                ),
                post_parser=ResultWrapper[ReportGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[ReportGetResponse], ResultWrapper[ReportGetResponse]),
        )


class AsyncReportsResource(AsyncAPIResource):
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
        cdn_traffic: bool | Omit = omit,
        since: Union[str, datetime] | Omit = omit,
        until: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportGetResponse:
        """
        Retrieves a list of total bandwidth by zone over a given time period.

        Args:
          cdn_traffic: Include CDN traffic in the bandwidth aggregation.

          since: Start of time interval to query, defaults to `until` - 6 hours. Timestamp must
              be in RFC3339 format and uses UTC unless otherwise specified.

          until: End of time interval to query, defaults to current time. Timestamp must be in
              RFC3339 format and uses UTC unless otherwise specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/user/spectrum_analytics/zones/report",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cdn_traffic": cdn_traffic,
                        "since": since,
                        "until": until,
                    },
                    report_get_params.ReportGetParams,
                ),
                post_parser=ResultWrapper[ReportGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[ReportGetResponse], ResultWrapper[ReportGetResponse]),
        )


class ReportsResourceWithRawResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

        self.get = to_raw_response_wrapper(
            reports.get,
        )


class AsyncReportsResourceWithRawResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

        self.get = async_to_raw_response_wrapper(
            reports.get,
        )


class ReportsResourceWithStreamingResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

        self.get = to_streamed_response_wrapper(
            reports.get,
        )


class AsyncReportsResourceWithStreamingResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

        self.get = async_to_streamed_response_wrapper(
            reports.get,
        )
