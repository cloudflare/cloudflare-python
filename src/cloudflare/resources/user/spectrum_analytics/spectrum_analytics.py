# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from .zones.zones import (
    ZonesResource,
    AsyncZonesResource,
    ZonesResourceWithRawResponse,
    AsyncZonesResourceWithRawResponse,
    ZonesResourceWithStreamingResponse,
    AsyncZonesResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["SpectrumAnalyticsResource", "AsyncSpectrumAnalyticsResource"]


class SpectrumAnalyticsResource(SyncAPIResource):
    @cached_property
    def zones(self) -> ZonesResource:
        return ZonesResource(self._client)

    @cached_property
    def with_raw_response(self) -> SpectrumAnalyticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SpectrumAnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpectrumAnalyticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SpectrumAnalyticsResourceWithStreamingResponse(self)


class AsyncSpectrumAnalyticsResource(AsyncAPIResource):
    @cached_property
    def zones(self) -> AsyncZonesResource:
        return AsyncZonesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSpectrumAnalyticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSpectrumAnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpectrumAnalyticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSpectrumAnalyticsResourceWithStreamingResponse(self)


class SpectrumAnalyticsResourceWithRawResponse:
    def __init__(self, spectrum_analytics: SpectrumAnalyticsResource) -> None:
        self._spectrum_analytics = spectrum_analytics

    @cached_property
    def zones(self) -> ZonesResourceWithRawResponse:
        return ZonesResourceWithRawResponse(self._spectrum_analytics.zones)


class AsyncSpectrumAnalyticsResourceWithRawResponse:
    def __init__(self, spectrum_analytics: AsyncSpectrumAnalyticsResource) -> None:
        self._spectrum_analytics = spectrum_analytics

    @cached_property
    def zones(self) -> AsyncZonesResourceWithRawResponse:
        return AsyncZonesResourceWithRawResponse(self._spectrum_analytics.zones)


class SpectrumAnalyticsResourceWithStreamingResponse:
    def __init__(self, spectrum_analytics: SpectrumAnalyticsResource) -> None:
        self._spectrum_analytics = spectrum_analytics

    @cached_property
    def zones(self) -> ZonesResourceWithStreamingResponse:
        return ZonesResourceWithStreamingResponse(self._spectrum_analytics.zones)


class AsyncSpectrumAnalyticsResourceWithStreamingResponse:
    def __init__(self, spectrum_analytics: AsyncSpectrumAnalyticsResource) -> None:
        self._spectrum_analytics = spectrum_analytics

    @cached_property
    def zones(self) -> AsyncZonesResourceWithStreamingResponse:
        return AsyncZonesResourceWithStreamingResponse(self._spectrum_analytics.zones)
