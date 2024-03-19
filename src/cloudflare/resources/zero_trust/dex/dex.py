# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .colos import (
    Colos,
    AsyncColos,
    ColosWithRawResponse,
    AsyncColosWithRawResponse,
    ColosWithStreamingResponse,
    AsyncColosWithStreamingResponse,
)
from .tests import (
    Tests,
    AsyncTests,
    TestsWithRawResponse,
    AsyncTestsWithRawResponse,
    TestsWithStreamingResponse,
    AsyncTestsWithStreamingResponse,
)
from ...._compat import cached_property
from .http_tests import (
    HTTPTests,
    AsyncHTTPTests,
    HTTPTestsWithRawResponse,
    AsyncHTTPTestsWithRawResponse,
    HTTPTestsWithStreamingResponse,
    AsyncHTTPTestsWithStreamingResponse,
)
from .tests.tests import Tests, AsyncTests
from ...._resource import SyncAPIResource, AsyncAPIResource
from .fleet_status import (
    FleetStatus,
    AsyncFleetStatus,
    FleetStatusWithRawResponse,
    AsyncFleetStatusWithRawResponse,
    FleetStatusWithStreamingResponse,
    AsyncFleetStatusWithStreamingResponse,
)
from .traceroute_tests import (
    TracerouteTests,
    AsyncTracerouteTests,
    TracerouteTestsWithRawResponse,
    AsyncTracerouteTestsWithRawResponse,
    TracerouteTestsWithStreamingResponse,
    AsyncTracerouteTestsWithStreamingResponse,
)
from .http_tests.http_tests import HTTPTests, AsyncHTTPTests
from .traceroute_test_results import (
    TracerouteTestResults,
    AsyncTracerouteTestResults,
    TracerouteTestResultsWithRawResponse,
    AsyncTracerouteTestResultsWithRawResponse,
    TracerouteTestResultsWithStreamingResponse,
    AsyncTracerouteTestResultsWithStreamingResponse,
)
from .fleet_status.fleet_status import FleetStatus, AsyncFleetStatus
from .traceroute_test_results.traceroute_test_results import TracerouteTestResults, AsyncTracerouteTestResults

__all__ = ["DEX", "AsyncDEX"]


class DEX(SyncAPIResource):
    @cached_property
    def colos(self) -> Colos:
        return Colos(self._client)

    @cached_property
    def fleet_status(self) -> FleetStatus:
        return FleetStatus(self._client)

    @cached_property
    def http_tests(self) -> HTTPTests:
        return HTTPTests(self._client)

    @cached_property
    def tests(self) -> Tests:
        return Tests(self._client)

    @cached_property
    def traceroute_test_results(self) -> TracerouteTestResults:
        return TracerouteTestResults(self._client)

    @cached_property
    def traceroute_tests(self) -> TracerouteTests:
        return TracerouteTests(self._client)

    @cached_property
    def with_raw_response(self) -> DEXWithRawResponse:
        return DEXWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DEXWithStreamingResponse:
        return DEXWithStreamingResponse(self)


class AsyncDEX(AsyncAPIResource):
    @cached_property
    def colos(self) -> AsyncColos:
        return AsyncColos(self._client)

    @cached_property
    def fleet_status(self) -> AsyncFleetStatus:
        return AsyncFleetStatus(self._client)

    @cached_property
    def http_tests(self) -> AsyncHTTPTests:
        return AsyncHTTPTests(self._client)

    @cached_property
    def tests(self) -> AsyncTests:
        return AsyncTests(self._client)

    @cached_property
    def traceroute_test_results(self) -> AsyncTracerouteTestResults:
        return AsyncTracerouteTestResults(self._client)

    @cached_property
    def traceroute_tests(self) -> AsyncTracerouteTests:
        return AsyncTracerouteTests(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDEXWithRawResponse:
        return AsyncDEXWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDEXWithStreamingResponse:
        return AsyncDEXWithStreamingResponse(self)


class DEXWithRawResponse:
    def __init__(self, dex: DEX) -> None:
        self._dex = dex

    @cached_property
    def colos(self) -> ColosWithRawResponse:
        return ColosWithRawResponse(self._dex.colos)

    @cached_property
    def fleet_status(self) -> FleetStatusWithRawResponse:
        return FleetStatusWithRawResponse(self._dex.fleet_status)

    @cached_property
    def http_tests(self) -> HTTPTestsWithRawResponse:
        return HTTPTestsWithRawResponse(self._dex.http_tests)

    @cached_property
    def tests(self) -> TestsWithRawResponse:
        return TestsWithRawResponse(self._dex.tests)

    @cached_property
    def traceroute_test_results(self) -> TracerouteTestResultsWithRawResponse:
        return TracerouteTestResultsWithRawResponse(self._dex.traceroute_test_results)

    @cached_property
    def traceroute_tests(self) -> TracerouteTestsWithRawResponse:
        return TracerouteTestsWithRawResponse(self._dex.traceroute_tests)


class AsyncDEXWithRawResponse:
    def __init__(self, dex: AsyncDEX) -> None:
        self._dex = dex

    @cached_property
    def colos(self) -> AsyncColosWithRawResponse:
        return AsyncColosWithRawResponse(self._dex.colos)

    @cached_property
    def fleet_status(self) -> AsyncFleetStatusWithRawResponse:
        return AsyncFleetStatusWithRawResponse(self._dex.fleet_status)

    @cached_property
    def http_tests(self) -> AsyncHTTPTestsWithRawResponse:
        return AsyncHTTPTestsWithRawResponse(self._dex.http_tests)

    @cached_property
    def tests(self) -> AsyncTestsWithRawResponse:
        return AsyncTestsWithRawResponse(self._dex.tests)

    @cached_property
    def traceroute_test_results(self) -> AsyncTracerouteTestResultsWithRawResponse:
        return AsyncTracerouteTestResultsWithRawResponse(self._dex.traceroute_test_results)

    @cached_property
    def traceroute_tests(self) -> AsyncTracerouteTestsWithRawResponse:
        return AsyncTracerouteTestsWithRawResponse(self._dex.traceroute_tests)


class DEXWithStreamingResponse:
    def __init__(self, dex: DEX) -> None:
        self._dex = dex

    @cached_property
    def colos(self) -> ColosWithStreamingResponse:
        return ColosWithStreamingResponse(self._dex.colos)

    @cached_property
    def fleet_status(self) -> FleetStatusWithStreamingResponse:
        return FleetStatusWithStreamingResponse(self._dex.fleet_status)

    @cached_property
    def http_tests(self) -> HTTPTestsWithStreamingResponse:
        return HTTPTestsWithStreamingResponse(self._dex.http_tests)

    @cached_property
    def tests(self) -> TestsWithStreamingResponse:
        return TestsWithStreamingResponse(self._dex.tests)

    @cached_property
    def traceroute_test_results(self) -> TracerouteTestResultsWithStreamingResponse:
        return TracerouteTestResultsWithStreamingResponse(self._dex.traceroute_test_results)

    @cached_property
    def traceroute_tests(self) -> TracerouteTestsWithStreamingResponse:
        return TracerouteTestsWithStreamingResponse(self._dex.traceroute_tests)


class AsyncDEXWithStreamingResponse:
    def __init__(self, dex: AsyncDEX) -> None:
        self._dex = dex

    @cached_property
    def colos(self) -> AsyncColosWithStreamingResponse:
        return AsyncColosWithStreamingResponse(self._dex.colos)

    @cached_property
    def fleet_status(self) -> AsyncFleetStatusWithStreamingResponse:
        return AsyncFleetStatusWithStreamingResponse(self._dex.fleet_status)

    @cached_property
    def http_tests(self) -> AsyncHTTPTestsWithStreamingResponse:
        return AsyncHTTPTestsWithStreamingResponse(self._dex.http_tests)

    @cached_property
    def tests(self) -> AsyncTestsWithStreamingResponse:
        return AsyncTestsWithStreamingResponse(self._dex.tests)

    @cached_property
    def traceroute_test_results(self) -> AsyncTracerouteTestResultsWithStreamingResponse:
        return AsyncTracerouteTestResultsWithStreamingResponse(self._dex.traceroute_test_results)

    @cached_property
    def traceroute_tests(self) -> AsyncTracerouteTestsWithStreamingResponse:
        return AsyncTracerouteTestsWithStreamingResponse(self._dex.traceroute_tests)
