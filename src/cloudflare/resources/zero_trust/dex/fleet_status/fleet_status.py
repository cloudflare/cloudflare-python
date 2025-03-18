# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from .devices import (
    DevicesResource,
    AsyncDevicesResource,
    DevicesResourceWithRawResponse,
    AsyncDevicesResourceWithRawResponse,
    DevicesResourceWithStreamingResponse,
    AsyncDevicesResourceWithStreamingResponse,
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
from ....._base_client import make_request_options
from .....types.zero_trust.dex import fleet_status_live_params, fleet_status_over_time_params
from .....types.zero_trust.dex.fleet_status_live_response import FleetStatusLiveResponse

__all__ = ["FleetStatusResource", "AsyncFleetStatusResource"]


class FleetStatusResource(SyncAPIResource):
    @cached_property
    def devices(self) -> DevicesResource:
        return DevicesResource(self._client)

    @cached_property
    def with_raw_response(self) -> FleetStatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return FleetStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FleetStatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return FleetStatusResourceWithStreamingResponse(self)

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
    ) -> Optional[FleetStatusLiveResponse]:
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
                post_parser=ResultWrapper[Optional[FleetStatusLiveResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FleetStatusLiveResponse]], ResultWrapper[FleetStatusLiveResponse]),
        )

    def over_time(
        self,
        *,
        account_id: str,
        from_: str,
        to: str,
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
          from_: Time range beginning in ISO format

          to: Time range end in ISO format

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
                        "from_": from_,
                        "to": to,
                        "colo": colo,
                        "device_id": device_id,
                    },
                    fleet_status_over_time_params.FleetStatusOverTimeParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncFleetStatusResource(AsyncAPIResource):
    @cached_property
    def devices(self) -> AsyncDevicesResource:
        return AsyncDevicesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFleetStatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFleetStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFleetStatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncFleetStatusResourceWithStreamingResponse(self)

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
    ) -> Optional[FleetStatusLiveResponse]:
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
                post_parser=ResultWrapper[Optional[FleetStatusLiveResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FleetStatusLiveResponse]], ResultWrapper[FleetStatusLiveResponse]),
        )

    async def over_time(
        self,
        *,
        account_id: str,
        from_: str,
        to: str,
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
          from_: Time range beginning in ISO format

          to: Time range end in ISO format

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
                        "from_": from_,
                        "to": to,
                        "colo": colo,
                        "device_id": device_id,
                    },
                    fleet_status_over_time_params.FleetStatusOverTimeParams,
                ),
            ),
            cast_to=NoneType,
        )


class FleetStatusResourceWithRawResponse:
    def __init__(self, fleet_status: FleetStatusResource) -> None:
        self._fleet_status = fleet_status

        self.live = to_raw_response_wrapper(
            fleet_status.live,
        )
        self.over_time = to_raw_response_wrapper(
            fleet_status.over_time,
        )

    @cached_property
    def devices(self) -> DevicesResourceWithRawResponse:
        return DevicesResourceWithRawResponse(self._fleet_status.devices)


class AsyncFleetStatusResourceWithRawResponse:
    def __init__(self, fleet_status: AsyncFleetStatusResource) -> None:
        self._fleet_status = fleet_status

        self.live = async_to_raw_response_wrapper(
            fleet_status.live,
        )
        self.over_time = async_to_raw_response_wrapper(
            fleet_status.over_time,
        )

    @cached_property
    def devices(self) -> AsyncDevicesResourceWithRawResponse:
        return AsyncDevicesResourceWithRawResponse(self._fleet_status.devices)


class FleetStatusResourceWithStreamingResponse:
    def __init__(self, fleet_status: FleetStatusResource) -> None:
        self._fleet_status = fleet_status

        self.live = to_streamed_response_wrapper(
            fleet_status.live,
        )
        self.over_time = to_streamed_response_wrapper(
            fleet_status.over_time,
        )

    @cached_property
    def devices(self) -> DevicesResourceWithStreamingResponse:
        return DevicesResourceWithStreamingResponse(self._fleet_status.devices)


class AsyncFleetStatusResourceWithStreamingResponse:
    def __init__(self, fleet_status: AsyncFleetStatusResource) -> None:
        self._fleet_status = fleet_status

        self.live = async_to_streamed_response_wrapper(
            fleet_status.live,
        )
        self.over_time = async_to_streamed_response_wrapper(
            fleet_status.over_time,
        )

    @cached_property
    def devices(self) -> AsyncDevicesResourceWithStreamingResponse:
        return AsyncDevicesResourceWithStreamingResponse(self._fleet_status.devices)
