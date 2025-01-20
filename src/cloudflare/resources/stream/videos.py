# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ..._base_client import make_request_options
from ...types.stream import video_storage_usage_params
from ...types.stream.video_storage_usage_response import VideoStorageUsageResponse

__all__ = ["VideosResource", "AsyncVideosResource"]


class VideosResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VideosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return VideosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VideosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return VideosResourceWithStreamingResponse(self)

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
    ) -> Optional[VideoStorageUsageResponse]:
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
                post_parser=ResultWrapper[Optional[VideoStorageUsageResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[VideoStorageUsageResponse]], ResultWrapper[VideoStorageUsageResponse]),
        )


class AsyncVideosResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVideosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVideosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVideosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncVideosResourceWithStreamingResponse(self)

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
    ) -> Optional[VideoStorageUsageResponse]:
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
                post_parser=ResultWrapper[Optional[VideoStorageUsageResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[VideoStorageUsageResponse]], ResultWrapper[VideoStorageUsageResponse]),
        )


class VideosResourceWithRawResponse:
    def __init__(self, videos: VideosResource) -> None:
        self._videos = videos

        self.storage_usage = to_raw_response_wrapper(
            videos.storage_usage,
        )


class AsyncVideosResourceWithRawResponse:
    def __init__(self, videos: AsyncVideosResource) -> None:
        self._videos = videos

        self.storage_usage = async_to_raw_response_wrapper(
            videos.storage_usage,
        )


class VideosResourceWithStreamingResponse:
    def __init__(self, videos: VideosResource) -> None:
        self._videos = videos

        self.storage_usage = to_streamed_response_wrapper(
            videos.storage_usage,
        )


class AsyncVideosResourceWithStreamingResponse:
    def __init__(self, videos: AsyncVideosResource) -> None:
        self._videos = videos

        self.storage_usage = async_to_streamed_response_wrapper(
            videos.storage_usage,
        )
