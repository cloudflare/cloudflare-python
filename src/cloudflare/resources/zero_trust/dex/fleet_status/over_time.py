# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

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
from ....._base_client import (
    make_request_options,
)
from .....types.zero_trust.dex.fleet_status import over_time_list_params

__all__ = ["OverTime", "AsyncOverTime"]


class OverTime(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OverTimeWithRawResponse:
        return OverTimeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OverTimeWithStreamingResponse:
        return OverTimeWithStreamingResponse(self)

    def list(
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
                    over_time_list_params.OverTimeListParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncOverTime(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOverTimeWithRawResponse:
        return AsyncOverTimeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOverTimeWithStreamingResponse:
        return AsyncOverTimeWithStreamingResponse(self)

    async def list(
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
                    over_time_list_params.OverTimeListParams,
                ),
            ),
            cast_to=NoneType,
        )


class OverTimeWithRawResponse:
    def __init__(self, over_time: OverTime) -> None:
        self._over_time = over_time

        self.list = to_raw_response_wrapper(
            over_time.list,
        )


class AsyncOverTimeWithRawResponse:
    def __init__(self, over_time: AsyncOverTime) -> None:
        self._over_time = over_time

        self.list = async_to_raw_response_wrapper(
            over_time.list,
        )


class OverTimeWithStreamingResponse:
    def __init__(self, over_time: OverTime) -> None:
        self._over_time = over_time

        self.list = to_streamed_response_wrapper(
            over_time.list,
        )


class AsyncOverTimeWithStreamingResponse:
    def __init__(self, over_time: AsyncOverTime) -> None:
        self._over_time = over_time

        self.list = async_to_streamed_response_wrapper(
            over_time.list,
        )
