# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .colos import (
    ColosResource,
    AsyncColosResource,
    ColosResourceWithRawResponse,
    AsyncColosResourceWithRawResponse,
    ColosResourceWithStreamingResponse,
    AsyncColosResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .tests.tests import (
    TestsResource,
    AsyncTestsResource,
    TestsResourceWithRawResponse,
    AsyncTestsResourceWithRawResponse,
    TestsResourceWithStreamingResponse,
    AsyncTestsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from .traceroute_tests import (
    TracerouteTestsResource,
    AsyncTracerouteTestsResource,
    TracerouteTestsResourceWithRawResponse,
    AsyncTracerouteTestsResourceWithRawResponse,
    TracerouteTestsResourceWithStreamingResponse,
    AsyncTracerouteTestsResourceWithStreamingResponse,
)
from .commands.commands import (
    CommandsResource,
    AsyncCommandsResource,
    CommandsResourceWithRawResponse,
    AsyncCommandsResourceWithRawResponse,
    CommandsResourceWithStreamingResponse,
    AsyncCommandsResourceWithStreamingResponse,
)
from .http_tests.http_tests import (
    HTTPTestsResource,
    AsyncHTTPTestsResource,
    HTTPTestsResourceWithRawResponse,
    AsyncHTTPTestsResourceWithRawResponse,
    HTTPTestsResourceWithStreamingResponse,
    AsyncHTTPTestsResourceWithStreamingResponse,
)
from .fleet_status.fleet_status import (
    FleetStatusResource,
    AsyncFleetStatusResource,
    FleetStatusResourceWithRawResponse,
    AsyncFleetStatusResourceWithRawResponse,
    FleetStatusResourceWithStreamingResponse,
    AsyncFleetStatusResourceWithStreamingResponse,
)
from .traceroute_test_results.traceroute_test_results import (
    TracerouteTestResultsResource,
    AsyncTracerouteTestResultsResource,
    TracerouteTestResultsResourceWithRawResponse,
    AsyncTracerouteTestResultsResourceWithRawResponse,
    TracerouteTestResultsResourceWithStreamingResponse,
    AsyncTracerouteTestResultsResourceWithStreamingResponse,
)

__all__ = ["DEXResource", "AsyncDEXResource"]


class DEXResource(SyncAPIResource):
    @cached_property
    def commands(self) -> CommandsResource:
        return CommandsResource(self._client)

    @cached_property
    def colos(self) -> ColosResource:
        return ColosResource(self._client)

    @cached_property
    def fleet_status(self) -> FleetStatusResource:
        return FleetStatusResource(self._client)

    @cached_property
    def http_tests(self) -> HTTPTestsResource:
        return HTTPTestsResource(self._client)

    @cached_property
    def tests(self) -> TestsResource:
        return TestsResource(self._client)

    @cached_property
    def traceroute_test_results(self) -> TracerouteTestResultsResource:
        return TracerouteTestResultsResource(self._client)

    @cached_property
    def traceroute_tests(self) -> TracerouteTestsResource:
        return TracerouteTestsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DEXResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DEXResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DEXResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DEXResourceWithStreamingResponse(self)


class AsyncDEXResource(AsyncAPIResource):
    @cached_property
    def commands(self) -> AsyncCommandsResource:
        return AsyncCommandsResource(self._client)

    @cached_property
    def colos(self) -> AsyncColosResource:
        return AsyncColosResource(self._client)

    @cached_property
    def fleet_status(self) -> AsyncFleetStatusResource:
        return AsyncFleetStatusResource(self._client)

    @cached_property
    def http_tests(self) -> AsyncHTTPTestsResource:
        return AsyncHTTPTestsResource(self._client)

    @cached_property
    def tests(self) -> AsyncTestsResource:
        return AsyncTestsResource(self._client)

    @cached_property
    def traceroute_test_results(self) -> AsyncTracerouteTestResultsResource:
        return AsyncTracerouteTestResultsResource(self._client)

    @cached_property
    def traceroute_tests(self) -> AsyncTracerouteTestsResource:
        return AsyncTracerouteTestsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDEXResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDEXResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDEXResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDEXResourceWithStreamingResponse(self)


class DEXResourceWithRawResponse:
    def __init__(self, dex: DEXResource) -> None:
        self._dex = dex

    @cached_property
    def commands(self) -> CommandsResourceWithRawResponse:
        return CommandsResourceWithRawResponse(self._dex.commands)

    @cached_property
    def colos(self) -> ColosResourceWithRawResponse:
        return ColosResourceWithRawResponse(self._dex.colos)

    @cached_property
    def fleet_status(self) -> FleetStatusResourceWithRawResponse:
        return FleetStatusResourceWithRawResponse(self._dex.fleet_status)

    @cached_property
    def http_tests(self) -> HTTPTestsResourceWithRawResponse:
        return HTTPTestsResourceWithRawResponse(self._dex.http_tests)

    @cached_property
    def tests(self) -> TestsResourceWithRawResponse:
        return TestsResourceWithRawResponse(self._dex.tests)

    @cached_property
    def traceroute_test_results(self) -> TracerouteTestResultsResourceWithRawResponse:
        return TracerouteTestResultsResourceWithRawResponse(self._dex.traceroute_test_results)

    @cached_property
    def traceroute_tests(self) -> TracerouteTestsResourceWithRawResponse:
        return TracerouteTestsResourceWithRawResponse(self._dex.traceroute_tests)


class AsyncDEXResourceWithRawResponse:
    def __init__(self, dex: AsyncDEXResource) -> None:
        self._dex = dex

    @cached_property
    def commands(self) -> AsyncCommandsResourceWithRawResponse:
        return AsyncCommandsResourceWithRawResponse(self._dex.commands)

    @cached_property
    def colos(self) -> AsyncColosResourceWithRawResponse:
        return AsyncColosResourceWithRawResponse(self._dex.colos)

    @cached_property
    def fleet_status(self) -> AsyncFleetStatusResourceWithRawResponse:
        return AsyncFleetStatusResourceWithRawResponse(self._dex.fleet_status)

    @cached_property
    def http_tests(self) -> AsyncHTTPTestsResourceWithRawResponse:
        return AsyncHTTPTestsResourceWithRawResponse(self._dex.http_tests)

    @cached_property
    def tests(self) -> AsyncTestsResourceWithRawResponse:
        return AsyncTestsResourceWithRawResponse(self._dex.tests)

    @cached_property
    def traceroute_test_results(self) -> AsyncTracerouteTestResultsResourceWithRawResponse:
        return AsyncTracerouteTestResultsResourceWithRawResponse(self._dex.traceroute_test_results)

    @cached_property
    def traceroute_tests(self) -> AsyncTracerouteTestsResourceWithRawResponse:
        return AsyncTracerouteTestsResourceWithRawResponse(self._dex.traceroute_tests)


class DEXResourceWithStreamingResponse:
    def __init__(self, dex: DEXResource) -> None:
        self._dex = dex

    @cached_property
    def commands(self) -> CommandsResourceWithStreamingResponse:
        return CommandsResourceWithStreamingResponse(self._dex.commands)

    @cached_property
    def colos(self) -> ColosResourceWithStreamingResponse:
        return ColosResourceWithStreamingResponse(self._dex.colos)

    @cached_property
    def fleet_status(self) -> FleetStatusResourceWithStreamingResponse:
        return FleetStatusResourceWithStreamingResponse(self._dex.fleet_status)

    @cached_property
    def http_tests(self) -> HTTPTestsResourceWithStreamingResponse:
        return HTTPTestsResourceWithStreamingResponse(self._dex.http_tests)

    @cached_property
    def tests(self) -> TestsResourceWithStreamingResponse:
        return TestsResourceWithStreamingResponse(self._dex.tests)

    @cached_property
    def traceroute_test_results(self) -> TracerouteTestResultsResourceWithStreamingResponse:
        return TracerouteTestResultsResourceWithStreamingResponse(self._dex.traceroute_test_results)

    @cached_property
    def traceroute_tests(self) -> TracerouteTestsResourceWithStreamingResponse:
        return TracerouteTestsResourceWithStreamingResponse(self._dex.traceroute_tests)


class AsyncDEXResourceWithStreamingResponse:
    def __init__(self, dex: AsyncDEXResource) -> None:
        self._dex = dex

    @cached_property
    def commands(self) -> AsyncCommandsResourceWithStreamingResponse:
        return AsyncCommandsResourceWithStreamingResponse(self._dex.commands)

    @cached_property
    def colos(self) -> AsyncColosResourceWithStreamingResponse:
        return AsyncColosResourceWithStreamingResponse(self._dex.colos)

    @cached_property
    def fleet_status(self) -> AsyncFleetStatusResourceWithStreamingResponse:
        return AsyncFleetStatusResourceWithStreamingResponse(self._dex.fleet_status)

    @cached_property
    def http_tests(self) -> AsyncHTTPTestsResourceWithStreamingResponse:
        return AsyncHTTPTestsResourceWithStreamingResponse(self._dex.http_tests)

    @cached_property
    def tests(self) -> AsyncTestsResourceWithStreamingResponse:
        return AsyncTestsResourceWithStreamingResponse(self._dex.tests)

    @cached_property
    def traceroute_test_results(self) -> AsyncTracerouteTestResultsResourceWithStreamingResponse:
        return AsyncTracerouteTestResultsResourceWithStreamingResponse(self._dex.traceroute_test_results)

    @cached_property
    def traceroute_tests(self) -> AsyncTracerouteTestsResourceWithStreamingResponse:
        return AsyncTracerouteTestsResourceWithStreamingResponse(self._dex.traceroute_tests)
