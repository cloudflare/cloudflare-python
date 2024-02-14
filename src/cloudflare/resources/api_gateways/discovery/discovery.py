# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ...._compat import cached_property
from .operations import (
    Operations,
    AsyncOperations,
    OperationsWithRawResponse,
    AsyncOperationsWithRawResponse,
    OperationsWithStreamingResponse,
    AsyncOperationsWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Discovery", "AsyncDiscovery"]


class Discovery(SyncAPIResource):
    @cached_property
    def operations(self) -> Operations:
        return Operations(self._client)

    @cached_property
    def with_raw_response(self) -> DiscoveryWithRawResponse:
        return DiscoveryWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DiscoveryWithStreamingResponse:
        return DiscoveryWithStreamingResponse(self)


class AsyncDiscovery(AsyncAPIResource):
    @cached_property
    def operations(self) -> AsyncOperations:
        return AsyncOperations(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDiscoveryWithRawResponse:
        return AsyncDiscoveryWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDiscoveryWithStreamingResponse:
        return AsyncDiscoveryWithStreamingResponse(self)


class DiscoveryWithRawResponse:
    def __init__(self, discovery: Discovery) -> None:
        self._discovery = discovery

    @cached_property
    def operations(self) -> OperationsWithRawResponse:
        return OperationsWithRawResponse(self._discovery.operations)


class AsyncDiscoveryWithRawResponse:
    def __init__(self, discovery: AsyncDiscovery) -> None:
        self._discovery = discovery

    @cached_property
    def operations(self) -> AsyncOperationsWithRawResponse:
        return AsyncOperationsWithRawResponse(self._discovery.operations)


class DiscoveryWithStreamingResponse:
    def __init__(self, discovery: Discovery) -> None:
        self._discovery = discovery

    @cached_property
    def operations(self) -> OperationsWithStreamingResponse:
        return OperationsWithStreamingResponse(self._discovery.operations)


class AsyncDiscoveryWithStreamingResponse:
    def __init__(self, discovery: AsyncDiscovery) -> None:
        self._discovery = discovery

    @cached_property
    def operations(self) -> AsyncOperationsWithStreamingResponse:
        return AsyncOperationsWithStreamingResponse(self._discovery.operations)
