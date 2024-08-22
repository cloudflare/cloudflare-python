# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .dex_tests import DEXTestsResource, AsyncDEXTestsResource

from ...._compat import cached_property

from .networks import NetworksResource, AsyncNetworksResource

from .policies.policies import PoliciesResource, AsyncPoliciesResource

from .posture.posture import PostureResource, AsyncPostureResource

from .revoke import RevokeResource, AsyncRevokeResource

from .settings import SettingsResource, AsyncSettingsResource

from .unrevoke import UnrevokeResource, AsyncUnrevokeResource

from .override_codes import OverrideCodesResource, AsyncOverrideCodesResource

from ....types.zero_trust.device import Device

from ....pagination import SyncSinglePage, AsyncSinglePage

from ...._base_client import make_request_options, AsyncPaginator

from ....types.zero_trust.device_get_response import DeviceGetResponse

from ...._wrappers import ResultWrapper

from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from .dex_tests import DEXTestsResource, AsyncDEXTestsResource, DEXTestsResourceWithRawResponse, AsyncDEXTestsResourceWithRawResponse, DEXTestsResourceWithStreamingResponse, AsyncDEXTestsResourceWithStreamingResponse
from .networks import NetworksResource, AsyncNetworksResource, NetworksResourceWithRawResponse, AsyncNetworksResourceWithRawResponse, NetworksResourceWithStreamingResponse, AsyncNetworksResourceWithStreamingResponse
from .policies import PoliciesResource, AsyncPoliciesResource, PoliciesResourceWithRawResponse, AsyncPoliciesResourceWithRawResponse, PoliciesResourceWithStreamingResponse, AsyncPoliciesResourceWithStreamingResponse
from .posture import PostureResource, AsyncPostureResource, PostureResourceWithRawResponse, AsyncPostureResourceWithRawResponse, PostureResourceWithStreamingResponse, AsyncPostureResourceWithStreamingResponse
from .revoke import RevokeResource, AsyncRevokeResource, RevokeResourceWithRawResponse, AsyncRevokeResourceWithRawResponse, RevokeResourceWithStreamingResponse, AsyncRevokeResourceWithStreamingResponse
from .settings import SettingsResource, AsyncSettingsResource, SettingsResourceWithRawResponse, AsyncSettingsResourceWithRawResponse, SettingsResourceWithStreamingResponse, AsyncSettingsResourceWithStreamingResponse
from .unrevoke import UnrevokeResource, AsyncUnrevokeResource, UnrevokeResourceWithRawResponse, AsyncUnrevokeResourceWithRawResponse, UnrevokeResourceWithStreamingResponse, AsyncUnrevokeResourceWithStreamingResponse
from .override_codes import OverrideCodesResource, AsyncOverrideCodesResource, OverrideCodesResourceWithRawResponse, AsyncOverrideCodesResourceWithRawResponse, OverrideCodesResourceWithStreamingResponse, AsyncOverrideCodesResourceWithStreamingResponse
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["DevicesResource", "AsyncDevicesResource"]

class DevicesResource(SyncAPIResource):
    @cached_property
    def dex_tests(self) -> DEXTestsResource:
        return DEXTestsResource(self._client)

    @cached_property
    def networks(self) -> NetworksResource:
        return NetworksResource(self._client)

    @cached_property
    def policies(self) -> PoliciesResource:
        return PoliciesResource(self._client)

    @cached_property
    def posture(self) -> PostureResource:
        return PostureResource(self._client)

    @cached_property
    def revoke(self) -> RevokeResource:
        return RevokeResource(self._client)

    @cached_property
    def settings(self) -> SettingsResource:
        return SettingsResource(self._client)

    @cached_property
    def unrevoke(self) -> UnrevokeResource:
        return UnrevokeResource(self._client)

    @cached_property
    def override_codes(self) -> OverrideCodesResource:
        return OverrideCodesResource(self._client)

    @cached_property
    def with_raw_response(self) -> DevicesResourceWithRawResponse:
        return DevicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DevicesResourceWithStreamingResponse:
        return DevicesResourceWithStreamingResponse(self)

    def list(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> SyncSinglePage[Device]:
        """
        Fetches a list of enrolled devices.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get_api_list(
            f"/accounts/{account_id}/devices",
            page = SyncSinglePage[Device],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            model=Device,
        )

    def get(self,
    device_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> DeviceGetResponse:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not device_id:
          raise ValueError(
            f'Expected a non-empty value for `device_id` but received {device_id!r}'
          )
        return cast(DeviceGetResponse, self._get(
            f"/accounts/{account_id}/devices/{device_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[DeviceGetResponse]._unwrapper),
            cast_to=cast(Any, ResultWrapper[DeviceGetResponse]),  # Union types cannot be passed in as arguments in the type system
        ))

class AsyncDevicesResource(AsyncAPIResource):
    @cached_property
    def dex_tests(self) -> AsyncDEXTestsResource:
        return AsyncDEXTestsResource(self._client)

    @cached_property
    def networks(self) -> AsyncNetworksResource:
        return AsyncNetworksResource(self._client)

    @cached_property
    def policies(self) -> AsyncPoliciesResource:
        return AsyncPoliciesResource(self._client)

    @cached_property
    def posture(self) -> AsyncPostureResource:
        return AsyncPostureResource(self._client)

    @cached_property
    def revoke(self) -> AsyncRevokeResource:
        return AsyncRevokeResource(self._client)

    @cached_property
    def settings(self) -> AsyncSettingsResource:
        return AsyncSettingsResource(self._client)

    @cached_property
    def unrevoke(self) -> AsyncUnrevokeResource:
        return AsyncUnrevokeResource(self._client)

    @cached_property
    def override_codes(self) -> AsyncOverrideCodesResource:
        return AsyncOverrideCodesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDevicesResourceWithRawResponse:
        return AsyncDevicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDevicesResourceWithStreamingResponse:
        return AsyncDevicesResourceWithStreamingResponse(self)

    def list(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AsyncPaginator[Device, AsyncSinglePage[Device]]:
        """
        Fetches a list of enrolled devices.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get_api_list(
            f"/accounts/{account_id}/devices",
            page = AsyncSinglePage[Device],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            model=Device,
        )

    async def get(self,
    device_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> DeviceGetResponse:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not device_id:
          raise ValueError(
            f'Expected a non-empty value for `device_id` but received {device_id!r}'
          )
        return cast(DeviceGetResponse, await self._get(
            f"/accounts/{account_id}/devices/{device_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[DeviceGetResponse]._unwrapper),
            cast_to=cast(Any, ResultWrapper[DeviceGetResponse]),  # Union types cannot be passed in as arguments in the type system
        ))

class DevicesResourceWithRawResponse:
    def __init__(self, devices: DevicesResource) -> None:
        self._devices = devices

        self.list = to_raw_response_wrapper(
            devices.list,
        )
        self.get = to_raw_response_wrapper(
            devices.get,
        )

    @cached_property
    def dex_tests(self) -> DEXTestsResourceWithRawResponse:
        return DEXTestsResourceWithRawResponse(self._devices.dex_tests)

    @cached_property
    def networks(self) -> NetworksResourceWithRawResponse:
        return NetworksResourceWithRawResponse(self._devices.networks)

    @cached_property
    def policies(self) -> PoliciesResourceWithRawResponse:
        return PoliciesResourceWithRawResponse(self._devices.policies)

    @cached_property
    def posture(self) -> PostureResourceWithRawResponse:
        return PostureResourceWithRawResponse(self._devices.posture)

    @cached_property
    def revoke(self) -> RevokeResourceWithRawResponse:
        return RevokeResourceWithRawResponse(self._devices.revoke)

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self._devices.settings)

    @cached_property
    def unrevoke(self) -> UnrevokeResourceWithRawResponse:
        return UnrevokeResourceWithRawResponse(self._devices.unrevoke)

    @cached_property
    def override_codes(self) -> OverrideCodesResourceWithRawResponse:
        return OverrideCodesResourceWithRawResponse(self._devices.override_codes)

class AsyncDevicesResourceWithRawResponse:
    def __init__(self, devices: AsyncDevicesResource) -> None:
        self._devices = devices

        self.list = async_to_raw_response_wrapper(
            devices.list,
        )
        self.get = async_to_raw_response_wrapper(
            devices.get,
        )

    @cached_property
    def dex_tests(self) -> AsyncDEXTestsResourceWithRawResponse:
        return AsyncDEXTestsResourceWithRawResponse(self._devices.dex_tests)

    @cached_property
    def networks(self) -> AsyncNetworksResourceWithRawResponse:
        return AsyncNetworksResourceWithRawResponse(self._devices.networks)

    @cached_property
    def policies(self) -> AsyncPoliciesResourceWithRawResponse:
        return AsyncPoliciesResourceWithRawResponse(self._devices.policies)

    @cached_property
    def posture(self) -> AsyncPostureResourceWithRawResponse:
        return AsyncPostureResourceWithRawResponse(self._devices.posture)

    @cached_property
    def revoke(self) -> AsyncRevokeResourceWithRawResponse:
        return AsyncRevokeResourceWithRawResponse(self._devices.revoke)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self._devices.settings)

    @cached_property
    def unrevoke(self) -> AsyncUnrevokeResourceWithRawResponse:
        return AsyncUnrevokeResourceWithRawResponse(self._devices.unrevoke)

    @cached_property
    def override_codes(self) -> AsyncOverrideCodesResourceWithRawResponse:
        return AsyncOverrideCodesResourceWithRawResponse(self._devices.override_codes)

class DevicesResourceWithStreamingResponse:
    def __init__(self, devices: DevicesResource) -> None:
        self._devices = devices

        self.list = to_streamed_response_wrapper(
            devices.list,
        )
        self.get = to_streamed_response_wrapper(
            devices.get,
        )

    @cached_property
    def dex_tests(self) -> DEXTestsResourceWithStreamingResponse:
        return DEXTestsResourceWithStreamingResponse(self._devices.dex_tests)

    @cached_property
    def networks(self) -> NetworksResourceWithStreamingResponse:
        return NetworksResourceWithStreamingResponse(self._devices.networks)

    @cached_property
    def policies(self) -> PoliciesResourceWithStreamingResponse:
        return PoliciesResourceWithStreamingResponse(self._devices.policies)

    @cached_property
    def posture(self) -> PostureResourceWithStreamingResponse:
        return PostureResourceWithStreamingResponse(self._devices.posture)

    @cached_property
    def revoke(self) -> RevokeResourceWithStreamingResponse:
        return RevokeResourceWithStreamingResponse(self._devices.revoke)

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self._devices.settings)

    @cached_property
    def unrevoke(self) -> UnrevokeResourceWithStreamingResponse:
        return UnrevokeResourceWithStreamingResponse(self._devices.unrevoke)

    @cached_property
    def override_codes(self) -> OverrideCodesResourceWithStreamingResponse:
        return OverrideCodesResourceWithStreamingResponse(self._devices.override_codes)

class AsyncDevicesResourceWithStreamingResponse:
    def __init__(self, devices: AsyncDevicesResource) -> None:
        self._devices = devices

        self.list = async_to_streamed_response_wrapper(
            devices.list,
        )
        self.get = async_to_streamed_response_wrapper(
            devices.get,
        )

    @cached_property
    def dex_tests(self) -> AsyncDEXTestsResourceWithStreamingResponse:
        return AsyncDEXTestsResourceWithStreamingResponse(self._devices.dex_tests)

    @cached_property
    def networks(self) -> AsyncNetworksResourceWithStreamingResponse:
        return AsyncNetworksResourceWithStreamingResponse(self._devices.networks)

    @cached_property
    def policies(self) -> AsyncPoliciesResourceWithStreamingResponse:
        return AsyncPoliciesResourceWithStreamingResponse(self._devices.policies)

    @cached_property
    def posture(self) -> AsyncPostureResourceWithStreamingResponse:
        return AsyncPostureResourceWithStreamingResponse(self._devices.posture)

    @cached_property
    def revoke(self) -> AsyncRevokeResourceWithStreamingResponse:
        return AsyncRevokeResourceWithStreamingResponse(self._devices.revoke)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self._devices.settings)

    @cached_property
    def unrevoke(self) -> AsyncUnrevokeResourceWithStreamingResponse:
        return AsyncUnrevokeResourceWithStreamingResponse(self._devices.unrevoke)

    @cached_property
    def override_codes(self) -> AsyncOverrideCodesResourceWithStreamingResponse:
        return AsyncOverrideCodesResourceWithStreamingResponse(self._devices.override_codes)