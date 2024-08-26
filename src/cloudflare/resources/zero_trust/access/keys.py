# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.zero_trust.access.key_update_response import KeyUpdateResponse

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type

from ...._base_client import make_request_options

from ....types.zero_trust.access.key_get_response import KeyGetResponse

from ....types.zero_trust.access.key_rotate_response import KeyRotateResponse

from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.zero_trust.access import key_update_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["KeysResource", "AsyncKeysResource"]

class KeysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KeysResourceWithRawResponse:
        return KeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KeysResourceWithStreamingResponse:
        return KeysResourceWithStreamingResponse(self)

    def update(self,
    *,
    account_id: str,
    key_rotation_interval_days: float,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[KeyUpdateResponse]:
        """
        Updates the Access key rotation settings for an account.

        Args:
          account_id: Identifier

          key_rotation_interval_days: The number of days between key rotations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._put(
            f"/accounts/{account_id}/access/keys",
            body=maybe_transform({
                "key_rotation_interval_days": key_rotation_interval_days
            }, key_update_params.KeyUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[KeyUpdateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[KeyUpdateResponse]], ResultWrapper[KeyUpdateResponse]),
        )

    def get(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[KeyGetResponse]:
        """
        Gets the Access key rotation settings for an account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get(
            f"/accounts/{account_id}/access/keys",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[KeyGetResponse]]._unwrapper),
            cast_to=cast(Type[Optional[KeyGetResponse]], ResultWrapper[KeyGetResponse]),
        )

    def rotate(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[KeyRotateResponse]:
        """
        Perfoms a key rotation for an account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._post(
            f"/accounts/{account_id}/access/keys/rotate",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[KeyRotateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[KeyRotateResponse]], ResultWrapper[KeyRotateResponse]),
        )

class AsyncKeysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKeysResourceWithRawResponse:
        return AsyncKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKeysResourceWithStreamingResponse:
        return AsyncKeysResourceWithStreamingResponse(self)

    async def update(self,
    *,
    account_id: str,
    key_rotation_interval_days: float,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[KeyUpdateResponse]:
        """
        Updates the Access key rotation settings for an account.

        Args:
          account_id: Identifier

          key_rotation_interval_days: The number of days between key rotations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return await self._put(
            f"/accounts/{account_id}/access/keys",
            body=await async_maybe_transform({
                "key_rotation_interval_days": key_rotation_interval_days
            }, key_update_params.KeyUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[KeyUpdateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[KeyUpdateResponse]], ResultWrapper[KeyUpdateResponse]),
        )

    async def get(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[KeyGetResponse]:
        """
        Gets the Access key rotation settings for an account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return await self._get(
            f"/accounts/{account_id}/access/keys",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[KeyGetResponse]]._unwrapper),
            cast_to=cast(Type[Optional[KeyGetResponse]], ResultWrapper[KeyGetResponse]),
        )

    async def rotate(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[KeyRotateResponse]:
        """
        Perfoms a key rotation for an account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return await self._post(
            f"/accounts/{account_id}/access/keys/rotate",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[KeyRotateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[KeyRotateResponse]], ResultWrapper[KeyRotateResponse]),
        )

class KeysResourceWithRawResponse:
    def __init__(self, keys: KeysResource) -> None:
        self._keys = keys

        self.update = to_raw_response_wrapper(
            keys.update,
        )
        self.get = to_raw_response_wrapper(
            keys.get,
        )
        self.rotate = to_raw_response_wrapper(
            keys.rotate,
        )

class AsyncKeysResourceWithRawResponse:
    def __init__(self, keys: AsyncKeysResource) -> None:
        self._keys = keys

        self.update = async_to_raw_response_wrapper(
            keys.update,
        )
        self.get = async_to_raw_response_wrapper(
            keys.get,
        )
        self.rotate = async_to_raw_response_wrapper(
            keys.rotate,
        )

class KeysResourceWithStreamingResponse:
    def __init__(self, keys: KeysResource) -> None:
        self._keys = keys

        self.update = to_streamed_response_wrapper(
            keys.update,
        )
        self.get = to_streamed_response_wrapper(
            keys.get,
        )
        self.rotate = to_streamed_response_wrapper(
            keys.rotate,
        )

class AsyncKeysResourceWithStreamingResponse:
    def __init__(self, keys: AsyncKeysResource) -> None:
        self._keys = keys

        self.update = async_to_streamed_response_wrapper(
            keys.update,
        )
        self.get = async_to_streamed_response_wrapper(
            keys.get,
        )
        self.rotate = async_to_streamed_response_wrapper(
            keys.rotate,
        )