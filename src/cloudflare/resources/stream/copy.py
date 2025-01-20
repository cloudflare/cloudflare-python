# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, Optional, cast
from datetime import datetime

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    strip_not_given,
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
from ...types.stream import copy_create_params
from ...types.stream.video import Video
from ...types.stream.allowed_origins import AllowedOrigins

__all__ = ["CopyResource", "AsyncCopyResource"]


class CopyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CopyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CopyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CopyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CopyResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        url: str,
        allowed_origins: List[AllowedOrigins] | NotGiven = NOT_GIVEN,
        creator: str | NotGiven = NOT_GIVEN,
        meta: object | NotGiven = NOT_GIVEN,
        require_signed_urls: bool | NotGiven = NOT_GIVEN,
        scheduled_deletion: Union[str, datetime] | NotGiven = NOT_GIVEN,
        thumbnail_timestamp_pct: float | NotGiven = NOT_GIVEN,
        watermark: copy_create_params.Watermark | NotGiven = NOT_GIVEN,
        upload_creator: str | NotGiven = NOT_GIVEN,
        upload_metadata: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Video]:
        """
        Uploads a video to Stream from a provided URL.

        Args:
          account_id: The account identifier tag.

          url: A video's URL. The server must be publicly routable and support `HTTP HEAD`
              requests and `HTTP GET` range requests. The server should respond to `HTTP HEAD`
              requests with a `content-range` header that includes the size of the file.

          allowed_origins: Lists the origins allowed to display the video. Enter allowed origin domains in
              an array and use `*` for wildcard subdomains. Empty arrays allow the video to be
              viewed on any origin.

          creator: A user-defined identifier for the media creator.

          meta: A user modifiable key-value store used to reference other systems of record for
              managing videos.

          require_signed_urls: Indicates whether the video can be a accessed using the UID. When set to `true`,
              a signed token must be generated with a signing key to view the video.

          scheduled_deletion: Indicates the date and time at which the video will be deleted. Omit the field
              to indicate no change, or include with a `null` value to remove an existing
              scheduled deletion. If specified, must be at least 30 days from upload time.

          thumbnail_timestamp_pct: The timestamp for a thumbnail image calculated as a percentage value of the
              video's duration. To convert from a second-wise timestamp to a percentage,
              divide the desired timestamp by the total duration of the video. If this value
              is not set, the default thumbnail image is taken from 0s of the video.

          upload_creator: A user-defined identifier for the media creator.

          upload_metadata: Comma-separated key-value pairs following the TUS protocol specification. Values
              are Base-64 encoded. Supported keys: `name`, `requiresignedurls`,
              `allowedorigins`, `thumbnailtimestamppct`, `watermark`, `scheduleddeletion`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Upload-Creator": upload_creator,
                    "Upload-Metadata": upload_metadata,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            f"/accounts/{account_id}/stream/copy",
            body=maybe_transform(
                {
                    "url": url,
                    "allowed_origins": allowed_origins,
                    "creator": creator,
                    "meta": meta,
                    "require_signed_urls": require_signed_urls,
                    "scheduled_deletion": scheduled_deletion,
                    "thumbnail_timestamp_pct": thumbnail_timestamp_pct,
                    "watermark": watermark,
                },
                copy_create_params.CopyCreateParams,
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


class AsyncCopyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCopyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCopyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCopyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCopyResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        url: str,
        allowed_origins: List[AllowedOrigins] | NotGiven = NOT_GIVEN,
        creator: str | NotGiven = NOT_GIVEN,
        meta: object | NotGiven = NOT_GIVEN,
        require_signed_urls: bool | NotGiven = NOT_GIVEN,
        scheduled_deletion: Union[str, datetime] | NotGiven = NOT_GIVEN,
        thumbnail_timestamp_pct: float | NotGiven = NOT_GIVEN,
        watermark: copy_create_params.Watermark | NotGiven = NOT_GIVEN,
        upload_creator: str | NotGiven = NOT_GIVEN,
        upload_metadata: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Video]:
        """
        Uploads a video to Stream from a provided URL.

        Args:
          account_id: The account identifier tag.

          url: A video's URL. The server must be publicly routable and support `HTTP HEAD`
              requests and `HTTP GET` range requests. The server should respond to `HTTP HEAD`
              requests with a `content-range` header that includes the size of the file.

          allowed_origins: Lists the origins allowed to display the video. Enter allowed origin domains in
              an array and use `*` for wildcard subdomains. Empty arrays allow the video to be
              viewed on any origin.

          creator: A user-defined identifier for the media creator.

          meta: A user modifiable key-value store used to reference other systems of record for
              managing videos.

          require_signed_urls: Indicates whether the video can be a accessed using the UID. When set to `true`,
              a signed token must be generated with a signing key to view the video.

          scheduled_deletion: Indicates the date and time at which the video will be deleted. Omit the field
              to indicate no change, or include with a `null` value to remove an existing
              scheduled deletion. If specified, must be at least 30 days from upload time.

          thumbnail_timestamp_pct: The timestamp for a thumbnail image calculated as a percentage value of the
              video's duration. To convert from a second-wise timestamp to a percentage,
              divide the desired timestamp by the total duration of the video. If this value
              is not set, the default thumbnail image is taken from 0s of the video.

          upload_creator: A user-defined identifier for the media creator.

          upload_metadata: Comma-separated key-value pairs following the TUS protocol specification. Values
              are Base-64 encoded. Supported keys: `name`, `requiresignedurls`,
              `allowedorigins`, `thumbnailtimestamppct`, `watermark`, `scheduleddeletion`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Upload-Creator": upload_creator,
                    "Upload-Metadata": upload_metadata,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            f"/accounts/{account_id}/stream/copy",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "allowed_origins": allowed_origins,
                    "creator": creator,
                    "meta": meta,
                    "require_signed_urls": require_signed_urls,
                    "scheduled_deletion": scheduled_deletion,
                    "thumbnail_timestamp_pct": thumbnail_timestamp_pct,
                    "watermark": watermark,
                },
                copy_create_params.CopyCreateParams,
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


class CopyResourceWithRawResponse:
    def __init__(self, copy: CopyResource) -> None:
        self._copy = copy

        self.create = to_raw_response_wrapper(
            copy.create,
        )


class AsyncCopyResourceWithRawResponse:
    def __init__(self, copy: AsyncCopyResource) -> None:
        self._copy = copy

        self.create = async_to_raw_response_wrapper(
            copy.create,
        )


class CopyResourceWithStreamingResponse:
    def __init__(self, copy: CopyResource) -> None:
        self._copy = copy

        self.create = to_streamed_response_wrapper(
            copy.create,
        )


class AsyncCopyResourceWithStreamingResponse:
    def __init__(self, copy: AsyncCopyResource) -> None:
        self._copy = copy

        self.create = async_to_streamed_response_wrapper(
            copy.create,
        )
