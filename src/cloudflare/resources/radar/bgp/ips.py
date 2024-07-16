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
        return IPsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IPsResourceWithStreamingResponse:
        return IPsResourceWithStreamingResponse(self)

    def timeseries(
        self,
        *,
        asn: str | NotGiven = NOT_GIVEN,
        date_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        date_range: str | NotGiven = NOT_GIVEN,
        date_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        include_delay: bool | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPTimeseriesResponse:
        """
        Gets time-series data for the announced IP space count, represented as the
        number of IPv4 /24s and IPv6 /48s, for a given ASN.

        Args:
          asn: Comma separated list of ASNs.

          date_end: End of the date range (inclusive).

          date_range: Shorthand date ranges for the last X days - use when you don't need specific
              start and end dates.

          date_start: Start of the date range (inclusive).

          format: Format results are returned in.

          include_delay: Include data delay meta information

          location: Comma separated list of locations.

          name: Array of names that will be used to name the series in responses.

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
        return AsyncIPsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIPsResourceWithStreamingResponse:
        return AsyncIPsResourceWithStreamingResponse(self)

    async def timeseries(
        self,
        *,
        asn: str | NotGiven = NOT_GIVEN,
        date_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        date_range: str | NotGiven = NOT_GIVEN,
        date_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        include_delay: bool | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPTimeseriesResponse:
        """
        Gets time-series data for the announced IP space count, represented as the
        number of IPv4 /24s and IPv6 /48s, for a given ASN.

        Args:
          asn: Comma separated list of ASNs.

          date_end: End of the date range (inclusive).

          date_range: Shorthand date ranges for the last X days - use when you don't need specific
              start and end dates.

          date_start: Start of the date range (inclusive).

          format: Format results are returned in.

          include_delay: Include data delay meta information

          location: Comma separated list of locations.

          name: Array of names that will be used to name the series in responses.

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
