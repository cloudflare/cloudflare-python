# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from .....types.zero_trust.gateway.lists import ItemListResponse

__all__ = ["Items", "AsyncItems"]


class Items(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ItemsWithRawResponse:
        return ItemsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ItemsWithStreamingResponse:
        return ItemsWithStreamingResponse(self)

    def list(
        self,
        list_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ItemListResponse]:
        """
        Fetches all items in a single Zero Trust list.

        Args:
          list_id: API Resource UUID tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._get(
            f"/accounts/{account_id}/gateway/lists/{list_id}/items",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ItemListResponse]], ResultWrapper[ItemListResponse]),
        )


class AsyncItems(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncItemsWithRawResponse:
        return AsyncItemsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncItemsWithStreamingResponse:
        return AsyncItemsWithStreamingResponse(self)

    async def list(
        self,
        list_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ItemListResponse]:
        """
        Fetches all items in a single Zero Trust list.

        Args:
          list_id: API Resource UUID tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return await self._get(
            f"/accounts/{account_id}/gateway/lists/{list_id}/items",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ItemListResponse]], ResultWrapper[ItemListResponse]),
        )


class ItemsWithRawResponse:
    def __init__(self, items: Items) -> None:
        self._items = items

        self.list = to_raw_response_wrapper(
            items.list,
        )


class AsyncItemsWithRawResponse:
    def __init__(self, items: AsyncItems) -> None:
        self._items = items

        self.list = async_to_raw_response_wrapper(
            items.list,
        )


class ItemsWithStreamingResponse:
    def __init__(self, items: Items) -> None:
        self._items = items

        self.list = to_streamed_response_wrapper(
            items.list,
        )


class AsyncItemsWithStreamingResponse:
    def __init__(self, items: AsyncItems) -> None:
        self._items = items

        self.list = async_to_streamed_response_wrapper(
            items.list,
        )
