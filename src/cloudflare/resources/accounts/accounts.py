# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from .roles import (
    RolesResource,
    AsyncRolesResource,
    RolesResourceWithRawResponse,
    AsyncRolesResourceWithRawResponse,
    RolesResourceWithStreamingResponse,
    AsyncRolesResourceWithStreamingResponse,
)
from .members import (
    MembersResource,
    AsyncMembersResource,
    MembersResourceWithRawResponse,
    AsyncMembersResourceWithRawResponse,
    MembersResourceWithStreamingResponse,
    AsyncMembersResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ..._base_client import AsyncPaginator, make_request_options
from ...types.accounts import account_list_params, account_update_params

__all__ = ["AccountsResource", "AsyncAccountsResource"]


class AccountsResource(SyncAPIResource):
    @cached_property
    def members(self) -> MembersResource:
        return MembersResource(self._client)

    @cached_property
    def roles(self) -> RolesResource:
        return RolesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AccountsResourceWithRawResponse:
        return AccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsResourceWithStreamingResponse:
        return AccountsResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        account_id: str,
        name: str,
        settings: account_update_params.Settings | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Update an existing account.

        Args:
          account_id: Account identifier tag.

          name: Account name

          settings: Account settings

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._put(
            f"/accounts/{account_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "settings": settings,
                },
                account_update_params.AccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def list(
        self,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[object]:
        """
        List all accounts you have ownership or verified access to.

        Args:
          direction: Direction to order results.

          name: Name of the account.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/accounts",
            page=SyncV4PagePaginationArray[object],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                    },
                    account_list_params.AccountListParams,
                ),
            ),
            model=object,
        )

    def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get information about a specific account that you are a member of.

        Args:
          account_id: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class AsyncAccountsResource(AsyncAPIResource):
    @cached_property
    def members(self) -> AsyncMembersResource:
        return AsyncMembersResource(self._client)

    @cached_property
    def roles(self) -> AsyncRolesResource:
        return AsyncRolesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAccountsResourceWithRawResponse:
        return AsyncAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsResourceWithStreamingResponse:
        return AsyncAccountsResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        account_id: str,
        name: str,
        settings: account_update_params.Settings | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Update an existing account.

        Args:
          account_id: Account identifier tag.

          name: Account name

          settings: Account settings

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._put(
            f"/accounts/{account_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "settings": settings,
                },
                account_update_params.AccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def list(
        self,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[object, AsyncV4PagePaginationArray[object]]:
        """
        List all accounts you have ownership or verified access to.

        Args:
          direction: Direction to order results.

          name: Name of the account.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/accounts",
            page=AsyncV4PagePaginationArray[object],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                    },
                    account_list_params.AccountListParams,
                ),
            ),
            model=object,
        )

    async def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get information about a specific account that you are a member of.

        Args:
          account_id: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class AccountsResourceWithRawResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.update = to_raw_response_wrapper(
            accounts.update,
        )
        self.list = to_raw_response_wrapper(
            accounts.list,
        )
        self.get = to_raw_response_wrapper(
            accounts.get,
        )

    @cached_property
    def members(self) -> MembersResourceWithRawResponse:
        return MembersResourceWithRawResponse(self._accounts.members)

    @cached_property
    def roles(self) -> RolesResourceWithRawResponse:
        return RolesResourceWithRawResponse(self._accounts.roles)


class AsyncAccountsResourceWithRawResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.update = async_to_raw_response_wrapper(
            accounts.update,
        )
        self.list = async_to_raw_response_wrapper(
            accounts.list,
        )
        self.get = async_to_raw_response_wrapper(
            accounts.get,
        )

    @cached_property
    def members(self) -> AsyncMembersResourceWithRawResponse:
        return AsyncMembersResourceWithRawResponse(self._accounts.members)

    @cached_property
    def roles(self) -> AsyncRolesResourceWithRawResponse:
        return AsyncRolesResourceWithRawResponse(self._accounts.roles)


class AccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.update = to_streamed_response_wrapper(
            accounts.update,
        )
        self.list = to_streamed_response_wrapper(
            accounts.list,
        )
        self.get = to_streamed_response_wrapper(
            accounts.get,
        )

    @cached_property
    def members(self) -> MembersResourceWithStreamingResponse:
        return MembersResourceWithStreamingResponse(self._accounts.members)

    @cached_property
    def roles(self) -> RolesResourceWithStreamingResponse:
        return RolesResourceWithStreamingResponse(self._accounts.roles)


class AsyncAccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.update = async_to_streamed_response_wrapper(
            accounts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            accounts.list,
        )
        self.get = async_to_streamed_response_wrapper(
            accounts.get,
        )

    @cached_property
    def members(self) -> AsyncMembersResourceWithStreamingResponse:
        return AsyncMembersResourceWithStreamingResponse(self._accounts.members)

    @cached_property
    def roles(self) -> AsyncRolesResourceWithStreamingResponse:
        return AsyncRolesResourceWithStreamingResponse(self._accounts.roles)
