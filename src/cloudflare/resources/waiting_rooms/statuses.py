# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.waiting_rooms import StatusGetResponse

__all__ = ["Statuses", "AsyncStatuses"]


class Statuses(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StatusesWithRawResponse:
        return StatusesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatusesWithStreamingResponse:
        return StatusesWithStreamingResponse(self)

    def get(
        self,
        waiting_room_id: object,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatusGetResponse:
        """Fetches the status of a configured waiting room.

        Response fields include:

        1. `status`: String indicating the status of the waiting room. The possible
           status are:
           - **not_queueing** indicates that the configured thresholds have not been met
             and all users are going through to the origin.
           - **queueing** indicates that the thresholds have been met and some users are
             held in the waiting room.
           - **event_prequeueing** indicates that an event is active and is currently
             prequeueing users before it starts.
        2. `event_id`: String of the current event's `id` if an event is active,
           otherwise an empty string.
        3. `estimated_queued_users`: Integer of the estimated number of users currently
           waiting in the queue.
        4. `estimated_total_active_users`: Integer of the estimated number of users
           currently active on the origin.
        5. `max_estimated_time_minutes`: Integer of the maximum estimated time currently
           presented to the users.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._get(
            f"/zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[StatusGetResponse], ResultWrapper[StatusGetResponse]),
        )


class AsyncStatuses(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStatusesWithRawResponse:
        return AsyncStatusesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatusesWithStreamingResponse:
        return AsyncStatusesWithStreamingResponse(self)

    async def get(
        self,
        waiting_room_id: object,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatusGetResponse:
        """Fetches the status of a configured waiting room.

        Response fields include:

        1. `status`: String indicating the status of the waiting room. The possible
           status are:
           - **not_queueing** indicates that the configured thresholds have not been met
             and all users are going through to the origin.
           - **queueing** indicates that the thresholds have been met and some users are
             held in the waiting room.
           - **event_prequeueing** indicates that an event is active and is currently
             prequeueing users before it starts.
        2. `event_id`: String of the current event's `id` if an event is active,
           otherwise an empty string.
        3. `estimated_queued_users`: Integer of the estimated number of users currently
           waiting in the queue.
        4. `estimated_total_active_users`: Integer of the estimated number of users
           currently active on the origin.
        5. `max_estimated_time_minutes`: Integer of the maximum estimated time currently
           presented to the users.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._get(
            f"/zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[StatusGetResponse], ResultWrapper[StatusGetResponse]),
        )


class StatusesWithRawResponse:
    def __init__(self, statuses: Statuses) -> None:
        self._statuses = statuses

        self.get = to_raw_response_wrapper(
            statuses.get,
        )


class AsyncStatusesWithRawResponse:
    def __init__(self, statuses: AsyncStatuses) -> None:
        self._statuses = statuses

        self.get = async_to_raw_response_wrapper(
            statuses.get,
        )


class StatusesWithStreamingResponse:
    def __init__(self, statuses: Statuses) -> None:
        self._statuses = statuses

        self.get = to_streamed_response_wrapper(
            statuses.get,
        )


class AsyncStatusesWithStreamingResponse:
    def __init__(self, statuses: AsyncStatuses) -> None:
        self._statuses = statuses

        self.get = async_to_streamed_response_wrapper(
            statuses.get,
        )
