# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .transformations import (
    TransformationsResource,
    AsyncTransformationsResource,
    TransformationsResourceWithRawResponse,
    AsyncTransformationsResourceWithRawResponse,
    TransformationsResourceWithStreamingResponse,
    AsyncTransformationsResourceWithStreamingResponse,
)

__all__ = ["SpeedSettingsResource", "AsyncSpeedSettingsResource"]


class SpeedSettingsResource(SyncAPIResource):
    @cached_property
    def transformations(self) -> TransformationsResource:
        return TransformationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SpeedSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SpeedSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpeedSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SpeedSettingsResourceWithStreamingResponse(self)


class AsyncSpeedSettingsResource(AsyncAPIResource):
    @cached_property
    def transformations(self) -> AsyncTransformationsResource:
        return AsyncTransformationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSpeedSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSpeedSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpeedSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSpeedSettingsResourceWithStreamingResponse(self)


class SpeedSettingsResourceWithRawResponse:
    def __init__(self, speed_settings: SpeedSettingsResource) -> None:
        self._speed_settings = speed_settings

    @cached_property
    def transformations(self) -> TransformationsResourceWithRawResponse:
        return TransformationsResourceWithRawResponse(self._speed_settings.transformations)


class AsyncSpeedSettingsResourceWithRawResponse:
    def __init__(self, speed_settings: AsyncSpeedSettingsResource) -> None:
        self._speed_settings = speed_settings

    @cached_property
    def transformations(self) -> AsyncTransformationsResourceWithRawResponse:
        return AsyncTransformationsResourceWithRawResponse(self._speed_settings.transformations)


class SpeedSettingsResourceWithStreamingResponse:
    def __init__(self, speed_settings: SpeedSettingsResource) -> None:
        self._speed_settings = speed_settings

    @cached_property
    def transformations(self) -> TransformationsResourceWithStreamingResponse:
        return TransformationsResourceWithStreamingResponse(self._speed_settings.transformations)


class AsyncSpeedSettingsResourceWithStreamingResponse:
    def __init__(self, speed_settings: AsyncSpeedSettingsResource) -> None:
        self._speed_settings = speed_settings

    @cached_property
    def transformations(self) -> AsyncTransformationsResourceWithStreamingResponse:
        return AsyncTransformationsResourceWithStreamingResponse(self._speed_settings.transformations)
