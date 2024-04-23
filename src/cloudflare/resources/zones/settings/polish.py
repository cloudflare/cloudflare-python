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
from ....types.zones.settings import Polish, polish_edit_params
from ....types.zones.settings.polish import Polish
from ....types.zones.settings.polish_param import PolishParam

__all__ = ["PolishResource", "AsyncPolishResource"]


class PolishResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PolishResourceWithRawResponse:
        return PolishResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PolishResourceWithStreamingResponse:
        return PolishResourceWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: PolishParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Polish]:
        """
        Automatically optimize image loading for website visitors on mobile devices.
        Refer to our [blog post](http://blog.cloudflare.com/polish-solving-mobile-speed)
        for more information.

        Args:
          zone_id: Identifier

          value: Removes metadata and compresses your images for faster page load times. Basic
              (Lossless): Reduce the size of PNG, JPEG, and GIF files - no impact on visual
              quality. Basic + JPEG (Lossy): Further reduce the size of JPEG files for faster
              image loading. Larger JPEGs are converted to progressive images, loading a
              lower-resolution image first and ending in a higher-resolution version. Not
              recommended for hi-res photography sites.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/polish",
            body=maybe_transform({"value": value}, polish_edit_params.PolishEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Polish]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Polish]], ResultWrapper[Polish]),
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
    ) -> Optional[Polish]:
        """
        Automatically optimize image loading for website visitors on mobile devices.
        Refer to our [blog post](http://blog.cloudflare.com/polish-solving-mobile-speed)
        for more information.

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
            f"/zones/{zone_id}/settings/polish",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Polish]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Polish]], ResultWrapper[Polish]),
        )


class AsyncPolishResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPolishResourceWithRawResponse:
        return AsyncPolishResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPolishResourceWithStreamingResponse:
        return AsyncPolishResourceWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: PolishParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Polish]:
        """
        Automatically optimize image loading for website visitors on mobile devices.
        Refer to our [blog post](http://blog.cloudflare.com/polish-solving-mobile-speed)
        for more information.

        Args:
          zone_id: Identifier

          value: Removes metadata and compresses your images for faster page load times. Basic
              (Lossless): Reduce the size of PNG, JPEG, and GIF files - no impact on visual
              quality. Basic + JPEG (Lossy): Further reduce the size of JPEG files for faster
              image loading. Larger JPEGs are converted to progressive images, loading a
              lower-resolution image first and ending in a higher-resolution version. Not
              recommended for hi-res photography sites.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/polish",
            body=await async_maybe_transform({"value": value}, polish_edit_params.PolishEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Polish]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Polish]], ResultWrapper[Polish]),
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
    ) -> Optional[Polish]:
        """
        Automatically optimize image loading for website visitors on mobile devices.
        Refer to our [blog post](http://blog.cloudflare.com/polish-solving-mobile-speed)
        for more information.

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
            f"/zones/{zone_id}/settings/polish",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Polish]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Polish]], ResultWrapper[Polish]),
        )


class PolishResourceWithRawResponse:
    def __init__(self, polish: PolishResource) -> None:
        self._polish = polish

        self.edit = to_raw_response_wrapper(
            polish.edit,
        )
        self.get = to_raw_response_wrapper(
            polish.get,
        )


class AsyncPolishResourceWithRawResponse:
    def __init__(self, polish: AsyncPolishResource) -> None:
        self._polish = polish

        self.edit = async_to_raw_response_wrapper(
            polish.edit,
        )
        self.get = async_to_raw_response_wrapper(
            polish.get,
        )


class PolishResourceWithStreamingResponse:
    def __init__(self, polish: PolishResource) -> None:
        self._polish = polish

        self.edit = to_streamed_response_wrapper(
            polish.edit,
        )
        self.get = to_streamed_response_wrapper(
            polish.get,
        )


class AsyncPolishResourceWithStreamingResponse:
    def __init__(self, polish: AsyncPolishResource) -> None:
        self._polish = polish

        self.edit = async_to_streamed_response_wrapper(
            polish.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            polish.get,
        )
