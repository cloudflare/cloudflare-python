# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type

from ...._base_client import make_request_options

from ...._response import BinaryAPIResponse, AsyncBinaryAPIResponse, to_raw_response_wrapper, to_custom_raw_response_wrapper, async_to_raw_response_wrapper, async_to_custom_raw_response_wrapper, to_streamed_response_wrapper, to_custom_streamed_response_wrapper, StreamedBinaryAPIResponse, async_to_streamed_response_wrapper, async_to_custom_streamed_response_wrapper, AsyncStreamedBinaryAPIResponse

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.kv.namespaces import value_update_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["ValuesResource", "AsyncValuesResource"]

class ValuesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ValuesResourceWithRawResponse:
        return ValuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ValuesResourceWithStreamingResponse:
        return ValuesResourceWithStreamingResponse(self)

    def update(self,
    key_name: str,
    *,
    account_id: str,
    namespace_id: str,
    metadata: str,
    value: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> object:
        """Write a value identified by a key.

        Use URL-encoding to use special characters
        (for example, `:`, `!`, `%`) in the key name. Body should be the value to be
        stored along with JSON metadata to be associated with the key/value pair.
        Existing values, expirations, and metadata will be overwritten. If neither
        `expiration` nor `expiration_ttl` is specified, the key-value pair will never
        expire. If both are set, `expiration_ttl` is used and `expiration` is ignored.

        Args:
          account_id: Identifier

          namespace_id: Namespace identifier tag.

          key_name: A key's name. The name may be at most 512 bytes. All printable, non-whitespace
              characters are valid. Use percent-encoding to define key names as part of a URL.

          metadata: Arbitrary JSON to be associated with a key/value pair.

          value: A byte sequence to be stored, up to 25 MiB in length.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not namespace_id:
          raise ValueError(
            f'Expected a non-empty value for `namespace_id` but received {namespace_id!r}'
          )
        if not key_name:
          raise ValueError(
            f'Expected a non-empty value for `key_name` but received {key_name!r}'
          )
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._put(
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}",
            body=maybe_transform({
                "metadata": metadata,
                "value": value,
            }, value_update_params.ValueUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[object]]._unwrapper),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def delete(self,
    key_name: str,
    *,
    account_id: str,
    namespace_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> object:
        """Remove a KV pair from the namespace.

        Use URL-encoding to use special characters
        (for example, `:`, `!`, `%`) in the key name.

        Args:
          account_id: Identifier

          namespace_id: Namespace identifier tag.

          key_name: A key's name. The name may be at most 512 bytes. All printable, non-whitespace
              characters are valid. Use percent-encoding to define key names as part of a URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not namespace_id:
          raise ValueError(
            f'Expected a non-empty value for `namespace_id` but received {namespace_id!r}'
          )
        if not key_name:
          raise ValueError(
            f'Expected a non-empty value for `key_name` but received {key_name!r}'
          )
        return self._delete(
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[object]]._unwrapper),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def get(self,
    key_name: str,
    *,
    account_id: str,
    namespace_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> BinaryAPIResponse:
        """Returns the value associated with the given key in the given namespace.

        Use
        URL-encoding to use special characters (for example, `:`, `!`, `%`) in the key
        name. If the KV-pair is set to expire at some point, the expiration time as
        measured in seconds since the UNIX epoch will be returned in the `expiration`
        response header.

        Args:
          account_id: Identifier

          namespace_id: Namespace identifier tag.

          key_name: A key's name. The name may be at most 512 bytes. All printable, non-whitespace
              characters are valid. Use percent-encoding to define key names as part of a URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not namespace_id:
          raise ValueError(
            f'Expected a non-empty value for `namespace_id` but received {namespace_id!r}'
          )
        if not key_name:
          raise ValueError(
            f'Expected a non-empty value for `key_name` but received {key_name!r}'
          )
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=BinaryAPIResponse,
        )

class AsyncValuesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncValuesResourceWithRawResponse:
        return AsyncValuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncValuesResourceWithStreamingResponse:
        return AsyncValuesResourceWithStreamingResponse(self)

    async def update(self,
    key_name: str,
    *,
    account_id: str,
    namespace_id: str,
    metadata: str,
    value: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> object:
        """Write a value identified by a key.

        Use URL-encoding to use special characters
        (for example, `:`, `!`, `%`) in the key name. Body should be the value to be
        stored along with JSON metadata to be associated with the key/value pair.
        Existing values, expirations, and metadata will be overwritten. If neither
        `expiration` nor `expiration_ttl` is specified, the key-value pair will never
        expire. If both are set, `expiration_ttl` is used and `expiration` is ignored.

        Args:
          account_id: Identifier

          namespace_id: Namespace identifier tag.

          key_name: A key's name. The name may be at most 512 bytes. All printable, non-whitespace
              characters are valid. Use percent-encoding to define key names as part of a URL.

          metadata: Arbitrary JSON to be associated with a key/value pair.

          value: A byte sequence to be stored, up to 25 MiB in length.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not namespace_id:
          raise ValueError(
            f'Expected a non-empty value for `namespace_id` but received {namespace_id!r}'
          )
        if not key_name:
          raise ValueError(
            f'Expected a non-empty value for `key_name` but received {key_name!r}'
          )
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._put(
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}",
            body=await async_maybe_transform({
                "metadata": metadata,
                "value": value,
            }, value_update_params.ValueUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[object]]._unwrapper),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    async def delete(self,
    key_name: str,
    *,
    account_id: str,
    namespace_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> object:
        """Remove a KV pair from the namespace.

        Use URL-encoding to use special characters
        (for example, `:`, `!`, `%`) in the key name.

        Args:
          account_id: Identifier

          namespace_id: Namespace identifier tag.

          key_name: A key's name. The name may be at most 512 bytes. All printable, non-whitespace
              characters are valid. Use percent-encoding to define key names as part of a URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not namespace_id:
          raise ValueError(
            f'Expected a non-empty value for `namespace_id` but received {namespace_id!r}'
          )
        if not key_name:
          raise ValueError(
            f'Expected a non-empty value for `key_name` but received {key_name!r}'
          )
        return await self._delete(
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[object]]._unwrapper),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    async def get(self,
    key_name: str,
    *,
    account_id: str,
    namespace_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AsyncBinaryAPIResponse:
        """Returns the value associated with the given key in the given namespace.

        Use
        URL-encoding to use special characters (for example, `:`, `!`, `%`) in the key
        name. If the KV-pair is set to expire at some point, the expiration time as
        measured in seconds since the UNIX epoch will be returned in the `expiration`
        response header.

        Args:
          account_id: Identifier

          namespace_id: Namespace identifier tag.

          key_name: A key's name. The name may be at most 512 bytes. All printable, non-whitespace
              characters are valid. Use percent-encoding to define key names as part of a URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not namespace_id:
          raise ValueError(
            f'Expected a non-empty value for `namespace_id` but received {namespace_id!r}'
          )
        if not key_name:
          raise ValueError(
            f'Expected a non-empty value for `key_name` but received {key_name!r}'
          )
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AsyncBinaryAPIResponse,
        )

class ValuesResourceWithRawResponse:
    def __init__(self, values: ValuesResource) -> None:
        self._values = values

        self.update = to_raw_response_wrapper(
            values.update,
        )
        self.delete = to_raw_response_wrapper(
            values.delete,
        )
        self.get = to_custom_raw_response_wrapper(
            values.get,
            BinaryAPIResponse,
        )

class AsyncValuesResourceWithRawResponse:
    def __init__(self, values: AsyncValuesResource) -> None:
        self._values = values

        self.update = async_to_raw_response_wrapper(
            values.update,
        )
        self.delete = async_to_raw_response_wrapper(
            values.delete,
        )
        self.get = async_to_custom_raw_response_wrapper(
            values.get,
            AsyncBinaryAPIResponse,
        )

class ValuesResourceWithStreamingResponse:
    def __init__(self, values: ValuesResource) -> None:
        self._values = values

        self.update = to_streamed_response_wrapper(
            values.update,
        )
        self.delete = to_streamed_response_wrapper(
            values.delete,
        )
        self.get = to_custom_streamed_response_wrapper(
            values.get,
            StreamedBinaryAPIResponse,
        )

class AsyncValuesResourceWithStreamingResponse:
    def __init__(self, values: AsyncValuesResource) -> None:
        self._values = values

        self.update = async_to_streamed_response_wrapper(
            values.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            values.delete,
        )
        self.get = async_to_custom_streamed_response_wrapper(
            values.get,
            AsyncStreamedBinaryAPIResponse,
        )