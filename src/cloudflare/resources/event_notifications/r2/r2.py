# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .configuration import (
    Configuration,
    AsyncConfiguration,
    ConfigurationWithRawResponse,
    AsyncConfigurationWithRawResponse,
    ConfigurationWithStreamingResponse,
    AsyncConfigurationWithStreamingResponse,
)
from .configuration.configuration import Configuration, AsyncConfiguration

__all__ = ["R2", "AsyncR2"]


class R2(SyncAPIResource):
    @cached_property
    def configuration(self) -> Configuration:
        return Configuration(self._client)

    @cached_property
    def with_raw_response(self) -> R2WithRawResponse:
        return R2WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> R2WithStreamingResponse:
        return R2WithStreamingResponse(self)


class AsyncR2(AsyncAPIResource):
    @cached_property
    def configuration(self) -> AsyncConfiguration:
        return AsyncConfiguration(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncR2WithRawResponse:
        return AsyncR2WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncR2WithStreamingResponse:
        return AsyncR2WithStreamingResponse(self)


class R2WithRawResponse:
    def __init__(self, r2: R2) -> None:
        self._r2 = r2

    @cached_property
    def configuration(self) -> ConfigurationWithRawResponse:
        return ConfigurationWithRawResponse(self._r2.configuration)


class AsyncR2WithRawResponse:
    def __init__(self, r2: AsyncR2) -> None:
        self._r2 = r2

    @cached_property
    def configuration(self) -> AsyncConfigurationWithRawResponse:
        return AsyncConfigurationWithRawResponse(self._r2.configuration)


class R2WithStreamingResponse:
    def __init__(self, r2: R2) -> None:
        self._r2 = r2

    @cached_property
    def configuration(self) -> ConfigurationWithStreamingResponse:
        return ConfigurationWithStreamingResponse(self._r2.configuration)


class AsyncR2WithStreamingResponse:
    def __init__(self, r2: AsyncR2) -> None:
        self._r2 = r2

    @cached_property
    def configuration(self) -> AsyncConfigurationWithStreamingResponse:
        return AsyncConfigurationWithStreamingResponse(self._r2.configuration)
