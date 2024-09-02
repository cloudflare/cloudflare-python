# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.waiting_rooms.status_get_response import StatusGetResponse

from ..._wrappers import ResultWrapper

from ..._base_client import make_request_options

from typing import Type

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from typing import cast
from typing import cast

__all__ = ["StatusesResource", "AsyncStatusesResource"]


class StatusesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StatusesResourceWithRawResponse:
        return StatusesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatusesResourceWithStreamingResponse:
        return StatusesResourceWithStreamingResponse(self)

    def get(
        self,
        waiting_room_id: str,
        *,
        zone_id: str,
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
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        return self._get(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[StatusGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[StatusGetResponse], ResultWrapper[StatusGetResponse]),
        )


class AsyncStatusesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStatusesResourceWithRawResponse:
        return AsyncStatusesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatusesResourceWithStreamingResponse:
        return AsyncStatusesResourceWithStreamingResponse(self)

    async def get(
        self,
        waiting_room_id: str,
        *,
        zone_id: str,
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
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        return await self._get(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[StatusGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[StatusGetResponse], ResultWrapper[StatusGetResponse]),
        )


class StatusesResourceWithRawResponse:
    def __init__(self, statuses: StatusesResource) -> None:
        self._statuses = statuses

        self.get = to_raw_response_wrapper(
            statuses.get,
        )


class AsyncStatusesResourceWithRawResponse:
    def __init__(self, statuses: AsyncStatusesResource) -> None:
        self._statuses = statuses

        self.get = async_to_raw_response_wrapper(
            statuses.get,
        )


class StatusesResourceWithStreamingResponse:
    def __init__(self, statuses: StatusesResource) -> None:
        self._statuses = statuses

        self.get = to_streamed_response_wrapper(
            statuses.get,
        )


class AsyncStatusesResourceWithStreamingResponse:
    def __init__(self, statuses: AsyncStatusesResource) -> None:
        self._statuses = statuses

        self.get = async_to_streamed_response_wrapper(
            statuses.get,
        )
