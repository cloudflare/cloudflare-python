# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from .doh import (
    DOHResource,
    AsyncDOHResource,
    DOHResourceWithRawResponse,
    AsyncDOHResourceWithRawResponse,
    DOHResourceWithStreamingResponse,
    AsyncDOHResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.zero_trust import (
    organization_create_params,
    organization_update_params,
    organization_revoke_users_params,
)
from ....types.zero_trust.organization import Organization
from ....types.zero_trust.login_design_param import LoginDesignParam
from ....types.zero_trust.organization_revoke_users_response import OrganizationRevokeUsersResponse

__all__ = ["OrganizationsResource", "AsyncOrganizationsResource"]


class OrganizationsResource(SyncAPIResource):
    @cached_property
    def doh(self) -> DOHResource:
        return DOHResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrganizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return OrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return OrganizationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        auth_domain: str,
        name: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        is_ui_read_only: bool | NotGiven = NOT_GIVEN,
        login_design: LoginDesignParam | NotGiven = NOT_GIVEN,
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
    ) -> Optional[Organization]:
        """
        Sets up a Zero Trust organization for your account or zone.

        Args:
          auth_domain: The unique subdomain assigned to your Zero Trust organization.

          name: The name of your Zero Trust organization.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
              longer counts against your Teams seat count. Minimum value for this setting is 1
              month (730h). Must be in the format `300ms` or `2h45m`. Valid time units are:
              `ns`, `us` (or `µs`), `ms`, `s`, `m`, `h`.

          warp_auth_session_duration: The amount of time that tokens issued for applications will be valid. Must be in
              the format `30m` or `2h45m`. Valid time units are: m, h.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
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
                organization_create_params.OrganizationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Organization]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Organization]], ResultWrapper[Organization]),
        )

    def update(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        auth_domain: str | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        custom_pages: organization_update_params.CustomPages | NotGiven = NOT_GIVEN,
        is_ui_read_only: bool | NotGiven = NOT_GIVEN,
        login_design: LoginDesignParam | NotGiven = NOT_GIVEN,
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
    ) -> Optional[Organization]:
        """
        Updates the configuration for your Zero Trust organization.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
              longer counts against your Teams seat count. Minimum value for this setting is 1
              month (730h). Must be in the format `300ms` or `2h45m`. Valid time units are:
              `ns`, `us` (or `µs`), `ms`, `s`, `m`, `h`.

          warp_auth_session_duration: The amount of time that tokens issued for applications will be valid. Must be in
              the format `30m` or `2h45m`. Valid time units are: m, h.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
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
                organization_update_params.OrganizationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Organization]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Organization]], ResultWrapper[Organization]),
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Organization]:
        """
        Returns the configuration for your Zero Trust organization.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._get(
            f"/{account_or_zone}/{account_or_zone_id}/access/organizations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Organization]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Organization]], ResultWrapper[Organization]),
        )

    def revoke_users(
        self,
        *,
        email: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        query_devices: bool | NotGiven = NOT_GIVEN,
        body_devices: bool | NotGiven = NOT_GIVEN,
        user_uid: str | NotGiven = NOT_GIVEN,
        warp_session_reauth: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OrganizationRevokeUsersResponse]:
        """
        Revokes a user's access across all applications.

        Args:
          email: The email of the user to revoke.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          query_devices: When set to `true`, all devices associated with the user will be revoked.

          body_devices: When set to `true`, all devices associated with the user will be revoked.

          user_uid: The uuid of the user to revoke.

          warp_session_reauth: When set to `true`, the user will be required to re-authenticate to WARP for all
              Gateway policies that enforce a WARP client session duration. When `false`, the
              user’s WARP session will remain active

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._post(
            f"/{account_or_zone}/{account_or_zone_id}/access/organizations/revoke_user",
            body=maybe_transform(
                {
                    "email": email,
                    "body_devices": body_devices,
                    "user_uid": user_uid,
                    "warp_session_reauth": warp_session_reauth,
                },
                organization_revoke_users_params.OrganizationRevokeUsersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"query_devices": query_devices}, organization_revoke_users_params.OrganizationRevokeUsersParams
                ),
                post_parser=ResultWrapper[Optional[OrganizationRevokeUsersResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OrganizationRevokeUsersResponse]], ResultWrapper[OrganizationRevokeUsersResponse]
            ),
        )


class AsyncOrganizationsResource(AsyncAPIResource):
    @cached_property
    def doh(self) -> AsyncDOHResource:
        return AsyncDOHResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrganizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncOrganizationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        auth_domain: str,
        name: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        is_ui_read_only: bool | NotGiven = NOT_GIVEN,
        login_design: LoginDesignParam | NotGiven = NOT_GIVEN,
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
    ) -> Optional[Organization]:
        """
        Sets up a Zero Trust organization for your account or zone.

        Args:
          auth_domain: The unique subdomain assigned to your Zero Trust organization.

          name: The name of your Zero Trust organization.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
              longer counts against your Teams seat count. Minimum value for this setting is 1
              month (730h). Must be in the format `300ms` or `2h45m`. Valid time units are:
              `ns`, `us` (or `µs`), `ms`, `s`, `m`, `h`.

          warp_auth_session_duration: The amount of time that tokens issued for applications will be valid. Must be in
              the format `30m` or `2h45m`. Valid time units are: m, h.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return await self._post(
            f"/{account_or_zone}/{account_or_zone_id}/access/organizations",
            body=await async_maybe_transform(
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
                organization_create_params.OrganizationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Organization]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Organization]], ResultWrapper[Organization]),
        )

    async def update(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        auth_domain: str | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        custom_pages: organization_update_params.CustomPages | NotGiven = NOT_GIVEN,
        is_ui_read_only: bool | NotGiven = NOT_GIVEN,
        login_design: LoginDesignParam | NotGiven = NOT_GIVEN,
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
    ) -> Optional[Organization]:
        """
        Updates the configuration for your Zero Trust organization.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
              longer counts against your Teams seat count. Minimum value for this setting is 1
              month (730h). Must be in the format `300ms` or `2h45m`. Valid time units are:
              `ns`, `us` (or `µs`), `ms`, `s`, `m`, `h`.

          warp_auth_session_duration: The amount of time that tokens issued for applications will be valid. Must be in
              the format `30m` or `2h45m`. Valid time units are: m, h.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return await self._put(
            f"/{account_or_zone}/{account_or_zone_id}/access/organizations",
            body=await async_maybe_transform(
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
                organization_update_params.OrganizationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Organization]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Organization]], ResultWrapper[Organization]),
        )

    async def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Organization]:
        """
        Returns the configuration for your Zero Trust organization.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return await self._get(
            f"/{account_or_zone}/{account_or_zone_id}/access/organizations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Organization]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Organization]], ResultWrapper[Organization]),
        )

    async def revoke_users(
        self,
        *,
        email: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        query_devices: bool | NotGiven = NOT_GIVEN,
        body_devices: bool | NotGiven = NOT_GIVEN,
        user_uid: str | NotGiven = NOT_GIVEN,
        warp_session_reauth: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OrganizationRevokeUsersResponse]:
        """
        Revokes a user's access across all applications.

        Args:
          email: The email of the user to revoke.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          query_devices: When set to `true`, all devices associated with the user will be revoked.

          body_devices: When set to `true`, all devices associated with the user will be revoked.

          user_uid: The uuid of the user to revoke.

          warp_session_reauth: When set to `true`, the user will be required to re-authenticate to WARP for all
              Gateway policies that enforce a WARP client session duration. When `false`, the
              user’s WARP session will remain active

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return await self._post(
            f"/{account_or_zone}/{account_or_zone_id}/access/organizations/revoke_user",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "body_devices": body_devices,
                    "user_uid": user_uid,
                    "warp_session_reauth": warp_session_reauth,
                },
                organization_revoke_users_params.OrganizationRevokeUsersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"query_devices": query_devices}, organization_revoke_users_params.OrganizationRevokeUsersParams
                ),
                post_parser=ResultWrapper[Optional[OrganizationRevokeUsersResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OrganizationRevokeUsersResponse]], ResultWrapper[OrganizationRevokeUsersResponse]
            ),
        )


class OrganizationsResourceWithRawResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

        self.create = to_raw_response_wrapper(
            organizations.create,
        )
        self.update = to_raw_response_wrapper(
            organizations.update,
        )
        self.list = to_raw_response_wrapper(
            organizations.list,
        )
        self.revoke_users = to_raw_response_wrapper(
            organizations.revoke_users,
        )

    @cached_property
    def doh(self) -> DOHResourceWithRawResponse:
        return DOHResourceWithRawResponse(self._organizations.doh)


class AsyncOrganizationsResourceWithRawResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

        self.create = async_to_raw_response_wrapper(
            organizations.create,
        )
        self.update = async_to_raw_response_wrapper(
            organizations.update,
        )
        self.list = async_to_raw_response_wrapper(
            organizations.list,
        )
        self.revoke_users = async_to_raw_response_wrapper(
            organizations.revoke_users,
        )

    @cached_property
    def doh(self) -> AsyncDOHResourceWithRawResponse:
        return AsyncDOHResourceWithRawResponse(self._organizations.doh)


class OrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

        self.create = to_streamed_response_wrapper(
            organizations.create,
        )
        self.update = to_streamed_response_wrapper(
            organizations.update,
        )
        self.list = to_streamed_response_wrapper(
            organizations.list,
        )
        self.revoke_users = to_streamed_response_wrapper(
            organizations.revoke_users,
        )

    @cached_property
    def doh(self) -> DOHResourceWithStreamingResponse:
        return DOHResourceWithStreamingResponse(self._organizations.doh)


class AsyncOrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

        self.create = async_to_streamed_response_wrapper(
            organizations.create,
        )
        self.update = async_to_streamed_response_wrapper(
            organizations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            organizations.list,
        )
        self.revoke_users = async_to_streamed_response_wrapper(
            organizations.revoke_users,
        )

    @cached_property
    def doh(self) -> AsyncDOHResourceWithStreamingResponse:
        return AsyncDOHResourceWithStreamingResponse(self._organizations.doh)
