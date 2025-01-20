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
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.stream import watermark_create_params
from ...types.stream.watermark import Watermark
from ...types.stream.watermark_delete_response import WatermarkDeleteResponse

__all__ = ["WatermarksResource", "AsyncWatermarksResource"]


class WatermarksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WatermarksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return WatermarksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WatermarksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return WatermarksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
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
    ) -> Optional[Watermark]:
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
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
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
                watermark_create_params.WatermarkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Watermark]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Watermark]], ResultWrapper[Watermark]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[Watermark]:
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
        return self._get_api_list(
            f"/accounts/{account_id}/stream/watermarks",
            page=SyncSinglePage[Watermark],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Watermark,
        )

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
    ) -> str:
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
        return self._delete(
            f"/accounts/{account_id}/stream/watermarks/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[WatermarkDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
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
    ) -> Optional[Watermark]:
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
        return self._get(
            f"/accounts/{account_id}/stream/watermarks/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Watermark]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Watermark]], ResultWrapper[Watermark]),
        )


class AsyncWatermarksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWatermarksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWatermarksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWatermarksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncWatermarksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
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
    ) -> Optional[Watermark]:
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
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            f"/accounts/{account_id}/stream/watermarks",
            body=await async_maybe_transform(
                {
                    "file": file,
                    "name": name,
                    "opacity": opacity,
                    "padding": padding,
                    "position": position,
                    "scale": scale,
                },
                watermark_create_params.WatermarkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Watermark]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Watermark]], ResultWrapper[Watermark]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Watermark, AsyncSinglePage[Watermark]]:
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
        return self._get_api_list(
            f"/accounts/{account_id}/stream/watermarks",
            page=AsyncSinglePage[Watermark],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Watermark,
        )

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
    ) -> str:
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
        return await self._delete(
            f"/accounts/{account_id}/stream/watermarks/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[WatermarkDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
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
    ) -> Optional[Watermark]:
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
        return await self._get(
            f"/accounts/{account_id}/stream/watermarks/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Watermark]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Watermark]], ResultWrapper[Watermark]),
        )


class WatermarksResourceWithRawResponse:
    def __init__(self, watermarks: WatermarksResource) -> None:
        self._watermarks = watermarks

        self.create = to_raw_response_wrapper(
            watermarks.create,
        )
        self.list = to_raw_response_wrapper(
            watermarks.list,
        )
        self.delete = to_raw_response_wrapper(
            watermarks.delete,
        )
        self.get = to_raw_response_wrapper(
            watermarks.get,
        )


class AsyncWatermarksResourceWithRawResponse:
    def __init__(self, watermarks: AsyncWatermarksResource) -> None:
        self._watermarks = watermarks

        self.create = async_to_raw_response_wrapper(
            watermarks.create,
        )
        self.list = async_to_raw_response_wrapper(
            watermarks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            watermarks.delete,
        )
        self.get = async_to_raw_response_wrapper(
            watermarks.get,
        )


class WatermarksResourceWithStreamingResponse:
    def __init__(self, watermarks: WatermarksResource) -> None:
        self._watermarks = watermarks

        self.create = to_streamed_response_wrapper(
            watermarks.create,
        )
        self.list = to_streamed_response_wrapper(
            watermarks.list,
        )
        self.delete = to_streamed_response_wrapper(
            watermarks.delete,
        )
        self.get = to_streamed_response_wrapper(
            watermarks.get,
        )


class AsyncWatermarksResourceWithStreamingResponse:
    def __init__(self, watermarks: AsyncWatermarksResource) -> None:
        self._watermarks = watermarks

        self.create = async_to_streamed_response_wrapper(
            watermarks.create,
        )
        self.list = async_to_streamed_response_wrapper(
            watermarks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            watermarks.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            watermarks.get,
        )
