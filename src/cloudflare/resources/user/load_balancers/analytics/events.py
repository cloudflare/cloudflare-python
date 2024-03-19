# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, Optional, cast
from datetime import datetime

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from .....types.user.load_balancers.analytics import EventListResponse, event_list_params

__all__ = ["Events", "AsyncEvents"]


class Events(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EventsWithRawResponse:
        return EventsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsWithStreamingResponse:
        return EventsWithStreamingResponse(self)

    def list(
        self,
        *,
        origin_healthy: bool | NotGiven = NOT_GIVEN,
        origin_name: str | NotGiven = NOT_GIVEN,
        pool_healthy: bool | NotGiven = NOT_GIVEN,
        pool_id: str | NotGiven = NOT_GIVEN,
        pool_name: str | NotGiven = NOT_GIVEN,
        since: Union[str, datetime] | NotGiven = NOT_GIVEN,
        until: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EventListResponse]:
        """
        List origin health changes.

        Args:
          origin_healthy: If true, filter events where the origin status is healthy. If false, filter
              events where the origin status is unhealthy.

          origin_name: The name for the origin to filter.

          pool_healthy: If true, filter events where the pool status is healthy. If false, filter events
              where the pool status is unhealthy.

          pool_name: The name for the pool to filter.

          since: Start date and time of requesting data period in the ISO8601 format.

          until: End date and time of requesting data period in the ISO8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/user/load_balancing_analytics/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "origin_healthy": origin_healthy,
                        "origin_name": origin_name,
                        "pool_healthy": pool_healthy,
                        "pool_id": pool_id,
                        "pool_name": pool_name,
                        "since": since,
                        "until": until,
                    },
                    event_list_params.EventListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[EventListResponse]], ResultWrapper[EventListResponse]),
        )


class AsyncEvents(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEventsWithRawResponse:
        return AsyncEventsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsWithStreamingResponse:
        return AsyncEventsWithStreamingResponse(self)

    async def list(
        self,
        *,
        origin_healthy: bool | NotGiven = NOT_GIVEN,
        origin_name: str | NotGiven = NOT_GIVEN,
        pool_healthy: bool | NotGiven = NOT_GIVEN,
        pool_id: str | NotGiven = NOT_GIVEN,
        pool_name: str | NotGiven = NOT_GIVEN,
        since: Union[str, datetime] | NotGiven = NOT_GIVEN,
        until: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EventListResponse]:
        """
        List origin health changes.

        Args:
          origin_healthy: If true, filter events where the origin status is healthy. If false, filter
              events where the origin status is unhealthy.

          origin_name: The name for the origin to filter.

          pool_healthy: If true, filter events where the pool status is healthy. If false, filter events
              where the pool status is unhealthy.

          pool_name: The name for the pool to filter.

          since: Start date and time of requesting data period in the ISO8601 format.

          until: End date and time of requesting data period in the ISO8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/user/load_balancing_analytics/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "origin_healthy": origin_healthy,
                        "origin_name": origin_name,
                        "pool_healthy": pool_healthy,
                        "pool_id": pool_id,
                        "pool_name": pool_name,
                        "since": since,
                        "until": until,
                    },
                    event_list_params.EventListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[EventListResponse]], ResultWrapper[EventListResponse]),
        )


class EventsWithRawResponse:
    def __init__(self, events: Events) -> None:
        self._events = events

        self.list = to_raw_response_wrapper(
            events.list,
        )


class AsyncEventsWithRawResponse:
    def __init__(self, events: AsyncEvents) -> None:
        self._events = events

        self.list = async_to_raw_response_wrapper(
            events.list,
        )


class EventsWithStreamingResponse:
    def __init__(self, events: Events) -> None:
        self._events = events

        self.list = to_streamed_response_wrapper(
            events.list,
        )


class AsyncEventsWithStreamingResponse:
    def __init__(self, events: AsyncEvents) -> None:
        self._events = events

        self.list = async_to_streamed_response_wrapper(
            events.list,
        )
