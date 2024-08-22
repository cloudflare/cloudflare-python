# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ......_compat import cached_property

from ......types.radar.attacks.layer3.top.location_origin_response import LocationOriginResponse

from ......_wrappers import ResultWrapper

from ......_utils import maybe_transform, async_maybe_transform

from ......_base_client import make_request_options

from typing import Type, List, Union

from datetime import datetime

from typing_extensions import Literal

from ......types.radar.attacks.layer3.top.location_target_response import LocationTargetResponse

from ......_response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ......_utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ......_types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......types import shared_params
from ......types.radar.attacks.layer3.top import location_origin_params
from ......types.radar.attacks.layer3.top import location_target_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["LocationsResource", "AsyncLocationsResource"]

class LocationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LocationsResourceWithRawResponse:
        return LocationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LocationsResourceWithStreamingResponse:
        return LocationsResourceWithStreamingResponse(self)

    def origin(self,
    *,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    date_range: List[str] | NotGiven = NOT_GIVEN,
    date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
    limit: int | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    protocol: List[Literal["UDP", "TCP", "ICMP", "GRE"]] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> LocationOriginResponse:
        """
        Get the origin locations of attacks.

        Args:
          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          ip_version: Filter for ip version.

          limit: Limit the number of objects in the response.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          protocol: Array of L3/4 attack types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/attacks/layer3/top/locations/origin",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "format": format,
                "ip_version": ip_version,
                "limit": limit,
                "location": location,
                "name": name,
                "protocol": protocol,
            }, location_origin_params.LocationOriginParams), post_parser=ResultWrapper[LocationOriginResponse]._unwrapper),
            cast_to=cast(Type[LocationOriginResponse], ResultWrapper[LocationOriginResponse]),
        )

    def target(self,
    *,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    date_range: List[str] | NotGiven = NOT_GIVEN,
    date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
    limit: int | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    protocol: List[Literal["UDP", "TCP", "ICMP", "GRE"]] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> LocationTargetResponse:
        """
        Get the target locations of attacks.

        Args:
          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          ip_version: Filter for ip version.

          limit: Limit the number of objects in the response.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          protocol: Array of L3/4 attack types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/attacks/layer3/top/locations/target",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "format": format,
                "ip_version": ip_version,
                "limit": limit,
                "location": location,
                "name": name,
                "protocol": protocol,
            }, location_target_params.LocationTargetParams), post_parser=ResultWrapper[LocationTargetResponse]._unwrapper),
            cast_to=cast(Type[LocationTargetResponse], ResultWrapper[LocationTargetResponse]),
        )

class AsyncLocationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLocationsResourceWithRawResponse:
        return AsyncLocationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLocationsResourceWithStreamingResponse:
        return AsyncLocationsResourceWithStreamingResponse(self)

    async def origin(self,
    *,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    date_range: List[str] | NotGiven = NOT_GIVEN,
    date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
    limit: int | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    protocol: List[Literal["UDP", "TCP", "ICMP", "GRE"]] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> LocationOriginResponse:
        """
        Get the origin locations of attacks.

        Args:
          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          ip_version: Filter for ip version.

          limit: Limit the number of objects in the response.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          protocol: Array of L3/4 attack types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/attacks/layer3/top/locations/origin",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "format": format,
                "ip_version": ip_version,
                "limit": limit,
                "location": location,
                "name": name,
                "protocol": protocol,
            }, location_origin_params.LocationOriginParams), post_parser=ResultWrapper[LocationOriginResponse]._unwrapper),
            cast_to=cast(Type[LocationOriginResponse], ResultWrapper[LocationOriginResponse]),
        )

    async def target(self,
    *,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    date_range: List[str] | NotGiven = NOT_GIVEN,
    date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
    limit: int | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    protocol: List[Literal["UDP", "TCP", "ICMP", "GRE"]] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> LocationTargetResponse:
        """
        Get the target locations of attacks.

        Args:
          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          ip_version: Filter for ip version.

          limit: Limit the number of objects in the response.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          protocol: Array of L3/4 attack types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/attacks/layer3/top/locations/target",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "format": format,
                "ip_version": ip_version,
                "limit": limit,
                "location": location,
                "name": name,
                "protocol": protocol,
            }, location_target_params.LocationTargetParams), post_parser=ResultWrapper[LocationTargetResponse]._unwrapper),
            cast_to=cast(Type[LocationTargetResponse], ResultWrapper[LocationTargetResponse]),
        )

class LocationsResourceWithRawResponse:
    def __init__(self, locations: LocationsResource) -> None:
        self._locations = locations

        self.origin = to_raw_response_wrapper(
            locations.origin,
        )
        self.target = to_raw_response_wrapper(
            locations.target,
        )

class AsyncLocationsResourceWithRawResponse:
    def __init__(self, locations: AsyncLocationsResource) -> None:
        self._locations = locations

        self.origin = async_to_raw_response_wrapper(
            locations.origin,
        )
        self.target = async_to_raw_response_wrapper(
            locations.target,
        )

class LocationsResourceWithStreamingResponse:
    def __init__(self, locations: LocationsResource) -> None:
        self._locations = locations

        self.origin = to_streamed_response_wrapper(
            locations.origin,
        )
        self.target = to_streamed_response_wrapper(
            locations.target,
        )

class AsyncLocationsResourceWithStreamingResponse:
    def __init__(self, locations: AsyncLocationsResource) -> None:
        self._locations = locations

        self.origin = async_to_streamed_response_wrapper(
            locations.origin,
        )
        self.target = async_to_streamed_response_wrapper(
            locations.target,
        )