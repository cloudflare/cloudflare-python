# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .traces import (
    Traces,
    AsyncTraces,
    TracesWithRawResponse,
    AsyncTracesWithRawResponse,
    TracesWithStreamingResponse,
    AsyncTracesWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["RequestTracers", "AsyncRequestTracers"]


class RequestTracers(SyncAPIResource):
    @cached_property
    def traces(self) -> Traces:
        return Traces(self._client)

    @cached_property
    def with_raw_response(self) -> RequestTracersWithRawResponse:
        return RequestTracersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RequestTracersWithStreamingResponse:
        return RequestTracersWithStreamingResponse(self)


class AsyncRequestTracers(AsyncAPIResource):
    @cached_property
    def traces(self) -> AsyncTraces:
        return AsyncTraces(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRequestTracersWithRawResponse:
        return AsyncRequestTracersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRequestTracersWithStreamingResponse:
        return AsyncRequestTracersWithStreamingResponse(self)


class RequestTracersWithRawResponse:
    def __init__(self, request_tracers: RequestTracers) -> None:
        self._request_tracers = request_tracers

    @cached_property
    def traces(self) -> TracesWithRawResponse:
        return TracesWithRawResponse(self._request_tracers.traces)


class AsyncRequestTracersWithRawResponse:
    def __init__(self, request_tracers: AsyncRequestTracers) -> None:
        self._request_tracers = request_tracers

    @cached_property
    def traces(self) -> AsyncTracesWithRawResponse:
        return AsyncTracesWithRawResponse(self._request_tracers.traces)


class RequestTracersWithStreamingResponse:
    def __init__(self, request_tracers: RequestTracers) -> None:
        self._request_tracers = request_tracers

    @cached_property
    def traces(self) -> TracesWithStreamingResponse:
        return TracesWithStreamingResponse(self._request_tracers.traces)


class AsyncRequestTracersWithStreamingResponse:
    def __init__(self, request_tracers: AsyncRequestTracers) -> None:
        self._request_tracers = request_tracers

    @cached_property
    def traces(self) -> AsyncTracesWithStreamingResponse:
        return AsyncTracesWithStreamingResponse(self._request_tracers.traces)
