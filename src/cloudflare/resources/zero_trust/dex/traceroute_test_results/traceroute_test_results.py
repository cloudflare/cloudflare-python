# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._compat import cached_property
from .network_path import (
    NetworkPathResource,
    AsyncNetworkPathResource,
    NetworkPathResourceWithRawResponse,
    AsyncNetworkPathResourceWithRawResponse,
    NetworkPathResourceWithStreamingResponse,
    AsyncNetworkPathResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["TracerouteTestResults", "AsyncTracerouteTestResults"]


class TracerouteTestResults(SyncAPIResource):
    @cached_property
    def network_path(self) -> NetworkPathResource:
        return NetworkPathResource(self._client)

    @cached_property
    def with_raw_response(self) -> TracerouteTestResultsWithRawResponse:
        return TracerouteTestResultsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TracerouteTestResultsWithStreamingResponse:
        return TracerouteTestResultsWithStreamingResponse(self)


class AsyncTracerouteTestResults(AsyncAPIResource):
    @cached_property
    def network_path(self) -> AsyncNetworkPathResource:
        return AsyncNetworkPathResource(self._client)

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
    def network_path(self) -> NetworkPathResourceWithRawResponse:
        return NetworkPathResourceWithRawResponse(self._traceroute_test_results.network_path)


class AsyncTracerouteTestResultsWithRawResponse:
    def __init__(self, traceroute_test_results: AsyncTracerouteTestResults) -> None:
        self._traceroute_test_results = traceroute_test_results

    @cached_property
    def network_path(self) -> AsyncNetworkPathResourceWithRawResponse:
        return AsyncNetworkPathResourceWithRawResponse(self._traceroute_test_results.network_path)


class TracerouteTestResultsWithStreamingResponse:
    def __init__(self, traceroute_test_results: TracerouteTestResults) -> None:
        self._traceroute_test_results = traceroute_test_results

    @cached_property
    def network_path(self) -> NetworkPathResourceWithStreamingResponse:
        return NetworkPathResourceWithStreamingResponse(self._traceroute_test_results.network_path)


class AsyncTracerouteTestResultsWithStreamingResponse:
    def __init__(self, traceroute_test_results: AsyncTracerouteTestResults) -> None:
        self._traceroute_test_results = traceroute_test_results

    @cached_property
    def network_path(self) -> AsyncNetworkPathResourceWithStreamingResponse:
        return AsyncNetworkPathResourceWithStreamingResponse(self._traceroute_test_results.network_path)
