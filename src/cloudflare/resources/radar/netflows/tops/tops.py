# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .ases import (
    Ases,
    AsyncAses,
    AsesWithRawResponse,
    AsyncAsesWithRawResponse,
    AsesWithStreamingResponse,
    AsyncAsesWithStreamingResponse,
)
from .locations import (
    Locations,
    AsyncLocations,
    LocationsWithRawResponse,
    AsyncLocationsWithRawResponse,
    LocationsWithStreamingResponse,
    AsyncLocationsWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Tops", "AsyncTops"]


class Tops(SyncAPIResource):
    @cached_property
    def ases(self) -> Ases:
        return Ases(self._client)

    @cached_property
    def locations(self) -> Locations:
        return Locations(self._client)

    @cached_property
    def with_raw_response(self) -> TopsWithRawResponse:
        return TopsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TopsWithStreamingResponse:
        return TopsWithStreamingResponse(self)


class AsyncTops(AsyncAPIResource):
    @cached_property
    def ases(self) -> AsyncAses:
        return AsyncAses(self._client)

    @cached_property
    def locations(self) -> AsyncLocations:
        return AsyncLocations(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTopsWithRawResponse:
        return AsyncTopsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTopsWithStreamingResponse:
        return AsyncTopsWithStreamingResponse(self)


class TopsWithRawResponse:
    def __init__(self, tops: Tops) -> None:
        self._tops = tops

    @cached_property
    def ases(self) -> AsesWithRawResponse:
        return AsesWithRawResponse(self._tops.ases)

    @cached_property
    def locations(self) -> LocationsWithRawResponse:
        return LocationsWithRawResponse(self._tops.locations)


class AsyncTopsWithRawResponse:
    def __init__(self, tops: AsyncTops) -> None:
        self._tops = tops

    @cached_property
    def ases(self) -> AsyncAsesWithRawResponse:
        return AsyncAsesWithRawResponse(self._tops.ases)

    @cached_property
    def locations(self) -> AsyncLocationsWithRawResponse:
        return AsyncLocationsWithRawResponse(self._tops.locations)


class TopsWithStreamingResponse:
    def __init__(self, tops: Tops) -> None:
        self._tops = tops

    @cached_property
    def ases(self) -> AsesWithStreamingResponse:
        return AsesWithStreamingResponse(self._tops.ases)

    @cached_property
    def locations(self) -> LocationsWithStreamingResponse:
        return LocationsWithStreamingResponse(self._tops.locations)


class AsyncTopsWithStreamingResponse:
    def __init__(self, tops: AsyncTops) -> None:
        self._tops = tops

    @cached_property
    def ases(self) -> AsyncAsesWithStreamingResponse:
        return AsyncAsesWithStreamingResponse(self._tops.ases)

    @cached_property
    def locations(self) -> AsyncLocationsWithStreamingResponse:
        return AsyncLocationsWithStreamingResponse(self._tops.locations)
