# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .network_path import NetworkPathResource, AsyncNetworkPathResource

from ....._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .network_path import (
    NetworkPathResource,
    AsyncNetworkPathResource,
    NetworkPathResourceWithRawResponse,
    AsyncNetworkPathResourceWithRawResponse,
    NetworkPathResourceWithStreamingResponse,
    AsyncNetworkPathResourceWithStreamingResponse,
)

__all__ = ["TracerouteTestResultsResource", "AsyncTracerouteTestResultsResource"]


class TracerouteTestResultsResource(SyncAPIResource):
    @cached_property
    def network_path(self) -> NetworkPathResource:
        return NetworkPathResource(self._client)

    @cached_property
    def with_raw_response(self) -> TracerouteTestResultsResourceWithRawResponse:
        return TracerouteTestResultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TracerouteTestResultsResourceWithStreamingResponse:
        return TracerouteTestResultsResourceWithStreamingResponse(self)


class AsyncTracerouteTestResultsResource(AsyncAPIResource):
    @cached_property
    def network_path(self) -> AsyncNetworkPathResource:
        return AsyncNetworkPathResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTracerouteTestResultsResourceWithRawResponse:
        return AsyncTracerouteTestResultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTracerouteTestResultsResourceWithStreamingResponse:
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
