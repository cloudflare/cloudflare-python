# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .events import (
    EventsResource,
    AsyncEventsResource,
    EventsResourceWithRawResponse,
    AsyncEventsResourceWithRawResponse,
    EventsResourceWithStreamingResponse,
    AsyncEventsResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["LeaksResource", "AsyncLeaksResource"]


class LeaksResource(SyncAPIResource):
    @cached_property
    def events(self) -> EventsResource:
        return EventsResource(self._client)

    @cached_property
    def with_raw_response(self) -> LeaksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return LeaksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LeaksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return LeaksResourceWithStreamingResponse(self)


class AsyncLeaksResource(AsyncAPIResource):
    @cached_property
    def events(self) -> AsyncEventsResource:
        return AsyncEventsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLeaksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLeaksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLeaksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncLeaksResourceWithStreamingResponse(self)


class LeaksResourceWithRawResponse:
    def __init__(self, leaks: LeaksResource) -> None:
        self._leaks = leaks

    @cached_property
    def events(self) -> EventsResourceWithRawResponse:
        return EventsResourceWithRawResponse(self._leaks.events)


class AsyncLeaksResourceWithRawResponse:
    def __init__(self, leaks: AsyncLeaksResource) -> None:
        self._leaks = leaks

    @cached_property
    def events(self) -> AsyncEventsResourceWithRawResponse:
        return AsyncEventsResourceWithRawResponse(self._leaks.events)


class LeaksResourceWithStreamingResponse:
    def __init__(self, leaks: LeaksResource) -> None:
        self._leaks = leaks

    @cached_property
    def events(self) -> EventsResourceWithStreamingResponse:
        return EventsResourceWithStreamingResponse(self._leaks.events)


class AsyncLeaksResourceWithStreamingResponse:
    def __init__(self, leaks: AsyncLeaksResource) -> None:
        self._leaks = leaks

    @cached_property
    def events(self) -> AsyncEventsResourceWithStreamingResponse:
        return AsyncEventsResourceWithStreamingResponse(self._leaks.events)
