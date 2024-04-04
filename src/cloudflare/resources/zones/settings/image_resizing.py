# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
from ....types.zones.settings import ImageResizing, ImageResizingParam, image_resizing_edit_params

__all__ = ["ImageResizingResource", "AsyncImageResizingResource"]


class ImageResizingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ImageResizingResourceWithRawResponse:
        return ImageResizingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImageResizingResourceWithStreamingResponse:
        return ImageResizingResourceWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: ImageResizingParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ImageResizing]:
        """
        Image Resizing provides on-demand resizing, conversion and optimisation for
        images served through Cloudflare's network. Refer to the
        [Image Resizing documentation](https://developers.cloudflare.com/images/) for
        more information.

        Args:
          zone_id: Identifier

          value: Image Resizing provides on-demand resizing, conversion and optimisation for
              images served through Cloudflare's network. Refer to the
              [Image Resizing documentation](https://developers.cloudflare.com/images/) for
              more information.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/image_resizing",
            body=maybe_transform({"value": value}, image_resizing_edit_params.ImageResizingEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ImageResizing]], ResultWrapper[ImageResizing]),
        )

    def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ImageResizing]:
        """
        Image Resizing provides on-demand resizing, conversion and optimisation for
        images served through Cloudflare's network. Refer to the
        [Image Resizing documentation](https://developers.cloudflare.com/images/) for
        more information.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/settings/image_resizing",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ImageResizing]], ResultWrapper[ImageResizing]),
        )


class AsyncImageResizingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncImageResizingResourceWithRawResponse:
        return AsyncImageResizingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImageResizingResourceWithStreamingResponse:
        return AsyncImageResizingResourceWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: ImageResizingParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ImageResizing]:
        """
        Image Resizing provides on-demand resizing, conversion and optimisation for
        images served through Cloudflare's network. Refer to the
        [Image Resizing documentation](https://developers.cloudflare.com/images/) for
        more information.

        Args:
          zone_id: Identifier

          value: Image Resizing provides on-demand resizing, conversion and optimisation for
              images served through Cloudflare's network. Refer to the
              [Image Resizing documentation](https://developers.cloudflare.com/images/) for
              more information.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/image_resizing",
            body=await async_maybe_transform({"value": value}, image_resizing_edit_params.ImageResizingEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ImageResizing]], ResultWrapper[ImageResizing]),
        )

    async def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ImageResizing]:
        """
        Image Resizing provides on-demand resizing, conversion and optimisation for
        images served through Cloudflare's network. Refer to the
        [Image Resizing documentation](https://developers.cloudflare.com/images/) for
        more information.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/settings/image_resizing",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ImageResizing]], ResultWrapper[ImageResizing]),
        )


class ImageResizingResourceWithRawResponse:
    def __init__(self, image_resizing: ImageResizingResource) -> None:
        self._image_resizing = image_resizing

        self.edit = to_raw_response_wrapper(
            image_resizing.edit,
        )
        self.get = to_raw_response_wrapper(
            image_resizing.get,
        )


class AsyncImageResizingResourceWithRawResponse:
    def __init__(self, image_resizing: AsyncImageResizingResource) -> None:
        self._image_resizing = image_resizing

        self.edit = async_to_raw_response_wrapper(
            image_resizing.edit,
        )
        self.get = async_to_raw_response_wrapper(
            image_resizing.get,
        )


class ImageResizingResourceWithStreamingResponse:
    def __init__(self, image_resizing: ImageResizingResource) -> None:
        self._image_resizing = image_resizing

        self.edit = to_streamed_response_wrapper(
            image_resizing.edit,
        )
        self.get = to_streamed_response_wrapper(
            image_resizing.get,
        )


class AsyncImageResizingResourceWithStreamingResponse:
    def __init__(self, image_resizing: AsyncImageResizingResource) -> None:
        self._image_resizing = image_resizing

        self.edit = async_to_streamed_response_wrapper(
            image_resizing.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            image_resizing.get,
        )
