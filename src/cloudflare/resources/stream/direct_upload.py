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
from ...types.stream import direct_upload_create_params
from ...types.stream.allowed_origins import AllowedOrigins
from ...types.stream.direct_upload_create_response import DirectUploadCreateResponse

__all__ = ["DirectUploadResource", "AsyncDirectUploadResource"]


class DirectUploadResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DirectUploadResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DirectUploadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DirectUploadResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DirectUploadResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        max_duration_seconds: int,
        allowed_origins: List[AllowedOrigins] | NotGiven = NOT_GIVEN,
        creator: str | NotGiven = NOT_GIVEN,
        expiry: Union[str, datetime] | NotGiven = NOT_GIVEN,
        meta: object | NotGiven = NOT_GIVEN,
        require_signed_urls: bool | NotGiven = NOT_GIVEN,
        scheduled_deletion: Union[str, datetime] | NotGiven = NOT_GIVEN,
        thumbnail_timestamp_pct: float | NotGiven = NOT_GIVEN,
        watermark: direct_upload_create_params.Watermark | NotGiven = NOT_GIVEN,
        upload_creator: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DirectUploadCreateResponse]:
        """
        Creates a direct upload that allows video uploads without an API key.

        Args:
          account_id: The account identifier tag.

          max_duration_seconds: The maximum duration in seconds for a video upload. Can be set for a video that
              is not yet uploaded to limit its duration. Uploads that exceed the specified
              duration will fail during processing. A value of `-1` means the value is
              unknown.

          allowed_origins: Lists the origins allowed to display the video. Enter allowed origin domains in
              an array and use `*` for wildcard subdomains. Empty arrays allow the video to be
              viewed on any origin.

          creator: A user-defined identifier for the media creator.

          expiry: The date and time after upload when videos will not be accepted.

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {**strip_not_given({"Upload-Creator": upload_creator}), **(extra_headers or {})}
        return self._post(
            f"/accounts/{account_id}/stream/direct_upload",
            body=maybe_transform(
                {
                    "max_duration_seconds": max_duration_seconds,
                    "allowed_origins": allowed_origins,
                    "creator": creator,
                    "expiry": expiry,
                    "meta": meta,
                    "require_signed_urls": require_signed_urls,
                    "scheduled_deletion": scheduled_deletion,
                    "thumbnail_timestamp_pct": thumbnail_timestamp_pct,
                    "watermark": watermark,
                },
                direct_upload_create_params.DirectUploadCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DirectUploadCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DirectUploadCreateResponse]], ResultWrapper[DirectUploadCreateResponse]),
        )


class AsyncDirectUploadResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDirectUploadResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDirectUploadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDirectUploadResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDirectUploadResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        max_duration_seconds: int,
        allowed_origins: List[AllowedOrigins] | NotGiven = NOT_GIVEN,
        creator: str | NotGiven = NOT_GIVEN,
        expiry: Union[str, datetime] | NotGiven = NOT_GIVEN,
        meta: object | NotGiven = NOT_GIVEN,
        require_signed_urls: bool | NotGiven = NOT_GIVEN,
        scheduled_deletion: Union[str, datetime] | NotGiven = NOT_GIVEN,
        thumbnail_timestamp_pct: float | NotGiven = NOT_GIVEN,
        watermark: direct_upload_create_params.Watermark | NotGiven = NOT_GIVEN,
        upload_creator: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DirectUploadCreateResponse]:
        """
        Creates a direct upload that allows video uploads without an API key.

        Args:
          account_id: The account identifier tag.

          max_duration_seconds: The maximum duration in seconds for a video upload. Can be set for a video that
              is not yet uploaded to limit its duration. Uploads that exceed the specified
              duration will fail during processing. A value of `-1` means the value is
              unknown.

          allowed_origins: Lists the origins allowed to display the video. Enter allowed origin domains in
              an array and use `*` for wildcard subdomains. Empty arrays allow the video to be
              viewed on any origin.

          creator: A user-defined identifier for the media creator.

          expiry: The date and time after upload when videos will not be accepted.

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {**strip_not_given({"Upload-Creator": upload_creator}), **(extra_headers or {})}
        return await self._post(
            f"/accounts/{account_id}/stream/direct_upload",
            body=await async_maybe_transform(
                {
                    "max_duration_seconds": max_duration_seconds,
                    "allowed_origins": allowed_origins,
                    "creator": creator,
                    "expiry": expiry,
                    "meta": meta,
                    "require_signed_urls": require_signed_urls,
                    "scheduled_deletion": scheduled_deletion,
                    "thumbnail_timestamp_pct": thumbnail_timestamp_pct,
                    "watermark": watermark,
                },
                direct_upload_create_params.DirectUploadCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DirectUploadCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DirectUploadCreateResponse]], ResultWrapper[DirectUploadCreateResponse]),
        )


class DirectUploadResourceWithRawResponse:
    def __init__(self, direct_upload: DirectUploadResource) -> None:
        self._direct_upload = direct_upload

        self.create = to_raw_response_wrapper(
            direct_upload.create,
        )


class AsyncDirectUploadResourceWithRawResponse:
    def __init__(self, direct_upload: AsyncDirectUploadResource) -> None:
        self._direct_upload = direct_upload

        self.create = async_to_raw_response_wrapper(
            direct_upload.create,
        )


class DirectUploadResourceWithStreamingResponse:
    def __init__(self, direct_upload: DirectUploadResource) -> None:
        self._direct_upload = direct_upload

        self.create = to_streamed_response_wrapper(
            direct_upload.create,
        )


class AsyncDirectUploadResourceWithStreamingResponse:
    def __init__(self, direct_upload: AsyncDirectUploadResource) -> None:
        self._direct_upload = direct_upload

        self.create = async_to_streamed_response_wrapper(
            direct_upload.create,
        )
