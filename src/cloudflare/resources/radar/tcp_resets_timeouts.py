# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.radar.tcp_resets_timeout_summary_response import TCPResetsTimeoutSummaryResponse

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from ..._base_client import make_request_options

from typing import Type, List, Union

from datetime import datetime

from typing_extensions import Literal

from ...types.radar.tcp_resets_timeout_timeseries_groups_response import TCPResetsTimeoutTimeseriesGroupsResponse

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from ...types.radar import tcp_resets_timeout_summary_params
from ...types.radar import tcp_resets_timeout_timeseries_groups_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["TCPResetsTimeoutsResource", "AsyncTCPResetsTimeoutsResource"]

class TCPResetsTimeoutsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TCPResetsTimeoutsResourceWithRawResponse:
        return TCPResetsTimeoutsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TCPResetsTimeoutsResourceWithStreamingResponse:
        return TCPResetsTimeoutsResourceWithStreamingResponse(self)

    def summary(self,
    *,
    asn: List[str] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    date_range: List[str] | NotGiven = NOT_GIVEN,
    date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TCPResetsTimeoutSummaryResponse:
        """
        Percentage distribution by connection stage of TCP connections terminated within
        the first 10 packets by a reset or timeout, for a given time period.

        Args:
          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/tcp_resets_timeouts/summary",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "asn": asn,
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "format": format,
                "location": location,
                "name": name,
            }, tcp_resets_timeout_summary_params.TCPResetsTimeoutSummaryParams), post_parser=ResultWrapper[TCPResetsTimeoutSummaryResponse]._unwrapper),
            cast_to=cast(Type[TCPResetsTimeoutSummaryResponse], ResultWrapper[TCPResetsTimeoutSummaryResponse]),
        )

    def timeseries_groups(self,
    *,
    agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
    asn: List[str] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    date_range: List[str] | NotGiven = NOT_GIVEN,
    date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TCPResetsTimeoutTimeseriesGroupsResponse:
        """
        Percentage distribution by connection stage of TCP connections terminated within
        the first 10 packets by a reset or timeout, over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/tcp_resets_timeouts/timeseries_groups",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "agg_interval": agg_interval,
                "asn": asn,
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "format": format,
                "location": location,
                "name": name,
            }, tcp_resets_timeout_timeseries_groups_params.TCPResetsTimeoutTimeseriesGroupsParams), post_parser=ResultWrapper[TCPResetsTimeoutTimeseriesGroupsResponse]._unwrapper),
            cast_to=cast(Type[TCPResetsTimeoutTimeseriesGroupsResponse], ResultWrapper[TCPResetsTimeoutTimeseriesGroupsResponse]),
        )

class AsyncTCPResetsTimeoutsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTCPResetsTimeoutsResourceWithRawResponse:
        return AsyncTCPResetsTimeoutsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTCPResetsTimeoutsResourceWithStreamingResponse:
        return AsyncTCPResetsTimeoutsResourceWithStreamingResponse(self)

    async def summary(self,
    *,
    asn: List[str] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    date_range: List[str] | NotGiven = NOT_GIVEN,
    date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TCPResetsTimeoutSummaryResponse:
        """
        Percentage distribution by connection stage of TCP connections terminated within
        the first 10 packets by a reset or timeout, for a given time period.

        Args:
          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/tcp_resets_timeouts/summary",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "asn": asn,
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "format": format,
                "location": location,
                "name": name,
            }, tcp_resets_timeout_summary_params.TCPResetsTimeoutSummaryParams), post_parser=ResultWrapper[TCPResetsTimeoutSummaryResponse]._unwrapper),
            cast_to=cast(Type[TCPResetsTimeoutSummaryResponse], ResultWrapper[TCPResetsTimeoutSummaryResponse]),
        )

    async def timeseries_groups(self,
    *,
    agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
    asn: List[str] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    date_range: List[str] | NotGiven = NOT_GIVEN,
    date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TCPResetsTimeoutTimeseriesGroupsResponse:
        """
        Percentage distribution by connection stage of TCP connections terminated within
        the first 10 packets by a reset or timeout, over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/tcp_resets_timeouts/timeseries_groups",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "agg_interval": agg_interval,
                "asn": asn,
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "format": format,
                "location": location,
                "name": name,
            }, tcp_resets_timeout_timeseries_groups_params.TCPResetsTimeoutTimeseriesGroupsParams), post_parser=ResultWrapper[TCPResetsTimeoutTimeseriesGroupsResponse]._unwrapper),
            cast_to=cast(Type[TCPResetsTimeoutTimeseriesGroupsResponse], ResultWrapper[TCPResetsTimeoutTimeseriesGroupsResponse]),
        )

class TCPResetsTimeoutsResourceWithRawResponse:
    def __init__(self, tcp_resets_timeouts: TCPResetsTimeoutsResource) -> None:
        self._tcp_resets_timeouts = tcp_resets_timeouts

        self.summary = to_raw_response_wrapper(
            tcp_resets_timeouts.summary,
        )
        self.timeseries_groups = to_raw_response_wrapper(
            tcp_resets_timeouts.timeseries_groups,
        )

class AsyncTCPResetsTimeoutsResourceWithRawResponse:
    def __init__(self, tcp_resets_timeouts: AsyncTCPResetsTimeoutsResource) -> None:
        self._tcp_resets_timeouts = tcp_resets_timeouts

        self.summary = async_to_raw_response_wrapper(
            tcp_resets_timeouts.summary,
        )
        self.timeseries_groups = async_to_raw_response_wrapper(
            tcp_resets_timeouts.timeseries_groups,
        )

class TCPResetsTimeoutsResourceWithStreamingResponse:
    def __init__(self, tcp_resets_timeouts: TCPResetsTimeoutsResource) -> None:
        self._tcp_resets_timeouts = tcp_resets_timeouts

        self.summary = to_streamed_response_wrapper(
            tcp_resets_timeouts.summary,
        )
        self.timeseries_groups = to_streamed_response_wrapper(
            tcp_resets_timeouts.timeseries_groups,
        )

class AsyncTCPResetsTimeoutsResourceWithStreamingResponse:
    def __init__(self, tcp_resets_timeouts: AsyncTCPResetsTimeoutsResource) -> None:
        self._tcp_resets_timeouts = tcp_resets_timeouts

        self.summary = async_to_streamed_response_wrapper(
            tcp_resets_timeouts.summary,
        )
        self.timeseries_groups = async_to_streamed_response_wrapper(
            tcp_resets_timeouts.timeseries_groups,
        )