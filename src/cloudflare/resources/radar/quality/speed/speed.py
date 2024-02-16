# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .top import (
    Top,
    AsyncTop,
    TopWithRawResponse,
    AsyncTopWithRawResponse,
    TopWithStreamingResponse,
    AsyncTopWithStreamingResponse,
)
from .summary import (
    Summary,
    AsyncSummary,
    SummaryWithRawResponse,
    AsyncSummaryWithRawResponse,
    SummaryWithStreamingResponse,
    AsyncSummaryWithStreamingResponse,
)
from .top.top import Top, AsyncTop
from .histogram import (
    Histogram,
    AsyncHistogram,
    HistogramWithRawResponse,
    AsyncHistogramWithRawResponse,
    HistogramWithStreamingResponse,
    AsyncHistogramWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Speed", "AsyncSpeed"]


class Speed(SyncAPIResource):
    @cached_property
    def histogram(self) -> Histogram:
        return Histogram(self._client)

    @cached_property
    def summary(self) -> Summary:
        return Summary(self._client)

    @cached_property
    def top(self) -> Top:
        return Top(self._client)

    @cached_property
    def with_raw_response(self) -> SpeedWithRawResponse:
        return SpeedWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpeedWithStreamingResponse:
        return SpeedWithStreamingResponse(self)


class AsyncSpeed(AsyncAPIResource):
    @cached_property
    def histogram(self) -> AsyncHistogram:
        return AsyncHistogram(self._client)

    @cached_property
    def summary(self) -> AsyncSummary:
        return AsyncSummary(self._client)

    @cached_property
    def top(self) -> AsyncTop:
        return AsyncTop(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSpeedWithRawResponse:
        return AsyncSpeedWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpeedWithStreamingResponse:
        return AsyncSpeedWithStreamingResponse(self)


class SpeedWithRawResponse:
    def __init__(self, speed: Speed) -> None:
        self._speed = speed

    @cached_property
    def histogram(self) -> HistogramWithRawResponse:
        return HistogramWithRawResponse(self._speed.histogram)

    @cached_property
    def summary(self) -> SummaryWithRawResponse:
        return SummaryWithRawResponse(self._speed.summary)

    @cached_property
    def top(self) -> TopWithRawResponse:
        return TopWithRawResponse(self._speed.top)


class AsyncSpeedWithRawResponse:
    def __init__(self, speed: AsyncSpeed) -> None:
        self._speed = speed

    @cached_property
    def histogram(self) -> AsyncHistogramWithRawResponse:
        return AsyncHistogramWithRawResponse(self._speed.histogram)

    @cached_property
    def summary(self) -> AsyncSummaryWithRawResponse:
        return AsyncSummaryWithRawResponse(self._speed.summary)

    @cached_property
    def top(self) -> AsyncTopWithRawResponse:
        return AsyncTopWithRawResponse(self._speed.top)


class SpeedWithStreamingResponse:
    def __init__(self, speed: Speed) -> None:
        self._speed = speed

    @cached_property
    def histogram(self) -> HistogramWithStreamingResponse:
        return HistogramWithStreamingResponse(self._speed.histogram)

    @cached_property
    def summary(self) -> SummaryWithStreamingResponse:
        return SummaryWithStreamingResponse(self._speed.summary)

    @cached_property
    def top(self) -> TopWithStreamingResponse:
        return TopWithStreamingResponse(self._speed.top)


class AsyncSpeedWithStreamingResponse:
    def __init__(self, speed: AsyncSpeed) -> None:
        self._speed = speed

    @cached_property
    def histogram(self) -> AsyncHistogramWithStreamingResponse:
        return AsyncHistogramWithStreamingResponse(self._speed.histogram)

    @cached_property
    def summary(self) -> AsyncSummaryWithStreamingResponse:
        return AsyncSummaryWithStreamingResponse(self._speed.summary)

    @cached_property
    def top(self) -> AsyncTopWithStreamingResponse:
        return AsyncTopWithStreamingResponse(self._speed.top)
