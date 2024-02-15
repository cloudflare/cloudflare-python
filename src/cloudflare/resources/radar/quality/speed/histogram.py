# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.radar.quality.speed import HistogramGetResponse

from typing import Type, List, Union

from datetime import datetime

from typing_extensions import Literal

from ....._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from .....types import shared_params
from .....types.radar.quality.speed import histogram_get_params
from ....._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Histogram", "AsyncHistogram"]


class Histogram(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HistogramWithRawResponse:
        return HistogramWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HistogramWithStreamingResponse:
        return HistogramWithStreamingResponse(self)

    def get(
        self,
        *,
        asn: List[str] | NotGiven = NOT_GIVEN,
        bucket_size: int | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HistogramGetResponse:
        """
        Get an histogram from the previous 90 days of Cloudflare Speed Test data, split
        into fixed bandwidth (Mbps), latency (ms) or jitter (ms) buckets.

        Args:
          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          bucket_size: The width for every bucket in the histogram.

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
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asn": asn,
                        "bucket_size": bucket_size,
                        "date_end": date_end,
                        "format": format,
                        "location": location,
                        "metric_group": metric_group,
                        "name": name,
                    },
                    histogram_get_params.HistogramGetParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[HistogramGetResponse], ResultWrapper[HistogramGetResponse]),
        )


class AsyncHistogram(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHistogramWithRawResponse:
        return AsyncHistogramWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHistogramWithStreamingResponse:
        return AsyncHistogramWithStreamingResponse(self)

    async def get(
        self,
        *,
        asn: List[str] | NotGiven = NOT_GIVEN,
        bucket_size: int | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HistogramGetResponse:
        """
        Get an histogram from the previous 90 days of Cloudflare Speed Test data, split
        into fixed bandwidth (Mbps), latency (ms) or jitter (ms) buckets.

        Args:
          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          bucket_size: The width for every bucket in the histogram.

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
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asn": asn,
                        "bucket_size": bucket_size,
                        "date_end": date_end,
                        "format": format,
                        "location": location,
                        "metric_group": metric_group,
                        "name": name,
                    },
                    histogram_get_params.HistogramGetParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[HistogramGetResponse], ResultWrapper[HistogramGetResponse]),
        )


class HistogramWithRawResponse:
    def __init__(self, histogram: Histogram) -> None:
        self._histogram = histogram

        self.get = to_raw_response_wrapper(
            histogram.get,
        )


class AsyncHistogramWithRawResponse:
    def __init__(self, histogram: AsyncHistogram) -> None:
        self._histogram = histogram

        self.get = async_to_raw_response_wrapper(
            histogram.get,
        )


class HistogramWithStreamingResponse:
    def __init__(self, histogram: Histogram) -> None:
        self._histogram = histogram

        self.get = to_streamed_response_wrapper(
            histogram.get,
        )


class AsyncHistogramWithStreamingResponse:
    def __init__(self, histogram: AsyncHistogram) -> None:
        self._histogram = histogram

        self.get = async_to_streamed_response_wrapper(
            histogram.get,
        )
