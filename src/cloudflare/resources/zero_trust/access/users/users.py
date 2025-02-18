# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .failed_logins import (
    FailedLoginsResource,
    AsyncFailedLoginsResource,
    FailedLoginsResourceWithRawResponse,
    AsyncFailedLoginsResourceWithRawResponse,
    FailedLoginsResourceWithStreamingResponse,
    AsyncFailedLoginsResourceWithStreamingResponse,
)
from .....pagination import SyncSinglePage, AsyncSinglePage
from .active_sessions import (
    ActiveSessionsResource,
    AsyncActiveSessionsResource,
    ActiveSessionsResourceWithRawResponse,
    AsyncActiveSessionsResourceWithRawResponse,
    ActiveSessionsResourceWithStreamingResponse,
    AsyncActiveSessionsResourceWithStreamingResponse,
)
from ....._base_client import AsyncPaginator, make_request_options
from .last_seen_identity import (
    LastSeenIdentityResource,
    AsyncLastSeenIdentityResource,
    LastSeenIdentityResourceWithRawResponse,
    AsyncLastSeenIdentityResourceWithRawResponse,
    LastSeenIdentityResourceWithStreamingResponse,
    AsyncLastSeenIdentityResourceWithStreamingResponse,
)
from .....types.zero_trust.access import user_list_params
from .....types.zero_trust.access.user_list_response import UserListResponse

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def active_sessions(self) -> ActiveSessionsResource:
        return ActiveSessionsResource(self._client)

    @cached_property
    def last_seen_identity(self) -> LastSeenIdentityResource:
        return LastSeenIdentityResource(self._client)

    @cached_property
    def failed_logins(self) -> FailedLoginsResource:
        return FailedLoginsResource(self._client)

    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        email: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[UserListResponse]:
        """
        Gets a list of users for an account.

        Args:
          account_id: Identifier

          email: The email of the user.

          name: The name of the user.

          search: Search for users by other listed query parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/access/users",
            page=SyncSinglePage[UserListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "email": email,
                        "name": name,
                        "search": search,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            model=UserListResponse,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def active_sessions(self) -> AsyncActiveSessionsResource:
        return AsyncActiveSessionsResource(self._client)

    @cached_property
    def last_seen_identity(self) -> AsyncLastSeenIdentityResource:
        return AsyncLastSeenIdentityResource(self._client)

    @cached_property
    def failed_logins(self) -> AsyncFailedLoginsResource:
        return AsyncFailedLoginsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        email: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[UserListResponse, AsyncSinglePage[UserListResponse]]:
        """
        Gets a list of users for an account.

        Args:
          account_id: Identifier

          email: The email of the user.

          name: The name of the user.

          search: Search for users by other listed query parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/access/users",
            page=AsyncSinglePage[UserListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "email": email,
                        "name": name,
                        "search": search,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            model=UserListResponse,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.list = to_raw_response_wrapper(
            users.list,
        )

    @cached_property
    def active_sessions(self) -> ActiveSessionsResourceWithRawResponse:
        return ActiveSessionsResourceWithRawResponse(self._users.active_sessions)

    @cached_property
    def last_seen_identity(self) -> LastSeenIdentityResourceWithRawResponse:
        return LastSeenIdentityResourceWithRawResponse(self._users.last_seen_identity)

    @cached_property
    def failed_logins(self) -> FailedLoginsResourceWithRawResponse:
        return FailedLoginsResourceWithRawResponse(self._users.failed_logins)


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.list = async_to_raw_response_wrapper(
            users.list,
        )

    @cached_property
    def active_sessions(self) -> AsyncActiveSessionsResourceWithRawResponse:
        return AsyncActiveSessionsResourceWithRawResponse(self._users.active_sessions)

    @cached_property
    def last_seen_identity(self) -> AsyncLastSeenIdentityResourceWithRawResponse:
        return AsyncLastSeenIdentityResourceWithRawResponse(self._users.last_seen_identity)

    @cached_property
    def failed_logins(self) -> AsyncFailedLoginsResourceWithRawResponse:
        return AsyncFailedLoginsResourceWithRawResponse(self._users.failed_logins)


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.list = to_streamed_response_wrapper(
            users.list,
        )

    @cached_property
    def active_sessions(self) -> ActiveSessionsResourceWithStreamingResponse:
        return ActiveSessionsResourceWithStreamingResponse(self._users.active_sessions)

    @cached_property
    def last_seen_identity(self) -> LastSeenIdentityResourceWithStreamingResponse:
        return LastSeenIdentityResourceWithStreamingResponse(self._users.last_seen_identity)

    @cached_property
    def failed_logins(self) -> FailedLoginsResourceWithStreamingResponse:
        return FailedLoginsResourceWithStreamingResponse(self._users.failed_logins)


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.list = async_to_streamed_response_wrapper(
            users.list,
        )

    @cached_property
    def active_sessions(self) -> AsyncActiveSessionsResourceWithStreamingResponse:
        return AsyncActiveSessionsResourceWithStreamingResponse(self._users.active_sessions)

    @cached_property
    def last_seen_identity(self) -> AsyncLastSeenIdentityResourceWithStreamingResponse:
        return AsyncLastSeenIdentityResourceWithStreamingResponse(self._users.last_seen_identity)

    @cached_property
    def failed_logins(self) -> AsyncFailedLoginsResourceWithStreamingResponse:
        return AsyncFailedLoginsResourceWithStreamingResponse(self._users.failed_logins)
