# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from .items import (
    ItemsResource,
    AsyncItemsResource,
    ItemsResourceWithRawResponse,
    AsyncItemsResourceWithRawResponse,
    ItemsResourceWithStreamingResponse,
    AsyncItemsResourceWithStreamingResponse,
)
from ......_types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ......_utils import path_template, maybe_transform, async_maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_wrappers import ResultWrapper
from ......pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ......_base_client import AsyncPaginator, make_request_options
from ......types.ddos_protection.advanced_tcp_protection.syn_protection import filter_list_params, filter_create_params
from ......types.ddos_protection.advanced_tcp_protection.syn_protection.filter_list_response import FilterListResponse
from ......types.ddos_protection.advanced_tcp_protection.syn_protection.filter_create_response import (
    FilterCreateResponse,
)
from ......types.ddos_protection.advanced_tcp_protection.syn_protection.filter_bulk_delete_response import (
    FilterBulkDeleteResponse,
)

__all__ = ["FiltersResource", "AsyncFiltersResource"]


class FiltersResource(SyncAPIResource):
    @cached_property
    def items(self) -> ItemsResource:
        return ItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> FiltersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return FiltersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FiltersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return FiltersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        expression: str,
        mode: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[FilterCreateResponse]:
        """
        Create a SYN Protection filter for an account.

        Args:
          account_id: Identifier.

          expression: The filter expression.

          mode: The filter's mode. Must be one of 'enabled', 'disabled', 'monitoring'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/filters",
                account_id=account_id,
            ),
            body=maybe_transform(
                {
                    "expression": expression,
                    "mode": mode,
                },
                filter_create_params.FilterCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FilterCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FilterCreateResponse]], ResultWrapper[FilterCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: str | Omit = omit,
        mode: str | Omit = omit,
        order: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[FilterListResponse]:
        """
        List all SYN Protection filters for an account.

        Args:
          account_id: Identifier.

          direction: The direction of ordering (ASC or DESC). Defaults to 'ASC'.

          mode: The mode of the filters to get. Optional. Valid values: 'enabled', 'disabled',
              'monitoring'.

          order: The field to order by. Defaults to 'prefix'.

          page: The page number for pagination. Defaults to 1.

          per_page: The number of items per page. Must be between 10 and 1000. Defaults to 25.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/filters",
                account_id=account_id,
            ),
            page=SyncV4PagePaginationArray[FilterListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "mode": mode,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    filter_list_params.FilterListParams,
                ),
            ),
            model=FilterListResponse,
        )

    def bulk_delete(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilterBulkDeleteResponse:
        """
        Delete all SYN Protection filters for an account.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/filters",
                account_id=account_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FilterBulkDeleteResponse,
        )


class AsyncFiltersResource(AsyncAPIResource):
    @cached_property
    def items(self) -> AsyncItemsResource:
        return AsyncItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFiltersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFiltersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFiltersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncFiltersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        expression: str,
        mode: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[FilterCreateResponse]:
        """
        Create a SYN Protection filter for an account.

        Args:
          account_id: Identifier.

          expression: The filter expression.

          mode: The filter's mode. Must be one of 'enabled', 'disabled', 'monitoring'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/filters",
                account_id=account_id,
            ),
            body=await async_maybe_transform(
                {
                    "expression": expression,
                    "mode": mode,
                },
                filter_create_params.FilterCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FilterCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FilterCreateResponse]], ResultWrapper[FilterCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: str | Omit = omit,
        mode: str | Omit = omit,
        order: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[FilterListResponse, AsyncV4PagePaginationArray[FilterListResponse]]:
        """
        List all SYN Protection filters for an account.

        Args:
          account_id: Identifier.

          direction: The direction of ordering (ASC or DESC). Defaults to 'ASC'.

          mode: The mode of the filters to get. Optional. Valid values: 'enabled', 'disabled',
              'monitoring'.

          order: The field to order by. Defaults to 'prefix'.

          page: The page number for pagination. Defaults to 1.

          per_page: The number of items per page. Must be between 10 and 1000. Defaults to 25.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/filters",
                account_id=account_id,
            ),
            page=AsyncV4PagePaginationArray[FilterListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "mode": mode,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    filter_list_params.FilterListParams,
                ),
            ),
            model=FilterListResponse,
        )

    async def bulk_delete(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilterBulkDeleteResponse:
        """
        Delete all SYN Protection filters for an account.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/filters",
                account_id=account_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FilterBulkDeleteResponse,
        )


class FiltersResourceWithRawResponse:
    def __init__(self, filters: FiltersResource) -> None:
        self._filters = filters

        self.create = to_raw_response_wrapper(
            filters.create,
        )
        self.list = to_raw_response_wrapper(
            filters.list,
        )
        self.bulk_delete = to_raw_response_wrapper(
            filters.bulk_delete,
        )

    @cached_property
    def items(self) -> ItemsResourceWithRawResponse:
        return ItemsResourceWithRawResponse(self._filters.items)


class AsyncFiltersResourceWithRawResponse:
    def __init__(self, filters: AsyncFiltersResource) -> None:
        self._filters = filters

        self.create = async_to_raw_response_wrapper(
            filters.create,
        )
        self.list = async_to_raw_response_wrapper(
            filters.list,
        )
        self.bulk_delete = async_to_raw_response_wrapper(
            filters.bulk_delete,
        )

    @cached_property
    def items(self) -> AsyncItemsResourceWithRawResponse:
        return AsyncItemsResourceWithRawResponse(self._filters.items)


class FiltersResourceWithStreamingResponse:
    def __init__(self, filters: FiltersResource) -> None:
        self._filters = filters

        self.create = to_streamed_response_wrapper(
            filters.create,
        )
        self.list = to_streamed_response_wrapper(
            filters.list,
        )
        self.bulk_delete = to_streamed_response_wrapper(
            filters.bulk_delete,
        )

    @cached_property
    def items(self) -> ItemsResourceWithStreamingResponse:
        return ItemsResourceWithStreamingResponse(self._filters.items)


class AsyncFiltersResourceWithStreamingResponse:
    def __init__(self, filters: AsyncFiltersResource) -> None:
        self._filters = filters

        self.create = async_to_streamed_response_wrapper(
            filters.create,
        )
        self.list = async_to_streamed_response_wrapper(
            filters.list,
        )
        self.bulk_delete = async_to_streamed_response_wrapper(
            filters.bulk_delete,
        )

    @cached_property
    def items(self) -> AsyncItemsResourceWithStreamingResponse:
        return AsyncItemsResourceWithStreamingResponse(self._filters.items)
