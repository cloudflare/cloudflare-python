# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .exists import (
    Exists,
    AsyncExists,
    ExistsWithRawResponse,
    AsyncExistsWithRawResponse,
    ExistsWithStreamingResponse,
    AsyncExistsWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Destinations", "AsyncDestinations"]


class Destinations(SyncAPIResource):
    @cached_property
    def exists(self) -> Exists:
        return Exists(self._client)

    @cached_property
    def with_raw_response(self) -> DestinationsWithRawResponse:
        return DestinationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DestinationsWithStreamingResponse:
        return DestinationsWithStreamingResponse(self)


class AsyncDestinations(AsyncAPIResource):
    @cached_property
    def exists(self) -> AsyncExists:
        return AsyncExists(self._client)

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
    def exists(self) -> ExistsWithRawResponse:
        return ExistsWithRawResponse(self._destinations.exists)


class AsyncDestinationsWithRawResponse:
    def __init__(self, destinations: AsyncDestinations) -> None:
        self._destinations = destinations

    @cached_property
    def exists(self) -> AsyncExistsWithRawResponse:
        return AsyncExistsWithRawResponse(self._destinations.exists)


class DestinationsWithStreamingResponse:
    def __init__(self, destinations: Destinations) -> None:
        self._destinations = destinations

    @cached_property
    def exists(self) -> ExistsWithStreamingResponse:
        return ExistsWithStreamingResponse(self._destinations.exists)


class AsyncDestinationsWithStreamingResponse:
    def __init__(self, destinations: AsyncDestinations) -> None:
        self._destinations = destinations

    @cached_property
    def exists(self) -> AsyncExistsWithStreamingResponse:
        return AsyncExistsWithStreamingResponse(self._destinations.exists)
