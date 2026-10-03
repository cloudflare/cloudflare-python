# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Any, Type, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncCursorLimitPagination, AsyncCursorLimitPagination
from ...._base_client import AsyncPaginator, make_request_options
from ....types.kv.namespaces import key_list_params, key_bulk_get_params, key_bulk_update_params
from ....types.kv.namespaces.key import Key
from ....types.kv.namespaces.key_bulk_get_response import KeyBulkGetResponse
from ....types.kv.namespaces.key_bulk_delete_response import KeyBulkDeleteResponse
from ....types.kv.namespaces.key_bulk_update_response import KeyBulkUpdateResponse

__all__ = ["KeysResource", "AsyncKeysResource"]


class KeysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return KeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return KeysResourceWithStreamingResponse(self)

    def list(
        self,
        namespace_id: str,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        limit: float | Omit = omit,
        prefix: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorLimitPagination[Key]:
        """
        Lists key names in the specified Workers KV namespace, with expiration times and
        metadata when present. Use `prefix` to filter names and `cursor` to request the
        next page. Values are not included.

        Args:
          account_id: ID of the Cloudflare account that owns the Workers KV namespaces.

          namespace_id: ID of the Workers KV namespace.

          cursor: Opaque pagination token from `result_info.cursor` in the previous response. Pass
              it unchanged to request the next page of keys.

          limit: Maximum number of keys to return in one response. Pass `result_info.cursor` from
              the response as `cursor` to request the next page.

          prefix: Filters returned keys by a name prefix. Exact matches and any key names that
              begin with the prefix will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/keys",
                account_id=account_id,
                namespace_id=namespace_id,
            ),
            page=SyncCursorLimitPagination[Key],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "prefix": prefix,
                    },
                    key_list_params.KeyListParams,
                ),
            ),
            model=Key,
        )

    @typing_extensions.deprecated("Please use kv.namespaces.bulk_delete instead")
    def bulk_delete(
        self,
        namespace_id: str,
        *,
        account_id: str,
        body: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[KeyBulkDeleteResponse]:
        """
        Deletes up to 10,000 key-value pairs from the specified Workers KV namespace.
        Send a JSON array of the key names to delete. The result reports the number of
        successful deletions and any keys that failed and should be retried.

        Args:
          account_id: ID of the Cloudflare account that owns the Workers KV namespaces.

          namespace_id: ID of the Workers KV namespace.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk/delete",
                account_id=account_id,
                namespace_id=namespace_id,
            ),
            body=maybe_transform(body, SequenceNotStr[str]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[KeyBulkDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[KeyBulkDeleteResponse]], ResultWrapper[KeyBulkDeleteResponse]),
        )

    @typing_extensions.deprecated("Please use kv.namespaces.bulk_get instead")
    def bulk_get(
        self,
        namespace_id: str,
        *,
        account_id: str,
        keys: SequenceNotStr[str],
        type: Literal["text", "json"] | Omit = omit,
        with_metadata: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[KeyBulkGetResponse]:
        """
        Retrieves the text-based values of up to 100 keys from the specified Workers KV
        namespace. The result maps each requested key to its value. Set `type` to `json`
        to parse JSON values instead of returning strings, and set `withMetadata` to
        `true` to include metadata with each value. Binary values are not supported by
        this operation.

        Args:
          account_id: ID of the Cloudflare account that owns the Workers KV namespaces.

          namespace_id: ID of the Workers KV namespace.

          keys: Array of keys to retrieve (maximum of 100).

          type: Return values as strings with `text`, or parse stored JSON values with `json`.

          with_metadata: Whether to include metadata in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        return cast(
            Optional[KeyBulkGetResponse],
            self._post(
                path_template(
                    "/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk/get",
                    account_id=account_id,
                    namespace_id=namespace_id,
                ),
                body=maybe_transform(
                    {
                        "keys": keys,
                        "type": type,
                        "with_metadata": with_metadata,
                    },
                    key_bulk_get_params.KeyBulkGetParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[KeyBulkGetResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[KeyBulkGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @typing_extensions.deprecated("Please use kv.namespaces.bulk_update instead")
    def bulk_update(
        self,
        namespace_id: str,
        *,
        account_id: str,
        body: Iterable[key_bulk_update_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[KeyBulkUpdateResponse]:
        """
        Writes up to 10,000 key-value pairs to the specified Workers KV namespace from a
        JSON array, with optional metadata and expiration settings for each pair.
        Existing values and expirations are overwritten. If neither `expiration` nor
        `expiration_ttl` is specified, the key-value pair will not expire. If both are
        set, `expiration_ttl` takes precedence. The entire request must be 100 megabytes
        or less. The result reports the number of successful writes and any keys that
        failed and should be retried.

        Args:
          account_id: ID of the Cloudflare account that owns the Workers KV namespaces.

          namespace_id: ID of the Workers KV namespace.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        return self._put(
            path_template(
                "/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk",
                account_id=account_id,
                namespace_id=namespace_id,
            ),
            body=maybe_transform(body, Iterable[key_bulk_update_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[KeyBulkUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[KeyBulkUpdateResponse]], ResultWrapper[KeyBulkUpdateResponse]),
        )


class AsyncKeysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncKeysResourceWithStreamingResponse(self)

    def list(
        self,
        namespace_id: str,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        limit: float | Omit = omit,
        prefix: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Key, AsyncCursorLimitPagination[Key]]:
        """
        Lists key names in the specified Workers KV namespace, with expiration times and
        metadata when present. Use `prefix` to filter names and `cursor` to request the
        next page. Values are not included.

        Args:
          account_id: ID of the Cloudflare account that owns the Workers KV namespaces.

          namespace_id: ID of the Workers KV namespace.

          cursor: Opaque pagination token from `result_info.cursor` in the previous response. Pass
              it unchanged to request the next page of keys.

          limit: Maximum number of keys to return in one response. Pass `result_info.cursor` from
              the response as `cursor` to request the next page.

          prefix: Filters returned keys by a name prefix. Exact matches and any key names that
              begin with the prefix will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/keys",
                account_id=account_id,
                namespace_id=namespace_id,
            ),
            page=AsyncCursorLimitPagination[Key],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "prefix": prefix,
                    },
                    key_list_params.KeyListParams,
                ),
            ),
            model=Key,
        )

    @typing_extensions.deprecated("Please use kv.namespaces.bulk_delete instead")
    async def bulk_delete(
        self,
        namespace_id: str,
        *,
        account_id: str,
        body: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[KeyBulkDeleteResponse]:
        """
        Deletes up to 10,000 key-value pairs from the specified Workers KV namespace.
        Send a JSON array of the key names to delete. The result reports the number of
        successful deletions and any keys that failed and should be retried.

        Args:
          account_id: ID of the Cloudflare account that owns the Workers KV namespaces.

          namespace_id: ID of the Workers KV namespace.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk/delete",
                account_id=account_id,
                namespace_id=namespace_id,
            ),
            body=await async_maybe_transform(body, SequenceNotStr[str]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[KeyBulkDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[KeyBulkDeleteResponse]], ResultWrapper[KeyBulkDeleteResponse]),
        )

    @typing_extensions.deprecated("Please use kv.namespaces.bulk_get instead")
    async def bulk_get(
        self,
        namespace_id: str,
        *,
        account_id: str,
        keys: SequenceNotStr[str],
        type: Literal["text", "json"] | Omit = omit,
        with_metadata: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[KeyBulkGetResponse]:
        """
        Retrieves the text-based values of up to 100 keys from the specified Workers KV
        namespace. The result maps each requested key to its value. Set `type` to `json`
        to parse JSON values instead of returning strings, and set `withMetadata` to
        `true` to include metadata with each value. Binary values are not supported by
        this operation.

        Args:
          account_id: ID of the Cloudflare account that owns the Workers KV namespaces.

          namespace_id: ID of the Workers KV namespace.

          keys: Array of keys to retrieve (maximum of 100).

          type: Return values as strings with `text`, or parse stored JSON values with `json`.

          with_metadata: Whether to include metadata in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        return cast(
            Optional[KeyBulkGetResponse],
            await self._post(
                path_template(
                    "/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk/get",
                    account_id=account_id,
                    namespace_id=namespace_id,
                ),
                body=await async_maybe_transform(
                    {
                        "keys": keys,
                        "type": type,
                        "with_metadata": with_metadata,
                    },
                    key_bulk_get_params.KeyBulkGetParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[KeyBulkGetResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[KeyBulkGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @typing_extensions.deprecated("Please use kv.namespaces.bulk_update instead")
    async def bulk_update(
        self,
        namespace_id: str,
        *,
        account_id: str,
        body: Iterable[key_bulk_update_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[KeyBulkUpdateResponse]:
        """
        Writes up to 10,000 key-value pairs to the specified Workers KV namespace from a
        JSON array, with optional metadata and expiration settings for each pair.
        Existing values and expirations are overwritten. If neither `expiration` nor
        `expiration_ttl` is specified, the key-value pair will not expire. If both are
        set, `expiration_ttl` takes precedence. The entire request must be 100 megabytes
        or less. The result reports the number of successful writes and any keys that
        failed and should be retried.

        Args:
          account_id: ID of the Cloudflare account that owns the Workers KV namespaces.

          namespace_id: ID of the Workers KV namespace.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        return await self._put(
            path_template(
                "/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk",
                account_id=account_id,
                namespace_id=namespace_id,
            ),
            body=await async_maybe_transform(body, Iterable[key_bulk_update_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[KeyBulkUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[KeyBulkUpdateResponse]], ResultWrapper[KeyBulkUpdateResponse]),
        )


class KeysResourceWithRawResponse:
    def __init__(self, keys: KeysResource) -> None:
        self._keys = keys

        self.list = to_raw_response_wrapper(
            keys.list,
        )
        self.bulk_delete = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                keys.bulk_delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.bulk_get = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                keys.bulk_get,  # pyright: ignore[reportDeprecated],
            )
        )
        self.bulk_update = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                keys.bulk_update,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncKeysResourceWithRawResponse:
    def __init__(self, keys: AsyncKeysResource) -> None:
        self._keys = keys

        self.list = async_to_raw_response_wrapper(
            keys.list,
        )
        self.bulk_delete = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                keys.bulk_delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.bulk_get = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                keys.bulk_get,  # pyright: ignore[reportDeprecated],
            )
        )
        self.bulk_update = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                keys.bulk_update,  # pyright: ignore[reportDeprecated],
            )
        )


class KeysResourceWithStreamingResponse:
    def __init__(self, keys: KeysResource) -> None:
        self._keys = keys

        self.list = to_streamed_response_wrapper(
            keys.list,
        )
        self.bulk_delete = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                keys.bulk_delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.bulk_get = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                keys.bulk_get,  # pyright: ignore[reportDeprecated],
            )
        )
        self.bulk_update = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                keys.bulk_update,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncKeysResourceWithStreamingResponse:
    def __init__(self, keys: AsyncKeysResource) -> None:
        self._keys = keys

        self.list = async_to_streamed_response_wrapper(
            keys.list,
        )
        self.bulk_delete = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                keys.bulk_delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.bulk_get = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                keys.bulk_get,  # pyright: ignore[reportDeprecated],
            )
        )
        self.bulk_update = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                keys.bulk_update,  # pyright: ignore[reportDeprecated],
            )
        )
