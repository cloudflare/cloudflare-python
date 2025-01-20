# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .traceroutes import (
    TraceroutesResource,
    AsyncTraceroutesResource,
    TraceroutesResourceWithRawResponse,
    AsyncTraceroutesResourceWithRawResponse,
    TraceroutesResourceWithStreamingResponse,
    AsyncTraceroutesResourceWithStreamingResponse,
)

__all__ = ["DiagnosticsResource", "AsyncDiagnosticsResource"]


class DiagnosticsResource(SyncAPIResource):
    @cached_property
    def traceroutes(self) -> TraceroutesResource:
        return TraceroutesResource(self._client)

    @cached_property
    def with_raw_response(self) -> DiagnosticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DiagnosticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DiagnosticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DiagnosticsResourceWithStreamingResponse(self)


class AsyncDiagnosticsResource(AsyncAPIResource):
    @cached_property
    def traceroutes(self) -> AsyncTraceroutesResource:
        return AsyncTraceroutesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDiagnosticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDiagnosticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDiagnosticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDiagnosticsResourceWithStreamingResponse(self)


class DiagnosticsResourceWithRawResponse:
    def __init__(self, diagnostics: DiagnosticsResource) -> None:
        self._diagnostics = diagnostics

    @cached_property
    def traceroutes(self) -> TraceroutesResourceWithRawResponse:
        return TraceroutesResourceWithRawResponse(self._diagnostics.traceroutes)


class AsyncDiagnosticsResourceWithRawResponse:
    def __init__(self, diagnostics: AsyncDiagnosticsResource) -> None:
        self._diagnostics = diagnostics

    @cached_property
    def traceroutes(self) -> AsyncTraceroutesResourceWithRawResponse:
        return AsyncTraceroutesResourceWithRawResponse(self._diagnostics.traceroutes)


class DiagnosticsResourceWithStreamingResponse:
    def __init__(self, diagnostics: DiagnosticsResource) -> None:
        self._diagnostics = diagnostics

    @cached_property
    def traceroutes(self) -> TraceroutesResourceWithStreamingResponse:
        return TraceroutesResourceWithStreamingResponse(self._diagnostics.traceroutes)


class AsyncDiagnosticsResourceWithStreamingResponse:
    def __init__(self, diagnostics: AsyncDiagnosticsResource) -> None:
        self._diagnostics = diagnostics

    @cached_property
    def traceroutes(self) -> AsyncTraceroutesResourceWithStreamingResponse:
        return AsyncTraceroutesResourceWithStreamingResponse(self._diagnostics.traceroutes)
