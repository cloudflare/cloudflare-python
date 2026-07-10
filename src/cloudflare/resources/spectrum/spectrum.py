# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .apps import (
    AppsResource,
    AsyncAppsResource,
    AppsResourceWithRawResponse,
    AsyncAppsResourceWithRawResponse,
    AppsResourceWithStreamingResponse,
    AsyncAppsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .analytics.analytics import (
    AnalyticsResource,
    AsyncAnalyticsResource,
    AnalyticsResourceWithRawResponse,
    AsyncAnalyticsResourceWithRawResponse,
    AnalyticsResourceWithStreamingResponse,
    AsyncAnalyticsResourceWithStreamingResponse,
)

__all__ = ["SpectrumResource", "AsyncSpectrumResource"]


class SpectrumResource(SyncAPIResource):
    @cached_property
    def analytics(self) -> AnalyticsResource:
        return AnalyticsResource(self._client)

    @cached_property
    def apps(self) -> AppsResource:
        return AppsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SpectrumResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SpectrumResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpectrumResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SpectrumResourceWithStreamingResponse(self)


class AsyncSpectrumResource(AsyncAPIResource):
    @cached_property
    def analytics(self) -> AsyncAnalyticsResource:
        return AsyncAnalyticsResource(self._client)

    @cached_property
    def apps(self) -> AsyncAppsResource:
        return AsyncAppsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSpectrumResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSpectrumResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpectrumResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSpectrumResourceWithStreamingResponse(self)


class SpectrumResourceWithRawResponse:
    def __init__(self, spectrum: SpectrumResource) -> None:
        self._spectrum = spectrum

    @cached_property
    def analytics(self) -> AnalyticsResourceWithRawResponse:
        return AnalyticsResourceWithRawResponse(self._spectrum.analytics)

    @cached_property
    def apps(self) -> AppsResourceWithRawResponse:
        return AppsResourceWithRawResponse(self._spectrum.apps)


class AsyncSpectrumResourceWithRawResponse:
    def __init__(self, spectrum: AsyncSpectrumResource) -> None:
        self._spectrum = spectrum

    @cached_property
    def analytics(self) -> AsyncAnalyticsResourceWithRawResponse:
        return AsyncAnalyticsResourceWithRawResponse(self._spectrum.analytics)

    @cached_property
    def apps(self) -> AsyncAppsResourceWithRawResponse:
        return AsyncAppsResourceWithRawResponse(self._spectrum.apps)


class SpectrumResourceWithStreamingResponse:
    def __init__(self, spectrum: SpectrumResource) -> None:
        self._spectrum = spectrum

    @cached_property
    def analytics(self) -> AnalyticsResourceWithStreamingResponse:
        return AnalyticsResourceWithStreamingResponse(self._spectrum.analytics)

    @cached_property
    def apps(self) -> AppsResourceWithStreamingResponse:
        return AppsResourceWithStreamingResponse(self._spectrum.apps)


class AsyncSpectrumResourceWithStreamingResponse:
    def __init__(self, spectrum: AsyncSpectrumResource) -> None:
        self._spectrum = spectrum

    @cached_property
    def analytics(self) -> AsyncAnalyticsResourceWithStreamingResponse:
        return AsyncAnalyticsResourceWithStreamingResponse(self._spectrum.analytics)

    @cached_property
    def apps(self) -> AsyncAppsResourceWithStreamingResponse:
        return AsyncAppsResourceWithStreamingResponse(self._spectrum.apps)
