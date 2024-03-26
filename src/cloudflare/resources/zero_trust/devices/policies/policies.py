# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from .excludes import (
    Excludes,
    AsyncExcludes,
    ExcludesWithRawResponse,
    AsyncExcludesWithRawResponse,
    ExcludesWithStreamingResponse,
    AsyncExcludesWithStreamingResponse,
)
from .includes import (
    Includes,
    AsyncIncludes,
    IncludesWithRawResponse,
    AsyncIncludesWithRawResponse,
    IncludesWithStreamingResponse,
    AsyncIncludesWithStreamingResponse,
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
from .default_policy import (
    DefaultPolicy,
    AsyncDefaultPolicy,
    DefaultPolicyWithRawResponse,
    AsyncDefaultPolicyWithRawResponse,
    DefaultPolicyWithStreamingResponse,
    AsyncDefaultPolicyWithStreamingResponse,
)
from ....._base_client import (
    make_request_options,
)
from .fallback_domains import (
    FallbackDomains,
    AsyncFallbackDomains,
    FallbackDomainsWithRawResponse,
    AsyncFallbackDomainsWithRawResponse,
    FallbackDomainsWithStreamingResponse,
    AsyncFallbackDomainsWithStreamingResponse,
)
from .....types.zero_trust.devices import (
    PolicyListResponse,
    PolicyDeleteResponse,
    TeamsDevicesDeviceSettingsPolicy,
    policy_edit_params,
    policy_create_params,
)

__all__ = ["Policies", "AsyncPolicies"]


class Policies(SyncAPIResource):
    @cached_property
    def default_policy(self) -> DefaultPolicy:
        return DefaultPolicy(self._client)

    @cached_property
    def excludes(self) -> Excludes:
        return Excludes(self._client)

    @cached_property
    def fallback_domains(self) -> FallbackDomains:
        return FallbackDomains(self._client)

    @cached_property
    def includes(self) -> Includes:
        return Includes(self._client)

    @cached_property
    def with_raw_response(self) -> PoliciesWithRawResponse:
        return PoliciesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PoliciesWithStreamingResponse:
        return PoliciesWithStreamingResponse(self)

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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TeamsDevicesDeviceSettingsPolicy]:
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
                },
                policy_create_params.PolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[TeamsDevicesDeviceSettingsPolicy]], ResultWrapper[TeamsDevicesDeviceSettingsPolicy]
            ),
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
    ) -> Optional[PolicyListResponse]:
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
        return self._get(
            f"/accounts/{account_id}/devices/policies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PolicyListResponse]], ResultWrapper[PolicyListResponse]),
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
                post_parser=ResultWrapper._unwrapper,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TeamsDevicesDeviceSettingsPolicy]:
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
                },
                policy_edit_params.PolicyEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[TeamsDevicesDeviceSettingsPolicy]], ResultWrapper[TeamsDevicesDeviceSettingsPolicy]
            ),
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
    ) -> Optional[TeamsDevicesDeviceSettingsPolicy]:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[TeamsDevicesDeviceSettingsPolicy]], ResultWrapper[TeamsDevicesDeviceSettingsPolicy]
            ),
        )


class AsyncPolicies(AsyncAPIResource):
    @cached_property
    def default_policy(self) -> AsyncDefaultPolicy:
        return AsyncDefaultPolicy(self._client)

    @cached_property
    def excludes(self) -> AsyncExcludes:
        return AsyncExcludes(self._client)

    @cached_property
    def fallback_domains(self) -> AsyncFallbackDomains:
        return AsyncFallbackDomains(self._client)

    @cached_property
    def includes(self) -> AsyncIncludes:
        return AsyncIncludes(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPoliciesWithRawResponse:
        return AsyncPoliciesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPoliciesWithStreamingResponse:
        return AsyncPoliciesWithStreamingResponse(self)

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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TeamsDevicesDeviceSettingsPolicy]:
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
                },
                policy_create_params.PolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[TeamsDevicesDeviceSettingsPolicy]], ResultWrapper[TeamsDevicesDeviceSettingsPolicy]
            ),
        )

    async def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PolicyListResponse]:
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
        return await self._get(
            f"/accounts/{account_id}/devices/policies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PolicyListResponse]], ResultWrapper[PolicyListResponse]),
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
                post_parser=ResultWrapper._unwrapper,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TeamsDevicesDeviceSettingsPolicy]:
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
                },
                policy_edit_params.PolicyEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[TeamsDevicesDeviceSettingsPolicy]], ResultWrapper[TeamsDevicesDeviceSettingsPolicy]
            ),
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
    ) -> Optional[TeamsDevicesDeviceSettingsPolicy]:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[TeamsDevicesDeviceSettingsPolicy]], ResultWrapper[TeamsDevicesDeviceSettingsPolicy]
            ),
        )


class PoliciesWithRawResponse:
    def __init__(self, policies: Policies) -> None:
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
    def default_policy(self) -> DefaultPolicyWithRawResponse:
        return DefaultPolicyWithRawResponse(self._policies.default_policy)

    @cached_property
    def excludes(self) -> ExcludesWithRawResponse:
        return ExcludesWithRawResponse(self._policies.excludes)

    @cached_property
    def fallback_domains(self) -> FallbackDomainsWithRawResponse:
        return FallbackDomainsWithRawResponse(self._policies.fallback_domains)

    @cached_property
    def includes(self) -> IncludesWithRawResponse:
        return IncludesWithRawResponse(self._policies.includes)


class AsyncPoliciesWithRawResponse:
    def __init__(self, policies: AsyncPolicies) -> None:
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
    def default_policy(self) -> AsyncDefaultPolicyWithRawResponse:
        return AsyncDefaultPolicyWithRawResponse(self._policies.default_policy)

    @cached_property
    def excludes(self) -> AsyncExcludesWithRawResponse:
        return AsyncExcludesWithRawResponse(self._policies.excludes)

    @cached_property
    def fallback_domains(self) -> AsyncFallbackDomainsWithRawResponse:
        return AsyncFallbackDomainsWithRawResponse(self._policies.fallback_domains)

    @cached_property
    def includes(self) -> AsyncIncludesWithRawResponse:
        return AsyncIncludesWithRawResponse(self._policies.includes)


class PoliciesWithStreamingResponse:
    def __init__(self, policies: Policies) -> None:
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
    def default_policy(self) -> DefaultPolicyWithStreamingResponse:
        return DefaultPolicyWithStreamingResponse(self._policies.default_policy)

    @cached_property
    def excludes(self) -> ExcludesWithStreamingResponse:
        return ExcludesWithStreamingResponse(self._policies.excludes)

    @cached_property
    def fallback_domains(self) -> FallbackDomainsWithStreamingResponse:
        return FallbackDomainsWithStreamingResponse(self._policies.fallback_domains)

    @cached_property
    def includes(self) -> IncludesWithStreamingResponse:
        return IncludesWithStreamingResponse(self._policies.includes)


class AsyncPoliciesWithStreamingResponse:
    def __init__(self, policies: AsyncPolicies) -> None:
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
    def default_policy(self) -> AsyncDefaultPolicyWithStreamingResponse:
        return AsyncDefaultPolicyWithStreamingResponse(self._policies.default_policy)

    @cached_property
    def excludes(self) -> AsyncExcludesWithStreamingResponse:
        return AsyncExcludesWithStreamingResponse(self._policies.excludes)

    @cached_property
    def fallback_domains(self) -> AsyncFallbackDomainsWithStreamingResponse:
        return AsyncFallbackDomainsWithStreamingResponse(self._policies.fallback_domains)

    @cached_property
    def includes(self) -> AsyncIncludesWithStreamingResponse:
        return AsyncIncludesWithStreamingResponse(self._policies.includes)
