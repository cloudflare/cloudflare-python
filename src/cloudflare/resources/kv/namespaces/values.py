# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.kv.namespaces import value_update_params
from ....types.kv.namespaces.value_delete_response import ValueDeleteResponse
from ....types.kv.namespaces.value_update_response import ValueUpdateResponse

__all__ = ["ValuesResource", "AsyncValuesResource"]


class ValuesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ValuesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ValuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ValuesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ValuesResourceWithStreamingResponse(self)

    def update(
        self,
        key_name: str,
        *,
        account_id: str,
        namespace_id: str,
        metadata: str,
        value: str,
        expiration: float | NotGiven = NOT_GIVEN,
        expiration_ttl: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ValueUpdateResponse]:
        """Write a value identified by a key.

        Use URL-encoding to use special characters
        (for example, `:`, `!`, `%`) in the key name. Body should be the value to be
        stored. If JSON metadata to be associated with the key/value pair is needed, use
        `multipart/form-data` content type for your PUT request (see dropdown below in
        `REQUEST BODY SCHEMA`). Existing values, expirations, and metadata will be
        overwritten. If neither `expiration` nor `expiration_ttl` is specified, the
        key-value pair will never expire. If both are set, `expiration_ttl` is used and
        `expiration` is ignored.

        Args:
          account_id: Identifier

          namespace_id: Namespace identifier tag.

          key_name: A key's name. The name may be at most 512 bytes. All printable, non-whitespace
              characters are valid. Use percent-encoding to define key names as part of a URL.

          metadata: Arbitrary JSON to be associated with a key/value pair.

          value: A byte sequence to be stored, up to 25 MiB in length.

          expiration: The time, measured in number of seconds since the UNIX epoch, at which the key
              should expire.

          expiration_ttl: The number of seconds for which the key should be visible before it expires. At
              least 60.

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
        return self._put(
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
                query=maybe_transform(
                    {
                        "expiration": expiration,
                        "expiration_ttl": expiration_ttl,
                    },
                    value_update_params.ValueUpdateParams,
                ),
                post_parser=ResultWrapper[Optional[ValueUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ValueUpdateResponse]], ResultWrapper[ValueUpdateResponse]),
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
    ) -> Optional[ValueDeleteResponse]:
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
        return self._delete(
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ValueDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ValueDeleteResponse]], ResultWrapper[ValueDeleteResponse]),
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
    ) -> BinaryAPIResponse:
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
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncValuesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncValuesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncValuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncValuesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncValuesResourceWithStreamingResponse(self)

    async def update(
        self,
        key_name: str,
        *,
        account_id: str,
        namespace_id: str,
        metadata: str,
        value: str,
        expiration: float | NotGiven = NOT_GIVEN,
        expiration_ttl: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ValueUpdateResponse]:
        """Write a value identified by a key.

        Use URL-encoding to use special characters
        (for example, `:`, `!`, `%`) in the key name. Body should be the value to be
        stored. If JSON metadata to be associated with the key/value pair is needed, use
        `multipart/form-data` content type for your PUT request (see dropdown below in
        `REQUEST BODY SCHEMA`). Existing values, expirations, and metadata will be
        overwritten. If neither `expiration` nor `expiration_ttl` is specified, the
        key-value pair will never expire. If both are set, `expiration_ttl` is used and
        `expiration` is ignored.

        Args:
          account_id: Identifier

          namespace_id: Namespace identifier tag.

          key_name: A key's name. The name may be at most 512 bytes. All printable, non-whitespace
              characters are valid. Use percent-encoding to define key names as part of a URL.

          metadata: Arbitrary JSON to be associated with a key/value pair.

          value: A byte sequence to be stored, up to 25 MiB in length.

          expiration: The time, measured in number of seconds since the UNIX epoch, at which the key
              should expire.

          expiration_ttl: The number of seconds for which the key should be visible before it expires. At
              least 60.

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
        return await self._put(
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}",
            body=await async_maybe_transform(
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
                query=await async_maybe_transform(
                    {
                        "expiration": expiration,
                        "expiration_ttl": expiration_ttl,
                    },
                    value_update_params.ValueUpdateParams,
                ),
                post_parser=ResultWrapper[Optional[ValueUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ValueUpdateResponse]], ResultWrapper[ValueUpdateResponse]),
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
    ) -> Optional[ValueDeleteResponse]:
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
        return await self._delete(
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ValueDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ValueDeleteResponse]], ResultWrapper[ValueDeleteResponse]),
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
    ) -> AsyncBinaryAPIResponse:
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
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
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
