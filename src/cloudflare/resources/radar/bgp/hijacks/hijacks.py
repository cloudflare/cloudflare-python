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

__all__ = ["HijacksResource", "AsyncHijacksResource"]


class HijacksResource(SyncAPIResource):
    @cached_property
    def events(self) -> EventsResource:
        return EventsResource(self._client)

    @cached_property
    def with_raw_response(self) -> HijacksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return HijacksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HijacksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return HijacksResourceWithStreamingResponse(self)


class AsyncHijacksResource(AsyncAPIResource):
    @cached_property
    def events(self) -> AsyncEventsResource:
        return AsyncEventsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHijacksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHijacksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHijacksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncHijacksResourceWithStreamingResponse(self)


class HijacksResourceWithRawResponse:
    def __init__(self, hijacks: HijacksResource) -> None:
        self._hijacks = hijacks

    @cached_property
    def events(self) -> EventsResourceWithRawResponse:
        return EventsResourceWithRawResponse(self._hijacks.events)


class AsyncHijacksResourceWithRawResponse:
    def __init__(self, hijacks: AsyncHijacksResource) -> None:
        self._hijacks = hijacks

    @cached_property
    def events(self) -> AsyncEventsResourceWithRawResponse:
        return AsyncEventsResourceWithRawResponse(self._hijacks.events)


class HijacksResourceWithStreamingResponse:
    def __init__(self, hijacks: HijacksResource) -> None:
        self._hijacks = hijacks

    @cached_property
    def events(self) -> EventsResourceWithStreamingResponse:
        return EventsResourceWithStreamingResponse(self._hijacks.events)


class AsyncHijacksResourceWithStreamingResponse:
    def __init__(self, hijacks: AsyncHijacksResource) -> None:
        self._hijacks = hijacks

    @cached_property
    def events(self) -> AsyncEventsResourceWithStreamingResponse:
        return AsyncEventsResourceWithStreamingResponse(self._hijacks.events)
