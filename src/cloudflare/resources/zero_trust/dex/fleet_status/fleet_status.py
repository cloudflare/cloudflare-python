# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from .devices import (
    Devices,
    AsyncDevices,
    DevicesWithRawResponse,
    AsyncDevicesWithRawResponse,
    DevicesWithStreamingResponse,
    AsyncDevicesWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from .....types.zero_trust.dex import FleetStatusLiveResponse, fleet_status_live_params, fleet_status_over_time_params

__all__ = ["FleetStatus", "AsyncFleetStatus"]


class FleetStatus(SyncAPIResource):
    @cached_property
    def devices(self) -> Devices:
        return Devices(self._client)

    @cached_property
    def with_raw_response(self) -> FleetStatusWithRawResponse:
        return FleetStatusWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FleetStatusWithStreamingResponse:
        return FleetStatusWithStreamingResponse(self)

    def live(
        self,
        *,
        account_id: str,
        since_minutes: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FleetStatusLiveResponse:
        """
        List details for live (up to 60 minutes) devices using WARP

        Args:
          since_minutes: Number of minutes before current time

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/dex/fleet-status/live",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"since_minutes": since_minutes}, fleet_status_live_params.FleetStatusLiveParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[FleetStatusLiveResponse], ResultWrapper[FleetStatusLiveResponse]),
        )

    def over_time(
        self,
        *,
        account_id: str,
        time_end: str,
        time_start: str,
        colo: str | NotGiven = NOT_GIVEN,
        device_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        List details for devices using WARP, up to 7 days

        Args:
          time_end: Timestamp in ISO format

          time_start: Timestamp in ISO format

          colo: Cloudflare colo

          device_id: Device-specific ID, given as UUID v4

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/accounts/{account_id}/dex/fleet-status/over-time",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "time_end": time_end,
                        "time_start": time_start,
                        "colo": colo,
                        "device_id": device_id,
                    },
                    fleet_status_over_time_params.FleetStatusOverTimeParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncFleetStatus(AsyncAPIResource):
    @cached_property
    def devices(self) -> AsyncDevices:
        return AsyncDevices(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFleetStatusWithRawResponse:
        return AsyncFleetStatusWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFleetStatusWithStreamingResponse:
        return AsyncFleetStatusWithStreamingResponse(self)

    async def live(
        self,
        *,
        account_id: str,
        since_minutes: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FleetStatusLiveResponse:
        """
        List details for live (up to 60 minutes) devices using WARP

        Args:
          since_minutes: Number of minutes before current time

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/dex/fleet-status/live",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"since_minutes": since_minutes}, fleet_status_live_params.FleetStatusLiveParams
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[FleetStatusLiveResponse], ResultWrapper[FleetStatusLiveResponse]),
        )

    async def over_time(
        self,
        *,
        account_id: str,
        time_end: str,
        time_start: str,
        colo: str | NotGiven = NOT_GIVEN,
        device_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        List details for devices using WARP, up to 7 days

        Args:
          time_end: Timestamp in ISO format

          time_start: Timestamp in ISO format

          colo: Cloudflare colo

          device_id: Device-specific ID, given as UUID v4

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/accounts/{account_id}/dex/fleet-status/over-time",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "time_end": time_end,
                        "time_start": time_start,
                        "colo": colo,
                        "device_id": device_id,
                    },
                    fleet_status_over_time_params.FleetStatusOverTimeParams,
                ),
            ),
            cast_to=NoneType,
        )


class FleetStatusWithRawResponse:
    def __init__(self, fleet_status: FleetStatus) -> None:
        self._fleet_status = fleet_status

        self.live = to_raw_response_wrapper(
            fleet_status.live,
        )
        self.over_time = to_raw_response_wrapper(
            fleet_status.over_time,
        )

    @cached_property
    def devices(self) -> DevicesWithRawResponse:
        return DevicesWithRawResponse(self._fleet_status.devices)


class AsyncFleetStatusWithRawResponse:
    def __init__(self, fleet_status: AsyncFleetStatus) -> None:
        self._fleet_status = fleet_status

        self.live = async_to_raw_response_wrapper(
            fleet_status.live,
        )
        self.over_time = async_to_raw_response_wrapper(
            fleet_status.over_time,
        )

    @cached_property
    def devices(self) -> AsyncDevicesWithRawResponse:
        return AsyncDevicesWithRawResponse(self._fleet_status.devices)


class FleetStatusWithStreamingResponse:
    def __init__(self, fleet_status: FleetStatus) -> None:
        self._fleet_status = fleet_status

        self.live = to_streamed_response_wrapper(
            fleet_status.live,
        )
        self.over_time = to_streamed_response_wrapper(
            fleet_status.over_time,
        )

    @cached_property
    def devices(self) -> DevicesWithStreamingResponse:
        return DevicesWithStreamingResponse(self._fleet_status.devices)


class AsyncFleetStatusWithStreamingResponse:
    def __init__(self, fleet_status: AsyncFleetStatus) -> None:
        self._fleet_status = fleet_status

        self.live = async_to_streamed_response_wrapper(
            fleet_status.live,
        )
        self.over_time = async_to_streamed_response_wrapper(
            fleet_status.over_time,
        )

    @cached_property
    def devices(self) -> AsyncDevicesWithStreamingResponse:
        return AsyncDevicesWithStreamingResponse(self._fleet_status.devices)
