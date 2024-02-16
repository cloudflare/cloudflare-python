# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .events import (
    Events,
    AsyncEvents,
    EventsWithRawResponse,
    AsyncEventsWithRawResponse,
    EventsWithStreamingResponse,
    AsyncEventsWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Leaks", "AsyncLeaks"]


class Leaks(SyncAPIResource):
    @cached_property
    def events(self) -> Events:
        return Events(self._client)

    @cached_property
    def with_raw_response(self) -> LeaksWithRawResponse:
        return LeaksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LeaksWithStreamingResponse:
        return LeaksWithStreamingResponse(self)


class AsyncLeaks(AsyncAPIResource):
    @cached_property
    def events(self) -> AsyncEvents:
        return AsyncEvents(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLeaksWithRawResponse:
        return AsyncLeaksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLeaksWithStreamingResponse:
        return AsyncLeaksWithStreamingResponse(self)


class LeaksWithRawResponse:
    def __init__(self, leaks: Leaks) -> None:
        self._leaks = leaks

    @cached_property
    def events(self) -> EventsWithRawResponse:
        return EventsWithRawResponse(self._leaks.events)


class AsyncLeaksWithRawResponse:
    def __init__(self, leaks: AsyncLeaks) -> None:
        self._leaks = leaks

    @cached_property
    def events(self) -> AsyncEventsWithRawResponse:
        return AsyncEventsWithRawResponse(self._leaks.events)


class LeaksWithStreamingResponse:
    def __init__(self, leaks: Leaks) -> None:
        self._leaks = leaks

    @cached_property
    def events(self) -> EventsWithStreamingResponse:
        return EventsWithStreamingResponse(self._leaks.events)


class AsyncLeaksWithStreamingResponse:
    def __init__(self, leaks: AsyncLeaks) -> None:
        self._leaks = leaks

    @cached_property
    def events(self) -> AsyncEventsWithStreamingResponse:
        return AsyncEventsWithStreamingResponse(self._leaks.events)
