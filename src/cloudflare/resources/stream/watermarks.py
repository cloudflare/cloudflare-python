# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.stream import (
    WatermarkDeleteResponse,
    WatermarkGetResponse,
    WatermarkStreamWatermarkProfileCreateWatermarkProfilesViaBasicUploadResponse,
    WatermarkStreamWatermarkProfileListWatermarkProfilesResponse,
)

from typing import Type

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.stream import watermark_stream_watermark_profile_create_watermark_profiles_via_basic_upload_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Watermarks", "AsyncWatermarks"]


class Watermarks(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WatermarksWithRawResponse:
        return WatermarksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WatermarksWithStreamingResponse:
        return WatermarksWithStreamingResponse(self)

    def delete(
        self,
        identifier: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WatermarkDeleteResponse:
        """
        Deletes a watermark profile.

        Args:
          account_id: The account identifier tag.

          identifier: The unique identifier for a watermark profile.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return cast(
            WatermarkDeleteResponse,
            self._delete(
                f"/accounts/{account_id}/stream/watermarks/{identifier}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[WatermarkDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        identifier: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WatermarkGetResponse:
        """
        Retrieves details for a single watermark profile.

        Args:
          account_id: The account identifier tag.

          identifier: The unique identifier for a watermark profile.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return cast(
            WatermarkGetResponse,
            self._get(
                f"/accounts/{account_id}/stream/watermarks/{identifier}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[WatermarkGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def stream_watermark_profile_create_watermark_profiles_via_basic_upload(
        self,
        account_id: str,
        *,
        file: str,
        name: str | NotGiven = NOT_GIVEN,
        opacity: float | NotGiven = NOT_GIVEN,
        padding: float | NotGiven = NOT_GIVEN,
        position: str | NotGiven = NOT_GIVEN,
        scale: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WatermarkStreamWatermarkProfileCreateWatermarkProfilesViaBasicUploadResponse:
        """
        Creates watermark profiles using a single `HTTP POST multipart/form-data`
        request.

        Args:
          account_id: The account identifier tag.

          file: The image file to upload.

          name: A short description of the watermark profile.

          opacity: The translucency of the image. A value of `0.0` makes the image completely
              transparent, and `1.0` makes the image completely opaque. Note that if the image
              is already semi-transparent, setting this to `1.0` will not make the image
              completely opaque.

          padding: The whitespace between the adjacent edges (determined by position) of the video
              and the image. `0.0` indicates no padding, and `1.0` indicates a fully padded
              video width or length, as determined by the algorithm.

          position: The location of the image. Valid positions are: `upperRight`, `upperLeft`,
              `lowerLeft`, `lowerRight`, and `center`. Note that `center` ignores the
              `padding` parameter.

          scale: The size of the image relative to the overall size of the video. This parameter
              will adapt to horizontal and vertical videos automatically. `0.0` indicates no
              scaling (use the size of the image as-is), and `1.0 `fills the entire video.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            WatermarkStreamWatermarkProfileCreateWatermarkProfilesViaBasicUploadResponse,
            self._post(
                f"/accounts/{account_id}/stream/watermarks",
                body=maybe_transform(
                    {
                        "file": file,
                        "name": name,
                        "opacity": opacity,
                        "padding": padding,
                        "position": position,
                        "scale": scale,
                    },
                    watermark_stream_watermark_profile_create_watermark_profiles_via_basic_upload_params.WatermarkStreamWatermarkProfileCreateWatermarkProfilesViaBasicUploadParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[WatermarkStreamWatermarkProfileCreateWatermarkProfilesViaBasicUploadResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def stream_watermark_profile_list_watermark_profiles(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WatermarkStreamWatermarkProfileListWatermarkProfilesResponse:
        """
        Lists all watermark profiles for an account.

        Args:
          account_id: The account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/stream/watermarks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[WatermarkStreamWatermarkProfileListWatermarkProfilesResponse],
                ResultWrapper[WatermarkStreamWatermarkProfileListWatermarkProfilesResponse],
            ),
        )


class AsyncWatermarks(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWatermarksWithRawResponse:
        return AsyncWatermarksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWatermarksWithStreamingResponse:
        return AsyncWatermarksWithStreamingResponse(self)

    async def delete(
        self,
        identifier: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WatermarkDeleteResponse:
        """
        Deletes a watermark profile.

        Args:
          account_id: The account identifier tag.

          identifier: The unique identifier for a watermark profile.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return cast(
            WatermarkDeleteResponse,
            await self._delete(
                f"/accounts/{account_id}/stream/watermarks/{identifier}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[WatermarkDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        identifier: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WatermarkGetResponse:
        """
        Retrieves details for a single watermark profile.

        Args:
          account_id: The account identifier tag.

          identifier: The unique identifier for a watermark profile.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return cast(
            WatermarkGetResponse,
            await self._get(
                f"/accounts/{account_id}/stream/watermarks/{identifier}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[WatermarkGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def stream_watermark_profile_create_watermark_profiles_via_basic_upload(
        self,
        account_id: str,
        *,
        file: str,
        name: str | NotGiven = NOT_GIVEN,
        opacity: float | NotGiven = NOT_GIVEN,
        padding: float | NotGiven = NOT_GIVEN,
        position: str | NotGiven = NOT_GIVEN,
        scale: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WatermarkStreamWatermarkProfileCreateWatermarkProfilesViaBasicUploadResponse:
        """
        Creates watermark profiles using a single `HTTP POST multipart/form-data`
        request.

        Args:
          account_id: The account identifier tag.

          file: The image file to upload.

          name: A short description of the watermark profile.

          opacity: The translucency of the image. A value of `0.0` makes the image completely
              transparent, and `1.0` makes the image completely opaque. Note that if the image
              is already semi-transparent, setting this to `1.0` will not make the image
              completely opaque.

          padding: The whitespace between the adjacent edges (determined by position) of the video
              and the image. `0.0` indicates no padding, and `1.0` indicates a fully padded
              video width or length, as determined by the algorithm.

          position: The location of the image. Valid positions are: `upperRight`, `upperLeft`,
              `lowerLeft`, `lowerRight`, and `center`. Note that `center` ignores the
              `padding` parameter.

          scale: The size of the image relative to the overall size of the video. This parameter
              will adapt to horizontal and vertical videos automatically. `0.0` indicates no
              scaling (use the size of the image as-is), and `1.0 `fills the entire video.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            WatermarkStreamWatermarkProfileCreateWatermarkProfilesViaBasicUploadResponse,
            await self._post(
                f"/accounts/{account_id}/stream/watermarks",
                body=maybe_transform(
                    {
                        "file": file,
                        "name": name,
                        "opacity": opacity,
                        "padding": padding,
                        "position": position,
                        "scale": scale,
                    },
                    watermark_stream_watermark_profile_create_watermark_profiles_via_basic_upload_params.WatermarkStreamWatermarkProfileCreateWatermarkProfilesViaBasicUploadParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[WatermarkStreamWatermarkProfileCreateWatermarkProfilesViaBasicUploadResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def stream_watermark_profile_list_watermark_profiles(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WatermarkStreamWatermarkProfileListWatermarkProfilesResponse:
        """
        Lists all watermark profiles for an account.

        Args:
          account_id: The account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/stream/watermarks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[WatermarkStreamWatermarkProfileListWatermarkProfilesResponse],
                ResultWrapper[WatermarkStreamWatermarkProfileListWatermarkProfilesResponse],
            ),
        )


class WatermarksWithRawResponse:
    def __init__(self, watermarks: Watermarks) -> None:
        self._watermarks = watermarks

        self.delete = to_raw_response_wrapper(
            watermarks.delete,
        )
        self.get = to_raw_response_wrapper(
            watermarks.get,
        )
        self.stream_watermark_profile_create_watermark_profiles_via_basic_upload = to_raw_response_wrapper(
            watermarks.stream_watermark_profile_create_watermark_profiles_via_basic_upload,
        )
        self.stream_watermark_profile_list_watermark_profiles = to_raw_response_wrapper(
            watermarks.stream_watermark_profile_list_watermark_profiles,
        )


class AsyncWatermarksWithRawResponse:
    def __init__(self, watermarks: AsyncWatermarks) -> None:
        self._watermarks = watermarks

        self.delete = async_to_raw_response_wrapper(
            watermarks.delete,
        )
        self.get = async_to_raw_response_wrapper(
            watermarks.get,
        )
        self.stream_watermark_profile_create_watermark_profiles_via_basic_upload = async_to_raw_response_wrapper(
            watermarks.stream_watermark_profile_create_watermark_profiles_via_basic_upload,
        )
        self.stream_watermark_profile_list_watermark_profiles = async_to_raw_response_wrapper(
            watermarks.stream_watermark_profile_list_watermark_profiles,
        )


class WatermarksWithStreamingResponse:
    def __init__(self, watermarks: Watermarks) -> None:
        self._watermarks = watermarks

        self.delete = to_streamed_response_wrapper(
            watermarks.delete,
        )
        self.get = to_streamed_response_wrapper(
            watermarks.get,
        )
        self.stream_watermark_profile_create_watermark_profiles_via_basic_upload = to_streamed_response_wrapper(
            watermarks.stream_watermark_profile_create_watermark_profiles_via_basic_upload,
        )
        self.stream_watermark_profile_list_watermark_profiles = to_streamed_response_wrapper(
            watermarks.stream_watermark_profile_list_watermark_profiles,
        )


class AsyncWatermarksWithStreamingResponse:
    def __init__(self, watermarks: AsyncWatermarks) -> None:
        self._watermarks = watermarks

        self.delete = async_to_streamed_response_wrapper(
            watermarks.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            watermarks.get,
        )
        self.stream_watermark_profile_create_watermark_profiles_via_basic_upload = async_to_streamed_response_wrapper(
            watermarks.stream_watermark_profile_create_watermark_profiles_via_basic_upload,
        )
        self.stream_watermark_profile_list_watermark_profiles = async_to_streamed_response_wrapper(
            watermarks.stream_watermark_profile_list_watermark_profiles,
        )
