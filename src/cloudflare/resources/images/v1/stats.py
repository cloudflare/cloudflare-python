# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.images.v1 import ImagesImagesStats

__all__ = ["Stats", "AsyncStats"]


class Stats(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StatsWithRawResponse:
        return StatsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatsWithStreamingResponse:
        return StatsWithStreamingResponse(self)

    def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImagesImagesStats:
        """
        Fetch usage statistics details for Cloudflare Images.

        Args:
          account_id: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/images/v1/stats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ImagesImagesStats], ResultWrapper[ImagesImagesStats]),
        )


class AsyncStats(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStatsWithRawResponse:
        return AsyncStatsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatsWithStreamingResponse:
        return AsyncStatsWithStreamingResponse(self)

    async def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImagesImagesStats:
        """
        Fetch usage statistics details for Cloudflare Images.

        Args:
          account_id: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/images/v1/stats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ImagesImagesStats], ResultWrapper[ImagesImagesStats]),
        )


class StatsWithRawResponse:
    def __init__(self, stats: Stats) -> None:
        self._stats = stats

        self.get = to_raw_response_wrapper(
            stats.get,
        )


class AsyncStatsWithRawResponse:
    def __init__(self, stats: AsyncStats) -> None:
        self._stats = stats

        self.get = async_to_raw_response_wrapper(
            stats.get,
        )


class StatsWithStreamingResponse:
    def __init__(self, stats: Stats) -> None:
        self._stats = stats

        self.get = to_streamed_response_wrapper(
            stats.get,
        )


class AsyncStatsWithStreamingResponse:
    def __init__(self, stats: AsyncStats) -> None:
        self._stats = stats

        self.get = async_to_streamed_response_wrapper(
            stats.get,
        )
