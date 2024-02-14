# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.settings import ImageResizingUpdateResponse, ImageResizingGetResponse, image_resizing_update_params

from typing import Type, Optional

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
from ...types.settings import image_resizing_update_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["ImageResizing", "AsyncImageResizing"]


class ImageResizing(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ImageResizingWithRawResponse:
        return ImageResizingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImageResizingWithStreamingResponse:
        return ImageResizingWithStreamingResponse(self)

    def update(
        self,
        zone_id: str,
        *,
        value: image_resizing_update_params.Value,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ImageResizingUpdateResponse]:
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
            body=maybe_transform({"value": value}, image_resizing_update_params.ImageResizingUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ImageResizingUpdateResponse]], ResultWrapper[ImageResizingUpdateResponse]),
        )

    def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ImageResizingGetResponse]:
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
            cast_to=cast(Type[Optional[ImageResizingGetResponse]], ResultWrapper[ImageResizingGetResponse]),
        )


class AsyncImageResizing(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncImageResizingWithRawResponse:
        return AsyncImageResizingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImageResizingWithStreamingResponse:
        return AsyncImageResizingWithStreamingResponse(self)

    async def update(
        self,
        zone_id: str,
        *,
        value: image_resizing_update_params.Value,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ImageResizingUpdateResponse]:
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
            body=maybe_transform({"value": value}, image_resizing_update_params.ImageResizingUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ImageResizingUpdateResponse]], ResultWrapper[ImageResizingUpdateResponse]),
        )

    async def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ImageResizingGetResponse]:
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
            cast_to=cast(Type[Optional[ImageResizingGetResponse]], ResultWrapper[ImageResizingGetResponse]),
        )


class ImageResizingWithRawResponse:
    def __init__(self, image_resizing: ImageResizing) -> None:
        self._image_resizing = image_resizing

        self.update = to_raw_response_wrapper(
            image_resizing.update,
        )
        self.get = to_raw_response_wrapper(
            image_resizing.get,
        )


class AsyncImageResizingWithRawResponse:
    def __init__(self, image_resizing: AsyncImageResizing) -> None:
        self._image_resizing = image_resizing

        self.update = async_to_raw_response_wrapper(
            image_resizing.update,
        )
        self.get = async_to_raw_response_wrapper(
            image_resizing.get,
        )


class ImageResizingWithStreamingResponse:
    def __init__(self, image_resizing: ImageResizing) -> None:
        self._image_resizing = image_resizing

        self.update = to_streamed_response_wrapper(
            image_resizing.update,
        )
        self.get = to_streamed_response_wrapper(
            image_resizing.get,
        )


class AsyncImageResizingWithStreamingResponse:
    def __init__(self, image_resizing: AsyncImageResizing) -> None:
        self._image_resizing = image_resizing

        self.update = async_to_streamed_response_wrapper(
            image_resizing.update,
        )
        self.get = async_to_streamed_response_wrapper(
            image_resizing.get,
        )
