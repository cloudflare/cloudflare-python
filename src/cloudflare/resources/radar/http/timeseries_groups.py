# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import List, Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

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
from ...._base_client import make_request_options
from ....types.radar.http import (
    timeseries_group_os_params,
    timeseries_group_browser_params,
    timeseries_group_bot_class_params,
    timeseries_group_ip_version_params,
    timeseries_group_device_type_params,
    timeseries_group_tls_version_params,
    timeseries_group_http_version_params,
    timeseries_group_post_quantum_params,
    timeseries_group_http_protocol_params,
    timeseries_group_browser_family_params,
)
from ....types.radar.http.timeseries_group_os_response import TimeseriesGroupOSResponse
from ....types.radar.http.timeseries_group_browser_response import TimeseriesGroupBrowserResponse
from ....types.radar.http.timeseries_group_bot_class_response import TimeseriesGroupBotClassResponse
from ....types.radar.http.timeseries_group_ip_version_response import TimeseriesGroupIPVersionResponse
from ....types.radar.http.timeseries_group_device_type_response import TimeseriesGroupDeviceTypeResponse
from ....types.radar.http.timeseries_group_tls_version_response import TimeseriesGroupTLSVersionResponse
from ....types.radar.http.timeseries_group_http_version_response import TimeseriesGroupHTTPVersionResponse
from ....types.radar.http.timeseries_group_post_quantum_response import TimeseriesGroupPostQuantumResponse
from ....types.radar.http.timeseries_group_http_protocol_response import TimeseriesGroupHTTPProtocolResponse
from ....types.radar.http.timeseries_group_browser_family_response import TimeseriesGroupBrowserFamilyResponse

__all__ = ["TimeseriesGroupsResource", "AsyncTimeseriesGroupsResource"]


class TimeseriesGroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TimeseriesGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TimeseriesGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TimeseriesGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TimeseriesGroupsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    def bot_class(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        asn: SequenceNotStr[str] | Omit = omit,
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
        os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | Omit = omit,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeseriesGroupBotClassResponse:
        """
        Retrieves the distribution of HTTP requests classified as automated or human
        over time. Visit https://developers.cloudflare.com/radar/concepts/bot-classes/
        for more information.

        Args:
          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Filters results by Autonomous System. Specify one or more Autonomous System
              Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from
              results. For example, `-174, 3356` excludes results from AS174, but includes
              results from AS3356.

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

          os: Filters results by operating system.

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/http/timeseries_groups/bot_class",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "asn": asn,
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
                        "os": os,
                        "tls_version": tls_version,
                    },
                    timeseries_group_bot_class_params.TimeseriesGroupBotClassParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupBotClassResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupBotClassResponse], ResultWrapper[TimeseriesGroupBotClassResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    def browser(
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
    ) -> TimeseriesGroupBrowserResponse:
        """
        Retrieves the distribution of HTTP requests by user agent over time.

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
        return self._get(
            "/radar/http/timeseries_groups/browser",
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
                        "limit_per_group": limit_per_group,
                        "location": location,
                        "name": name,
                        "os": os,
                        "tls_version": tls_version,
                    },
                    timeseries_group_browser_params.TimeseriesGroupBrowserParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupBrowserResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupBrowserResponse], ResultWrapper[TimeseriesGroupBrowserResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    def browser_family(
        self,
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
        os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | Omit = omit,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeseriesGroupBrowserFamilyResponse:
        """
        Retrieves the distribution of HTTP requests by user agent family over time.

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
        return self._get(
            "/radar/http/timeseries_groups/browser_family",
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
                        "os": os,
                        "tls_version": tls_version,
                    },
                    timeseries_group_browser_family_params.TimeseriesGroupBrowserFamilyParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupBrowserFamilyResponse]._unwrapper,
            ),
            cast_to=cast(
                Type[TimeseriesGroupBrowserFamilyResponse], ResultWrapper[TimeseriesGroupBrowserFamilyResponse]
            ),
        )

    @typing_extensions.deprecated("deprecated")
    def device_type(
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
        format: Literal["JSON", "CSV"] | Omit = omit,
        geo_id: SequenceNotStr[str] | Omit = omit,
        http_protocol: List[Literal["HTTP", "HTTPS"]] | Omit = omit,
        http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
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
    ) -> TimeseriesGroupDeviceTypeResponse:
        """
        Retrieves the distribution of HTTP requests by device type over time.

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

          os: Filters results by operating system.

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/http/timeseries_groups/device_type",
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
                        "format": format,
                        "geo_id": geo_id,
                        "http_protocol": http_protocol,
                        "http_version": http_version,
                        "ip_version": ip_version,
                        "location": location,
                        "name": name,
                        "os": os,
                        "tls_version": tls_version,
                    },
                    timeseries_group_device_type_params.TimeseriesGroupDeviceTypeParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupDeviceTypeResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupDeviceTypeResponse], ResultWrapper[TimeseriesGroupDeviceTypeResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    def http_protocol(
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
        http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
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
    ) -> TimeseriesGroupHTTPProtocolResponse:
        """Retrieves the distribution of HTTP requests by HTTP protocol (HTTP vs.

        HTTPS)
        over time.

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

          http_version: Filters results by HTTP version.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

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
        return self._get(
            "/radar/http/timeseries_groups/http_protocol",
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
                        "http_version": http_version,
                        "ip_version": ip_version,
                        "location": location,
                        "name": name,
                        "os": os,
                        "tls_version": tls_version,
                    },
                    timeseries_group_http_protocol_params.TimeseriesGroupHTTPProtocolParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupHTTPProtocolResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupHTTPProtocolResponse], ResultWrapper[TimeseriesGroupHTTPProtocolResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    def http_version(
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
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
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
    ) -> TimeseriesGroupHTTPVersionResponse:
        """
        Retrieves the distribution of HTTP requests by HTTP version over time.

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

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

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
        return self._get(
            "/radar/http/timeseries_groups/http_version",
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
                        "ip_version": ip_version,
                        "location": location,
                        "name": name,
                        "os": os,
                        "tls_version": tls_version,
                    },
                    timeseries_group_http_version_params.TimeseriesGroupHTTPVersionParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupHTTPVersionResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupHTTPVersionResponse], ResultWrapper[TimeseriesGroupHTTPVersionResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    def ip_version(
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
    ) -> TimeseriesGroupIPVersionResponse:
        """
        Retrieves the distribution of HTTP requests by IP version over time.

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
        return self._get(
            "/radar/http/timeseries_groups/ip_version",
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
                        "location": location,
                        "name": name,
                        "os": os,
                        "tls_version": tls_version,
                    },
                    timeseries_group_ip_version_params.TimeseriesGroupIPVersionParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupIPVersionResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupIPVersionResponse], ResultWrapper[TimeseriesGroupIPVersionResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    def os(
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
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeseriesGroupOSResponse:
        """
        Retrieves the distribution of HTTP requests by operating system over time.

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

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/http/timeseries_groups/os",
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
                        "tls_version": tls_version,
                    },
                    timeseries_group_os_params.TimeseriesGroupOSParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupOSResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupOSResponse], ResultWrapper[TimeseriesGroupOSResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    def post_quantum(
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
        os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | Omit = omit,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeseriesGroupPostQuantumResponse:
        """
        Retrieves the distribution of HTTP requests by post-quantum support over time.

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

          os: Filters results by operating system.

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/http/timeseries_groups/post_quantum",
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
                        "os": os,
                        "tls_version": tls_version,
                    },
                    timeseries_group_post_quantum_params.TimeseriesGroupPostQuantumParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupPostQuantumResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupPostQuantumResponse], ResultWrapper[TimeseriesGroupPostQuantumResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    def tls_version(
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
        os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeseriesGroupTLSVersionResponse:
        """
        Retrieves the distribution of HTTP requests by TLS version over time.

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

          os: Filters results by operating system.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/http/timeseries_groups/tls_version",
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
                        "os": os,
                    },
                    timeseries_group_tls_version_params.TimeseriesGroupTLSVersionParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupTLSVersionResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupTLSVersionResponse], ResultWrapper[TimeseriesGroupTLSVersionResponse]),
        )


class AsyncTimeseriesGroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTimeseriesGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTimeseriesGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTimeseriesGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTimeseriesGroupsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    async def bot_class(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        asn: SequenceNotStr[str] | Omit = omit,
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
        os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | Omit = omit,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeseriesGroupBotClassResponse:
        """
        Retrieves the distribution of HTTP requests classified as automated or human
        over time. Visit https://developers.cloudflare.com/radar/concepts/bot-classes/
        for more information.

        Args:
          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Filters results by Autonomous System. Specify one or more Autonomous System
              Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from
              results. For example, `-174, 3356` excludes results from AS174, but includes
              results from AS3356.

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

          os: Filters results by operating system.

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/http/timeseries_groups/bot_class",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "asn": asn,
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
                        "os": os,
                        "tls_version": tls_version,
                    },
                    timeseries_group_bot_class_params.TimeseriesGroupBotClassParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupBotClassResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupBotClassResponse], ResultWrapper[TimeseriesGroupBotClassResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    async def browser(
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
    ) -> TimeseriesGroupBrowserResponse:
        """
        Retrieves the distribution of HTTP requests by user agent over time.

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
        return await self._get(
            "/radar/http/timeseries_groups/browser",
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
                        "limit_per_group": limit_per_group,
                        "location": location,
                        "name": name,
                        "os": os,
                        "tls_version": tls_version,
                    },
                    timeseries_group_browser_params.TimeseriesGroupBrowserParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupBrowserResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupBrowserResponse], ResultWrapper[TimeseriesGroupBrowserResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    async def browser_family(
        self,
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
        os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | Omit = omit,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeseriesGroupBrowserFamilyResponse:
        """
        Retrieves the distribution of HTTP requests by user agent family over time.

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
        return await self._get(
            "/radar/http/timeseries_groups/browser_family",
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
                        "os": os,
                        "tls_version": tls_version,
                    },
                    timeseries_group_browser_family_params.TimeseriesGroupBrowserFamilyParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupBrowserFamilyResponse]._unwrapper,
            ),
            cast_to=cast(
                Type[TimeseriesGroupBrowserFamilyResponse], ResultWrapper[TimeseriesGroupBrowserFamilyResponse]
            ),
        )

    @typing_extensions.deprecated("deprecated")
    async def device_type(
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
        format: Literal["JSON", "CSV"] | Omit = omit,
        geo_id: SequenceNotStr[str] | Omit = omit,
        http_protocol: List[Literal["HTTP", "HTTPS"]] | Omit = omit,
        http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
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
    ) -> TimeseriesGroupDeviceTypeResponse:
        """
        Retrieves the distribution of HTTP requests by device type over time.

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

          os: Filters results by operating system.

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/http/timeseries_groups/device_type",
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
                        "format": format,
                        "geo_id": geo_id,
                        "http_protocol": http_protocol,
                        "http_version": http_version,
                        "ip_version": ip_version,
                        "location": location,
                        "name": name,
                        "os": os,
                        "tls_version": tls_version,
                    },
                    timeseries_group_device_type_params.TimeseriesGroupDeviceTypeParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupDeviceTypeResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupDeviceTypeResponse], ResultWrapper[TimeseriesGroupDeviceTypeResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    async def http_protocol(
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
        http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
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
    ) -> TimeseriesGroupHTTPProtocolResponse:
        """Retrieves the distribution of HTTP requests by HTTP protocol (HTTP vs.

        HTTPS)
        over time.

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

          http_version: Filters results by HTTP version.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

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
        return await self._get(
            "/radar/http/timeseries_groups/http_protocol",
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
                        "http_version": http_version,
                        "ip_version": ip_version,
                        "location": location,
                        "name": name,
                        "os": os,
                        "tls_version": tls_version,
                    },
                    timeseries_group_http_protocol_params.TimeseriesGroupHTTPProtocolParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupHTTPProtocolResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupHTTPProtocolResponse], ResultWrapper[TimeseriesGroupHTTPProtocolResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    async def http_version(
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
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
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
    ) -> TimeseriesGroupHTTPVersionResponse:
        """
        Retrieves the distribution of HTTP requests by HTTP version over time.

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

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

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
        return await self._get(
            "/radar/http/timeseries_groups/http_version",
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
                        "ip_version": ip_version,
                        "location": location,
                        "name": name,
                        "os": os,
                        "tls_version": tls_version,
                    },
                    timeseries_group_http_version_params.TimeseriesGroupHTTPVersionParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupHTTPVersionResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupHTTPVersionResponse], ResultWrapper[TimeseriesGroupHTTPVersionResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    async def ip_version(
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
    ) -> TimeseriesGroupIPVersionResponse:
        """
        Retrieves the distribution of HTTP requests by IP version over time.

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
        return await self._get(
            "/radar/http/timeseries_groups/ip_version",
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
                        "location": location,
                        "name": name,
                        "os": os,
                        "tls_version": tls_version,
                    },
                    timeseries_group_ip_version_params.TimeseriesGroupIPVersionParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupIPVersionResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupIPVersionResponse], ResultWrapper[TimeseriesGroupIPVersionResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    async def os(
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
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeseriesGroupOSResponse:
        """
        Retrieves the distribution of HTTP requests by operating system over time.

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

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/http/timeseries_groups/os",
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
                        "tls_version": tls_version,
                    },
                    timeseries_group_os_params.TimeseriesGroupOSParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupOSResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupOSResponse], ResultWrapper[TimeseriesGroupOSResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    async def post_quantum(
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
        os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | Omit = omit,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeseriesGroupPostQuantumResponse:
        """
        Retrieves the distribution of HTTP requests by post-quantum support over time.

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

          os: Filters results by operating system.

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/http/timeseries_groups/post_quantum",
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
                        "os": os,
                        "tls_version": tls_version,
                    },
                    timeseries_group_post_quantum_params.TimeseriesGroupPostQuantumParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupPostQuantumResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupPostQuantumResponse], ResultWrapper[TimeseriesGroupPostQuantumResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    async def tls_version(
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
        os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeseriesGroupTLSVersionResponse:
        """
        Retrieves the distribution of HTTP requests by TLS version over time.

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

          os: Filters results by operating system.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/http/timeseries_groups/tls_version",
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
                        "os": os,
                    },
                    timeseries_group_tls_version_params.TimeseriesGroupTLSVersionParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupTLSVersionResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupTLSVersionResponse], ResultWrapper[TimeseriesGroupTLSVersionResponse]),
        )


class TimeseriesGroupsResourceWithRawResponse:
    def __init__(self, timeseries_groups: TimeseriesGroupsResource) -> None:
        self._timeseries_groups = timeseries_groups

        self.bot_class = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                timeseries_groups.bot_class,  # pyright: ignore[reportDeprecated],
            )
        )
        self.browser = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                timeseries_groups.browser,  # pyright: ignore[reportDeprecated],
            )
        )
        self.browser_family = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                timeseries_groups.browser_family,  # pyright: ignore[reportDeprecated],
            )
        )
        self.device_type = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                timeseries_groups.device_type,  # pyright: ignore[reportDeprecated],
            )
        )
        self.http_protocol = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                timeseries_groups.http_protocol,  # pyright: ignore[reportDeprecated],
            )
        )
        self.http_version = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                timeseries_groups.http_version,  # pyright: ignore[reportDeprecated],
            )
        )
        self.ip_version = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                timeseries_groups.ip_version,  # pyright: ignore[reportDeprecated],
            )
        )
        self.os = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                timeseries_groups.os,  # pyright: ignore[reportDeprecated],
            )
        )
        self.post_quantum = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                timeseries_groups.post_quantum,  # pyright: ignore[reportDeprecated],
            )
        )
        self.tls_version = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                timeseries_groups.tls_version,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncTimeseriesGroupsResourceWithRawResponse:
    def __init__(self, timeseries_groups: AsyncTimeseriesGroupsResource) -> None:
        self._timeseries_groups = timeseries_groups

        self.bot_class = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                timeseries_groups.bot_class,  # pyright: ignore[reportDeprecated],
            )
        )
        self.browser = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                timeseries_groups.browser,  # pyright: ignore[reportDeprecated],
            )
        )
        self.browser_family = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                timeseries_groups.browser_family,  # pyright: ignore[reportDeprecated],
            )
        )
        self.device_type = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                timeseries_groups.device_type,  # pyright: ignore[reportDeprecated],
            )
        )
        self.http_protocol = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                timeseries_groups.http_protocol,  # pyright: ignore[reportDeprecated],
            )
        )
        self.http_version = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                timeseries_groups.http_version,  # pyright: ignore[reportDeprecated],
            )
        )
        self.ip_version = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                timeseries_groups.ip_version,  # pyright: ignore[reportDeprecated],
            )
        )
        self.os = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                timeseries_groups.os,  # pyright: ignore[reportDeprecated],
            )
        )
        self.post_quantum = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                timeseries_groups.post_quantum,  # pyright: ignore[reportDeprecated],
            )
        )
        self.tls_version = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                timeseries_groups.tls_version,  # pyright: ignore[reportDeprecated],
            )
        )


class TimeseriesGroupsResourceWithStreamingResponse:
    def __init__(self, timeseries_groups: TimeseriesGroupsResource) -> None:
        self._timeseries_groups = timeseries_groups

        self.bot_class = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                timeseries_groups.bot_class,  # pyright: ignore[reportDeprecated],
            )
        )
        self.browser = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                timeseries_groups.browser,  # pyright: ignore[reportDeprecated],
            )
        )
        self.browser_family = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                timeseries_groups.browser_family,  # pyright: ignore[reportDeprecated],
            )
        )
        self.device_type = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                timeseries_groups.device_type,  # pyright: ignore[reportDeprecated],
            )
        )
        self.http_protocol = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                timeseries_groups.http_protocol,  # pyright: ignore[reportDeprecated],
            )
        )
        self.http_version = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                timeseries_groups.http_version,  # pyright: ignore[reportDeprecated],
            )
        )
        self.ip_version = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                timeseries_groups.ip_version,  # pyright: ignore[reportDeprecated],
            )
        )
        self.os = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                timeseries_groups.os,  # pyright: ignore[reportDeprecated],
            )
        )
        self.post_quantum = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                timeseries_groups.post_quantum,  # pyright: ignore[reportDeprecated],
            )
        )
        self.tls_version = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                timeseries_groups.tls_version,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncTimeseriesGroupsResourceWithStreamingResponse:
    def __init__(self, timeseries_groups: AsyncTimeseriesGroupsResource) -> None:
        self._timeseries_groups = timeseries_groups

        self.bot_class = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                timeseries_groups.bot_class,  # pyright: ignore[reportDeprecated],
            )
        )
        self.browser = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                timeseries_groups.browser,  # pyright: ignore[reportDeprecated],
            )
        )
        self.browser_family = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                timeseries_groups.browser_family,  # pyright: ignore[reportDeprecated],
            )
        )
        self.device_type = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                timeseries_groups.device_type,  # pyright: ignore[reportDeprecated],
            )
        )
        self.http_protocol = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                timeseries_groups.http_protocol,  # pyright: ignore[reportDeprecated],
            )
        )
        self.http_version = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                timeseries_groups.http_version,  # pyright: ignore[reportDeprecated],
            )
        )
        self.ip_version = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                timeseries_groups.ip_version,  # pyright: ignore[reportDeprecated],
            )
        )
        self.os = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                timeseries_groups.os,  # pyright: ignore[reportDeprecated],
            )
        )
        self.post_quantum = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                timeseries_groups.post_quantum,  # pyright: ignore[reportDeprecated],
            )
        )
        self.tls_version = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                timeseries_groups.tls_version,  # pyright: ignore[reportDeprecated],
            )
        )
