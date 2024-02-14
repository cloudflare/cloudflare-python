# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.dex.tests import UniqueDeviceListResponse

from typing import Type, List

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ....types.dex.tests import unique_device_list_params
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast

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
        account_id: str,
        *,
        device_id: List[str] | NotGiven = NOT_GIVEN,
        test_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UniqueDeviceListResponse:
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
            cast_to=cast(Type[UniqueDeviceListResponse], ResultWrapper[UniqueDeviceListResponse]),
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
        account_id: str,
        *,
        device_id: List[str] | NotGiven = NOT_GIVEN,
        test_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UniqueDeviceListResponse:
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
                query=maybe_transform(
                    {
                        "device_id": device_id,
                        "test_name": test_name,
                    },
                    unique_device_list_params.UniqueDeviceListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[UniqueDeviceListResponse], ResultWrapper[UniqueDeviceListResponse]),
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
