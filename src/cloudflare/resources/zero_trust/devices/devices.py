# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Optional, cast

import httpx

from .revoke import (
    Revoke,
    AsyncRevoke,
    RevokeWithRawResponse,
    AsyncRevokeWithRawResponse,
    RevokeWithStreamingResponse,
    AsyncRevokeWithStreamingResponse,
)
from .posture import (
    Posture,
    AsyncPosture,
    PostureWithRawResponse,
    AsyncPostureWithRawResponse,
    PostureWithStreamingResponse,
    AsyncPostureWithStreamingResponse,
)
from .networks import (
    Networks,
    AsyncNetworks,
    NetworksWithRawResponse,
    AsyncNetworksWithRawResponse,
    NetworksWithStreamingResponse,
    AsyncNetworksWithStreamingResponse,
)
from .policies import (
    Policies,
    AsyncPolicies,
    PoliciesWithRawResponse,
    AsyncPoliciesWithRawResponse,
    PoliciesWithStreamingResponse,
    AsyncPoliciesWithStreamingResponse,
)
from .settings import (
    Settings,
    AsyncSettings,
    SettingsWithRawResponse,
    AsyncSettingsWithRawResponse,
    SettingsWithStreamingResponse,
    AsyncSettingsWithStreamingResponse,
)
from .unrevoke import (
    Unrevoke,
    AsyncUnrevoke,
    UnrevokeWithRawResponse,
    AsyncUnrevokeWithRawResponse,
    UnrevokeWithStreamingResponse,
    AsyncUnrevokeWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .dex_tests import (
    DEXTests,
    AsyncDEXTests,
    DEXTestsWithRawResponse,
    AsyncDEXTestsWithRawResponse,
    DEXTestsWithStreamingResponse,
    AsyncDEXTestsWithStreamingResponse,
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
from .override_codes import (
    OverrideCodes,
    AsyncOverrideCodes,
    OverrideCodesWithRawResponse,
    AsyncOverrideCodesWithRawResponse,
    OverrideCodesWithStreamingResponse,
    AsyncOverrideCodesWithStreamingResponse,
)
from ...._base_client import (
    make_request_options,
)
from .posture.posture import Posture, AsyncPosture
from .policies.policies import Policies, AsyncPolicies
from ....types.zero_trust import DeviceGetResponse, DeviceListResponse

__all__ = ["Devices", "AsyncDevices"]


class Devices(SyncAPIResource):
    @cached_property
    def dex_tests(self) -> DEXTests:
        return DEXTests(self._client)

    @cached_property
    def networks(self) -> Networks:
        return Networks(self._client)

    @cached_property
    def policies(self) -> Policies:
        return Policies(self._client)

    @cached_property
    def posture(self) -> Posture:
        return Posture(self._client)

    @cached_property
    def revoke(self) -> Revoke:
        return Revoke(self._client)

    @cached_property
    def settings(self) -> Settings:
        return Settings(self._client)

    @cached_property
    def unrevoke(self) -> Unrevoke:
        return Unrevoke(self._client)

    @cached_property
    def override_codes(self) -> OverrideCodes:
        return OverrideCodes(self._client)

    @cached_property
    def with_raw_response(self) -> DevicesWithRawResponse:
        return DevicesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DevicesWithStreamingResponse:
        return DevicesWithStreamingResponse(self)

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
    ) -> Optional[DeviceListResponse]:
        """
        Fetches a list of enrolled devices.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/devices",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[DeviceListResponse]], ResultWrapper[DeviceListResponse]),
        )

    def get(
        self,
        device_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DeviceGetResponse]:
        """
        Fetches details for a single device.

        Args:
          device_id: Device ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return cast(
            Optional[DeviceGetResponse],
            self._get(
                f"/accounts/{account_id}/devices/{device_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[DeviceGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncDevices(AsyncAPIResource):
    @cached_property
    def dex_tests(self) -> AsyncDEXTests:
        return AsyncDEXTests(self._client)

    @cached_property
    def networks(self) -> AsyncNetworks:
        return AsyncNetworks(self._client)

    @cached_property
    def policies(self) -> AsyncPolicies:
        return AsyncPolicies(self._client)

    @cached_property
    def posture(self) -> AsyncPosture:
        return AsyncPosture(self._client)

    @cached_property
    def revoke(self) -> AsyncRevoke:
        return AsyncRevoke(self._client)

    @cached_property
    def settings(self) -> AsyncSettings:
        return AsyncSettings(self._client)

    @cached_property
    def unrevoke(self) -> AsyncUnrevoke:
        return AsyncUnrevoke(self._client)

    @cached_property
    def override_codes(self) -> AsyncOverrideCodes:
        return AsyncOverrideCodes(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDevicesWithRawResponse:
        return AsyncDevicesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDevicesWithStreamingResponse:
        return AsyncDevicesWithStreamingResponse(self)

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
    ) -> Optional[DeviceListResponse]:
        """
        Fetches a list of enrolled devices.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/devices",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[DeviceListResponse]], ResultWrapper[DeviceListResponse]),
        )

    async def get(
        self,
        device_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DeviceGetResponse]:
        """
        Fetches details for a single device.

        Args:
          device_id: Device ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return cast(
            Optional[DeviceGetResponse],
            await self._get(
                f"/accounts/{account_id}/devices/{device_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[DeviceGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class DevicesWithRawResponse:
    def __init__(self, devices: Devices) -> None:
        self._devices = devices

        self.list = to_raw_response_wrapper(
            devices.list,
        )
        self.get = to_raw_response_wrapper(
            devices.get,
        )

    @cached_property
    def dex_tests(self) -> DEXTestsWithRawResponse:
        return DEXTestsWithRawResponse(self._devices.dex_tests)

    @cached_property
    def networks(self) -> NetworksWithRawResponse:
        return NetworksWithRawResponse(self._devices.networks)

    @cached_property
    def policies(self) -> PoliciesWithRawResponse:
        return PoliciesWithRawResponse(self._devices.policies)

    @cached_property
    def posture(self) -> PostureWithRawResponse:
        return PostureWithRawResponse(self._devices.posture)

    @cached_property
    def revoke(self) -> RevokeWithRawResponse:
        return RevokeWithRawResponse(self._devices.revoke)

    @cached_property
    def settings(self) -> SettingsWithRawResponse:
        return SettingsWithRawResponse(self._devices.settings)

    @cached_property
    def unrevoke(self) -> UnrevokeWithRawResponse:
        return UnrevokeWithRawResponse(self._devices.unrevoke)

    @cached_property
    def override_codes(self) -> OverrideCodesWithRawResponse:
        return OverrideCodesWithRawResponse(self._devices.override_codes)


class AsyncDevicesWithRawResponse:
    def __init__(self, devices: AsyncDevices) -> None:
        self._devices = devices

        self.list = async_to_raw_response_wrapper(
            devices.list,
        )
        self.get = async_to_raw_response_wrapper(
            devices.get,
        )

    @cached_property
    def dex_tests(self) -> AsyncDEXTestsWithRawResponse:
        return AsyncDEXTestsWithRawResponse(self._devices.dex_tests)

    @cached_property
    def networks(self) -> AsyncNetworksWithRawResponse:
        return AsyncNetworksWithRawResponse(self._devices.networks)

    @cached_property
    def policies(self) -> AsyncPoliciesWithRawResponse:
        return AsyncPoliciesWithRawResponse(self._devices.policies)

    @cached_property
    def posture(self) -> AsyncPostureWithRawResponse:
        return AsyncPostureWithRawResponse(self._devices.posture)

    @cached_property
    def revoke(self) -> AsyncRevokeWithRawResponse:
        return AsyncRevokeWithRawResponse(self._devices.revoke)

    @cached_property
    def settings(self) -> AsyncSettingsWithRawResponse:
        return AsyncSettingsWithRawResponse(self._devices.settings)

    @cached_property
    def unrevoke(self) -> AsyncUnrevokeWithRawResponse:
        return AsyncUnrevokeWithRawResponse(self._devices.unrevoke)

    @cached_property
    def override_codes(self) -> AsyncOverrideCodesWithRawResponse:
        return AsyncOverrideCodesWithRawResponse(self._devices.override_codes)


class DevicesWithStreamingResponse:
    def __init__(self, devices: Devices) -> None:
        self._devices = devices

        self.list = to_streamed_response_wrapper(
            devices.list,
        )
        self.get = to_streamed_response_wrapper(
            devices.get,
        )

    @cached_property
    def dex_tests(self) -> DEXTestsWithStreamingResponse:
        return DEXTestsWithStreamingResponse(self._devices.dex_tests)

    @cached_property
    def networks(self) -> NetworksWithStreamingResponse:
        return NetworksWithStreamingResponse(self._devices.networks)

    @cached_property
    def policies(self) -> PoliciesWithStreamingResponse:
        return PoliciesWithStreamingResponse(self._devices.policies)

    @cached_property
    def posture(self) -> PostureWithStreamingResponse:
        return PostureWithStreamingResponse(self._devices.posture)

    @cached_property
    def revoke(self) -> RevokeWithStreamingResponse:
        return RevokeWithStreamingResponse(self._devices.revoke)

    @cached_property
    def settings(self) -> SettingsWithStreamingResponse:
        return SettingsWithStreamingResponse(self._devices.settings)

    @cached_property
    def unrevoke(self) -> UnrevokeWithStreamingResponse:
        return UnrevokeWithStreamingResponse(self._devices.unrevoke)

    @cached_property
    def override_codes(self) -> OverrideCodesWithStreamingResponse:
        return OverrideCodesWithStreamingResponse(self._devices.override_codes)


class AsyncDevicesWithStreamingResponse:
    def __init__(self, devices: AsyncDevices) -> None:
        self._devices = devices

        self.list = async_to_streamed_response_wrapper(
            devices.list,
        )
        self.get = async_to_streamed_response_wrapper(
            devices.get,
        )

    @cached_property
    def dex_tests(self) -> AsyncDEXTestsWithStreamingResponse:
        return AsyncDEXTestsWithStreamingResponse(self._devices.dex_tests)

    @cached_property
    def networks(self) -> AsyncNetworksWithStreamingResponse:
        return AsyncNetworksWithStreamingResponse(self._devices.networks)

    @cached_property
    def policies(self) -> AsyncPoliciesWithStreamingResponse:
        return AsyncPoliciesWithStreamingResponse(self._devices.policies)

    @cached_property
    def posture(self) -> AsyncPostureWithStreamingResponse:
        return AsyncPostureWithStreamingResponse(self._devices.posture)

    @cached_property
    def revoke(self) -> AsyncRevokeWithStreamingResponse:
        return AsyncRevokeWithStreamingResponse(self._devices.revoke)

    @cached_property
    def settings(self) -> AsyncSettingsWithStreamingResponse:
        return AsyncSettingsWithStreamingResponse(self._devices.settings)

    @cached_property
    def unrevoke(self) -> AsyncUnrevokeWithStreamingResponse:
        return AsyncUnrevokeWithStreamingResponse(self._devices.unrevoke)

    @cached_property
    def override_codes(self) -> AsyncOverrideCodesWithStreamingResponse:
        return AsyncOverrideCodesWithStreamingResponse(self._devices.override_codes)
