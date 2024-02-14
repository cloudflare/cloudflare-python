# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from .items import (
    Items,
    AsyncItems,
    ItemsWithRawResponse,
    AsyncItemsWithRawResponse,
    ItemsWithStreamingResponse,
    AsyncItemsWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....types.rules import (
    ListGetResponse,
    ListDeleteResponse,
    ListUpdateResponse,
    ListListsGetListsResponse,
    ListListsCreateAListResponse,
    list_update_params,
    list_lists_create_a_list_params,
)
from ...._base_client import (
    make_request_options,
)
from .bulk_operations import (
    BulkOperations,
    AsyncBulkOperations,
    BulkOperationsWithRawResponse,
    AsyncBulkOperationsWithRawResponse,
    BulkOperationsWithStreamingResponse,
    AsyncBulkOperationsWithStreamingResponse,
)

__all__ = ["Lists", "AsyncLists"]


class Lists(SyncAPIResource):
    @cached_property
    def bulk_operations(self) -> BulkOperations:
        return BulkOperations(self._client)

    @cached_property
    def items(self) -> Items:
        return Items(self._client)

    @cached_property
    def with_raw_response(self) -> ListsWithRawResponse:
        return ListsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ListsWithStreamingResponse:
        return ListsWithStreamingResponse(self)

    def update(
        self,
        list_id: str,
        *,
        account_id: str,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ListUpdateResponse]:
        """
        Updates the description of a list.

        Args:
          account_id: Identifier

          list_id: The unique ID of the list.

          description: An informative summary of the list.

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
            f"/accounts/{account_id}/rules/lists/{list_id}",
            body=maybe_transform({"description": description}, list_update_params.ListUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ListUpdateResponse]], ResultWrapper[ListUpdateResponse]),
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
    ) -> Optional[ListDeleteResponse]:
        """
        Deletes a specific list and all its items.

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
            f"/accounts/{account_id}/rules/lists/{list_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ListDeleteResponse]], ResultWrapper[ListDeleteResponse]),
        )

    def get(
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
    ) -> Optional[ListGetResponse]:
        """
        Fetches the details of a list.

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
        return self._get(
            f"/accounts/{account_id}/rules/lists/{list_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ListGetResponse]], ResultWrapper[ListGetResponse]),
        )

    def lists_create_a_list(
        self,
        account_id: str,
        *,
        kind: Literal["ip", "redirect", "hostname", "asn"],
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ListListsCreateAListResponse]:
        """
        Creates a new list of the specified type.

        Args:
          account_id: Identifier

          kind: The type of the list. Each type supports specific list items (IP addresses,
              ASNs, hostnames or redirects).

          name: An informative name for the list. Use this name in filter and rule expressions.

          description: An informative summary of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/rules/lists",
            body=maybe_transform(
                {
                    "kind": kind,
                    "name": name,
                    "description": description,
                },
                list_lists_create_a_list_params.ListListsCreateAListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ListListsCreateAListResponse]], ResultWrapper[ListListsCreateAListResponse]),
        )

    def lists_get_lists(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ListListsGetListsResponse]:
        """
        Fetches all lists in the account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/rules/lists",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ListListsGetListsResponse]], ResultWrapper[ListListsGetListsResponse]),
        )


class AsyncLists(AsyncAPIResource):
    @cached_property
    def bulk_operations(self) -> AsyncBulkOperations:
        return AsyncBulkOperations(self._client)

    @cached_property
    def items(self) -> AsyncItems:
        return AsyncItems(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncListsWithRawResponse:
        return AsyncListsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncListsWithStreamingResponse:
        return AsyncListsWithStreamingResponse(self)

    async def update(
        self,
        list_id: str,
        *,
        account_id: str,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ListUpdateResponse]:
        """
        Updates the description of a list.

        Args:
          account_id: Identifier

          list_id: The unique ID of the list.

          description: An informative summary of the list.

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
            f"/accounts/{account_id}/rules/lists/{list_id}",
            body=maybe_transform({"description": description}, list_update_params.ListUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ListUpdateResponse]], ResultWrapper[ListUpdateResponse]),
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
    ) -> Optional[ListDeleteResponse]:
        """
        Deletes a specific list and all its items.

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
            f"/accounts/{account_id}/rules/lists/{list_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ListDeleteResponse]], ResultWrapper[ListDeleteResponse]),
        )

    async def get(
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
    ) -> Optional[ListGetResponse]:
        """
        Fetches the details of a list.

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
        return await self._get(
            f"/accounts/{account_id}/rules/lists/{list_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ListGetResponse]], ResultWrapper[ListGetResponse]),
        )

    async def lists_create_a_list(
        self,
        account_id: str,
        *,
        kind: Literal["ip", "redirect", "hostname", "asn"],
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ListListsCreateAListResponse]:
        """
        Creates a new list of the specified type.

        Args:
          account_id: Identifier

          kind: The type of the list. Each type supports specific list items (IP addresses,
              ASNs, hostnames or redirects).

          name: An informative name for the list. Use this name in filter and rule expressions.

          description: An informative summary of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/rules/lists",
            body=maybe_transform(
                {
                    "kind": kind,
                    "name": name,
                    "description": description,
                },
                list_lists_create_a_list_params.ListListsCreateAListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ListListsCreateAListResponse]], ResultWrapper[ListListsCreateAListResponse]),
        )

    async def lists_get_lists(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ListListsGetListsResponse]:
        """
        Fetches all lists in the account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/rules/lists",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ListListsGetListsResponse]], ResultWrapper[ListListsGetListsResponse]),
        )


class ListsWithRawResponse:
    def __init__(self, lists: Lists) -> None:
        self._lists = lists

        self.update = to_raw_response_wrapper(
            lists.update,
        )
        self.delete = to_raw_response_wrapper(
            lists.delete,
        )
        self.get = to_raw_response_wrapper(
            lists.get,
        )
        self.lists_create_a_list = to_raw_response_wrapper(
            lists.lists_create_a_list,
        )
        self.lists_get_lists = to_raw_response_wrapper(
            lists.lists_get_lists,
        )

    @cached_property
    def bulk_operations(self) -> BulkOperationsWithRawResponse:
        return BulkOperationsWithRawResponse(self._lists.bulk_operations)

    @cached_property
    def items(self) -> ItemsWithRawResponse:
        return ItemsWithRawResponse(self._lists.items)


class AsyncListsWithRawResponse:
    def __init__(self, lists: AsyncLists) -> None:
        self._lists = lists

        self.update = async_to_raw_response_wrapper(
            lists.update,
        )
        self.delete = async_to_raw_response_wrapper(
            lists.delete,
        )
        self.get = async_to_raw_response_wrapper(
            lists.get,
        )
        self.lists_create_a_list = async_to_raw_response_wrapper(
            lists.lists_create_a_list,
        )
        self.lists_get_lists = async_to_raw_response_wrapper(
            lists.lists_get_lists,
        )

    @cached_property
    def bulk_operations(self) -> AsyncBulkOperationsWithRawResponse:
        return AsyncBulkOperationsWithRawResponse(self._lists.bulk_operations)

    @cached_property
    def items(self) -> AsyncItemsWithRawResponse:
        return AsyncItemsWithRawResponse(self._lists.items)


class ListsWithStreamingResponse:
    def __init__(self, lists: Lists) -> None:
        self._lists = lists

        self.update = to_streamed_response_wrapper(
            lists.update,
        )
        self.delete = to_streamed_response_wrapper(
            lists.delete,
        )
        self.get = to_streamed_response_wrapper(
            lists.get,
        )
        self.lists_create_a_list = to_streamed_response_wrapper(
            lists.lists_create_a_list,
        )
        self.lists_get_lists = to_streamed_response_wrapper(
            lists.lists_get_lists,
        )

    @cached_property
    def bulk_operations(self) -> BulkOperationsWithStreamingResponse:
        return BulkOperationsWithStreamingResponse(self._lists.bulk_operations)

    @cached_property
    def items(self) -> ItemsWithStreamingResponse:
        return ItemsWithStreamingResponse(self._lists.items)


class AsyncListsWithStreamingResponse:
    def __init__(self, lists: AsyncLists) -> None:
        self._lists = lists

        self.update = async_to_streamed_response_wrapper(
            lists.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            lists.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            lists.get,
        )
        self.lists_create_a_list = async_to_streamed_response_wrapper(
            lists.lists_create_a_list,
        )
        self.lists_get_lists = async_to_streamed_response_wrapper(
            lists.lists_get_lists,
        )

    @cached_property
    def bulk_operations(self) -> AsyncBulkOperationsWithStreamingResponse:
        return AsyncBulkOperationsWithStreamingResponse(self._lists.bulk_operations)

    @cached_property
    def items(self) -> AsyncItemsWithStreamingResponse:
        return AsyncItemsWithStreamingResponse(self._lists.items)
