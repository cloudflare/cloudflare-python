# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ..._base_client import AsyncPaginator, make_request_options
from ...types.tenants import account_list_params
from ...types.tenants.account_list_response import AccountListResponse

__all__ = ["AccountsResource", "AsyncAccountsResource"]


class AccountsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AccountsResourceWithStreamingResponse(self)

    def list(
        self,
        tenant_id: str,
        *,
        account_pubname: account_list_params.AccountPubname | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        include_total: bool | Omit = omit,
        name: account_list_params.Name | Omit = omit,
        order_by: Literal["account_name"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        page_token: str | Omit = omit,
        per_page: int | Omit = omit,
        status: Literal["active", "deleted"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[AccountListResponse]:
        """
        Lists all Cloudflare accounts across this tenant's hierarchy using the legacy
        Account response shape. Use `GET /organizations/{organization_id}/accounts` to
        list only accounts immediately attached to a specific Organization using the
        modern Account response shape. Use `page_token` and `page_size` for cursor
        pagination, or provide `page` and `per_page` together for legacy offset
        pagination. Cursor pagination takes precedence when requested.

        Args:
          direction: Sort direction for the order_by field. Valid values: `asc`, `desc`. Defaults to
              `asc` when order_by is specified.

          include_total: Whether to calculate and return the exact `result_info.total_size` for cursor
              pagination. Defaults to true. When false, `total_size` is omitted. Legacy
              `page`/`per_page` requests always calculate `total_count`.

          order_by: Field to order results by. Currently supported values: `account_name`.

          page: Legacy offset page number. Must be provided with `per_page`. Values below 1 are
              treated as

              1. Cursor pagination takes precedence when requested.

          page_size: The amount of items to return. Defaults to 10.

          page_token: An opaque token returned from the last list response that when provided will
              retrieve the next page.

              Parameters used to filter the retrieved list must remain in subsequent requests
              with a page token.

          per_page: Legacy offset page size. Must be provided with `page`. Values are clamped to the
              range 1-100. Cursor pagination takes precedence when requested.

          status: Filter accounts by lifecycle status. Defaults to `active`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return self._get_api_list(
            path_template("/tenants/{tenant_id}/accounts", tenant_id=tenant_id),
            page=SyncV4PagePaginationArray[AccountListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_pubname": account_pubname,
                        "direction": direction,
                        "include_total": include_total,
                        "name": name,
                        "order_by": order_by,
                        "page": page,
                        "page_size": page_size,
                        "page_token": page_token,
                        "per_page": per_page,
                        "status": status,
                    },
                    account_list_params.AccountListParams,
                ),
            ),
            model=AccountListResponse,
        )


class AsyncAccountsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAccountsResourceWithStreamingResponse(self)

    def list(
        self,
        tenant_id: str,
        *,
        account_pubname: account_list_params.AccountPubname | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        include_total: bool | Omit = omit,
        name: account_list_params.Name | Omit = omit,
        order_by: Literal["account_name"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        page_token: str | Omit = omit,
        per_page: int | Omit = omit,
        status: Literal["active", "deleted"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AccountListResponse, AsyncV4PagePaginationArray[AccountListResponse]]:
        """
        Lists all Cloudflare accounts across this tenant's hierarchy using the legacy
        Account response shape. Use `GET /organizations/{organization_id}/accounts` to
        list only accounts immediately attached to a specific Organization using the
        modern Account response shape. Use `page_token` and `page_size` for cursor
        pagination, or provide `page` and `per_page` together for legacy offset
        pagination. Cursor pagination takes precedence when requested.

        Args:
          direction: Sort direction for the order_by field. Valid values: `asc`, `desc`. Defaults to
              `asc` when order_by is specified.

          include_total: Whether to calculate and return the exact `result_info.total_size` for cursor
              pagination. Defaults to true. When false, `total_size` is omitted. Legacy
              `page`/`per_page` requests always calculate `total_count`.

          order_by: Field to order results by. Currently supported values: `account_name`.

          page: Legacy offset page number. Must be provided with `per_page`. Values below 1 are
              treated as

              1. Cursor pagination takes precedence when requested.

          page_size: The amount of items to return. Defaults to 10.

          page_token: An opaque token returned from the last list response that when provided will
              retrieve the next page.

              Parameters used to filter the retrieved list must remain in subsequent requests
              with a page token.

          per_page: Legacy offset page size. Must be provided with `page`. Values are clamped to the
              range 1-100. Cursor pagination takes precedence when requested.

          status: Filter accounts by lifecycle status. Defaults to `active`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return self._get_api_list(
            path_template("/tenants/{tenant_id}/accounts", tenant_id=tenant_id),
            page=AsyncV4PagePaginationArray[AccountListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_pubname": account_pubname,
                        "direction": direction,
                        "include_total": include_total,
                        "name": name,
                        "order_by": order_by,
                        "page": page,
                        "page_size": page_size,
                        "page_token": page_token,
                        "per_page": per_page,
                        "status": status,
                    },
                    account_list_params.AccountListParams,
                ),
            ),
            model=AccountListResponse,
        )


class AccountsResourceWithRawResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.list = to_raw_response_wrapper(
            accounts.list,
        )


class AsyncAccountsResourceWithRawResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.list = async_to_raw_response_wrapper(
            accounts.list,
        )


class AccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.list = to_streamed_response_wrapper(
            accounts.list,
        )


class AsyncAccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.list = async_to_streamed_response_wrapper(
            accounts.list,
        )
