# File generated from our OpenAPI spec by Stainless.

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

__all__ = ["Universals", "AsyncUniversals"]


class Universals(SyncAPIResource):
    @cached_property
    def settings(self) -> Settings:
        return Settings(self._client)

    @cached_property
    def with_raw_response(self) -> UniversalsWithRawResponse:
        return UniversalsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UniversalsWithStreamingResponse:
        return UniversalsWithStreamingResponse(self)


class AsyncUniversals(AsyncAPIResource):
    @cached_property
    def settings(self) -> AsyncSettings:
        return AsyncSettings(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUniversalsWithRawResponse:
        return AsyncUniversalsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUniversalsWithStreamingResponse:
        return AsyncUniversalsWithStreamingResponse(self)


class UniversalsWithRawResponse:
    def __init__(self, universals: Universals) -> None:
        self._universals = universals

    @cached_property
    def settings(self) -> SettingsWithRawResponse:
        return SettingsWithRawResponse(self._universals.settings)


class AsyncUniversalsWithRawResponse:
    def __init__(self, universals: AsyncUniversals) -> None:
        self._universals = universals

    @cached_property
    def settings(self) -> AsyncSettingsWithRawResponse:
        return AsyncSettingsWithRawResponse(self._universals.settings)


class UniversalsWithStreamingResponse:
    def __init__(self, universals: Universals) -> None:
        self._universals = universals

    @cached_property
    def settings(self) -> SettingsWithStreamingResponse:
        return SettingsWithStreamingResponse(self._universals.settings)


class AsyncUniversalsWithStreamingResponse:
    def __init__(self, universals: AsyncUniversals) -> None:
        self._universals = universals

    @cached_property
    def settings(self) -> AsyncSettingsWithStreamingResponse:
        return AsyncSettingsWithStreamingResponse(self._universals.settings)
