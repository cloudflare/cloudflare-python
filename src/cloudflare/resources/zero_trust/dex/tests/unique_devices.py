# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.zero_trust.dex.tests.unique_devices import UniqueDevices

from ....._wrappers import ResultWrapper

from ....._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type, List

from ....._base_client import make_request_options

from ....._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .....types.zero_trust.dex.tests import unique_device_list_params
from typing import cast
from typing import cast

__all__ = ["UniqueDevicesResource", "AsyncUniqueDevicesResource"]


class UniqueDevicesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UniqueDevicesResourceWithRawResponse:
        return UniqueDevicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UniqueDevicesResourceWithStreamingResponse:
        return UniqueDevicesResourceWithStreamingResponse(self)

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
    ) -> Optional[UniqueDevices]:
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
                post_parser=ResultWrapper[Optional[UniqueDevices]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UniqueDevices]], ResultWrapper[UniqueDevices]),
        )


class AsyncUniqueDevicesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUniqueDevicesResourceWithRawResponse:
        return AsyncUniqueDevicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUniqueDevicesResourceWithStreamingResponse:
        return AsyncUniqueDevicesResourceWithStreamingResponse(self)

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
    ) -> Optional[UniqueDevices]:
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
                post_parser=ResultWrapper[Optional[UniqueDevices]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UniqueDevices]], ResultWrapper[UniqueDevices]),
        )


class UniqueDevicesResourceWithRawResponse:
    def __init__(self, unique_devices: UniqueDevicesResource) -> None:
        self._unique_devices = unique_devices

        self.list = to_raw_response_wrapper(
            unique_devices.list,
        )


class AsyncUniqueDevicesResourceWithRawResponse:
    def __init__(self, unique_devices: AsyncUniqueDevicesResource) -> None:
        self._unique_devices = unique_devices

        self.list = async_to_raw_response_wrapper(
            unique_devices.list,
        )


class UniqueDevicesResourceWithStreamingResponse:
    def __init__(self, unique_devices: UniqueDevicesResource) -> None:
        self._unique_devices = unique_devices

        self.list = to_streamed_response_wrapper(
            unique_devices.list,
        )


class AsyncUniqueDevicesResourceWithStreamingResponse:
    def __init__(self, unique_devices: AsyncUniqueDevicesResource) -> None:
        self._unique_devices = unique_devices

        self.list = async_to_streamed_response_wrapper(
            unique_devices.list,
        )
