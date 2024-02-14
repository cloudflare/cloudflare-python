# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .connectivity_settings import (
    ConnectivitySettings,
    AsyncConnectivitySettings,
    ConnectivitySettingsWithRawResponse,
    AsyncConnectivitySettingsWithRawResponse,
    ConnectivitySettingsWithStreamingResponse,
    AsyncConnectivitySettingsWithStreamingResponse,
)

__all__ = ["Zerotrust", "AsyncZerotrust"]


class Zerotrust(SyncAPIResource):
    @cached_property
    def connectivity_settings(self) -> ConnectivitySettings:
        return ConnectivitySettings(self._client)

    @cached_property
    def with_raw_response(self) -> ZerotrustWithRawResponse:
        return ZerotrustWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ZerotrustWithStreamingResponse:
        return ZerotrustWithStreamingResponse(self)


class AsyncZerotrust(AsyncAPIResource):
    @cached_property
    def connectivity_settings(self) -> AsyncConnectivitySettings:
        return AsyncConnectivitySettings(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncZerotrustWithRawResponse:
        return AsyncZerotrustWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncZerotrustWithStreamingResponse:
        return AsyncZerotrustWithStreamingResponse(self)


class ZerotrustWithRawResponse:
    def __init__(self, zerotrust: Zerotrust) -> None:
        self._zerotrust = zerotrust

    @cached_property
    def connectivity_settings(self) -> ConnectivitySettingsWithRawResponse:
        return ConnectivitySettingsWithRawResponse(self._zerotrust.connectivity_settings)


class AsyncZerotrustWithRawResponse:
    def __init__(self, zerotrust: AsyncZerotrust) -> None:
        self._zerotrust = zerotrust

    @cached_property
    def connectivity_settings(self) -> AsyncConnectivitySettingsWithRawResponse:
        return AsyncConnectivitySettingsWithRawResponse(self._zerotrust.connectivity_settings)


class ZerotrustWithStreamingResponse:
    def __init__(self, zerotrust: Zerotrust) -> None:
        self._zerotrust = zerotrust

    @cached_property
    def connectivity_settings(self) -> ConnectivitySettingsWithStreamingResponse:
        return ConnectivitySettingsWithStreamingResponse(self._zerotrust.connectivity_settings)


class AsyncZerotrustWithStreamingResponse:
    def __init__(self, zerotrust: AsyncZerotrust) -> None:
        self._zerotrust = zerotrust

    @cached_property
    def connectivity_settings(self) -> AsyncConnectivitySettingsWithStreamingResponse:
        return AsyncConnectivitySettingsWithStreamingResponse(self._zerotrust.connectivity_settings)
