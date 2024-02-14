# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.dex.fleet_status import DeviceListResponse

from typing import Type, Optional

from typing_extensions import Literal

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
from ....types.dex.fleet_status import device_list_params
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Devices", "AsyncDevices"]


class Devices(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DevicesWithRawResponse:
        return DevicesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DevicesWithStreamingResponse:
        return DevicesWithStreamingResponse(self)

    def list(
        self,
        account_id: str,
        *,
        page: float,
        per_page: float,
        time_end: str,
        time_start: str,
        colo: str | NotGiven = NOT_GIVEN,
        device_id: str | NotGiven = NOT_GIVEN,
        mode: str | NotGiven = NOT_GIVEN,
        platform: str | NotGiven = NOT_GIVEN,
        sort_by: Literal["colo", "device_id", "mode", "platform", "status", "timestamp", "version"]
        | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DeviceListResponse]:
        """
        List details for devices using WARP

        Args:
          page: Page number of paginated results

          per_page: Number of items per page

          time_end: Timestamp in ISO format

          time_start: Timestamp in ISO format

          colo: Cloudflare colo

          device_id: Device-specific ID, given as UUID v4

          mode: The mode under which the WARP client is run

          platform: Operating system

          sort_by: Dimension to sort results by

          status: Network status

          version: WARP client version

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/dex/fleet-status/devices",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "time_end": time_end,
                        "time_start": time_start,
                        "colo": colo,
                        "device_id": device_id,
                        "mode": mode,
                        "platform": platform,
                        "sort_by": sort_by,
                        "status": status,
                        "version": version,
                    },
                    device_list_params.DeviceListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[DeviceListResponse]], ResultWrapper[DeviceListResponse]),
        )


class AsyncDevices(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDevicesWithRawResponse:
        return AsyncDevicesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDevicesWithStreamingResponse:
        return AsyncDevicesWithStreamingResponse(self)

    async def list(
        self,
        account_id: str,
        *,
        page: float,
        per_page: float,
        time_end: str,
        time_start: str,
        colo: str | NotGiven = NOT_GIVEN,
        device_id: str | NotGiven = NOT_GIVEN,
        mode: str | NotGiven = NOT_GIVEN,
        platform: str | NotGiven = NOT_GIVEN,
        sort_by: Literal["colo", "device_id", "mode", "platform", "status", "timestamp", "version"]
        | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DeviceListResponse]:
        """
        List details for devices using WARP

        Args:
          page: Page number of paginated results

          per_page: Number of items per page

          time_end: Timestamp in ISO format

          time_start: Timestamp in ISO format

          colo: Cloudflare colo

          device_id: Device-specific ID, given as UUID v4

          mode: The mode under which the WARP client is run

          platform: Operating system

          sort_by: Dimension to sort results by

          status: Network status

          version: WARP client version

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/dex/fleet-status/devices",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "time_end": time_end,
                        "time_start": time_start,
                        "colo": colo,
                        "device_id": device_id,
                        "mode": mode,
                        "platform": platform,
                        "sort_by": sort_by,
                        "status": status,
                        "version": version,
                    },
                    device_list_params.DeviceListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[DeviceListResponse]], ResultWrapper[DeviceListResponse]),
        )


class DevicesWithRawResponse:
    def __init__(self, devices: Devices) -> None:
        self._devices = devices

        self.list = to_raw_response_wrapper(
            devices.list,
        )


class AsyncDevicesWithRawResponse:
    def __init__(self, devices: AsyncDevices) -> None:
        self._devices = devices

        self.list = async_to_raw_response_wrapper(
            devices.list,
        )


class DevicesWithStreamingResponse:
    def __init__(self, devices: Devices) -> None:
        self._devices = devices

        self.list = to_streamed_response_wrapper(
            devices.list,
        )


class AsyncDevicesWithStreamingResponse:
    def __init__(self, devices: AsyncDevices) -> None:
        self._devices = devices

        self.list = async_to_streamed_response_wrapper(
            devices.list,
        )
