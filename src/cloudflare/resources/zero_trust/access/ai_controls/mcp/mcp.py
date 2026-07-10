# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .portals import (
    PortalsResource,
    AsyncPortalsResource,
    PortalsResourceWithRawResponse,
    AsyncPortalsResourceWithRawResponse,
    PortalsResourceWithStreamingResponse,
    AsyncPortalsResourceWithStreamingResponse,
)
from .servers import (
    ServersResource,
    AsyncServersResource,
    ServersResourceWithRawResponse,
    AsyncServersResourceWithRawResponse,
    ServersResourceWithStreamingResponse,
    AsyncServersResourceWithStreamingResponse,
)
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource

__all__ = ["McpResource", "AsyncMcpResource"]


class McpResource(SyncAPIResource):
    @cached_property
    def portals(self) -> PortalsResource:
        return PortalsResource(self._client)

    @cached_property
    def servers(self) -> ServersResource:
        return ServersResource(self._client)

    @cached_property
    def with_raw_response(self) -> McpResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return McpResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> McpResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return McpResourceWithStreamingResponse(self)


class AsyncMcpResource(AsyncAPIResource):
    @cached_property
    def portals(self) -> AsyncPortalsResource:
        return AsyncPortalsResource(self._client)

    @cached_property
    def servers(self) -> AsyncServersResource:
        return AsyncServersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMcpResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMcpResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMcpResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncMcpResourceWithStreamingResponse(self)


class McpResourceWithRawResponse:
    def __init__(self, mcp: McpResource) -> None:
        self._mcp = mcp

    @cached_property
    def portals(self) -> PortalsResourceWithRawResponse:
        return PortalsResourceWithRawResponse(self._mcp.portals)

    @cached_property
    def servers(self) -> ServersResourceWithRawResponse:
        return ServersResourceWithRawResponse(self._mcp.servers)


class AsyncMcpResourceWithRawResponse:
    def __init__(self, mcp: AsyncMcpResource) -> None:
        self._mcp = mcp

    @cached_property
    def portals(self) -> AsyncPortalsResourceWithRawResponse:
        return AsyncPortalsResourceWithRawResponse(self._mcp.portals)

    @cached_property
    def servers(self) -> AsyncServersResourceWithRawResponse:
        return AsyncServersResourceWithRawResponse(self._mcp.servers)


class McpResourceWithStreamingResponse:
    def __init__(self, mcp: McpResource) -> None:
        self._mcp = mcp

    @cached_property
    def portals(self) -> PortalsResourceWithStreamingResponse:
        return PortalsResourceWithStreamingResponse(self._mcp.portals)

    @cached_property
    def servers(self) -> ServersResourceWithStreamingResponse:
        return ServersResourceWithStreamingResponse(self._mcp.servers)


class AsyncMcpResourceWithStreamingResponse:
    def __init__(self, mcp: AsyncMcpResource) -> None:
        self._mcp = mcp

    @cached_property
    def portals(self) -> AsyncPortalsResourceWithStreamingResponse:
        return AsyncPortalsResourceWithStreamingResponse(self._mcp.portals)

    @cached_property
    def servers(self) -> AsyncServersResourceWithStreamingResponse:
        return AsyncServersResourceWithStreamingResponse(self._mcp.servers)
