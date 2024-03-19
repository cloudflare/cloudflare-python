# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .top import (
    Top,
    AsyncTop,
    TopWithRawResponse,
    AsyncTopWithRawResponse,
    TopWithStreamingResponse,
    AsyncTopWithStreamingResponse,
)
from .summary import (
    Summary,
    AsyncSummary,
    SummaryWithRawResponse,
    AsyncSummaryWithRawResponse,
    SummaryWithStreamingResponse,
    AsyncSummaryWithStreamingResponse,
)
from .top.top import Top, AsyncTop
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
from .timeseries_groups import (
    TimeseriesGroups,
    AsyncTimeseriesGroups,
    TimeseriesGroupsWithRawResponse,
    AsyncTimeseriesGroupsWithRawResponse,
    TimeseriesGroupsWithStreamingResponse,
    AsyncTimeseriesGroupsWithStreamingResponse,
)
from .....types.radar.attacks import Layer3TimeseriesResponse, layer3_timeseries_params

__all__ = ["Layer3", "AsyncLayer3"]


class Layer3(SyncAPIResource):
    @cached_property
    def summary(self) -> Summary:
        return Summary(self._client)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroups:
        return TimeseriesGroups(self._client)

    @cached_property
    def top(self) -> Top:
        return Top(self._client)

    @cached_property
    def with_raw_response(self) -> Layer3WithRawResponse:
        return Layer3WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> Layer3WithStreamingResponse:
        return Layer3WithStreamingResponse(self)

    def timeseries(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[
            Literal[
                "1d",
                "2d",
                "7d",
                "14d",
                "28d",
                "12w",
                "24w",
                "52w",
                "1dControl",
                "2dControl",
                "7dControl",
                "14dControl",
                "28dControl",
                "12wControl",
                "24wControl",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        direction: Literal["ORIGIN", "TARGET"] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        metric: Literal["BYTES", "BYTES_OLD"] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        normalization: Literal["PERCENTAGE_CHANGE", "MIN0_MAX"] | NotGiven = NOT_GIVEN,
        protocol: List[Literal["UDP", "TCP", "ICMP", "GRE"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Layer3TimeseriesResponse:
        """
        Get attacks change over time by bytes.

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

          direction: Together with the `location` parameter, will apply the filter to origin or
              target location.

          format: Format results are returned in.

          ip_version: Filter for ip version.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          metric: Measurement units, eg. bytes.

          name: Array of names that will be used to name the series in responses.

          normalization: Normalization method applied. Refer to
              [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

          protocol: Array of L3/4 attack types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/attacks/layer3/timeseries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "asn": asn,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "direction": direction,
                        "format": format,
                        "ip_version": ip_version,
                        "location": location,
                        "metric": metric,
                        "name": name,
                        "normalization": normalization,
                        "protocol": protocol,
                    },
                    layer3_timeseries_params.Layer3TimeseriesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Layer3TimeseriesResponse], ResultWrapper[Layer3TimeseriesResponse]),
        )


class AsyncLayer3(AsyncAPIResource):
    @cached_property
    def summary(self) -> AsyncSummary:
        return AsyncSummary(self._client)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroups:
        return AsyncTimeseriesGroups(self._client)

    @cached_property
    def top(self) -> AsyncTop:
        return AsyncTop(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLayer3WithRawResponse:
        return AsyncLayer3WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLayer3WithStreamingResponse:
        return AsyncLayer3WithStreamingResponse(self)

    async def timeseries(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[
            Literal[
                "1d",
                "2d",
                "7d",
                "14d",
                "28d",
                "12w",
                "24w",
                "52w",
                "1dControl",
                "2dControl",
                "7dControl",
                "14dControl",
                "28dControl",
                "12wControl",
                "24wControl",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        direction: Literal["ORIGIN", "TARGET"] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        metric: Literal["BYTES", "BYTES_OLD"] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        normalization: Literal["PERCENTAGE_CHANGE", "MIN0_MAX"] | NotGiven = NOT_GIVEN,
        protocol: List[Literal["UDP", "TCP", "ICMP", "GRE"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Layer3TimeseriesResponse:
        """
        Get attacks change over time by bytes.

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

          direction: Together with the `location` parameter, will apply the filter to origin or
              target location.

          format: Format results are returned in.

          ip_version: Filter for ip version.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          metric: Measurement units, eg. bytes.

          name: Array of names that will be used to name the series in responses.

          normalization: Normalization method applied. Refer to
              [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

          protocol: Array of L3/4 attack types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/attacks/layer3/timeseries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "asn": asn,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "direction": direction,
                        "format": format,
                        "ip_version": ip_version,
                        "location": location,
                        "metric": metric,
                        "name": name,
                        "normalization": normalization,
                        "protocol": protocol,
                    },
                    layer3_timeseries_params.Layer3TimeseriesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Layer3TimeseriesResponse], ResultWrapper[Layer3TimeseriesResponse]),
        )


class Layer3WithRawResponse:
    def __init__(self, layer3: Layer3) -> None:
        self._layer3 = layer3

        self.timeseries = to_raw_response_wrapper(
            layer3.timeseries,
        )

    @cached_property
    def summary(self) -> SummaryWithRawResponse:
        return SummaryWithRawResponse(self._layer3.summary)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsWithRawResponse:
        return TimeseriesGroupsWithRawResponse(self._layer3.timeseries_groups)

    @cached_property
    def top(self) -> TopWithRawResponse:
        return TopWithRawResponse(self._layer3.top)


class AsyncLayer3WithRawResponse:
    def __init__(self, layer3: AsyncLayer3) -> None:
        self._layer3 = layer3

        self.timeseries = async_to_raw_response_wrapper(
            layer3.timeseries,
        )

    @cached_property
    def summary(self) -> AsyncSummaryWithRawResponse:
        return AsyncSummaryWithRawResponse(self._layer3.summary)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsWithRawResponse:
        return AsyncTimeseriesGroupsWithRawResponse(self._layer3.timeseries_groups)

    @cached_property
    def top(self) -> AsyncTopWithRawResponse:
        return AsyncTopWithRawResponse(self._layer3.top)


class Layer3WithStreamingResponse:
    def __init__(self, layer3: Layer3) -> None:
        self._layer3 = layer3

        self.timeseries = to_streamed_response_wrapper(
            layer3.timeseries,
        )

    @cached_property
    def summary(self) -> SummaryWithStreamingResponse:
        return SummaryWithStreamingResponse(self._layer3.summary)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsWithStreamingResponse:
        return TimeseriesGroupsWithStreamingResponse(self._layer3.timeseries_groups)

    @cached_property
    def top(self) -> TopWithStreamingResponse:
        return TopWithStreamingResponse(self._layer3.top)


class AsyncLayer3WithStreamingResponse:
    def __init__(self, layer3: AsyncLayer3) -> None:
        self._layer3 = layer3

        self.timeseries = async_to_streamed_response_wrapper(
            layer3.timeseries,
        )

    @cached_property
    def summary(self) -> AsyncSummaryWithStreamingResponse:
        return AsyncSummaryWithStreamingResponse(self._layer3.summary)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsWithStreamingResponse:
        return AsyncTimeseriesGroupsWithStreamingResponse(self._layer3.timeseries_groups)

    @cached_property
    def top(self) -> AsyncTopWithStreamingResponse:
        return AsyncTopWithStreamingResponse(self._layer3.top)
