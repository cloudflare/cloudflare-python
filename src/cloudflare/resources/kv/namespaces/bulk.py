# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Iterable, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.kv.namespaces import BulkDeleteResponse, BulkUpdateResponse, bulk_delete_params, bulk_update_params

__all__ = ["Bulk", "AsyncBulk"]


class Bulk(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BulkWithRawResponse:
        return BulkWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BulkWithStreamingResponse:
        return BulkWithStreamingResponse(self)

    def update(
        self,
        namespace_id: str,
        *,
        account_id: str,
        body: Iterable[bulk_update_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkUpdateResponse:
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
            BulkUpdateResponse,
            self._put(
                f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk",
                body=maybe_transform(body, bulk_update_params.BulkUpdateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[BulkUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

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


class AsyncBulk(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBulkWithRawResponse:
        return AsyncBulkWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBulkWithStreamingResponse:
        return AsyncBulkWithStreamingResponse(self)

    async def update(
        self,
        namespace_id: str,
        *,
        account_id: str,
        body: Iterable[bulk_update_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkUpdateResponse:
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
            BulkUpdateResponse,
            await self._put(
                f"/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk",
                body=await async_maybe_transform(body, bulk_update_params.BulkUpdateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[BulkUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

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
                body=await async_maybe_transform(body, bulk_delete_params.BulkDeleteParams),
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


class BulkWithRawResponse:
    def __init__(self, bulk: Bulk) -> None:
        self._bulk = bulk

        self.update = to_raw_response_wrapper(
            bulk.update,
        )
        self.delete = to_raw_response_wrapper(
            bulk.delete,
        )


class AsyncBulkWithRawResponse:
    def __init__(self, bulk: AsyncBulk) -> None:
        self._bulk = bulk

        self.update = async_to_raw_response_wrapper(
            bulk.update,
        )
        self.delete = async_to_raw_response_wrapper(
            bulk.delete,
        )


class BulkWithStreamingResponse:
    def __init__(self, bulk: Bulk) -> None:
        self._bulk = bulk

        self.update = to_streamed_response_wrapper(
            bulk.update,
        )
        self.delete = to_streamed_response_wrapper(
            bulk.delete,
        )


class AsyncBulkWithStreamingResponse:
    def __init__(self, bulk: AsyncBulk) -> None:
        self._bulk = bulk

        self.update = async_to_streamed_response_wrapper(
            bulk.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            bulk.delete,
        )
