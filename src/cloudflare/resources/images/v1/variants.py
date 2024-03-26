# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, cast

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
from ....types.images.v1 import (
    ImageVariant,
    ImageVariants,
    VariantDeleteResponse,
    variant_edit_params,
    variant_create_params,
)

__all__ = ["Variants", "AsyncVariants"]


class Variants(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VariantsWithRawResponse:
        return VariantsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VariantsWithStreamingResponse:
        return VariantsWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        id: str,
        options: variant_create_params.Options,
        never_require_signed_urls: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImageVariant:
        """
        Specify variants that allow you to resize images for different use cases.

        Args:
          account_id: Account identifier tag.

          options: Allows you to define image resizing sizes for different use cases.

          never_require_signed_urls: Indicates whether the variant can access an image without a signature,
              regardless of image access control.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/images/v1/variants",
            body=maybe_transform(
                {
                    "id": id,
                    "options": options,
                    "never_require_signed_urls": never_require_signed_urls,
                },
                variant_create_params.VariantCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ImageVariant], ResultWrapper[ImageVariant]),
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
    ) -> ImageVariants:
        """
        Lists existing variants.

        Args:
          account_id: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/images/v1/variants",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ImageVariants], ResultWrapper[ImageVariants]),
        )

    def delete(
        self,
        variant_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VariantDeleteResponse:
        """
        Deleting a variant purges the cache for all images associated with the variant.

        Args:
          account_id: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not variant_id:
            raise ValueError(f"Expected a non-empty value for `variant_id` but received {variant_id!r}")
        return cast(
            VariantDeleteResponse,
            self._delete(
                f"/accounts/{account_id}/images/v1/variants/{variant_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[VariantDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def edit(
        self,
        variant_id: str,
        *,
        account_id: str,
        options: variant_edit_params.Options,
        never_require_signed_urls: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImageVariant:
        """
        Updating a variant purges the cache for all images associated with the variant.

        Args:
          account_id: Account identifier tag.

          options: Allows you to define image resizing sizes for different use cases.

          never_require_signed_urls: Indicates whether the variant can access an image without a signature,
              regardless of image access control.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not variant_id:
            raise ValueError(f"Expected a non-empty value for `variant_id` but received {variant_id!r}")
        return self._patch(
            f"/accounts/{account_id}/images/v1/variants/{variant_id}",
            body=maybe_transform(
                {
                    "options": options,
                    "never_require_signed_urls": never_require_signed_urls,
                },
                variant_edit_params.VariantEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ImageVariant], ResultWrapper[ImageVariant]),
        )

    def get(
        self,
        variant_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImageVariant:
        """
        Fetch details for a single variant.

        Args:
          account_id: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not variant_id:
            raise ValueError(f"Expected a non-empty value for `variant_id` but received {variant_id!r}")
        return self._get(
            f"/accounts/{account_id}/images/v1/variants/{variant_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ImageVariant], ResultWrapper[ImageVariant]),
        )


class AsyncVariants(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVariantsWithRawResponse:
        return AsyncVariantsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVariantsWithStreamingResponse:
        return AsyncVariantsWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        id: str,
        options: variant_create_params.Options,
        never_require_signed_urls: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImageVariant:
        """
        Specify variants that allow you to resize images for different use cases.

        Args:
          account_id: Account identifier tag.

          options: Allows you to define image resizing sizes for different use cases.

          never_require_signed_urls: Indicates whether the variant can access an image without a signature,
              regardless of image access control.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/images/v1/variants",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "options": options,
                    "never_require_signed_urls": never_require_signed_urls,
                },
                variant_create_params.VariantCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ImageVariant], ResultWrapper[ImageVariant]),
        )

    async def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImageVariants:
        """
        Lists existing variants.

        Args:
          account_id: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/images/v1/variants",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ImageVariants], ResultWrapper[ImageVariants]),
        )

    async def delete(
        self,
        variant_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VariantDeleteResponse:
        """
        Deleting a variant purges the cache for all images associated with the variant.

        Args:
          account_id: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not variant_id:
            raise ValueError(f"Expected a non-empty value for `variant_id` but received {variant_id!r}")
        return cast(
            VariantDeleteResponse,
            await self._delete(
                f"/accounts/{account_id}/images/v1/variants/{variant_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[VariantDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def edit(
        self,
        variant_id: str,
        *,
        account_id: str,
        options: variant_edit_params.Options,
        never_require_signed_urls: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImageVariant:
        """
        Updating a variant purges the cache for all images associated with the variant.

        Args:
          account_id: Account identifier tag.

          options: Allows you to define image resizing sizes for different use cases.

          never_require_signed_urls: Indicates whether the variant can access an image without a signature,
              regardless of image access control.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not variant_id:
            raise ValueError(f"Expected a non-empty value for `variant_id` but received {variant_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/images/v1/variants/{variant_id}",
            body=await async_maybe_transform(
                {
                    "options": options,
                    "never_require_signed_urls": never_require_signed_urls,
                },
                variant_edit_params.VariantEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ImageVariant], ResultWrapper[ImageVariant]),
        )

    async def get(
        self,
        variant_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImageVariant:
        """
        Fetch details for a single variant.

        Args:
          account_id: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not variant_id:
            raise ValueError(f"Expected a non-empty value for `variant_id` but received {variant_id!r}")
        return await self._get(
            f"/accounts/{account_id}/images/v1/variants/{variant_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ImageVariant], ResultWrapper[ImageVariant]),
        )


class VariantsWithRawResponse:
    def __init__(self, variants: Variants) -> None:
        self._variants = variants

        self.create = to_raw_response_wrapper(
            variants.create,
        )
        self.list = to_raw_response_wrapper(
            variants.list,
        )
        self.delete = to_raw_response_wrapper(
            variants.delete,
        )
        self.edit = to_raw_response_wrapper(
            variants.edit,
        )
        self.get = to_raw_response_wrapper(
            variants.get,
        )


class AsyncVariantsWithRawResponse:
    def __init__(self, variants: AsyncVariants) -> None:
        self._variants = variants

        self.create = async_to_raw_response_wrapper(
            variants.create,
        )
        self.list = async_to_raw_response_wrapper(
            variants.list,
        )
        self.delete = async_to_raw_response_wrapper(
            variants.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            variants.edit,
        )
        self.get = async_to_raw_response_wrapper(
            variants.get,
        )


class VariantsWithStreamingResponse:
    def __init__(self, variants: Variants) -> None:
        self._variants = variants

        self.create = to_streamed_response_wrapper(
            variants.create,
        )
        self.list = to_streamed_response_wrapper(
            variants.list,
        )
        self.delete = to_streamed_response_wrapper(
            variants.delete,
        )
        self.edit = to_streamed_response_wrapper(
            variants.edit,
        )
        self.get = to_streamed_response_wrapper(
            variants.get,
        )


class AsyncVariantsWithStreamingResponse:
    def __init__(self, variants: AsyncVariants) -> None:
        self._variants = variants

        self.create = async_to_streamed_response_wrapper(
            variants.create,
        )
        self.list = async_to_streamed_response_wrapper(
            variants.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            variants.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            variants.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            variants.get,
        )
