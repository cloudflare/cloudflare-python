# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, cast

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
from ...types.stream import StreamClipping, clip_create_params

__all__ = ["Clip", "AsyncClip"]


class Clip(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClipWithRawResponse:
        return ClipWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClipWithStreamingResponse:
        return ClipWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        clipped_from_video_uid: str,
        end_time_seconds: int,
        start_time_seconds: int,
        allowed_origins: List[str] | NotGiven = NOT_GIVEN,
        creator: str | NotGiven = NOT_GIVEN,
        max_duration_seconds: int | NotGiven = NOT_GIVEN,
        require_signed_urls: bool | NotGiven = NOT_GIVEN,
        thumbnail_timestamp_pct: float | NotGiven = NOT_GIVEN,
        watermark: clip_create_params.Watermark | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StreamClipping:
        """
        Clips a video based on the specified start and end times provided in seconds.

        Args:
          account_id: The account identifier tag.

          clipped_from_video_uid: The unique video identifier (UID).

          end_time_seconds: Specifies the end time for the video clip in seconds.

          start_time_seconds: Specifies the start time for the video clip in seconds.

          allowed_origins: Lists the origins allowed to display the video. Enter allowed origin domains in
              an array and use `*` for wildcard subdomains. Empty arrays allow the video to be
              viewed on any origin.

          creator: A user-defined identifier for the media creator.

          max_duration_seconds: The maximum duration in seconds for a video upload. Can be set for a video that
              is not yet uploaded to limit its duration. Uploads that exceed the specified
              duration will fail during processing. A value of `-1` means the value is
              unknown.

          require_signed_urls: Indicates whether the video can be a accessed using the UID. When set to `true`,
              a signed token must be generated with a signing key to view the video.

          thumbnail_timestamp_pct: The timestamp for a thumbnail image calculated as a percentage value of the
              video's duration. To convert from a second-wise timestamp to a percentage,
              divide the desired timestamp by the total duration of the video. If this value
              is not set, the default thumbnail image is taken from 0s of the video.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/stream/clip",
            body=maybe_transform(
                {
                    "clipped_from_video_uid": clipped_from_video_uid,
                    "end_time_seconds": end_time_seconds,
                    "start_time_seconds": start_time_seconds,
                    "allowed_origins": allowed_origins,
                    "creator": creator,
                    "max_duration_seconds": max_duration_seconds,
                    "require_signed_urls": require_signed_urls,
                    "thumbnail_timestamp_pct": thumbnail_timestamp_pct,
                    "watermark": watermark,
                },
                clip_create_params.ClipCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[StreamClipping], ResultWrapper[StreamClipping]),
        )


class AsyncClip(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClipWithRawResponse:
        return AsyncClipWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClipWithStreamingResponse:
        return AsyncClipWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        clipped_from_video_uid: str,
        end_time_seconds: int,
        start_time_seconds: int,
        allowed_origins: List[str] | NotGiven = NOT_GIVEN,
        creator: str | NotGiven = NOT_GIVEN,
        max_duration_seconds: int | NotGiven = NOT_GIVEN,
        require_signed_urls: bool | NotGiven = NOT_GIVEN,
        thumbnail_timestamp_pct: float | NotGiven = NOT_GIVEN,
        watermark: clip_create_params.Watermark | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StreamClipping:
        """
        Clips a video based on the specified start and end times provided in seconds.

        Args:
          account_id: The account identifier tag.

          clipped_from_video_uid: The unique video identifier (UID).

          end_time_seconds: Specifies the end time for the video clip in seconds.

          start_time_seconds: Specifies the start time for the video clip in seconds.

          allowed_origins: Lists the origins allowed to display the video. Enter allowed origin domains in
              an array and use `*` for wildcard subdomains. Empty arrays allow the video to be
              viewed on any origin.

          creator: A user-defined identifier for the media creator.

          max_duration_seconds: The maximum duration in seconds for a video upload. Can be set for a video that
              is not yet uploaded to limit its duration. Uploads that exceed the specified
              duration will fail during processing. A value of `-1` means the value is
              unknown.

          require_signed_urls: Indicates whether the video can be a accessed using the UID. When set to `true`,
              a signed token must be generated with a signing key to view the video.

          thumbnail_timestamp_pct: The timestamp for a thumbnail image calculated as a percentage value of the
              video's duration. To convert from a second-wise timestamp to a percentage,
              divide the desired timestamp by the total duration of the video. If this value
              is not set, the default thumbnail image is taken from 0s of the video.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/stream/clip",
            body=await async_maybe_transform(
                {
                    "clipped_from_video_uid": clipped_from_video_uid,
                    "end_time_seconds": end_time_seconds,
                    "start_time_seconds": start_time_seconds,
                    "allowed_origins": allowed_origins,
                    "creator": creator,
                    "max_duration_seconds": max_duration_seconds,
                    "require_signed_urls": require_signed_urls,
                    "thumbnail_timestamp_pct": thumbnail_timestamp_pct,
                    "watermark": watermark,
                },
                clip_create_params.ClipCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[StreamClipping], ResultWrapper[StreamClipping]),
        )


class ClipWithRawResponse:
    def __init__(self, clip: Clip) -> None:
        self._clip = clip

        self.create = to_raw_response_wrapper(
            clip.create,
        )


class AsyncClipWithRawResponse:
    def __init__(self, clip: AsyncClip) -> None:
        self._clip = clip

        self.create = async_to_raw_response_wrapper(
            clip.create,
        )


class ClipWithStreamingResponse:
    def __init__(self, clip: Clip) -> None:
        self._clip = clip

        self.create = to_streamed_response_wrapper(
            clip.create,
        )


class AsyncClipWithStreamingResponse:
    def __init__(self, clip: AsyncClip) -> None:
        self._clip = clip

        self.create = async_to_streamed_response_wrapper(
            clip.create,
        )
