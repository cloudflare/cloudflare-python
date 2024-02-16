# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .tops import (
    Tops,
    AsyncTops,
    TopsWithRawResponse,
    AsyncTopsWithRawResponse,
    TopsWithStreamingResponse,
    AsyncTopsWithStreamingResponse,
)
from .leaks import (
    Leaks,
    AsyncLeaks,
    LeaksWithRawResponse,
    AsyncLeaksWithRawResponse,
    LeaksWithStreamingResponse,
    AsyncLeaksWithStreamingResponse,
)
from .routes import (
    Routes,
    AsyncRoutes,
    RoutesWithRawResponse,
    AsyncRoutesWithRawResponse,
    RoutesWithStreamingResponse,
    AsyncRoutesWithStreamingResponse,
)
from .hijacks import (
    Hijacks,
    AsyncHijacks,
    HijacksWithRawResponse,
    AsyncHijacksWithRawResponse,
    HijacksWithStreamingResponse,
    AsyncHijacksWithStreamingResponse,
)
from .tops.tops import Tops, AsyncTops
from ...._compat import cached_property
from .timeseries import (
    Timeseries,
    AsyncTimeseries,
    TimeseriesWithRawResponse,
    AsyncTimeseriesWithRawResponse,
    TimeseriesWithStreamingResponse,
    AsyncTimeseriesWithStreamingResponse,
)
from .leaks.leaks import Leaks, AsyncLeaks
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["BGP", "AsyncBGP"]


class BGP(SyncAPIResource):
    @cached_property
    def leaks(self) -> Leaks:
        return Leaks(self._client)

    @cached_property
    def timeseries(self) -> Timeseries:
        return Timeseries(self._client)

    @cached_property
    def tops(self) -> Tops:
        return Tops(self._client)

    @cached_property
    def hijacks(self) -> Hijacks:
        return Hijacks(self._client)

    @cached_property
    def routes(self) -> Routes:
        return Routes(self._client)

    @cached_property
    def with_raw_response(self) -> BGPWithRawResponse:
        return BGPWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BGPWithStreamingResponse:
        return BGPWithStreamingResponse(self)


class AsyncBGP(AsyncAPIResource):
    @cached_property
    def leaks(self) -> AsyncLeaks:
        return AsyncLeaks(self._client)

    @cached_property
    def timeseries(self) -> AsyncTimeseries:
        return AsyncTimeseries(self._client)

    @cached_property
    def tops(self) -> AsyncTops:
        return AsyncTops(self._client)

    @cached_property
    def hijacks(self) -> AsyncHijacks:
        return AsyncHijacks(self._client)

    @cached_property
    def routes(self) -> AsyncRoutes:
        return AsyncRoutes(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBGPWithRawResponse:
        return AsyncBGPWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBGPWithStreamingResponse:
        return AsyncBGPWithStreamingResponse(self)


class BGPWithRawResponse:
    def __init__(self, bgp: BGP) -> None:
        self._bgp = bgp

    @cached_property
    def leaks(self) -> LeaksWithRawResponse:
        return LeaksWithRawResponse(self._bgp.leaks)

    @cached_property
    def timeseries(self) -> TimeseriesWithRawResponse:
        return TimeseriesWithRawResponse(self._bgp.timeseries)

    @cached_property
    def tops(self) -> TopsWithRawResponse:
        return TopsWithRawResponse(self._bgp.tops)

    @cached_property
    def hijacks(self) -> HijacksWithRawResponse:
        return HijacksWithRawResponse(self._bgp.hijacks)

    @cached_property
    def routes(self) -> RoutesWithRawResponse:
        return RoutesWithRawResponse(self._bgp.routes)


class AsyncBGPWithRawResponse:
    def __init__(self, bgp: AsyncBGP) -> None:
        self._bgp = bgp

    @cached_property
    def leaks(self) -> AsyncLeaksWithRawResponse:
        return AsyncLeaksWithRawResponse(self._bgp.leaks)

    @cached_property
    def timeseries(self) -> AsyncTimeseriesWithRawResponse:
        return AsyncTimeseriesWithRawResponse(self._bgp.timeseries)

    @cached_property
    def tops(self) -> AsyncTopsWithRawResponse:
        return AsyncTopsWithRawResponse(self._bgp.tops)

    @cached_property
    def hijacks(self) -> AsyncHijacksWithRawResponse:
        return AsyncHijacksWithRawResponse(self._bgp.hijacks)

    @cached_property
    def routes(self) -> AsyncRoutesWithRawResponse:
        return AsyncRoutesWithRawResponse(self._bgp.routes)


class BGPWithStreamingResponse:
    def __init__(self, bgp: BGP) -> None:
        self._bgp = bgp

    @cached_property
    def leaks(self) -> LeaksWithStreamingResponse:
        return LeaksWithStreamingResponse(self._bgp.leaks)

    @cached_property
    def timeseries(self) -> TimeseriesWithStreamingResponse:
        return TimeseriesWithStreamingResponse(self._bgp.timeseries)

    @cached_property
    def tops(self) -> TopsWithStreamingResponse:
        return TopsWithStreamingResponse(self._bgp.tops)

    @cached_property
    def hijacks(self) -> HijacksWithStreamingResponse:
        return HijacksWithStreamingResponse(self._bgp.hijacks)

    @cached_property
    def routes(self) -> RoutesWithStreamingResponse:
        return RoutesWithStreamingResponse(self._bgp.routes)


class AsyncBGPWithStreamingResponse:
    def __init__(self, bgp: AsyncBGP) -> None:
        self._bgp = bgp

    @cached_property
    def leaks(self) -> AsyncLeaksWithStreamingResponse:
        return AsyncLeaksWithStreamingResponse(self._bgp.leaks)

    @cached_property
    def timeseries(self) -> AsyncTimeseriesWithStreamingResponse:
        return AsyncTimeseriesWithStreamingResponse(self._bgp.timeseries)

    @cached_property
    def tops(self) -> AsyncTopsWithStreamingResponse:
        return AsyncTopsWithStreamingResponse(self._bgp.tops)

    @cached_property
    def hijacks(self) -> AsyncHijacksWithStreamingResponse:
        return AsyncHijacksWithStreamingResponse(self._bgp.hijacks)

    @cached_property
    def routes(self) -> AsyncRoutesWithStreamingResponse:
        return AsyncRoutesWithStreamingResponse(self._bgp.routes)
