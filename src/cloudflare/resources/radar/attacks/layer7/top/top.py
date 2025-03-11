# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .ases import (
    AsesResource,
    AsyncAsesResource,
    AsesResourceWithRawResponse,
    AsyncAsesResourceWithRawResponse,
    AsesResourceWithStreamingResponse,
    AsyncAsesResourceWithStreamingResponse,
)
from .locations import (
    LocationsResource,
    AsyncLocationsResource,
    LocationsResourceWithRawResponse,
    AsyncLocationsResourceWithRawResponse,
    LocationsResourceWithStreamingResponse,
    AsyncLocationsResourceWithStreamingResponse,
)
from ......_types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ......_utils import (
    maybe_transform,
    async_maybe_transform,
)
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_wrappers import ResultWrapper
from ......_base_client import make_request_options
from ......types.radar.attacks.layer7 import top_attacks_params, top_industry_params, top_vertical_params
from ......types.radar.attacks.layer7.top_attacks_response import TopAttacksResponse
from ......types.radar.attacks.layer7.top_industry_response import TopIndustryResponse
from ......types.radar.attacks.layer7.top_vertical_response import TopVerticalResponse

__all__ = ["TopResource", "AsyncTopResource"]


class TopResource(SyncAPIResource):
    @cached_property
    def locations(self) -> LocationsResource:
        return LocationsResource(self._client)

    @cached_property
    def ases(self) -> AsesResource:
        return AsesResource(self._client)

    @cached_property
    def with_raw_response(self) -> TopResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TopResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TopResourceWithStreamingResponse(self)

    def attacks(
        self,
        *,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        limit_direction: Literal["ORIGIN", "TARGET"] | NotGiven = NOT_GIVEN,
        limit_per_location: int | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        magnitude: Literal["AFFECTED_ZONES", "MITIGATED_REQUESTS"] | NotGiven = NOT_GIVEN,
        mitigation_product: List[
            Literal[
                "DDOS", "WAF", "BOT_MANAGEMENT", "ACCESS_RULES", "IP_REPUTATION", "API_SHIELD", "DATA_LOSS_PREVENTION"
            ]
        ]
        | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        normalization: Literal["PERCENTAGE", "MIN_MAX"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TopAttacksResponse:
        """Retrieves the top attacks from origin to target location.

        Values are percentages
        of the total layer 7 attacks (with billing country). The attack magnitude can be
        defined by the number of mitigated requests or by the number of zones affected.
        You can optionally limit the number of attacks by origin/target location (useful
        if all the top attacks are from or to the same location).

        Args:
          asn: Comma-separated list of Autonomous System Numbers (ASNs). Prefix with `-` to
              exclude ASNs from results. For example, `-174, 3356` excludes results from
              AS174, but includes results from AS3356.

          continent: Comma-separated list of continents (alpha-2 continent codes). Prefix with `-` to
              exclude continents from results. For example, `-EU,NA` excludes results from EU,
              but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          limit: Limits the number of objects returned in the response.

          limit_direction: Array of attack origin/target location attack limits. Together with
              `limitPerLocation`, limits how many objects will be fetched per origin/target
              location.

          limit_per_location: Limits the number of attacks per origin/target (refer to `limitDirection`
              parameter) location.

          location: Comma-separated list of locations (alpha-2 codes). Prefix with `-` to exclude
              locations from results. For example, `-US,PT` excludes results from the US, but
              includes results from PT.

          magnitude: This parameter is deprecated. In the future, we will only support attack
              magnitude defined by the total number of mitigated requests
              (MITIGATED_REQUESTS).

          mitigation_product: Array of L7 mitigation products.

          name: Array of names used to label the series in the response.

          normalization: Normalization method applied. Refer to
              [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/attacks/layer7/top/attacks",
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
                        "limit": limit,
                        "limit_direction": limit_direction,
                        "limit_per_location": limit_per_location,
                        "location": location,
                        "magnitude": magnitude,
                        "mitigation_product": mitigation_product,
                        "name": name,
                        "normalization": normalization,
                    },
                    top_attacks_params.TopAttacksParams,
                ),
                post_parser=ResultWrapper[TopAttacksResponse]._unwrapper,
            ),
            cast_to=cast(Type[TopAttacksResponse], ResultWrapper[TopAttacksResponse]),
        )

    def industry(
        self,
        *,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        http_method: List[
            Literal[
                "GET",
                "POST",
                "DELETE",
                "PUT",
                "HEAD",
                "PURGE",
                "OPTIONS",
                "PROPFIND",
                "MKCOL",
                "PATCH",
                "ACL",
                "BCOPY",
                "BDELETE",
                "BMOVE",
                "BPROPFIND",
                "BPROPPATCH",
                "CHECKIN",
                "CHECKOUT",
                "CONNECT",
                "COPY",
                "LABEL",
                "LOCK",
                "MERGE",
                "MKACTIVITY",
                "MKWORKSPACE",
                "MOVE",
                "NOTIFY",
                "ORDERPATCH",
                "POLL",
                "PROPPATCH",
                "REPORT",
                "SEARCH",
                "SUBSCRIBE",
                "TRACE",
                "UNCHECKOUT",
                "UNLOCK",
                "UNSUBSCRIBE",
                "UPDATE",
                "VERSIONCONTROL",
                "BASELINECONTROL",
                "XMSENUMATTS",
                "RPC_OUT_DATA",
                "RPC_IN_DATA",
                "JSON",
                "COOK",
                "TRACK",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
        ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        mitigation_product: List[
            Literal[
                "DDOS", "WAF", "BOT_MANAGEMENT", "ACCESS_RULES", "IP_REPUTATION", "API_SHIELD", "DATA_LOSS_PREVENTION"
            ]
        ]
        | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TopIndustryResponse:
        """
        Retrieves the industries targeted by layer 7 attacks.

        Args:
          asn: Comma-separated list of Autonomous System Numbers (ASNs). Prefix with `-` to
              exclude ASNs from results. For example, `-174, 3356` excludes results from
              AS174, but includes results from AS3356.

          continent: Comma-separated list of continents (alpha-2 continent codes). Prefix with `-` to
              exclude continents from results. For example, `-EU,NA` excludes results from EU,
              but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          http_method: Filters results by HTTP method.

          http_version: Filters results by HTTP version.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          limit: Limits the number of objects returned in the response.

          location: Comma-separated list of locations (alpha-2 codes). Prefix with `-` to exclude
              locations from results. For example, `-US,PT` excludes results from the US, but
              includes results from PT.

          mitigation_product: Array of L7 mitigation products.

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/attacks/layer7/top/industry",
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
                        "http_method": http_method,
                        "http_version": http_version,
                        "ip_version": ip_version,
                        "limit": limit,
                        "location": location,
                        "mitigation_product": mitigation_product,
                        "name": name,
                    },
                    top_industry_params.TopIndustryParams,
                ),
                post_parser=ResultWrapper[TopIndustryResponse]._unwrapper,
            ),
            cast_to=cast(Type[TopIndustryResponse], ResultWrapper[TopIndustryResponse]),
        )

    def vertical(
        self,
        *,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        http_method: List[
            Literal[
                "GET",
                "POST",
                "DELETE",
                "PUT",
                "HEAD",
                "PURGE",
                "OPTIONS",
                "PROPFIND",
                "MKCOL",
                "PATCH",
                "ACL",
                "BCOPY",
                "BDELETE",
                "BMOVE",
                "BPROPFIND",
                "BPROPPATCH",
                "CHECKIN",
                "CHECKOUT",
                "CONNECT",
                "COPY",
                "LABEL",
                "LOCK",
                "MERGE",
                "MKACTIVITY",
                "MKWORKSPACE",
                "MOVE",
                "NOTIFY",
                "ORDERPATCH",
                "POLL",
                "PROPPATCH",
                "REPORT",
                "SEARCH",
                "SUBSCRIBE",
                "TRACE",
                "UNCHECKOUT",
                "UNLOCK",
                "UNSUBSCRIBE",
                "UPDATE",
                "VERSIONCONTROL",
                "BASELINECONTROL",
                "XMSENUMATTS",
                "RPC_OUT_DATA",
                "RPC_IN_DATA",
                "JSON",
                "COOK",
                "TRACK",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
        ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        mitigation_product: List[
            Literal[
                "DDOS", "WAF", "BOT_MANAGEMENT", "ACCESS_RULES", "IP_REPUTATION", "API_SHIELD", "DATA_LOSS_PREVENTION"
            ]
        ]
        | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TopVerticalResponse:
        """
        Retrieves the verticals targeted by layer 7 attacks.

        Args:
          asn: Comma-separated list of Autonomous System Numbers (ASNs). Prefix with `-` to
              exclude ASNs from results. For example, `-174, 3356` excludes results from
              AS174, but includes results from AS3356.

          continent: Comma-separated list of continents (alpha-2 continent codes). Prefix with `-` to
              exclude continents from results. For example, `-EU,NA` excludes results from EU,
              but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          http_method: Filters results by HTTP method.

          http_version: Filters results by HTTP version.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          limit: Limits the number of objects returned in the response.

          location: Comma-separated list of locations (alpha-2 codes). Prefix with `-` to exclude
              locations from results. For example, `-US,PT` excludes results from the US, but
              includes results from PT.

          mitigation_product: Array of L7 mitigation products.

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/attacks/layer7/top/vertical",
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
                        "http_method": http_method,
                        "http_version": http_version,
                        "ip_version": ip_version,
                        "limit": limit,
                        "location": location,
                        "mitigation_product": mitigation_product,
                        "name": name,
                    },
                    top_vertical_params.TopVerticalParams,
                ),
                post_parser=ResultWrapper[TopVerticalResponse]._unwrapper,
            ),
            cast_to=cast(Type[TopVerticalResponse], ResultWrapper[TopVerticalResponse]),
        )


class AsyncTopResource(AsyncAPIResource):
    @cached_property
    def locations(self) -> AsyncLocationsResource:
        return AsyncLocationsResource(self._client)

    @cached_property
    def ases(self) -> AsyncAsesResource:
        return AsyncAsesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTopResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTopResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTopResourceWithStreamingResponse(self)

    async def attacks(
        self,
        *,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        limit_direction: Literal["ORIGIN", "TARGET"] | NotGiven = NOT_GIVEN,
        limit_per_location: int | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        magnitude: Literal["AFFECTED_ZONES", "MITIGATED_REQUESTS"] | NotGiven = NOT_GIVEN,
        mitigation_product: List[
            Literal[
                "DDOS", "WAF", "BOT_MANAGEMENT", "ACCESS_RULES", "IP_REPUTATION", "API_SHIELD", "DATA_LOSS_PREVENTION"
            ]
        ]
        | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        normalization: Literal["PERCENTAGE", "MIN_MAX"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TopAttacksResponse:
        """Retrieves the top attacks from origin to target location.

        Values are percentages
        of the total layer 7 attacks (with billing country). The attack magnitude can be
        defined by the number of mitigated requests or by the number of zones affected.
        You can optionally limit the number of attacks by origin/target location (useful
        if all the top attacks are from or to the same location).

        Args:
          asn: Comma-separated list of Autonomous System Numbers (ASNs). Prefix with `-` to
              exclude ASNs from results. For example, `-174, 3356` excludes results from
              AS174, but includes results from AS3356.

          continent: Comma-separated list of continents (alpha-2 continent codes). Prefix with `-` to
              exclude continents from results. For example, `-EU,NA` excludes results from EU,
              but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          limit: Limits the number of objects returned in the response.

          limit_direction: Array of attack origin/target location attack limits. Together with
              `limitPerLocation`, limits how many objects will be fetched per origin/target
              location.

          limit_per_location: Limits the number of attacks per origin/target (refer to `limitDirection`
              parameter) location.

          location: Comma-separated list of locations (alpha-2 codes). Prefix with `-` to exclude
              locations from results. For example, `-US,PT` excludes results from the US, but
              includes results from PT.

          magnitude: This parameter is deprecated. In the future, we will only support attack
              magnitude defined by the total number of mitigated requests
              (MITIGATED_REQUESTS).

          mitigation_product: Array of L7 mitigation products.

          name: Array of names used to label the series in the response.

          normalization: Normalization method applied. Refer to
              [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/attacks/layer7/top/attacks",
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
                        "limit": limit,
                        "limit_direction": limit_direction,
                        "limit_per_location": limit_per_location,
                        "location": location,
                        "magnitude": magnitude,
                        "mitigation_product": mitigation_product,
                        "name": name,
                        "normalization": normalization,
                    },
                    top_attacks_params.TopAttacksParams,
                ),
                post_parser=ResultWrapper[TopAttacksResponse]._unwrapper,
            ),
            cast_to=cast(Type[TopAttacksResponse], ResultWrapper[TopAttacksResponse]),
        )

    async def industry(
        self,
        *,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        http_method: List[
            Literal[
                "GET",
                "POST",
                "DELETE",
                "PUT",
                "HEAD",
                "PURGE",
                "OPTIONS",
                "PROPFIND",
                "MKCOL",
                "PATCH",
                "ACL",
                "BCOPY",
                "BDELETE",
                "BMOVE",
                "BPROPFIND",
                "BPROPPATCH",
                "CHECKIN",
                "CHECKOUT",
                "CONNECT",
                "COPY",
                "LABEL",
                "LOCK",
                "MERGE",
                "MKACTIVITY",
                "MKWORKSPACE",
                "MOVE",
                "NOTIFY",
                "ORDERPATCH",
                "POLL",
                "PROPPATCH",
                "REPORT",
                "SEARCH",
                "SUBSCRIBE",
                "TRACE",
                "UNCHECKOUT",
                "UNLOCK",
                "UNSUBSCRIBE",
                "UPDATE",
                "VERSIONCONTROL",
                "BASELINECONTROL",
                "XMSENUMATTS",
                "RPC_OUT_DATA",
                "RPC_IN_DATA",
                "JSON",
                "COOK",
                "TRACK",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
        ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        mitigation_product: List[
            Literal[
                "DDOS", "WAF", "BOT_MANAGEMENT", "ACCESS_RULES", "IP_REPUTATION", "API_SHIELD", "DATA_LOSS_PREVENTION"
            ]
        ]
        | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TopIndustryResponse:
        """
        Retrieves the industries targeted by layer 7 attacks.

        Args:
          asn: Comma-separated list of Autonomous System Numbers (ASNs). Prefix with `-` to
              exclude ASNs from results. For example, `-174, 3356` excludes results from
              AS174, but includes results from AS3356.

          continent: Comma-separated list of continents (alpha-2 continent codes). Prefix with `-` to
              exclude continents from results. For example, `-EU,NA` excludes results from EU,
              but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          http_method: Filters results by HTTP method.

          http_version: Filters results by HTTP version.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          limit: Limits the number of objects returned in the response.

          location: Comma-separated list of locations (alpha-2 codes). Prefix with `-` to exclude
              locations from results. For example, `-US,PT` excludes results from the US, but
              includes results from PT.

          mitigation_product: Array of L7 mitigation products.

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/attacks/layer7/top/industry",
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
                        "http_method": http_method,
                        "http_version": http_version,
                        "ip_version": ip_version,
                        "limit": limit,
                        "location": location,
                        "mitigation_product": mitigation_product,
                        "name": name,
                    },
                    top_industry_params.TopIndustryParams,
                ),
                post_parser=ResultWrapper[TopIndustryResponse]._unwrapper,
            ),
            cast_to=cast(Type[TopIndustryResponse], ResultWrapper[TopIndustryResponse]),
        )

    async def vertical(
        self,
        *,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        http_method: List[
            Literal[
                "GET",
                "POST",
                "DELETE",
                "PUT",
                "HEAD",
                "PURGE",
                "OPTIONS",
                "PROPFIND",
                "MKCOL",
                "PATCH",
                "ACL",
                "BCOPY",
                "BDELETE",
                "BMOVE",
                "BPROPFIND",
                "BPROPPATCH",
                "CHECKIN",
                "CHECKOUT",
                "CONNECT",
                "COPY",
                "LABEL",
                "LOCK",
                "MERGE",
                "MKACTIVITY",
                "MKWORKSPACE",
                "MOVE",
                "NOTIFY",
                "ORDERPATCH",
                "POLL",
                "PROPPATCH",
                "REPORT",
                "SEARCH",
                "SUBSCRIBE",
                "TRACE",
                "UNCHECKOUT",
                "UNLOCK",
                "UNSUBSCRIBE",
                "UPDATE",
                "VERSIONCONTROL",
                "BASELINECONTROL",
                "XMSENUMATTS",
                "RPC_OUT_DATA",
                "RPC_IN_DATA",
                "JSON",
                "COOK",
                "TRACK",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
        ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        mitigation_product: List[
            Literal[
                "DDOS", "WAF", "BOT_MANAGEMENT", "ACCESS_RULES", "IP_REPUTATION", "API_SHIELD", "DATA_LOSS_PREVENTION"
            ]
        ]
        | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TopVerticalResponse:
        """
        Retrieves the verticals targeted by layer 7 attacks.

        Args:
          asn: Comma-separated list of Autonomous System Numbers (ASNs). Prefix with `-` to
              exclude ASNs from results. For example, `-174, 3356` excludes results from
              AS174, but includes results from AS3356.

          continent: Comma-separated list of continents (alpha-2 continent codes). Prefix with `-` to
              exclude continents from results. For example, `-EU,NA` excludes results from EU,
              but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          http_method: Filters results by HTTP method.

          http_version: Filters results by HTTP version.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          limit: Limits the number of objects returned in the response.

          location: Comma-separated list of locations (alpha-2 codes). Prefix with `-` to exclude
              locations from results. For example, `-US,PT` excludes results from the US, but
              includes results from PT.

          mitigation_product: Array of L7 mitigation products.

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/attacks/layer7/top/vertical",
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
                        "http_method": http_method,
                        "http_version": http_version,
                        "ip_version": ip_version,
                        "limit": limit,
                        "location": location,
                        "mitigation_product": mitigation_product,
                        "name": name,
                    },
                    top_vertical_params.TopVerticalParams,
                ),
                post_parser=ResultWrapper[TopVerticalResponse]._unwrapper,
            ),
            cast_to=cast(Type[TopVerticalResponse], ResultWrapper[TopVerticalResponse]),
        )


class TopResourceWithRawResponse:
    def __init__(self, top: TopResource) -> None:
        self._top = top

        self.attacks = to_raw_response_wrapper(
            top.attacks,
        )
        self.industry = to_raw_response_wrapper(
            top.industry,
        )
        self.vertical = to_raw_response_wrapper(
            top.vertical,
        )

    @cached_property
    def locations(self) -> LocationsResourceWithRawResponse:
        return LocationsResourceWithRawResponse(self._top.locations)

    @cached_property
    def ases(self) -> AsesResourceWithRawResponse:
        return AsesResourceWithRawResponse(self._top.ases)


class AsyncTopResourceWithRawResponse:
    def __init__(self, top: AsyncTopResource) -> None:
        self._top = top

        self.attacks = async_to_raw_response_wrapper(
            top.attacks,
        )
        self.industry = async_to_raw_response_wrapper(
            top.industry,
        )
        self.vertical = async_to_raw_response_wrapper(
            top.vertical,
        )

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithRawResponse:
        return AsyncLocationsResourceWithRawResponse(self._top.locations)

    @cached_property
    def ases(self) -> AsyncAsesResourceWithRawResponse:
        return AsyncAsesResourceWithRawResponse(self._top.ases)


class TopResourceWithStreamingResponse:
    def __init__(self, top: TopResource) -> None:
        self._top = top

        self.attacks = to_streamed_response_wrapper(
            top.attacks,
        )
        self.industry = to_streamed_response_wrapper(
            top.industry,
        )
        self.vertical = to_streamed_response_wrapper(
            top.vertical,
        )

    @cached_property
    def locations(self) -> LocationsResourceWithStreamingResponse:
        return LocationsResourceWithStreamingResponse(self._top.locations)

    @cached_property
    def ases(self) -> AsesResourceWithStreamingResponse:
        return AsesResourceWithStreamingResponse(self._top.ases)


class AsyncTopResourceWithStreamingResponse:
    def __init__(self, top: AsyncTopResource) -> None:
        self._top = top

        self.attacks = async_to_streamed_response_wrapper(
            top.attacks,
        )
        self.industry = async_to_streamed_response_wrapper(
            top.industry,
        )
        self.vertical = async_to_streamed_response_wrapper(
            top.vertical,
        )

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithStreamingResponse:
        return AsyncLocationsResourceWithStreamingResponse(self._top.locations)

    @cached_property
    def ases(self) -> AsyncAsesResourceWithStreamingResponse:
        return AsyncAsesResourceWithStreamingResponse(self._top.ases)
