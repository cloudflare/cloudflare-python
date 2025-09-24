# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import List, Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .top import (
    TopResource,
    AsyncTopResource,
    TopResourceWithRawResponse,
    AsyncTopResourceWithRawResponse,
    TopResourceWithStreamingResponse,
    AsyncTopResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....types.radar import netflow_summary_params, netflow_timeseries_params
from ...._base_client import make_request_options
from ....types.radar.netflow_summary_response import NetflowSummaryResponse
from ....types.radar.netflow_timeseries_response import NetflowTimeseriesResponse

__all__ = ["NetflowsResource", "AsyncNetflowsResource"]


class NetflowsResource(SyncAPIResource):
    @cached_property
    def top(self) -> TopResource:
        return TopResource(self._client)

    @cached_property
    def with_raw_response(self) -> NetflowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return NetflowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NetflowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return NetflowsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    def summary(
        self,
        *,
        asn: SequenceNotStr[str] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        geo_id: SequenceNotStr[str] | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NetflowSummaryResponse:
        """
        Retrieves the distribution of network traffic (NetFlows) by HTTP vs other
        protocols.

        Args:
          asn: Filters results by Autonomous System. Specify one or more Autonomous System
              Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from
              results. For example, `-174, 3356` excludes results from AS174, but includes
              results from AS3356.

          continent: Filters results by continent. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude continents from results. For example, `-EU,NA`
              excludes results from EU, but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          geo_id: Filters results by Geolocation. Specify a comma-separated list of GeoNames IDs.
              Prefix with `-` to exclude geoIds from results. For example, `-2267056,360689`
              excludes results from the 2267056 (Lisbon), but includes results from 5128638
              (New York).

          location: Filters results by location. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude locations from results. For example, `-US,PT`
              excludes results from the US, but includes results from PT.

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/netflows/summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asn": asn,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "geo_id": geo_id,
                        "location": location,
                        "name": name,
                    },
                    netflow_summary_params.NetflowSummaryParams,
                ),
                post_parser=ResultWrapper[NetflowSummaryResponse]._unwrapper,
            ),
            cast_to=cast(Type[NetflowSummaryResponse], ResultWrapper[NetflowSummaryResponse]),
        )

    def timeseries(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        asn: SequenceNotStr[str] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        geo_id: SequenceNotStr[str] | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        normalization: Literal["PERCENTAGE_CHANGE", "MIN0_MAX"] | Omit = omit,
        product: List[Literal["HTTP", "ALL"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NetflowTimeseriesResponse:
        """
        Retrieves network traffic (NetFlows) over time.

        Args:
          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Filters results by Autonomous System. Specify one or more Autonomous System
              Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from
              results. For example, `-174, 3356` excludes results from AS174, but includes
              results from AS3356.

          continent: Filters results by continent. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude continents from results. For example, `-EU,NA`
              excludes results from EU, but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          geo_id: Filters results by Geolocation. Specify a comma-separated list of GeoNames IDs.
              Prefix with `-` to exclude geoIds from results. For example, `-2267056,360689`
              excludes results from the 2267056 (Lisbon), but includes results from 5128638
              (New York).

          location: Filters results by location. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude locations from results. For example, `-US,PT`
              excludes results from the US, but includes results from PT.

          name: Array of names used to label the series in the response.

          normalization: Normalization method applied to the results. Refer to
              [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

          product: Filters the results by network traffic product types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/netflows/timeseries",
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
                        "format": format,
                        "geo_id": geo_id,
                        "location": location,
                        "name": name,
                        "normalization": normalization,
                        "product": product,
                    },
                    netflow_timeseries_params.NetflowTimeseriesParams,
                ),
                post_parser=ResultWrapper[NetflowTimeseriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[NetflowTimeseriesResponse], ResultWrapper[NetflowTimeseriesResponse]),
        )


class AsyncNetflowsResource(AsyncAPIResource):
    @cached_property
    def top(self) -> AsyncTopResource:
        return AsyncTopResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNetflowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNetflowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNetflowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncNetflowsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    async def summary(
        self,
        *,
        asn: SequenceNotStr[str] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        geo_id: SequenceNotStr[str] | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NetflowSummaryResponse:
        """
        Retrieves the distribution of network traffic (NetFlows) by HTTP vs other
        protocols.

        Args:
          asn: Filters results by Autonomous System. Specify one or more Autonomous System
              Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from
              results. For example, `-174, 3356` excludes results from AS174, but includes
              results from AS3356.

          continent: Filters results by continent. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude continents from results. For example, `-EU,NA`
              excludes results from EU, but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          geo_id: Filters results by Geolocation. Specify a comma-separated list of GeoNames IDs.
              Prefix with `-` to exclude geoIds from results. For example, `-2267056,360689`
              excludes results from the 2267056 (Lisbon), but includes results from 5128638
              (New York).

          location: Filters results by location. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude locations from results. For example, `-US,PT`
              excludes results from the US, but includes results from PT.

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/netflows/summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asn": asn,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "geo_id": geo_id,
                        "location": location,
                        "name": name,
                    },
                    netflow_summary_params.NetflowSummaryParams,
                ),
                post_parser=ResultWrapper[NetflowSummaryResponse]._unwrapper,
            ),
            cast_to=cast(Type[NetflowSummaryResponse], ResultWrapper[NetflowSummaryResponse]),
        )

    async def timeseries(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        asn: SequenceNotStr[str] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        geo_id: SequenceNotStr[str] | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        normalization: Literal["PERCENTAGE_CHANGE", "MIN0_MAX"] | Omit = omit,
        product: List[Literal["HTTP", "ALL"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NetflowTimeseriesResponse:
        """
        Retrieves network traffic (NetFlows) over time.

        Args:
          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Filters results by Autonomous System. Specify one or more Autonomous System
              Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from
              results. For example, `-174, 3356` excludes results from AS174, but includes
              results from AS3356.

          continent: Filters results by continent. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude continents from results. For example, `-EU,NA`
              excludes results from EU, but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          geo_id: Filters results by Geolocation. Specify a comma-separated list of GeoNames IDs.
              Prefix with `-` to exclude geoIds from results. For example, `-2267056,360689`
              excludes results from the 2267056 (Lisbon), but includes results from 5128638
              (New York).

          location: Filters results by location. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude locations from results. For example, `-US,PT`
              excludes results from the US, but includes results from PT.

          name: Array of names used to label the series in the response.

          normalization: Normalization method applied to the results. Refer to
              [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

          product: Filters the results by network traffic product types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/netflows/timeseries",
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
                        "format": format,
                        "geo_id": geo_id,
                        "location": location,
                        "name": name,
                        "normalization": normalization,
                        "product": product,
                    },
                    netflow_timeseries_params.NetflowTimeseriesParams,
                ),
                post_parser=ResultWrapper[NetflowTimeseriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[NetflowTimeseriesResponse], ResultWrapper[NetflowTimeseriesResponse]),
        )


class NetflowsResourceWithRawResponse:
    def __init__(self, netflows: NetflowsResource) -> None:
        self._netflows = netflows

        self.summary = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                netflows.summary,  # pyright: ignore[reportDeprecated],
            )
        )
        self.timeseries = to_raw_response_wrapper(
            netflows.timeseries,
        )

    @cached_property
    def top(self) -> TopResourceWithRawResponse:
        return TopResourceWithRawResponse(self._netflows.top)


class AsyncNetflowsResourceWithRawResponse:
    def __init__(self, netflows: AsyncNetflowsResource) -> None:
        self._netflows = netflows

        self.summary = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                netflows.summary,  # pyright: ignore[reportDeprecated],
            )
        )
        self.timeseries = async_to_raw_response_wrapper(
            netflows.timeseries,
        )

    @cached_property
    def top(self) -> AsyncTopResourceWithRawResponse:
        return AsyncTopResourceWithRawResponse(self._netflows.top)


class NetflowsResourceWithStreamingResponse:
    def __init__(self, netflows: NetflowsResource) -> None:
        self._netflows = netflows

        self.summary = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                netflows.summary,  # pyright: ignore[reportDeprecated],
            )
        )
        self.timeseries = to_streamed_response_wrapper(
            netflows.timeseries,
        )

    @cached_property
    def top(self) -> TopResourceWithStreamingResponse:
        return TopResourceWithStreamingResponse(self._netflows.top)


class AsyncNetflowsResourceWithStreamingResponse:
    def __init__(self, netflows: AsyncNetflowsResource) -> None:
        self._netflows = netflows

        self.summary = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                netflows.summary,  # pyright: ignore[reportDeprecated],
            )
        )
        self.timeseries = async_to_streamed_response_wrapper(
            netflows.timeseries,
        )

    @cached_property
    def top(self) -> AsyncTopResourceWithStreamingResponse:
        return AsyncTopResourceWithStreamingResponse(self._netflows.top)
