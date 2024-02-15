# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .active_sessions import ActiveSessions, AsyncActiveSessions

from ...._compat import cached_property

from .last_seen_identity import LastSeenIdentity, AsyncLastSeenIdentity

from .failed_logins import FailedLogins, AsyncFailedLogins

from ....types.access import UserListResponse

from typing import Type, Optional

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from .active_sessions import (
    ActiveSessions,
    AsyncActiveSessions,
    ActiveSessionsWithRawResponse,
    AsyncActiveSessionsWithRawResponse,
    ActiveSessionsWithStreamingResponse,
    AsyncActiveSessionsWithStreamingResponse,
)
from .last_seen_identity import (
    LastSeenIdentity,
    AsyncLastSeenIdentity,
    LastSeenIdentityWithRawResponse,
    AsyncLastSeenIdentityWithRawResponse,
    LastSeenIdentityWithStreamingResponse,
    AsyncLastSeenIdentityWithStreamingResponse,
)
from .failed_logins import (
    FailedLogins,
    AsyncFailedLogins,
    FailedLoginsWithRawResponse,
    AsyncFailedLoginsWithRawResponse,
    FailedLoginsWithStreamingResponse,
    AsyncFailedLoginsWithStreamingResponse,
)
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Users", "AsyncUsers"]


class Users(SyncAPIResource):
    @cached_property
    def active_sessions(self) -> ActiveSessions:
        return ActiveSessions(self._client)

    @cached_property
    def last_seen_identity(self) -> LastSeenIdentity:
        return LastSeenIdentity(self._client)

    @cached_property
    def failed_logins(self) -> FailedLogins:
        return FailedLogins(self._client)

    @cached_property
    def with_raw_response(self) -> UsersWithRawResponse:
        return UsersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersWithStreamingResponse:
        return UsersWithStreamingResponse(self)

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
    ) -> Optional[UserListResponse]:
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
        return self._get(
            f"/accounts/{identifier}/access/users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[UserListResponse]], ResultWrapper[UserListResponse]),
        )


class AsyncUsers(AsyncAPIResource):
    @cached_property
    def active_sessions(self) -> AsyncActiveSessions:
        return AsyncActiveSessions(self._client)

    @cached_property
    def last_seen_identity(self) -> AsyncLastSeenIdentity:
        return AsyncLastSeenIdentity(self._client)

    @cached_property
    def failed_logins(self) -> AsyncFailedLogins:
        return AsyncFailedLogins(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUsersWithRawResponse:
        return AsyncUsersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersWithStreamingResponse:
        return AsyncUsersWithStreamingResponse(self)

    async def list(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[UserListResponse]:
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
        return await self._get(
            f"/accounts/{identifier}/access/users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[UserListResponse]], ResultWrapper[UserListResponse]),
        )


class UsersWithRawResponse:
    def __init__(self, users: Users) -> None:
        self._users = users

        self.list = to_raw_response_wrapper(
            users.list,
        )

    @cached_property
    def active_sessions(self) -> ActiveSessionsWithRawResponse:
        return ActiveSessionsWithRawResponse(self._users.active_sessions)

    @cached_property
    def last_seen_identity(self) -> LastSeenIdentityWithRawResponse:
        return LastSeenIdentityWithRawResponse(self._users.last_seen_identity)

    @cached_property
    def failed_logins(self) -> FailedLoginsWithRawResponse:
        return FailedLoginsWithRawResponse(self._users.failed_logins)


class AsyncUsersWithRawResponse:
    def __init__(self, users: AsyncUsers) -> None:
        self._users = users

        self.list = async_to_raw_response_wrapper(
            users.list,
        )

    @cached_property
    def active_sessions(self) -> AsyncActiveSessionsWithRawResponse:
        return AsyncActiveSessionsWithRawResponse(self._users.active_sessions)

    @cached_property
    def last_seen_identity(self) -> AsyncLastSeenIdentityWithRawResponse:
        return AsyncLastSeenIdentityWithRawResponse(self._users.last_seen_identity)

    @cached_property
    def failed_logins(self) -> AsyncFailedLoginsWithRawResponse:
        return AsyncFailedLoginsWithRawResponse(self._users.failed_logins)


class UsersWithStreamingResponse:
    def __init__(self, users: Users) -> None:
        self._users = users

        self.list = to_streamed_response_wrapper(
            users.list,
        )

    @cached_property
    def active_sessions(self) -> ActiveSessionsWithStreamingResponse:
        return ActiveSessionsWithStreamingResponse(self._users.active_sessions)

    @cached_property
    def last_seen_identity(self) -> LastSeenIdentityWithStreamingResponse:
        return LastSeenIdentityWithStreamingResponse(self._users.last_seen_identity)

    @cached_property
    def failed_logins(self) -> FailedLoginsWithStreamingResponse:
        return FailedLoginsWithStreamingResponse(self._users.failed_logins)


class AsyncUsersWithStreamingResponse:
    def __init__(self, users: AsyncUsers) -> None:
        self._users = users

        self.list = async_to_streamed_response_wrapper(
            users.list,
        )

    @cached_property
    def active_sessions(self) -> AsyncActiveSessionsWithStreamingResponse:
        return AsyncActiveSessionsWithStreamingResponse(self._users.active_sessions)

    @cached_property
    def last_seen_identity(self) -> AsyncLastSeenIdentityWithStreamingResponse:
        return AsyncLastSeenIdentityWithStreamingResponse(self._users.last_seen_identity)

    @cached_property
    def failed_logins(self) -> AsyncFailedLoginsWithStreamingResponse:
        return AsyncFailedLoginsWithStreamingResponse(self._users.failed_logins)
