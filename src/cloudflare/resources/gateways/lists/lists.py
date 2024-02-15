# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, Type, Iterable, Optional, cast
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
from ...._base_client import (
    make_request_options,
)
from ....types.gateways import (
    ListGetResponse,
    ListDeleteResponse,
    ListUpdateResponse,
    ListZeroTrustListsListZeroTrustListsResponse,
    ListZeroTrustListsCreateZeroTrustListResponse,
    list_update_params,
    list_zero_trust_lists_create_zero_trust_list_params,
)

__all__ = ["Lists", "AsyncLists"]


class Lists(SyncAPIResource):
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
        account_id: object,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListUpdateResponse:
        """
        Updates a configured Zero Trust list.

        Args:
          list_id: API Resource UUID tag.

          name: The name of the list.

          description: The description of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._put(
            f"/accounts/{account_id}/gateway/lists/{list_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                },
                list_update_params.ListUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ListUpdateResponse], ResultWrapper[ListUpdateResponse]),
        )

    def delete(
        self,
        list_id: str,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListDeleteResponse:
        """
        Deletes a Zero Trust list.

        Args:
          list_id: API Resource UUID tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return cast(
            ListDeleteResponse,
            self._delete(
                f"/accounts/{account_id}/gateway/lists/{list_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ListDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        list_id: str,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListGetResponse:
        """
        Fetches a single Zero Trust list.

        Args:
          list_id: API Resource UUID tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._get(
            f"/accounts/{account_id}/gateway/lists/{list_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ListGetResponse], ResultWrapper[ListGetResponse]),
        )

    def zero_trust_lists_create_zero_trust_list(
        self,
        account_id: object,
        *,
        name: str,
        type: Literal["SERIAL", "URL", "DOMAIN", "EMAIL", "IP"],
        description: str | NotGiven = NOT_GIVEN,
        items: Iterable[list_zero_trust_lists_create_zero_trust_list_params.Item] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListZeroTrustListsCreateZeroTrustListResponse:
        """
        Creates a new Zero Trust list.

        Args:
          name: The name of the list.

          type: The type of list.

          description: The description of the list.

          items: The items in the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/accounts/{account_id}/gateway/lists",
            body=maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "description": description,
                    "items": items,
                },
                list_zero_trust_lists_create_zero_trust_list_params.ListZeroTrustListsCreateZeroTrustListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ListZeroTrustListsCreateZeroTrustListResponse],
                ResultWrapper[ListZeroTrustListsCreateZeroTrustListResponse],
            ),
        )

    def zero_trust_lists_list_zero_trust_lists(
        self,
        account_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ListZeroTrustListsListZeroTrustListsResponse]:
        """
        Fetches all Zero Trust lists for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_id}/gateway/lists",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ListZeroTrustListsListZeroTrustListsResponse]],
                ResultWrapper[ListZeroTrustListsListZeroTrustListsResponse],
            ),
        )


class AsyncLists(AsyncAPIResource):
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
        account_id: object,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListUpdateResponse:
        """
        Updates a configured Zero Trust list.

        Args:
          list_id: API Resource UUID tag.

          name: The name of the list.

          description: The description of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return await self._put(
            f"/accounts/{account_id}/gateway/lists/{list_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                },
                list_update_params.ListUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ListUpdateResponse], ResultWrapper[ListUpdateResponse]),
        )

    async def delete(
        self,
        list_id: str,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListDeleteResponse:
        """
        Deletes a Zero Trust list.

        Args:
          list_id: API Resource UUID tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return cast(
            ListDeleteResponse,
            await self._delete(
                f"/accounts/{account_id}/gateway/lists/{list_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ListDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        list_id: str,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListGetResponse:
        """
        Fetches a single Zero Trust list.

        Args:
          list_id: API Resource UUID tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return await self._get(
            f"/accounts/{account_id}/gateway/lists/{list_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ListGetResponse], ResultWrapper[ListGetResponse]),
        )

    async def zero_trust_lists_create_zero_trust_list(
        self,
        account_id: object,
        *,
        name: str,
        type: Literal["SERIAL", "URL", "DOMAIN", "EMAIL", "IP"],
        description: str | NotGiven = NOT_GIVEN,
        items: Iterable[list_zero_trust_lists_create_zero_trust_list_params.Item] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListZeroTrustListsCreateZeroTrustListResponse:
        """
        Creates a new Zero Trust list.

        Args:
          name: The name of the list.

          type: The type of list.

          description: The description of the list.

          items: The items in the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/accounts/{account_id}/gateway/lists",
            body=maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "description": description,
                    "items": items,
                },
                list_zero_trust_lists_create_zero_trust_list_params.ListZeroTrustListsCreateZeroTrustListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ListZeroTrustListsCreateZeroTrustListResponse],
                ResultWrapper[ListZeroTrustListsCreateZeroTrustListResponse],
            ),
        )

    async def zero_trust_lists_list_zero_trust_lists(
        self,
        account_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ListZeroTrustListsListZeroTrustListsResponse]:
        """
        Fetches all Zero Trust lists for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_id}/gateway/lists",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ListZeroTrustListsListZeroTrustListsResponse]],
                ResultWrapper[ListZeroTrustListsListZeroTrustListsResponse],
            ),
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
        self.zero_trust_lists_create_zero_trust_list = to_raw_response_wrapper(
            lists.zero_trust_lists_create_zero_trust_list,
        )
        self.zero_trust_lists_list_zero_trust_lists = to_raw_response_wrapper(
            lists.zero_trust_lists_list_zero_trust_lists,
        )

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
        self.zero_trust_lists_create_zero_trust_list = async_to_raw_response_wrapper(
            lists.zero_trust_lists_create_zero_trust_list,
        )
        self.zero_trust_lists_list_zero_trust_lists = async_to_raw_response_wrapper(
            lists.zero_trust_lists_list_zero_trust_lists,
        )

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
        self.zero_trust_lists_create_zero_trust_list = to_streamed_response_wrapper(
            lists.zero_trust_lists_create_zero_trust_list,
        )
        self.zero_trust_lists_list_zero_trust_lists = to_streamed_response_wrapper(
            lists.zero_trust_lists_list_zero_trust_lists,
        )

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
        self.zero_trust_lists_create_zero_trust_list = async_to_streamed_response_wrapper(
            lists.zero_trust_lists_create_zero_trust_list,
        )
        self.zero_trust_lists_list_zero_trust_lists = async_to_streamed_response_wrapper(
            lists.zero_trust_lists_list_zero_trust_lists,
        )

    @cached_property
    def items(self) -> AsyncItemsWithStreamingResponse:
        return AsyncItemsWithStreamingResponse(self._lists.items)
