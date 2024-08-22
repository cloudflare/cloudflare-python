# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.calls.turn.key_create_response import KeyCreateResponse

from ...._utils import maybe_transform, async_maybe_transform

from ...._base_client import make_request_options, AsyncPaginator

from ...._wrappers import ResultWrapper

from typing import Optional, Type

from ....types.calls.turn.key_update_response import KeyUpdateResponse

from ....pagination import SyncSinglePage, AsyncSinglePage

from ....types.calls.turn.key_list_response import KeyListResponse

from ....types.calls.turn.key_delete_response import KeyDeleteResponse

from ....types.calls.turn.key_get_response import KeyGetResponse

from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.calls.turn import key_create_params
from ....types.calls.turn import key_update_params
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

    def create(self,
    *,
    account_id: str,
    name: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> KeyCreateResponse:
        """
        Creates a new Cloudflare Calls TURN key.

        Args:
          account_id: The account identifier tag.

          name: A short description of a TURN key, not shown to end users.

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
            f"/accounts/{account_id}/calls/turn_keys",
            body=maybe_transform({
                "name": name
            }, key_create_params.KeyCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=KeyCreateResponse,
        )

    def update(self,
    key_id: str,
    *,
    account_id: str,
    name: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> str:
        """
        Edit details for a single TURN key.

        Args:
          account_id: The account identifier tag.

          key_id: A Cloudflare-generated unique identifier for a item.

          name: A short description of a TURN key, not shown to end users.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not key_id:
          raise ValueError(
            f'Expected a non-empty value for `key_id` but received {key_id!r}'
          )
        return self._put(
            f"/accounts/{account_id}/calls/turn_keys/{key_id}",
            body=maybe_transform({
                "name": name
            }, key_update_params.KeyUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[KeyUpdateResponse]]._unwrapper),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    def list(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> SyncSinglePage[KeyListResponse]:
        """
        Lists all TURN keys in the Cloudflare account

        Args:
          account_id: The account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get_api_list(
            f"/accounts/{account_id}/calls/turn_keys",
            page = SyncSinglePage[KeyListResponse],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            model=str,
        )

    def delete(self,
    key_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> str:
        """
        Deletes a TURN key from Cloudflare Calls

        Args:
          account_id: The account identifier tag.

          key_id: A Cloudflare-generated unique identifier for a item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not key_id:
          raise ValueError(
            f'Expected a non-empty value for `key_id` but received {key_id!r}'
          )
        return self._delete(
            f"/accounts/{account_id}/calls/turn_keys/{key_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[KeyDeleteResponse]]._unwrapper),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    def get(self,
    key_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> str:
        """
        Fetches details for a single TURN key.

        Args:
          account_id: The account identifier tag.

          key_id: A Cloudflare-generated unique identifier for a item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not key_id:
          raise ValueError(
            f'Expected a non-empty value for `key_id` but received {key_id!r}'
          )
        return self._get(
            f"/accounts/{account_id}/calls/turn_keys/{key_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[KeyGetResponse]]._unwrapper),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

class AsyncKeysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKeysResourceWithRawResponse:
        return AsyncKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKeysResourceWithStreamingResponse:
        return AsyncKeysResourceWithStreamingResponse(self)

    async def create(self,
    *,
    account_id: str,
    name: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> KeyCreateResponse:
        """
        Creates a new Cloudflare Calls TURN key.

        Args:
          account_id: The account identifier tag.

          name: A short description of a TURN key, not shown to end users.

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
            f"/accounts/{account_id}/calls/turn_keys",
            body=await async_maybe_transform({
                "name": name
            }, key_create_params.KeyCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=KeyCreateResponse,
        )

    async def update(self,
    key_id: str,
    *,
    account_id: str,
    name: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> str:
        """
        Edit details for a single TURN key.

        Args:
          account_id: The account identifier tag.

          key_id: A Cloudflare-generated unique identifier for a item.

          name: A short description of a TURN key, not shown to end users.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not key_id:
          raise ValueError(
            f'Expected a non-empty value for `key_id` but received {key_id!r}'
          )
        return await self._put(
            f"/accounts/{account_id}/calls/turn_keys/{key_id}",
            body=await async_maybe_transform({
                "name": name
            }, key_update_params.KeyUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[KeyUpdateResponse]]._unwrapper),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    def list(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AsyncPaginator[KeyListResponse, AsyncSinglePage[KeyListResponse]]:
        """
        Lists all TURN keys in the Cloudflare account

        Args:
          account_id: The account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get_api_list(
            f"/accounts/{account_id}/calls/turn_keys",
            page = AsyncSinglePage[KeyListResponse],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            model=str,
        )

    async def delete(self,
    key_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> str:
        """
        Deletes a TURN key from Cloudflare Calls

        Args:
          account_id: The account identifier tag.

          key_id: A Cloudflare-generated unique identifier for a item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not key_id:
          raise ValueError(
            f'Expected a non-empty value for `key_id` but received {key_id!r}'
          )
        return await self._delete(
            f"/accounts/{account_id}/calls/turn_keys/{key_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[KeyDeleteResponse]]._unwrapper),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    async def get(self,
    key_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> str:
        """
        Fetches details for a single TURN key.

        Args:
          account_id: The account identifier tag.

          key_id: A Cloudflare-generated unique identifier for a item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not key_id:
          raise ValueError(
            f'Expected a non-empty value for `key_id` but received {key_id!r}'
          )
        return await self._get(
            f"/accounts/{account_id}/calls/turn_keys/{key_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[KeyGetResponse]]._unwrapper),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

class KeysResourceWithRawResponse:
    def __init__(self, keys: KeysResource) -> None:
        self._keys = keys

        self.create = to_raw_response_wrapper(
            keys.create,
        )
        self.update = to_raw_response_wrapper(
            keys.update,
        )
        self.list = to_raw_response_wrapper(
            keys.list,
        )
        self.delete = to_raw_response_wrapper(
            keys.delete,
        )
        self.get = to_raw_response_wrapper(
            keys.get,
        )

class AsyncKeysResourceWithRawResponse:
    def __init__(self, keys: AsyncKeysResource) -> None:
        self._keys = keys

        self.create = async_to_raw_response_wrapper(
            keys.create,
        )
        self.update = async_to_raw_response_wrapper(
            keys.update,
        )
        self.list = async_to_raw_response_wrapper(
            keys.list,
        )
        self.delete = async_to_raw_response_wrapper(
            keys.delete,
        )
        self.get = async_to_raw_response_wrapper(
            keys.get,
        )

class KeysResourceWithStreamingResponse:
    def __init__(self, keys: KeysResource) -> None:
        self._keys = keys

        self.create = to_streamed_response_wrapper(
            keys.create,
        )
        self.update = to_streamed_response_wrapper(
            keys.update,
        )
        self.list = to_streamed_response_wrapper(
            keys.list,
        )
        self.delete = to_streamed_response_wrapper(
            keys.delete,
        )
        self.get = to_streamed_response_wrapper(
            keys.get,
        )

class AsyncKeysResourceWithStreamingResponse:
    def __init__(self, keys: AsyncKeysResource) -> None:
        self._keys = keys

        self.create = async_to_streamed_response_wrapper(
            keys.create,
        )
        self.update = async_to_streamed_response_wrapper(
            keys.update,
        )
        self.list = async_to_streamed_response_wrapper(
            keys.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            keys.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            keys.get,
        )