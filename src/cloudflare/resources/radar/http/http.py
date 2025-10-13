# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from .summary import (
    SummaryResource,
    AsyncSummaryResource,
    SummaryResourceWithRawResponse,
    AsyncSummaryResourceWithRawResponse,
    SummaryResourceWithStreamingResponse,
    AsyncSummaryResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from .ases.ases import (
    AsesResource,
    AsyncAsesResource,
    AsesResourceWithRawResponse,
    AsyncAsesResourceWithRawResponse,
    AsesResourceWithStreamingResponse,
    AsyncAsesResourceWithStreamingResponse,
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
from ....types.radar import http_summary_v2_params, http_timeseries_params, http_timeseries_groups_v2_params
from ...._base_client import make_request_options
from .timeseries_groups import (
    TimeseriesGroupsResource,
    AsyncTimeseriesGroupsResource,
    TimeseriesGroupsResourceWithRawResponse,
    AsyncTimeseriesGroupsResourceWithRawResponse,
    TimeseriesGroupsResourceWithStreamingResponse,
    AsyncTimeseriesGroupsResourceWithStreamingResponse,
)
from .locations.locations import (
    LocationsResource,
    AsyncLocationsResource,
    LocationsResourceWithRawResponse,
    AsyncLocationsResourceWithRawResponse,
    LocationsResourceWithStreamingResponse,
    AsyncLocationsResourceWithStreamingResponse,
)
from ....types.radar.http_summary_v2_response import HTTPSummaryV2Response
from ....types.radar.http_timeseries_response import HTTPTimeseriesResponse
from ....types.radar.http_timeseries_groups_v2_response import HTTPTimeseriesGroupsV2Response

__all__ = ["HTTPResource", "AsyncHTTPResource"]


class HTTPResource(SyncAPIResource):
    @cached_property
    def locations(self) -> LocationsResource:
        return LocationsResource(self._client)

    @cached_property
    def ases(self) -> AsesResource:
        return AsesResource(self._client)

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
    def with_raw_response(self) -> HTTPResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return HTTPResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HTTPResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return HTTPResourceWithStreamingResponse(self)

    def summary_v2(
        self,
        dimension: Literal[
            "ADM1",
            "BOT_CLASS",
            "BROWSER",
            "BROWSER_FAMILY",
            "DEVICE_TYPE",
            "HTTP_PROTOCOL",
            "HTTP_VERSION",
            "IP_VERSION",
            "OS",
            "POST_QUANTUM",
            "TLS_VERSION",
        ],
        *,
        asn: SequenceNotStr[str] | Omit = omit,
        bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        device_type: List[Literal["DESKTOP", "MOBILE", "OTHER"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        geo_id: SequenceNotStr[str] | Omit = omit,
        http_protocol: List[Literal["HTTP", "HTTPS"]] | Omit = omit,
        http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
        limit_per_group: int | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | Omit = omit,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HTTPSummaryV2Response:
        """
        Retrieves the distribution of HTTP requests by the specified dimension.

        Args:
          dimension: Specifies the HTTP attribute by which to group the results.

          asn: Filters results by Autonomous System. Specify one or more Autonomous System
              Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from
              results. For example, `-174, 3356` excludes results from AS174, but includes
              results from AS3356.

          bot_class: Filters results by bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          continent: Filters results by continent. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude continents from results. For example, `-EU,NA`
              excludes results from EU, but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          device_type: Filters results by device type.

          format: Format in which results will be returned.

          geo_id: Filters results by Geolocation. Specify a comma-separated list of GeoNames IDs.
              Prefix with `-` to exclude geoIds from results. For example, `-2267056,360689`
              excludes results from the 2267056 (Lisbon), but includes results from 5128638
              (New York).

          http_protocol: Filters results by HTTP protocol (HTTP vs. HTTPS).

          http_version: Filters results by HTTP version.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          limit_per_group: Limits the number of objects per group to the top items within the specified
              time range. When item count exceeds the limit, extra items appear grouped under
              an "other" category.

          location: Filters results by location. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude locations from results. For example, `-US,PT`
              excludes results from the US, but includes results from PT.

          name: Array of names used to label the series in the response.

          os: Filters results by operating system.

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return self._get(
            f"/radar/http/summary/{dimension}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asn": asn,
                        "bot_class": bot_class,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "device_type": device_type,
                        "format": format,
                        "geo_id": geo_id,
                        "http_protocol": http_protocol,
                        "http_version": http_version,
                        "ip_version": ip_version,
                        "limit_per_group": limit_per_group,
                        "location": location,
                        "name": name,
                        "os": os,
                        "tls_version": tls_version,
                    },
                    http_summary_v2_params.HTTPSummaryV2Params,
                ),
                post_parser=ResultWrapper[HTTPSummaryV2Response]._unwrapper,
            ),
            cast_to=cast(Type[HTTPSummaryV2Response], ResultWrapper[HTTPSummaryV2Response]),
        )

    def timeseries(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        asn: SequenceNotStr[str] | Omit = omit,
        bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | Omit = omit,
        browser_family: List[Literal["CHROME", "EDGE", "FIREFOX", "SAFARI"]] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        device_type: List[Literal["DESKTOP", "MOBILE", "OTHER"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        geo_id: SequenceNotStr[str] | Omit = omit,
        http_protocol: List[Literal["HTTP", "HTTPS"]] | Omit = omit,
        http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        normalization: Literal["PERCENTAGE_CHANGE", "MIN0_MAX"] | Omit = omit,
        os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | Omit = omit,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HTTPTimeseriesResponse:
        """
        Retrieves the HTTP requests over time.

        Args:
          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Filters results by Autonomous System. Specify one or more Autonomous System
              Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from
              results. For example, `-174, 3356` excludes results from AS174, but includes
              results from AS3356.

          bot_class: Filters results by bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          browser_family: Filters results by browser family.

          continent: Filters results by continent. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude continents from results. For example, `-EU,NA`
              excludes results from EU, but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          device_type: Filters results by device type.

          format: Format in which results will be returned.

          geo_id: Filters results by Geolocation. Specify a comma-separated list of GeoNames IDs.
              Prefix with `-` to exclude geoIds from results. For example, `-2267056,360689`
              excludes results from the 2267056 (Lisbon), but includes results from 5128638
              (New York).

          http_protocol: Filters results by HTTP protocol (HTTP vs. HTTPS).

          http_version: Filters results by HTTP version.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          location: Filters results by location. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude locations from results. For example, `-US,PT`
              excludes results from the US, but includes results from PT.

          name: Array of names used to label the series in the response.

          normalization: Normalization method applied to the results. Refer to
              [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

          os: Filters results by operating system.

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/http/timeseries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "asn": asn,
                        "bot_class": bot_class,
                        "browser_family": browser_family,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "device_type": device_type,
                        "format": format,
                        "geo_id": geo_id,
                        "http_protocol": http_protocol,
                        "http_version": http_version,
                        "ip_version": ip_version,
                        "location": location,
                        "name": name,
                        "normalization": normalization,
                        "os": os,
                        "tls_version": tls_version,
                    },
                    http_timeseries_params.HTTPTimeseriesParams,
                ),
                post_parser=ResultWrapper[HTTPTimeseriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[HTTPTimeseriesResponse], ResultWrapper[HTTPTimeseriesResponse]),
        )

    def timeseries_groups_v2(
        self,
        dimension: Literal[
            "ADM1",
            "BOT_CLASS",
            "BROWSER",
            "BROWSER_FAMILY",
            "DEVICE_TYPE",
            "HTTP_PROTOCOL",
            "HTTP_VERSION",
            "IP_VERSION",
            "OS",
            "POST_QUANTUM",
            "TLS_VERSION",
        ],
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        asn: SequenceNotStr[str] | Omit = omit,
        bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        device_type: List[Literal["DESKTOP", "MOBILE", "OTHER"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        geo_id: SequenceNotStr[str] | Omit = omit,
        http_protocol: List[Literal["HTTP", "HTTPS"]] | Omit = omit,
        http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
        limit_per_group: int | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        normalization: Literal["PERCENTAGE", "MIN0_MAX"] | Omit = omit,
        os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | Omit = omit,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HTTPTimeseriesGroupsV2Response:
        """
        Retrieves the distribution of HTTP requests grouped by dimension.

        Args:
          dimension: Specifies the HTTP attribute by which to group the results.

          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Filters results by Autonomous System. Specify one or more Autonomous System
              Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from
              results. For example, `-174, 3356` excludes results from AS174, but includes
              results from AS3356.

          bot_class: Filters results by bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          continent: Filters results by continent. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude continents from results. For example, `-EU,NA`
              excludes results from EU, but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          device_type: Filters results by device type.

          format: Format in which results will be returned.

          geo_id: Filters results by Geolocation. Specify a comma-separated list of GeoNames IDs.
              Prefix with `-` to exclude geoIds from results. For example, `-2267056,360689`
              excludes results from the 2267056 (Lisbon), but includes results from 5128638
              (New York).

          http_protocol: Filters results by HTTP protocol (HTTP vs. HTTPS).

          http_version: Filters results by HTTP version.

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

          os: Filters results by operating system.

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return self._get(
            f"/radar/http/timeseries_groups/{dimension}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "asn": asn,
                        "bot_class": bot_class,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "device_type": device_type,
                        "format": format,
                        "geo_id": geo_id,
                        "http_protocol": http_protocol,
                        "http_version": http_version,
                        "ip_version": ip_version,
                        "limit_per_group": limit_per_group,
                        "location": location,
                        "name": name,
                        "normalization": normalization,
                        "os": os,
                        "tls_version": tls_version,
                    },
                    http_timeseries_groups_v2_params.HTTPTimeseriesGroupsV2Params,
                ),
                post_parser=ResultWrapper[HTTPTimeseriesGroupsV2Response]._unwrapper,
            ),
            cast_to=cast(Type[HTTPTimeseriesGroupsV2Response], ResultWrapper[HTTPTimeseriesGroupsV2Response]),
        )


class AsyncHTTPResource(AsyncAPIResource):
    @cached_property
    def locations(self) -> AsyncLocationsResource:
        return AsyncLocationsResource(self._client)

    @cached_property
    def ases(self) -> AsyncAsesResource:
        return AsyncAsesResource(self._client)

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
    def with_raw_response(self) -> AsyncHTTPResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHTTPResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHTTPResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncHTTPResourceWithStreamingResponse(self)

    async def summary_v2(
        self,
        dimension: Literal[
            "ADM1",
            "BOT_CLASS",
            "BROWSER",
            "BROWSER_FAMILY",
            "DEVICE_TYPE",
            "HTTP_PROTOCOL",
            "HTTP_VERSION",
            "IP_VERSION",
            "OS",
            "POST_QUANTUM",
            "TLS_VERSION",
        ],
        *,
        asn: SequenceNotStr[str] | Omit = omit,
        bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        device_type: List[Literal["DESKTOP", "MOBILE", "OTHER"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        geo_id: SequenceNotStr[str] | Omit = omit,
        http_protocol: List[Literal["HTTP", "HTTPS"]] | Omit = omit,
        http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
        limit_per_group: int | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | Omit = omit,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HTTPSummaryV2Response:
        """
        Retrieves the distribution of HTTP requests by the specified dimension.

        Args:
          dimension: Specifies the HTTP attribute by which to group the results.

          asn: Filters results by Autonomous System. Specify one or more Autonomous System
              Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from
              results. For example, `-174, 3356` excludes results from AS174, but includes
              results from AS3356.

          bot_class: Filters results by bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          continent: Filters results by continent. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude continents from results. For example, `-EU,NA`
              excludes results from EU, but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          device_type: Filters results by device type.

          format: Format in which results will be returned.

          geo_id: Filters results by Geolocation. Specify a comma-separated list of GeoNames IDs.
              Prefix with `-` to exclude geoIds from results. For example, `-2267056,360689`
              excludes results from the 2267056 (Lisbon), but includes results from 5128638
              (New York).

          http_protocol: Filters results by HTTP protocol (HTTP vs. HTTPS).

          http_version: Filters results by HTTP version.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          limit_per_group: Limits the number of objects per group to the top items within the specified
              time range. When item count exceeds the limit, extra items appear grouped under
              an "other" category.

          location: Filters results by location. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude locations from results. For example, `-US,PT`
              excludes results from the US, but includes results from PT.

          name: Array of names used to label the series in the response.

          os: Filters results by operating system.

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return await self._get(
            f"/radar/http/summary/{dimension}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asn": asn,
                        "bot_class": bot_class,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "device_type": device_type,
                        "format": format,
                        "geo_id": geo_id,
                        "http_protocol": http_protocol,
                        "http_version": http_version,
                        "ip_version": ip_version,
                        "limit_per_group": limit_per_group,
                        "location": location,
                        "name": name,
                        "os": os,
                        "tls_version": tls_version,
                    },
                    http_summary_v2_params.HTTPSummaryV2Params,
                ),
                post_parser=ResultWrapper[HTTPSummaryV2Response]._unwrapper,
            ),
            cast_to=cast(Type[HTTPSummaryV2Response], ResultWrapper[HTTPSummaryV2Response]),
        )

    async def timeseries(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        asn: SequenceNotStr[str] | Omit = omit,
        bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | Omit = omit,
        browser_family: List[Literal["CHROME", "EDGE", "FIREFOX", "SAFARI"]] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        device_type: List[Literal["DESKTOP", "MOBILE", "OTHER"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        geo_id: SequenceNotStr[str] | Omit = omit,
        http_protocol: List[Literal["HTTP", "HTTPS"]] | Omit = omit,
        http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        normalization: Literal["PERCENTAGE_CHANGE", "MIN0_MAX"] | Omit = omit,
        os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | Omit = omit,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HTTPTimeseriesResponse:
        """
        Retrieves the HTTP requests over time.

        Args:
          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Filters results by Autonomous System. Specify one or more Autonomous System
              Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from
              results. For example, `-174, 3356` excludes results from AS174, but includes
              results from AS3356.

          bot_class: Filters results by bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          browser_family: Filters results by browser family.

          continent: Filters results by continent. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude continents from results. For example, `-EU,NA`
              excludes results from EU, but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          device_type: Filters results by device type.

          format: Format in which results will be returned.

          geo_id: Filters results by Geolocation. Specify a comma-separated list of GeoNames IDs.
              Prefix with `-` to exclude geoIds from results. For example, `-2267056,360689`
              excludes results from the 2267056 (Lisbon), but includes results from 5128638
              (New York).

          http_protocol: Filters results by HTTP protocol (HTTP vs. HTTPS).

          http_version: Filters results by HTTP version.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          location: Filters results by location. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude locations from results. For example, `-US,PT`
              excludes results from the US, but includes results from PT.

          name: Array of names used to label the series in the response.

          normalization: Normalization method applied to the results. Refer to
              [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

          os: Filters results by operating system.

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/http/timeseries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "asn": asn,
                        "bot_class": bot_class,
                        "browser_family": browser_family,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "device_type": device_type,
                        "format": format,
                        "geo_id": geo_id,
                        "http_protocol": http_protocol,
                        "http_version": http_version,
                        "ip_version": ip_version,
                        "location": location,
                        "name": name,
                        "normalization": normalization,
                        "os": os,
                        "tls_version": tls_version,
                    },
                    http_timeseries_params.HTTPTimeseriesParams,
                ),
                post_parser=ResultWrapper[HTTPTimeseriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[HTTPTimeseriesResponse], ResultWrapper[HTTPTimeseriesResponse]),
        )

    async def timeseries_groups_v2(
        self,
        dimension: Literal[
            "ADM1",
            "BOT_CLASS",
            "BROWSER",
            "BROWSER_FAMILY",
            "DEVICE_TYPE",
            "HTTP_PROTOCOL",
            "HTTP_VERSION",
            "IP_VERSION",
            "OS",
            "POST_QUANTUM",
            "TLS_VERSION",
        ],
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        asn: SequenceNotStr[str] | Omit = omit,
        bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        device_type: List[Literal["DESKTOP", "MOBILE", "OTHER"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        geo_id: SequenceNotStr[str] | Omit = omit,
        http_protocol: List[Literal["HTTP", "HTTPS"]] | Omit = omit,
        http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
        limit_per_group: int | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        normalization: Literal["PERCENTAGE", "MIN0_MAX"] | Omit = omit,
        os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | Omit = omit,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HTTPTimeseriesGroupsV2Response:
        """
        Retrieves the distribution of HTTP requests grouped by dimension.

        Args:
          dimension: Specifies the HTTP attribute by which to group the results.

          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Filters results by Autonomous System. Specify one or more Autonomous System
              Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from
              results. For example, `-174, 3356` excludes results from AS174, but includes
              results from AS3356.

          bot_class: Filters results by bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          continent: Filters results by continent. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude continents from results. For example, `-EU,NA`
              excludes results from EU, but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          device_type: Filters results by device type.

          format: Format in which results will be returned.

          geo_id: Filters results by Geolocation. Specify a comma-separated list of GeoNames IDs.
              Prefix with `-` to exclude geoIds from results. For example, `-2267056,360689`
              excludes results from the 2267056 (Lisbon), but includes results from 5128638
              (New York).

          http_protocol: Filters results by HTTP protocol (HTTP vs. HTTPS).

          http_version: Filters results by HTTP version.

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

          os: Filters results by operating system.

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return await self._get(
            f"/radar/http/timeseries_groups/{dimension}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "asn": asn,
                        "bot_class": bot_class,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "device_type": device_type,
                        "format": format,
                        "geo_id": geo_id,
                        "http_protocol": http_protocol,
                        "http_version": http_version,
                        "ip_version": ip_version,
                        "limit_per_group": limit_per_group,
                        "location": location,
                        "name": name,
                        "normalization": normalization,
                        "os": os,
                        "tls_version": tls_version,
                    },
                    http_timeseries_groups_v2_params.HTTPTimeseriesGroupsV2Params,
                ),
                post_parser=ResultWrapper[HTTPTimeseriesGroupsV2Response]._unwrapper,
            ),
            cast_to=cast(Type[HTTPTimeseriesGroupsV2Response], ResultWrapper[HTTPTimeseriesGroupsV2Response]),
        )


class HTTPResourceWithRawResponse:
    def __init__(self, http: HTTPResource) -> None:
        self._http = http

        self.summary_v2 = to_raw_response_wrapper(
            http.summary_v2,
        )
        self.timeseries = to_raw_response_wrapper(
            http.timeseries,
        )
        self.timeseries_groups_v2 = to_raw_response_wrapper(
            http.timeseries_groups_v2,
        )

    @cached_property
    def locations(self) -> LocationsResourceWithRawResponse:
        return LocationsResourceWithRawResponse(self._http.locations)

    @cached_property
    def ases(self) -> AsesResourceWithRawResponse:
        return AsesResourceWithRawResponse(self._http.ases)

    @cached_property
    def summary(self) -> SummaryResourceWithRawResponse:
        return SummaryResourceWithRawResponse(self._http.summary)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResourceWithRawResponse:
        return TimeseriesGroupsResourceWithRawResponse(self._http.timeseries_groups)

    @cached_property
    def top(self) -> TopResourceWithRawResponse:
        return TopResourceWithRawResponse(self._http.top)


class AsyncHTTPResourceWithRawResponse:
    def __init__(self, http: AsyncHTTPResource) -> None:
        self._http = http

        self.summary_v2 = async_to_raw_response_wrapper(
            http.summary_v2,
        )
        self.timeseries = async_to_raw_response_wrapper(
            http.timeseries,
        )
        self.timeseries_groups_v2 = async_to_raw_response_wrapper(
            http.timeseries_groups_v2,
        )

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithRawResponse:
        return AsyncLocationsResourceWithRawResponse(self._http.locations)

    @cached_property
    def ases(self) -> AsyncAsesResourceWithRawResponse:
        return AsyncAsesResourceWithRawResponse(self._http.ases)

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithRawResponse:
        return AsyncSummaryResourceWithRawResponse(self._http.summary)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResourceWithRawResponse:
        return AsyncTimeseriesGroupsResourceWithRawResponse(self._http.timeseries_groups)

    @cached_property
    def top(self) -> AsyncTopResourceWithRawResponse:
        return AsyncTopResourceWithRawResponse(self._http.top)


class HTTPResourceWithStreamingResponse:
    def __init__(self, http: HTTPResource) -> None:
        self._http = http

        self.summary_v2 = to_streamed_response_wrapper(
            http.summary_v2,
        )
        self.timeseries = to_streamed_response_wrapper(
            http.timeseries,
        )
        self.timeseries_groups_v2 = to_streamed_response_wrapper(
            http.timeseries_groups_v2,
        )

    @cached_property
    def locations(self) -> LocationsResourceWithStreamingResponse:
        return LocationsResourceWithStreamingResponse(self._http.locations)

    @cached_property
    def ases(self) -> AsesResourceWithStreamingResponse:
        return AsesResourceWithStreamingResponse(self._http.ases)

    @cached_property
    def summary(self) -> SummaryResourceWithStreamingResponse:
        return SummaryResourceWithStreamingResponse(self._http.summary)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResourceWithStreamingResponse:
        return TimeseriesGroupsResourceWithStreamingResponse(self._http.timeseries_groups)

    @cached_property
    def top(self) -> TopResourceWithStreamingResponse:
        return TopResourceWithStreamingResponse(self._http.top)


class AsyncHTTPResourceWithStreamingResponse:
    def __init__(self, http: AsyncHTTPResource) -> None:
        self._http = http

        self.summary_v2 = async_to_streamed_response_wrapper(
            http.summary_v2,
        )
        self.timeseries = async_to_streamed_response_wrapper(
            http.timeseries,
        )
        self.timeseries_groups_v2 = async_to_streamed_response_wrapper(
            http.timeseries_groups_v2,
        )

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithStreamingResponse:
        return AsyncLocationsResourceWithStreamingResponse(self._http.locations)

    @cached_property
    def ases(self) -> AsyncAsesResourceWithStreamingResponse:
        return AsyncAsesResourceWithStreamingResponse(self._http.ases)

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithStreamingResponse:
        return AsyncSummaryResourceWithStreamingResponse(self._http.summary)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResourceWithStreamingResponse:
        return AsyncTimeseriesGroupsResourceWithStreamingResponse(self._http.timeseries_groups)

    @cached_property
    def top(self) -> AsyncTopResourceWithStreamingResponse:
        return AsyncTopResourceWithStreamingResponse(self._http.top)
