# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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

__all__ = ["Hijacks", "AsyncHijacks"]


class Hijacks(SyncAPIResource):
    @cached_property
    def events(self) -> Events:
        return Events(self._client)

    @cached_property
    def with_raw_response(self) -> HijacksWithRawResponse:
        return HijacksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HijacksWithStreamingResponse:
        return HijacksWithStreamingResponse(self)


class AsyncHijacks(AsyncAPIResource):
    @cached_property
    def events(self) -> AsyncEvents:
        return AsyncEvents(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHijacksWithRawResponse:
        return AsyncHijacksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHijacksWithStreamingResponse:
        return AsyncHijacksWithStreamingResponse(self)


class HijacksWithRawResponse:
    def __init__(self, hijacks: Hijacks) -> None:
        self._hijacks = hijacks

    @cached_property
    def events(self) -> EventsWithRawResponse:
        return EventsWithRawResponse(self._hijacks.events)


class AsyncHijacksWithRawResponse:
    def __init__(self, hijacks: AsyncHijacks) -> None:
        self._hijacks = hijacks

    @cached_property
    def events(self) -> AsyncEventsWithRawResponse:
        return AsyncEventsWithRawResponse(self._hijacks.events)


class HijacksWithStreamingResponse:
    def __init__(self, hijacks: Hijacks) -> None:
        self._hijacks = hijacks

    @cached_property
    def events(self) -> EventsWithStreamingResponse:
        return EventsWithStreamingResponse(self._hijacks.events)


class AsyncHijacksWithStreamingResponse:
    def __init__(self, hijacks: AsyncHijacks) -> None:
        self._hijacks = hijacks

    @cached_property
    def events(self) -> AsyncEventsWithStreamingResponse:
        return AsyncEventsWithStreamingResponse(self._hijacks.events)
