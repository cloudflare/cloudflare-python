# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, Optional, cast
from datetime import datetime

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
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
from ...types.stream import clip_create_params
from ...types.stream.video import Video
from ...types.stream.allowed_origins import AllowedOrigins

__all__ = ["ClipResource", "AsyncClipResource"]


class ClipResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClipResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ClipResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClipResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ClipResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str | None = None,
        clipped_from_video_uid: str,
        end_time_seconds: int,
        start_time_seconds: int,
        allowed_origins: SequenceNotStr[AllowedOrigins] | Omit = omit,
        creator: str | Omit = omit,
        input: str | Omit = omit,
        meta: object | Omit = omit,
        name: str | Omit = omit,
        require_signed_urls: bool | Omit = omit,
        scheduled_deletion: Union[str, datetime] | Omit = omit,
        thumbnail_timestamp_pct: float | Omit = omit,
        url: str | Omit = omit,
        watermark: clip_create_params.Watermark | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Video]:
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

          input: A video's URL. Preferred over 'url'.

          meta: A user modifiable key-value store used to reference other systems of record for
              managing videos.

          name: A name for the video.

          require_signed_urls: Indicates whether the video can be a accessed using the UID. When set to `true`,
              a signed token must be generated with a signing key to view the video.

          scheduled_deletion: Indicates the date and time at which the video will be deleted. Omit the field
              to indicate no change, or include with a `null` value to remove an existing
              scheduled deletion. If specified, must be at least 30 days from upload time.

          thumbnail_timestamp_pct: The timestamp for a thumbnail image calculated as a percentage value of the
              video's duration. To convert from a second-wise timestamp to a percentage,
              divide the desired timestamp by the total duration of the video. If this value
              is not set, the default thumbnail image is taken from 0s of the video.

          url: A video's URL (legacy field, use 'input' instead).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/stream/clip", account_id=account_id),
            body=maybe_transform(
                {
                    "clipped_from_video_uid": clipped_from_video_uid,
                    "end_time_seconds": end_time_seconds,
                    "start_time_seconds": start_time_seconds,
                    "allowed_origins": allowed_origins,
                    "creator": creator,
                    "input": input,
                    "meta": meta,
                    "name": name,
                    "require_signed_urls": require_signed_urls,
                    "scheduled_deletion": scheduled_deletion,
                    "thumbnail_timestamp_pct": thumbnail_timestamp_pct,
                    "url": url,
                    "watermark": watermark,
                },
                clip_create_params.ClipCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Video]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Video]], ResultWrapper[Video]),
        )


class AsyncClipResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClipResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClipResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClipResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncClipResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str | None = None,
        clipped_from_video_uid: str,
        end_time_seconds: int,
        start_time_seconds: int,
        allowed_origins: SequenceNotStr[AllowedOrigins] | Omit = omit,
        creator: str | Omit = omit,
        input: str | Omit = omit,
        meta: object | Omit = omit,
        name: str | Omit = omit,
        require_signed_urls: bool | Omit = omit,
        scheduled_deletion: Union[str, datetime] | Omit = omit,
        thumbnail_timestamp_pct: float | Omit = omit,
        url: str | Omit = omit,
        watermark: clip_create_params.Watermark | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Video]:
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

          input: A video's URL. Preferred over 'url'.

          meta: A user modifiable key-value store used to reference other systems of record for
              managing videos.

          name: A name for the video.

          require_signed_urls: Indicates whether the video can be a accessed using the UID. When set to `true`,
              a signed token must be generated with a signing key to view the video.

          scheduled_deletion: Indicates the date and time at which the video will be deleted. Omit the field
              to indicate no change, or include with a `null` value to remove an existing
              scheduled deletion. If specified, must be at least 30 days from upload time.

          thumbnail_timestamp_pct: The timestamp for a thumbnail image calculated as a percentage value of the
              video's duration. To convert from a second-wise timestamp to a percentage,
              divide the desired timestamp by the total duration of the video. If this value
              is not set, the default thumbnail image is taken from 0s of the video.

          url: A video's URL (legacy field, use 'input' instead).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/stream/clip", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "clipped_from_video_uid": clipped_from_video_uid,
                    "end_time_seconds": end_time_seconds,
                    "start_time_seconds": start_time_seconds,
                    "allowed_origins": allowed_origins,
                    "creator": creator,
                    "input": input,
                    "meta": meta,
                    "name": name,
                    "require_signed_urls": require_signed_urls,
                    "scheduled_deletion": scheduled_deletion,
                    "thumbnail_timestamp_pct": thumbnail_timestamp_pct,
                    "url": url,
                    "watermark": watermark,
                },
                clip_create_params.ClipCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Video]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Video]], ResultWrapper[Video]),
        )


class ClipResourceWithRawResponse:
    def __init__(self, clip: ClipResource) -> None:
        self._clip = clip

        self.create = to_raw_response_wrapper(
            clip.create,
        )


class AsyncClipResourceWithRawResponse:
    def __init__(self, clip: AsyncClipResource) -> None:
        self._clip = clip

        self.create = async_to_raw_response_wrapper(
            clip.create,
        )


class ClipResourceWithStreamingResponse:
    def __init__(self, clip: ClipResource) -> None:
        self._clip = clip

        self.create = to_streamed_response_wrapper(
            clip.create,
        )


class AsyncClipResourceWithStreamingResponse:
    def __init__(self, clip: AsyncClipResource) -> None:
        self._clip = clip

        self.create = async_to_streamed_response_wrapper(
            clip.create,
        )
