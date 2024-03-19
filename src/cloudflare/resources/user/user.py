# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast

import httpx

from .tokens import (
    Tokens,
    AsyncTokens,
    TokensWithRawResponse,
    AsyncTokensWithRawResponse,
    TokensWithStreamingResponse,
    AsyncTokensWithStreamingResponse,
)
from ...types import UserGetResponse, UserEditResponse, user_edit_params
from .billing import (
    Billing,
    AsyncBilling,
    BillingWithRawResponse,
    AsyncBillingWithRawResponse,
    BillingWithStreamingResponse,
    AsyncBillingWithStreamingResponse,
)
from .invites import (
    Invites,
    AsyncInvites,
    InvitesWithRawResponse,
    AsyncInvitesWithRawResponse,
    InvitesWithStreamingResponse,
    AsyncInvitesWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .firewall import (
    Firewall,
    AsyncFirewall,
    FirewallWithRawResponse,
    AsyncFirewallWithRawResponse,
    FirewallWithStreamingResponse,
    AsyncFirewallWithStreamingResponse,
)
from ..._compat import cached_property
from .audit_logs import (
    AuditLogs,
    AsyncAuditLogs,
    AuditLogsWithRawResponse,
    AsyncAuditLogsWithRawResponse,
    AuditLogsWithStreamingResponse,
    AsyncAuditLogsWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
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
from .tokens.tokens import Tokens, AsyncTokens
from ..._base_client import (
    make_request_options,
)
from .load_balancers import (
    LoadBalancers,
    AsyncLoadBalancers,
    LoadBalancersWithRawResponse,
    AsyncLoadBalancersWithRawResponse,
    LoadBalancersWithStreamingResponse,
    AsyncLoadBalancersWithStreamingResponse,
)
from .billing.billing import Billing, AsyncBilling
from .firewall.firewall import Firewall, AsyncFirewall
from .load_balancers.load_balancers import LoadBalancers, AsyncLoadBalancers

__all__ = ["UserResource", "AsyncUserResource"]


class UserResource(SyncAPIResource):
    @cached_property
    def audit_logs(self) -> AuditLogs:
        return AuditLogs(self._client)

    @cached_property
    def billing(self) -> Billing:
        return Billing(self._client)

    @cached_property
    def firewall(self) -> Firewall:
        return Firewall(self._client)

    @cached_property
    def invites(self) -> Invites:
        return Invites(self._client)

    @cached_property
    def load_balancers(self) -> LoadBalancers:
        return LoadBalancers(self._client)

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
    def with_raw_response(self) -> UserResourceWithRawResponse:
        return UserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserResourceWithStreamingResponse:
        return UserResourceWithStreamingResponse(self)

    def edit(
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
    ) -> UserEditResponse:
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
            UserEditResponse,
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
                    user_edit_params.UserEditParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[UserEditResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserGetResponse:
        """User Details"""
        return cast(
            UserGetResponse,
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
                    Any, ResultWrapper[UserGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncUserResource(AsyncAPIResource):
    @cached_property
    def audit_logs(self) -> AsyncAuditLogs:
        return AsyncAuditLogs(self._client)

    @cached_property
    def billing(self) -> AsyncBilling:
        return AsyncBilling(self._client)

    @cached_property
    def firewall(self) -> AsyncFirewall:
        return AsyncFirewall(self._client)

    @cached_property
    def invites(self) -> AsyncInvites:
        return AsyncInvites(self._client)

    @cached_property
    def load_balancers(self) -> AsyncLoadBalancers:
        return AsyncLoadBalancers(self._client)

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
    def with_raw_response(self) -> AsyncUserResourceWithRawResponse:
        return AsyncUserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserResourceWithStreamingResponse:
        return AsyncUserResourceWithStreamingResponse(self)

    async def edit(
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
    ) -> UserEditResponse:
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
            UserEditResponse,
            await self._patch(
                "/user",
                body=await async_maybe_transform(
                    {
                        "country": country,
                        "first_name": first_name,
                        "last_name": last_name,
                        "telephone": telephone,
                        "zipcode": zipcode,
                    },
                    user_edit_params.UserEditParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[UserEditResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserGetResponse:
        """User Details"""
        return cast(
            UserGetResponse,
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
                    Any, ResultWrapper[UserGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class UserResourceWithRawResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.edit = to_raw_response_wrapper(
            user.edit,
        )
        self.get = to_raw_response_wrapper(
            user.get,
        )

    @cached_property
    def audit_logs(self) -> AuditLogsWithRawResponse:
        return AuditLogsWithRawResponse(self._user.audit_logs)

    @cached_property
    def billing(self) -> BillingWithRawResponse:
        return BillingWithRawResponse(self._user.billing)

    @cached_property
    def firewall(self) -> FirewallWithRawResponse:
        return FirewallWithRawResponse(self._user.firewall)

    @cached_property
    def invites(self) -> InvitesWithRawResponse:
        return InvitesWithRawResponse(self._user.invites)

    @cached_property
    def load_balancers(self) -> LoadBalancersWithRawResponse:
        return LoadBalancersWithRawResponse(self._user.load_balancers)

    @cached_property
    def organizations(self) -> OrganizationsWithRawResponse:
        return OrganizationsWithRawResponse(self._user.organizations)

    @cached_property
    def subscriptions(self) -> SubscriptionsWithRawResponse:
        return SubscriptionsWithRawResponse(self._user.subscriptions)

    @cached_property
    def tokens(self) -> TokensWithRawResponse:
        return TokensWithRawResponse(self._user.tokens)


class AsyncUserResourceWithRawResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.edit = async_to_raw_response_wrapper(
            user.edit,
        )
        self.get = async_to_raw_response_wrapper(
            user.get,
        )

    @cached_property
    def audit_logs(self) -> AsyncAuditLogsWithRawResponse:
        return AsyncAuditLogsWithRawResponse(self._user.audit_logs)

    @cached_property
    def billing(self) -> AsyncBillingWithRawResponse:
        return AsyncBillingWithRawResponse(self._user.billing)

    @cached_property
    def firewall(self) -> AsyncFirewallWithRawResponse:
        return AsyncFirewallWithRawResponse(self._user.firewall)

    @cached_property
    def invites(self) -> AsyncInvitesWithRawResponse:
        return AsyncInvitesWithRawResponse(self._user.invites)

    @cached_property
    def load_balancers(self) -> AsyncLoadBalancersWithRawResponse:
        return AsyncLoadBalancersWithRawResponse(self._user.load_balancers)

    @cached_property
    def organizations(self) -> AsyncOrganizationsWithRawResponse:
        return AsyncOrganizationsWithRawResponse(self._user.organizations)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsWithRawResponse:
        return AsyncSubscriptionsWithRawResponse(self._user.subscriptions)

    @cached_property
    def tokens(self) -> AsyncTokensWithRawResponse:
        return AsyncTokensWithRawResponse(self._user.tokens)


class UserResourceWithStreamingResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.edit = to_streamed_response_wrapper(
            user.edit,
        )
        self.get = to_streamed_response_wrapper(
            user.get,
        )

    @cached_property
    def audit_logs(self) -> AuditLogsWithStreamingResponse:
        return AuditLogsWithStreamingResponse(self._user.audit_logs)

    @cached_property
    def billing(self) -> BillingWithStreamingResponse:
        return BillingWithStreamingResponse(self._user.billing)

    @cached_property
    def firewall(self) -> FirewallWithStreamingResponse:
        return FirewallWithStreamingResponse(self._user.firewall)

    @cached_property
    def invites(self) -> InvitesWithStreamingResponse:
        return InvitesWithStreamingResponse(self._user.invites)

    @cached_property
    def load_balancers(self) -> LoadBalancersWithStreamingResponse:
        return LoadBalancersWithStreamingResponse(self._user.load_balancers)

    @cached_property
    def organizations(self) -> OrganizationsWithStreamingResponse:
        return OrganizationsWithStreamingResponse(self._user.organizations)

    @cached_property
    def subscriptions(self) -> SubscriptionsWithStreamingResponse:
        return SubscriptionsWithStreamingResponse(self._user.subscriptions)

    @cached_property
    def tokens(self) -> TokensWithStreamingResponse:
        return TokensWithStreamingResponse(self._user.tokens)


class AsyncUserResourceWithStreamingResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.edit = async_to_streamed_response_wrapper(
            user.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            user.get,
        )

    @cached_property
    def audit_logs(self) -> AsyncAuditLogsWithStreamingResponse:
        return AsyncAuditLogsWithStreamingResponse(self._user.audit_logs)

    @cached_property
    def billing(self) -> AsyncBillingWithStreamingResponse:
        return AsyncBillingWithStreamingResponse(self._user.billing)

    @cached_property
    def firewall(self) -> AsyncFirewallWithStreamingResponse:
        return AsyncFirewallWithStreamingResponse(self._user.firewall)

    @cached_property
    def invites(self) -> AsyncInvitesWithStreamingResponse:
        return AsyncInvitesWithStreamingResponse(self._user.invites)

    @cached_property
    def load_balancers(self) -> AsyncLoadBalancersWithStreamingResponse:
        return AsyncLoadBalancersWithStreamingResponse(self._user.load_balancers)

    @cached_property
    def organizations(self) -> AsyncOrganizationsWithStreamingResponse:
        return AsyncOrganizationsWithStreamingResponse(self._user.organizations)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsWithStreamingResponse:
        return AsyncSubscriptionsWithStreamingResponse(self._user.subscriptions)

    @cached_property
    def tokens(self) -> AsyncTokensWithStreamingResponse:
        return AsyncTokensWithStreamingResponse(self._user.tokens)
