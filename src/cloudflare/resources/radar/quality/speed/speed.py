# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .top import TopResource, AsyncTopResource

from ....._compat import cached_property

from .....types.radar.quality.speed_histogram_response import SpeedHistogramResponse

from ....._wrappers import ResultWrapper

from ....._utils import maybe_transform, async_maybe_transform

from ....._base_client import make_request_options

from typing import Type, List, Union

from datetime import datetime

from typing_extensions import Literal

from .....types.radar.quality.speed_summary_response import SpeedSummaryResponse

from ....._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .....types.radar.quality import speed_histogram_params
from .....types.radar.quality import speed_summary_params
from .top import TopResource, AsyncTopResource, TopResourceWithRawResponse, AsyncTopResourceWithRawResponse, TopResourceWithStreamingResponse, AsyncTopResourceWithStreamingResponse
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["SpeedResource", "AsyncSpeedResource"]

class SpeedResource(SyncAPIResource):
    @cached_property
    def top(self) -> TopResource:
        return TopResource(self._client)

    @cached_property
    def with_raw_response(self) -> SpeedResourceWithRawResponse:
        return SpeedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpeedResourceWithStreamingResponse:
        return SpeedResourceWithStreamingResponse(self)

    def histogram(self,
    *,
    asn: List[str] | NotGiven = NOT_GIVEN,
    bucket_size: int | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    metric_group: Literal["BANDWIDTH", "LATENCY", "JITTER"] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> SpeedHistogramResponse:
        """
        Get an histogram from the previous 90 days of Cloudflare Speed Test data, split
        into fixed bandwidth (Mbps), latency (ms) or jitter (ms) buckets.

        Args:
          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          bucket_size: The width for every bucket in the histogram.

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          format: Format results are returned in.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          metric_group: Metrics to be returned.

          name: Array of names that will be used to name the series in responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/quality/speed/histogram",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "asn": asn,
                "bucket_size": bucket_size,
                "continent": continent,
                "date_end": date_end,
                "format": format,
                "location": location,
                "metric_group": metric_group,
                "name": name,
            }, speed_histogram_params.SpeedHistogramParams), post_parser=ResultWrapper[SpeedHistogramResponse]._unwrapper),
            cast_to=cast(Type[SpeedHistogramResponse], ResultWrapper[SpeedHistogramResponse]),
        )

    def summary(self,
    *,
    asn: List[str] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> SpeedSummaryResponse:
        """
        Get a summary of bandwidth, latency, jitter and packet loss, from the previous
        90 days of Cloudflare Speed Test data.

        Args:
          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          format: Format results are returned in.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/quality/speed/summary",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "asn": asn,
                "continent": continent,
                "date_end": date_end,
                "format": format,
                "location": location,
                "name": name,
            }, speed_summary_params.SpeedSummaryParams), post_parser=ResultWrapper[SpeedSummaryResponse]._unwrapper),
            cast_to=cast(Type[SpeedSummaryResponse], ResultWrapper[SpeedSummaryResponse]),
        )

class AsyncSpeedResource(AsyncAPIResource):
    @cached_property
    def top(self) -> AsyncTopResource:
        return AsyncTopResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSpeedResourceWithRawResponse:
        return AsyncSpeedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpeedResourceWithStreamingResponse:
        return AsyncSpeedResourceWithStreamingResponse(self)

    async def histogram(self,
    *,
    asn: List[str] | NotGiven = NOT_GIVEN,
    bucket_size: int | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    metric_group: Literal["BANDWIDTH", "LATENCY", "JITTER"] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> SpeedHistogramResponse:
        """
        Get an histogram from the previous 90 days of Cloudflare Speed Test data, split
        into fixed bandwidth (Mbps), latency (ms) or jitter (ms) buckets.

        Args:
          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          bucket_size: The width for every bucket in the histogram.

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          format: Format results are returned in.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          metric_group: Metrics to be returned.

          name: Array of names that will be used to name the series in responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/quality/speed/histogram",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "asn": asn,
                "bucket_size": bucket_size,
                "continent": continent,
                "date_end": date_end,
                "format": format,
                "location": location,
                "metric_group": metric_group,
                "name": name,
            }, speed_histogram_params.SpeedHistogramParams), post_parser=ResultWrapper[SpeedHistogramResponse]._unwrapper),
            cast_to=cast(Type[SpeedHistogramResponse], ResultWrapper[SpeedHistogramResponse]),
        )

    async def summary(self,
    *,
    asn: List[str] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> SpeedSummaryResponse:
        """
        Get a summary of bandwidth, latency, jitter and packet loss, from the previous
        90 days of Cloudflare Speed Test data.

        Args:
          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          format: Format results are returned in.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/quality/speed/summary",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "asn": asn,
                "continent": continent,
                "date_end": date_end,
                "format": format,
                "location": location,
                "name": name,
            }, speed_summary_params.SpeedSummaryParams), post_parser=ResultWrapper[SpeedSummaryResponse]._unwrapper),
            cast_to=cast(Type[SpeedSummaryResponse], ResultWrapper[SpeedSummaryResponse]),
        )

class SpeedResourceWithRawResponse:
    def __init__(self, speed: SpeedResource) -> None:
        self._speed = speed

        self.histogram = to_raw_response_wrapper(
            speed.histogram,
        )
        self.summary = to_raw_response_wrapper(
            speed.summary,
        )

    @cached_property
    def top(self) -> TopResourceWithRawResponse:
        return TopResourceWithRawResponse(self._speed.top)

class AsyncSpeedResourceWithRawResponse:
    def __init__(self, speed: AsyncSpeedResource) -> None:
        self._speed = speed

        self.histogram = async_to_raw_response_wrapper(
            speed.histogram,
        )
        self.summary = async_to_raw_response_wrapper(
            speed.summary,
        )

    @cached_property
    def top(self) -> AsyncTopResourceWithRawResponse:
        return AsyncTopResourceWithRawResponse(self._speed.top)

class SpeedResourceWithStreamingResponse:
    def __init__(self, speed: SpeedResource) -> None:
        self._speed = speed

        self.histogram = to_streamed_response_wrapper(
            speed.histogram,
        )
        self.summary = to_streamed_response_wrapper(
            speed.summary,
        )

    @cached_property
    def top(self) -> TopResourceWithStreamingResponse:
        return TopResourceWithStreamingResponse(self._speed.top)

class AsyncSpeedResourceWithStreamingResponse:
    def __init__(self, speed: AsyncSpeedResource) -> None:
        self._speed = speed

        self.histogram = async_to_streamed_response_wrapper(
            speed.histogram,
        )
        self.summary = async_to_streamed_response_wrapper(
            speed.summary,
        )

    @cached_property
    def top(self) -> AsyncTopResourceWithStreamingResponse:
        return AsyncTopResourceWithStreamingResponse(self._speed.top)