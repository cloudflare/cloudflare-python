# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .traceroutes import (
    Traceroutes,
    AsyncTraceroutes,
    TraceroutesWithRawResponse,
    AsyncTraceroutesWithRawResponse,
    TraceroutesWithStreamingResponse,
    AsyncTraceroutesWithStreamingResponse,
)

__all__ = ["Diagnostics", "AsyncDiagnostics"]


class Diagnostics(SyncAPIResource):
    @cached_property
    def traceroutes(self) -> Traceroutes:
        return Traceroutes(self._client)

    @cached_property
    def with_raw_response(self) -> DiagnosticsWithRawResponse:
        return DiagnosticsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DiagnosticsWithStreamingResponse:
        return DiagnosticsWithStreamingResponse(self)


class AsyncDiagnostics(AsyncAPIResource):
    @cached_property
    def traceroutes(self) -> AsyncTraceroutes:
        return AsyncTraceroutes(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDiagnosticsWithRawResponse:
        return AsyncDiagnosticsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDiagnosticsWithStreamingResponse:
        return AsyncDiagnosticsWithStreamingResponse(self)


class DiagnosticsWithRawResponse:
    def __init__(self, diagnostics: Diagnostics) -> None:
        self._diagnostics = diagnostics

    @cached_property
    def traceroutes(self) -> TraceroutesWithRawResponse:
        return TraceroutesWithRawResponse(self._diagnostics.traceroutes)


class AsyncDiagnosticsWithRawResponse:
    def __init__(self, diagnostics: AsyncDiagnostics) -> None:
        self._diagnostics = diagnostics

    @cached_property
    def traceroutes(self) -> AsyncTraceroutesWithRawResponse:
        return AsyncTraceroutesWithRawResponse(self._diagnostics.traceroutes)


class DiagnosticsWithStreamingResponse:
    def __init__(self, diagnostics: Diagnostics) -> None:
        self._diagnostics = diagnostics

    @cached_property
    def traceroutes(self) -> TraceroutesWithStreamingResponse:
        return TraceroutesWithStreamingResponse(self._diagnostics.traceroutes)


class AsyncDiagnosticsWithStreamingResponse:
    def __init__(self, diagnostics: AsyncDiagnostics) -> None:
        self._diagnostics = diagnostics

    @cached_property
    def traceroutes(self) -> AsyncTraceroutesWithStreamingResponse:
        return AsyncTraceroutesWithStreamingResponse(self._diagnostics.traceroutes)
