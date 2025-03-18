# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from .details import (
    DetailsResource,
    AsyncDetailsResource,
    DetailsResourceWithRawResponse,
    AsyncDetailsResourceWithRawResponse,
    DetailsResourceWithStreamingResponse,
    AsyncDetailsResourceWithStreamingResponse,
)
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
from ...._wrappers import ResultWrapper
from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...._base_client import AsyncPaginator, make_request_options
from ....types.waiting_rooms import event_edit_params, event_list_params, event_create_params, event_update_params
from ....types.waiting_rooms.event import Event
from ....types.waiting_rooms.event_delete_response import EventDeleteResponse

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
    @cached_property
    def details(self) -> DetailsResource:
        return DetailsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return EventsResourceWithStreamingResponse(self)

    def create(
        self,
        waiting_room_id: str,
        *,
        zone_id: str,
        event_end_time: str,
        event_start_time: str,
        name: str,
        custom_page_html: Optional[str] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        disable_session_renewal: Optional[bool] | NotGiven = NOT_GIVEN,
        new_users_per_minute: Optional[int] | NotGiven = NOT_GIVEN,
        prequeue_start_time: Optional[str] | NotGiven = NOT_GIVEN,
        queueing_method: Optional[str] | NotGiven = NOT_GIVEN,
        session_duration: Optional[int] | NotGiven = NOT_GIVEN,
        shuffle_at_event_start: bool | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        total_active_users: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Event:
        """Only available for the Waiting Room Advanced subscription.

        Creates an event for
        a waiting room. An event takes place during a specified period of time,
        temporarily changing the behavior of a waiting room. While the event is active,
        some of the properties in the event's configuration may either override or
        inherit from the waiting room's configuration. Note that events cannot overlap
        with each other, so only one event can be active at a time.

        Args:
          zone_id: Identifier

          event_end_time: An ISO 8601 timestamp that marks the end of the event.

          event_start_time: An ISO 8601 timestamp that marks the start of the event. At this time, queued
              users will be processed with the event's configuration. The start time must be
              at least one minute before `event_end_time`.

          name: A unique name to identify the event. Only alphanumeric characters, hyphens and
              underscores are allowed.

          custom_page_html: If set, the event will override the waiting room's `custom_page_html` property
              while it is active. If null, the event will inherit it.

          description: A note that you can use to add more details about the event.

          disable_session_renewal: If set, the event will override the waiting room's `disable_session_renewal`
              property while it is active. If null, the event will inherit it.

          new_users_per_minute: If set, the event will override the waiting room's `new_users_per_minute`
              property while it is active. If null, the event will inherit it. This can only
              be set if the event's `total_active_users` property is also set.

          prequeue_start_time: An ISO 8601 timestamp that marks when to begin queueing all users before the
              event starts. The prequeue must start at least five minutes before
              `event_start_time`.

          queueing_method: If set, the event will override the waiting room's `queueing_method` property
              while it is active. If null, the event will inherit it.

          session_duration: If set, the event will override the waiting room's `session_duration` property
              while it is active. If null, the event will inherit it.

          shuffle_at_event_start: If enabled, users in the prequeue will be shuffled randomly at the
              `event_start_time`. Requires that `prequeue_start_time` is not null. This is
              useful for situations when many users will join the event prequeue at the same
              time and you want to shuffle them to ensure fairness. Naturally, it makes the
              most sense to enable this feature when the `queueing_method` during the event
              respects ordering such as **fifo**, or else the shuffling may be unnecessary.

          suspended: Suspends or allows an event. If set to `true`, the event is ignored and traffic
              will be handled based on the waiting room configuration.

          total_active_users: If set, the event will override the waiting room's `total_active_users` property
              while it is active. If null, the event will inherit it. This can only be set if
              the event's `new_users_per_minute` property is also set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        return self._post(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/events",
            body=maybe_transform(
                {
                    "event_end_time": event_end_time,
                    "event_start_time": event_start_time,
                    "name": name,
                    "custom_page_html": custom_page_html,
                    "description": description,
                    "disable_session_renewal": disable_session_renewal,
                    "new_users_per_minute": new_users_per_minute,
                    "prequeue_start_time": prequeue_start_time,
                    "queueing_method": queueing_method,
                    "session_duration": session_duration,
                    "shuffle_at_event_start": shuffle_at_event_start,
                    "suspended": suspended,
                    "total_active_users": total_active_users,
                },
                event_create_params.EventCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Event]._unwrapper,
            ),
            cast_to=cast(Type[Event], ResultWrapper[Event]),
        )

    def update(
        self,
        event_id: str,
        *,
        zone_id: str,
        waiting_room_id: str,
        event_end_time: str,
        event_start_time: str,
        name: str,
        custom_page_html: Optional[str] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        disable_session_renewal: Optional[bool] | NotGiven = NOT_GIVEN,
        new_users_per_minute: Optional[int] | NotGiven = NOT_GIVEN,
        prequeue_start_time: Optional[str] | NotGiven = NOT_GIVEN,
        queueing_method: Optional[str] | NotGiven = NOT_GIVEN,
        session_duration: Optional[int] | NotGiven = NOT_GIVEN,
        shuffle_at_event_start: bool | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        total_active_users: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Event:
        """
        Updates a configured event for a waiting room.

        Args:
          zone_id: Identifier

          event_end_time: An ISO 8601 timestamp that marks the end of the event.

          event_start_time: An ISO 8601 timestamp that marks the start of the event. At this time, queued
              users will be processed with the event's configuration. The start time must be
              at least one minute before `event_end_time`.

          name: A unique name to identify the event. Only alphanumeric characters, hyphens and
              underscores are allowed.

          custom_page_html: If set, the event will override the waiting room's `custom_page_html` property
              while it is active. If null, the event will inherit it.

          description: A note that you can use to add more details about the event.

          disable_session_renewal: If set, the event will override the waiting room's `disable_session_renewal`
              property while it is active. If null, the event will inherit it.

          new_users_per_minute: If set, the event will override the waiting room's `new_users_per_minute`
              property while it is active. If null, the event will inherit it. This can only
              be set if the event's `total_active_users` property is also set.

          prequeue_start_time: An ISO 8601 timestamp that marks when to begin queueing all users before the
              event starts. The prequeue must start at least five minutes before
              `event_start_time`.

          queueing_method: If set, the event will override the waiting room's `queueing_method` property
              while it is active. If null, the event will inherit it.

          session_duration: If set, the event will override the waiting room's `session_duration` property
              while it is active. If null, the event will inherit it.

          shuffle_at_event_start: If enabled, users in the prequeue will be shuffled randomly at the
              `event_start_time`. Requires that `prequeue_start_time` is not null. This is
              useful for situations when many users will join the event prequeue at the same
              time and you want to shuffle them to ensure fairness. Naturally, it makes the
              most sense to enable this feature when the `queueing_method` during the event
              respects ordering such as **fifo**, or else the shuffling may be unnecessary.

          suspended: Suspends or allows an event. If set to `true`, the event is ignored and traffic
              will be handled based on the waiting room configuration.

          total_active_users: If set, the event will override the waiting room's `total_active_users` property
              while it is active. If null, the event will inherit it. This can only be set if
              the event's `new_users_per_minute` property is also set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._put(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/events/{event_id}",
            body=maybe_transform(
                {
                    "event_end_time": event_end_time,
                    "event_start_time": event_start_time,
                    "name": name,
                    "custom_page_html": custom_page_html,
                    "description": description,
                    "disable_session_renewal": disable_session_renewal,
                    "new_users_per_minute": new_users_per_minute,
                    "prequeue_start_time": prequeue_start_time,
                    "queueing_method": queueing_method,
                    "session_duration": session_duration,
                    "shuffle_at_event_start": shuffle_at_event_start,
                    "suspended": suspended,
                    "total_active_users": total_active_users,
                },
                event_update_params.EventUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Event]._unwrapper,
            ),
            cast_to=cast(Type[Event], ResultWrapper[Event]),
        )

    def list(
        self,
        waiting_room_id: str,
        *,
        zone_id: str,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[Event]:
        """
        Lists events for a waiting room.

        Args:
          zone_id: Identifier

          page: Page number of paginated results.

          per_page: Maximum number of results per page. Must be a multiple of 5.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/events",
            page=SyncV4PagePaginationArray[Event],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    event_list_params.EventListParams,
                ),
            ),
            model=Event,
        )

    def delete(
        self,
        event_id: str,
        *,
        zone_id: str,
        waiting_room_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EventDeleteResponse:
        """
        Deletes an event for a waiting room.

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
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._delete(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/events/{event_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[EventDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[EventDeleteResponse], ResultWrapper[EventDeleteResponse]),
        )

    def edit(
        self,
        event_id: str,
        *,
        zone_id: str,
        waiting_room_id: str,
        event_end_time: str,
        event_start_time: str,
        name: str,
        custom_page_html: Optional[str] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        disable_session_renewal: Optional[bool] | NotGiven = NOT_GIVEN,
        new_users_per_minute: Optional[int] | NotGiven = NOT_GIVEN,
        prequeue_start_time: Optional[str] | NotGiven = NOT_GIVEN,
        queueing_method: Optional[str] | NotGiven = NOT_GIVEN,
        session_duration: Optional[int] | NotGiven = NOT_GIVEN,
        shuffle_at_event_start: bool | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        total_active_users: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Event:
        """
        Patches a configured event for a waiting room.

        Args:
          zone_id: Identifier

          event_end_time: An ISO 8601 timestamp that marks the end of the event.

          event_start_time: An ISO 8601 timestamp that marks the start of the event. At this time, queued
              users will be processed with the event's configuration. The start time must be
              at least one minute before `event_end_time`.

          name: A unique name to identify the event. Only alphanumeric characters, hyphens and
              underscores are allowed.

          custom_page_html: If set, the event will override the waiting room's `custom_page_html` property
              while it is active. If null, the event will inherit it.

          description: A note that you can use to add more details about the event.

          disable_session_renewal: If set, the event will override the waiting room's `disable_session_renewal`
              property while it is active. If null, the event will inherit it.

          new_users_per_minute: If set, the event will override the waiting room's `new_users_per_minute`
              property while it is active. If null, the event will inherit it. This can only
              be set if the event's `total_active_users` property is also set.

          prequeue_start_time: An ISO 8601 timestamp that marks when to begin queueing all users before the
              event starts. The prequeue must start at least five minutes before
              `event_start_time`.

          queueing_method: If set, the event will override the waiting room's `queueing_method` property
              while it is active. If null, the event will inherit it.

          session_duration: If set, the event will override the waiting room's `session_duration` property
              while it is active. If null, the event will inherit it.

          shuffle_at_event_start: If enabled, users in the prequeue will be shuffled randomly at the
              `event_start_time`. Requires that `prequeue_start_time` is not null. This is
              useful for situations when many users will join the event prequeue at the same
              time and you want to shuffle them to ensure fairness. Naturally, it makes the
              most sense to enable this feature when the `queueing_method` during the event
              respects ordering such as **fifo**, or else the shuffling may be unnecessary.

          suspended: Suspends or allows an event. If set to `true`, the event is ignored and traffic
              will be handled based on the waiting room configuration.

          total_active_users: If set, the event will override the waiting room's `total_active_users` property
              while it is active. If null, the event will inherit it. This can only be set if
              the event's `new_users_per_minute` property is also set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._patch(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/events/{event_id}",
            body=maybe_transform(
                {
                    "event_end_time": event_end_time,
                    "event_start_time": event_start_time,
                    "name": name,
                    "custom_page_html": custom_page_html,
                    "description": description,
                    "disable_session_renewal": disable_session_renewal,
                    "new_users_per_minute": new_users_per_minute,
                    "prequeue_start_time": prequeue_start_time,
                    "queueing_method": queueing_method,
                    "session_duration": session_duration,
                    "shuffle_at_event_start": shuffle_at_event_start,
                    "suspended": suspended,
                    "total_active_users": total_active_users,
                },
                event_edit_params.EventEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Event]._unwrapper,
            ),
            cast_to=cast(Type[Event], ResultWrapper[Event]),
        )

    def get(
        self,
        event_id: str,
        *,
        zone_id: str,
        waiting_room_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Event:
        """
        Fetches a single configured event for a waiting room.

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
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._get(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/events/{event_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Event]._unwrapper,
            ),
            cast_to=cast(Type[Event], ResultWrapper[Event]),
        )


class AsyncEventsResource(AsyncAPIResource):
    @cached_property
    def details(self) -> AsyncDetailsResource:
        return AsyncDetailsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncEventsResourceWithStreamingResponse(self)

    async def create(
        self,
        waiting_room_id: str,
        *,
        zone_id: str,
        event_end_time: str,
        event_start_time: str,
        name: str,
        custom_page_html: Optional[str] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        disable_session_renewal: Optional[bool] | NotGiven = NOT_GIVEN,
        new_users_per_minute: Optional[int] | NotGiven = NOT_GIVEN,
        prequeue_start_time: Optional[str] | NotGiven = NOT_GIVEN,
        queueing_method: Optional[str] | NotGiven = NOT_GIVEN,
        session_duration: Optional[int] | NotGiven = NOT_GIVEN,
        shuffle_at_event_start: bool | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        total_active_users: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Event:
        """Only available for the Waiting Room Advanced subscription.

        Creates an event for
        a waiting room. An event takes place during a specified period of time,
        temporarily changing the behavior of a waiting room. While the event is active,
        some of the properties in the event's configuration may either override or
        inherit from the waiting room's configuration. Note that events cannot overlap
        with each other, so only one event can be active at a time.

        Args:
          zone_id: Identifier

          event_end_time: An ISO 8601 timestamp that marks the end of the event.

          event_start_time: An ISO 8601 timestamp that marks the start of the event. At this time, queued
              users will be processed with the event's configuration. The start time must be
              at least one minute before `event_end_time`.

          name: A unique name to identify the event. Only alphanumeric characters, hyphens and
              underscores are allowed.

          custom_page_html: If set, the event will override the waiting room's `custom_page_html` property
              while it is active. If null, the event will inherit it.

          description: A note that you can use to add more details about the event.

          disable_session_renewal: If set, the event will override the waiting room's `disable_session_renewal`
              property while it is active. If null, the event will inherit it.

          new_users_per_minute: If set, the event will override the waiting room's `new_users_per_minute`
              property while it is active. If null, the event will inherit it. This can only
              be set if the event's `total_active_users` property is also set.

          prequeue_start_time: An ISO 8601 timestamp that marks when to begin queueing all users before the
              event starts. The prequeue must start at least five minutes before
              `event_start_time`.

          queueing_method: If set, the event will override the waiting room's `queueing_method` property
              while it is active. If null, the event will inherit it.

          session_duration: If set, the event will override the waiting room's `session_duration` property
              while it is active. If null, the event will inherit it.

          shuffle_at_event_start: If enabled, users in the prequeue will be shuffled randomly at the
              `event_start_time`. Requires that `prequeue_start_time` is not null. This is
              useful for situations when many users will join the event prequeue at the same
              time and you want to shuffle them to ensure fairness. Naturally, it makes the
              most sense to enable this feature when the `queueing_method` during the event
              respects ordering such as **fifo**, or else the shuffling may be unnecessary.

          suspended: Suspends or allows an event. If set to `true`, the event is ignored and traffic
              will be handled based on the waiting room configuration.

          total_active_users: If set, the event will override the waiting room's `total_active_users` property
              while it is active. If null, the event will inherit it. This can only be set if
              the event's `new_users_per_minute` property is also set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        return await self._post(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/events",
            body=await async_maybe_transform(
                {
                    "event_end_time": event_end_time,
                    "event_start_time": event_start_time,
                    "name": name,
                    "custom_page_html": custom_page_html,
                    "description": description,
                    "disable_session_renewal": disable_session_renewal,
                    "new_users_per_minute": new_users_per_minute,
                    "prequeue_start_time": prequeue_start_time,
                    "queueing_method": queueing_method,
                    "session_duration": session_duration,
                    "shuffle_at_event_start": shuffle_at_event_start,
                    "suspended": suspended,
                    "total_active_users": total_active_users,
                },
                event_create_params.EventCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Event]._unwrapper,
            ),
            cast_to=cast(Type[Event], ResultWrapper[Event]),
        )

    async def update(
        self,
        event_id: str,
        *,
        zone_id: str,
        waiting_room_id: str,
        event_end_time: str,
        event_start_time: str,
        name: str,
        custom_page_html: Optional[str] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        disable_session_renewal: Optional[bool] | NotGiven = NOT_GIVEN,
        new_users_per_minute: Optional[int] | NotGiven = NOT_GIVEN,
        prequeue_start_time: Optional[str] | NotGiven = NOT_GIVEN,
        queueing_method: Optional[str] | NotGiven = NOT_GIVEN,
        session_duration: Optional[int] | NotGiven = NOT_GIVEN,
        shuffle_at_event_start: bool | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        total_active_users: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Event:
        """
        Updates a configured event for a waiting room.

        Args:
          zone_id: Identifier

          event_end_time: An ISO 8601 timestamp that marks the end of the event.

          event_start_time: An ISO 8601 timestamp that marks the start of the event. At this time, queued
              users will be processed with the event's configuration. The start time must be
              at least one minute before `event_end_time`.

          name: A unique name to identify the event. Only alphanumeric characters, hyphens and
              underscores are allowed.

          custom_page_html: If set, the event will override the waiting room's `custom_page_html` property
              while it is active. If null, the event will inherit it.

          description: A note that you can use to add more details about the event.

          disable_session_renewal: If set, the event will override the waiting room's `disable_session_renewal`
              property while it is active. If null, the event will inherit it.

          new_users_per_minute: If set, the event will override the waiting room's `new_users_per_minute`
              property while it is active. If null, the event will inherit it. This can only
              be set if the event's `total_active_users` property is also set.

          prequeue_start_time: An ISO 8601 timestamp that marks when to begin queueing all users before the
              event starts. The prequeue must start at least five minutes before
              `event_start_time`.

          queueing_method: If set, the event will override the waiting room's `queueing_method` property
              while it is active. If null, the event will inherit it.

          session_duration: If set, the event will override the waiting room's `session_duration` property
              while it is active. If null, the event will inherit it.

          shuffle_at_event_start: If enabled, users in the prequeue will be shuffled randomly at the
              `event_start_time`. Requires that `prequeue_start_time` is not null. This is
              useful for situations when many users will join the event prequeue at the same
              time and you want to shuffle them to ensure fairness. Naturally, it makes the
              most sense to enable this feature when the `queueing_method` during the event
              respects ordering such as **fifo**, or else the shuffling may be unnecessary.

          suspended: Suspends or allows an event. If set to `true`, the event is ignored and traffic
              will be handled based on the waiting room configuration.

          total_active_users: If set, the event will override the waiting room's `total_active_users` property
              while it is active. If null, the event will inherit it. This can only be set if
              the event's `new_users_per_minute` property is also set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._put(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/events/{event_id}",
            body=await async_maybe_transform(
                {
                    "event_end_time": event_end_time,
                    "event_start_time": event_start_time,
                    "name": name,
                    "custom_page_html": custom_page_html,
                    "description": description,
                    "disable_session_renewal": disable_session_renewal,
                    "new_users_per_minute": new_users_per_minute,
                    "prequeue_start_time": prequeue_start_time,
                    "queueing_method": queueing_method,
                    "session_duration": session_duration,
                    "shuffle_at_event_start": shuffle_at_event_start,
                    "suspended": suspended,
                    "total_active_users": total_active_users,
                },
                event_update_params.EventUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Event]._unwrapper,
            ),
            cast_to=cast(Type[Event], ResultWrapper[Event]),
        )

    def list(
        self,
        waiting_room_id: str,
        *,
        zone_id: str,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Event, AsyncV4PagePaginationArray[Event]]:
        """
        Lists events for a waiting room.

        Args:
          zone_id: Identifier

          page: Page number of paginated results.

          per_page: Maximum number of results per page. Must be a multiple of 5.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/events",
            page=AsyncV4PagePaginationArray[Event],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    event_list_params.EventListParams,
                ),
            ),
            model=Event,
        )

    async def delete(
        self,
        event_id: str,
        *,
        zone_id: str,
        waiting_room_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EventDeleteResponse:
        """
        Deletes an event for a waiting room.

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
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._delete(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/events/{event_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[EventDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[EventDeleteResponse], ResultWrapper[EventDeleteResponse]),
        )

    async def edit(
        self,
        event_id: str,
        *,
        zone_id: str,
        waiting_room_id: str,
        event_end_time: str,
        event_start_time: str,
        name: str,
        custom_page_html: Optional[str] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        disable_session_renewal: Optional[bool] | NotGiven = NOT_GIVEN,
        new_users_per_minute: Optional[int] | NotGiven = NOT_GIVEN,
        prequeue_start_time: Optional[str] | NotGiven = NOT_GIVEN,
        queueing_method: Optional[str] | NotGiven = NOT_GIVEN,
        session_duration: Optional[int] | NotGiven = NOT_GIVEN,
        shuffle_at_event_start: bool | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        total_active_users: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Event:
        """
        Patches a configured event for a waiting room.

        Args:
          zone_id: Identifier

          event_end_time: An ISO 8601 timestamp that marks the end of the event.

          event_start_time: An ISO 8601 timestamp that marks the start of the event. At this time, queued
              users will be processed with the event's configuration. The start time must be
              at least one minute before `event_end_time`.

          name: A unique name to identify the event. Only alphanumeric characters, hyphens and
              underscores are allowed.

          custom_page_html: If set, the event will override the waiting room's `custom_page_html` property
              while it is active. If null, the event will inherit it.

          description: A note that you can use to add more details about the event.

          disable_session_renewal: If set, the event will override the waiting room's `disable_session_renewal`
              property while it is active. If null, the event will inherit it.

          new_users_per_minute: If set, the event will override the waiting room's `new_users_per_minute`
              property while it is active. If null, the event will inherit it. This can only
              be set if the event's `total_active_users` property is also set.

          prequeue_start_time: An ISO 8601 timestamp that marks when to begin queueing all users before the
              event starts. The prequeue must start at least five minutes before
              `event_start_time`.

          queueing_method: If set, the event will override the waiting room's `queueing_method` property
              while it is active. If null, the event will inherit it.

          session_duration: If set, the event will override the waiting room's `session_duration` property
              while it is active. If null, the event will inherit it.

          shuffle_at_event_start: If enabled, users in the prequeue will be shuffled randomly at the
              `event_start_time`. Requires that `prequeue_start_time` is not null. This is
              useful for situations when many users will join the event prequeue at the same
              time and you want to shuffle them to ensure fairness. Naturally, it makes the
              most sense to enable this feature when the `queueing_method` during the event
              respects ordering such as **fifo**, or else the shuffling may be unnecessary.

          suspended: Suspends or allows an event. If set to `true`, the event is ignored and traffic
              will be handled based on the waiting room configuration.

          total_active_users: If set, the event will override the waiting room's `total_active_users` property
              while it is active. If null, the event will inherit it. This can only be set if
              the event's `new_users_per_minute` property is also set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/events/{event_id}",
            body=await async_maybe_transform(
                {
                    "event_end_time": event_end_time,
                    "event_start_time": event_start_time,
                    "name": name,
                    "custom_page_html": custom_page_html,
                    "description": description,
                    "disable_session_renewal": disable_session_renewal,
                    "new_users_per_minute": new_users_per_minute,
                    "prequeue_start_time": prequeue_start_time,
                    "queueing_method": queueing_method,
                    "session_duration": session_duration,
                    "shuffle_at_event_start": shuffle_at_event_start,
                    "suspended": suspended,
                    "total_active_users": total_active_users,
                },
                event_edit_params.EventEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Event]._unwrapper,
            ),
            cast_to=cast(Type[Event], ResultWrapper[Event]),
        )

    async def get(
        self,
        event_id: str,
        *,
        zone_id: str,
        waiting_room_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Event:
        """
        Fetches a single configured event for a waiting room.

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
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._get(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/events/{event_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Event]._unwrapper,
            ),
            cast_to=cast(Type[Event], ResultWrapper[Event]),
        )


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.create = to_raw_response_wrapper(
            events.create,
        )
        self.update = to_raw_response_wrapper(
            events.update,
        )
        self.list = to_raw_response_wrapper(
            events.list,
        )
        self.delete = to_raw_response_wrapper(
            events.delete,
        )
        self.edit = to_raw_response_wrapper(
            events.edit,
        )
        self.get = to_raw_response_wrapper(
            events.get,
        )

    @cached_property
    def details(self) -> DetailsResourceWithRawResponse:
        return DetailsResourceWithRawResponse(self._events.details)


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.create = async_to_raw_response_wrapper(
            events.create,
        )
        self.update = async_to_raw_response_wrapper(
            events.update,
        )
        self.list = async_to_raw_response_wrapper(
            events.list,
        )
        self.delete = async_to_raw_response_wrapper(
            events.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            events.edit,
        )
        self.get = async_to_raw_response_wrapper(
            events.get,
        )

    @cached_property
    def details(self) -> AsyncDetailsResourceWithRawResponse:
        return AsyncDetailsResourceWithRawResponse(self._events.details)


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.create = to_streamed_response_wrapper(
            events.create,
        )
        self.update = to_streamed_response_wrapper(
            events.update,
        )
        self.list = to_streamed_response_wrapper(
            events.list,
        )
        self.delete = to_streamed_response_wrapper(
            events.delete,
        )
        self.edit = to_streamed_response_wrapper(
            events.edit,
        )
        self.get = to_streamed_response_wrapper(
            events.get,
        )

    @cached_property
    def details(self) -> DetailsResourceWithStreamingResponse:
        return DetailsResourceWithStreamingResponse(self._events.details)


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.create = async_to_streamed_response_wrapper(
            events.create,
        )
        self.update = async_to_streamed_response_wrapper(
            events.update,
        )
        self.list = async_to_streamed_response_wrapper(
            events.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            events.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            events.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            events.get,
        )

    @cached_property
    def details(self) -> AsyncDetailsResourceWithStreamingResponse:
        return AsyncDetailsResourceWithStreamingResponse(self._events.details)
