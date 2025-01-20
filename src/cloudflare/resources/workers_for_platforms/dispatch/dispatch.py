# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .namespaces.namespaces import (
    NamespacesResource,
    AsyncNamespacesResource,
    NamespacesResourceWithRawResponse,
    AsyncNamespacesResourceWithRawResponse,
    NamespacesResourceWithStreamingResponse,
    AsyncNamespacesResourceWithStreamingResponse,
)

__all__ = ["DispatchResource", "AsyncDispatchResource"]


class DispatchResource(SyncAPIResource):
    @cached_property
    def namespaces(self) -> NamespacesResource:
        return NamespacesResource(self._client)

    @cached_property
    def with_raw_response(self) -> DispatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DispatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DispatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DispatchResourceWithStreamingResponse(self)


class AsyncDispatchResource(AsyncAPIResource):
    @cached_property
    def namespaces(self) -> AsyncNamespacesResource:
        return AsyncNamespacesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDispatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDispatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDispatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDispatchResourceWithStreamingResponse(self)


class DispatchResourceWithRawResponse:
    def __init__(self, dispatch: DispatchResource) -> None:
        self._dispatch = dispatch

    @cached_property
    def namespaces(self) -> NamespacesResourceWithRawResponse:
        return NamespacesResourceWithRawResponse(self._dispatch.namespaces)


class AsyncDispatchResourceWithRawResponse:
    def __init__(self, dispatch: AsyncDispatchResource) -> None:
        self._dispatch = dispatch

    @cached_property
    def namespaces(self) -> AsyncNamespacesResourceWithRawResponse:
        return AsyncNamespacesResourceWithRawResponse(self._dispatch.namespaces)


class DispatchResourceWithStreamingResponse:
    def __init__(self, dispatch: DispatchResource) -> None:
        self._dispatch = dispatch

    @cached_property
    def namespaces(self) -> NamespacesResourceWithStreamingResponse:
        return NamespacesResourceWithStreamingResponse(self._dispatch.namespaces)


class AsyncDispatchResourceWithStreamingResponse:
    def __init__(self, dispatch: AsyncDispatchResource) -> None:
        self._dispatch = dispatch

    @cached_property
    def namespaces(self) -> AsyncNamespacesResourceWithStreamingResponse:
        return AsyncNamespacesResourceWithStreamingResponse(self._dispatch.namespaces)
