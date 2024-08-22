# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.radar.http.locations.ip_version_get_response import IPVersionGetResponse

from ....._wrappers import ResultWrapper

from ....._utils import maybe_transform, async_maybe_transform

from ....._base_client import make_request_options

from typing import Type, List, Union

from typing_extensions import Literal

from datetime import datetime

from ....._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .....types.radar.http.locations import ip_version_get_params
from typing import cast
from typing import cast

__all__ = ["IPVersionResource", "AsyncIPVersionResource"]

class IPVersionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IPVersionResourceWithRawResponse:
        return IPVersionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IPVersionResourceWithStreamingResponse:
        return IPVersionResourceWithStreamingResponse(self)

    def get(self,
    ip_version: Literal["IPv4", "IPv6"],
    *,
    asn: List[str] | NotGiven = NOT_GIVEN,
    bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | NotGiven = NOT_GIVEN,
    browser_family: List[Literal["CHROME", "EDGE", "FIREFOX", "SAFARI"]] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    date_range: List[str] | NotGiven = NOT_GIVEN,
    date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    device_type: List[Literal["DESKTOP", "MOBILE", "OTHER"]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    http_protocol: List[Literal["HTTP", "HTTPS"]] | NotGiven = NOT_GIVEN,
    http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
    limit: int | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | NotGiven = NOT_GIVEN,
    tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> IPVersionGetResponse:
        """
        Get the top locations, by HTTP traffic, of the requested IP protocol version.
        Values are a percentage out of the total traffic.

        Args:
          ip_version: IP version.

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          bot_class: Filter for bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          browser_family: Filter for browser family.

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

          limit: Limit the number of objects in the response.

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
        if not ip_version:
          raise ValueError(
            f'Expected a non-empty value for `ip_version` but received {ip_version!r}'
          )
        return self._get(
            f"/radar/http/top/locations/ip_version/{ip_version}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "asn": asn,
                "bot_class": bot_class,
                "browser_family": browser_family,
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "device_type": device_type,
                "format": format,
                "http_protocol": http_protocol,
                "http_version": http_version,
                "limit": limit,
                "location": location,
                "name": name,
                "os": os,
                "tls_version": tls_version,
            }, ip_version_get_params.IPVersionGetParams), post_parser=ResultWrapper[IPVersionGetResponse]._unwrapper),
            cast_to=cast(Type[IPVersionGetResponse], ResultWrapper[IPVersionGetResponse]),
        )

class AsyncIPVersionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIPVersionResourceWithRawResponse:
        return AsyncIPVersionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIPVersionResourceWithStreamingResponse:
        return AsyncIPVersionResourceWithStreamingResponse(self)

    async def get(self,
    ip_version: Literal["IPv4", "IPv6"],
    *,
    asn: List[str] | NotGiven = NOT_GIVEN,
    bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | NotGiven = NOT_GIVEN,
    browser_family: List[Literal["CHROME", "EDGE", "FIREFOX", "SAFARI"]] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    date_range: List[str] | NotGiven = NOT_GIVEN,
    date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    device_type: List[Literal["DESKTOP", "MOBILE", "OTHER"]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    http_protocol: List[Literal["HTTP", "HTTPS"]] | NotGiven = NOT_GIVEN,
    http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
    limit: int | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]] | NotGiven = NOT_GIVEN,
    tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> IPVersionGetResponse:
        """
        Get the top locations, by HTTP traffic, of the requested IP protocol version.
        Values are a percentage out of the total traffic.

        Args:
          ip_version: IP version.

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          bot_class: Filter for bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          browser_family: Filter for browser family.

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

          limit: Limit the number of objects in the response.

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
        if not ip_version:
          raise ValueError(
            f'Expected a non-empty value for `ip_version` but received {ip_version!r}'
          )
        return await self._get(
            f"/radar/http/top/locations/ip_version/{ip_version}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "asn": asn,
                "bot_class": bot_class,
                "browser_family": browser_family,
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "device_type": device_type,
                "format": format,
                "http_protocol": http_protocol,
                "http_version": http_version,
                "limit": limit,
                "location": location,
                "name": name,
                "os": os,
                "tls_version": tls_version,
            }, ip_version_get_params.IPVersionGetParams), post_parser=ResultWrapper[IPVersionGetResponse]._unwrapper),
            cast_to=cast(Type[IPVersionGetResponse], ResultWrapper[IPVersionGetResponse]),
        )

class IPVersionResourceWithRawResponse:
    def __init__(self, ip_version: IPVersionResource) -> None:
        self._ip_version = ip_version

        self.get = to_raw_response_wrapper(
            ip_version.get,
        )

class AsyncIPVersionResourceWithRawResponse:
    def __init__(self, ip_version: AsyncIPVersionResource) -> None:
        self._ip_version = ip_version

        self.get = async_to_raw_response_wrapper(
            ip_version.get,
        )

class IPVersionResourceWithStreamingResponse:
    def __init__(self, ip_version: IPVersionResource) -> None:
        self._ip_version = ip_version

        self.get = to_streamed_response_wrapper(
            ip_version.get,
        )

class AsyncIPVersionResourceWithStreamingResponse:
    def __init__(self, ip_version: AsyncIPVersionResource) -> None:
        self._ip_version = ip_version

        self.get = async_to_streamed_response_wrapper(
            ip_version.get,
        )