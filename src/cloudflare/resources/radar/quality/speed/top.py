# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.radar.quality.speed.top_ases_response import TopAsesResponse

from ....._wrappers import ResultWrapper

from ....._utils import maybe_transform, async_maybe_transform

from ....._base_client import make_request_options

from typing import Type, List, Union

from datetime import datetime

from typing_extensions import Literal

from .....types.radar.quality.speed.top_locations_response import TopLocationsResponse

from ....._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .....types.radar.quality.speed import top_ases_params
from .....types.radar.quality.speed import top_locations_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["TopResource", "AsyncTopResource"]

class TopResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TopResourceWithRawResponse:
        return TopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TopResourceWithStreamingResponse:
        return TopResourceWithStreamingResponse(self)

    def ases(self,
    *,
    asn: List[str] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    limit: int | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    order_by: Literal["BANDWIDTH_DOWNLOAD", "BANDWIDTH_UPLOAD", "LATENCY_IDLE", "LATENCY_LOADED", "JITTER_IDLE", "JITTER_LOADED"] | NotGiven = NOT_GIVEN,
    reverse: bool | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TopAsesResponse:
        """
        Get the top autonomous systems by bandwidth, latency, jitter or packet loss,
        from the previous 90 days of Cloudflare Speed Test data.

        Args:
          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          order_by: Metric to order the results by.

          reverse: Reverse the order of results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/quality/speed/top/ases",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "asn": asn,
                "continent": continent,
                "date_end": date_end,
                "format": format,
                "limit": limit,
                "location": location,
                "name": name,
                "order_by": order_by,
                "reverse": reverse,
            }, top_ases_params.TopAsesParams), post_parser=ResultWrapper[TopAsesResponse]._unwrapper),
            cast_to=cast(Type[TopAsesResponse], ResultWrapper[TopAsesResponse]),
        )

    def locations(self,
    *,
    asn: List[str] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    limit: int | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    order_by: Literal["BANDWIDTH_DOWNLOAD", "BANDWIDTH_UPLOAD", "LATENCY_IDLE", "LATENCY_LOADED", "JITTER_IDLE", "JITTER_LOADED"] | NotGiven = NOT_GIVEN,
    reverse: bool | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TopLocationsResponse:
        """
        Get the top locations by bandwidth, latency, jitter or packet loss, from the
        previous 90 days of Cloudflare Speed Test data.

        Args:
          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          order_by: Metric to order the results by.

          reverse: Reverse the order of results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/quality/speed/top/locations",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "asn": asn,
                "continent": continent,
                "date_end": date_end,
                "format": format,
                "limit": limit,
                "location": location,
                "name": name,
                "order_by": order_by,
                "reverse": reverse,
            }, top_locations_params.TopLocationsParams), post_parser=ResultWrapper[TopLocationsResponse]._unwrapper),
            cast_to=cast(Type[TopLocationsResponse], ResultWrapper[TopLocationsResponse]),
        )

class AsyncTopResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTopResourceWithRawResponse:
        return AsyncTopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTopResourceWithStreamingResponse:
        return AsyncTopResourceWithStreamingResponse(self)

    async def ases(self,
    *,
    asn: List[str] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    limit: int | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    order_by: Literal["BANDWIDTH_DOWNLOAD", "BANDWIDTH_UPLOAD", "LATENCY_IDLE", "LATENCY_LOADED", "JITTER_IDLE", "JITTER_LOADED"] | NotGiven = NOT_GIVEN,
    reverse: bool | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TopAsesResponse:
        """
        Get the top autonomous systems by bandwidth, latency, jitter or packet loss,
        from the previous 90 days of Cloudflare Speed Test data.

        Args:
          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          order_by: Metric to order the results by.

          reverse: Reverse the order of results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/quality/speed/top/ases",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "asn": asn,
                "continent": continent,
                "date_end": date_end,
                "format": format,
                "limit": limit,
                "location": location,
                "name": name,
                "order_by": order_by,
                "reverse": reverse,
            }, top_ases_params.TopAsesParams), post_parser=ResultWrapper[TopAsesResponse]._unwrapper),
            cast_to=cast(Type[TopAsesResponse], ResultWrapper[TopAsesResponse]),
        )

    async def locations(self,
    *,
    asn: List[str] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    limit: int | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    order_by: Literal["BANDWIDTH_DOWNLOAD", "BANDWIDTH_UPLOAD", "LATENCY_IDLE", "LATENCY_LOADED", "JITTER_IDLE", "JITTER_LOADED"] | NotGiven = NOT_GIVEN,
    reverse: bool | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TopLocationsResponse:
        """
        Get the top locations by bandwidth, latency, jitter or packet loss, from the
        previous 90 days of Cloudflare Speed Test data.

        Args:
          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          order_by: Metric to order the results by.

          reverse: Reverse the order of results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/quality/speed/top/locations",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "asn": asn,
                "continent": continent,
                "date_end": date_end,
                "format": format,
                "limit": limit,
                "location": location,
                "name": name,
                "order_by": order_by,
                "reverse": reverse,
            }, top_locations_params.TopLocationsParams), post_parser=ResultWrapper[TopLocationsResponse]._unwrapper),
            cast_to=cast(Type[TopLocationsResponse], ResultWrapper[TopLocationsResponse]),
        )

class TopResourceWithRawResponse:
    def __init__(self, top: TopResource) -> None:
        self._top = top

        self.ases = to_raw_response_wrapper(
            top.ases,
        )
        self.locations = to_raw_response_wrapper(
            top.locations,
        )

class AsyncTopResourceWithRawResponse:
    def __init__(self, top: AsyncTopResource) -> None:
        self._top = top

        self.ases = async_to_raw_response_wrapper(
            top.ases,
        )
        self.locations = async_to_raw_response_wrapper(
            top.locations,
        )

class TopResourceWithStreamingResponse:
    def __init__(self, top: TopResource) -> None:
        self._top = top

        self.ases = to_streamed_response_wrapper(
            top.ases,
        )
        self.locations = to_streamed_response_wrapper(
            top.locations,
        )

class AsyncTopResourceWithStreamingResponse:
    def __init__(self, top: AsyncTopResource) -> None:
        self._top = top

        self.ases = async_to_streamed_response_wrapper(
            top.ases,
        )
        self.locations = async_to_streamed_response_wrapper(
            top.locations,
        )