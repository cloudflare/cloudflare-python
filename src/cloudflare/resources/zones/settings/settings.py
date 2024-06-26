# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .font_settings import (
    FontSettingsResource,
    AsyncFontSettingsResource,
    FontSettingsResourceWithRawResponse,
    AsyncFontSettingsResourceWithRawResponse,
    FontSettingsResourceWithStreamingResponse,
    AsyncFontSettingsResourceWithStreamingResponse,
)
from .origin_max_http_version import (
    OriginMaxHTTPVersionResource,
    AsyncOriginMaxHTTPVersionResource,
    OriginMaxHTTPVersionResourceWithRawResponse,
    AsyncOriginMaxHTTPVersionResourceWithRawResponse,
    OriginMaxHTTPVersionResourceWithStreamingResponse,
    AsyncOriginMaxHTTPVersionResourceWithStreamingResponse,
)

__all__ = ["SettingsResource", "AsyncSettingsResource"]


class SettingsResource(SyncAPIResource):
    @cached_property
    def origin_max_http_version(self) -> OriginMaxHTTPVersionResource:
        return OriginMaxHTTPVersionResource(self._client)

    @cached_property
    def font_settings(self) -> FontSettingsResource:
        return FontSettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self)


class AsyncSettingsResource(AsyncAPIResource):
    @cached_property
    def origin_max_http_version(self) -> AsyncOriginMaxHTTPVersionResource:
        return AsyncOriginMaxHTTPVersionResource(self._client)

    @cached_property
    def font_settings(self) -> AsyncFontSettingsResource:
        return AsyncFontSettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self)


class SettingsResourceWithRawResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

    @cached_property
    def origin_max_http_version(self) -> OriginMaxHTTPVersionResourceWithRawResponse:
        return OriginMaxHTTPVersionResourceWithRawResponse(self._settings.origin_max_http_version)

    @cached_property
    def font_settings(self) -> FontSettingsResourceWithRawResponse:
        return FontSettingsResourceWithRawResponse(self._settings.font_settings)


class AsyncSettingsResourceWithRawResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

    @cached_property
    def origin_max_http_version(self) -> AsyncOriginMaxHTTPVersionResourceWithRawResponse:
        return AsyncOriginMaxHTTPVersionResourceWithRawResponse(self._settings.origin_max_http_version)

    @cached_property
    def font_settings(self) -> AsyncFontSettingsResourceWithRawResponse:
        return AsyncFontSettingsResourceWithRawResponse(self._settings.font_settings)


class SettingsResourceWithStreamingResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

    @cached_property
    def origin_max_http_version(self) -> OriginMaxHTTPVersionResourceWithStreamingResponse:
        return OriginMaxHTTPVersionResourceWithStreamingResponse(self._settings.origin_max_http_version)

    @cached_property
    def font_settings(self) -> FontSettingsResourceWithStreamingResponse:
        return FontSettingsResourceWithStreamingResponse(self._settings.font_settings)


class AsyncSettingsResourceWithStreamingResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

    @cached_property
    def origin_max_http_version(self) -> AsyncOriginMaxHTTPVersionResourceWithStreamingResponse:
        return AsyncOriginMaxHTTPVersionResourceWithStreamingResponse(self._settings.origin_max_http_version)

    @cached_property
    def font_settings(self) -> AsyncFontSettingsResourceWithStreamingResponse:
        return AsyncFontSettingsResourceWithStreamingResponse(self._settings.font_settings)
