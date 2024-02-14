# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .audit_logs import AuditLogs, AsyncAuditLogs

from ..._compat import cached_property

from .billings.billings import Billings, AsyncBillings

from .firewalls.firewalls import Firewalls, AsyncFirewalls

from .invites import Invites, AsyncInvites

from .load_balancers.load_balancers import LoadBalancers, AsyncLoadBalancers

from .load_balancing_analytics.load_balancing_analytics import LoadBalancingAnalytics, AsyncLoadBalancingAnalytics

from .organizations import Organizations, AsyncOrganizations

from .subscriptions import Subscriptions, AsyncSubscriptions

from .tokens.tokens import Tokens, AsyncTokens

from ...types import UserUserEditUserResponse, UserUserUserDetailsResponse

from typing import Optional

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types import user_user_edit_user_params
from .audit_logs import (
    AuditLogs,
    AsyncAuditLogs,
    AuditLogsWithRawResponse,
    AsyncAuditLogsWithRawResponse,
    AuditLogsWithStreamingResponse,
    AsyncAuditLogsWithStreamingResponse,
)
from .billings import (
    Billings,
    AsyncBillings,
    BillingsWithRawResponse,
    AsyncBillingsWithRawResponse,
    BillingsWithStreamingResponse,
    AsyncBillingsWithStreamingResponse,
)
from .firewalls import (
    Firewalls,
    AsyncFirewalls,
    FirewallsWithRawResponse,
    AsyncFirewallsWithRawResponse,
    FirewallsWithStreamingResponse,
    AsyncFirewallsWithStreamingResponse,
)
from .invites import (
    Invites,
    AsyncInvites,
    InvitesWithRawResponse,
    AsyncInvitesWithRawResponse,
    InvitesWithStreamingResponse,
    AsyncInvitesWithStreamingResponse,
)
from .load_balancers import (
    LoadBalancers,
    AsyncLoadBalancers,
    LoadBalancersWithRawResponse,
    AsyncLoadBalancersWithRawResponse,
    LoadBalancersWithStreamingResponse,
    AsyncLoadBalancersWithStreamingResponse,
)
from .load_balancing_analytics import (
    LoadBalancingAnalytics,
    AsyncLoadBalancingAnalytics,
    LoadBalancingAnalyticsWithRawResponse,
    AsyncLoadBalancingAnalyticsWithRawResponse,
    LoadBalancingAnalyticsWithStreamingResponse,
    AsyncLoadBalancingAnalyticsWithStreamingResponse,
)
from .organizations import (
    Organizations,
    AsyncOrganizations,
    OrganizationsWithRawResponse,
    AsyncOrganizationsWithRawResponse,
    OrganizationsWithStreamingResponse,
    AsyncOrganizationsWithStreamingResponse,
)
from .subscriptions import (
    Subscriptions,
    AsyncSubscriptions,
    SubscriptionsWithRawResponse,
    AsyncSubscriptionsWithRawResponse,
    SubscriptionsWithStreamingResponse,
    AsyncSubscriptionsWithStreamingResponse,
)
from .tokens import (
    Tokens,
    AsyncTokens,
    TokensWithRawResponse,
    AsyncTokensWithRawResponse,
    TokensWithStreamingResponse,
    AsyncTokensWithStreamingResponse,
)
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Users", "AsyncUsers"]


class Users(SyncAPIResource):
    @cached_property
    def audit_logs(self) -> AuditLogs:
        return AuditLogs(self._client)

    @cached_property
    def billings(self) -> Billings:
        return Billings(self._client)

    @cached_property
    def firewalls(self) -> Firewalls:
        return Firewalls(self._client)

    @cached_property
    def invites(self) -> Invites:
        return Invites(self._client)

    @cached_property
    def load_balancers(self) -> LoadBalancers:
        return LoadBalancers(self._client)

    @cached_property
    def load_balancing_analytics(self) -> LoadBalancingAnalytics:
        return LoadBalancingAnalytics(self._client)

    @cached_property
    def organizations(self) -> Organizations:
        return Organizations(self._client)

    @cached_property
    def subscriptions(self) -> Subscriptions:
        return Subscriptions(self._client)

    @cached_property
    def tokens(self) -> Tokens:
        return Tokens(self._client)

    @cached_property
    def with_raw_response(self) -> UsersWithRawResponse:
        return UsersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersWithStreamingResponse:
        return UsersWithStreamingResponse(self)

    def user_edit_user(
        self,
        *,
        country: Optional[str] | NotGiven = NOT_GIVEN,
        first_name: Optional[str] | NotGiven = NOT_GIVEN,
        last_name: Optional[str] | NotGiven = NOT_GIVEN,
        telephone: Optional[str] | NotGiven = NOT_GIVEN,
        zipcode: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserUserEditUserResponse:
        """
        Edit part of your user details.

        Args:
          country: The country in which the user lives.

          first_name: User's first name

          last_name: User's last name

          telephone: User's telephone number

          zipcode: The zipcode or postal code where the user lives.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            UserUserEditUserResponse,
            self._patch(
                "/user",
                body=maybe_transform(
                    {
                        "country": country,
                        "first_name": first_name,
                        "last_name": last_name,
                        "telephone": telephone,
                        "zipcode": zipcode,
                    },
                    user_user_edit_user_params.UserUserEditUserParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[UserUserEditUserResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def user_user_details(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserUserUserDetailsResponse:
        """User Details"""
        return cast(
            UserUserUserDetailsResponse,
            self._get(
                "/user",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[UserUserUserDetailsResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncUsers(AsyncAPIResource):
    @cached_property
    def audit_logs(self) -> AsyncAuditLogs:
        return AsyncAuditLogs(self._client)

    @cached_property
    def billings(self) -> AsyncBillings:
        return AsyncBillings(self._client)

    @cached_property
    def firewalls(self) -> AsyncFirewalls:
        return AsyncFirewalls(self._client)

    @cached_property
    def invites(self) -> AsyncInvites:
        return AsyncInvites(self._client)

    @cached_property
    def load_balancers(self) -> AsyncLoadBalancers:
        return AsyncLoadBalancers(self._client)

    @cached_property
    def load_balancing_analytics(self) -> AsyncLoadBalancingAnalytics:
        return AsyncLoadBalancingAnalytics(self._client)

    @cached_property
    def organizations(self) -> AsyncOrganizations:
        return AsyncOrganizations(self._client)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptions:
        return AsyncSubscriptions(self._client)

    @cached_property
    def tokens(self) -> AsyncTokens:
        return AsyncTokens(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUsersWithRawResponse:
        return AsyncUsersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersWithStreamingResponse:
        return AsyncUsersWithStreamingResponse(self)

    async def user_edit_user(
        self,
        *,
        country: Optional[str] | NotGiven = NOT_GIVEN,
        first_name: Optional[str] | NotGiven = NOT_GIVEN,
        last_name: Optional[str] | NotGiven = NOT_GIVEN,
        telephone: Optional[str] | NotGiven = NOT_GIVEN,
        zipcode: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserUserEditUserResponse:
        """
        Edit part of your user details.

        Args:
          country: The country in which the user lives.

          first_name: User's first name

          last_name: User's last name

          telephone: User's telephone number

          zipcode: The zipcode or postal code where the user lives.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            UserUserEditUserResponse,
            await self._patch(
                "/user",
                body=maybe_transform(
                    {
                        "country": country,
                        "first_name": first_name,
                        "last_name": last_name,
                        "telephone": telephone,
                        "zipcode": zipcode,
                    },
                    user_user_edit_user_params.UserUserEditUserParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[UserUserEditUserResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def user_user_details(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserUserUserDetailsResponse:
        """User Details"""
        return cast(
            UserUserUserDetailsResponse,
            await self._get(
                "/user",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[UserUserUserDetailsResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class UsersWithRawResponse:
    def __init__(self, users: Users) -> None:
        self._users = users

        self.user_edit_user = to_raw_response_wrapper(
            users.user_edit_user,
        )
        self.user_user_details = to_raw_response_wrapper(
            users.user_user_details,
        )

    @cached_property
    def audit_logs(self) -> AuditLogsWithRawResponse:
        return AuditLogsWithRawResponse(self._users.audit_logs)

    @cached_property
    def billings(self) -> BillingsWithRawResponse:
        return BillingsWithRawResponse(self._users.billings)

    @cached_property
    def firewalls(self) -> FirewallsWithRawResponse:
        return FirewallsWithRawResponse(self._users.firewalls)

    @cached_property
    def invites(self) -> InvitesWithRawResponse:
        return InvitesWithRawResponse(self._users.invites)

    @cached_property
    def load_balancers(self) -> LoadBalancersWithRawResponse:
        return LoadBalancersWithRawResponse(self._users.load_balancers)

    @cached_property
    def load_balancing_analytics(self) -> LoadBalancingAnalyticsWithRawResponse:
        return LoadBalancingAnalyticsWithRawResponse(self._users.load_balancing_analytics)

    @cached_property
    def organizations(self) -> OrganizationsWithRawResponse:
        return OrganizationsWithRawResponse(self._users.organizations)

    @cached_property
    def subscriptions(self) -> SubscriptionsWithRawResponse:
        return SubscriptionsWithRawResponse(self._users.subscriptions)

    @cached_property
    def tokens(self) -> TokensWithRawResponse:
        return TokensWithRawResponse(self._users.tokens)


class AsyncUsersWithRawResponse:
    def __init__(self, users: AsyncUsers) -> None:
        self._users = users

        self.user_edit_user = async_to_raw_response_wrapper(
            users.user_edit_user,
        )
        self.user_user_details = async_to_raw_response_wrapper(
            users.user_user_details,
        )

    @cached_property
    def audit_logs(self) -> AsyncAuditLogsWithRawResponse:
        return AsyncAuditLogsWithRawResponse(self._users.audit_logs)

    @cached_property
    def billings(self) -> AsyncBillingsWithRawResponse:
        return AsyncBillingsWithRawResponse(self._users.billings)

    @cached_property
    def firewalls(self) -> AsyncFirewallsWithRawResponse:
        return AsyncFirewallsWithRawResponse(self._users.firewalls)

    @cached_property
    def invites(self) -> AsyncInvitesWithRawResponse:
        return AsyncInvitesWithRawResponse(self._users.invites)

    @cached_property
    def load_balancers(self) -> AsyncLoadBalancersWithRawResponse:
        return AsyncLoadBalancersWithRawResponse(self._users.load_balancers)

    @cached_property
    def load_balancing_analytics(self) -> AsyncLoadBalancingAnalyticsWithRawResponse:
        return AsyncLoadBalancingAnalyticsWithRawResponse(self._users.load_balancing_analytics)

    @cached_property
    def organizations(self) -> AsyncOrganizationsWithRawResponse:
        return AsyncOrganizationsWithRawResponse(self._users.organizations)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsWithRawResponse:
        return AsyncSubscriptionsWithRawResponse(self._users.subscriptions)

    @cached_property
    def tokens(self) -> AsyncTokensWithRawResponse:
        return AsyncTokensWithRawResponse(self._users.tokens)


class UsersWithStreamingResponse:
    def __init__(self, users: Users) -> None:
        self._users = users

        self.user_edit_user = to_streamed_response_wrapper(
            users.user_edit_user,
        )
        self.user_user_details = to_streamed_response_wrapper(
            users.user_user_details,
        )

    @cached_property
    def audit_logs(self) -> AuditLogsWithStreamingResponse:
        return AuditLogsWithStreamingResponse(self._users.audit_logs)

    @cached_property
    def billings(self) -> BillingsWithStreamingResponse:
        return BillingsWithStreamingResponse(self._users.billings)

    @cached_property
    def firewalls(self) -> FirewallsWithStreamingResponse:
        return FirewallsWithStreamingResponse(self._users.firewalls)

    @cached_property
    def invites(self) -> InvitesWithStreamingResponse:
        return InvitesWithStreamingResponse(self._users.invites)

    @cached_property
    def load_balancers(self) -> LoadBalancersWithStreamingResponse:
        return LoadBalancersWithStreamingResponse(self._users.load_balancers)

    @cached_property
    def load_balancing_analytics(self) -> LoadBalancingAnalyticsWithStreamingResponse:
        return LoadBalancingAnalyticsWithStreamingResponse(self._users.load_balancing_analytics)

    @cached_property
    def organizations(self) -> OrganizationsWithStreamingResponse:
        return OrganizationsWithStreamingResponse(self._users.organizations)

    @cached_property
    def subscriptions(self) -> SubscriptionsWithStreamingResponse:
        return SubscriptionsWithStreamingResponse(self._users.subscriptions)

    @cached_property
    def tokens(self) -> TokensWithStreamingResponse:
        return TokensWithStreamingResponse(self._users.tokens)


class AsyncUsersWithStreamingResponse:
    def __init__(self, users: AsyncUsers) -> None:
        self._users = users

        self.user_edit_user = async_to_streamed_response_wrapper(
            users.user_edit_user,
        )
        self.user_user_details = async_to_streamed_response_wrapper(
            users.user_user_details,
        )

    @cached_property
    def audit_logs(self) -> AsyncAuditLogsWithStreamingResponse:
        return AsyncAuditLogsWithStreamingResponse(self._users.audit_logs)

    @cached_property
    def billings(self) -> AsyncBillingsWithStreamingResponse:
        return AsyncBillingsWithStreamingResponse(self._users.billings)

    @cached_property
    def firewalls(self) -> AsyncFirewallsWithStreamingResponse:
        return AsyncFirewallsWithStreamingResponse(self._users.firewalls)

    @cached_property
    def invites(self) -> AsyncInvitesWithStreamingResponse:
        return AsyncInvitesWithStreamingResponse(self._users.invites)

    @cached_property
    def load_balancers(self) -> AsyncLoadBalancersWithStreamingResponse:
        return AsyncLoadBalancersWithStreamingResponse(self._users.load_balancers)

    @cached_property
    def load_balancing_analytics(self) -> AsyncLoadBalancingAnalyticsWithStreamingResponse:
        return AsyncLoadBalancingAnalyticsWithStreamingResponse(self._users.load_balancing_analytics)

    @cached_property
    def organizations(self) -> AsyncOrganizationsWithStreamingResponse:
        return AsyncOrganizationsWithStreamingResponse(self._users.organizations)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsWithStreamingResponse:
        return AsyncSubscriptionsWithStreamingResponse(self._users.subscriptions)

    @cached_property
    def tokens(self) -> AsyncTokensWithStreamingResponse:
        return AsyncTokensWithStreamingResponse(self._users.tokens)
