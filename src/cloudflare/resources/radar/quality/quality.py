# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .iqi import (
    IQI,
    AsyncIQI,
    IQIWithRawResponse,
    AsyncIQIWithRawResponse,
    IQIWithStreamingResponse,
    AsyncIQIWithStreamingResponse,
)
from .speed import (
    Speed,
    AsyncSpeed,
    SpeedWithRawResponse,
    AsyncSpeedWithRawResponse,
    SpeedWithStreamingResponse,
    AsyncSpeedWithStreamingResponse,
)
from ...._compat import cached_property
from .speed.speed import Speed, AsyncSpeed
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Quality", "AsyncQuality"]


class Quality(SyncAPIResource):
    @cached_property
    def iqi(self) -> IQI:
        return IQI(self._client)

    @cached_property
    def speed(self) -> Speed:
        return Speed(self._client)

    @cached_property
    def with_raw_response(self) -> QualityWithRawResponse:
        return QualityWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QualityWithStreamingResponse:
        return QualityWithStreamingResponse(self)


class AsyncQuality(AsyncAPIResource):
    @cached_property
    def iqi(self) -> AsyncIQI:
        return AsyncIQI(self._client)

    @cached_property
    def speed(self) -> AsyncSpeed:
        return AsyncSpeed(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncQualityWithRawResponse:
        return AsyncQualityWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQualityWithStreamingResponse:
        return AsyncQualityWithStreamingResponse(self)


class QualityWithRawResponse:
    def __init__(self, quality: Quality) -> None:
        self._quality = quality

    @cached_property
    def iqi(self) -> IQIWithRawResponse:
        return IQIWithRawResponse(self._quality.iqi)

    @cached_property
    def speed(self) -> SpeedWithRawResponse:
        return SpeedWithRawResponse(self._quality.speed)


class AsyncQualityWithRawResponse:
    def __init__(self, quality: AsyncQuality) -> None:
        self._quality = quality

    @cached_property
    def iqi(self) -> AsyncIQIWithRawResponse:
        return AsyncIQIWithRawResponse(self._quality.iqi)

    @cached_property
    def speed(self) -> AsyncSpeedWithRawResponse:
        return AsyncSpeedWithRawResponse(self._quality.speed)


class QualityWithStreamingResponse:
    def __init__(self, quality: Quality) -> None:
        self._quality = quality

    @cached_property
    def iqi(self) -> IQIWithStreamingResponse:
        return IQIWithStreamingResponse(self._quality.iqi)

    @cached_property
    def speed(self) -> SpeedWithStreamingResponse:
        return SpeedWithStreamingResponse(self._quality.speed)


class AsyncQualityWithStreamingResponse:
    def __init__(self, quality: AsyncQuality) -> None:
        self._quality = quality

    @cached_property
    def iqi(self) -> AsyncIQIWithStreamingResponse:
        return AsyncIQIWithStreamingResponse(self._quality.iqi)

    @cached_property
    def speed(self) -> AsyncSpeedWithStreamingResponse:
        return AsyncSpeedWithStreamingResponse(self._quality.speed)
