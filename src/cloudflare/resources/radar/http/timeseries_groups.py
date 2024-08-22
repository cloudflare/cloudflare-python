# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.radar.http.timeseries_group_bot_class_response import TimeseriesGroupBotClassResponse

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from ...._base_client import make_request_options

from typing import Type, List, Union

from typing_extensions import Literal

from datetime import datetime

from ....types.radar.http.timeseries_group_browser_response import TimeseriesGroupBrowserResponse

from ....types.radar.http.timeseries_group_browser_family_response import TimeseriesGroupBrowserFamilyResponse

from ....types.radar.http.timeseries_group_device_type_response import TimeseriesGroupDeviceTypeResponse

from ....types.radar.http.timeseries_group_http_protocol_response import TimeseriesGroupHTTPProtocolResponse

from ....types.radar.http.timeseries_group_http_version_response import TimeseriesGroupHTTPVersionResponse

from ....types.radar.http.timeseries_group_ip_version_response import TimeseriesGroupIPVersionResponse

from ....types.radar.http.timeseries_group_os_response import TimeseriesGroupOSResponse

from ....types.radar.http.timeseries_group_post_quantum_response import TimeseriesGroupPostQuantumResponse

from ....types.radar.http.timeseries_group_tls_version_response import TimeseriesGroupTLSVersionResponse

from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.radar.http import timeseries_group_bot_class_params
from ....types.radar.http import timeseries_group_browser_params
from ....types.radar.http import timeseries_group_browser_family_params
from ....types.radar.http import timeseries_group_device_type_params
from ....types.radar.http import timeseries_group_http_protocol_params
from ....types.radar.http import timeseries_group_http_version_params
from ....types.radar.http import timeseries_group_ip_version_params
from ....types.radar.http import timeseries_group_os_params
from ....types.radar.http import timeseries_group_post_quantum_params
from ....types.radar.http import timeseries_group_tls_version_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["TimeseriesGroupsResource", "AsyncTimeseriesGroupsResource"]

class TimeseriesGroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TimeseriesGroupsResourceWithRawResponse:
        return TimeseriesGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TimeseriesGroupsResourceWithStreamingResponse:
        return TimeseriesGroupsResourceWithStreamingResponse(self)

    def bot_class(self,
    *,
    agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
    asn: List[str] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    date_range: List[str] | NotGiven = NOT_GIVEN,
    date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    device_type: List[Literal["DESKTOP", "MOBILE", "OTHER"]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    http_protocol: List[Literal["HTTP", "HTTPS"]] | NotGiven = NOT_GIVEN,
    http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
    ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | NotGiven = NOT_GIVEN,
    tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TimeseriesGroupBotClassResponse:
        """
        Get a time series of the percentage distribution of traffic classified as
        automated or human. Visit
        https://developers.cloudflare.com/radar/concepts/bot-classes/ for more
        information.

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

          device_type: Filter for device type.

          format: Format results are returned in.

          http_protocol: Filter for http protocol.

          http_version: Filter for http version.

          ip_version: Filter for ip version.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          os: Filter for os name.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/http/timeseries_groups/bot_class",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "agg_interval": agg_interval,
                "asn": asn,
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "device_type": device_type,
                "format": format,
                "http_protocol": http_protocol,
                "http_version": http_version,
                "ip_version": ip_version,
                "location": location,
                "name": name,
                "os": os,
                "tls_version": tls_version,
            }, timeseries_group_bot_class_params.TimeseriesGroupBotClassParams), post_parser=ResultWrapper[TimeseriesGroupBotClassResponse]._unwrapper),
            cast_to=cast(Type[TimeseriesGroupBotClassResponse], ResultWrapper[TimeseriesGroupBotClassResponse]),
        )

    def browser(self,
    *,
    agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
    asn: List[str] | NotGiven = NOT_GIVEN,
    bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    date_range: List[str] | NotGiven = NOT_GIVEN,
    date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    device_type: List[Literal["DESKTOP", "MOBILE", "OTHER"]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    http_protocol: List[Literal["HTTP", "HTTPS"]] | NotGiven = NOT_GIVEN,
    http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
    ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
    limit_per_group: int | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | NotGiven = NOT_GIVEN,
    tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TimeseriesGroupBrowserResponse:
        """
        Get a time series of the percentage distribution of traffic of the top user
        agents.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          bot_class: Filter for bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          device_type: Filter for device type.

          format: Format results are returned in.

          http_protocol: Filter for http protocol.

          http_version: Filter for http version.

          ip_version: Filter for ip version.

          limit_per_group: Limit the number of objects (eg browsers, verticals, etc) to the top items over
              the time range.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          os: Filter for os name.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/http/timeseries_groups/browser",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "agg_interval": agg_interval,
                "asn": asn,
                "bot_class": bot_class,
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "device_type": device_type,
                "format": format,
                "http_protocol": http_protocol,
                "http_version": http_version,
                "ip_version": ip_version,
                "limit_per_group": limit_per_group,
                "location": location,
                "name": name,
                "os": os,
                "tls_version": tls_version,
            }, timeseries_group_browser_params.TimeseriesGroupBrowserParams), post_parser=ResultWrapper[TimeseriesGroupBrowserResponse]._unwrapper),
            cast_to=cast(Type[TimeseriesGroupBrowserResponse], ResultWrapper[TimeseriesGroupBrowserResponse]),
        )

    def browser_family(self,
    *,
    agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
    asn: List[str] | NotGiven = NOT_GIVEN,
    bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    date_range: List[str] | NotGiven = NOT_GIVEN,
    date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    device_type: List[Literal["DESKTOP", "MOBILE", "OTHER"]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    http_protocol: List[Literal["HTTP", "HTTPS"]] | NotGiven = NOT_GIVEN,
    http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
    ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | NotGiven = NOT_GIVEN,
    tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TimeseriesGroupBrowserFamilyResponse:
        """
        Get a time series of the percentage distribution of traffic of the top user
        agents aggregated in families.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          bot_class: Filter for bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          device_type: Filter for device type.

          format: Format results are returned in.

          http_protocol: Filter for http protocol.

          http_version: Filter for http version.

          ip_version: Filter for ip version.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          os: Filter for os name.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/http/timeseries_groups/browser_family",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "agg_interval": agg_interval,
                "asn": asn,
                "bot_class": bot_class,
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "device_type": device_type,
                "format": format,
                "http_protocol": http_protocol,
                "http_version": http_version,
                "ip_version": ip_version,
                "location": location,
                "name": name,
                "os": os,
                "tls_version": tls_version,
            }, timeseries_group_browser_family_params.TimeseriesGroupBrowserFamilyParams), post_parser=ResultWrapper[TimeseriesGroupBrowserFamilyResponse]._unwrapper),
            cast_to=cast(Type[TimeseriesGroupBrowserFamilyResponse], ResultWrapper[TimeseriesGroupBrowserFamilyResponse]),
        )

    def device_type(self,
    *,
    agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
    asn: List[str] | NotGiven = NOT_GIVEN,
    bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    date_range: List[str] | NotGiven = NOT_GIVEN,
    date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    http_protocol: List[Literal["HTTP", "HTTPS"]] | NotGiven = NOT_GIVEN,
    http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
    ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | NotGiven = NOT_GIVEN,
    tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TimeseriesGroupDeviceTypeResponse:
        """
        Get a time series of the percentage distribution of traffic per device type.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          bot_class: Filter for bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          http_protocol: Filter for http protocol.

          http_version: Filter for http version.

          ip_version: Filter for ip version.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          os: Filter for os name.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/http/timeseries_groups/device_type",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "agg_interval": agg_interval,
                "asn": asn,
                "bot_class": bot_class,
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "format": format,
                "http_protocol": http_protocol,
                "http_version": http_version,
                "ip_version": ip_version,
                "location": location,
                "name": name,
                "os": os,
                "tls_version": tls_version,
            }, timeseries_group_device_type_params.TimeseriesGroupDeviceTypeParams), post_parser=ResultWrapper[TimeseriesGroupDeviceTypeResponse]._unwrapper),
            cast_to=cast(Type[TimeseriesGroupDeviceTypeResponse], ResultWrapper[TimeseriesGroupDeviceTypeResponse]),
        )

    def http_protocol(self,
    *,
    agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
    asn: List[str] | NotGiven = NOT_GIVEN,
    bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    date_range: List[str] | NotGiven = NOT_GIVEN,
    date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    device_type: List[Literal["DESKTOP", "MOBILE", "OTHER"]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
    ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | NotGiven = NOT_GIVEN,
    tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TimeseriesGroupHTTPProtocolResponse:
        """
        Get a time series of the percentage distribution of traffic per HTTP protocol.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          bot_class: Filter for bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          device_type: Filter for device type.

          format: Format results are returned in.

          http_version: Filter for http version.

          ip_version: Filter for ip version.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          os: Filter for os name.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/http/timeseries_groups/http_protocol",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "agg_interval": agg_interval,
                "asn": asn,
                "bot_class": bot_class,
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "device_type": device_type,
                "format": format,
                "http_version": http_version,
                "ip_version": ip_version,
                "location": location,
                "name": name,
                "os": os,
                "tls_version": tls_version,
            }, timeseries_group_http_protocol_params.TimeseriesGroupHTTPProtocolParams), post_parser=ResultWrapper[TimeseriesGroupHTTPProtocolResponse]._unwrapper),
            cast_to=cast(Type[TimeseriesGroupHTTPProtocolResponse], ResultWrapper[TimeseriesGroupHTTPProtocolResponse]),
        )

    def http_version(self,
    *,
    agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
    asn: List[str] | NotGiven = NOT_GIVEN,
    bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    date_range: List[str] | NotGiven = NOT_GIVEN,
    date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    device_type: List[Literal["DESKTOP", "MOBILE", "OTHER"]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    http_protocol: List[Literal["HTTP", "HTTPS"]] | NotGiven = NOT_GIVEN,
    ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | NotGiven = NOT_GIVEN,
    tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TimeseriesGroupHTTPVersionResponse:
        """
        Get a time series of the percentage distribution of traffic per HTTP protocol
        version.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          bot_class: Filter for bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          device_type: Filter for device type.

          format: Format results are returned in.

          http_protocol: Filter for http protocol.

          ip_version: Filter for ip version.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          os: Filter for os name.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/http/timeseries_groups/http_version",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "agg_interval": agg_interval,
                "asn": asn,
                "bot_class": bot_class,
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "device_type": device_type,
                "format": format,
                "http_protocol": http_protocol,
                "ip_version": ip_version,
                "location": location,
                "name": name,
                "os": os,
                "tls_version": tls_version,
            }, timeseries_group_http_version_params.TimeseriesGroupHTTPVersionParams), post_parser=ResultWrapper[TimeseriesGroupHTTPVersionResponse]._unwrapper),
            cast_to=cast(Type[TimeseriesGroupHTTPVersionResponse], ResultWrapper[TimeseriesGroupHTTPVersionResponse]),
        )

    def ip_version(self,
    *,
    agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
    asn: List[str] | NotGiven = NOT_GIVEN,
    bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    date_range: List[str] | NotGiven = NOT_GIVEN,
    date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    device_type: List[Literal["DESKTOP", "MOBILE", "OTHER"]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    http_protocol: List[Literal["HTTP", "HTTPS"]] | NotGiven = NOT_GIVEN,
    http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | NotGiven = NOT_GIVEN,
    tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TimeseriesGroupIPVersionResponse:
        """
        Get a time series of the percentage distribution of traffic per IP protocol
        version.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          bot_class: Filter for bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          device_type: Filter for device type.

          format: Format results are returned in.

          http_protocol: Filter for http protocol.

          http_version: Filter for http version.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          os: Filter for os name.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/http/timeseries_groups/ip_version",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "agg_interval": agg_interval,
                "asn": asn,
                "bot_class": bot_class,
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "device_type": device_type,
                "format": format,
                "http_protocol": http_protocol,
                "http_version": http_version,
                "location": location,
                "name": name,
                "os": os,
                "tls_version": tls_version,
            }, timeseries_group_ip_version_params.TimeseriesGroupIPVersionParams), post_parser=ResultWrapper[TimeseriesGroupIPVersionResponse]._unwrapper),
            cast_to=cast(Type[TimeseriesGroupIPVersionResponse], ResultWrapper[TimeseriesGroupIPVersionResponse]),
        )

    def os(self,
    *,
    agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
    asn: List[str] | NotGiven = NOT_GIVEN,
    bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    date_range: List[str] | NotGiven = NOT_GIVEN,
    date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    device_type: List[Literal["DESKTOP", "MOBILE", "OTHER"]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    http_protocol: List[Literal["HTTP", "HTTPS"]] | NotGiven = NOT_GIVEN,
    http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
    ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TimeseriesGroupOSResponse:
        """
        Get a time series of the percentage distribution of traffic of the top operating
        systems.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          bot_class: Filter for bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          device_type: Filter for device type.

          format: Format results are returned in.

          http_protocol: Filter for http protocol.

          http_version: Filter for http version.

          ip_version: Filter for ip version.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/http/timeseries_groups/os",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "agg_interval": agg_interval,
                "asn": asn,
                "bot_class": bot_class,
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "device_type": device_type,
                "format": format,
                "http_protocol": http_protocol,
                "http_version": http_version,
                "ip_version": ip_version,
                "location": location,
                "name": name,
                "tls_version": tls_version,
            }, timeseries_group_os_params.TimeseriesGroupOSParams), post_parser=ResultWrapper[TimeseriesGroupOSResponse]._unwrapper),
            cast_to=cast(Type[TimeseriesGroupOSResponse], ResultWrapper[TimeseriesGroupOSResponse]),
        )

    def post_quantum(self,
    *,
    agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
    asn: List[str] | NotGiven = NOT_GIVEN,
    bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    date_range: List[str] | NotGiven = NOT_GIVEN,
    date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    device_type: List[Literal["DESKTOP", "MOBILE", "OTHER"]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    http_protocol: List[Literal["HTTP", "HTTPS"]] | NotGiven = NOT_GIVEN,
    http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
    ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | NotGiven = NOT_GIVEN,
    tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TimeseriesGroupPostQuantumResponse:
        """
        Get a time series of the percentage distribution of traffic per Post Quantum
        suport.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          bot_class: Filter for bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          device_type: Filter for device type.

          format: Format results are returned in.

          http_protocol: Filter for http protocol.

          http_version: Filter for http version.

          ip_version: Filter for ip version.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          os: Filter for os name.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/http/timeseries_groups/post_quantum",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "agg_interval": agg_interval,
                "asn": asn,
                "bot_class": bot_class,
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "device_type": device_type,
                "format": format,
                "http_protocol": http_protocol,
                "http_version": http_version,
                "ip_version": ip_version,
                "location": location,
                "name": name,
                "os": os,
                "tls_version": tls_version,
            }, timeseries_group_post_quantum_params.TimeseriesGroupPostQuantumParams), post_parser=ResultWrapper[TimeseriesGroupPostQuantumResponse]._unwrapper),
            cast_to=cast(Type[TimeseriesGroupPostQuantumResponse], ResultWrapper[TimeseriesGroupPostQuantumResponse]),
        )

    def tls_version(self,
    *,
    agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
    asn: List[str] | NotGiven = NOT_GIVEN,
    bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    date_range: List[str] | NotGiven = NOT_GIVEN,
    date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    device_type: List[Literal["DESKTOP", "MOBILE", "OTHER"]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    http_protocol: List[Literal["HTTP", "HTTPS"]] | NotGiven = NOT_GIVEN,
    http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
    ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TimeseriesGroupTLSVersionResponse:
        """
        Get a time series of the percentage distribution of traffic per TLS protocol
        version.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          bot_class: Filter for bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          device_type: Filter for device type.

          format: Format results are returned in.

          http_protocol: Filter for http protocol.

          http_version: Filter for http version.

          ip_version: Filter for ip version.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          os: Filter for os name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/http/timeseries_groups/tls_version",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "agg_interval": agg_interval,
                "asn": asn,
                "bot_class": bot_class,
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "device_type": device_type,
                "format": format,
                "http_protocol": http_protocol,
                "http_version": http_version,
                "ip_version": ip_version,
                "location": location,
                "name": name,
                "os": os,
            }, timeseries_group_tls_version_params.TimeseriesGroupTLSVersionParams), post_parser=ResultWrapper[TimeseriesGroupTLSVersionResponse]._unwrapper),
            cast_to=cast(Type[TimeseriesGroupTLSVersionResponse], ResultWrapper[TimeseriesGroupTLSVersionResponse]),
        )

class AsyncTimeseriesGroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTimeseriesGroupsResourceWithRawResponse:
        return AsyncTimeseriesGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTimeseriesGroupsResourceWithStreamingResponse:
        return AsyncTimeseriesGroupsResourceWithStreamingResponse(self)

    async def bot_class(self,
    *,
    agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
    asn: List[str] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    date_range: List[str] | NotGiven = NOT_GIVEN,
    date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    device_type: List[Literal["DESKTOP", "MOBILE", "OTHER"]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    http_protocol: List[Literal["HTTP", "HTTPS"]] | NotGiven = NOT_GIVEN,
    http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
    ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | NotGiven = NOT_GIVEN,
    tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TimeseriesGroupBotClassResponse:
        """
        Get a time series of the percentage distribution of traffic classified as
        automated or human. Visit
        https://developers.cloudflare.com/radar/concepts/bot-classes/ for more
        information.

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

          device_type: Filter for device type.

          format: Format results are returned in.

          http_protocol: Filter for http protocol.

          http_version: Filter for http version.

          ip_version: Filter for ip version.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          os: Filter for os name.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/http/timeseries_groups/bot_class",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "agg_interval": agg_interval,
                "asn": asn,
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "device_type": device_type,
                "format": format,
                "http_protocol": http_protocol,
                "http_version": http_version,
                "ip_version": ip_version,
                "location": location,
                "name": name,
                "os": os,
                "tls_version": tls_version,
            }, timeseries_group_bot_class_params.TimeseriesGroupBotClassParams), post_parser=ResultWrapper[TimeseriesGroupBotClassResponse]._unwrapper),
            cast_to=cast(Type[TimeseriesGroupBotClassResponse], ResultWrapper[TimeseriesGroupBotClassResponse]),
        )

    async def browser(self,
    *,
    agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
    asn: List[str] | NotGiven = NOT_GIVEN,
    bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    date_range: List[str] | NotGiven = NOT_GIVEN,
    date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    device_type: List[Literal["DESKTOP", "MOBILE", "OTHER"]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    http_protocol: List[Literal["HTTP", "HTTPS"]] | NotGiven = NOT_GIVEN,
    http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
    ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
    limit_per_group: int | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | NotGiven = NOT_GIVEN,
    tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TimeseriesGroupBrowserResponse:
        """
        Get a time series of the percentage distribution of traffic of the top user
        agents.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          bot_class: Filter for bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          device_type: Filter for device type.

          format: Format results are returned in.

          http_protocol: Filter for http protocol.

          http_version: Filter for http version.

          ip_version: Filter for ip version.

          limit_per_group: Limit the number of objects (eg browsers, verticals, etc) to the top items over
              the time range.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          os: Filter for os name.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/http/timeseries_groups/browser",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "agg_interval": agg_interval,
                "asn": asn,
                "bot_class": bot_class,
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "device_type": device_type,
                "format": format,
                "http_protocol": http_protocol,
                "http_version": http_version,
                "ip_version": ip_version,
                "limit_per_group": limit_per_group,
                "location": location,
                "name": name,
                "os": os,
                "tls_version": tls_version,
            }, timeseries_group_browser_params.TimeseriesGroupBrowserParams), post_parser=ResultWrapper[TimeseriesGroupBrowserResponse]._unwrapper),
            cast_to=cast(Type[TimeseriesGroupBrowserResponse], ResultWrapper[TimeseriesGroupBrowserResponse]),
        )

    async def browser_family(self,
    *,
    agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
    asn: List[str] | NotGiven = NOT_GIVEN,
    bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    date_range: List[str] | NotGiven = NOT_GIVEN,
    date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    device_type: List[Literal["DESKTOP", "MOBILE", "OTHER"]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    http_protocol: List[Literal["HTTP", "HTTPS"]] | NotGiven = NOT_GIVEN,
    http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
    ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | NotGiven = NOT_GIVEN,
    tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TimeseriesGroupBrowserFamilyResponse:
        """
        Get a time series of the percentage distribution of traffic of the top user
        agents aggregated in families.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          bot_class: Filter for bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          device_type: Filter for device type.

          format: Format results are returned in.

          http_protocol: Filter for http protocol.

          http_version: Filter for http version.

          ip_version: Filter for ip version.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          os: Filter for os name.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/http/timeseries_groups/browser_family",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "agg_interval": agg_interval,
                "asn": asn,
                "bot_class": bot_class,
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "device_type": device_type,
                "format": format,
                "http_protocol": http_protocol,
                "http_version": http_version,
                "ip_version": ip_version,
                "location": location,
                "name": name,
                "os": os,
                "tls_version": tls_version,
            }, timeseries_group_browser_family_params.TimeseriesGroupBrowserFamilyParams), post_parser=ResultWrapper[TimeseriesGroupBrowserFamilyResponse]._unwrapper),
            cast_to=cast(Type[TimeseriesGroupBrowserFamilyResponse], ResultWrapper[TimeseriesGroupBrowserFamilyResponse]),
        )

    async def device_type(self,
    *,
    agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
    asn: List[str] | NotGiven = NOT_GIVEN,
    bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    date_range: List[str] | NotGiven = NOT_GIVEN,
    date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    http_protocol: List[Literal["HTTP", "HTTPS"]] | NotGiven = NOT_GIVEN,
    http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
    ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | NotGiven = NOT_GIVEN,
    tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TimeseriesGroupDeviceTypeResponse:
        """
        Get a time series of the percentage distribution of traffic per device type.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          bot_class: Filter for bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          http_protocol: Filter for http protocol.

          http_version: Filter for http version.

          ip_version: Filter for ip version.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          os: Filter for os name.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/http/timeseries_groups/device_type",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "agg_interval": agg_interval,
                "asn": asn,
                "bot_class": bot_class,
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "format": format,
                "http_protocol": http_protocol,
                "http_version": http_version,
                "ip_version": ip_version,
                "location": location,
                "name": name,
                "os": os,
                "tls_version": tls_version,
            }, timeseries_group_device_type_params.TimeseriesGroupDeviceTypeParams), post_parser=ResultWrapper[TimeseriesGroupDeviceTypeResponse]._unwrapper),
            cast_to=cast(Type[TimeseriesGroupDeviceTypeResponse], ResultWrapper[TimeseriesGroupDeviceTypeResponse]),
        )

    async def http_protocol(self,
    *,
    agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
    asn: List[str] | NotGiven = NOT_GIVEN,
    bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    date_range: List[str] | NotGiven = NOT_GIVEN,
    date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    device_type: List[Literal["DESKTOP", "MOBILE", "OTHER"]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
    ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | NotGiven = NOT_GIVEN,
    tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TimeseriesGroupHTTPProtocolResponse:
        """
        Get a time series of the percentage distribution of traffic per HTTP protocol.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          bot_class: Filter for bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          device_type: Filter for device type.

          format: Format results are returned in.

          http_version: Filter for http version.

          ip_version: Filter for ip version.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          os: Filter for os name.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/http/timeseries_groups/http_protocol",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "agg_interval": agg_interval,
                "asn": asn,
                "bot_class": bot_class,
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "device_type": device_type,
                "format": format,
                "http_version": http_version,
                "ip_version": ip_version,
                "location": location,
                "name": name,
                "os": os,
                "tls_version": tls_version,
            }, timeseries_group_http_protocol_params.TimeseriesGroupHTTPProtocolParams), post_parser=ResultWrapper[TimeseriesGroupHTTPProtocolResponse]._unwrapper),
            cast_to=cast(Type[TimeseriesGroupHTTPProtocolResponse], ResultWrapper[TimeseriesGroupHTTPProtocolResponse]),
        )

    async def http_version(self,
    *,
    agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
    asn: List[str] | NotGiven = NOT_GIVEN,
    bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    date_range: List[str] | NotGiven = NOT_GIVEN,
    date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    device_type: List[Literal["DESKTOP", "MOBILE", "OTHER"]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    http_protocol: List[Literal["HTTP", "HTTPS"]] | NotGiven = NOT_GIVEN,
    ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | NotGiven = NOT_GIVEN,
    tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TimeseriesGroupHTTPVersionResponse:
        """
        Get a time series of the percentage distribution of traffic per HTTP protocol
        version.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          bot_class: Filter for bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          device_type: Filter for device type.

          format: Format results are returned in.

          http_protocol: Filter for http protocol.

          ip_version: Filter for ip version.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          os: Filter for os name.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/http/timeseries_groups/http_version",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "agg_interval": agg_interval,
                "asn": asn,
                "bot_class": bot_class,
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "device_type": device_type,
                "format": format,
                "http_protocol": http_protocol,
                "ip_version": ip_version,
                "location": location,
                "name": name,
                "os": os,
                "tls_version": tls_version,
            }, timeseries_group_http_version_params.TimeseriesGroupHTTPVersionParams), post_parser=ResultWrapper[TimeseriesGroupHTTPVersionResponse]._unwrapper),
            cast_to=cast(Type[TimeseriesGroupHTTPVersionResponse], ResultWrapper[TimeseriesGroupHTTPVersionResponse]),
        )

    async def ip_version(self,
    *,
    agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
    asn: List[str] | NotGiven = NOT_GIVEN,
    bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    date_range: List[str] | NotGiven = NOT_GIVEN,
    date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    device_type: List[Literal["DESKTOP", "MOBILE", "OTHER"]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    http_protocol: List[Literal["HTTP", "HTTPS"]] | NotGiven = NOT_GIVEN,
    http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | NotGiven = NOT_GIVEN,
    tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TimeseriesGroupIPVersionResponse:
        """
        Get a time series of the percentage distribution of traffic per IP protocol
        version.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          bot_class: Filter for bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          device_type: Filter for device type.

          format: Format results are returned in.

          http_protocol: Filter for http protocol.

          http_version: Filter for http version.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          os: Filter for os name.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/http/timeseries_groups/ip_version",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "agg_interval": agg_interval,
                "asn": asn,
                "bot_class": bot_class,
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "device_type": device_type,
                "format": format,
                "http_protocol": http_protocol,
                "http_version": http_version,
                "location": location,
                "name": name,
                "os": os,
                "tls_version": tls_version,
            }, timeseries_group_ip_version_params.TimeseriesGroupIPVersionParams), post_parser=ResultWrapper[TimeseriesGroupIPVersionResponse]._unwrapper),
            cast_to=cast(Type[TimeseriesGroupIPVersionResponse], ResultWrapper[TimeseriesGroupIPVersionResponse]),
        )

    async def os(self,
    *,
    agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
    asn: List[str] | NotGiven = NOT_GIVEN,
    bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    date_range: List[str] | NotGiven = NOT_GIVEN,
    date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    device_type: List[Literal["DESKTOP", "MOBILE", "OTHER"]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    http_protocol: List[Literal["HTTP", "HTTPS"]] | NotGiven = NOT_GIVEN,
    http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
    ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TimeseriesGroupOSResponse:
        """
        Get a time series of the percentage distribution of traffic of the top operating
        systems.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          bot_class: Filter for bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          device_type: Filter for device type.

          format: Format results are returned in.

          http_protocol: Filter for http protocol.

          http_version: Filter for http version.

          ip_version: Filter for ip version.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/http/timeseries_groups/os",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "agg_interval": agg_interval,
                "asn": asn,
                "bot_class": bot_class,
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "device_type": device_type,
                "format": format,
                "http_protocol": http_protocol,
                "http_version": http_version,
                "ip_version": ip_version,
                "location": location,
                "name": name,
                "tls_version": tls_version,
            }, timeseries_group_os_params.TimeseriesGroupOSParams), post_parser=ResultWrapper[TimeseriesGroupOSResponse]._unwrapper),
            cast_to=cast(Type[TimeseriesGroupOSResponse], ResultWrapper[TimeseriesGroupOSResponse]),
        )

    async def post_quantum(self,
    *,
    agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
    asn: List[str] | NotGiven = NOT_GIVEN,
    bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    date_range: List[str] | NotGiven = NOT_GIVEN,
    date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    device_type: List[Literal["DESKTOP", "MOBILE", "OTHER"]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    http_protocol: List[Literal["HTTP", "HTTPS"]] | NotGiven = NOT_GIVEN,
    http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
    ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | NotGiven = NOT_GIVEN,
    tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TimeseriesGroupPostQuantumResponse:
        """
        Get a time series of the percentage distribution of traffic per Post Quantum
        suport.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          bot_class: Filter for bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          device_type: Filter for device type.

          format: Format results are returned in.

          http_protocol: Filter for http protocol.

          http_version: Filter for http version.

          ip_version: Filter for ip version.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          os: Filter for os name.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/http/timeseries_groups/post_quantum",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "agg_interval": agg_interval,
                "asn": asn,
                "bot_class": bot_class,
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "device_type": device_type,
                "format": format,
                "http_protocol": http_protocol,
                "http_version": http_version,
                "ip_version": ip_version,
                "location": location,
                "name": name,
                "os": os,
                "tls_version": tls_version,
            }, timeseries_group_post_quantum_params.TimeseriesGroupPostQuantumParams), post_parser=ResultWrapper[TimeseriesGroupPostQuantumResponse]._unwrapper),
            cast_to=cast(Type[TimeseriesGroupPostQuantumResponse], ResultWrapper[TimeseriesGroupPostQuantumResponse]),
        )

    async def tls_version(self,
    *,
    agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
    asn: List[str] | NotGiven = NOT_GIVEN,
    bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    date_range: List[str] | NotGiven = NOT_GIVEN,
    date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    device_type: List[Literal["DESKTOP", "MOBILE", "OTHER"]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    http_protocol: List[Literal["HTTP", "HTTPS"]] | NotGiven = NOT_GIVEN,
    http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
    ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TimeseriesGroupTLSVersionResponse:
        """
        Get a time series of the percentage distribution of traffic per TLS protocol
        version.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          bot_class: Filter for bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          device_type: Filter for device type.

          format: Format results are returned in.

          http_protocol: Filter for http protocol.

          http_version: Filter for http version.

          ip_version: Filter for ip version.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          os: Filter for os name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/http/timeseries_groups/tls_version",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "agg_interval": agg_interval,
                "asn": asn,
                "bot_class": bot_class,
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "device_type": device_type,
                "format": format,
                "http_protocol": http_protocol,
                "http_version": http_version,
                "ip_version": ip_version,
                "location": location,
                "name": name,
                "os": os,
            }, timeseries_group_tls_version_params.TimeseriesGroupTLSVersionParams), post_parser=ResultWrapper[TimeseriesGroupTLSVersionResponse]._unwrapper),
            cast_to=cast(Type[TimeseriesGroupTLSVersionResponse], ResultWrapper[TimeseriesGroupTLSVersionResponse]),
        )

class TimeseriesGroupsResourceWithRawResponse:
    def __init__(self, timeseries_groups: TimeseriesGroupsResource) -> None:
        self._timeseries_groups = timeseries_groups

        self.bot_class = to_raw_response_wrapper(
            timeseries_groups.bot_class,
        )
        self.browser = to_raw_response_wrapper(
            timeseries_groups.browser,
        )
        self.browser_family = to_raw_response_wrapper(
            timeseries_groups.browser_family,
        )
        self.device_type = to_raw_response_wrapper(
            timeseries_groups.device_type,
        )
        self.http_protocol = to_raw_response_wrapper(
            timeseries_groups.http_protocol,
        )
        self.http_version = to_raw_response_wrapper(
            timeseries_groups.http_version,
        )
        self.ip_version = to_raw_response_wrapper(
            timeseries_groups.ip_version,
        )
        self.os = to_raw_response_wrapper(
            timeseries_groups.os,
        )
        self.post_quantum = to_raw_response_wrapper(
            timeseries_groups.post_quantum,
        )
        self.tls_version = to_raw_response_wrapper(
            timeseries_groups.tls_version,
        )

class AsyncTimeseriesGroupsResourceWithRawResponse:
    def __init__(self, timeseries_groups: AsyncTimeseriesGroupsResource) -> None:
        self._timeseries_groups = timeseries_groups

        self.bot_class = async_to_raw_response_wrapper(
            timeseries_groups.bot_class,
        )
        self.browser = async_to_raw_response_wrapper(
            timeseries_groups.browser,
        )
        self.browser_family = async_to_raw_response_wrapper(
            timeseries_groups.browser_family,
        )
        self.device_type = async_to_raw_response_wrapper(
            timeseries_groups.device_type,
        )
        self.http_protocol = async_to_raw_response_wrapper(
            timeseries_groups.http_protocol,
        )
        self.http_version = async_to_raw_response_wrapper(
            timeseries_groups.http_version,
        )
        self.ip_version = async_to_raw_response_wrapper(
            timeseries_groups.ip_version,
        )
        self.os = async_to_raw_response_wrapper(
            timeseries_groups.os,
        )
        self.post_quantum = async_to_raw_response_wrapper(
            timeseries_groups.post_quantum,
        )
        self.tls_version = async_to_raw_response_wrapper(
            timeseries_groups.tls_version,
        )

class TimeseriesGroupsResourceWithStreamingResponse:
    def __init__(self, timeseries_groups: TimeseriesGroupsResource) -> None:
        self._timeseries_groups = timeseries_groups

        self.bot_class = to_streamed_response_wrapper(
            timeseries_groups.bot_class,
        )
        self.browser = to_streamed_response_wrapper(
            timeseries_groups.browser,
        )
        self.browser_family = to_streamed_response_wrapper(
            timeseries_groups.browser_family,
        )
        self.device_type = to_streamed_response_wrapper(
            timeseries_groups.device_type,
        )
        self.http_protocol = to_streamed_response_wrapper(
            timeseries_groups.http_protocol,
        )
        self.http_version = to_streamed_response_wrapper(
            timeseries_groups.http_version,
        )
        self.ip_version = to_streamed_response_wrapper(
            timeseries_groups.ip_version,
        )
        self.os = to_streamed_response_wrapper(
            timeseries_groups.os,
        )
        self.post_quantum = to_streamed_response_wrapper(
            timeseries_groups.post_quantum,
        )
        self.tls_version = to_streamed_response_wrapper(
            timeseries_groups.tls_version,
        )

class AsyncTimeseriesGroupsResourceWithStreamingResponse:
    def __init__(self, timeseries_groups: AsyncTimeseriesGroupsResource) -> None:
        self._timeseries_groups = timeseries_groups

        self.bot_class = async_to_streamed_response_wrapper(
            timeseries_groups.bot_class,
        )
        self.browser = async_to_streamed_response_wrapper(
            timeseries_groups.browser,
        )
        self.browser_family = async_to_streamed_response_wrapper(
            timeseries_groups.browser_family,
        )
        self.device_type = async_to_streamed_response_wrapper(
            timeseries_groups.device_type,
        )
        self.http_protocol = async_to_streamed_response_wrapper(
            timeseries_groups.http_protocol,
        )
        self.http_version = async_to_streamed_response_wrapper(
            timeseries_groups.http_version,
        )
        self.ip_version = async_to_streamed_response_wrapper(
            timeseries_groups.ip_version,
        )
        self.os = async_to_streamed_response_wrapper(
            timeseries_groups.os,
        )
        self.post_quantum = async_to_streamed_response_wrapper(
            timeseries_groups.post_quantum,
        )
        self.tls_version = async_to_streamed_response_wrapper(
            timeseries_groups.tls_version,
        )