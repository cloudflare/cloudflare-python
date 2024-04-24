# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .os import (
    OSResource,
    AsyncOSResource,
    OSResourceWithRawResponse,
    AsyncOSResourceWithRawResponse,
    OSResourceWithStreamingResponse,
    AsyncOSResourceWithStreamingResponse,
)
from .bot_class import (
    BotClassResource,
    AsyncBotClassResource,
    BotClassResourceWithRawResponse,
    AsyncBotClassResourceWithRawResponse,
    BotClassResourceWithStreamingResponse,
    AsyncBotClassResourceWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .ip_version import (
    IPVersionResource,
    AsyncIPVersionResource,
    IPVersionResourceWithRawResponse,
    AsyncIPVersionResourceWithRawResponse,
    IPVersionResourceWithStreamingResponse,
    AsyncIPVersionResourceWithStreamingResponse,
)
from ....._compat import cached_property
from .device_type import (
    DeviceTypeResource,
    AsyncDeviceTypeResource,
    DeviceTypeResourceWithRawResponse,
    AsyncDeviceTypeResourceWithRawResponse,
    DeviceTypeResourceWithStreamingResponse,
    AsyncDeviceTypeResourceWithStreamingResponse,
)
from .http_method import (
    HTTPMethodResource,
    AsyncHTTPMethodResource,
    HTTPMethodResourceWithRawResponse,
    AsyncHTTPMethodResourceWithRawResponse,
    HTTPMethodResourceWithStreamingResponse,
    AsyncHTTPMethodResourceWithStreamingResponse,
)
from .tls_version import (
    TLSVersionResource,
    AsyncTLSVersionResource,
    TLSVersionResourceWithRawResponse,
    AsyncTLSVersionResourceWithRawResponse,
    TLSVersionResourceWithStreamingResponse,
    AsyncTLSVersionResourceWithStreamingResponse,
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
    HTTPProtocolResource,
    AsyncHTTPProtocolResource,
    HTTPProtocolResourceWithRawResponse,
    AsyncHTTPProtocolResourceWithRawResponse,
    HTTPProtocolResourceWithStreamingResponse,
    AsyncHTTPProtocolResourceWithStreamingResponse,
)
from ....._base_client import (
    make_request_options,
)
from .....types.radar.http import ase_get_params
from .....types.radar.http.ase_get_response import AseGetResponse

__all__ = ["AsesResource", "AsyncAsesResource"]


class AsesResource(SyncAPIResource):
    @cached_property
    def bot_class(self) -> BotClassResource:
        return BotClassResource(self._client)

    @cached_property
    def device_type(self) -> DeviceTypeResource:
        return DeviceTypeResource(self._client)

    @cached_property
    def http_protocol(self) -> HTTPProtocolResource:
        return HTTPProtocolResource(self._client)

    @cached_property
    def http_method(self) -> HTTPMethodResource:
        return HTTPMethodResource(self._client)

    @cached_property
    def ip_version(self) -> IPVersionResource:
        return IPVersionResource(self._client)

    @cached_property
    def os(self) -> OSResource:
        return OSResource(self._client)

    @cached_property
    def tls_version(self) -> TLSVersionResource:
        return TLSVersionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsesResourceWithRawResponse:
        return AsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsesResourceWithStreamingResponse:
        return AsesResourceWithStreamingResponse(self)

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
    ) -> AseGetResponse:
        """Get the top autonomous systems by HTTP traffic.

        Values are a percentage out of
        the total traffic.

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
            "/radar/http/top/ases",
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
                    ase_get_params.AseGetParams,
                ),
                post_parser=ResultWrapper[AseGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[AseGetResponse], ResultWrapper[AseGetResponse]),
        )


class AsyncAsesResource(AsyncAPIResource):
    @cached_property
    def bot_class(self) -> AsyncBotClassResource:
        return AsyncBotClassResource(self._client)

    @cached_property
    def device_type(self) -> AsyncDeviceTypeResource:
        return AsyncDeviceTypeResource(self._client)

    @cached_property
    def http_protocol(self) -> AsyncHTTPProtocolResource:
        return AsyncHTTPProtocolResource(self._client)

    @cached_property
    def http_method(self) -> AsyncHTTPMethodResource:
        return AsyncHTTPMethodResource(self._client)

    @cached_property
    def ip_version(self) -> AsyncIPVersionResource:
        return AsyncIPVersionResource(self._client)

    @cached_property
    def os(self) -> AsyncOSResource:
        return AsyncOSResource(self._client)

    @cached_property
    def tls_version(self) -> AsyncTLSVersionResource:
        return AsyncTLSVersionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAsesResourceWithRawResponse:
        return AsyncAsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAsesResourceWithStreamingResponse:
        return AsyncAsesResourceWithStreamingResponse(self)

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
    ) -> AseGetResponse:
        """Get the top autonomous systems by HTTP traffic.

        Values are a percentage out of
        the total traffic.

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
            "/radar/http/top/ases",
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
                    ase_get_params.AseGetParams,
                ),
                post_parser=ResultWrapper[AseGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[AseGetResponse], ResultWrapper[AseGetResponse]),
        )


class AsesResourceWithRawResponse:
    def __init__(self, ases: AsesResource) -> None:
        self._ases = ases

        self.get = to_raw_response_wrapper(
            ases.get,
        )

    @cached_property
    def bot_class(self) -> BotClassResourceWithRawResponse:
        return BotClassResourceWithRawResponse(self._ases.bot_class)

    @cached_property
    def device_type(self) -> DeviceTypeResourceWithRawResponse:
        return DeviceTypeResourceWithRawResponse(self._ases.device_type)

    @cached_property
    def http_protocol(self) -> HTTPProtocolResourceWithRawResponse:
        return HTTPProtocolResourceWithRawResponse(self._ases.http_protocol)

    @cached_property
    def http_method(self) -> HTTPMethodResourceWithRawResponse:
        return HTTPMethodResourceWithRawResponse(self._ases.http_method)

    @cached_property
    def ip_version(self) -> IPVersionResourceWithRawResponse:
        return IPVersionResourceWithRawResponse(self._ases.ip_version)

    @cached_property
    def os(self) -> OSResourceWithRawResponse:
        return OSResourceWithRawResponse(self._ases.os)

    @cached_property
    def tls_version(self) -> TLSVersionResourceWithRawResponse:
        return TLSVersionResourceWithRawResponse(self._ases.tls_version)


class AsyncAsesResourceWithRawResponse:
    def __init__(self, ases: AsyncAsesResource) -> None:
        self._ases = ases

        self.get = async_to_raw_response_wrapper(
            ases.get,
        )

    @cached_property
    def bot_class(self) -> AsyncBotClassResourceWithRawResponse:
        return AsyncBotClassResourceWithRawResponse(self._ases.bot_class)

    @cached_property
    def device_type(self) -> AsyncDeviceTypeResourceWithRawResponse:
        return AsyncDeviceTypeResourceWithRawResponse(self._ases.device_type)

    @cached_property
    def http_protocol(self) -> AsyncHTTPProtocolResourceWithRawResponse:
        return AsyncHTTPProtocolResourceWithRawResponse(self._ases.http_protocol)

    @cached_property
    def http_method(self) -> AsyncHTTPMethodResourceWithRawResponse:
        return AsyncHTTPMethodResourceWithRawResponse(self._ases.http_method)

    @cached_property
    def ip_version(self) -> AsyncIPVersionResourceWithRawResponse:
        return AsyncIPVersionResourceWithRawResponse(self._ases.ip_version)

    @cached_property
    def os(self) -> AsyncOSResourceWithRawResponse:
        return AsyncOSResourceWithRawResponse(self._ases.os)

    @cached_property
    def tls_version(self) -> AsyncTLSVersionResourceWithRawResponse:
        return AsyncTLSVersionResourceWithRawResponse(self._ases.tls_version)


class AsesResourceWithStreamingResponse:
    def __init__(self, ases: AsesResource) -> None:
        self._ases = ases

        self.get = to_streamed_response_wrapper(
            ases.get,
        )

    @cached_property
    def bot_class(self) -> BotClassResourceWithStreamingResponse:
        return BotClassResourceWithStreamingResponse(self._ases.bot_class)

    @cached_property
    def device_type(self) -> DeviceTypeResourceWithStreamingResponse:
        return DeviceTypeResourceWithStreamingResponse(self._ases.device_type)

    @cached_property
    def http_protocol(self) -> HTTPProtocolResourceWithStreamingResponse:
        return HTTPProtocolResourceWithStreamingResponse(self._ases.http_protocol)

    @cached_property
    def http_method(self) -> HTTPMethodResourceWithStreamingResponse:
        return HTTPMethodResourceWithStreamingResponse(self._ases.http_method)

    @cached_property
    def ip_version(self) -> IPVersionResourceWithStreamingResponse:
        return IPVersionResourceWithStreamingResponse(self._ases.ip_version)

    @cached_property
    def os(self) -> OSResourceWithStreamingResponse:
        return OSResourceWithStreamingResponse(self._ases.os)

    @cached_property
    def tls_version(self) -> TLSVersionResourceWithStreamingResponse:
        return TLSVersionResourceWithStreamingResponse(self._ases.tls_version)


class AsyncAsesResourceWithStreamingResponse:
    def __init__(self, ases: AsyncAsesResource) -> None:
        self._ases = ases

        self.get = async_to_streamed_response_wrapper(
            ases.get,
        )

    @cached_property
    def bot_class(self) -> AsyncBotClassResourceWithStreamingResponse:
        return AsyncBotClassResourceWithStreamingResponse(self._ases.bot_class)

    @cached_property
    def device_type(self) -> AsyncDeviceTypeResourceWithStreamingResponse:
        return AsyncDeviceTypeResourceWithStreamingResponse(self._ases.device_type)

    @cached_property
    def http_protocol(self) -> AsyncHTTPProtocolResourceWithStreamingResponse:
        return AsyncHTTPProtocolResourceWithStreamingResponse(self._ases.http_protocol)

    @cached_property
    def http_method(self) -> AsyncHTTPMethodResourceWithStreamingResponse:
        return AsyncHTTPMethodResourceWithStreamingResponse(self._ases.http_method)

    @cached_property
    def ip_version(self) -> AsyncIPVersionResourceWithStreamingResponse:
        return AsyncIPVersionResourceWithStreamingResponse(self._ases.ip_version)

    @cached_property
    def os(self) -> AsyncOSResourceWithStreamingResponse:
        return AsyncOSResourceWithStreamingResponse(self._ases.os)

    @cached_property
    def tls_version(self) -> AsyncTLSVersionResourceWithStreamingResponse:
        return AsyncTLSVersionResourceWithStreamingResponse(self._ases.tls_version)
