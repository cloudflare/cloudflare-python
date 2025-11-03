# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .mcp.mcp import (
    McpResource,
    AsyncMcpResource,
    McpResourceWithRawResponse,
    AsyncMcpResourceWithRawResponse,
    McpResourceWithStreamingResponse,
    AsyncMcpResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["AIControlsResource", "AsyncAIControlsResource"]


class AIControlsResource(SyncAPIResource):
    @cached_property
    def mcp(self) -> McpResource:
        return McpResource(self._client)

    @cached_property
    def with_raw_response(self) -> AIControlsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AIControlsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AIControlsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AIControlsResourceWithStreamingResponse(self)


class AsyncAIControlsResource(AsyncAPIResource):
    @cached_property
    def mcp(self) -> AsyncMcpResource:
        return AsyncMcpResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAIControlsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAIControlsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAIControlsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAIControlsResourceWithStreamingResponse(self)


class AIControlsResourceWithRawResponse:
    def __init__(self, ai_controls: AIControlsResource) -> None:
        self._ai_controls = ai_controls

    @cached_property
    def mcp(self) -> McpResourceWithRawResponse:
        return McpResourceWithRawResponse(self._ai_controls.mcp)


class AsyncAIControlsResourceWithRawResponse:
    def __init__(self, ai_controls: AsyncAIControlsResource) -> None:
        self._ai_controls = ai_controls

    @cached_property
    def mcp(self) -> AsyncMcpResourceWithRawResponse:
        return AsyncMcpResourceWithRawResponse(self._ai_controls.mcp)


class AIControlsResourceWithStreamingResponse:
    def __init__(self, ai_controls: AIControlsResource) -> None:
        self._ai_controls = ai_controls

    @cached_property
    def mcp(self) -> McpResourceWithStreamingResponse:
        return McpResourceWithStreamingResponse(self._ai_controls.mcp)


class AsyncAIControlsResourceWithStreamingResponse:
    def __init__(self, ai_controls: AsyncAIControlsResource) -> None:
        self._ai_controls = ai_controls

    @cached_property
    def mcp(self) -> AsyncMcpResourceWithStreamingResponse:
        return AsyncMcpResourceWithStreamingResponse(self._ai_controls.mcp)
