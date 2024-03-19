# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .apps import (
    Apps,
    AsyncApps,
    AppsWithRawResponse,
    AsyncAppsWithRawResponse,
    AppsWithStreamingResponse,
    AsyncAppsWithStreamingResponse,
)
from ..._compat import cached_property
from .analytics import (
    Analytics,
    AsyncAnalytics,
    AnalyticsWithRawResponse,
    AsyncAnalyticsWithRawResponse,
    AnalyticsWithStreamingResponse,
    AsyncAnalyticsWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .analytics.analytics import Analytics, AsyncAnalytics

__all__ = ["Spectrum", "AsyncSpectrum"]


class Spectrum(SyncAPIResource):
    @cached_property
    def analytics(self) -> Analytics:
        return Analytics(self._client)

    @cached_property
    def apps(self) -> Apps:
        return Apps(self._client)

    @cached_property
    def with_raw_response(self) -> SpectrumWithRawResponse:
        return SpectrumWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpectrumWithStreamingResponse:
        return SpectrumWithStreamingResponse(self)


class AsyncSpectrum(AsyncAPIResource):
    @cached_property
    def analytics(self) -> AsyncAnalytics:
        return AsyncAnalytics(self._client)

    @cached_property
    def apps(self) -> AsyncApps:
        return AsyncApps(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSpectrumWithRawResponse:
        return AsyncSpectrumWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpectrumWithStreamingResponse:
        return AsyncSpectrumWithStreamingResponse(self)


class SpectrumWithRawResponse:
    def __init__(self, spectrum: Spectrum) -> None:
        self._spectrum = spectrum

    @cached_property
    def analytics(self) -> AnalyticsWithRawResponse:
        return AnalyticsWithRawResponse(self._spectrum.analytics)

    @cached_property
    def apps(self) -> AppsWithRawResponse:
        return AppsWithRawResponse(self._spectrum.apps)


class AsyncSpectrumWithRawResponse:
    def __init__(self, spectrum: AsyncSpectrum) -> None:
        self._spectrum = spectrum

    @cached_property
    def analytics(self) -> AsyncAnalyticsWithRawResponse:
        return AsyncAnalyticsWithRawResponse(self._spectrum.analytics)

    @cached_property
    def apps(self) -> AsyncAppsWithRawResponse:
        return AsyncAppsWithRawResponse(self._spectrum.apps)


class SpectrumWithStreamingResponse:
    def __init__(self, spectrum: Spectrum) -> None:
        self._spectrum = spectrum

    @cached_property
    def analytics(self) -> AnalyticsWithStreamingResponse:
        return AnalyticsWithStreamingResponse(self._spectrum.analytics)

    @cached_property
    def apps(self) -> AppsWithStreamingResponse:
        return AppsWithStreamingResponse(self._spectrum.apps)


class AsyncSpectrumWithStreamingResponse:
    def __init__(self, spectrum: AsyncSpectrum) -> None:
        self._spectrum = spectrum

    @cached_property
    def analytics(self) -> AsyncAnalyticsWithStreamingResponse:
        return AsyncAnalyticsWithStreamingResponse(self._spectrum.analytics)

    @cached_property
    def apps(self) -> AsyncAppsWithStreamingResponse:
        return AsyncAppsWithStreamingResponse(self._spectrum.apps)
