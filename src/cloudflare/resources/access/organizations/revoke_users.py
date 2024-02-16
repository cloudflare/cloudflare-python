# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

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
from ....types.access.organizations import (
    RevokeUserZeroTrustOrganizationRevokeAllAccessTokensForAUserResponse,
    revoke_user_zero_trust_organization_revoke_all_access_tokens_for_a_user_params,
)

__all__ = ["RevokeUsers", "AsyncRevokeUsers"]


class RevokeUsers(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RevokeUsersWithRawResponse:
        return RevokeUsersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RevokeUsersWithStreamingResponse:
        return RevokeUsersWithStreamingResponse(self)

    def zero_trust_organization_revoke_all_access_tokens_for_a_user(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RevokeUserZeroTrustOrganizationRevokeAllAccessTokensForAUserResponse]:
        """
        Revokes a user's access across all applications.

        Args:
          account_or_zone_id: Identifier

          email: The email of the user to revoke.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return self._post(
            f"/{account_or_zone}/{account_or_zone_id}/access/organizations/revoke_user",
            body=maybe_transform(
                {"email": email},
                revoke_user_zero_trust_organization_revoke_all_access_tokens_for_a_user_params.RevokeUserZeroTrustOrganizationRevokeAllAccessTokensForAUserParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RevokeUserZeroTrustOrganizationRevokeAllAccessTokensForAUserResponse]],
                ResultWrapper[RevokeUserZeroTrustOrganizationRevokeAllAccessTokensForAUserResponse],
            ),
        )


class AsyncRevokeUsers(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRevokeUsersWithRawResponse:
        return AsyncRevokeUsersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRevokeUsersWithStreamingResponse:
        return AsyncRevokeUsersWithStreamingResponse(self)

    async def zero_trust_organization_revoke_all_access_tokens_for_a_user(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RevokeUserZeroTrustOrganizationRevokeAllAccessTokensForAUserResponse]:
        """
        Revokes a user's access across all applications.

        Args:
          account_or_zone_id: Identifier

          email: The email of the user to revoke.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return await self._post(
            f"/{account_or_zone}/{account_or_zone_id}/access/organizations/revoke_user",
            body=maybe_transform(
                {"email": email},
                revoke_user_zero_trust_organization_revoke_all_access_tokens_for_a_user_params.RevokeUserZeroTrustOrganizationRevokeAllAccessTokensForAUserParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RevokeUserZeroTrustOrganizationRevokeAllAccessTokensForAUserResponse]],
                ResultWrapper[RevokeUserZeroTrustOrganizationRevokeAllAccessTokensForAUserResponse],
            ),
        )


class RevokeUsersWithRawResponse:
    def __init__(self, revoke_users: RevokeUsers) -> None:
        self._revoke_users = revoke_users

        self.zero_trust_organization_revoke_all_access_tokens_for_a_user = to_raw_response_wrapper(
            revoke_users.zero_trust_organization_revoke_all_access_tokens_for_a_user,
        )


class AsyncRevokeUsersWithRawResponse:
    def __init__(self, revoke_users: AsyncRevokeUsers) -> None:
        self._revoke_users = revoke_users

        self.zero_trust_organization_revoke_all_access_tokens_for_a_user = async_to_raw_response_wrapper(
            revoke_users.zero_trust_organization_revoke_all_access_tokens_for_a_user,
        )


class RevokeUsersWithStreamingResponse:
    def __init__(self, revoke_users: RevokeUsers) -> None:
        self._revoke_users = revoke_users

        self.zero_trust_organization_revoke_all_access_tokens_for_a_user = to_streamed_response_wrapper(
            revoke_users.zero_trust_organization_revoke_all_access_tokens_for_a_user,
        )


class AsyncRevokeUsersWithStreamingResponse:
    def __init__(self, revoke_users: AsyncRevokeUsers) -> None:
        self._revoke_users = revoke_users

        self.zero_trust_organization_revoke_all_access_tokens_for_a_user = async_to_streamed_response_wrapper(
            revoke_users.zero_trust_organization_revoke_all_access_tokens_for_a_user,
        )
