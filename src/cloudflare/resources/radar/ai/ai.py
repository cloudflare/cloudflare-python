# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .gateway import (
    GatewayResource,
    AsyncGatewayResource,
    GatewayResourceWithRawResponse,
    AsyncGatewayResourceWithRawResponse,
    GatewayResourceWithStreamingResponse,
    AsyncGatewayResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .gateway.gateway import GatewayResource, AsyncGatewayResource

__all__ = ["AIResource", "AsyncAIResource"]


class AIResource(SyncAPIResource):
    @cached_property
    def gateway(self) -> GatewayResource:
        return GatewayResource(self._client)

    @cached_property
    def with_raw_response(self) -> AIResourceWithRawResponse:
        return AIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AIResourceWithStreamingResponse:
        return AIResourceWithStreamingResponse(self)


class AsyncAIResource(AsyncAPIResource):
    @cached_property
    def gateway(self) -> AsyncGatewayResource:
        return AsyncGatewayResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAIResourceWithRawResponse:
        return AsyncAIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAIResourceWithStreamingResponse:
        return AsyncAIResourceWithStreamingResponse(self)


class AIResourceWithRawResponse:
    def __init__(self, ai: AIResource) -> None:
        self._ai = ai

    @cached_property
    def gateway(self) -> GatewayResourceWithRawResponse:
        return GatewayResourceWithRawResponse(self._ai.gateway)


class AsyncAIResourceWithRawResponse:
    def __init__(self, ai: AsyncAIResource) -> None:
        self._ai = ai

    @cached_property
    def gateway(self) -> AsyncGatewayResourceWithRawResponse:
        return AsyncGatewayResourceWithRawResponse(self._ai.gateway)


class AIResourceWithStreamingResponse:
    def __init__(self, ai: AIResource) -> None:
        self._ai = ai

    @cached_property
    def gateway(self) -> GatewayResourceWithStreamingResponse:
        return GatewayResourceWithStreamingResponse(self._ai.gateway)


class AsyncAIResourceWithStreamingResponse:
    def __init__(self, ai: AsyncAIResource) -> None:
        self._ai = ai

    @cached_property
    def gateway(self) -> AsyncGatewayResourceWithStreamingResponse:
        return AsyncGatewayResourceWithStreamingResponse(self._ai.gateway)
