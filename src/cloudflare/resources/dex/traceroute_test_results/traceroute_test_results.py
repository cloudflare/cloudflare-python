# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .network_path import NetworkPath, AsyncNetworkPath

from ...._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from .network_path import (
    NetworkPath,
    AsyncNetworkPath,
    NetworkPathWithRawResponse,
    AsyncNetworkPathWithRawResponse,
    NetworkPathWithStreamingResponse,
    AsyncNetworkPathWithStreamingResponse,
)
from ...._wrappers import ResultWrapper

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
