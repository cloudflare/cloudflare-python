# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .iqi import (
    IQIResource,
    AsyncIQIResource,
    IQIResourceWithRawResponse,
    AsyncIQIResourceWithRawResponse,
    IQIResourceWithStreamingResponse,
    AsyncIQIResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .speed.speed import (
    SpeedResource,
    AsyncSpeedResource,
    SpeedResourceWithRawResponse,
    AsyncSpeedResourceWithRawResponse,
    SpeedResourceWithStreamingResponse,
    AsyncSpeedResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["QualityResource", "AsyncQualityResource"]


class QualityResource(SyncAPIResource):
    @cached_property
    def iqi(self) -> IQIResource:
        return IQIResource(self._client)

    @cached_property
    def speed(self) -> SpeedResource:
        return SpeedResource(self._client)

    @cached_property
    def with_raw_response(self) -> QualityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return QualityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QualityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return QualityResourceWithStreamingResponse(self)


class AsyncQualityResource(AsyncAPIResource):
    @cached_property
    def iqi(self) -> AsyncIQIResource:
        return AsyncIQIResource(self._client)

    @cached_property
    def speed(self) -> AsyncSpeedResource:
        return AsyncSpeedResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncQualityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQualityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQualityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncQualityResourceWithStreamingResponse(self)


class QualityResourceWithRawResponse:
    def __init__(self, quality: QualityResource) -> None:
        self._quality = quality

    @cached_property
    def iqi(self) -> IQIResourceWithRawResponse:
        return IQIResourceWithRawResponse(self._quality.iqi)

    @cached_property
    def speed(self) -> SpeedResourceWithRawResponse:
        return SpeedResourceWithRawResponse(self._quality.speed)


class AsyncQualityResourceWithRawResponse:
    def __init__(self, quality: AsyncQualityResource) -> None:
        self._quality = quality

    @cached_property
    def iqi(self) -> AsyncIQIResourceWithRawResponse:
        return AsyncIQIResourceWithRawResponse(self._quality.iqi)

    @cached_property
    def speed(self) -> AsyncSpeedResourceWithRawResponse:
        return AsyncSpeedResourceWithRawResponse(self._quality.speed)


class QualityResourceWithStreamingResponse:
    def __init__(self, quality: QualityResource) -> None:
        self._quality = quality

    @cached_property
    def iqi(self) -> IQIResourceWithStreamingResponse:
        return IQIResourceWithStreamingResponse(self._quality.iqi)

    @cached_property
    def speed(self) -> SpeedResourceWithStreamingResponse:
        return SpeedResourceWithStreamingResponse(self._quality.speed)


class AsyncQualityResourceWithStreamingResponse:
    def __init__(self, quality: AsyncQualityResource) -> None:
        self._quality = quality

    @cached_property
    def iqi(self) -> AsyncIQIResourceWithStreamingResponse:
        return AsyncIQIResourceWithStreamingResponse(self._quality.iqi)

    @cached_property
    def speed(self) -> AsyncSpeedResourceWithStreamingResponse:
        return AsyncSpeedResourceWithStreamingResponse(self._quality.speed)
