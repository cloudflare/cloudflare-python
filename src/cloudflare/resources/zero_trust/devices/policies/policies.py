# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from .excludes import (
    ExcludesResource,
    AsyncExcludesResource,
    ExcludesResourceWithRawResponse,
    AsyncExcludesResourceWithRawResponse,
    ExcludesResourceWithStreamingResponse,
    AsyncExcludesResourceWithStreamingResponse,
)
from .includes import (
    IncludesResource,
    AsyncIncludesResource,
    IncludesResourceWithRawResponse,
    AsyncIncludesResourceWithRawResponse,
    IncludesResourceWithStreamingResponse,
    AsyncIncludesResourceWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from .....pagination import SyncSinglePage, AsyncSinglePage
from .default_policy import (
    DefaultPolicyResource,
    AsyncDefaultPolicyResource,
    DefaultPolicyResourceWithRawResponse,
    AsyncDefaultPolicyResourceWithRawResponse,
    DefaultPolicyResourceWithStreamingResponse,
    AsyncDefaultPolicyResourceWithStreamingResponse,
)
from ....._base_client import AsyncPaginator, make_request_options
from .fallback_domains import (
    FallbackDomainsResource,
    AsyncFallbackDomainsResource,
    FallbackDomainsResourceWithRawResponse,
    AsyncFallbackDomainsResourceWithRawResponse,
    FallbackDomainsResourceWithStreamingResponse,
    AsyncFallbackDomainsResourceWithStreamingResponse,
)
from .....types.zero_trust.devices import policy_edit_params, policy_create_params
from .....types.zero_trust.devices.settings_policy import SettingsPolicy
from .....types.zero_trust.devices.policy_delete_response import PolicyDeleteResponse

__all__ = ["PoliciesResource", "AsyncPoliciesResource"]


class PoliciesResource(SyncAPIResource):
    @cached_property
    def default_policy(self) -> DefaultPolicyResource:
        return DefaultPolicyResource(self._client)

    @cached_property
    def excludes(self) -> ExcludesResource:
        return ExcludesResource(self._client)

    @cached_property
    def fallback_domains(self) -> FallbackDomainsResource:
        return FallbackDomainsResource(self._client)

    @cached_property
    def includes(self) -> IncludesResource:
        return IncludesResource(self._client)

    @cached_property
    def with_raw_response(self) -> PoliciesResourceWithRawResponse:
        return PoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PoliciesResourceWithStreamingResponse:
        return PoliciesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        match: str,
        name: str,
        precedence: float,
        allow_mode_switch: bool | NotGiven = NOT_GIVEN,
        allow_updates: bool | NotGiven = NOT_GIVEN,
        allowed_to_leave: bool | NotGiven = NOT_GIVEN,
        auto_connect: float | NotGiven = NOT_GIVEN,
        captive_portal: float | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        disable_auto_fallback: bool | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exclude_office_ips: bool | NotGiven = NOT_GIVEN,
        lan_allow_minutes: float | NotGiven = NOT_GIVEN,
        lan_allow_subnet_size: float | NotGiven = NOT_GIVEN,
        service_mode_v2: policy_create_params.ServiceModeV2 | NotGiven = NOT_GIVEN,
        support_url: str | NotGiven = NOT_GIVEN,
        switch_locked: bool | NotGiven = NOT_GIVEN,
        tunnel_protocol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingsPolicy]:
        """
        Creates a device settings profile to be applied to certain devices matching the
        criteria.

        Args:
          match: The wirefilter expression to match devices.

          name: The name of the device settings profile.

          precedence: The precedence of the policy. Lower values indicate higher precedence. Policies
              will be evaluated in ascending order of this field.

          allow_mode_switch: Whether to allow the user to switch WARP between modes.

          allow_updates: Whether to receive update notifications when a new version of the client is
              available.

          allowed_to_leave: Whether to allow devices to leave the organization.

          auto_connect: The amount of time in minutes to reconnect after having been disabled.

          captive_portal: Turn on the captive portal after the specified amount of time.

          description: A description of the policy.

          disable_auto_fallback: If the `dns_server` field of a fallback domain is not present, the client will
              fall back to a best guess of the default/system DNS resolvers unless this policy
              option is set to `true`.

          enabled: Whether the policy will be applied to matching devices.

          exclude_office_ips: Whether to add Microsoft IPs to Split Tunnel exclusions.

          lan_allow_minutes: The amount of time in minutes a user is allowed access to their LAN. A value of
              0 will allow LAN access until the next WARP reconnection, such as a reboot or a
              laptop waking from sleep. Note that this field is omitted from the response if
              null or unset.

          lan_allow_subnet_size: The size of the subnet for the local access network. Note that this field is
              omitted from the response if null or unset.

          support_url: The URL to launch when the Send Feedback button is clicked.

          switch_locked: Whether to allow the user to turn off the WARP switch and disconnect the client.

          tunnel_protocol: Determines which tunnel protocol to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/devices/policy",
            body=maybe_transform(
                {
                    "match": match,
                    "name": name,
                    "precedence": precedence,
                    "allow_mode_switch": allow_mode_switch,
                    "allow_updates": allow_updates,
                    "allowed_to_leave": allowed_to_leave,
                    "auto_connect": auto_connect,
                    "captive_portal": captive_portal,
                    "description": description,
                    "disable_auto_fallback": disable_auto_fallback,
                    "enabled": enabled,
                    "exclude_office_ips": exclude_office_ips,
                    "lan_allow_minutes": lan_allow_minutes,
                    "lan_allow_subnet_size": lan_allow_subnet_size,
                    "service_mode_v2": service_mode_v2,
                    "support_url": support_url,
                    "switch_locked": switch_locked,
                    "tunnel_protocol": tunnel_protocol,
                },
                policy_create_params.PolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SettingsPolicy]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SettingsPolicy]], ResultWrapper[SettingsPolicy]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[SettingsPolicy]:
        """
        Fetches a list of the device settings profiles for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/devices/policies",
            page=SyncSinglePage[SettingsPolicy],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=SettingsPolicy,
        )

    def delete(
        self,
        policy_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PolicyDeleteResponse]:
        """
        Deletes a device settings profile and fetches a list of the remaining profiles
        for an account.

        Args:
          policy_id: Device ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return self._delete(
            f"/accounts/{account_id}/devices/policy/{policy_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PolicyDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PolicyDeleteResponse]], ResultWrapper[PolicyDeleteResponse]),
        )

    def edit(
        self,
        policy_id: str,
        *,
        account_id: str,
        allow_mode_switch: bool | NotGiven = NOT_GIVEN,
        allow_updates: bool | NotGiven = NOT_GIVEN,
        allowed_to_leave: bool | NotGiven = NOT_GIVEN,
        auto_connect: float | NotGiven = NOT_GIVEN,
        captive_portal: float | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        disable_auto_fallback: bool | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exclude_office_ips: bool | NotGiven = NOT_GIVEN,
        match: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        precedence: float | NotGiven = NOT_GIVEN,
        service_mode_v2: policy_edit_params.ServiceModeV2 | NotGiven = NOT_GIVEN,
        support_url: str | NotGiven = NOT_GIVEN,
        switch_locked: bool | NotGiven = NOT_GIVEN,
        tunnel_protocol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingsPolicy]:
        """
        Updates a configured device settings profile.

        Args:
          policy_id: Device ID.

          allow_mode_switch: Whether to allow the user to switch WARP between modes.

          allow_updates: Whether to receive update notifications when a new version of the client is
              available.

          allowed_to_leave: Whether to allow devices to leave the organization.

          auto_connect: The amount of time in minutes to reconnect after having been disabled.

          captive_portal: Turn on the captive portal after the specified amount of time.

          description: A description of the policy.

          disable_auto_fallback: If the `dns_server` field of a fallback domain is not present, the client will
              fall back to a best guess of the default/system DNS resolvers unless this policy
              option is set to `true`.

          enabled: Whether the policy will be applied to matching devices.

          exclude_office_ips: Whether to add Microsoft IPs to Split Tunnel exclusions.

          match: The wirefilter expression to match devices.

          name: The name of the device settings profile.

          precedence: The precedence of the policy. Lower values indicate higher precedence. Policies
              will be evaluated in ascending order of this field.

          support_url: The URL to launch when the Send Feedback button is clicked.

          switch_locked: Whether to allow the user to turn off the WARP switch and disconnect the client.

          tunnel_protocol: Determines which tunnel protocol to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return self._patch(
            f"/accounts/{account_id}/devices/policy/{policy_id}",
            body=maybe_transform(
                {
                    "allow_mode_switch": allow_mode_switch,
                    "allow_updates": allow_updates,
                    "allowed_to_leave": allowed_to_leave,
                    "auto_connect": auto_connect,
                    "captive_portal": captive_portal,
                    "description": description,
                    "disable_auto_fallback": disable_auto_fallback,
                    "enabled": enabled,
                    "exclude_office_ips": exclude_office_ips,
                    "match": match,
                    "name": name,
                    "precedence": precedence,
                    "service_mode_v2": service_mode_v2,
                    "support_url": support_url,
                    "switch_locked": switch_locked,
                    "tunnel_protocol": tunnel_protocol,
                },
                policy_edit_params.PolicyEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SettingsPolicy]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SettingsPolicy]], ResultWrapper[SettingsPolicy]),
        )

    def get(
        self,
        policy_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingsPolicy]:
        """
        Fetches a device settings profile by ID.

        Args:
          policy_id: Device ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return self._get(
            f"/accounts/{account_id}/devices/policy/{policy_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SettingsPolicy]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SettingsPolicy]], ResultWrapper[SettingsPolicy]),
        )


class AsyncPoliciesResource(AsyncAPIResource):
    @cached_property
    def default_policy(self) -> AsyncDefaultPolicyResource:
        return AsyncDefaultPolicyResource(self._client)

    @cached_property
    def excludes(self) -> AsyncExcludesResource:
        return AsyncExcludesResource(self._client)

    @cached_property
    def fallback_domains(self) -> AsyncFallbackDomainsResource:
        return AsyncFallbackDomainsResource(self._client)

    @cached_property
    def includes(self) -> AsyncIncludesResource:
        return AsyncIncludesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPoliciesResourceWithRawResponse:
        return AsyncPoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPoliciesResourceWithStreamingResponse:
        return AsyncPoliciesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        match: str,
        name: str,
        precedence: float,
        allow_mode_switch: bool | NotGiven = NOT_GIVEN,
        allow_updates: bool | NotGiven = NOT_GIVEN,
        allowed_to_leave: bool | NotGiven = NOT_GIVEN,
        auto_connect: float | NotGiven = NOT_GIVEN,
        captive_portal: float | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        disable_auto_fallback: bool | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exclude_office_ips: bool | NotGiven = NOT_GIVEN,
        lan_allow_minutes: float | NotGiven = NOT_GIVEN,
        lan_allow_subnet_size: float | NotGiven = NOT_GIVEN,
        service_mode_v2: policy_create_params.ServiceModeV2 | NotGiven = NOT_GIVEN,
        support_url: str | NotGiven = NOT_GIVEN,
        switch_locked: bool | NotGiven = NOT_GIVEN,
        tunnel_protocol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingsPolicy]:
        """
        Creates a device settings profile to be applied to certain devices matching the
        criteria.

        Args:
          match: The wirefilter expression to match devices.

          name: The name of the device settings profile.

          precedence: The precedence of the policy. Lower values indicate higher precedence. Policies
              will be evaluated in ascending order of this field.

          allow_mode_switch: Whether to allow the user to switch WARP between modes.

          allow_updates: Whether to receive update notifications when a new version of the client is
              available.

          allowed_to_leave: Whether to allow devices to leave the organization.

          auto_connect: The amount of time in minutes to reconnect after having been disabled.

          captive_portal: Turn on the captive portal after the specified amount of time.

          description: A description of the policy.

          disable_auto_fallback: If the `dns_server` field of a fallback domain is not present, the client will
              fall back to a best guess of the default/system DNS resolvers unless this policy
              option is set to `true`.

          enabled: Whether the policy will be applied to matching devices.

          exclude_office_ips: Whether to add Microsoft IPs to Split Tunnel exclusions.

          lan_allow_minutes: The amount of time in minutes a user is allowed access to their LAN. A value of
              0 will allow LAN access until the next WARP reconnection, such as a reboot or a
              laptop waking from sleep. Note that this field is omitted from the response if
              null or unset.

          lan_allow_subnet_size: The size of the subnet for the local access network. Note that this field is
              omitted from the response if null or unset.

          support_url: The URL to launch when the Send Feedback button is clicked.

          switch_locked: Whether to allow the user to turn off the WARP switch and disconnect the client.

          tunnel_protocol: Determines which tunnel protocol to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/devices/policy",
            body=await async_maybe_transform(
                {
                    "match": match,
                    "name": name,
                    "precedence": precedence,
                    "allow_mode_switch": allow_mode_switch,
                    "allow_updates": allow_updates,
                    "allowed_to_leave": allowed_to_leave,
                    "auto_connect": auto_connect,
                    "captive_portal": captive_portal,
                    "description": description,
                    "disable_auto_fallback": disable_auto_fallback,
                    "enabled": enabled,
                    "exclude_office_ips": exclude_office_ips,
                    "lan_allow_minutes": lan_allow_minutes,
                    "lan_allow_subnet_size": lan_allow_subnet_size,
                    "service_mode_v2": service_mode_v2,
                    "support_url": support_url,
                    "switch_locked": switch_locked,
                    "tunnel_protocol": tunnel_protocol,
                },
                policy_create_params.PolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SettingsPolicy]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SettingsPolicy]], ResultWrapper[SettingsPolicy]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SettingsPolicy, AsyncSinglePage[SettingsPolicy]]:
        """
        Fetches a list of the device settings profiles for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/devices/policies",
            page=AsyncSinglePage[SettingsPolicy],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=SettingsPolicy,
        )

    async def delete(
        self,
        policy_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PolicyDeleteResponse]:
        """
        Deletes a device settings profile and fetches a list of the remaining profiles
        for an account.

        Args:
          policy_id: Device ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/devices/policy/{policy_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PolicyDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PolicyDeleteResponse]], ResultWrapper[PolicyDeleteResponse]),
        )

    async def edit(
        self,
        policy_id: str,
        *,
        account_id: str,
        allow_mode_switch: bool | NotGiven = NOT_GIVEN,
        allow_updates: bool | NotGiven = NOT_GIVEN,
        allowed_to_leave: bool | NotGiven = NOT_GIVEN,
        auto_connect: float | NotGiven = NOT_GIVEN,
        captive_portal: float | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        disable_auto_fallback: bool | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exclude_office_ips: bool | NotGiven = NOT_GIVEN,
        match: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        precedence: float | NotGiven = NOT_GIVEN,
        service_mode_v2: policy_edit_params.ServiceModeV2 | NotGiven = NOT_GIVEN,
        support_url: str | NotGiven = NOT_GIVEN,
        switch_locked: bool | NotGiven = NOT_GIVEN,
        tunnel_protocol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingsPolicy]:
        """
        Updates a configured device settings profile.

        Args:
          policy_id: Device ID.

          allow_mode_switch: Whether to allow the user to switch WARP between modes.

          allow_updates: Whether to receive update notifications when a new version of the client is
              available.

          allowed_to_leave: Whether to allow devices to leave the organization.

          auto_connect: The amount of time in minutes to reconnect after having been disabled.

          captive_portal: Turn on the captive portal after the specified amount of time.

          description: A description of the policy.

          disable_auto_fallback: If the `dns_server` field of a fallback domain is not present, the client will
              fall back to a best guess of the default/system DNS resolvers unless this policy
              option is set to `true`.

          enabled: Whether the policy will be applied to matching devices.

          exclude_office_ips: Whether to add Microsoft IPs to Split Tunnel exclusions.

          match: The wirefilter expression to match devices.

          name: The name of the device settings profile.

          precedence: The precedence of the policy. Lower values indicate higher precedence. Policies
              will be evaluated in ascending order of this field.

          support_url: The URL to launch when the Send Feedback button is clicked.

          switch_locked: Whether to allow the user to turn off the WARP switch and disconnect the client.

          tunnel_protocol: Determines which tunnel protocol to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/devices/policy/{policy_id}",
            body=await async_maybe_transform(
                {
                    "allow_mode_switch": allow_mode_switch,
                    "allow_updates": allow_updates,
                    "allowed_to_leave": allowed_to_leave,
                    "auto_connect": auto_connect,
                    "captive_portal": captive_portal,
                    "description": description,
                    "disable_auto_fallback": disable_auto_fallback,
                    "enabled": enabled,
                    "exclude_office_ips": exclude_office_ips,
                    "match": match,
                    "name": name,
                    "precedence": precedence,
                    "service_mode_v2": service_mode_v2,
                    "support_url": support_url,
                    "switch_locked": switch_locked,
                    "tunnel_protocol": tunnel_protocol,
                },
                policy_edit_params.PolicyEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SettingsPolicy]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SettingsPolicy]], ResultWrapper[SettingsPolicy]),
        )

    async def get(
        self,
        policy_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingsPolicy]:
        """
        Fetches a device settings profile by ID.

        Args:
          policy_id: Device ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return await self._get(
            f"/accounts/{account_id}/devices/policy/{policy_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SettingsPolicy]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SettingsPolicy]], ResultWrapper[SettingsPolicy]),
        )


class PoliciesResourceWithRawResponse:
    def __init__(self, policies: PoliciesResource) -> None:
        self._policies = policies

        self.create = to_raw_response_wrapper(
            policies.create,
        )
        self.list = to_raw_response_wrapper(
            policies.list,
        )
        self.delete = to_raw_response_wrapper(
            policies.delete,
        )
        self.edit = to_raw_response_wrapper(
            policies.edit,
        )
        self.get = to_raw_response_wrapper(
            policies.get,
        )

    @cached_property
    def default_policy(self) -> DefaultPolicyResourceWithRawResponse:
        return DefaultPolicyResourceWithRawResponse(self._policies.default_policy)

    @cached_property
    def excludes(self) -> ExcludesResourceWithRawResponse:
        return ExcludesResourceWithRawResponse(self._policies.excludes)

    @cached_property
    def fallback_domains(self) -> FallbackDomainsResourceWithRawResponse:
        return FallbackDomainsResourceWithRawResponse(self._policies.fallback_domains)

    @cached_property
    def includes(self) -> IncludesResourceWithRawResponse:
        return IncludesResourceWithRawResponse(self._policies.includes)


class AsyncPoliciesResourceWithRawResponse:
    def __init__(self, policies: AsyncPoliciesResource) -> None:
        self._policies = policies

        self.create = async_to_raw_response_wrapper(
            policies.create,
        )
        self.list = async_to_raw_response_wrapper(
            policies.list,
        )
        self.delete = async_to_raw_response_wrapper(
            policies.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            policies.edit,
        )
        self.get = async_to_raw_response_wrapper(
            policies.get,
        )

    @cached_property
    def default_policy(self) -> AsyncDefaultPolicyResourceWithRawResponse:
        return AsyncDefaultPolicyResourceWithRawResponse(self._policies.default_policy)

    @cached_property
    def excludes(self) -> AsyncExcludesResourceWithRawResponse:
        return AsyncExcludesResourceWithRawResponse(self._policies.excludes)

    @cached_property
    def fallback_domains(self) -> AsyncFallbackDomainsResourceWithRawResponse:
        return AsyncFallbackDomainsResourceWithRawResponse(self._policies.fallback_domains)

    @cached_property
    def includes(self) -> AsyncIncludesResourceWithRawResponse:
        return AsyncIncludesResourceWithRawResponse(self._policies.includes)


class PoliciesResourceWithStreamingResponse:
    def __init__(self, policies: PoliciesResource) -> None:
        self._policies = policies

        self.create = to_streamed_response_wrapper(
            policies.create,
        )
        self.list = to_streamed_response_wrapper(
            policies.list,
        )
        self.delete = to_streamed_response_wrapper(
            policies.delete,
        )
        self.edit = to_streamed_response_wrapper(
            policies.edit,
        )
        self.get = to_streamed_response_wrapper(
            policies.get,
        )

    @cached_property
    def default_policy(self) -> DefaultPolicyResourceWithStreamingResponse:
        return DefaultPolicyResourceWithStreamingResponse(self._policies.default_policy)

    @cached_property
    def excludes(self) -> ExcludesResourceWithStreamingResponse:
        return ExcludesResourceWithStreamingResponse(self._policies.excludes)

    @cached_property
    def fallback_domains(self) -> FallbackDomainsResourceWithStreamingResponse:
        return FallbackDomainsResourceWithStreamingResponse(self._policies.fallback_domains)

    @cached_property
    def includes(self) -> IncludesResourceWithStreamingResponse:
        return IncludesResourceWithStreamingResponse(self._policies.includes)


class AsyncPoliciesResourceWithStreamingResponse:
    def __init__(self, policies: AsyncPoliciesResource) -> None:
        self._policies = policies

        self.create = async_to_streamed_response_wrapper(
            policies.create,
        )
        self.list = async_to_streamed_response_wrapper(
            policies.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            policies.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            policies.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            policies.get,
        )

    @cached_property
    def default_policy(self) -> AsyncDefaultPolicyResourceWithStreamingResponse:
        return AsyncDefaultPolicyResourceWithStreamingResponse(self._policies.default_policy)

    @cached_property
    def excludes(self) -> AsyncExcludesResourceWithStreamingResponse:
        return AsyncExcludesResourceWithStreamingResponse(self._policies.excludes)

    @cached_property
    def fallback_domains(self) -> AsyncFallbackDomainsResourceWithStreamingResponse:
        return AsyncFallbackDomainsResourceWithStreamingResponse(self._policies.fallback_domains)

    @cached_property
    def includes(self) -> AsyncIncludesResourceWithStreamingResponse:
        return AsyncIncludesResourceWithStreamingResponse(self._policies.includes)
