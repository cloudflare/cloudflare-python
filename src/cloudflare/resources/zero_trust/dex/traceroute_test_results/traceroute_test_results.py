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

__all__ = ["TracerouteTestResultsResource", "AsyncTracerouteTestResultsResource"]


class TracerouteTestResultsResource(SyncAPIResource):
    @cached_property
    def network_path(self) -> NetworkPathResource:
        return NetworkPathResource(self._client)

    @cached_property
    def with_raw_response(self) -> TracerouteTestResultsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TracerouteTestResultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TracerouteTestResultsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TracerouteTestResultsResourceWithStreamingResponse(self)


class AsyncTracerouteTestResultsResource(AsyncAPIResource):
    @cached_property
    def network_path(self) -> AsyncNetworkPathResource:
        return AsyncNetworkPathResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTracerouteTestResultsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTracerouteTestResultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTracerouteTestResultsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTracerouteTestResultsResourceWithStreamingResponse(self)


class TracerouteTestResultsResourceWithRawResponse:
    def __init__(self, traceroute_test_results: TracerouteTestResultsResource) -> None:
        self._traceroute_test_results = traceroute_test_results

    @cached_property
    def network_path(self) -> NetworkPathResourceWithRawResponse:
        return NetworkPathResourceWithRawResponse(self._traceroute_test_results.network_path)


class AsyncTracerouteTestResultsResourceWithRawResponse:
    def __init__(self, traceroute_test_results: AsyncTracerouteTestResultsResource) -> None:
        self._traceroute_test_results = traceroute_test_results

    @cached_property
    def network_path(self) -> AsyncNetworkPathResourceWithRawResponse:
        return AsyncNetworkPathResourceWithRawResponse(self._traceroute_test_results.network_path)


class TracerouteTestResultsResourceWithStreamingResponse:
    def __init__(self, traceroute_test_results: TracerouteTestResultsResource) -> None:
        self._traceroute_test_results = traceroute_test_results

    @cached_property
    def network_path(self) -> NetworkPathResourceWithStreamingResponse:
        return NetworkPathResourceWithStreamingResponse(self._traceroute_test_results.network_path)


class AsyncTracerouteTestResultsResourceWithStreamingResponse:
    def __init__(self, traceroute_test_results: AsyncTracerouteTestResultsResource) -> None:
        self._traceroute_test_results = traceroute_test_results

    @cached_property
    def network_path(self) -> AsyncNetworkPathResourceWithStreamingResponse:
        return AsyncNetworkPathResourceWithStreamingResponse(self._traceroute_test_results.network_path)
