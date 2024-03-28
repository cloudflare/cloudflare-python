# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .configs import (
    Configs,
    AsyncConfigs,
    ConfigsWithRawResponse,
    AsyncConfigsWithRawResponse,
    ConfigsWithStreamingResponse,
    AsyncConfigsWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["HyperdriveResource", "AsyncHyperdriveResource"]


class HyperdriveResource(SyncAPIResource):
    @cached_property
    def configs(self) -> Configs:
        return Configs(self._client)

    @cached_property
    def with_raw_response(self) -> HyperdriveResourceWithRawResponse:
        return HyperdriveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HyperdriveResourceWithStreamingResponse:
        return HyperdriveResourceWithStreamingResponse(self)


class AsyncHyperdriveResource(AsyncAPIResource):
    @cached_property
    def configs(self) -> AsyncConfigs:
        return AsyncConfigs(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHyperdriveResourceWithRawResponse:
        return AsyncHyperdriveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHyperdriveResourceWithStreamingResponse:
        return AsyncHyperdriveResourceWithStreamingResponse(self)


class HyperdriveResourceWithRawResponse:
    def __init__(self, hyperdrive: HyperdriveResource) -> None:
        self._hyperdrive = hyperdrive

    @cached_property
    def configs(self) -> ConfigsWithRawResponse:
        return ConfigsWithRawResponse(self._hyperdrive.configs)


class AsyncHyperdriveResourceWithRawResponse:
    def __init__(self, hyperdrive: AsyncHyperdriveResource) -> None:
        self._hyperdrive = hyperdrive

    @cached_property
    def configs(self) -> AsyncConfigsWithRawResponse:
        return AsyncConfigsWithRawResponse(self._hyperdrive.configs)


class HyperdriveResourceWithStreamingResponse:
    def __init__(self, hyperdrive: HyperdriveResource) -> None:
        self._hyperdrive = hyperdrive

    @cached_property
    def configs(self) -> ConfigsWithStreamingResponse:
        return ConfigsWithStreamingResponse(self._hyperdrive.configs)


class AsyncHyperdriveResourceWithStreamingResponse:
    def __init__(self, hyperdrive: AsyncHyperdriveResource) -> None:
        self._hyperdrive = hyperdrive

    @cached_property
    def configs(self) -> AsyncConfigsWithStreamingResponse:
        return AsyncConfigsWithStreamingResponse(self._hyperdrive.configs)
