# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast

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
from ......_types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ......_utils import (
    maybe_transform,
    async_maybe_transform,
)
from ......_compat import cached_property
from .certificates import (
    CertificatesResource,
    AsyncCertificatesResource,
    CertificatesResourceWithRawResponse,
    AsyncCertificatesResourceWithRawResponse,
    CertificatesResourceWithStreamingResponse,
    AsyncCertificatesResourceWithStreamingResponse,
)
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_wrappers import ResultWrapper
from .fallback_domains import (
    FallbackDomainsResource,
    AsyncFallbackDomainsResource,
    FallbackDomainsResourceWithRawResponse,
    AsyncFallbackDomainsResourceWithRawResponse,
    FallbackDomainsResourceWithStreamingResponse,
    AsyncFallbackDomainsResourceWithStreamingResponse,
)
from ......_base_client import make_request_options
from ......types.zero_trust.devices.policies import default_edit_params
from ......types.zero_trust.devices.split_tunnel_exclude_param import SplitTunnelExcludeParam
from ......types.zero_trust.devices.policies.default_get_response import DefaultGetResponse
from ......types.zero_trust.devices.policies.default_edit_response import DefaultEditResponse

__all__ = ["DefaultResource", "AsyncDefaultResource"]


class DefaultResource(SyncAPIResource):
    @cached_property
    def excludes(self) -> ExcludesResource:
        return ExcludesResource(self._client)

    @cached_property
    def includes(self) -> IncludesResource:
        return IncludesResource(self._client)

    @cached_property
    def fallback_domains(self) -> FallbackDomainsResource:
        return FallbackDomainsResource(self._client)

    @cached_property
    def certificates(self) -> CertificatesResource:
        return CertificatesResource(self._client)

    @cached_property
    def with_raw_response(self) -> DefaultResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DefaultResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DefaultResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DefaultResourceWithStreamingResponse(self)

    def edit(
        self,
        *,
        account_id: str,
        allow_mode_switch: bool | NotGiven = NOT_GIVEN,
        allow_updates: bool | NotGiven = NOT_GIVEN,
        allowed_to_leave: bool | NotGiven = NOT_GIVEN,
        auto_connect: float | NotGiven = NOT_GIVEN,
        captive_portal: float | NotGiven = NOT_GIVEN,
        disable_auto_fallback: bool | NotGiven = NOT_GIVEN,
        exclude: Iterable[SplitTunnelExcludeParam] | NotGiven = NOT_GIVEN,
        exclude_office_ips: bool | NotGiven = NOT_GIVEN,
        include: Iterable[SplitTunnelExcludeParam] | NotGiven = NOT_GIVEN,
        register_interface_ip_with_dns: bool | NotGiven = NOT_GIVEN,
        service_mode_v2: default_edit_params.ServiceModeV2 | NotGiven = NOT_GIVEN,
        support_url: str | NotGiven = NOT_GIVEN,
        switch_locked: bool | NotGiven = NOT_GIVEN,
        tunnel_protocol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DefaultEditResponse]:
        """
        Updates the default device settings profile for an account.

        Args:
          allow_mode_switch: Whether to allow the user to switch WARP between modes.

          allow_updates: Whether to receive update notifications when a new version of the client is
              available.

          allowed_to_leave: Whether to allow devices to leave the organization.

          auto_connect: The amount of time in seconds to reconnect after having been disabled.

          captive_portal: Turn on the captive portal after the specified amount of time.

          disable_auto_fallback: If the `dns_server` field of a fallback domain is not present, the client will
              fall back to a best guess of the default/system DNS resolvers unless this policy
              option is set to `true`.

          exclude: List of routes excluded in the WARP client's tunnel. Both 'exclude' and
              'include' cannot be set in the same request.

          exclude_office_ips: Whether to add Microsoft IPs to Split Tunnel exclusions.

          include: List of routes included in the WARP client's tunnel. Both 'exclude' and
              'include' cannot be set in the same request.

          register_interface_ip_with_dns: Determines if the operating system will register WARP's local interface IP with
              your on-premises DNS server.

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
        return self._patch(
            f"/accounts/{account_id}/devices/policy",
            body=maybe_transform(
                {
                    "allow_mode_switch": allow_mode_switch,
                    "allow_updates": allow_updates,
                    "allowed_to_leave": allowed_to_leave,
                    "auto_connect": auto_connect,
                    "captive_portal": captive_portal,
                    "disable_auto_fallback": disable_auto_fallback,
                    "exclude": exclude,
                    "exclude_office_ips": exclude_office_ips,
                    "include": include,
                    "register_interface_ip_with_dns": register_interface_ip_with_dns,
                    "service_mode_v2": service_mode_v2,
                    "support_url": support_url,
                    "switch_locked": switch_locked,
                    "tunnel_protocol": tunnel_protocol,
                },
                default_edit_params.DefaultEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DefaultEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DefaultEditResponse]], ResultWrapper[DefaultEditResponse]),
        )

    def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DefaultGetResponse]:
        """
        Fetches the default device settings profile for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/devices/policy",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DefaultGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DefaultGetResponse]], ResultWrapper[DefaultGetResponse]),
        )


class AsyncDefaultResource(AsyncAPIResource):
    @cached_property
    def excludes(self) -> AsyncExcludesResource:
        return AsyncExcludesResource(self._client)

    @cached_property
    def includes(self) -> AsyncIncludesResource:
        return AsyncIncludesResource(self._client)

    @cached_property
    def fallback_domains(self) -> AsyncFallbackDomainsResource:
        return AsyncFallbackDomainsResource(self._client)

    @cached_property
    def certificates(self) -> AsyncCertificatesResource:
        return AsyncCertificatesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDefaultResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDefaultResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDefaultResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDefaultResourceWithStreamingResponse(self)

    async def edit(
        self,
        *,
        account_id: str,
        allow_mode_switch: bool | NotGiven = NOT_GIVEN,
        allow_updates: bool | NotGiven = NOT_GIVEN,
        allowed_to_leave: bool | NotGiven = NOT_GIVEN,
        auto_connect: float | NotGiven = NOT_GIVEN,
        captive_portal: float | NotGiven = NOT_GIVEN,
        disable_auto_fallback: bool | NotGiven = NOT_GIVEN,
        exclude: Iterable[SplitTunnelExcludeParam] | NotGiven = NOT_GIVEN,
        exclude_office_ips: bool | NotGiven = NOT_GIVEN,
        include: Iterable[SplitTunnelExcludeParam] | NotGiven = NOT_GIVEN,
        register_interface_ip_with_dns: bool | NotGiven = NOT_GIVEN,
        service_mode_v2: default_edit_params.ServiceModeV2 | NotGiven = NOT_GIVEN,
        support_url: str | NotGiven = NOT_GIVEN,
        switch_locked: bool | NotGiven = NOT_GIVEN,
        tunnel_protocol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DefaultEditResponse]:
        """
        Updates the default device settings profile for an account.

        Args:
          allow_mode_switch: Whether to allow the user to switch WARP between modes.

          allow_updates: Whether to receive update notifications when a new version of the client is
              available.

          allowed_to_leave: Whether to allow devices to leave the organization.

          auto_connect: The amount of time in seconds to reconnect after having been disabled.

          captive_portal: Turn on the captive portal after the specified amount of time.

          disable_auto_fallback: If the `dns_server` field of a fallback domain is not present, the client will
              fall back to a best guess of the default/system DNS resolvers unless this policy
              option is set to `true`.

          exclude: List of routes excluded in the WARP client's tunnel. Both 'exclude' and
              'include' cannot be set in the same request.

          exclude_office_ips: Whether to add Microsoft IPs to Split Tunnel exclusions.

          include: List of routes included in the WARP client's tunnel. Both 'exclude' and
              'include' cannot be set in the same request.

          register_interface_ip_with_dns: Determines if the operating system will register WARP's local interface IP with
              your on-premises DNS server.

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
        return await self._patch(
            f"/accounts/{account_id}/devices/policy",
            body=await async_maybe_transform(
                {
                    "allow_mode_switch": allow_mode_switch,
                    "allow_updates": allow_updates,
                    "allowed_to_leave": allowed_to_leave,
                    "auto_connect": auto_connect,
                    "captive_portal": captive_portal,
                    "disable_auto_fallback": disable_auto_fallback,
                    "exclude": exclude,
                    "exclude_office_ips": exclude_office_ips,
                    "include": include,
                    "register_interface_ip_with_dns": register_interface_ip_with_dns,
                    "service_mode_v2": service_mode_v2,
                    "support_url": support_url,
                    "switch_locked": switch_locked,
                    "tunnel_protocol": tunnel_protocol,
                },
                default_edit_params.DefaultEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DefaultEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DefaultEditResponse]], ResultWrapper[DefaultEditResponse]),
        )

    async def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DefaultGetResponse]:
        """
        Fetches the default device settings profile for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/devices/policy",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DefaultGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DefaultGetResponse]], ResultWrapper[DefaultGetResponse]),
        )


class DefaultResourceWithRawResponse:
    def __init__(self, default: DefaultResource) -> None:
        self._default = default

        self.edit = to_raw_response_wrapper(
            default.edit,
        )
        self.get = to_raw_response_wrapper(
            default.get,
        )

    @cached_property
    def excludes(self) -> ExcludesResourceWithRawResponse:
        return ExcludesResourceWithRawResponse(self._default.excludes)

    @cached_property
    def includes(self) -> IncludesResourceWithRawResponse:
        return IncludesResourceWithRawResponse(self._default.includes)

    @cached_property
    def fallback_domains(self) -> FallbackDomainsResourceWithRawResponse:
        return FallbackDomainsResourceWithRawResponse(self._default.fallback_domains)

    @cached_property
    def certificates(self) -> CertificatesResourceWithRawResponse:
        return CertificatesResourceWithRawResponse(self._default.certificates)


class AsyncDefaultResourceWithRawResponse:
    def __init__(self, default: AsyncDefaultResource) -> None:
        self._default = default

        self.edit = async_to_raw_response_wrapper(
            default.edit,
        )
        self.get = async_to_raw_response_wrapper(
            default.get,
        )

    @cached_property
    def excludes(self) -> AsyncExcludesResourceWithRawResponse:
        return AsyncExcludesResourceWithRawResponse(self._default.excludes)

    @cached_property
    def includes(self) -> AsyncIncludesResourceWithRawResponse:
        return AsyncIncludesResourceWithRawResponse(self._default.includes)

    @cached_property
    def fallback_domains(self) -> AsyncFallbackDomainsResourceWithRawResponse:
        return AsyncFallbackDomainsResourceWithRawResponse(self._default.fallback_domains)

    @cached_property
    def certificates(self) -> AsyncCertificatesResourceWithRawResponse:
        return AsyncCertificatesResourceWithRawResponse(self._default.certificates)


class DefaultResourceWithStreamingResponse:
    def __init__(self, default: DefaultResource) -> None:
        self._default = default

        self.edit = to_streamed_response_wrapper(
            default.edit,
        )
        self.get = to_streamed_response_wrapper(
            default.get,
        )

    @cached_property
    def excludes(self) -> ExcludesResourceWithStreamingResponse:
        return ExcludesResourceWithStreamingResponse(self._default.excludes)

    @cached_property
    def includes(self) -> IncludesResourceWithStreamingResponse:
        return IncludesResourceWithStreamingResponse(self._default.includes)

    @cached_property
    def fallback_domains(self) -> FallbackDomainsResourceWithStreamingResponse:
        return FallbackDomainsResourceWithStreamingResponse(self._default.fallback_domains)

    @cached_property
    def certificates(self) -> CertificatesResourceWithStreamingResponse:
        return CertificatesResourceWithStreamingResponse(self._default.certificates)


class AsyncDefaultResourceWithStreamingResponse:
    def __init__(self, default: AsyncDefaultResource) -> None:
        self._default = default

        self.edit = async_to_streamed_response_wrapper(
            default.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            default.get,
        )

    @cached_property
    def excludes(self) -> AsyncExcludesResourceWithStreamingResponse:
        return AsyncExcludesResourceWithStreamingResponse(self._default.excludes)

    @cached_property
    def includes(self) -> AsyncIncludesResourceWithStreamingResponse:
        return AsyncIncludesResourceWithStreamingResponse(self._default.includes)

    @cached_property
    def fallback_domains(self) -> AsyncFallbackDomainsResourceWithStreamingResponse:
        return AsyncFallbackDomainsResourceWithStreamingResponse(self._default.fallback_domains)

    @cached_property
    def certificates(self) -> AsyncCertificatesResourceWithStreamingResponse:
        return AsyncCertificatesResourceWithStreamingResponse(self._default.certificates)
