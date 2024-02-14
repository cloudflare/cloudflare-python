# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.images.v1s import KeyCloudflareImagesKeysListSigningKeysResponse

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
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Keys", "AsyncKeys"]


class Keys(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KeysWithRawResponse:
        return KeysWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KeysWithStreamingResponse:
        return KeysWithStreamingResponse(self)

    def cloudflare_images_keys_list_signing_keys(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeyCloudflareImagesKeysListSigningKeysResponse:
        """Lists your signing keys.

        These can be found on your Cloudflare Images dashboard.

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
            f"/accounts/{account_id}/images/v1/keys",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[KeyCloudflareImagesKeysListSigningKeysResponse],
                ResultWrapper[KeyCloudflareImagesKeysListSigningKeysResponse],
            ),
        )


class AsyncKeys(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKeysWithRawResponse:
        return AsyncKeysWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKeysWithStreamingResponse:
        return AsyncKeysWithStreamingResponse(self)

    async def cloudflare_images_keys_list_signing_keys(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeyCloudflareImagesKeysListSigningKeysResponse:
        """Lists your signing keys.

        These can be found on your Cloudflare Images dashboard.

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
            f"/accounts/{account_id}/images/v1/keys",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[KeyCloudflareImagesKeysListSigningKeysResponse],
                ResultWrapper[KeyCloudflareImagesKeysListSigningKeysResponse],
            ),
        )


class KeysWithRawResponse:
    def __init__(self, keys: Keys) -> None:
        self._keys = keys

        self.cloudflare_images_keys_list_signing_keys = to_raw_response_wrapper(
            keys.cloudflare_images_keys_list_signing_keys,
        )


class AsyncKeysWithRawResponse:
    def __init__(self, keys: AsyncKeys) -> None:
        self._keys = keys

        self.cloudflare_images_keys_list_signing_keys = async_to_raw_response_wrapper(
            keys.cloudflare_images_keys_list_signing_keys,
        )


class KeysWithStreamingResponse:
    def __init__(self, keys: Keys) -> None:
        self._keys = keys

        self.cloudflare_images_keys_list_signing_keys = to_streamed_response_wrapper(
            keys.cloudflare_images_keys_list_signing_keys,
        )


class AsyncKeysWithStreamingResponse:
    def __init__(self, keys: AsyncKeys) -> None:
        self._keys = keys

        self.cloudflare_images_keys_list_signing_keys = async_to_streamed_response_wrapper(
            keys.cloudflare_images_keys_list_signing_keys,
        )
