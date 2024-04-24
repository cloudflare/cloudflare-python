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
        return DiagnosticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DiagnosticsResourceWithStreamingResponse:
        return DiagnosticsResourceWithStreamingResponse(self)


class AsyncDiagnosticsResource(AsyncAPIResource):
    @cached_property
    def traceroutes(self) -> AsyncTraceroutesResource:
        return AsyncTraceroutesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDiagnosticsResourceWithRawResponse:
        return AsyncDiagnosticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDiagnosticsResourceWithStreamingResponse:
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
