# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, List, Iterable, cast

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import (
    make_request_options,
)
from .....types.storage.kv.namespaces import (
    BulkDeleteResponse,
    BulkWorkersKvNamespaceWriteMultipleKeyValuePairsResponse,
    bulk_delete_params,
    bulk_workers_kv_namespace_write_multiple_key_value_pairs_params,
)

__all__ = ["Bulks", "AsyncBulks"]


class Bulks(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BulksWithRawResponse:
        return BulksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BulksWithStreamingResponse:
        return BulksWithStreamingResponse(self)

    def delete(
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
    ) -> BulkDeleteResponse:
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
        return cast(
            BulkDeleteResponse,
            self._delete(
                f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk",
                body=maybe_transform(body, bulk_delete_params.BulkDeleteParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[BulkDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def workers_kv_namespace_write_multiple_key_value_pairs(
        self,
        namespace_id: str,
        *,
        account_id: str,
        body: Iterable[bulk_workers_kv_namespace_write_multiple_key_value_pairs_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkWorkersKvNamespaceWriteMultipleKeyValuePairsResponse:
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
        return cast(
            BulkWorkersKvNamespaceWriteMultipleKeyValuePairsResponse,
            self._put(
                f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk",
                body=maybe_transform(
                    body,
                    bulk_workers_kv_namespace_write_multiple_key_value_pairs_params.BulkWorkersKvNamespaceWriteMultipleKeyValuePairsParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[BulkWorkersKvNamespaceWriteMultipleKeyValuePairsResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncBulks(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBulksWithRawResponse:
        return AsyncBulksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBulksWithStreamingResponse:
        return AsyncBulksWithStreamingResponse(self)

    async def delete(
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
    ) -> BulkDeleteResponse:
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
        return cast(
            BulkDeleteResponse,
            await self._delete(
                f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk",
                body=maybe_transform(body, bulk_delete_params.BulkDeleteParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[BulkDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def workers_kv_namespace_write_multiple_key_value_pairs(
        self,
        namespace_id: str,
        *,
        account_id: str,
        body: Iterable[bulk_workers_kv_namespace_write_multiple_key_value_pairs_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkWorkersKvNamespaceWriteMultipleKeyValuePairsResponse:
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
        return cast(
            BulkWorkersKvNamespaceWriteMultipleKeyValuePairsResponse,
            await self._put(
                f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk",
                body=maybe_transform(
                    body,
                    bulk_workers_kv_namespace_write_multiple_key_value_pairs_params.BulkWorkersKvNamespaceWriteMultipleKeyValuePairsParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[BulkWorkersKvNamespaceWriteMultipleKeyValuePairsResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class BulksWithRawResponse:
    def __init__(self, bulks: Bulks) -> None:
        self._bulks = bulks

        self.delete = to_raw_response_wrapper(
            bulks.delete,
        )
        self.workers_kv_namespace_write_multiple_key_value_pairs = to_raw_response_wrapper(
            bulks.workers_kv_namespace_write_multiple_key_value_pairs,
        )


class AsyncBulksWithRawResponse:
    def __init__(self, bulks: AsyncBulks) -> None:
        self._bulks = bulks

        self.delete = async_to_raw_response_wrapper(
            bulks.delete,
        )
        self.workers_kv_namespace_write_multiple_key_value_pairs = async_to_raw_response_wrapper(
            bulks.workers_kv_namespace_write_multiple_key_value_pairs,
        )


class BulksWithStreamingResponse:
    def __init__(self, bulks: Bulks) -> None:
        self._bulks = bulks

        self.delete = to_streamed_response_wrapper(
            bulks.delete,
        )
        self.workers_kv_namespace_write_multiple_key_value_pairs = to_streamed_response_wrapper(
            bulks.workers_kv_namespace_write_multiple_key_value_pairs,
        )


class AsyncBulksWithStreamingResponse:
    def __init__(self, bulks: AsyncBulks) -> None:
        self._bulks = bulks

        self.delete = async_to_streamed_response_wrapper(
            bulks.delete,
        )
        self.workers_kv_namespace_write_multiple_key_value_pairs = async_to_streamed_response_wrapper(
            bulks.workers_kv_namespace_write_multiple_key_value_pairs,
        )
