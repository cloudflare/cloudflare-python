# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .configs import (
    Configs,
    AsyncConfigs,
    ConfigsWithRawResponse,
    AsyncConfigsWithRawResponse,
    ConfigsWithStreamingResponse,
    AsyncConfigsWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Cmb", "AsyncCmb"]


class Cmb(SyncAPIResource):
    @cached_property
    def configs(self) -> Configs:
        return Configs(self._client)

    @cached_property
    def with_raw_response(self) -> CmbWithRawResponse:
        return CmbWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CmbWithStreamingResponse:
        return CmbWithStreamingResponse(self)


class AsyncCmb(AsyncAPIResource):
    @cached_property
    def configs(self) -> AsyncConfigs:
        return AsyncConfigs(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCmbWithRawResponse:
        return AsyncCmbWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCmbWithStreamingResponse:
        return AsyncCmbWithStreamingResponse(self)


class CmbWithRawResponse:
    def __init__(self, cmb: Cmb) -> None:
        self._cmb = cmb

    @cached_property
    def configs(self) -> ConfigsWithRawResponse:
        return ConfigsWithRawResponse(self._cmb.configs)


class AsyncCmbWithRawResponse:
    def __init__(self, cmb: AsyncCmb) -> None:
        self._cmb = cmb

    @cached_property
    def configs(self) -> AsyncConfigsWithRawResponse:
        return AsyncConfigsWithRawResponse(self._cmb.configs)


class CmbWithStreamingResponse:
    def __init__(self, cmb: Cmb) -> None:
        self._cmb = cmb

    @cached_property
    def configs(self) -> ConfigsWithStreamingResponse:
        return ConfigsWithStreamingResponse(self._cmb.configs)


class AsyncCmbWithStreamingResponse:
    def __init__(self, cmb: AsyncCmb) -> None:
        self._cmb = cmb

    @cached_property
    def configs(self) -> AsyncConfigsWithStreamingResponse:
        return AsyncConfigsWithStreamingResponse(self._cmb.configs)
