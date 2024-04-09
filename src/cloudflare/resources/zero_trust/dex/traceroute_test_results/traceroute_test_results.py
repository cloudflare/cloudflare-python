# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._compat import cached_property
from .network_path import (
    NetworkPath,
    AsyncNetworkPath,
    NetworkPathWithRawResponse,
    AsyncNetworkPathWithRawResponse,
    NetworkPathWithStreamingResponse,
    AsyncNetworkPathWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["TracerouteTestResults", "AsyncTracerouteTestResults"]


class TracerouteTestResults(SyncAPIResource):
    @cached_property
    def network_path(self) -> NetworkPath:
        return NetworkPath(self._client)

    @cached_property
    def with_raw_response(self) -> TracerouteTestResultsWithRawResponse:
        return TracerouteTestResultsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TracerouteTestResultsWithStreamingResponse:
        return TracerouteTestResultsWithStreamingResponse(self)


class AsyncTracerouteTestResults(AsyncAPIResource):
    @cached_property
    def network_path(self) -> AsyncNetworkPath:
        return AsyncNetworkPath(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTracerouteTestResultsWithRawResponse:
        return AsyncTracerouteTestResultsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTracerouteTestResultsWithStreamingResponse:
        return AsyncTracerouteTestResultsWithStreamingResponse(self)


class TracerouteTestResultsWithRawResponse:
    def __init__(self, traceroute_test_results: TracerouteTestResults) -> None:
        self._traceroute_test_results = traceroute_test_results

    @cached_property
    def network_path(self) -> NetworkPathWithRawResponse:
        return NetworkPathWithRawResponse(self._traceroute_test_results.network_path)


class AsyncTracerouteTestResultsWithRawResponse:
    def __init__(self, traceroute_test_results: AsyncTracerouteTestResults) -> None:
        self._traceroute_test_results = traceroute_test_results

    @cached_property
    def network_path(self) -> AsyncNetworkPathWithRawResponse:
        return AsyncNetworkPathWithRawResponse(self._traceroute_test_results.network_path)


class TracerouteTestResultsWithStreamingResponse:
    def __init__(self, traceroute_test_results: TracerouteTestResults) -> None:
        self._traceroute_test_results = traceroute_test_results

    @cached_property
    def network_path(self) -> NetworkPathWithStreamingResponse:
        return NetworkPathWithStreamingResponse(self._traceroute_test_results.network_path)


class AsyncTracerouteTestResultsWithStreamingResponse:
    def __init__(self, traceroute_test_results: AsyncTracerouteTestResults) -> None:
        self._traceroute_test_results = traceroute_test_results

    @cached_property
    def network_path(self) -> AsyncNetworkPathWithStreamingResponse:
        return AsyncNetworkPathWithStreamingResponse(self._traceroute_test_results.network_path)
