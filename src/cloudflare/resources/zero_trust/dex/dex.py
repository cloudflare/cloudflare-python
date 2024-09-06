# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .colos import ColosResource, AsyncColosResource

from ...._compat import cached_property

from .fleet_status.fleet_status import FleetStatusResource, AsyncFleetStatusResource

from .http_tests.http_tests import HTTPTestsResource, AsyncHTTPTestsResource

from .tests.tests import TestsResource, AsyncTestsResource

from .traceroute_test_results.traceroute_test_results import (
    TracerouteTestResultsResource,
    AsyncTracerouteTestResultsResource,
)

from .traceroute_tests import TracerouteTestsResource, AsyncTracerouteTestsResource

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from .colos import (
    ColosResource,
    AsyncColosResource,
    ColosResourceWithRawResponse,
    AsyncColosResourceWithRawResponse,
    ColosResourceWithStreamingResponse,
    AsyncColosResourceWithStreamingResponse,
)
from .fleet_status import (
    FleetStatusResource,
    AsyncFleetStatusResource,
    FleetStatusResourceWithRawResponse,
    AsyncFleetStatusResourceWithRawResponse,
    FleetStatusResourceWithStreamingResponse,
    AsyncFleetStatusResourceWithStreamingResponse,
)
from .http_tests import (
    HTTPTestsResource,
    AsyncHTTPTestsResource,
    HTTPTestsResourceWithRawResponse,
    AsyncHTTPTestsResourceWithRawResponse,
    HTTPTestsResourceWithStreamingResponse,
    AsyncHTTPTestsResourceWithStreamingResponse,
)
from .tests import (
    TestsResource,
    AsyncTestsResource,
    TestsResourceWithRawResponse,
    AsyncTestsResourceWithRawResponse,
    TestsResourceWithStreamingResponse,
    AsyncTestsResourceWithStreamingResponse,
)
from .traceroute_test_results import (
    TracerouteTestResultsResource,
    AsyncTracerouteTestResultsResource,
    TracerouteTestResultsResourceWithRawResponse,
    AsyncTracerouteTestResultsResourceWithRawResponse,
    TracerouteTestResultsResourceWithStreamingResponse,
    AsyncTracerouteTestResultsResourceWithStreamingResponse,
)
from .traceroute_tests import (
    TracerouteTestsResource,
    AsyncTracerouteTestsResource,
    TracerouteTestsResourceWithRawResponse,
    AsyncTracerouteTestsResourceWithRawResponse,
    TracerouteTestsResourceWithStreamingResponse,
    AsyncTracerouteTestsResourceWithStreamingResponse,
)

__all__ = ["DEXResource", "AsyncDEXResource"]


class DEXResource(SyncAPIResource):
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
        return DEXResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DEXResourceWithStreamingResponse:
        return DEXResourceWithStreamingResponse(self)


class AsyncDEXResource(AsyncAPIResource):
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
        return AsyncDEXResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDEXResourceWithStreamingResponse:
        return AsyncDEXResourceWithStreamingResponse(self)


class DEXResourceWithRawResponse:
    def __init__(self, dex: DEXResource) -> None:
        self._dex = dex

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
