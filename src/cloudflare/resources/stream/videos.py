# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.stream import VideoStorageUsageResponse, video_storage_usage_params

__all__ = ["Videos", "AsyncVideos"]


class Videos(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VideosWithRawResponse:
        return VideosWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VideosWithStreamingResponse:
        return VideosWithStreamingResponse(self)

    def storage_usage(
        self,
        *,
        account_id: str,
        creator: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VideoStorageUsageResponse:
        """
        Returns information about an account's storage use.

        Args:
          account_id: The account identifier tag.

          creator: A user-defined identifier for the media creator.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/stream/storage-usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"creator": creator}, video_storage_usage_params.VideoStorageUsageParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[VideoStorageUsageResponse], ResultWrapper[VideoStorageUsageResponse]),
        )


class AsyncVideos(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVideosWithRawResponse:
        return AsyncVideosWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVideosWithStreamingResponse:
        return AsyncVideosWithStreamingResponse(self)

    async def storage_usage(
        self,
        *,
        account_id: str,
        creator: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VideoStorageUsageResponse:
        """
        Returns information about an account's storage use.

        Args:
          account_id: The account identifier tag.

          creator: A user-defined identifier for the media creator.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/stream/storage-usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"creator": creator}, video_storage_usage_params.VideoStorageUsageParams
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[VideoStorageUsageResponse], ResultWrapper[VideoStorageUsageResponse]),
        )


class VideosWithRawResponse:
    def __init__(self, videos: Videos) -> None:
        self._videos = videos

        self.storage_usage = to_raw_response_wrapper(
            videos.storage_usage,
        )


class AsyncVideosWithRawResponse:
    def __init__(self, videos: AsyncVideos) -> None:
        self._videos = videos

        self.storage_usage = async_to_raw_response_wrapper(
            videos.storage_usage,
        )


class VideosWithStreamingResponse:
    def __init__(self, videos: Videos) -> None:
        self._videos = videos

        self.storage_usage = to_streamed_response_wrapper(
            videos.storage_usage,
        )


class AsyncVideosWithStreamingResponse:
    def __init__(self, videos: AsyncVideos) -> None:
        self._videos = videos

        self.storage_usage = async_to_streamed_response_wrapper(
            videos.storage_usage,
        )
