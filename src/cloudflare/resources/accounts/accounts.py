# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import Literal

import httpx

from .roles import (
    Roles,
    AsyncRoles,
    RolesWithRawResponse,
    AsyncRolesWithRawResponse,
    RolesWithStreamingResponse,
    AsyncRolesWithStreamingResponse,
)
from ...types import (
    AccountGetResponse,
    AccountUpdateResponse,
    account_list_params,
    account_update_params,
)
from .members import (
    Members,
    AsyncMembers,
    MembersWithRawResponse,
    AsyncMembersWithRawResponse,
    MembersWithStreamingResponse,
    AsyncMembersWithStreamingResponse,
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
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)

__all__ = ["Accounts", "AsyncAccounts"]


class Accounts(SyncAPIResource):
    @cached_property
    def members(self) -> Members:
        return Members(self._client)

    @cached_property
    def roles(self) -> Roles:
        return Roles(self._client)

    @cached_property
    def with_raw_response(self) -> AccountsWithRawResponse:
        return AccountsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsWithStreamingResponse:
        return AccountsWithStreamingResponse(self)

    def update(
        self,
        *,
        account_id: object,
        name: str,
        settings: account_update_params.Settings | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountUpdateResponse:
        """
        Update an existing account.

        Args:
          name: Account name

          settings: Account settings

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            AccountUpdateResponse,
            self._put(
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
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AccountUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
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
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountGetResponse:
        """
        Get information about a specific account that you are a member of.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            AccountGetResponse,
            self._get(
                f"/accounts/{account_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AccountGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncAccounts(AsyncAPIResource):
    @cached_property
    def members(self) -> AsyncMembers:
        return AsyncMembers(self._client)

    @cached_property
    def roles(self) -> AsyncRoles:
        return AsyncRoles(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAccountsWithRawResponse:
        return AsyncAccountsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsWithStreamingResponse:
        return AsyncAccountsWithStreamingResponse(self)

    async def update(
        self,
        *,
        account_id: object,
        name: str,
        settings: account_update_params.Settings | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountUpdateResponse:
        """
        Update an existing account.

        Args:
          name: Account name

          settings: Account settings

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            AccountUpdateResponse,
            await self._put(
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
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AccountUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
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
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountGetResponse:
        """
        Get information about a specific account that you are a member of.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            AccountGetResponse,
            await self._get(
                f"/accounts/{account_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AccountGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AccountsWithRawResponse:
    def __init__(self, accounts: Accounts) -> None:
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
    def members(self) -> MembersWithRawResponse:
        return MembersWithRawResponse(self._accounts.members)

    @cached_property
    def roles(self) -> RolesWithRawResponse:
        return RolesWithRawResponse(self._accounts.roles)


class AsyncAccountsWithRawResponse:
    def __init__(self, accounts: AsyncAccounts) -> None:
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
    def members(self) -> AsyncMembersWithRawResponse:
        return AsyncMembersWithRawResponse(self._accounts.members)

    @cached_property
    def roles(self) -> AsyncRolesWithRawResponse:
        return AsyncRolesWithRawResponse(self._accounts.roles)


class AccountsWithStreamingResponse:
    def __init__(self, accounts: Accounts) -> None:
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
    def members(self) -> MembersWithStreamingResponse:
        return MembersWithStreamingResponse(self._accounts.members)

    @cached_property
    def roles(self) -> RolesWithStreamingResponse:
        return RolesWithStreamingResponse(self._accounts.roles)


class AsyncAccountsWithStreamingResponse:
    def __init__(self, accounts: AsyncAccounts) -> None:
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
    def members(self) -> AsyncMembersWithStreamingResponse:
        return AsyncMembersWithStreamingResponse(self._accounts.members)

    @cached_property
    def roles(self) -> AsyncRolesWithStreamingResponse:
        return AsyncRolesWithStreamingResponse(self._accounts.roles)
