# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
from ....types.radar.bgp import ip_timeseries_params
from ....types.radar.bgp.ip_timeseries_response import IPTimeseriesResponse

__all__ = ["IPsResource", "AsyncIPsResource"]


class IPsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IPsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return IPsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IPsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return IPsResourceWithStreamingResponse(self)

    def timeseries(
        self,
        *,
        asn: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        include_delay: bool | NotGiven = NOT_GIVEN,
        ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPTimeseriesResponse:
        """
        Retrieves time series data for the announced IP space count, represented as the
        number of IPv4 /24s and IPv6 /48s, for a given ASN.

        Args:
          asn: Comma-separated list of Autonomous System Numbers (ASNs). Prefix with `-` to
              exclude ASNs from results. For example, `-174, 3356` excludes results from
              AS174, but includes results from AS3356.

          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          include_delay: Include data delay meta information.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          location: Comma-separated list of locations (alpha-2 codes).

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/bgp/ips/timeseries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asn": asn,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "include_delay": include_delay,
                        "ip_version": ip_version,
                        "location": location,
                        "name": name,
                    },
                    ip_timeseries_params.IPTimeseriesParams,
                ),
                post_parser=ResultWrapper[IPTimeseriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[IPTimeseriesResponse], ResultWrapper[IPTimeseriesResponse]),
        )


class AsyncIPsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIPsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIPsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIPsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncIPsResourceWithStreamingResponse(self)

    async def timeseries(
        self,
        *,
        asn: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        include_delay: bool | NotGiven = NOT_GIVEN,
        ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPTimeseriesResponse:
        """
        Retrieves time series data for the announced IP space count, represented as the
        number of IPv4 /24s and IPv6 /48s, for a given ASN.

        Args:
          asn: Comma-separated list of Autonomous System Numbers (ASNs). Prefix with `-` to
              exclude ASNs from results. For example, `-174, 3356` excludes results from
              AS174, but includes results from AS3356.

          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          include_delay: Include data delay meta information.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          location: Comma-separated list of locations (alpha-2 codes).

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/bgp/ips/timeseries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asn": asn,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "include_delay": include_delay,
                        "ip_version": ip_version,
                        "location": location,
                        "name": name,
                    },
                    ip_timeseries_params.IPTimeseriesParams,
                ),
                post_parser=ResultWrapper[IPTimeseriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[IPTimeseriesResponse], ResultWrapper[IPTimeseriesResponse]),
        )


class IPsResourceWithRawResponse:
    def __init__(self, ips: IPsResource) -> None:
        self._ips = ips

        self.timeseries = to_raw_response_wrapper(
            ips.timeseries,
        )


class AsyncIPsResourceWithRawResponse:
    def __init__(self, ips: AsyncIPsResource) -> None:
        self._ips = ips

        self.timeseries = async_to_raw_response_wrapper(
            ips.timeseries,
        )


class IPsResourceWithStreamingResponse:
    def __init__(self, ips: IPsResource) -> None:
        self._ips = ips

        self.timeseries = to_streamed_response_wrapper(
            ips.timeseries,
        )


class AsyncIPsResourceWithStreamingResponse:
    def __init__(self, ips: AsyncIPsResource) -> None:
        self._ips = ips

        self.timeseries = async_to_streamed_response_wrapper(
            ips.timeseries,
        )
