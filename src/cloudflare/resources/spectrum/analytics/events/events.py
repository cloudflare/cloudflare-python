# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .bytimes import (
    BytimesResource,
    AsyncBytimesResource,
    BytimesResourceWithRawResponse,
    AsyncBytimesResourceWithRawResponse,
    BytimesResourceWithStreamingResponse,
    AsyncBytimesResourceWithStreamingResponse,
)
from .summaries import (
    SummariesResource,
    AsyncSummariesResource,
    SummariesResourceWithRawResponse,
    AsyncSummariesResourceWithRawResponse,
    SummariesResourceWithStreamingResponse,
    AsyncSummariesResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
    @cached_property
    def bytimes(self) -> BytimesResource:
        return BytimesResource(self._client)

    @cached_property
    def summaries(self) -> SummariesResource:
        return SummariesResource(self._client)

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


class AsyncEventsResource(AsyncAPIResource):
    @cached_property
    def bytimes(self) -> AsyncBytimesResource:
        return AsyncBytimesResource(self._client)

    @cached_property
    def summaries(self) -> AsyncSummariesResource:
        return AsyncSummariesResource(self._client)

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


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

    @cached_property
    def bytimes(self) -> BytimesResourceWithRawResponse:
        return BytimesResourceWithRawResponse(self._events.bytimes)

    @cached_property
    def summaries(self) -> SummariesResourceWithRawResponse:
        return SummariesResourceWithRawResponse(self._events.summaries)


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

    @cached_property
    def bytimes(self) -> AsyncBytimesResourceWithRawResponse:
        return AsyncBytimesResourceWithRawResponse(self._events.bytimes)

    @cached_property
    def summaries(self) -> AsyncSummariesResourceWithRawResponse:
        return AsyncSummariesResourceWithRawResponse(self._events.summaries)


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

    @cached_property
    def bytimes(self) -> BytimesResourceWithStreamingResponse:
        return BytimesResourceWithStreamingResponse(self._events.bytimes)

    @cached_property
    def summaries(self) -> SummariesResourceWithStreamingResponse:
        return SummariesResourceWithStreamingResponse(self._events.summaries)


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

    @cached_property
    def bytimes(self) -> AsyncBytimesResourceWithStreamingResponse:
        return AsyncBytimesResourceWithStreamingResponse(self._events.bytimes)

    @cached_property
    def summaries(self) -> AsyncSummariesResourceWithStreamingResponse:
        return AsyncSummariesResourceWithStreamingResponse(self._events.summaries)
