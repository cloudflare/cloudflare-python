# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast

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
from ....pagination import SyncCursorPagination, AsyncCursorPagination
from ...._base_client import AsyncPaginator, make_request_options
from ....types.rules.lists import item_list_params, item_create_params, item_update_params
from ....types.rules.lists.item_get_response import ItemGetResponse
from ....types.rules.lists.item_list_response import ItemListResponse
from ....types.rules.lists.item_create_response import ItemCreateResponse
from ....types.rules.lists.item_delete_response import ItemDeleteResponse
from ....types.rules.lists.item_update_response import ItemUpdateResponse

__all__ = ["ItemsResource", "AsyncItemsResource"]


class ItemsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ItemsResourceWithStreamingResponse(self)

    def create(
        self,
        list_id: str,
        *,
        account_id: str,
        body: Iterable[item_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ItemCreateResponse:
        """Appends new items to the list.

        This operation is asynchronous.

        To get current the operation status, invoke the
        [Get bulk operation status](/operations/lists-get-bulk-operation-status)
        endpoint with the returned `operation_id`.

        Args:
          account_id: Identifier

          list_id: The unique ID of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._post(
            f"/accounts/{account_id}/rules/lists/{list_id}/items",
            body=maybe_transform(body, Iterable[item_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ItemCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[ItemCreateResponse], ResultWrapper[ItemCreateResponse]),
        )

    def update(
        self,
        list_id: str,
        *,
        account_id: str,
        body: Iterable[item_update_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ItemUpdateResponse:
        """
        Removes all existing items from the list and adds the provided items to the
        list.

        This operation is asynchronous. To get current the operation status, invoke the
        [Get bulk operation status](/operations/lists-get-bulk-operation-status)
        endpoint with the returned `operation_id`.

        Args:
          account_id: Identifier

          list_id: The unique ID of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._put(
            f"/accounts/{account_id}/rules/lists/{list_id}/items",
            body=maybe_transform(body, Iterable[item_update_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ItemUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[ItemUpdateResponse], ResultWrapper[ItemUpdateResponse]),
        )

    def list(
        self,
        list_id: str,
        *,
        account_id: str,
        cursor: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPagination[ItemListResponse]:
        """
        Fetches all the items in the list.

        Args:
          account_id: Identifier

          list_id: The unique ID of the list.

          cursor: The pagination cursor. An opaque string token indicating the position from which
              to continue when requesting the next/previous set of records. Cursor values are
              provided under `result_info.cursors` in the response. You should make no
              assumptions about a cursor's content or length.

          per_page: Amount of results to include in each paginated response. A non-negative 32 bit
              integer.

          search:
              A search query to filter returned items. Its meaning depends on the list type:
              IP addresses must start with the provided string, hostnames and bulk redirects
              must contain the string, and ASNs must match the string exactly.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/rules/lists/{list_id}/items",
            page=SyncCursorPagination[ItemListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "per_page": per_page,
                        "search": search,
                    },
                    item_list_params.ItemListParams,
                ),
            ),
            model=ItemListResponse,
        )

    def delete(
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
    ) -> ItemDeleteResponse:
        """Removes one or more items from a list.

        This operation is asynchronous.

        To get current the operation status, invoke the
        [Get bulk operation status](/operations/lists-get-bulk-operation-status)
        endpoint with the returned `operation_id`.

        Args:
          account_id: Identifier

          list_id: The unique ID of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._delete(
            f"/accounts/{account_id}/rules/lists/{list_id}/items",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ItemDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[ItemDeleteResponse], ResultWrapper[ItemDeleteResponse]),
        )

    def get(
        self,
        item_id: str,
        *,
        account_identifier: str,
        list_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ItemGetResponse:
        """
        Fetches a list item in the list.

        Args:
          account_identifier: Identifier

          list_id: The unique ID of the list.

          item_id: The unique ID of the item in the List.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return self._get(
            f"/accounts/{account_identifier}/rules/lists/{list_id}/items/{item_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ItemGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[ItemGetResponse], ResultWrapper[ItemGetResponse]),
        )


class AsyncItemsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncItemsResourceWithStreamingResponse(self)

    async def create(
        self,
        list_id: str,
        *,
        account_id: str,
        body: Iterable[item_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ItemCreateResponse:
        """Appends new items to the list.

        This operation is asynchronous.

        To get current the operation status, invoke the
        [Get bulk operation status](/operations/lists-get-bulk-operation-status)
        endpoint with the returned `operation_id`.

        Args:
          account_id: Identifier

          list_id: The unique ID of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return await self._post(
            f"/accounts/{account_id}/rules/lists/{list_id}/items",
            body=await async_maybe_transform(body, Iterable[item_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ItemCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[ItemCreateResponse], ResultWrapper[ItemCreateResponse]),
        )

    async def update(
        self,
        list_id: str,
        *,
        account_id: str,
        body: Iterable[item_update_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ItemUpdateResponse:
        """
        Removes all existing items from the list and adds the provided items to the
        list.

        This operation is asynchronous. To get current the operation status, invoke the
        [Get bulk operation status](/operations/lists-get-bulk-operation-status)
        endpoint with the returned `operation_id`.

        Args:
          account_id: Identifier

          list_id: The unique ID of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return await self._put(
            f"/accounts/{account_id}/rules/lists/{list_id}/items",
            body=await async_maybe_transform(body, Iterable[item_update_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ItemUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[ItemUpdateResponse], ResultWrapper[ItemUpdateResponse]),
        )

    def list(
        self,
        list_id: str,
        *,
        account_id: str,
        cursor: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ItemListResponse, AsyncCursorPagination[ItemListResponse]]:
        """
        Fetches all the items in the list.

        Args:
          account_id: Identifier

          list_id: The unique ID of the list.

          cursor: The pagination cursor. An opaque string token indicating the position from which
              to continue when requesting the next/previous set of records. Cursor values are
              provided under `result_info.cursors` in the response. You should make no
              assumptions about a cursor's content or length.

          per_page: Amount of results to include in each paginated response. A non-negative 32 bit
              integer.

          search:
              A search query to filter returned items. Its meaning depends on the list type:
              IP addresses must start with the provided string, hostnames and bulk redirects
              must contain the string, and ASNs must match the string exactly.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/rules/lists/{list_id}/items",
            page=AsyncCursorPagination[ItemListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "per_page": per_page,
                        "search": search,
                    },
                    item_list_params.ItemListParams,
                ),
            ),
            model=ItemListResponse,
        )

    async def delete(
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
    ) -> ItemDeleteResponse:
        """Removes one or more items from a list.

        This operation is asynchronous.

        To get current the operation status, invoke the
        [Get bulk operation status](/operations/lists-get-bulk-operation-status)
        endpoint with the returned `operation_id`.

        Args:
          account_id: Identifier

          list_id: The unique ID of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/rules/lists/{list_id}/items",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ItemDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[ItemDeleteResponse], ResultWrapper[ItemDeleteResponse]),
        )

    async def get(
        self,
        item_id: str,
        *,
        account_identifier: str,
        list_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ItemGetResponse:
        """
        Fetches a list item in the list.

        Args:
          account_identifier: Identifier

          list_id: The unique ID of the list.

          item_id: The unique ID of the item in the List.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return await self._get(
            f"/accounts/{account_identifier}/rules/lists/{list_id}/items/{item_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ItemGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[ItemGetResponse], ResultWrapper[ItemGetResponse]),
        )


class ItemsResourceWithRawResponse:
    def __init__(self, items: ItemsResource) -> None:
        self._items = items

        self.create = to_raw_response_wrapper(
            items.create,
        )
        self.update = to_raw_response_wrapper(
            items.update,
        )
        self.list = to_raw_response_wrapper(
            items.list,
        )
        self.delete = to_raw_response_wrapper(
            items.delete,
        )
        self.get = to_raw_response_wrapper(
            items.get,
        )


class AsyncItemsResourceWithRawResponse:
    def __init__(self, items: AsyncItemsResource) -> None:
        self._items = items

        self.create = async_to_raw_response_wrapper(
            items.create,
        )
        self.update = async_to_raw_response_wrapper(
            items.update,
        )
        self.list = async_to_raw_response_wrapper(
            items.list,
        )
        self.delete = async_to_raw_response_wrapper(
            items.delete,
        )
        self.get = async_to_raw_response_wrapper(
            items.get,
        )


class ItemsResourceWithStreamingResponse:
    def __init__(self, items: ItemsResource) -> None:
        self._items = items

        self.create = to_streamed_response_wrapper(
            items.create,
        )
        self.update = to_streamed_response_wrapper(
            items.update,
        )
        self.list = to_streamed_response_wrapper(
            items.list,
        )
        self.delete = to_streamed_response_wrapper(
            items.delete,
        )
        self.get = to_streamed_response_wrapper(
            items.get,
        )


class AsyncItemsResourceWithStreamingResponse:
    def __init__(self, items: AsyncItemsResource) -> None:
        self._items = items

        self.create = async_to_streamed_response_wrapper(
            items.create,
        )
        self.update = async_to_streamed_response_wrapper(
            items.update,
        )
        self.list = async_to_streamed_response_wrapper(
            items.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            items.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            items.get,
        )
