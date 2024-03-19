# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, cast

import httpx

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
from ....._base_client import (
    make_request_options,
)
from .....types.zero_trust.dex.tests import DigitalExperienceMonitoringUniqueDevices, unique_device_list_params

__all__ = ["UniqueDevices", "AsyncUniqueDevices"]


class UniqueDevices(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UniqueDevicesWithRawResponse:
        return UniqueDevicesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UniqueDevicesWithStreamingResponse:
        return UniqueDevicesWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        device_id: List[str] | NotGiven = NOT_GIVEN,
        test_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DigitalExperienceMonitoringUniqueDevices:
        """
        Returns unique count of devices that have run synthetic application monitoring
        tests in the past 7 days.

        Args:
          device_id: Optionally filter result stats to a specific device(s). Cannot be used in
              combination with colo param.

          test_name: Optionally filter results by test name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/dex/tests/unique-devices",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "device_id": device_id,
                        "test_name": test_name,
                    },
                    unique_device_list_params.UniqueDeviceListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[DigitalExperienceMonitoringUniqueDevices], ResultWrapper[DigitalExperienceMonitoringUniqueDevices]
            ),
        )


class AsyncUniqueDevices(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUniqueDevicesWithRawResponse:
        return AsyncUniqueDevicesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUniqueDevicesWithStreamingResponse:
        return AsyncUniqueDevicesWithStreamingResponse(self)

    async def list(
        self,
        *,
        account_id: str,
        device_id: List[str] | NotGiven = NOT_GIVEN,
        test_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DigitalExperienceMonitoringUniqueDevices:
        """
        Returns unique count of devices that have run synthetic application monitoring
        tests in the past 7 days.

        Args:
          device_id: Optionally filter result stats to a specific device(s). Cannot be used in
              combination with colo param.

          test_name: Optionally filter results by test name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/dex/tests/unique-devices",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "device_id": device_id,
                        "test_name": test_name,
                    },
                    unique_device_list_params.UniqueDeviceListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[DigitalExperienceMonitoringUniqueDevices], ResultWrapper[DigitalExperienceMonitoringUniqueDevices]
            ),
        )


class UniqueDevicesWithRawResponse:
    def __init__(self, unique_devices: UniqueDevices) -> None:
        self._unique_devices = unique_devices

        self.list = to_raw_response_wrapper(
            unique_devices.list,
        )


class AsyncUniqueDevicesWithRawResponse:
    def __init__(self, unique_devices: AsyncUniqueDevices) -> None:
        self._unique_devices = unique_devices

        self.list = async_to_raw_response_wrapper(
            unique_devices.list,
        )


class UniqueDevicesWithStreamingResponse:
    def __init__(self, unique_devices: UniqueDevices) -> None:
        self._unique_devices = unique_devices

        self.list = to_streamed_response_wrapper(
            unique_devices.list,
        )


class AsyncUniqueDevicesWithStreamingResponse:
    def __init__(self, unique_devices: AsyncUniqueDevices) -> None:
        self._unique_devices = unique_devices

        self.list = async_to_streamed_response_wrapper(
            unique_devices.list,
        )
