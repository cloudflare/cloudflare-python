# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .settings import (
    Settings,
    AsyncSettings,
    SettingsWithRawResponse,
    AsyncSettingsWithRawResponse,
    SettingsWithStreamingResponse,
    AsyncSettingsWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Universal", "AsyncUniversal"]


class Universal(SyncAPIResource):
    @cached_property
    def settings(self) -> Settings:
        return Settings(self._client)

    @cached_property
    def with_raw_response(self) -> UniversalWithRawResponse:
        return UniversalWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UniversalWithStreamingResponse:
        return UniversalWithStreamingResponse(self)


class AsyncUniversal(AsyncAPIResource):
    @cached_property
    def settings(self) -> AsyncSettings:
        return AsyncSettings(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUniversalWithRawResponse:
        return AsyncUniversalWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUniversalWithStreamingResponse:
        return AsyncUniversalWithStreamingResponse(self)


class UniversalWithRawResponse:
    def __init__(self, universal: Universal) -> None:
        self._universal = universal

    @cached_property
    def settings(self) -> SettingsWithRawResponse:
        return SettingsWithRawResponse(self._universal.settings)


class AsyncUniversalWithRawResponse:
    def __init__(self, universal: AsyncUniversal) -> None:
        self._universal = universal

    @cached_property
    def settings(self) -> AsyncSettingsWithRawResponse:
        return AsyncSettingsWithRawResponse(self._universal.settings)


class UniversalWithStreamingResponse:
    def __init__(self, universal: Universal) -> None:
        self._universal = universal

    @cached_property
    def settings(self) -> SettingsWithStreamingResponse:
        return SettingsWithStreamingResponse(self._universal.settings)


class AsyncUniversalWithStreamingResponse:
    def __init__(self, universal: AsyncUniversal) -> None:
        self._universal = universal

    @cached_property
    def settings(self) -> AsyncSettingsWithStreamingResponse:
        return AsyncSettingsWithStreamingResponse(self._universal.settings)
