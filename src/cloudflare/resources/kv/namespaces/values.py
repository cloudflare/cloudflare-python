# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, Mapping, Optional, cast

import httpx

from ...._files import deepcopy_with_paths
from ...._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from ...._utils import extract_files, path_template, maybe_transform, async_maybe_transform
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
        value: Union[str, FileTypes],
        expiration: float | Omit = omit,
        expiration_ttl: float | Omit = omit,
        metadata: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ValueUpdateResponse]:
        """
        Writes a value under the specified key in the Workers KV namespace, creating the
        key-value pair or replacing its existing value, expiration, and metadata. Send
        the value as an `application/octet-stream` request body, or use
        `multipart/form-data` with a `value` part and an optional JSON `metadata` part.
        Use URL-encoding for special characters (for example, `:`, `!`, `%`) in the key
        name when constructing the request URL. If neither `expiration` nor
        `expiration_ttl` is specified, the key-value pair will not expire. If both are
        set, `expiration_ttl` takes precedence.

        Args:
          account_id: ID of the Cloudflare account that owns the Workers KV namespaces.

          namespace_id: ID of the Workers KV namespace.

          key_name: A key's name. The name may be at most 512 bytes. All printable, non-whitespace
              characters are valid. Use percent-encoding to define key names as part of a URL.

          value: A byte sequence to be stored, up to 25 MiB in length.

          expiration: Expires the key at a certain time, measured in number of seconds since the UNIX
              epoch.

          expiration_ttl: Number of seconds until the key expires. Must be at least 60. Takes precedence
              over `expiration` when both are specified.

          metadata: Associates arbitrary JSON data with a key/value pair.

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
        body = deepcopy_with_paths(
            {
                "value": value,
                "metadata": metadata,
            },
            [["value"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["value"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._put(
            path_template(
                "/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}",
                account_id=account_id,
                namespace_id=namespace_id,
                key_name=key_name,
            ),
            body=maybe_transform(body, value_update_params.ValueUpdateParams),
            files=files,
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
                multipart_syntax="json",
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ValueDeleteResponse]:
        """Deletes the specified key and its value from the Workers KV namespace.

        Use
        URL-encoding for special characters (for example, `:`, `!`, `%`) in the key name
        when constructing the request URL.

        Args:
          account_id: ID of the Cloudflare account that owns the Workers KV namespaces.

          namespace_id: ID of the Workers KV namespace.

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
            path_template(
                "/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}",
                account_id=account_id,
                namespace_id=namespace_id,
                key_name=key_name,
            ),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Returns the value stored under the specified key in the Workers KV namespace as
        raw bytes. Use URL-encoding for special characters (for example, `:`, `!`, `%`)
        in the key name when constructing the request URL. If the key-value pair
        expires, the `expiration` response header contains its expiration time in
        seconds since the UNIX epoch.

        Args:
          account_id: ID of the Cloudflare account that owns the Workers KV namespaces.

          namespace_id: ID of the Workers KV namespace.

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
            path_template(
                "/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}",
                account_id=account_id,
                namespace_id=namespace_id,
                key_name=key_name,
            ),
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
        value: Union[str, FileTypes],
        expiration: float | Omit = omit,
        expiration_ttl: float | Omit = omit,
        metadata: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ValueUpdateResponse]:
        """
        Writes a value under the specified key in the Workers KV namespace, creating the
        key-value pair or replacing its existing value, expiration, and metadata. Send
        the value as an `application/octet-stream` request body, or use
        `multipart/form-data` with a `value` part and an optional JSON `metadata` part.
        Use URL-encoding for special characters (for example, `:`, `!`, `%`) in the key
        name when constructing the request URL. If neither `expiration` nor
        `expiration_ttl` is specified, the key-value pair will not expire. If both are
        set, `expiration_ttl` takes precedence.

        Args:
          account_id: ID of the Cloudflare account that owns the Workers KV namespaces.

          namespace_id: ID of the Workers KV namespace.

          key_name: A key's name. The name may be at most 512 bytes. All printable, non-whitespace
              characters are valid. Use percent-encoding to define key names as part of a URL.

          value: A byte sequence to be stored, up to 25 MiB in length.

          expiration: Expires the key at a certain time, measured in number of seconds since the UNIX
              epoch.

          expiration_ttl: Number of seconds until the key expires. Must be at least 60. Takes precedence
              over `expiration` when both are specified.

          metadata: Associates arbitrary JSON data with a key/value pair.

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
        body = deepcopy_with_paths(
            {
                "value": value,
                "metadata": metadata,
            },
            [["value"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["value"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._put(
            path_template(
                "/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}",
                account_id=account_id,
                namespace_id=namespace_id,
                key_name=key_name,
            ),
            body=await async_maybe_transform(body, value_update_params.ValueUpdateParams),
            files=files,
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
                multipart_syntax="json",
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ValueDeleteResponse]:
        """Deletes the specified key and its value from the Workers KV namespace.

        Use
        URL-encoding for special characters (for example, `:`, `!`, `%`) in the key name
        when constructing the request URL.

        Args:
          account_id: ID of the Cloudflare account that owns the Workers KV namespaces.

          namespace_id: ID of the Workers KV namespace.

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
            path_template(
                "/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}",
                account_id=account_id,
                namespace_id=namespace_id,
                key_name=key_name,
            ),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Returns the value stored under the specified key in the Workers KV namespace as
        raw bytes. Use URL-encoding for special characters (for example, `:`, `!`, `%`)
        in the key name when constructing the request URL. If the key-value pair
        expires, the `expiration` response header contains its expiration time in
        seconds since the UNIX epoch.

        Args:
          account_id: ID of the Cloudflare account that owns the Workers KV namespaces.

          namespace_id: ID of the Workers KV namespace.

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
            path_template(
                "/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}",
                account_id=account_id,
                namespace_id=namespace_id,
                key_name=key_name,
            ),
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
