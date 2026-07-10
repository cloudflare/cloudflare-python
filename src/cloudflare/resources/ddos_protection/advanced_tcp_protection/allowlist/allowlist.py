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
from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from .....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ....._base_client import AsyncPaginator, make_request_options
from .....types.ddos_protection.advanced_tcp_protection import allowlist_list_params, allowlist_create_params
from .....types.ddos_protection.advanced_tcp_protection.allowlist_list_response import AllowlistListResponse
from .....types.ddos_protection.advanced_tcp_protection.allowlist_create_response import AllowlistCreateResponse
from .....types.ddos_protection.advanced_tcp_protection.allowlist_bulk_delete_response import (
    AllowlistBulkDeleteResponse,
)

__all__ = ["AllowlistResource", "AsyncAllowlistResource"]


class AllowlistResource(SyncAPIResource):
    @cached_property
    def items(self) -> ItemsResource:
        return ItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AllowlistResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AllowlistResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AllowlistResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AllowlistResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        comment: str,
        enabled: bool,
        prefix: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AllowlistCreateResponse]:
        """
        Create an allowlist prefix for an account.

        Args:
          account_id: Identifier.

          comment: An comment describing the allowlist prefix.

          enabled: Whether to enable the allowlist prefix into effect.

          prefix: The allowlist prefix to add in CIDR format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/magic/advanced_tcp_protection/configs/allowlist", account_id=account_id
            ),
            body=maybe_transform(
                {
                    "comment": comment,
                    "enabled": enabled,
                    "prefix": prefix,
                },
                allowlist_create_params.AllowlistCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AllowlistCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AllowlistCreateResponse]], ResultWrapper[AllowlistCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: str | Omit = omit,
        order: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[AllowlistListResponse]:
        """
        List all allowlist prefixes for an account.

        Args:
          account_id: Identifier.

          direction: The direction of ordering (ASC or DESC). Defaults to 'ASC'.

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
                "/accounts/{account_id}/magic/advanced_tcp_protection/configs/allowlist", account_id=account_id
            ),
            page=SyncV4PagePaginationArray[AllowlistListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    allowlist_list_params.AllowlistListParams,
                ),
            ),
            model=AllowlistListResponse,
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
    ) -> AllowlistBulkDeleteResponse:
        """
        Delete all allowlist prefixes for an account.

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
                "/accounts/{account_id}/magic/advanced_tcp_protection/configs/allowlist", account_id=account_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AllowlistBulkDeleteResponse,
        )


class AsyncAllowlistResource(AsyncAPIResource):
    @cached_property
    def items(self) -> AsyncItemsResource:
        return AsyncItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAllowlistResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAllowlistResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAllowlistResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAllowlistResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        comment: str,
        enabled: bool,
        prefix: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AllowlistCreateResponse]:
        """
        Create an allowlist prefix for an account.

        Args:
          account_id: Identifier.

          comment: An comment describing the allowlist prefix.

          enabled: Whether to enable the allowlist prefix into effect.

          prefix: The allowlist prefix to add in CIDR format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/magic/advanced_tcp_protection/configs/allowlist", account_id=account_id
            ),
            body=await async_maybe_transform(
                {
                    "comment": comment,
                    "enabled": enabled,
                    "prefix": prefix,
                },
                allowlist_create_params.AllowlistCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AllowlistCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AllowlistCreateResponse]], ResultWrapper[AllowlistCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: str | Omit = omit,
        order: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AllowlistListResponse, AsyncV4PagePaginationArray[AllowlistListResponse]]:
        """
        List all allowlist prefixes for an account.

        Args:
          account_id: Identifier.

          direction: The direction of ordering (ASC or DESC). Defaults to 'ASC'.

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
                "/accounts/{account_id}/magic/advanced_tcp_protection/configs/allowlist", account_id=account_id
            ),
            page=AsyncV4PagePaginationArray[AllowlistListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    allowlist_list_params.AllowlistListParams,
                ),
            ),
            model=AllowlistListResponse,
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
    ) -> AllowlistBulkDeleteResponse:
        """
        Delete all allowlist prefixes for an account.

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
                "/accounts/{account_id}/magic/advanced_tcp_protection/configs/allowlist", account_id=account_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AllowlistBulkDeleteResponse,
        )


class AllowlistResourceWithRawResponse:
    def __init__(self, allowlist: AllowlistResource) -> None:
        self._allowlist = allowlist

        self.create = to_raw_response_wrapper(
            allowlist.create,
        )
        self.list = to_raw_response_wrapper(
            allowlist.list,
        )
        self.bulk_delete = to_raw_response_wrapper(
            allowlist.bulk_delete,
        )

    @cached_property
    def items(self) -> ItemsResourceWithRawResponse:
        return ItemsResourceWithRawResponse(self._allowlist.items)


class AsyncAllowlistResourceWithRawResponse:
    def __init__(self, allowlist: AsyncAllowlistResource) -> None:
        self._allowlist = allowlist

        self.create = async_to_raw_response_wrapper(
            allowlist.create,
        )
        self.list = async_to_raw_response_wrapper(
            allowlist.list,
        )
        self.bulk_delete = async_to_raw_response_wrapper(
            allowlist.bulk_delete,
        )

    @cached_property
    def items(self) -> AsyncItemsResourceWithRawResponse:
        return AsyncItemsResourceWithRawResponse(self._allowlist.items)


class AllowlistResourceWithStreamingResponse:
    def __init__(self, allowlist: AllowlistResource) -> None:
        self._allowlist = allowlist

        self.create = to_streamed_response_wrapper(
            allowlist.create,
        )
        self.list = to_streamed_response_wrapper(
            allowlist.list,
        )
        self.bulk_delete = to_streamed_response_wrapper(
            allowlist.bulk_delete,
        )

    @cached_property
    def items(self) -> ItemsResourceWithStreamingResponse:
        return ItemsResourceWithStreamingResponse(self._allowlist.items)


class AsyncAllowlistResourceWithStreamingResponse:
    def __init__(self, allowlist: AsyncAllowlistResource) -> None:
        self._allowlist = allowlist

        self.create = async_to_streamed_response_wrapper(
            allowlist.create,
        )
        self.list = async_to_streamed_response_wrapper(
            allowlist.list,
        )
        self.bulk_delete = async_to_streamed_response_wrapper(
            allowlist.bulk_delete,
        )

    @cached_property
    def items(self) -> AsyncItemsResourceWithStreamingResponse:
        return AsyncItemsResourceWithStreamingResponse(self._allowlist.items)
