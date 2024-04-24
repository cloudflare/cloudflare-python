# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ....._base_client import (
    AsyncPaginator,
    make_request_options,
)
from .....types.zero_trust.dex.fleet_status import device_list_params
from .....types.zero_trust.dex.fleet_status.device_list_response import DeviceListResponse

__all__ = ["DevicesResource", "AsyncDevicesResource"]


class DevicesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DevicesResourceWithRawResponse:
        return DevicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DevicesResourceWithStreamingResponse:
        return DevicesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
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
    ) -> SyncV4PagePaginationArray[DeviceListResponse]:
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
        return self._get_api_list(
            f"/accounts/{account_id}/dex/fleet-status/devices",
            page=SyncV4PagePaginationArray[DeviceListResponse],
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
            ),
            model=DeviceListResponse,
        )


class AsyncDevicesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDevicesResourceWithRawResponse:
        return AsyncDevicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDevicesResourceWithStreamingResponse:
        return AsyncDevicesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
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
    ) -> AsyncPaginator[DeviceListResponse, AsyncV4PagePaginationArray[DeviceListResponse]]:
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
        return self._get_api_list(
            f"/accounts/{account_id}/dex/fleet-status/devices",
            page=AsyncV4PagePaginationArray[DeviceListResponse],
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
            ),
            model=DeviceListResponse,
        )


class DevicesResourceWithRawResponse:
    def __init__(self, devices: DevicesResource) -> None:
        self._devices = devices

        self.list = to_raw_response_wrapper(
            devices.list,
        )


class AsyncDevicesResourceWithRawResponse:
    def __init__(self, devices: AsyncDevicesResource) -> None:
        self._devices = devices

        self.list = async_to_raw_response_wrapper(
            devices.list,
        )


class DevicesResourceWithStreamingResponse:
    def __init__(self, devices: DevicesResource) -> None:
        self._devices = devices

        self.list = to_streamed_response_wrapper(
            devices.list,
        )


class AsyncDevicesResourceWithStreamingResponse:
    def __init__(self, devices: AsyncDevicesResource) -> None:
        self._devices = devices

        self.list = async_to_streamed_response_wrapper(
            devices.list,
        )
