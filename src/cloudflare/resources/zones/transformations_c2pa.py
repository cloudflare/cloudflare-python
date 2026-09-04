# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

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
from ...types.zones import transformations_c2pa_edit_params
from ..._base_client import make_request_options
from ...types.zones.transformations_c2pa import TransformationsC2pa

__all__ = ["TransformationsC2paResource", "AsyncTransformationsC2paResource"]


class TransformationsC2paResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TransformationsC2paResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TransformationsC2paResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransformationsC2paResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TransformationsC2paResourceWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: Literal["off", "on"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[TransformationsC2pa]:
        """
        C2PA (Coalition for Content Provenance and Authenticity) signing adds
        cryptographic metadata to images processed through Cloudflare Image
        Transformations, enabling verification of image authenticity and provenance.

        Args:
          zone_id: Identifier.

          value: Whether C2PA signing is enabled for image transformations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            path_template("/zones/{zone_id}/settings/transformations_c2pa", zone_id=zone_id),
            body=maybe_transform({"value": value}, transformations_c2pa_edit_params.TransformationsC2paEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TransformationsC2pa]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TransformationsC2pa]], ResultWrapper[TransformationsC2pa]),
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
    ) -> Optional[TransformationsC2pa]:
        """
        C2PA (Coalition for Content Provenance and Authenticity) signing adds
        cryptographic metadata to images processed through Cloudflare Image
        Transformations, enabling verification of image authenticity and provenance.

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
            path_template("/zones/{zone_id}/settings/transformations_c2pa", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TransformationsC2pa]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TransformationsC2pa]], ResultWrapper[TransformationsC2pa]),
        )


class AsyncTransformationsC2paResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTransformationsC2paResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTransformationsC2paResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransformationsC2paResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTransformationsC2paResourceWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: Literal["off", "on"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[TransformationsC2pa]:
        """
        C2PA (Coalition for Content Provenance and Authenticity) signing adds
        cryptographic metadata to images processed through Cloudflare Image
        Transformations, enabling verification of image authenticity and provenance.

        Args:
          zone_id: Identifier.

          value: Whether C2PA signing is enabled for image transformations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            path_template("/zones/{zone_id}/settings/transformations_c2pa", zone_id=zone_id),
            body=await async_maybe_transform(
                {"value": value}, transformations_c2pa_edit_params.TransformationsC2paEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TransformationsC2pa]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TransformationsC2pa]], ResultWrapper[TransformationsC2pa]),
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
    ) -> Optional[TransformationsC2pa]:
        """
        C2PA (Coalition for Content Provenance and Authenticity) signing adds
        cryptographic metadata to images processed through Cloudflare Image
        Transformations, enabling verification of image authenticity and provenance.

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
            path_template("/zones/{zone_id}/settings/transformations_c2pa", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TransformationsC2pa]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TransformationsC2pa]], ResultWrapper[TransformationsC2pa]),
        )


class TransformationsC2paResourceWithRawResponse:
    def __init__(self, transformations_c2pa: TransformationsC2paResource) -> None:
        self._transformations_c2pa = transformations_c2pa

        self.edit = to_raw_response_wrapper(
            transformations_c2pa.edit,
        )
        self.get = to_raw_response_wrapper(
            transformations_c2pa.get,
        )


class AsyncTransformationsC2paResourceWithRawResponse:
    def __init__(self, transformations_c2pa: AsyncTransformationsC2paResource) -> None:
        self._transformations_c2pa = transformations_c2pa

        self.edit = async_to_raw_response_wrapper(
            transformations_c2pa.edit,
        )
        self.get = async_to_raw_response_wrapper(
            transformations_c2pa.get,
        )


class TransformationsC2paResourceWithStreamingResponse:
    def __init__(self, transformations_c2pa: TransformationsC2paResource) -> None:
        self._transformations_c2pa = transformations_c2pa

        self.edit = to_streamed_response_wrapper(
            transformations_c2pa.edit,
        )
        self.get = to_streamed_response_wrapper(
            transformations_c2pa.get,
        )


class AsyncTransformationsC2paResourceWithStreamingResponse:
    def __init__(self, transformations_c2pa: AsyncTransformationsC2paResource) -> None:
        self._transformations_c2pa = transformations_c2pa

        self.edit = async_to_streamed_response_wrapper(
            transformations_c2pa.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            transformations_c2pa.get,
        )
