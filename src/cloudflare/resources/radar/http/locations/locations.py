# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .os import (
    OS,
    AsyncOS,
    OSWithRawResponse,
    AsyncOSWithRawResponse,
    OSWithStreamingResponse,
    AsyncOSWithStreamingResponse,
)
from .bot_class import (
    BotClass,
    AsyncBotClass,
    BotClassWithRawResponse,
    AsyncBotClassWithRawResponse,
    BotClassWithStreamingResponse,
    AsyncBotClassWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .ip_version import (
    IPVersion,
    AsyncIPVersion,
    IPVersionWithRawResponse,
    AsyncIPVersionWithRawResponse,
    IPVersionWithStreamingResponse,
    AsyncIPVersionWithStreamingResponse,
)
from ....._compat import cached_property
from .device_type import (
    DeviceType,
    AsyncDeviceType,
    DeviceTypeWithRawResponse,
    AsyncDeviceTypeWithRawResponse,
    DeviceTypeWithStreamingResponse,
    AsyncDeviceTypeWithStreamingResponse,
)
from .http_method import (
    HTTPMethod,
    AsyncHTTPMethod,
    HTTPMethodWithRawResponse,
    AsyncHTTPMethodWithRawResponse,
    HTTPMethodWithStreamingResponse,
    AsyncHTTPMethodWithStreamingResponse,
)
from .tls_version import (
    TLSVersion,
    AsyncTLSVersion,
    TLSVersionWithRawResponse,
    AsyncTLSVersionWithRawResponse,
    TLSVersionWithStreamingResponse,
    AsyncTLSVersionWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from .http_protocol import (
    HTTPProtocol,
    AsyncHTTPProtocol,
    HTTPProtocolWithRawResponse,
    AsyncHTTPProtocolWithRawResponse,
    HTTPProtocolWithStreamingResponse,
    AsyncHTTPProtocolWithStreamingResponse,
)
from ....._base_client import (
    make_request_options,
)
from .....types.radar.http import LocationGetResponse, location_get_params

__all__ = ["Locations", "AsyncLocations"]


class Locations(SyncAPIResource):
    @cached_property
    def bot_class(self) -> BotClass:
        return BotClass(self._client)

    @cached_property
    def device_type(self) -> DeviceType:
        return DeviceType(self._client)

    @cached_property
    def http_protocol(self) -> HTTPProtocol:
        return HTTPProtocol(self._client)

    @cached_property
    def http_method(self) -> HTTPMethod:
        return HTTPMethod(self._client)

    @cached_property
    def ip_version(self) -> IPVersion:
        return IPVersion(self._client)

    @cached_property
    def os(self) -> OS:
        return OS(self._client)

    @cached_property
    def tls_version(self) -> TLSVersion:
        return TLSVersion(self._client)

    @cached_property
    def with_raw_response(self) -> LocationsWithRawResponse:
        return LocationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LocationsWithStreamingResponse:
        return LocationsWithStreamingResponse(self)

    def get(
        self,
        *,
        asn: List[str] | NotGiven = NOT_GIVEN,
        bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | NotGiven = NOT_GIVEN,
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
        device_type: List[Literal["DESKTOP", "MOBILE", "OTHER"]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        http_protocol: List[Literal["HTTP", "HTTPS"]] | NotGiven = NOT_GIVEN,
        http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
        ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]]
        | NotGiven = NOT_GIVEN,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LocationGetResponse:
        """Get the top locations by HTTP traffic.

        Values are a percentage out of the total
        traffic.

        Args:
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
        return self._get(
            "/radar/http/top/locations",
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
                        "http_protocol": http_protocol,
                        "http_version": http_version,
                        "ip_version": ip_version,
                        "limit": limit,
                        "location": location,
                        "name": name,
                        "os": os,
                        "tls_version": tls_version,
                    },
                    location_get_params.LocationGetParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LocationGetResponse], ResultWrapper[LocationGetResponse]),
        )


class AsyncLocations(AsyncAPIResource):
    @cached_property
    def bot_class(self) -> AsyncBotClass:
        return AsyncBotClass(self._client)

    @cached_property
    def device_type(self) -> AsyncDeviceType:
        return AsyncDeviceType(self._client)

    @cached_property
    def http_protocol(self) -> AsyncHTTPProtocol:
        return AsyncHTTPProtocol(self._client)

    @cached_property
    def http_method(self) -> AsyncHTTPMethod:
        return AsyncHTTPMethod(self._client)

    @cached_property
    def ip_version(self) -> AsyncIPVersion:
        return AsyncIPVersion(self._client)

    @cached_property
    def os(self) -> AsyncOS:
        return AsyncOS(self._client)

    @cached_property
    def tls_version(self) -> AsyncTLSVersion:
        return AsyncTLSVersion(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLocationsWithRawResponse:
        return AsyncLocationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLocationsWithStreamingResponse:
        return AsyncLocationsWithStreamingResponse(self)

    async def get(
        self,
        *,
        asn: List[str] | NotGiven = NOT_GIVEN,
        bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | NotGiven = NOT_GIVEN,
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
        device_type: List[Literal["DESKTOP", "MOBILE", "OTHER"]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        http_protocol: List[Literal["HTTP", "HTTPS"]] | NotGiven = NOT_GIVEN,
        http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
        ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]]
        | NotGiven = NOT_GIVEN,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LocationGetResponse:
        """Get the top locations by HTTP traffic.

        Values are a percentage out of the total
        traffic.

        Args:
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
        return await self._get(
            "/radar/http/top/locations",
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
                        "http_protocol": http_protocol,
                        "http_version": http_version,
                        "ip_version": ip_version,
                        "limit": limit,
                        "location": location,
                        "name": name,
                        "os": os,
                        "tls_version": tls_version,
                    },
                    location_get_params.LocationGetParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LocationGetResponse], ResultWrapper[LocationGetResponse]),
        )


class LocationsWithRawResponse:
    def __init__(self, locations: Locations) -> None:
        self._locations = locations

        self.get = to_raw_response_wrapper(
            locations.get,
        )

    @cached_property
    def bot_class(self) -> BotClassWithRawResponse:
        return BotClassWithRawResponse(self._locations.bot_class)

    @cached_property
    def device_type(self) -> DeviceTypeWithRawResponse:
        return DeviceTypeWithRawResponse(self._locations.device_type)

    @cached_property
    def http_protocol(self) -> HTTPProtocolWithRawResponse:
        return HTTPProtocolWithRawResponse(self._locations.http_protocol)

    @cached_property
    def http_method(self) -> HTTPMethodWithRawResponse:
        return HTTPMethodWithRawResponse(self._locations.http_method)

    @cached_property
    def ip_version(self) -> IPVersionWithRawResponse:
        return IPVersionWithRawResponse(self._locations.ip_version)

    @cached_property
    def os(self) -> OSWithRawResponse:
        return OSWithRawResponse(self._locations.os)

    @cached_property
    def tls_version(self) -> TLSVersionWithRawResponse:
        return TLSVersionWithRawResponse(self._locations.tls_version)


class AsyncLocationsWithRawResponse:
    def __init__(self, locations: AsyncLocations) -> None:
        self._locations = locations

        self.get = async_to_raw_response_wrapper(
            locations.get,
        )

    @cached_property
    def bot_class(self) -> AsyncBotClassWithRawResponse:
        return AsyncBotClassWithRawResponse(self._locations.bot_class)

    @cached_property
    def device_type(self) -> AsyncDeviceTypeWithRawResponse:
        return AsyncDeviceTypeWithRawResponse(self._locations.device_type)

    @cached_property
    def http_protocol(self) -> AsyncHTTPProtocolWithRawResponse:
        return AsyncHTTPProtocolWithRawResponse(self._locations.http_protocol)

    @cached_property
    def http_method(self) -> AsyncHTTPMethodWithRawResponse:
        return AsyncHTTPMethodWithRawResponse(self._locations.http_method)

    @cached_property
    def ip_version(self) -> AsyncIPVersionWithRawResponse:
        return AsyncIPVersionWithRawResponse(self._locations.ip_version)

    @cached_property
    def os(self) -> AsyncOSWithRawResponse:
        return AsyncOSWithRawResponse(self._locations.os)

    @cached_property
    def tls_version(self) -> AsyncTLSVersionWithRawResponse:
        return AsyncTLSVersionWithRawResponse(self._locations.tls_version)


class LocationsWithStreamingResponse:
    def __init__(self, locations: Locations) -> None:
        self._locations = locations

        self.get = to_streamed_response_wrapper(
            locations.get,
        )

    @cached_property
    def bot_class(self) -> BotClassWithStreamingResponse:
        return BotClassWithStreamingResponse(self._locations.bot_class)

    @cached_property
    def device_type(self) -> DeviceTypeWithStreamingResponse:
        return DeviceTypeWithStreamingResponse(self._locations.device_type)

    @cached_property
    def http_protocol(self) -> HTTPProtocolWithStreamingResponse:
        return HTTPProtocolWithStreamingResponse(self._locations.http_protocol)

    @cached_property
    def http_method(self) -> HTTPMethodWithStreamingResponse:
        return HTTPMethodWithStreamingResponse(self._locations.http_method)

    @cached_property
    def ip_version(self) -> IPVersionWithStreamingResponse:
        return IPVersionWithStreamingResponse(self._locations.ip_version)

    @cached_property
    def os(self) -> OSWithStreamingResponse:
        return OSWithStreamingResponse(self._locations.os)

    @cached_property
    def tls_version(self) -> TLSVersionWithStreamingResponse:
        return TLSVersionWithStreamingResponse(self._locations.tls_version)


class AsyncLocationsWithStreamingResponse:
    def __init__(self, locations: AsyncLocations) -> None:
        self._locations = locations

        self.get = async_to_streamed_response_wrapper(
            locations.get,
        )

    @cached_property
    def bot_class(self) -> AsyncBotClassWithStreamingResponse:
        return AsyncBotClassWithStreamingResponse(self._locations.bot_class)

    @cached_property
    def device_type(self) -> AsyncDeviceTypeWithStreamingResponse:
        return AsyncDeviceTypeWithStreamingResponse(self._locations.device_type)

    @cached_property
    def http_protocol(self) -> AsyncHTTPProtocolWithStreamingResponse:
        return AsyncHTTPProtocolWithStreamingResponse(self._locations.http_protocol)

    @cached_property
    def http_method(self) -> AsyncHTTPMethodWithStreamingResponse:
        return AsyncHTTPMethodWithStreamingResponse(self._locations.http_method)

    @cached_property
    def ip_version(self) -> AsyncIPVersionWithStreamingResponse:
        return AsyncIPVersionWithStreamingResponse(self._locations.ip_version)

    @cached_property
    def os(self) -> AsyncOSWithStreamingResponse:
        return AsyncOSWithStreamingResponse(self._locations.os)

    @cached_property
    def tls_version(self) -> AsyncTLSVersionWithStreamingResponse:
        return AsyncTLSVersionWithStreamingResponse(self._locations.tls_version)
