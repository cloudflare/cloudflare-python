# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .traces import Traces, AsyncTraces

from ..._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from .traces import (
    Traces,
    AsyncTraces,
    TracesWithRawResponse,
    AsyncTracesWithRawResponse,
    TracesWithStreamingResponse,
    AsyncTracesWithStreamingResponse,
)
from ..._wrappers import ResultWrapper

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
