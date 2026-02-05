# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
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
from ....types.zero_trust.devices import setting_edit_params, setting_update_params
from ....types.zero_trust.devices.device_settings import DeviceSettings

__all__ = ["SettingsResource", "AsyncSettingsResource"]


class SettingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SettingsResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        account_id: str,
        disable_for_time: float | Omit = omit,
        external_emergency_signal_enabled: bool | Omit = omit,
        external_emergency_signal_fingerprint: str | Omit = omit,
        external_emergency_signal_interval: str | Omit = omit,
        external_emergency_signal_url: str | Omit = omit,
        gateway_proxy_enabled: bool | Omit = omit,
        gateway_udp_proxy_enabled: bool | Omit = omit,
        root_certificate_installation_enabled: bool | Omit = omit,
        use_zt_virtual_ip: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DeviceSettings]:
        """
        Updates the current device settings for a Zero Trust account.

        Args:
          disable_for_time: Sets the time limit, in seconds, that a user can use an override code to bypass
              WARP.

          external_emergency_signal_enabled: Controls whether the external emergency disconnect feature is enabled.

          external_emergency_signal_fingerprint: The SHA256 fingerprint (64 hexadecimal characters) of the HTTPS server
              certificate for the external_emergency_signal_url. If provided, the WARP client
              will use this value to verify the server's identity. The device will ignore any
              response if the server's certificate fingerprint does not exactly match this
              value.

          external_emergency_signal_interval: The interval at which the WARP client fetches the emergency disconnect signal,
              formatted as a duration string (e.g., "5m", "2m30s", "1h"). Minimum 30 seconds.

          external_emergency_signal_url: The HTTPS URL from which to fetch the emergency disconnect signal. Must use
              HTTPS and have an IPv4 or IPv6 address as the host.

          gateway_proxy_enabled: Enable gateway proxy filtering on TCP.

          gateway_udp_proxy_enabled: Enable gateway proxy filtering on UDP.

          root_certificate_installation_enabled: Enable installation of cloudflare managed root certificate.

          use_zt_virtual_ip: Enable using CGNAT virtual IPv4.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._put(
            f"/accounts/{account_id}/devices/settings",
            body=maybe_transform(
                {
                    "disable_for_time": disable_for_time,
                    "external_emergency_signal_enabled": external_emergency_signal_enabled,
                    "external_emergency_signal_fingerprint": external_emergency_signal_fingerprint,
                    "external_emergency_signal_interval": external_emergency_signal_interval,
                    "external_emergency_signal_url": external_emergency_signal_url,
                    "gateway_proxy_enabled": gateway_proxy_enabled,
                    "gateway_udp_proxy_enabled": gateway_udp_proxy_enabled,
                    "root_certificate_installation_enabled": root_certificate_installation_enabled,
                    "use_zt_virtual_ip": use_zt_virtual_ip,
                },
                setting_update_params.SettingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DeviceSettings]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DeviceSettings]], ResultWrapper[DeviceSettings]),
        )

    def delete(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DeviceSettings]:
        """
        Resets the current device settings for a Zero Trust account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._delete(
            f"/accounts/{account_id}/devices/settings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DeviceSettings]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DeviceSettings]], ResultWrapper[DeviceSettings]),
        )

    def edit(
        self,
        *,
        account_id: str,
        disable_for_time: float | Omit = omit,
        external_emergency_signal_enabled: bool | Omit = omit,
        external_emergency_signal_fingerprint: str | Omit = omit,
        external_emergency_signal_interval: str | Omit = omit,
        external_emergency_signal_url: str | Omit = omit,
        gateway_proxy_enabled: bool | Omit = omit,
        gateway_udp_proxy_enabled: bool | Omit = omit,
        root_certificate_installation_enabled: bool | Omit = omit,
        use_zt_virtual_ip: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DeviceSettings]:
        """
        Patches the current device settings for a Zero Trust account.

        Args:
          disable_for_time: Sets the time limit, in seconds, that a user can use an override code to bypass
              WARP.

          external_emergency_signal_enabled: Controls whether the external emergency disconnect feature is enabled.

          external_emergency_signal_fingerprint: The SHA256 fingerprint (64 hexadecimal characters) of the HTTPS server
              certificate for the external_emergency_signal_url. If provided, the WARP client
              will use this value to verify the server's identity. The device will ignore any
              response if the server's certificate fingerprint does not exactly match this
              value.

          external_emergency_signal_interval: The interval at which the WARP client fetches the emergency disconnect signal,
              formatted as a duration string (e.g., "5m", "2m30s", "1h"). Minimum 30 seconds.

          external_emergency_signal_url: The HTTPS URL from which to fetch the emergency disconnect signal. Must use
              HTTPS and have an IPv4 or IPv6 address as the host.

          gateway_proxy_enabled: Enable gateway proxy filtering on TCP.

          gateway_udp_proxy_enabled: Enable gateway proxy filtering on UDP.

          root_certificate_installation_enabled: Enable installation of cloudflare managed root certificate.

          use_zt_virtual_ip: Enable using CGNAT virtual IPv4.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._patch(
            f"/accounts/{account_id}/devices/settings",
            body=maybe_transform(
                {
                    "disable_for_time": disable_for_time,
                    "external_emergency_signal_enabled": external_emergency_signal_enabled,
                    "external_emergency_signal_fingerprint": external_emergency_signal_fingerprint,
                    "external_emergency_signal_interval": external_emergency_signal_interval,
                    "external_emergency_signal_url": external_emergency_signal_url,
                    "gateway_proxy_enabled": gateway_proxy_enabled,
                    "gateway_udp_proxy_enabled": gateway_udp_proxy_enabled,
                    "root_certificate_installation_enabled": root_certificate_installation_enabled,
                    "use_zt_virtual_ip": use_zt_virtual_ip,
                },
                setting_edit_params.SettingEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DeviceSettings]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DeviceSettings]], ResultWrapper[DeviceSettings]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DeviceSettings]:
        """
        Describes the current device settings for a Zero Trust account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/devices/settings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DeviceSettings]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DeviceSettings]], ResultWrapper[DeviceSettings]),
        )


class AsyncSettingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSettingsResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        account_id: str,
        disable_for_time: float | Omit = omit,
        external_emergency_signal_enabled: bool | Omit = omit,
        external_emergency_signal_fingerprint: str | Omit = omit,
        external_emergency_signal_interval: str | Omit = omit,
        external_emergency_signal_url: str | Omit = omit,
        gateway_proxy_enabled: bool | Omit = omit,
        gateway_udp_proxy_enabled: bool | Omit = omit,
        root_certificate_installation_enabled: bool | Omit = omit,
        use_zt_virtual_ip: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DeviceSettings]:
        """
        Updates the current device settings for a Zero Trust account.

        Args:
          disable_for_time: Sets the time limit, in seconds, that a user can use an override code to bypass
              WARP.

          external_emergency_signal_enabled: Controls whether the external emergency disconnect feature is enabled.

          external_emergency_signal_fingerprint: The SHA256 fingerprint (64 hexadecimal characters) of the HTTPS server
              certificate for the external_emergency_signal_url. If provided, the WARP client
              will use this value to verify the server's identity. The device will ignore any
              response if the server's certificate fingerprint does not exactly match this
              value.

          external_emergency_signal_interval: The interval at which the WARP client fetches the emergency disconnect signal,
              formatted as a duration string (e.g., "5m", "2m30s", "1h"). Minimum 30 seconds.

          external_emergency_signal_url: The HTTPS URL from which to fetch the emergency disconnect signal. Must use
              HTTPS and have an IPv4 or IPv6 address as the host.

          gateway_proxy_enabled: Enable gateway proxy filtering on TCP.

          gateway_udp_proxy_enabled: Enable gateway proxy filtering on UDP.

          root_certificate_installation_enabled: Enable installation of cloudflare managed root certificate.

          use_zt_virtual_ip: Enable using CGNAT virtual IPv4.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._put(
            f"/accounts/{account_id}/devices/settings",
            body=await async_maybe_transform(
                {
                    "disable_for_time": disable_for_time,
                    "external_emergency_signal_enabled": external_emergency_signal_enabled,
                    "external_emergency_signal_fingerprint": external_emergency_signal_fingerprint,
                    "external_emergency_signal_interval": external_emergency_signal_interval,
                    "external_emergency_signal_url": external_emergency_signal_url,
                    "gateway_proxy_enabled": gateway_proxy_enabled,
                    "gateway_udp_proxy_enabled": gateway_udp_proxy_enabled,
                    "root_certificate_installation_enabled": root_certificate_installation_enabled,
                    "use_zt_virtual_ip": use_zt_virtual_ip,
                },
                setting_update_params.SettingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DeviceSettings]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DeviceSettings]], ResultWrapper[DeviceSettings]),
        )

    async def delete(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DeviceSettings]:
        """
        Resets the current device settings for a Zero Trust account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/devices/settings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DeviceSettings]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DeviceSettings]], ResultWrapper[DeviceSettings]),
        )

    async def edit(
        self,
        *,
        account_id: str,
        disable_for_time: float | Omit = omit,
        external_emergency_signal_enabled: bool | Omit = omit,
        external_emergency_signal_fingerprint: str | Omit = omit,
        external_emergency_signal_interval: str | Omit = omit,
        external_emergency_signal_url: str | Omit = omit,
        gateway_proxy_enabled: bool | Omit = omit,
        gateway_udp_proxy_enabled: bool | Omit = omit,
        root_certificate_installation_enabled: bool | Omit = omit,
        use_zt_virtual_ip: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DeviceSettings]:
        """
        Patches the current device settings for a Zero Trust account.

        Args:
          disable_for_time: Sets the time limit, in seconds, that a user can use an override code to bypass
              WARP.

          external_emergency_signal_enabled: Controls whether the external emergency disconnect feature is enabled.

          external_emergency_signal_fingerprint: The SHA256 fingerprint (64 hexadecimal characters) of the HTTPS server
              certificate for the external_emergency_signal_url. If provided, the WARP client
              will use this value to verify the server's identity. The device will ignore any
              response if the server's certificate fingerprint does not exactly match this
              value.

          external_emergency_signal_interval: The interval at which the WARP client fetches the emergency disconnect signal,
              formatted as a duration string (e.g., "5m", "2m30s", "1h"). Minimum 30 seconds.

          external_emergency_signal_url: The HTTPS URL from which to fetch the emergency disconnect signal. Must use
              HTTPS and have an IPv4 or IPv6 address as the host.

          gateway_proxy_enabled: Enable gateway proxy filtering on TCP.

          gateway_udp_proxy_enabled: Enable gateway proxy filtering on UDP.

          root_certificate_installation_enabled: Enable installation of cloudflare managed root certificate.

          use_zt_virtual_ip: Enable using CGNAT virtual IPv4.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/devices/settings",
            body=await async_maybe_transform(
                {
                    "disable_for_time": disable_for_time,
                    "external_emergency_signal_enabled": external_emergency_signal_enabled,
                    "external_emergency_signal_fingerprint": external_emergency_signal_fingerprint,
                    "external_emergency_signal_interval": external_emergency_signal_interval,
                    "external_emergency_signal_url": external_emergency_signal_url,
                    "gateway_proxy_enabled": gateway_proxy_enabled,
                    "gateway_udp_proxy_enabled": gateway_udp_proxy_enabled,
                    "root_certificate_installation_enabled": root_certificate_installation_enabled,
                    "use_zt_virtual_ip": use_zt_virtual_ip,
                },
                setting_edit_params.SettingEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DeviceSettings]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DeviceSettings]], ResultWrapper[DeviceSettings]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DeviceSettings]:
        """
        Describes the current device settings for a Zero Trust account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/devices/settings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DeviceSettings]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DeviceSettings]], ResultWrapper[DeviceSettings]),
        )


class SettingsResourceWithRawResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.update = to_raw_response_wrapper(
            settings.update,
        )
        self.delete = to_raw_response_wrapper(
            settings.delete,
        )
        self.edit = to_raw_response_wrapper(
            settings.edit,
        )
        self.get = to_raw_response_wrapper(
            settings.get,
        )


class AsyncSettingsResourceWithRawResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.update = async_to_raw_response_wrapper(
            settings.update,
        )
        self.delete = async_to_raw_response_wrapper(
            settings.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            settings.edit,
        )
        self.get = async_to_raw_response_wrapper(
            settings.get,
        )


class SettingsResourceWithStreamingResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.update = to_streamed_response_wrapper(
            settings.update,
        )
        self.delete = to_streamed_response_wrapper(
            settings.delete,
        )
        self.edit = to_streamed_response_wrapper(
            settings.edit,
        )
        self.get = to_streamed_response_wrapper(
            settings.get,
        )


class AsyncSettingsResourceWithStreamingResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.update = async_to_streamed_response_wrapper(
            settings.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            settings.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            settings.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            settings.get,
        )
