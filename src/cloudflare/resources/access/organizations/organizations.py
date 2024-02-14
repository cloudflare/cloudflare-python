# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast

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
from .revoke_users import (
    RevokeUsers,
    AsyncRevokeUsers,
    RevokeUsersWithRawResponse,
    AsyncRevokeUsersWithRawResponse,
    RevokeUsersWithStreamingResponse,
    AsyncRevokeUsersWithStreamingResponse,
)
from ...._base_client import (
    make_request_options,
)
from ....types.access import (
    OrganizationZeroTrustOrganizationGetYourZeroTrustOrganizationResponse,
    OrganizationZeroTrustOrganizationCreateYourZeroTrustOrganizationResponse,
    OrganizationZeroTrustOrganizationUpdateYourZeroTrustOrganizationResponse,
    organization_zero_trust_organization_create_your_zero_trust_organization_params,
    organization_zero_trust_organization_update_your_zero_trust_organization_params,
)

__all__ = ["Organizations", "AsyncOrganizations"]


class Organizations(SyncAPIResource):
    @cached_property
    def revoke_users(self) -> RevokeUsers:
        return RevokeUsers(self._client)

    @cached_property
    def with_raw_response(self) -> OrganizationsWithRawResponse:
        return OrganizationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationsWithStreamingResponse:
        return OrganizationsWithStreamingResponse(self)

    def zero_trust_organization_create_your_zero_trust_organization(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        auth_domain: str,
        name: str,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        is_ui_read_only: bool | NotGiven = NOT_GIVEN,
        login_design: organization_zero_trust_organization_create_your_zero_trust_organization_params.LoginDesign
        | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        ui_read_only_toggle_reason: str | NotGiven = NOT_GIVEN,
        user_seat_expiration_inactive_time: str | NotGiven = NOT_GIVEN,
        warp_auth_session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationZeroTrustOrganizationCreateYourZeroTrustOrganizationResponse:
        """
        Sets up a Zero Trust organization for your account or zone.

        Args:
          account_or_zone_id: Identifier

          auth_domain: The unique subdomain assigned to your Zero Trust organization.

          name: The name of your Zero Trust organization.

          allow_authenticate_via_warp: When set to true, users can authenticate via WARP for any application in your
              organization. Application settings will take precedence over this value.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login.

          is_ui_read_only: Lock all settings as Read-Only in the Dashboard, regardless of user permission.
              Updates may only be made via the API or Terraform for this account when enabled.

          session_duration: The amount of time that tokens issued for applications will be valid. Must be in
              the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m,
              h.

          ui_read_only_toggle_reason: A description of the reason why the UI read only field is being toggled.

          user_seat_expiration_inactive_time: The amount of time a user seat is inactive before it expires. When the user seat
              exceeds the set time of inactivity, the user is removed as an active seat and no
              longer counts against your Teams seat count. Must be in the format `300ms` or
              `2h45m`. Valid time units are: `ns`, `us` (or `µs`), `ms`, `s`, `m`, `h`.

          warp_auth_session_duration: The amount of time that tokens issued for applications will be valid. Must be in
              the format `30m` or `2h45m`. Valid time units are: m, h.

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
            f"/{account_or_zone}/{account_or_zone_id}/access/organizations",
            body=maybe_transform(
                {
                    "auth_domain": auth_domain,
                    "name": name,
                    "allow_authenticate_via_warp": allow_authenticate_via_warp,
                    "auto_redirect_to_identity": auto_redirect_to_identity,
                    "is_ui_read_only": is_ui_read_only,
                    "login_design": login_design,
                    "session_duration": session_duration,
                    "ui_read_only_toggle_reason": ui_read_only_toggle_reason,
                    "user_seat_expiration_inactive_time": user_seat_expiration_inactive_time,
                    "warp_auth_session_duration": warp_auth_session_duration,
                },
                organization_zero_trust_organization_create_your_zero_trust_organization_params.OrganizationZeroTrustOrganizationCreateYourZeroTrustOrganizationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[OrganizationZeroTrustOrganizationCreateYourZeroTrustOrganizationResponse],
                ResultWrapper[OrganizationZeroTrustOrganizationCreateYourZeroTrustOrganizationResponse],
            ),
        )

    def zero_trust_organization_get_your_zero_trust_organization(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationZeroTrustOrganizationGetYourZeroTrustOrganizationResponse:
        """
        Returns the configuration for your Zero Trust organization.

        Args:
          account_or_zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return self._get(
            f"/{account_or_zone}/{account_or_zone_id}/access/organizations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[OrganizationZeroTrustOrganizationGetYourZeroTrustOrganizationResponse],
                ResultWrapper[OrganizationZeroTrustOrganizationGetYourZeroTrustOrganizationResponse],
            ),
        )

    def zero_trust_organization_update_your_zero_trust_organization(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        auth_domain: str | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        custom_pages: organization_zero_trust_organization_update_your_zero_trust_organization_params.CustomPages
        | NotGiven = NOT_GIVEN,
        is_ui_read_only: bool | NotGiven = NOT_GIVEN,
        login_design: organization_zero_trust_organization_update_your_zero_trust_organization_params.LoginDesign
        | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        ui_read_only_toggle_reason: str | NotGiven = NOT_GIVEN,
        user_seat_expiration_inactive_time: str | NotGiven = NOT_GIVEN,
        warp_auth_session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationZeroTrustOrganizationUpdateYourZeroTrustOrganizationResponse:
        """
        Updates the configuration for your Zero Trust organization.

        Args:
          account_or_zone_id: Identifier

          allow_authenticate_via_warp: When set to true, users can authenticate via WARP for any application in your
              organization. Application settings will take precedence over this value.

          auth_domain: The unique subdomain assigned to your Zero Trust organization.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login.

          is_ui_read_only: Lock all settings as Read-Only in the Dashboard, regardless of user permission.
              Updates may only be made via the API or Terraform for this account when enabled.

          name: The name of your Zero Trust organization.

          session_duration: The amount of time that tokens issued for applications will be valid. Must be in
              the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m,
              h.

          ui_read_only_toggle_reason: A description of the reason why the UI read only field is being toggled.

          user_seat_expiration_inactive_time: The amount of time a user seat is inactive before it expires. When the user seat
              exceeds the set time of inactivity, the user is removed as an active seat and no
              longer counts against your Teams seat count. Must be in the format `300ms` or
              `2h45m`. Valid time units are: `ns`, `us` (or `µs`), `ms`, `s`, `m`, `h`.

          warp_auth_session_duration: The amount of time that tokens issued for applications will be valid. Must be in
              the format `30m` or `2h45m`. Valid time units are: m, h.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return self._put(
            f"/{account_or_zone}/{account_or_zone_id}/access/organizations",
            body=maybe_transform(
                {
                    "allow_authenticate_via_warp": allow_authenticate_via_warp,
                    "auth_domain": auth_domain,
                    "auto_redirect_to_identity": auto_redirect_to_identity,
                    "custom_pages": custom_pages,
                    "is_ui_read_only": is_ui_read_only,
                    "login_design": login_design,
                    "name": name,
                    "session_duration": session_duration,
                    "ui_read_only_toggle_reason": ui_read_only_toggle_reason,
                    "user_seat_expiration_inactive_time": user_seat_expiration_inactive_time,
                    "warp_auth_session_duration": warp_auth_session_duration,
                },
                organization_zero_trust_organization_update_your_zero_trust_organization_params.OrganizationZeroTrustOrganizationUpdateYourZeroTrustOrganizationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[OrganizationZeroTrustOrganizationUpdateYourZeroTrustOrganizationResponse],
                ResultWrapper[OrganizationZeroTrustOrganizationUpdateYourZeroTrustOrganizationResponse],
            ),
        )


class AsyncOrganizations(AsyncAPIResource):
    @cached_property
    def revoke_users(self) -> AsyncRevokeUsers:
        return AsyncRevokeUsers(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrganizationsWithRawResponse:
        return AsyncOrganizationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationsWithStreamingResponse:
        return AsyncOrganizationsWithStreamingResponse(self)

    async def zero_trust_organization_create_your_zero_trust_organization(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        auth_domain: str,
        name: str,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        is_ui_read_only: bool | NotGiven = NOT_GIVEN,
        login_design: organization_zero_trust_organization_create_your_zero_trust_organization_params.LoginDesign
        | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        ui_read_only_toggle_reason: str | NotGiven = NOT_GIVEN,
        user_seat_expiration_inactive_time: str | NotGiven = NOT_GIVEN,
        warp_auth_session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationZeroTrustOrganizationCreateYourZeroTrustOrganizationResponse:
        """
        Sets up a Zero Trust organization for your account or zone.

        Args:
          account_or_zone_id: Identifier

          auth_domain: The unique subdomain assigned to your Zero Trust organization.

          name: The name of your Zero Trust organization.

          allow_authenticate_via_warp: When set to true, users can authenticate via WARP for any application in your
              organization. Application settings will take precedence over this value.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login.

          is_ui_read_only: Lock all settings as Read-Only in the Dashboard, regardless of user permission.
              Updates may only be made via the API or Terraform for this account when enabled.

          session_duration: The amount of time that tokens issued for applications will be valid. Must be in
              the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m,
              h.

          ui_read_only_toggle_reason: A description of the reason why the UI read only field is being toggled.

          user_seat_expiration_inactive_time: The amount of time a user seat is inactive before it expires. When the user seat
              exceeds the set time of inactivity, the user is removed as an active seat and no
              longer counts against your Teams seat count. Must be in the format `300ms` or
              `2h45m`. Valid time units are: `ns`, `us` (or `µs`), `ms`, `s`, `m`, `h`.

          warp_auth_session_duration: The amount of time that tokens issued for applications will be valid. Must be in
              the format `30m` or `2h45m`. Valid time units are: m, h.

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
            f"/{account_or_zone}/{account_or_zone_id}/access/organizations",
            body=maybe_transform(
                {
                    "auth_domain": auth_domain,
                    "name": name,
                    "allow_authenticate_via_warp": allow_authenticate_via_warp,
                    "auto_redirect_to_identity": auto_redirect_to_identity,
                    "is_ui_read_only": is_ui_read_only,
                    "login_design": login_design,
                    "session_duration": session_duration,
                    "ui_read_only_toggle_reason": ui_read_only_toggle_reason,
                    "user_seat_expiration_inactive_time": user_seat_expiration_inactive_time,
                    "warp_auth_session_duration": warp_auth_session_duration,
                },
                organization_zero_trust_organization_create_your_zero_trust_organization_params.OrganizationZeroTrustOrganizationCreateYourZeroTrustOrganizationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[OrganizationZeroTrustOrganizationCreateYourZeroTrustOrganizationResponse],
                ResultWrapper[OrganizationZeroTrustOrganizationCreateYourZeroTrustOrganizationResponse],
            ),
        )

    async def zero_trust_organization_get_your_zero_trust_organization(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationZeroTrustOrganizationGetYourZeroTrustOrganizationResponse:
        """
        Returns the configuration for your Zero Trust organization.

        Args:
          account_or_zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return await self._get(
            f"/{account_or_zone}/{account_or_zone_id}/access/organizations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[OrganizationZeroTrustOrganizationGetYourZeroTrustOrganizationResponse],
                ResultWrapper[OrganizationZeroTrustOrganizationGetYourZeroTrustOrganizationResponse],
            ),
        )

    async def zero_trust_organization_update_your_zero_trust_organization(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        auth_domain: str | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        custom_pages: organization_zero_trust_organization_update_your_zero_trust_organization_params.CustomPages
        | NotGiven = NOT_GIVEN,
        is_ui_read_only: bool | NotGiven = NOT_GIVEN,
        login_design: organization_zero_trust_organization_update_your_zero_trust_organization_params.LoginDesign
        | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        ui_read_only_toggle_reason: str | NotGiven = NOT_GIVEN,
        user_seat_expiration_inactive_time: str | NotGiven = NOT_GIVEN,
        warp_auth_session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationZeroTrustOrganizationUpdateYourZeroTrustOrganizationResponse:
        """
        Updates the configuration for your Zero Trust organization.

        Args:
          account_or_zone_id: Identifier

          allow_authenticate_via_warp: When set to true, users can authenticate via WARP for any application in your
              organization. Application settings will take precedence over this value.

          auth_domain: The unique subdomain assigned to your Zero Trust organization.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login.

          is_ui_read_only: Lock all settings as Read-Only in the Dashboard, regardless of user permission.
              Updates may only be made via the API or Terraform for this account when enabled.

          name: The name of your Zero Trust organization.

          session_duration: The amount of time that tokens issued for applications will be valid. Must be in
              the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m,
              h.

          ui_read_only_toggle_reason: A description of the reason why the UI read only field is being toggled.

          user_seat_expiration_inactive_time: The amount of time a user seat is inactive before it expires. When the user seat
              exceeds the set time of inactivity, the user is removed as an active seat and no
              longer counts against your Teams seat count. Must be in the format `300ms` or
              `2h45m`. Valid time units are: `ns`, `us` (or `µs`), `ms`, `s`, `m`, `h`.

          warp_auth_session_duration: The amount of time that tokens issued for applications will be valid. Must be in
              the format `30m` or `2h45m`. Valid time units are: m, h.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return await self._put(
            f"/{account_or_zone}/{account_or_zone_id}/access/organizations",
            body=maybe_transform(
                {
                    "allow_authenticate_via_warp": allow_authenticate_via_warp,
                    "auth_domain": auth_domain,
                    "auto_redirect_to_identity": auto_redirect_to_identity,
                    "custom_pages": custom_pages,
                    "is_ui_read_only": is_ui_read_only,
                    "login_design": login_design,
                    "name": name,
                    "session_duration": session_duration,
                    "ui_read_only_toggle_reason": ui_read_only_toggle_reason,
                    "user_seat_expiration_inactive_time": user_seat_expiration_inactive_time,
                    "warp_auth_session_duration": warp_auth_session_duration,
                },
                organization_zero_trust_organization_update_your_zero_trust_organization_params.OrganizationZeroTrustOrganizationUpdateYourZeroTrustOrganizationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[OrganizationZeroTrustOrganizationUpdateYourZeroTrustOrganizationResponse],
                ResultWrapper[OrganizationZeroTrustOrganizationUpdateYourZeroTrustOrganizationResponse],
            ),
        )


class OrganizationsWithRawResponse:
    def __init__(self, organizations: Organizations) -> None:
        self._organizations = organizations

        self.zero_trust_organization_create_your_zero_trust_organization = to_raw_response_wrapper(
            organizations.zero_trust_organization_create_your_zero_trust_organization,
        )
        self.zero_trust_organization_get_your_zero_trust_organization = to_raw_response_wrapper(
            organizations.zero_trust_organization_get_your_zero_trust_organization,
        )
        self.zero_trust_organization_update_your_zero_trust_organization = to_raw_response_wrapper(
            organizations.zero_trust_organization_update_your_zero_trust_organization,
        )

    @cached_property
    def revoke_users(self) -> RevokeUsersWithRawResponse:
        return RevokeUsersWithRawResponse(self._organizations.revoke_users)


class AsyncOrganizationsWithRawResponse:
    def __init__(self, organizations: AsyncOrganizations) -> None:
        self._organizations = organizations

        self.zero_trust_organization_create_your_zero_trust_organization = async_to_raw_response_wrapper(
            organizations.zero_trust_organization_create_your_zero_trust_organization,
        )
        self.zero_trust_organization_get_your_zero_trust_organization = async_to_raw_response_wrapper(
            organizations.zero_trust_organization_get_your_zero_trust_organization,
        )
        self.zero_trust_organization_update_your_zero_trust_organization = async_to_raw_response_wrapper(
            organizations.zero_trust_organization_update_your_zero_trust_organization,
        )

    @cached_property
    def revoke_users(self) -> AsyncRevokeUsersWithRawResponse:
        return AsyncRevokeUsersWithRawResponse(self._organizations.revoke_users)


class OrganizationsWithStreamingResponse:
    def __init__(self, organizations: Organizations) -> None:
        self._organizations = organizations

        self.zero_trust_organization_create_your_zero_trust_organization = to_streamed_response_wrapper(
            organizations.zero_trust_organization_create_your_zero_trust_organization,
        )
        self.zero_trust_organization_get_your_zero_trust_organization = to_streamed_response_wrapper(
            organizations.zero_trust_organization_get_your_zero_trust_organization,
        )
        self.zero_trust_organization_update_your_zero_trust_organization = to_streamed_response_wrapper(
            organizations.zero_trust_organization_update_your_zero_trust_organization,
        )

    @cached_property
    def revoke_users(self) -> RevokeUsersWithStreamingResponse:
        return RevokeUsersWithStreamingResponse(self._organizations.revoke_users)


class AsyncOrganizationsWithStreamingResponse:
    def __init__(self, organizations: AsyncOrganizations) -> None:
        self._organizations = organizations

        self.zero_trust_organization_create_your_zero_trust_organization = async_to_streamed_response_wrapper(
            organizations.zero_trust_organization_create_your_zero_trust_organization,
        )
        self.zero_trust_organization_get_your_zero_trust_organization = async_to_streamed_response_wrapper(
            organizations.zero_trust_organization_get_your_zero_trust_organization,
        )
        self.zero_trust_organization_update_your_zero_trust_organization = async_to_streamed_response_wrapper(
            organizations.zero_trust_organization_update_your_zero_trust_organization,
        )

    @cached_property
    def revoke_users(self) -> AsyncRevokeUsersWithStreamingResponse:
        return AsyncRevokeUsersWithStreamingResponse(self._organizations.revoke_users)
