# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ....types.rules.lists import BulkOperationGetResponse

__all__ = ["BulkOperations", "AsyncBulkOperations"]


class BulkOperations(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BulkOperationsWithRawResponse:
        return BulkOperationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BulkOperationsWithStreamingResponse:
        return BulkOperationsWithStreamingResponse(self)

    def get(
        self,
        operation_id: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[BulkOperationGetResponse]:
        """
        Gets the current status of an asynchronous operation on a list.

        The `status` property can have one of the following values: `pending`,
        `running`, `completed`, or `failed`. If the status is `failed`, the `error`
        property will contain a message describing the error.

        Args:
          account_identifier: Identifier

          operation_id: The unique operation ID of the asynchronous action.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not operation_id:
            raise ValueError(f"Expected a non-empty value for `operation_id` but received {operation_id!r}")
        return self._get(
            f"/accounts/{account_identifier}/rules/lists/bulk_operations/{operation_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[BulkOperationGetResponse]], ResultWrapper[BulkOperationGetResponse]),
        )


class AsyncBulkOperations(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBulkOperationsWithRawResponse:
        return AsyncBulkOperationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBulkOperationsWithStreamingResponse:
        return AsyncBulkOperationsWithStreamingResponse(self)

    async def get(
        self,
        operation_id: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[BulkOperationGetResponse]:
        """
        Gets the current status of an asynchronous operation on a list.

        The `status` property can have one of the following values: `pending`,
        `running`, `completed`, or `failed`. If the status is `failed`, the `error`
        property will contain a message describing the error.

        Args:
          account_identifier: Identifier

          operation_id: The unique operation ID of the asynchronous action.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not operation_id:
            raise ValueError(f"Expected a non-empty value for `operation_id` but received {operation_id!r}")
        return await self._get(
            f"/accounts/{account_identifier}/rules/lists/bulk_operations/{operation_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[BulkOperationGetResponse]], ResultWrapper[BulkOperationGetResponse]),
        )


class BulkOperationsWithRawResponse:
    def __init__(self, bulk_operations: BulkOperations) -> None:
        self._bulk_operations = bulk_operations

        self.get = to_raw_response_wrapper(
            bulk_operations.get,
        )


class AsyncBulkOperationsWithRawResponse:
    def __init__(self, bulk_operations: AsyncBulkOperations) -> None:
        self._bulk_operations = bulk_operations

        self.get = async_to_raw_response_wrapper(
            bulk_operations.get,
        )


class BulkOperationsWithStreamingResponse:
    def __init__(self, bulk_operations: BulkOperations) -> None:
        self._bulk_operations = bulk_operations

        self.get = to_streamed_response_wrapper(
            bulk_operations.get,
        )


class AsyncBulkOperationsWithStreamingResponse:
    def __init__(self, bulk_operations: AsyncBulkOperations) -> None:
        self._bulk_operations = bulk_operations

        self.get = async_to_streamed_response_wrapper(
            bulk_operations.get,
        )
