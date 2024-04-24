# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ....._base_client import (
    AsyncPaginator,
    make_request_options,
)
from .last_seen_identity import (
    LastSeenIdentityResource,
    AsyncLastSeenIdentityResource,
    LastSeenIdentityResourceWithRawResponse,
    AsyncLastSeenIdentityResourceWithRawResponse,
    LastSeenIdentityResourceWithStreamingResponse,
    AsyncLastSeenIdentityResourceWithStreamingResponse,
)
from .....types.zero_trust.access.access_user import AccessUser

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
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self)

    def list(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[AccessUser]:
        """
        Gets a list of users for an account.

        Args:
          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._get_api_list(
            f"/accounts/{identifier}/access/users",
            page=SyncSinglePage[AccessUser],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=AccessUser,
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
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self)

    def list(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[AccessUser, AsyncSinglePage[AccessUser]]:
        """
        Gets a list of users for an account.

        Args:
          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._get_api_list(
            f"/accounts/{identifier}/access/users",
            page=AsyncSinglePage[AccessUser],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=AccessUser,
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
