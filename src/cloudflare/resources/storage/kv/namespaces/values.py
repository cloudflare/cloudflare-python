# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.storage.kv.namespaces import ValueUpdateResponse, ValueDeleteResponse, ValueGetResponse

from ....._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from .....types import shared_params
from .....types.storage.kv.namespaces import value_update_params
from ....._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Values", "AsyncValues"]


class Values(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ValuesWithRawResponse:
        return ValuesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ValuesWithStreamingResponse:
        return ValuesWithStreamingResponse(self)

    def update(
        self,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ValueUpdateResponse:
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
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        if not key_name:
            raise ValueError(f"Expected a non-empty value for `key_name` but received {key_name!r}")
        return cast(
            ValueUpdateResponse,
            self._put(
                f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}",
                body=maybe_transform(
                    {
                        "metadata": metadata,
                        "value": value,
                    },
                    value_update_params.ValueUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ValueUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def delete(
        self,
        key_name: str,
        *,
        account_id: str,
        namespace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ValueDeleteResponse:
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
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        if not key_name:
            raise ValueError(f"Expected a non-empty value for `key_name` but received {key_name!r}")
        return cast(
            ValueDeleteResponse,
            self._delete(
                f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ValueDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        key_name: str,
        *,
        account_id: str,
        namespace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
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
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        if not key_name:
            raise ValueError(f"Expected a non-empty value for `key_name` but received {key_name!r}")
        extra_headers = {"Accept": "application/json", **(extra_headers or {})}
        return self._get(
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncValues(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncValuesWithRawResponse:
        return AsyncValuesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncValuesWithStreamingResponse:
        return AsyncValuesWithStreamingResponse(self)

    async def update(
        self,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ValueUpdateResponse:
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
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        if not key_name:
            raise ValueError(f"Expected a non-empty value for `key_name` but received {key_name!r}")
        return cast(
            ValueUpdateResponse,
            await self._put(
                f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}",
                body=maybe_transform(
                    {
                        "metadata": metadata,
                        "value": value,
                    },
                    value_update_params.ValueUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ValueUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def delete(
        self,
        key_name: str,
        *,
        account_id: str,
        namespace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ValueDeleteResponse:
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
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        if not key_name:
            raise ValueError(f"Expected a non-empty value for `key_name` but received {key_name!r}")
        return cast(
            ValueDeleteResponse,
            await self._delete(
                f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ValueDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        key_name: str,
        *,
        account_id: str,
        namespace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
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
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        if not key_name:
            raise ValueError(f"Expected a non-empty value for `key_name` but received {key_name!r}")
        extra_headers = {"Accept": "application/json", **(extra_headers or {})}
        return await self._get(
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class ValuesWithRawResponse:
    def __init__(self, values: Values) -> None:
        self._values = values

        self.update = to_raw_response_wrapper(
            values.update,
        )
        self.delete = to_raw_response_wrapper(
            values.delete,
        )
        self.get = to_raw_response_wrapper(
            values.get,
        )


class AsyncValuesWithRawResponse:
    def __init__(self, values: AsyncValues) -> None:
        self._values = values

        self.update = async_to_raw_response_wrapper(
            values.update,
        )
        self.delete = async_to_raw_response_wrapper(
            values.delete,
        )
        self.get = async_to_raw_response_wrapper(
            values.get,
        )


class ValuesWithStreamingResponse:
    def __init__(self, values: Values) -> None:
        self._values = values

        self.update = to_streamed_response_wrapper(
            values.update,
        )
        self.delete = to_streamed_response_wrapper(
            values.delete,
        )
        self.get = to_streamed_response_wrapper(
            values.get,
        )


class AsyncValuesWithStreamingResponse:
    def __init__(self, values: AsyncValues) -> None:
        self._values = values

        self.update = async_to_streamed_response_wrapper(
            values.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            values.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            values.get,
        )
