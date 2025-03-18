# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.zero_trust.devices import fleet_status_get_params
from ....types.zero_trust.devices.fleet_status_get_response import FleetStatusGetResponse

__all__ = ["FleetStatusResource", "AsyncFleetStatusResource"]


class FleetStatusResource(SyncAPIResource):
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

    def get(
        self,
        device_id: str,
        *,
        account_id: str,
        since_minutes: float,
        colo: str | NotGiven = NOT_GIVEN,
        time_now: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FleetStatusGetResponse:
        """
        Get the live status of a latest device given device_id from the device_state
        table

        Args:
          device_id: Device-specific ID, given as UUID v4

          since_minutes: Number of minutes before current time

          colo: List of data centers to filter results

          time_now: Number of minutes before current time

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return self._get(
            f"/accounts/{account_id}/dex/devices/{device_id}/fleet-status/live",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "since_minutes": since_minutes,
                        "colo": colo,
                        "time_now": time_now,
                    },
                    fleet_status_get_params.FleetStatusGetParams,
                ),
            ),
            cast_to=FleetStatusGetResponse,
        )


class AsyncFleetStatusResource(AsyncAPIResource):
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

    async def get(
        self,
        device_id: str,
        *,
        account_id: str,
        since_minutes: float,
        colo: str | NotGiven = NOT_GIVEN,
        time_now: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FleetStatusGetResponse:
        """
        Get the live status of a latest device given device_id from the device_state
        table

        Args:
          device_id: Device-specific ID, given as UUID v4

          since_minutes: Number of minutes before current time

          colo: List of data centers to filter results

          time_now: Number of minutes before current time

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return await self._get(
            f"/accounts/{account_id}/dex/devices/{device_id}/fleet-status/live",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "since_minutes": since_minutes,
                        "colo": colo,
                        "time_now": time_now,
                    },
                    fleet_status_get_params.FleetStatusGetParams,
                ),
            ),
            cast_to=FleetStatusGetResponse,
        )


class FleetStatusResourceWithRawResponse:
    def __init__(self, fleet_status: FleetStatusResource) -> None:
        self._fleet_status = fleet_status

        self.get = to_raw_response_wrapper(
            fleet_status.get,
        )


class AsyncFleetStatusResourceWithRawResponse:
    def __init__(self, fleet_status: AsyncFleetStatusResource) -> None:
        self._fleet_status = fleet_status

        self.get = async_to_raw_response_wrapper(
            fleet_status.get,
        )


class FleetStatusResourceWithStreamingResponse:
    def __init__(self, fleet_status: FleetStatusResource) -> None:
        self._fleet_status = fleet_status

        self.get = to_streamed_response_wrapper(
            fleet_status.get,
        )


class AsyncFleetStatusResourceWithStreamingResponse:
    def __init__(self, fleet_status: AsyncFleetStatusResource) -> None:
        self._fleet_status = fleet_status

        self.get = async_to_streamed_response_wrapper(
            fleet_status.get,
        )
