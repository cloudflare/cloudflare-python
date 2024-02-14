# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.images.v1s import (
    VariantUpdateResponse,
    VariantDeleteResponse,
    VariantCloudflareImagesVariantsCreateAVariantResponse,
    VariantCloudflareImagesVariantsListVariantsResponse,
    VariantGetResponse,
    variant_update_params,
    variant_cloudflare_images_variants_create_a_variant_params,
)

from typing import Type

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ....types.images.v1s import variant_update_params
from ....types.images.v1s import variant_cloudflare_images_variants_create_a_variant_params
from ...._wrappers import ResultWrapper
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

__all__ = ["Variants", "AsyncVariants"]


class Variants(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VariantsWithRawResponse:
        return VariantsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VariantsWithStreamingResponse:
        return VariantsWithStreamingResponse(self)

    def update(
        self,
        variant_id: object,
        *,
        account_id: str,
        options: variant_update_params.Options,
        never_require_signed_urls: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VariantUpdateResponse:
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
        return self._patch(
            f"/accounts/{account_id}/images/v1/variants/{variant_id}",
            body=maybe_transform(
                {
                    "options": options,
                    "never_require_signed_urls": never_require_signed_urls,
                },
                variant_update_params.VariantUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[VariantUpdateResponse], ResultWrapper[VariantUpdateResponse]),
        )

    def delete(
        self,
        variant_id: object,
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

    def cloudflare_images_variants_create_a_variant(
        self,
        account_id: str,
        *,
        id: object,
        options: variant_cloudflare_images_variants_create_a_variant_params.Options,
        never_require_signed_urls: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VariantCloudflareImagesVariantsCreateAVariantResponse:
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
                variant_cloudflare_images_variants_create_a_variant_params.VariantCloudflareImagesVariantsCreateAVariantParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[VariantCloudflareImagesVariantsCreateAVariantResponse],
                ResultWrapper[VariantCloudflareImagesVariantsCreateAVariantResponse],
            ),
        )

    def cloudflare_images_variants_list_variants(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VariantCloudflareImagesVariantsListVariantsResponse:
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
            cast_to=cast(
                Type[VariantCloudflareImagesVariantsListVariantsResponse],
                ResultWrapper[VariantCloudflareImagesVariantsListVariantsResponse],
            ),
        )

    def get(
        self,
        variant_id: object,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VariantGetResponse:
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
        return self._get(
            f"/accounts/{account_id}/images/v1/variants/{variant_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[VariantGetResponse], ResultWrapper[VariantGetResponse]),
        )


class AsyncVariants(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVariantsWithRawResponse:
        return AsyncVariantsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVariantsWithStreamingResponse:
        return AsyncVariantsWithStreamingResponse(self)

    async def update(
        self,
        variant_id: object,
        *,
        account_id: str,
        options: variant_update_params.Options,
        never_require_signed_urls: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VariantUpdateResponse:
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
        return await self._patch(
            f"/accounts/{account_id}/images/v1/variants/{variant_id}",
            body=maybe_transform(
                {
                    "options": options,
                    "never_require_signed_urls": never_require_signed_urls,
                },
                variant_update_params.VariantUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[VariantUpdateResponse], ResultWrapper[VariantUpdateResponse]),
        )

    async def delete(
        self,
        variant_id: object,
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

    async def cloudflare_images_variants_create_a_variant(
        self,
        account_id: str,
        *,
        id: object,
        options: variant_cloudflare_images_variants_create_a_variant_params.Options,
        never_require_signed_urls: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VariantCloudflareImagesVariantsCreateAVariantResponse:
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
            body=maybe_transform(
                {
                    "id": id,
                    "options": options,
                    "never_require_signed_urls": never_require_signed_urls,
                },
                variant_cloudflare_images_variants_create_a_variant_params.VariantCloudflareImagesVariantsCreateAVariantParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[VariantCloudflareImagesVariantsCreateAVariantResponse],
                ResultWrapper[VariantCloudflareImagesVariantsCreateAVariantResponse],
            ),
        )

    async def cloudflare_images_variants_list_variants(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VariantCloudflareImagesVariantsListVariantsResponse:
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
            cast_to=cast(
                Type[VariantCloudflareImagesVariantsListVariantsResponse],
                ResultWrapper[VariantCloudflareImagesVariantsListVariantsResponse],
            ),
        )

    async def get(
        self,
        variant_id: object,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VariantGetResponse:
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
        return await self._get(
            f"/accounts/{account_id}/images/v1/variants/{variant_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[VariantGetResponse], ResultWrapper[VariantGetResponse]),
        )


class VariantsWithRawResponse:
    def __init__(self, variants: Variants) -> None:
        self._variants = variants

        self.update = to_raw_response_wrapper(
            variants.update,
        )
        self.delete = to_raw_response_wrapper(
            variants.delete,
        )
        self.cloudflare_images_variants_create_a_variant = to_raw_response_wrapper(
            variants.cloudflare_images_variants_create_a_variant,
        )
        self.cloudflare_images_variants_list_variants = to_raw_response_wrapper(
            variants.cloudflare_images_variants_list_variants,
        )
        self.get = to_raw_response_wrapper(
            variants.get,
        )


class AsyncVariantsWithRawResponse:
    def __init__(self, variants: AsyncVariants) -> None:
        self._variants = variants

        self.update = async_to_raw_response_wrapper(
            variants.update,
        )
        self.delete = async_to_raw_response_wrapper(
            variants.delete,
        )
        self.cloudflare_images_variants_create_a_variant = async_to_raw_response_wrapper(
            variants.cloudflare_images_variants_create_a_variant,
        )
        self.cloudflare_images_variants_list_variants = async_to_raw_response_wrapper(
            variants.cloudflare_images_variants_list_variants,
        )
        self.get = async_to_raw_response_wrapper(
            variants.get,
        )


class VariantsWithStreamingResponse:
    def __init__(self, variants: Variants) -> None:
        self._variants = variants

        self.update = to_streamed_response_wrapper(
            variants.update,
        )
        self.delete = to_streamed_response_wrapper(
            variants.delete,
        )
        self.cloudflare_images_variants_create_a_variant = to_streamed_response_wrapper(
            variants.cloudflare_images_variants_create_a_variant,
        )
        self.cloudflare_images_variants_list_variants = to_streamed_response_wrapper(
            variants.cloudflare_images_variants_list_variants,
        )
        self.get = to_streamed_response_wrapper(
            variants.get,
        )


class AsyncVariantsWithStreamingResponse:
    def __init__(self, variants: AsyncVariants) -> None:
        self._variants = variants

        self.update = async_to_streamed_response_wrapper(
            variants.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            variants.delete,
        )
        self.cloudflare_images_variants_create_a_variant = async_to_streamed_response_wrapper(
            variants.cloudflare_images_variants_create_a_variant,
        )
        self.cloudflare_images_variants_list_variants = async_to_streamed_response_wrapper(
            variants.cloudflare_images_variants_list_variants,
        )
        self.get = async_to_streamed_response_wrapper(
            variants.get,
        )
