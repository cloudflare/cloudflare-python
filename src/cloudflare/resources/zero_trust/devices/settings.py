# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

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
from ...._base_client import (
    make_request_options,
)
from ....types.zero_trust.devices import TeamsDevicesZeroTrustAccountDeviceSettings, setting_update_params

__all__ = ["Settings", "AsyncSettings"]


class Settings(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SettingsWithRawResponse:
        return SettingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsWithStreamingResponse:
        return SettingsWithStreamingResponse(self)

    def update(
        self,
        *,
        account_id: object,
        gateway_proxy_enabled: bool | NotGiven = NOT_GIVEN,
        gateway_udp_proxy_enabled: bool | NotGiven = NOT_GIVEN,
        root_certificate_installation_enabled: bool | NotGiven = NOT_GIVEN,
        use_zt_virtual_ip: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TeamsDevicesZeroTrustAccountDeviceSettings]:
        """
        Updates the current device settings for a Zero Trust account.

        Args:
          gateway_proxy_enabled: Enable gateway proxy filtering on TCP.

          gateway_udp_proxy_enabled: Enable gateway proxy filtering on UDP.

          root_certificate_installation_enabled: Enable installation of cloudflare managed root certificate.

          use_zt_virtual_ip: Enable using CGNAT virtual IPv4.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/accounts/{account_id}/devices/settings",
            body=maybe_transform(
                {
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[TeamsDevicesZeroTrustAccountDeviceSettings]],
                ResultWrapper[TeamsDevicesZeroTrustAccountDeviceSettings],
            ),
        )

    def list(
        self,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TeamsDevicesZeroTrustAccountDeviceSettings]:
        """
        Describes the current device settings for a Zero Trust account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_id}/devices/settings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[TeamsDevicesZeroTrustAccountDeviceSettings]],
                ResultWrapper[TeamsDevicesZeroTrustAccountDeviceSettings],
            ),
        )


class AsyncSettings(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSettingsWithRawResponse:
        return AsyncSettingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsWithStreamingResponse:
        return AsyncSettingsWithStreamingResponse(self)

    async def update(
        self,
        *,
        account_id: object,
        gateway_proxy_enabled: bool | NotGiven = NOT_GIVEN,
        gateway_udp_proxy_enabled: bool | NotGiven = NOT_GIVEN,
        root_certificate_installation_enabled: bool | NotGiven = NOT_GIVEN,
        use_zt_virtual_ip: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TeamsDevicesZeroTrustAccountDeviceSettings]:
        """
        Updates the current device settings for a Zero Trust account.

        Args:
          gateway_proxy_enabled: Enable gateway proxy filtering on TCP.

          gateway_udp_proxy_enabled: Enable gateway proxy filtering on UDP.

          root_certificate_installation_enabled: Enable installation of cloudflare managed root certificate.

          use_zt_virtual_ip: Enable using CGNAT virtual IPv4.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/accounts/{account_id}/devices/settings",
            body=await async_maybe_transform(
                {
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[TeamsDevicesZeroTrustAccountDeviceSettings]],
                ResultWrapper[TeamsDevicesZeroTrustAccountDeviceSettings],
            ),
        )

    async def list(
        self,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TeamsDevicesZeroTrustAccountDeviceSettings]:
        """
        Describes the current device settings for a Zero Trust account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_id}/devices/settings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[TeamsDevicesZeroTrustAccountDeviceSettings]],
                ResultWrapper[TeamsDevicesZeroTrustAccountDeviceSettings],
            ),
        )


class SettingsWithRawResponse:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

        self.update = to_raw_response_wrapper(
            settings.update,
        )
        self.list = to_raw_response_wrapper(
            settings.list,
        )


class AsyncSettingsWithRawResponse:
    def __init__(self, settings: AsyncSettings) -> None:
        self._settings = settings

        self.update = async_to_raw_response_wrapper(
            settings.update,
        )
        self.list = async_to_raw_response_wrapper(
            settings.list,
        )


class SettingsWithStreamingResponse:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

        self.update = to_streamed_response_wrapper(
            settings.update,
        )
        self.list = to_streamed_response_wrapper(
            settings.list,
        )


class AsyncSettingsWithStreamingResponse:
    def __init__(self, settings: AsyncSettings) -> None:
        self._settings = settings

        self.update = async_to_streamed_response_wrapper(
            settings.update,
        )
        self.list = async_to_streamed_response_wrapper(
            settings.list,
        )
