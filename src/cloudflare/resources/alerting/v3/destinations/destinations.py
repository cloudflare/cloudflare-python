# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .pagerduty import (
    Pagerduty,
    AsyncPagerduty,
    PagerdutyWithRawResponse,
    AsyncPagerdutyWithRawResponse,
    PagerdutyWithStreamingResponse,
    AsyncPagerdutyWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Destinations", "AsyncDestinations"]


class Destinations(SyncAPIResource):
    @cached_property
    def pagerduty(self) -> Pagerduty:
        return Pagerduty(self._client)

    @cached_property
    def with_raw_response(self) -> DestinationsWithRawResponse:
        return DestinationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DestinationsWithStreamingResponse:
        return DestinationsWithStreamingResponse(self)


class AsyncDestinations(AsyncAPIResource):
    @cached_property
    def pagerduty(self) -> AsyncPagerduty:
        return AsyncPagerduty(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDestinationsWithRawResponse:
        return AsyncDestinationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDestinationsWithStreamingResponse:
        return AsyncDestinationsWithStreamingResponse(self)


class DestinationsWithRawResponse:
    def __init__(self, destinations: Destinations) -> None:
        self._destinations = destinations

    @cached_property
    def pagerduty(self) -> PagerdutyWithRawResponse:
        return PagerdutyWithRawResponse(self._destinations.pagerduty)


class AsyncDestinationsWithRawResponse:
    def __init__(self, destinations: AsyncDestinations) -> None:
        self._destinations = destinations

    @cached_property
    def pagerduty(self) -> AsyncPagerdutyWithRawResponse:
        return AsyncPagerdutyWithRawResponse(self._destinations.pagerduty)


class DestinationsWithStreamingResponse:
    def __init__(self, destinations: Destinations) -> None:
        self._destinations = destinations

    @cached_property
    def pagerduty(self) -> PagerdutyWithStreamingResponse:
        return PagerdutyWithStreamingResponse(self._destinations.pagerduty)


class AsyncDestinationsWithStreamingResponse:
    def __init__(self, destinations: AsyncDestinations) -> None:
        self._destinations = destinations

    @cached_property
    def pagerduty(self) -> AsyncPagerdutyWithStreamingResponse:
        return AsyncPagerdutyWithStreamingResponse(self._destinations.pagerduty)
