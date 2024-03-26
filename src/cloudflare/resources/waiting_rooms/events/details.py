# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.waiting_rooms.events import WaitingroomEventDetailsResult

__all__ = ["Details", "AsyncDetails"]


class Details(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DetailsWithRawResponse:
        return DetailsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DetailsWithStreamingResponse:
        return DetailsWithStreamingResponse(self)

    def get(
        self,
        event_id: str,
        *,
        zone_identifier: str,
        waiting_room_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaitingroomEventDetailsResult:
        """Previews an event's configuration as if it was active.

        Inherited fields from the
        waiting room will be displayed with their current values.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._get(
            f"/zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/events/{event_id}/details",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WaitingroomEventDetailsResult], ResultWrapper[WaitingroomEventDetailsResult]),
        )


class AsyncDetails(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDetailsWithRawResponse:
        return AsyncDetailsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDetailsWithStreamingResponse:
        return AsyncDetailsWithStreamingResponse(self)

    async def get(
        self,
        event_id: str,
        *,
        zone_identifier: str,
        waiting_room_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaitingroomEventDetailsResult:
        """Previews an event's configuration as if it was active.

        Inherited fields from the
        waiting room will be displayed with their current values.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._get(
            f"/zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/events/{event_id}/details",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WaitingroomEventDetailsResult], ResultWrapper[WaitingroomEventDetailsResult]),
        )


class DetailsWithRawResponse:
    def __init__(self, details: Details) -> None:
        self._details = details

        self.get = to_raw_response_wrapper(
            details.get,
        )


class AsyncDetailsWithRawResponse:
    def __init__(self, details: AsyncDetails) -> None:
        self._details = details

        self.get = async_to_raw_response_wrapper(
            details.get,
        )


class DetailsWithStreamingResponse:
    def __init__(self, details: Details) -> None:
        self._details = details

        self.get = to_streamed_response_wrapper(
            details.get,
        )


class AsyncDetailsWithStreamingResponse:
    def __init__(self, details: AsyncDetails) -> None:
        self._details = details

        self.get = async_to_streamed_response_wrapper(
            details.get,
        )
