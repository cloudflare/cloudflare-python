# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .settings import (
    SettingsResource,
    AsyncSettingsResource,
    SettingsResourceWithRawResponse,
    AsyncSettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
    AsyncSettingsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["UniversalResource", "AsyncUniversalResource"]


class UniversalResource(SyncAPIResource):
    @cached_property
    def settings(self) -> SettingsResource:
        return SettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> UniversalResourceWithRawResponse:
        return UniversalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UniversalResourceWithStreamingResponse:
        return UniversalResourceWithStreamingResponse(self)


class AsyncUniversalResource(AsyncAPIResource):
    @cached_property
    def settings(self) -> AsyncSettingsResource:
        return AsyncSettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUniversalResourceWithRawResponse:
        return AsyncUniversalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUniversalResourceWithStreamingResponse:
        return AsyncUniversalResourceWithStreamingResponse(self)


class UniversalResourceWithRawResponse:
    def __init__(self, universal: UniversalResource) -> None:
        self._universal = universal

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self._universal.settings)


class AsyncUniversalResourceWithRawResponse:
    def __init__(self, universal: AsyncUniversalResource) -> None:
        self._universal = universal

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self._universal.settings)


class UniversalResourceWithStreamingResponse:
    def __init__(self, universal: UniversalResource) -> None:
        self._universal = universal

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self._universal.settings)


class AsyncUniversalResourceWithStreamingResponse:
    def __init__(self, universal: AsyncUniversalResource) -> None:
        self._universal = universal

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self._universal.settings)
