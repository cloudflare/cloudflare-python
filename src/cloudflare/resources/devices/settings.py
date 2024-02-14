# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.devices import (
    SettingZeroTrustAccountsGetDeviceSettingsForZeroTrustAccountResponse,
    SettingZeroTrustAccountsUpdateDeviceSettingsForTheZeroTrustAccountResponse,
)

from typing import Type, Optional

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
from ...types.devices import setting_zero_trust_accounts_update_device_settings_for_the_zero_trust_account_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Settings", "AsyncSettings"]


class Settings(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SettingsWithRawResponse:
        return SettingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsWithStreamingResponse:
        return SettingsWithStreamingResponse(self)

    def zero_trust_accounts_get_device_settings_for_zero_trust_account(
        self,
        identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingZeroTrustAccountsGetDeviceSettingsForZeroTrustAccountResponse]:
        """
        Describes the current device settings for a Zero Trust account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{identifier}/devices/settings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[SettingZeroTrustAccountsGetDeviceSettingsForZeroTrustAccountResponse]],
                ResultWrapper[SettingZeroTrustAccountsGetDeviceSettingsForZeroTrustAccountResponse],
            ),
        )

    def zero_trust_accounts_update_device_settings_for_the_zero_trust_account(
        self,
        identifier: object,
        *,
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
    ) -> Optional[SettingZeroTrustAccountsUpdateDeviceSettingsForTheZeroTrustAccountResponse]:
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
            f"/accounts/{identifier}/devices/settings",
            body=maybe_transform(
                {
                    "gateway_proxy_enabled": gateway_proxy_enabled,
                    "gateway_udp_proxy_enabled": gateway_udp_proxy_enabled,
                    "root_certificate_installation_enabled": root_certificate_installation_enabled,
                    "use_zt_virtual_ip": use_zt_virtual_ip,
                },
                setting_zero_trust_accounts_update_device_settings_for_the_zero_trust_account_params.SettingZeroTrustAccountsUpdateDeviceSettingsForTheZeroTrustAccountParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[SettingZeroTrustAccountsUpdateDeviceSettingsForTheZeroTrustAccountResponse]],
                ResultWrapper[SettingZeroTrustAccountsUpdateDeviceSettingsForTheZeroTrustAccountResponse],
            ),
        )


class AsyncSettings(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSettingsWithRawResponse:
        return AsyncSettingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsWithStreamingResponse:
        return AsyncSettingsWithStreamingResponse(self)

    async def zero_trust_accounts_get_device_settings_for_zero_trust_account(
        self,
        identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingZeroTrustAccountsGetDeviceSettingsForZeroTrustAccountResponse]:
        """
        Describes the current device settings for a Zero Trust account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{identifier}/devices/settings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[SettingZeroTrustAccountsGetDeviceSettingsForZeroTrustAccountResponse]],
                ResultWrapper[SettingZeroTrustAccountsGetDeviceSettingsForZeroTrustAccountResponse],
            ),
        )

    async def zero_trust_accounts_update_device_settings_for_the_zero_trust_account(
        self,
        identifier: object,
        *,
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
    ) -> Optional[SettingZeroTrustAccountsUpdateDeviceSettingsForTheZeroTrustAccountResponse]:
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
            f"/accounts/{identifier}/devices/settings",
            body=maybe_transform(
                {
                    "gateway_proxy_enabled": gateway_proxy_enabled,
                    "gateway_udp_proxy_enabled": gateway_udp_proxy_enabled,
                    "root_certificate_installation_enabled": root_certificate_installation_enabled,
                    "use_zt_virtual_ip": use_zt_virtual_ip,
                },
                setting_zero_trust_accounts_update_device_settings_for_the_zero_trust_account_params.SettingZeroTrustAccountsUpdateDeviceSettingsForTheZeroTrustAccountParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[SettingZeroTrustAccountsUpdateDeviceSettingsForTheZeroTrustAccountResponse]],
                ResultWrapper[SettingZeroTrustAccountsUpdateDeviceSettingsForTheZeroTrustAccountResponse],
            ),
        )


class SettingsWithRawResponse:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

        self.zero_trust_accounts_get_device_settings_for_zero_trust_account = to_raw_response_wrapper(
            settings.zero_trust_accounts_get_device_settings_for_zero_trust_account,
        )
        self.zero_trust_accounts_update_device_settings_for_the_zero_trust_account = to_raw_response_wrapper(
            settings.zero_trust_accounts_update_device_settings_for_the_zero_trust_account,
        )


class AsyncSettingsWithRawResponse:
    def __init__(self, settings: AsyncSettings) -> None:
        self._settings = settings

        self.zero_trust_accounts_get_device_settings_for_zero_trust_account = async_to_raw_response_wrapper(
            settings.zero_trust_accounts_get_device_settings_for_zero_trust_account,
        )
        self.zero_trust_accounts_update_device_settings_for_the_zero_trust_account = async_to_raw_response_wrapper(
            settings.zero_trust_accounts_update_device_settings_for_the_zero_trust_account,
        )


class SettingsWithStreamingResponse:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

        self.zero_trust_accounts_get_device_settings_for_zero_trust_account = to_streamed_response_wrapper(
            settings.zero_trust_accounts_get_device_settings_for_zero_trust_account,
        )
        self.zero_trust_accounts_update_device_settings_for_the_zero_trust_account = to_streamed_response_wrapper(
            settings.zero_trust_accounts_update_device_settings_for_the_zero_trust_account,
        )


class AsyncSettingsWithStreamingResponse:
    def __init__(self, settings: AsyncSettings) -> None:
        self._settings = settings

        self.zero_trust_accounts_get_device_settings_for_zero_trust_account = async_to_streamed_response_wrapper(
            settings.zero_trust_accounts_get_device_settings_for_zero_trust_account,
        )
        self.zero_trust_accounts_update_device_settings_for_the_zero_trust_account = async_to_streamed_response_wrapper(
            settings.zero_trust_accounts_update_device_settings_for_the_zero_trust_account,
        )
