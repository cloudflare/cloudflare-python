# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .summary import (
    SummaryResource,
    AsyncSummaryResource,
    SummaryResourceWithRawResponse,
    AsyncSummaryResourceWithRawResponse,
    SummaryResourceWithStreamingResponse,
    AsyncSummaryResourceWithStreamingResponse,
)
from .top.top import (
    TopResource,
    AsyncTopResource,
    TopResourceWithRawResponse,
    AsyncTopResourceWithRawResponse,
    TopResourceWithStreamingResponse,
    AsyncTopResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from .timeseries_groups import (
    TimeseriesGroupsResource,
    AsyncTimeseriesGroupsResource,
    TimeseriesGroupsResourceWithRawResponse,
    AsyncTimeseriesGroupsResourceWithRawResponse,
    TimeseriesGroupsResourceWithStreamingResponse,
    AsyncTimeseriesGroupsResourceWithStreamingResponse,
)
from .....types.radar.attacks import (
    layer3_summary_v2_params,
    layer3_timeseries_params,
    layer3_timeseries_groups_v2_params,
)
from .....types.radar.attacks.layer3_summary_v2_response import Layer3SummaryV2Response
from .....types.radar.attacks.layer3_timeseries_response import Layer3TimeseriesResponse
from .....types.radar.attacks.layer3_timeseries_groups_v2_response import Layer3TimeseriesGroupsV2Response

__all__ = ["Layer3Resource", "AsyncLayer3Resource"]


class Layer3Resource(SyncAPIResource):
    @cached_property
    def summary(self) -> SummaryResource:
        return SummaryResource(self._client)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResource:
        return TimeseriesGroupsResource(self._client)

    @cached_property
    def top(self) -> TopResource:
        return TopResource(self._client)

    @cached_property
    def with_raw_response(self) -> Layer3ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return Layer3ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> Layer3ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return Layer3ResourceWithStreamingResponse(self)

    def summary_v2(
        self,
        dimension: Literal["PROTOCOL", "IP_VERSION", "VECTOR", "DURATION", "BITRATE", "VERTICAL", "INDUSTRY"],
        *,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        direction: Literal["ORIGIN", "TARGET"] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
        limit_per_group: int | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        protocol: List[Literal["UDP", "TCP", "ICMP", "GRE"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Layer3SummaryV2Response:
        """
        Retrieves the distribution of layer 3 attacks by the specified dimension.

        Args:
          dimension: Specifies the attribute by which to group the results.

          continent: Filters results by continent. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude continents from results. For example, `-EU,NA`
              excludes results from EU, but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          direction: Specifies whether the `location` filter applies to the source or target
              location.

          format: Format in which results will be returned.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          limit_per_group: Limits the number of objects per group to the top items within the specified
              time range. When item count exceeds the limit, extra items appear grouped under
              an "other" category.

          location: Filters results by location. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude locations from results. For example, `-US,PT`
              excludes results from the US, but includes results from PT.

          name: Array of names used to label the series in the response.

          protocol: Filters the results by layer 3/4 protocol.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return self._get(
            f"/radar/attacks/layer3/summary/{dimension}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "direction": direction,
                        "format": format,
                        "ip_version": ip_version,
                        "limit_per_group": limit_per_group,
                        "location": location,
                        "name": name,
                        "protocol": protocol,
                    },
                    layer3_summary_v2_params.Layer3SummaryV2Params,
                ),
                post_parser=ResultWrapper[Layer3SummaryV2Response]._unwrapper,
            ),
            cast_to=cast(Type[Layer3SummaryV2Response], ResultWrapper[Layer3SummaryV2Response]),
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
        direction: Literal["ORIGIN", "TARGET"] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        metric: Literal["BYTES", "BYTES_OLD"] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        normalization: Literal["PERCENTAGE_CHANGE", "MIN0_MAX"] | Omit = omit,
        protocol: List[Literal["UDP", "TCP", "ICMP", "GRE"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Layer3TimeseriesResponse:
        """
        Retrieves layer 3 attacks over time.

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

          direction: Specifies whether the `location` filter applies to the source or target
              location.

          format: Format in which results will be returned.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          location: Filters results by location. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude locations from results. For example, `-US,PT`
              excludes results from the US, but includes results from PT.

          metric: Measurement units, eg. bytes.

          name: Array of names used to label the series in the response.

          normalization: Normalization method applied to the results. Refer to
              [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

          protocol: Filters the results by layer 3/4 protocol.

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
                post_parser=ResultWrapper[Layer3TimeseriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[Layer3TimeseriesResponse], ResultWrapper[Layer3TimeseriesResponse]),
        )

    def timeseries_groups_v2(
        self,
        dimension: Literal["PROTOCOL", "IP_VERSION", "VECTOR", "DURATION", "BITRATE", "VERTICAL", "INDUSTRY"],
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        direction: Literal["ORIGIN", "TARGET"] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
        limit_per_group: int | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        normalization: Literal["PERCENTAGE", "MIN0_MAX"] | Omit = omit,
        protocol: List[Literal["UDP", "TCP", "ICMP", "GRE"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Layer3TimeseriesGroupsV2Response:
        """
        Retrieves the distribution of layer 3 attacks grouped by dimension over time.

        Args:
          dimension: Specifies the attribute by which to group the results.

          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          continent: Filters results by continent. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude continents from results. For example, `-EU,NA`
              excludes results from EU, but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          direction: Specifies whether the `location` filter applies to the source or target
              location.

          format: Format in which results will be returned.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          limit_per_group: Limits the number of objects per group to the top items within the specified
              time range. When item count exceeds the limit, extra items appear grouped under
              an "other" category.

          location: Filters results by location. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude locations from results. For example, `-US,PT`
              excludes results from the US, but includes results from PT.

          name: Array of names used to label the series in the response.

          normalization: Normalization method applied to the results. Refer to
              [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

          protocol: Filters the results by layer 3/4 protocol.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return self._get(
            f"/radar/attacks/layer3/timeseries_groups/{dimension}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "direction": direction,
                        "format": format,
                        "ip_version": ip_version,
                        "limit_per_group": limit_per_group,
                        "location": location,
                        "name": name,
                        "normalization": normalization,
                        "protocol": protocol,
                    },
                    layer3_timeseries_groups_v2_params.Layer3TimeseriesGroupsV2Params,
                ),
                post_parser=ResultWrapper[Layer3TimeseriesGroupsV2Response]._unwrapper,
            ),
            cast_to=cast(Type[Layer3TimeseriesGroupsV2Response], ResultWrapper[Layer3TimeseriesGroupsV2Response]),
        )


class AsyncLayer3Resource(AsyncAPIResource):
    @cached_property
    def summary(self) -> AsyncSummaryResource:
        return AsyncSummaryResource(self._client)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResource:
        return AsyncTimeseriesGroupsResource(self._client)

    @cached_property
    def top(self) -> AsyncTopResource:
        return AsyncTopResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLayer3ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLayer3ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLayer3ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncLayer3ResourceWithStreamingResponse(self)

    async def summary_v2(
        self,
        dimension: Literal["PROTOCOL", "IP_VERSION", "VECTOR", "DURATION", "BITRATE", "VERTICAL", "INDUSTRY"],
        *,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        direction: Literal["ORIGIN", "TARGET"] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
        limit_per_group: int | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        protocol: List[Literal["UDP", "TCP", "ICMP", "GRE"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Layer3SummaryV2Response:
        """
        Retrieves the distribution of layer 3 attacks by the specified dimension.

        Args:
          dimension: Specifies the attribute by which to group the results.

          continent: Filters results by continent. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude continents from results. For example, `-EU,NA`
              excludes results from EU, but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          direction: Specifies whether the `location` filter applies to the source or target
              location.

          format: Format in which results will be returned.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          limit_per_group: Limits the number of objects per group to the top items within the specified
              time range. When item count exceeds the limit, extra items appear grouped under
              an "other" category.

          location: Filters results by location. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude locations from results. For example, `-US,PT`
              excludes results from the US, but includes results from PT.

          name: Array of names used to label the series in the response.

          protocol: Filters the results by layer 3/4 protocol.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return await self._get(
            f"/radar/attacks/layer3/summary/{dimension}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "direction": direction,
                        "format": format,
                        "ip_version": ip_version,
                        "limit_per_group": limit_per_group,
                        "location": location,
                        "name": name,
                        "protocol": protocol,
                    },
                    layer3_summary_v2_params.Layer3SummaryV2Params,
                ),
                post_parser=ResultWrapper[Layer3SummaryV2Response]._unwrapper,
            ),
            cast_to=cast(Type[Layer3SummaryV2Response], ResultWrapper[Layer3SummaryV2Response]),
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
        direction: Literal["ORIGIN", "TARGET"] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        metric: Literal["BYTES", "BYTES_OLD"] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        normalization: Literal["PERCENTAGE_CHANGE", "MIN0_MAX"] | Omit = omit,
        protocol: List[Literal["UDP", "TCP", "ICMP", "GRE"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Layer3TimeseriesResponse:
        """
        Retrieves layer 3 attacks over time.

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

          direction: Specifies whether the `location` filter applies to the source or target
              location.

          format: Format in which results will be returned.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          location: Filters results by location. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude locations from results. For example, `-US,PT`
              excludes results from the US, but includes results from PT.

          metric: Measurement units, eg. bytes.

          name: Array of names used to label the series in the response.

          normalization: Normalization method applied to the results. Refer to
              [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

          protocol: Filters the results by layer 3/4 protocol.

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
                post_parser=ResultWrapper[Layer3TimeseriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[Layer3TimeseriesResponse], ResultWrapper[Layer3TimeseriesResponse]),
        )

    async def timeseries_groups_v2(
        self,
        dimension: Literal["PROTOCOL", "IP_VERSION", "VECTOR", "DURATION", "BITRATE", "VERTICAL", "INDUSTRY"],
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        direction: Literal["ORIGIN", "TARGET"] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
        limit_per_group: int | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        normalization: Literal["PERCENTAGE", "MIN0_MAX"] | Omit = omit,
        protocol: List[Literal["UDP", "TCP", "ICMP", "GRE"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Layer3TimeseriesGroupsV2Response:
        """
        Retrieves the distribution of layer 3 attacks grouped by dimension over time.

        Args:
          dimension: Specifies the attribute by which to group the results.

          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          continent: Filters results by continent. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude continents from results. For example, `-EU,NA`
              excludes results from EU, but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          direction: Specifies whether the `location` filter applies to the source or target
              location.

          format: Format in which results will be returned.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          limit_per_group: Limits the number of objects per group to the top items within the specified
              time range. When item count exceeds the limit, extra items appear grouped under
              an "other" category.

          location: Filters results by location. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude locations from results. For example, `-US,PT`
              excludes results from the US, but includes results from PT.

          name: Array of names used to label the series in the response.

          normalization: Normalization method applied to the results. Refer to
              [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

          protocol: Filters the results by layer 3/4 protocol.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return await self._get(
            f"/radar/attacks/layer3/timeseries_groups/{dimension}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "direction": direction,
                        "format": format,
                        "ip_version": ip_version,
                        "limit_per_group": limit_per_group,
                        "location": location,
                        "name": name,
                        "normalization": normalization,
                        "protocol": protocol,
                    },
                    layer3_timeseries_groups_v2_params.Layer3TimeseriesGroupsV2Params,
                ),
                post_parser=ResultWrapper[Layer3TimeseriesGroupsV2Response]._unwrapper,
            ),
            cast_to=cast(Type[Layer3TimeseriesGroupsV2Response], ResultWrapper[Layer3TimeseriesGroupsV2Response]),
        )


class Layer3ResourceWithRawResponse:
    def __init__(self, layer3: Layer3Resource) -> None:
        self._layer3 = layer3

        self.summary_v2 = to_raw_response_wrapper(
            layer3.summary_v2,
        )
        self.timeseries = to_raw_response_wrapper(
            layer3.timeseries,
        )
        self.timeseries_groups_v2 = to_raw_response_wrapper(
            layer3.timeseries_groups_v2,
        )

    @cached_property
    def summary(self) -> SummaryResourceWithRawResponse:
        return SummaryResourceWithRawResponse(self._layer3.summary)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResourceWithRawResponse:
        return TimeseriesGroupsResourceWithRawResponse(self._layer3.timeseries_groups)

    @cached_property
    def top(self) -> TopResourceWithRawResponse:
        return TopResourceWithRawResponse(self._layer3.top)


class AsyncLayer3ResourceWithRawResponse:
    def __init__(self, layer3: AsyncLayer3Resource) -> None:
        self._layer3 = layer3

        self.summary_v2 = async_to_raw_response_wrapper(
            layer3.summary_v2,
        )
        self.timeseries = async_to_raw_response_wrapper(
            layer3.timeseries,
        )
        self.timeseries_groups_v2 = async_to_raw_response_wrapper(
            layer3.timeseries_groups_v2,
        )

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithRawResponse:
        return AsyncSummaryResourceWithRawResponse(self._layer3.summary)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResourceWithRawResponse:
        return AsyncTimeseriesGroupsResourceWithRawResponse(self._layer3.timeseries_groups)

    @cached_property
    def top(self) -> AsyncTopResourceWithRawResponse:
        return AsyncTopResourceWithRawResponse(self._layer3.top)


class Layer3ResourceWithStreamingResponse:
    def __init__(self, layer3: Layer3Resource) -> None:
        self._layer3 = layer3

        self.summary_v2 = to_streamed_response_wrapper(
            layer3.summary_v2,
        )
        self.timeseries = to_streamed_response_wrapper(
            layer3.timeseries,
        )
        self.timeseries_groups_v2 = to_streamed_response_wrapper(
            layer3.timeseries_groups_v2,
        )

    @cached_property
    def summary(self) -> SummaryResourceWithStreamingResponse:
        return SummaryResourceWithStreamingResponse(self._layer3.summary)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResourceWithStreamingResponse:
        return TimeseriesGroupsResourceWithStreamingResponse(self._layer3.timeseries_groups)

    @cached_property
    def top(self) -> TopResourceWithStreamingResponse:
        return TopResourceWithStreamingResponse(self._layer3.top)


class AsyncLayer3ResourceWithStreamingResponse:
    def __init__(self, layer3: AsyncLayer3Resource) -> None:
        self._layer3 = layer3

        self.summary_v2 = async_to_streamed_response_wrapper(
            layer3.summary_v2,
        )
        self.timeseries = async_to_streamed_response_wrapper(
            layer3.timeseries,
        )
        self.timeseries_groups_v2 = async_to_streamed_response_wrapper(
            layer3.timeseries_groups_v2,
        )

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithStreamingResponse:
        return AsyncSummaryResourceWithStreamingResponse(self._layer3.summary)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResourceWithStreamingResponse:
        return AsyncTimeseriesGroupsResourceWithStreamingResponse(self._layer3.timeseries_groups)

    @cached_property
    def top(self) -> AsyncTopResourceWithStreamingResponse:
        return AsyncTopResourceWithStreamingResponse(self._layer3.top)
