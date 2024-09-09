# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .configuration import (
    ConfigurationResource,
    AsyncConfigurationResource,
    ConfigurationResourceWithRawResponse,
    AsyncConfigurationResourceWithRawResponse,
    ConfigurationResourceWithStreamingResponse,
    AsyncConfigurationResourceWithStreamingResponse,
)
from .configuration.configuration import ConfigurationResource, AsyncConfigurationResource

__all__ = ["R2Resource", "AsyncR2Resource"]


class R2Resource(SyncAPIResource):
    @cached_property
    def configuration(self) -> ConfigurationResource:
        return ConfigurationResource(self._client)

    @cached_property
    def with_raw_response(self) -> R2ResourceWithRawResponse:
        return R2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> R2ResourceWithStreamingResponse:
        return R2ResourceWithStreamingResponse(self)


class AsyncR2Resource(AsyncAPIResource):
    @cached_property
    def configuration(self) -> AsyncConfigurationResource:
        return AsyncConfigurationResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncR2ResourceWithRawResponse:
        return AsyncR2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncR2ResourceWithStreamingResponse:
        return AsyncR2ResourceWithStreamingResponse(self)


class R2ResourceWithRawResponse:
    def __init__(self, r2: R2Resource) -> None:
        self._r2 = r2

    @cached_property
    def configuration(self) -> ConfigurationResourceWithRawResponse:
        return ConfigurationResourceWithRawResponse(self._r2.configuration)


class AsyncR2ResourceWithRawResponse:
    def __init__(self, r2: AsyncR2Resource) -> None:
        self._r2 = r2

    @cached_property
    def configuration(self) -> AsyncConfigurationResourceWithRawResponse:
        return AsyncConfigurationResourceWithRawResponse(self._r2.configuration)


class R2ResourceWithStreamingResponse:
    def __init__(self, r2: R2Resource) -> None:
        self._r2 = r2

    @cached_property
    def configuration(self) -> ConfigurationResourceWithStreamingResponse:
        return ConfigurationResourceWithStreamingResponse(self._r2.configuration)


class AsyncR2ResourceWithStreamingResponse:
    def __init__(self, r2: AsyncR2Resource) -> None:
        self._r2 = r2

    @cached_property
    def configuration(self) -> AsyncConfigurationResourceWithStreamingResponse:
        return AsyncConfigurationResourceWithStreamingResponse(self._r2.configuration)
