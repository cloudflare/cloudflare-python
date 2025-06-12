# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Any, List, Type, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
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
        cursor: str | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        prefix: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorLimitPagination[Key]:
        """
        Lists a namespace's keys.

        Args:
          account_id: Identifier

          namespace_id: Namespace identifier tag.

          cursor: Opaque token indicating the position from which to continue when requesting the
              next set of records if the amount of list results was limited by the limit
              parameter. A valid value for the cursor can be obtained from the `cursors`
              object in the `result_info` structure.

          limit: The number of keys to return. The cursor attribute may be used to iterate over
              the next batch of keys if there are more than the limit.

          prefix: A string prefix used to filter down which keys will be returned. Exact matches
              and any key names that begin with the prefix will be returned.

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
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/keys",
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
        body: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[KeyBulkDeleteResponse]:
        """Remove multiple KV pairs from the namespace.

        Body should be an array of up to
        10,000 keys to be removed.

        Args:
          account_id: Identifier

          namespace_id: Namespace identifier tag.

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
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk/delete",
            body=maybe_transform(body, List[str]),
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
        keys: List[str],
        type: Literal["text", "json"] | NotGiven = NOT_GIVEN,
        with_metadata: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[KeyBulkGetResponse]:
        """Get multiple KV pairs from the namespace.

        Body should contain keys to retrieve
        at most 100. Keys must contain text-based values. If value is json, it can be
        requested to return in JSON, instead of string. Metadata can be return if
        withMetadata is true.

        Args:
          account_id: Identifier

          namespace_id: Namespace identifier tag.

          keys: Array of keys to retrieve (maximum 100)

          type: Whether to parse JSON values in the response

          with_metadata: Whether to include metadata in the response

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
                f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk/get",
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[KeyBulkUpdateResponse]:
        """Write multiple keys and values at once.

        Body should be an array of up to 10,000
        key-value pairs to be stored, along with optional expiration information.
        Existing values and expirations will be overwritten. If neither `expiration` nor
        `expiration_ttl` is specified, the key-value pair will never expire. If both are
        set, `expiration_ttl` is used and `expiration` is ignored. The entire request
        size must be 100 megabytes or less.

        Args:
          account_id: Identifier

          namespace_id: Namespace identifier tag.

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
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk",
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
        cursor: str | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        prefix: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Key, AsyncCursorLimitPagination[Key]]:
        """
        Lists a namespace's keys.

        Args:
          account_id: Identifier

          namespace_id: Namespace identifier tag.

          cursor: Opaque token indicating the position from which to continue when requesting the
              next set of records if the amount of list results was limited by the limit
              parameter. A valid value for the cursor can be obtained from the `cursors`
              object in the `result_info` structure.

          limit: The number of keys to return. The cursor attribute may be used to iterate over
              the next batch of keys if there are more than the limit.

          prefix: A string prefix used to filter down which keys will be returned. Exact matches
              and any key names that begin with the prefix will be returned.

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
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/keys",
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
        body: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[KeyBulkDeleteResponse]:
        """Remove multiple KV pairs from the namespace.

        Body should be an array of up to
        10,000 keys to be removed.

        Args:
          account_id: Identifier

          namespace_id: Namespace identifier tag.

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
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk/delete",
            body=await async_maybe_transform(body, List[str]),
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
        keys: List[str],
        type: Literal["text", "json"] | NotGiven = NOT_GIVEN,
        with_metadata: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[KeyBulkGetResponse]:
        """Get multiple KV pairs from the namespace.

        Body should contain keys to retrieve
        at most 100. Keys must contain text-based values. If value is json, it can be
        requested to return in JSON, instead of string. Metadata can be return if
        withMetadata is true.

        Args:
          account_id: Identifier

          namespace_id: Namespace identifier tag.

          keys: Array of keys to retrieve (maximum 100)

          type: Whether to parse JSON values in the response

          with_metadata: Whether to include metadata in the response

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
                f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk/get",
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[KeyBulkUpdateResponse]:
        """Write multiple keys and values at once.

        Body should be an array of up to 10,000
        key-value pairs to be stored, along with optional expiration information.
        Existing values and expirations will be overwritten. If neither `expiration` nor
        `expiration_ttl` is specified, the key-value pair will never expire. If both are
        set, `expiration_ttl` is used and `expiration` is ignored. The entire request
        size must be 100 megabytes or less.

        Args:
          account_id: Identifier

          namespace_id: Namespace identifier tag.

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
            f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk",
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
                keys.bulk_delete  # pyright: ignore[reportDeprecated],
            )
        )
        self.bulk_get = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                keys.bulk_get  # pyright: ignore[reportDeprecated],
            )
        )
        self.bulk_update = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                keys.bulk_update  # pyright: ignore[reportDeprecated],
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
                keys.bulk_delete  # pyright: ignore[reportDeprecated],
            )
        )
        self.bulk_get = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                keys.bulk_get  # pyright: ignore[reportDeprecated],
            )
        )
        self.bulk_update = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                keys.bulk_update  # pyright: ignore[reportDeprecated],
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
                keys.bulk_delete  # pyright: ignore[reportDeprecated],
            )
        )
        self.bulk_get = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                keys.bulk_get  # pyright: ignore[reportDeprecated],
            )
        )
        self.bulk_update = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                keys.bulk_update  # pyright: ignore[reportDeprecated],
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
                keys.bulk_delete  # pyright: ignore[reportDeprecated],
            )
        )
        self.bulk_get = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                keys.bulk_get  # pyright: ignore[reportDeprecated],
            )
        )
        self.bulk_update = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                keys.bulk_update  # pyright: ignore[reportDeprecated],
            )
        )
