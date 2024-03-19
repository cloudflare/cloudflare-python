# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .config import (
    Config,
    AsyncConfig,
    ConfigWithRawResponse,
    AsyncConfigWithRawResponse,
    ConfigWithStreamingResponse,
    AsyncConfigWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Cmb", "AsyncCmb"]


class Cmb(SyncAPIResource):
    @cached_property
    def config(self) -> Config:
        return Config(self._client)

    @cached_property
    def with_raw_response(self) -> CmbWithRawResponse:
        return CmbWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CmbWithStreamingResponse:
        return CmbWithStreamingResponse(self)


class AsyncCmb(AsyncAPIResource):
    @cached_property
    def config(self) -> AsyncConfig:
        return AsyncConfig(self._client)

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
    def config(self) -> ConfigWithRawResponse:
        return ConfigWithRawResponse(self._cmb.config)


class AsyncCmbWithRawResponse:
    def __init__(self, cmb: AsyncCmb) -> None:
        self._cmb = cmb

    @cached_property
    def config(self) -> AsyncConfigWithRawResponse:
        return AsyncConfigWithRawResponse(self._cmb.config)


class CmbWithStreamingResponse:
    def __init__(self, cmb: Cmb) -> None:
        self._cmb = cmb

    @cached_property
    def config(self) -> ConfigWithStreamingResponse:
        return ConfigWithStreamingResponse(self._cmb.config)


class AsyncCmbWithStreamingResponse:
    def __init__(self, cmb: AsyncCmb) -> None:
        self._cmb = cmb

    @cached_property
    def config(self) -> AsyncConfigWithStreamingResponse:
        return AsyncConfigWithStreamingResponse(self._cmb.config)
