# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
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
from ...types.zones import transformations_allowed_origin_edit_params
from ..._base_client import make_request_options
from ...types.zones.transformations_allowed_origins import TransformationsAllowedOrigins

__all__ = ["TransformationsAllowedOriginsResource", "AsyncTransformationsAllowedOriginsResource"]


class TransformationsAllowedOriginsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TransformationsAllowedOriginsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TransformationsAllowedOriginsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransformationsAllowedOriginsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TransformationsAllowedOriginsResourceWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[TransformationsAllowedOrigins]:
        """
        Media Transformations Allowed Origins restricts transformations for images and
        video served through Cloudflare's network to requests originating from specified
        domains. Refer to the Image Transformations and Video Transformations
        documentation for more information.

        Args:
          zone_id: Identifier.

          value: Comma-separated list of allowed origin domains for image and video
              transformations. Use "\\**" to allow all origins (default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            path_template("/zones/{zone_id}/settings/transformations_allowed_origins", zone_id=zone_id),
            body=maybe_transform(
                {"value": value}, transformations_allowed_origin_edit_params.TransformationsAllowedOriginEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TransformationsAllowedOrigins]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TransformationsAllowedOrigins]], ResultWrapper[TransformationsAllowedOrigins]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[TransformationsAllowedOrigins]:
        """
        Media Transformations Allowed Origins restricts transformations for images and
        video served through Cloudflare's network to requests originating from specified
        domains. Refer to the Image Transformations and Video Transformations
        documentation for more information.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            path_template("/zones/{zone_id}/settings/transformations_allowed_origins", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TransformationsAllowedOrigins]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TransformationsAllowedOrigins]], ResultWrapper[TransformationsAllowedOrigins]),
        )


class AsyncTransformationsAllowedOriginsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTransformationsAllowedOriginsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTransformationsAllowedOriginsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransformationsAllowedOriginsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTransformationsAllowedOriginsResourceWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[TransformationsAllowedOrigins]:
        """
        Media Transformations Allowed Origins restricts transformations for images and
        video served through Cloudflare's network to requests originating from specified
        domains. Refer to the Image Transformations and Video Transformations
        documentation for more information.

        Args:
          zone_id: Identifier.

          value: Comma-separated list of allowed origin domains for image and video
              transformations. Use "\\**" to allow all origins (default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            path_template("/zones/{zone_id}/settings/transformations_allowed_origins", zone_id=zone_id),
            body=await async_maybe_transform(
                {"value": value}, transformations_allowed_origin_edit_params.TransformationsAllowedOriginEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TransformationsAllowedOrigins]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TransformationsAllowedOrigins]], ResultWrapper[TransformationsAllowedOrigins]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[TransformationsAllowedOrigins]:
        """
        Media Transformations Allowed Origins restricts transformations for images and
        video served through Cloudflare's network to requests originating from specified
        domains. Refer to the Image Transformations and Video Transformations
        documentation for more information.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            path_template("/zones/{zone_id}/settings/transformations_allowed_origins", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TransformationsAllowedOrigins]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TransformationsAllowedOrigins]], ResultWrapper[TransformationsAllowedOrigins]),
        )


class TransformationsAllowedOriginsResourceWithRawResponse:
    def __init__(self, transformations_allowed_origins: TransformationsAllowedOriginsResource) -> None:
        self._transformations_allowed_origins = transformations_allowed_origins

        self.edit = to_raw_response_wrapper(
            transformations_allowed_origins.edit,
        )
        self.get = to_raw_response_wrapper(
            transformations_allowed_origins.get,
        )


class AsyncTransformationsAllowedOriginsResourceWithRawResponse:
    def __init__(self, transformations_allowed_origins: AsyncTransformationsAllowedOriginsResource) -> None:
        self._transformations_allowed_origins = transformations_allowed_origins

        self.edit = async_to_raw_response_wrapper(
            transformations_allowed_origins.edit,
        )
        self.get = async_to_raw_response_wrapper(
            transformations_allowed_origins.get,
        )


class TransformationsAllowedOriginsResourceWithStreamingResponse:
    def __init__(self, transformations_allowed_origins: TransformationsAllowedOriginsResource) -> None:
        self._transformations_allowed_origins = transformations_allowed_origins

        self.edit = to_streamed_response_wrapper(
            transformations_allowed_origins.edit,
        )
        self.get = to_streamed_response_wrapper(
            transformations_allowed_origins.get,
        )


class AsyncTransformationsAllowedOriginsResourceWithStreamingResponse:
    def __init__(self, transformations_allowed_origins: AsyncTransformationsAllowedOriginsResource) -> None:
        self._transformations_allowed_origins = transformations_allowed_origins

        self.edit = async_to_streamed_response_wrapper(
            transformations_allowed_origins.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            transformations_allowed_origins.get,
        )
