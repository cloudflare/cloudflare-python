# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast

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
from .....pagination import SyncSinglePage, AsyncSinglePage, SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ....._base_client import AsyncPaginator, make_request_options
from .....types.ddos_protection.advanced_tcp_protection import (
    prefix_list_params,
    prefix_create_params,
    prefix_bulk_create_params,
)
from .....types.ddos_protection.advanced_tcp_protection.prefix_list_response import PrefixListResponse
from .....types.ddos_protection.advanced_tcp_protection.prefix_create_response import PrefixCreateResponse
from .....types.ddos_protection.advanced_tcp_protection.prefix_bulk_create_response import PrefixBulkCreateResponse
from .....types.ddos_protection.advanced_tcp_protection.prefix_bulk_delete_response import PrefixBulkDeleteResponse

__all__ = ["PrefixesResource", "AsyncPrefixesResource"]


class PrefixesResource(SyncAPIResource):
    @cached_property
    def items(self) -> ItemsResource:
        return ItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PrefixesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PrefixesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrefixesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PrefixesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        comment: str,
        excluded: bool,
        prefix: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[PrefixCreateResponse]:
        """
        Create a prefix for an account.

        Args:
          account_id: Identifier.

          comment: A comment describing the prefix.

          excluded: Whether to exclude the prefix from protection.

          prefix: The prefix to add in CIDR format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes", account_id=account_id
            ),
            body=maybe_transform(
                {
                    "comment": comment,
                    "excluded": excluded,
                    "prefix": prefix,
                },
                prefix_create_params.PrefixCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PrefixCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PrefixCreateResponse]], ResultWrapper[PrefixCreateResponse]),
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
    ) -> SyncV4PagePaginationArray[PrefixListResponse]:
        """
        List all prefixes for an account.

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
                "/accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes", account_id=account_id
            ),
            page=SyncV4PagePaginationArray[PrefixListResponse],
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
                    prefix_list_params.PrefixListParams,
                ),
            ),
            model=PrefixListResponse,
        )

    def bulk_create(
        self,
        *,
        account_id: str,
        body: Iterable[prefix_bulk_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[PrefixBulkCreateResponse]:
        """
        Create multiple prefixes for an account.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes/bulk", account_id=account_id
            ),
            page=SyncSinglePage[PrefixBulkCreateResponse],
            body=maybe_transform(body, Iterable[prefix_bulk_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=PrefixBulkCreateResponse,
            method="post",
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
    ) -> PrefixBulkDeleteResponse:
        """
        Delete all prefixes for an account.

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
                "/accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes", account_id=account_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrefixBulkDeleteResponse,
        )


class AsyncPrefixesResource(AsyncAPIResource):
    @cached_property
    def items(self) -> AsyncItemsResource:
        return AsyncItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPrefixesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPrefixesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrefixesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPrefixesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        comment: str,
        excluded: bool,
        prefix: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[PrefixCreateResponse]:
        """
        Create a prefix for an account.

        Args:
          account_id: Identifier.

          comment: A comment describing the prefix.

          excluded: Whether to exclude the prefix from protection.

          prefix: The prefix to add in CIDR format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes", account_id=account_id
            ),
            body=await async_maybe_transform(
                {
                    "comment": comment,
                    "excluded": excluded,
                    "prefix": prefix,
                },
                prefix_create_params.PrefixCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PrefixCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PrefixCreateResponse]], ResultWrapper[PrefixCreateResponse]),
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
    ) -> AsyncPaginator[PrefixListResponse, AsyncV4PagePaginationArray[PrefixListResponse]]:
        """
        List all prefixes for an account.

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
                "/accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes", account_id=account_id
            ),
            page=AsyncV4PagePaginationArray[PrefixListResponse],
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
                    prefix_list_params.PrefixListParams,
                ),
            ),
            model=PrefixListResponse,
        )

    def bulk_create(
        self,
        *,
        account_id: str,
        body: Iterable[prefix_bulk_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PrefixBulkCreateResponse, AsyncSinglePage[PrefixBulkCreateResponse]]:
        """
        Create multiple prefixes for an account.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes/bulk", account_id=account_id
            ),
            page=AsyncSinglePage[PrefixBulkCreateResponse],
            body=maybe_transform(body, Iterable[prefix_bulk_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=PrefixBulkCreateResponse,
            method="post",
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
    ) -> PrefixBulkDeleteResponse:
        """
        Delete all prefixes for an account.

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
                "/accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes", account_id=account_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrefixBulkDeleteResponse,
        )


class PrefixesResourceWithRawResponse:
    def __init__(self, prefixes: PrefixesResource) -> None:
        self._prefixes = prefixes

        self.create = to_raw_response_wrapper(
            prefixes.create,
        )
        self.list = to_raw_response_wrapper(
            prefixes.list,
        )
        self.bulk_create = to_raw_response_wrapper(
            prefixes.bulk_create,
        )
        self.bulk_delete = to_raw_response_wrapper(
            prefixes.bulk_delete,
        )

    @cached_property
    def items(self) -> ItemsResourceWithRawResponse:
        return ItemsResourceWithRawResponse(self._prefixes.items)


class AsyncPrefixesResourceWithRawResponse:
    def __init__(self, prefixes: AsyncPrefixesResource) -> None:
        self._prefixes = prefixes

        self.create = async_to_raw_response_wrapper(
            prefixes.create,
        )
        self.list = async_to_raw_response_wrapper(
            prefixes.list,
        )
        self.bulk_create = async_to_raw_response_wrapper(
            prefixes.bulk_create,
        )
        self.bulk_delete = async_to_raw_response_wrapper(
            prefixes.bulk_delete,
        )

    @cached_property
    def items(self) -> AsyncItemsResourceWithRawResponse:
        return AsyncItemsResourceWithRawResponse(self._prefixes.items)


class PrefixesResourceWithStreamingResponse:
    def __init__(self, prefixes: PrefixesResource) -> None:
        self._prefixes = prefixes

        self.create = to_streamed_response_wrapper(
            prefixes.create,
        )
        self.list = to_streamed_response_wrapper(
            prefixes.list,
        )
        self.bulk_create = to_streamed_response_wrapper(
            prefixes.bulk_create,
        )
        self.bulk_delete = to_streamed_response_wrapper(
            prefixes.bulk_delete,
        )

    @cached_property
    def items(self) -> ItemsResourceWithStreamingResponse:
        return ItemsResourceWithStreamingResponse(self._prefixes.items)


class AsyncPrefixesResourceWithStreamingResponse:
    def __init__(self, prefixes: AsyncPrefixesResource) -> None:
        self._prefixes = prefixes

        self.create = async_to_streamed_response_wrapper(
            prefixes.create,
        )
        self.list = async_to_streamed_response_wrapper(
            prefixes.list,
        )
        self.bulk_create = async_to_streamed_response_wrapper(
            prefixes.bulk_create,
        )
        self.bulk_delete = async_to_streamed_response_wrapper(
            prefixes.bulk_delete,
        )

    @cached_property
    def items(self) -> AsyncItemsResourceWithStreamingResponse:
        return AsyncItemsResourceWithStreamingResponse(self._prefixes.items)
