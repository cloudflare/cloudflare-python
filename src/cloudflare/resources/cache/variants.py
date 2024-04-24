# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

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
from ...types.cache import variant_edit_params
from ..._base_client import (
    make_request_options,
)
from ...types.cache.cache_variant import CacheVariant
from ...types.cache.variant_get_response import VariantGetResponse
from ...types.cache.variant_edit_response import VariantEditResponse

__all__ = ["VariantsResource", "AsyncVariantsResource"]


class VariantsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VariantsResourceWithRawResponse:
        return VariantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VariantsResourceWithStreamingResponse:
        return VariantsResourceWithStreamingResponse(self)

    def delete(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CacheVariant:
        """
        Variant support enables caching variants of images with certain file extensions
        in addition to the original. This only applies when the origin server sends the
        'Vary: Accept' response header. If the origin server sends 'Vary: Accept' but
        does not serve the variant requested, the response will not be cached. This will
        be indicated with BYPASS cache status in the response headers.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._delete(
            f"/zones/{zone_id}/cache/variants",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CacheVariant]._unwrapper,
            ),
            cast_to=cast(Type[CacheVariant], ResultWrapper[CacheVariant]),
        )

    def edit(
        self,
        *,
        zone_id: str,
        value: variant_edit_params.Value,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VariantEditResponse:
        """
        Variant support enables caching variants of images with certain file extensions
        in addition to the original. This only applies when the origin server sends the
        'Vary: Accept' response header. If the origin server sends 'Vary: Accept' but
        does not serve the variant requested, the response will not be cached. This will
        be indicated with BYPASS cache status in the response headers.

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/cache/variants",
            body=maybe_transform({"value": value}, variant_edit_params.VariantEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[VariantEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[VariantEditResponse], ResultWrapper[VariantEditResponse]),
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
    ) -> VariantGetResponse:
        """
        Variant support enables caching variants of images with certain file extensions
        in addition to the original. This only applies when the origin server sends the
        'Vary: Accept' response header. If the origin server sends 'Vary: Accept' but
        does not serve the variant requested, the response will not be cached. This will
        be indicated with BYPASS cache status in the response headers.

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
            f"/zones/{zone_id}/cache/variants",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[VariantGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[VariantGetResponse], ResultWrapper[VariantGetResponse]),
        )


class AsyncVariantsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVariantsResourceWithRawResponse:
        return AsyncVariantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVariantsResourceWithStreamingResponse:
        return AsyncVariantsResourceWithStreamingResponse(self)

    async def delete(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CacheVariant:
        """
        Variant support enables caching variants of images with certain file extensions
        in addition to the original. This only applies when the origin server sends the
        'Vary: Accept' response header. If the origin server sends 'Vary: Accept' but
        does not serve the variant requested, the response will not be cached. This will
        be indicated with BYPASS cache status in the response headers.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._delete(
            f"/zones/{zone_id}/cache/variants",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CacheVariant]._unwrapper,
            ),
            cast_to=cast(Type[CacheVariant], ResultWrapper[CacheVariant]),
        )

    async def edit(
        self,
        *,
        zone_id: str,
        value: variant_edit_params.Value,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VariantEditResponse:
        """
        Variant support enables caching variants of images with certain file extensions
        in addition to the original. This only applies when the origin server sends the
        'Vary: Accept' response header. If the origin server sends 'Vary: Accept' but
        does not serve the variant requested, the response will not be cached. This will
        be indicated with BYPASS cache status in the response headers.

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/cache/variants",
            body=await async_maybe_transform({"value": value}, variant_edit_params.VariantEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[VariantEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[VariantEditResponse], ResultWrapper[VariantEditResponse]),
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
    ) -> VariantGetResponse:
        """
        Variant support enables caching variants of images with certain file extensions
        in addition to the original. This only applies when the origin server sends the
        'Vary: Accept' response header. If the origin server sends 'Vary: Accept' but
        does not serve the variant requested, the response will not be cached. This will
        be indicated with BYPASS cache status in the response headers.

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
            f"/zones/{zone_id}/cache/variants",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[VariantGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[VariantGetResponse], ResultWrapper[VariantGetResponse]),
        )


class VariantsResourceWithRawResponse:
    def __init__(self, variants: VariantsResource) -> None:
        self._variants = variants

        self.delete = to_raw_response_wrapper(
            variants.delete,
        )
        self.edit = to_raw_response_wrapper(
            variants.edit,
        )
        self.get = to_raw_response_wrapper(
            variants.get,
        )


class AsyncVariantsResourceWithRawResponse:
    def __init__(self, variants: AsyncVariantsResource) -> None:
        self._variants = variants

        self.delete = async_to_raw_response_wrapper(
            variants.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            variants.edit,
        )
        self.get = async_to_raw_response_wrapper(
            variants.get,
        )


class VariantsResourceWithStreamingResponse:
    def __init__(self, variants: VariantsResource) -> None:
        self._variants = variants

        self.delete = to_streamed_response_wrapper(
            variants.delete,
        )
        self.edit = to_streamed_response_wrapper(
            variants.edit,
        )
        self.get = to_streamed_response_wrapper(
            variants.get,
        )


class AsyncVariantsResourceWithStreamingResponse:
    def __init__(self, variants: AsyncVariantsResource) -> None:
        self._variants = variants

        self.delete = async_to_streamed_response_wrapper(
            variants.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            variants.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            variants.get,
        )
