# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, cast
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
from ....types.radar.post_quantum import origin_summary_params, origin_timeseries_groups_params
from ....types.radar.post_quantum.origin_summary_response import OriginSummaryResponse
from ....types.radar.post_quantum.origin_timeseries_groups_response import OriginTimeseriesGroupsResponse

__all__ = ["OriginResource", "AsyncOriginResource"]


class OriginResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OriginResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return OriginResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OriginResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return OriginResourceWithStreamingResponse(self)

    def summary(
        self,
        dimension: Literal["KEY_AGREEMENT"],
        *,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginSummaryResponse:
        """
        Returns a summary of origin post-quantum data grouped by the specified
        dimension.

        Args:
          dimension: Specifies the origin post-quantum data dimension by which to group the results.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return self._get(
            f"/radar/post_quantum/origin/summary/{dimension}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "name": name,
                    },
                    origin_summary_params.OriginSummaryParams,
                ),
                post_parser=ResultWrapper[OriginSummaryResponse]._unwrapper,
            ),
            cast_to=cast(Type[OriginSummaryResponse], ResultWrapper[OriginSummaryResponse]),
        )

    def timeseries_groups(
        self,
        dimension: Literal["KEY_AGREEMENT"],
        *,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginTimeseriesGroupsResponse:
        """
        Returns a timeseries of origin post-quantum data grouped by the specified
        dimension.

        Args:
          dimension: Specifies the origin post-quantum data dimension by which to group the results.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return self._get(
            f"/radar/post_quantum/origin/timeseries_groups/{dimension}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "name": name,
                    },
                    origin_timeseries_groups_params.OriginTimeseriesGroupsParams,
                ),
                post_parser=ResultWrapper[OriginTimeseriesGroupsResponse]._unwrapper,
            ),
            cast_to=cast(Type[OriginTimeseriesGroupsResponse], ResultWrapper[OriginTimeseriesGroupsResponse]),
        )


class AsyncOriginResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOriginResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOriginResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOriginResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncOriginResourceWithStreamingResponse(self)

    async def summary(
        self,
        dimension: Literal["KEY_AGREEMENT"],
        *,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginSummaryResponse:
        """
        Returns a summary of origin post-quantum data grouped by the specified
        dimension.

        Args:
          dimension: Specifies the origin post-quantum data dimension by which to group the results.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return await self._get(
            f"/radar/post_quantum/origin/summary/{dimension}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "name": name,
                    },
                    origin_summary_params.OriginSummaryParams,
                ),
                post_parser=ResultWrapper[OriginSummaryResponse]._unwrapper,
            ),
            cast_to=cast(Type[OriginSummaryResponse], ResultWrapper[OriginSummaryResponse]),
        )

    async def timeseries_groups(
        self,
        dimension: Literal["KEY_AGREEMENT"],
        *,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginTimeseriesGroupsResponse:
        """
        Returns a timeseries of origin post-quantum data grouped by the specified
        dimension.

        Args:
          dimension: Specifies the origin post-quantum data dimension by which to group the results.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return await self._get(
            f"/radar/post_quantum/origin/timeseries_groups/{dimension}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "name": name,
                    },
                    origin_timeseries_groups_params.OriginTimeseriesGroupsParams,
                ),
                post_parser=ResultWrapper[OriginTimeseriesGroupsResponse]._unwrapper,
            ),
            cast_to=cast(Type[OriginTimeseriesGroupsResponse], ResultWrapper[OriginTimeseriesGroupsResponse]),
        )


class OriginResourceWithRawResponse:
    def __init__(self, origin: OriginResource) -> None:
        self._origin = origin

        self.summary = to_raw_response_wrapper(
            origin.summary,
        )
        self.timeseries_groups = to_raw_response_wrapper(
            origin.timeseries_groups,
        )


class AsyncOriginResourceWithRawResponse:
    def __init__(self, origin: AsyncOriginResource) -> None:
        self._origin = origin

        self.summary = async_to_raw_response_wrapper(
            origin.summary,
        )
        self.timeseries_groups = async_to_raw_response_wrapper(
            origin.timeseries_groups,
        )


class OriginResourceWithStreamingResponse:
    def __init__(self, origin: OriginResource) -> None:
        self._origin = origin

        self.summary = to_streamed_response_wrapper(
            origin.summary,
        )
        self.timeseries_groups = to_streamed_response_wrapper(
            origin.timeseries_groups,
        )


class AsyncOriginResourceWithStreamingResponse:
    def __init__(self, origin: AsyncOriginResource) -> None:
        self._origin = origin

        self.summary = async_to_streamed_response_wrapper(
            origin.summary,
        )
        self.timeseries_groups = async_to_streamed_response_wrapper(
            origin.timeseries_groups,
        )
