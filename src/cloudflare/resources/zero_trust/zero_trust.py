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

__all__ = ["ZeroTrust", "AsyncZeroTrust"]


class ZeroTrust(SyncAPIResource):
    @cached_property
    def connectivity_settings(self) -> ConnectivitySettings:
        return ConnectivitySettings(self._client)

    @cached_property
    def with_raw_response(self) -> ZeroTrustWithRawResponse:
        return ZeroTrustWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ZeroTrustWithStreamingResponse:
        return ZeroTrustWithStreamingResponse(self)


class AsyncZeroTrust(AsyncAPIResource):
    @cached_property
    def connectivity_settings(self) -> AsyncConnectivitySettings:
        return AsyncConnectivitySettings(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncZeroTrustWithRawResponse:
        return AsyncZeroTrustWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncZeroTrustWithStreamingResponse:
        return AsyncZeroTrustWithStreamingResponse(self)


class ZeroTrustWithRawResponse:
    def __init__(self, zero_trust: ZeroTrust) -> None:
        self._zero_trust = zero_trust

    @cached_property
    def connectivity_settings(self) -> ConnectivitySettingsWithRawResponse:
        return ConnectivitySettingsWithRawResponse(self._zero_trust.connectivity_settings)


class AsyncZeroTrustWithRawResponse:
    def __init__(self, zero_trust: AsyncZeroTrust) -> None:
        self._zero_trust = zero_trust

    @cached_property
    def connectivity_settings(self) -> AsyncConnectivitySettingsWithRawResponse:
        return AsyncConnectivitySettingsWithRawResponse(self._zero_trust.connectivity_settings)


class ZeroTrustWithStreamingResponse:
    def __init__(self, zero_trust: ZeroTrust) -> None:
        self._zero_trust = zero_trust

    @cached_property
    def connectivity_settings(self) -> ConnectivitySettingsWithStreamingResponse:
        return ConnectivitySettingsWithStreamingResponse(self._zero_trust.connectivity_settings)


class AsyncZeroTrustWithStreamingResponse:
    def __init__(self, zero_trust: AsyncZeroTrust) -> None:
        self._zero_trust = zero_trust

    @cached_property
    def connectivity_settings(self) -> AsyncConnectivitySettingsWithStreamingResponse:
        return AsyncConnectivitySettingsWithStreamingResponse(self._zero_trust.connectivity_settings)
