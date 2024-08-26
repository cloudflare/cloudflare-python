# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .traces import TracesResource, AsyncTracesResource

from ..._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from .traces import TracesResource, AsyncTracesResource, TracesResourceWithRawResponse, AsyncTracesResourceWithRawResponse, TracesResourceWithStreamingResponse, AsyncTracesResourceWithStreamingResponse

__all__ = ["RequestTracersResource", "AsyncRequestTracersResource"]

class RequestTracersResource(SyncAPIResource):
    @cached_property
    def traces(self) -> TracesResource:
        return TracesResource(self._client)

    @cached_property
    def with_raw_response(self) -> RequestTracersResourceWithRawResponse:
        return RequestTracersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RequestTracersResourceWithStreamingResponse:
        return RequestTracersResourceWithStreamingResponse(self)

class AsyncRequestTracersResource(AsyncAPIResource):
    @cached_property
    def traces(self) -> AsyncTracesResource:
        return AsyncTracesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRequestTracersResourceWithRawResponse:
        return AsyncRequestTracersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRequestTracersResourceWithStreamingResponse:
        return AsyncRequestTracersResourceWithStreamingResponse(self)

class RequestTracersResourceWithRawResponse:
    def __init__(self, request_tracers: RequestTracersResource) -> None:
        self._request_tracers = request_tracers

    @cached_property
    def traces(self) -> TracesResourceWithRawResponse:
        return TracesResourceWithRawResponse(self._request_tracers.traces)

class AsyncRequestTracersResourceWithRawResponse:
    def __init__(self, request_tracers: AsyncRequestTracersResource) -> None:
        self._request_tracers = request_tracers

    @cached_property
    def traces(self) -> AsyncTracesResourceWithRawResponse:
        return AsyncTracesResourceWithRawResponse(self._request_tracers.traces)

class RequestTracersResourceWithStreamingResponse:
    def __init__(self, request_tracers: RequestTracersResource) -> None:
        self._request_tracers = request_tracers

    @cached_property
    def traces(self) -> TracesResourceWithStreamingResponse:
        return TracesResourceWithStreamingResponse(self._request_tracers.traces)

class AsyncRequestTracersResourceWithStreamingResponse:
    def __init__(self, request_tracers: AsyncRequestTracersResource) -> None:
        self._request_tracers = request_tracers

    @cached_property
    def traces(self) -> AsyncTracesResourceWithStreamingResponse:
        return AsyncTracesResourceWithStreamingResponse(self._request_tracers.traces)