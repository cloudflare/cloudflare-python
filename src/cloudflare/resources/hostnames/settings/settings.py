# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .tls import (
    TLS,
    AsyncTLS,
    TLSWithRawResponse,
    AsyncTLSWithRawResponse,
    TLSWithStreamingResponse,
    AsyncTLSWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Settings", "AsyncSettings"]


class Settings(SyncAPIResource):
    @cached_property
    def tls(self) -> TLS:
        return TLS(self._client)

    @cached_property
    def with_raw_response(self) -> SettingsWithRawResponse:
        return SettingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsWithStreamingResponse:
        return SettingsWithStreamingResponse(self)


class AsyncSettings(AsyncAPIResource):
    @cached_property
    def tls(self) -> AsyncTLS:
        return AsyncTLS(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSettingsWithRawResponse:
        return AsyncSettingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsWithStreamingResponse:
        return AsyncSettingsWithStreamingResponse(self)


class SettingsWithRawResponse:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    @cached_property
    def tls(self) -> TLSWithRawResponse:
        return TLSWithRawResponse(self._settings.tls)


class AsyncSettingsWithRawResponse:
    def __init__(self, settings: AsyncSettings) -> None:
        self._settings = settings

    @cached_property
    def tls(self) -> AsyncTLSWithRawResponse:
        return AsyncTLSWithRawResponse(self._settings.tls)


class SettingsWithStreamingResponse:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    @cached_property
    def tls(self) -> TLSWithStreamingResponse:
        return TLSWithStreamingResponse(self._settings.tls)


class AsyncSettingsWithStreamingResponse:
    def __init__(self, settings: AsyncSettings) -> None:
        self._settings = settings

    @cached_property
    def tls(self) -> AsyncTLSWithStreamingResponse:
        return AsyncTLSWithStreamingResponse(self._settings.tls)
