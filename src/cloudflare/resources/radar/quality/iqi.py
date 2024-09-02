# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.radar.quality.iqi_summary_response import IQISummaryResponse

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from ...._base_client import make_request_options

from typing import Type, List, Union

from typing_extensions import Literal

from datetime import datetime

from ....types.radar.quality.iqi_timeseries_groups_response import IQITimeseriesGroupsResponse

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.radar.quality import iqi_summary_params
from ....types.radar.quality import iqi_timeseries_groups_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["IQIResource", "AsyncIQIResource"]


class IQIResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IQIResourceWithRawResponse:
        return IQIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IQIResourceWithStreamingResponse:
        return IQIResourceWithStreamingResponse(self)

    def summary(
        self,
        *,
        metric: Literal["BANDWIDTH", "DNS", "LATENCY"],
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IQISummaryResponse:
        """
        Get a summary (percentiles) of bandwidth, latency or DNS response time from the
        Radar Internet Quality Index (IQI).

        Args:
          metric: Which metric to return: bandwidth, latency or DNS response time.

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
            "/radar/quality/iqi/summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "metric": metric,
                        "asn": asn,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "location": location,
                        "name": name,
                    },
                    iqi_summary_params.IQISummaryParams,
                ),
                post_parser=ResultWrapper[IQISummaryResponse]._unwrapper,
            ),
            cast_to=cast(Type[IQISummaryResponse], ResultWrapper[IQISummaryResponse]),
        )

    def timeseries_groups(
        self,
        *,
        metric: Literal["BANDWIDTH", "DNS", "LATENCY"],
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        interpolation: bool | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IQITimeseriesGroupsResponse:
        """
        Get a time series (percentiles) of bandwidth, latency or DNS response time from
        the Radar Internet Quality Index (IQI).

        Args:
          metric: Which metric to return: bandwidth, latency or DNS response time.

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

          interpolation: Enable interpolation for all series (using the average).

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
            "/radar/quality/iqi/timeseries_groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "metric": metric,
                        "agg_interval": agg_interval,
                        "asn": asn,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "interpolation": interpolation,
                        "location": location,
                        "name": name,
                    },
                    iqi_timeseries_groups_params.IQITimeseriesGroupsParams,
                ),
                post_parser=ResultWrapper[IQITimeseriesGroupsResponse]._unwrapper,
            ),
            cast_to=cast(Type[IQITimeseriesGroupsResponse], ResultWrapper[IQITimeseriesGroupsResponse]),
        )


class AsyncIQIResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIQIResourceWithRawResponse:
        return AsyncIQIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIQIResourceWithStreamingResponse:
        return AsyncIQIResourceWithStreamingResponse(self)

    async def summary(
        self,
        *,
        metric: Literal["BANDWIDTH", "DNS", "LATENCY"],
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IQISummaryResponse:
        """
        Get a summary (percentiles) of bandwidth, latency or DNS response time from the
        Radar Internet Quality Index (IQI).

        Args:
          metric: Which metric to return: bandwidth, latency or DNS response time.

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
            "/radar/quality/iqi/summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "metric": metric,
                        "asn": asn,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "location": location,
                        "name": name,
                    },
                    iqi_summary_params.IQISummaryParams,
                ),
                post_parser=ResultWrapper[IQISummaryResponse]._unwrapper,
            ),
            cast_to=cast(Type[IQISummaryResponse], ResultWrapper[IQISummaryResponse]),
        )

    async def timeseries_groups(
        self,
        *,
        metric: Literal["BANDWIDTH", "DNS", "LATENCY"],
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        interpolation: bool | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IQITimeseriesGroupsResponse:
        """
        Get a time series (percentiles) of bandwidth, latency or DNS response time from
        the Radar Internet Quality Index (IQI).

        Args:
          metric: Which metric to return: bandwidth, latency or DNS response time.

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

          interpolation: Enable interpolation for all series (using the average).

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
            "/radar/quality/iqi/timeseries_groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "metric": metric,
                        "agg_interval": agg_interval,
                        "asn": asn,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "interpolation": interpolation,
                        "location": location,
                        "name": name,
                    },
                    iqi_timeseries_groups_params.IQITimeseriesGroupsParams,
                ),
                post_parser=ResultWrapper[IQITimeseriesGroupsResponse]._unwrapper,
            ),
            cast_to=cast(Type[IQITimeseriesGroupsResponse], ResultWrapper[IQITimeseriesGroupsResponse]),
        )


class IQIResourceWithRawResponse:
    def __init__(self, iqi: IQIResource) -> None:
        self._iqi = iqi

        self.summary = to_raw_response_wrapper(
            iqi.summary,
        )
        self.timeseries_groups = to_raw_response_wrapper(
            iqi.timeseries_groups,
        )


class AsyncIQIResourceWithRawResponse:
    def __init__(self, iqi: AsyncIQIResource) -> None:
        self._iqi = iqi

        self.summary = async_to_raw_response_wrapper(
            iqi.summary,
        )
        self.timeseries_groups = async_to_raw_response_wrapper(
            iqi.timeseries_groups,
        )


class IQIResourceWithStreamingResponse:
    def __init__(self, iqi: IQIResource) -> None:
        self._iqi = iqi

        self.summary = to_streamed_response_wrapper(
            iqi.summary,
        )
        self.timeseries_groups = to_streamed_response_wrapper(
            iqi.timeseries_groups,
        )


class AsyncIQIResourceWithStreamingResponse:
    def __init__(self, iqi: AsyncIQIResource) -> None:
        self._iqi = iqi

        self.summary = async_to_streamed_response_wrapper(
            iqi.summary,
        )
        self.timeseries_groups = async_to_streamed_response_wrapper(
            iqi.timeseries_groups,
        )
