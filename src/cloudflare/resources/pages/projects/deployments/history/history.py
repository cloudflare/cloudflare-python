# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .logs import LogsResource, AsyncLogsResource

from ......_compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ......_utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ......_types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......types import shared_params
from .logs import LogsResource, AsyncLogsResource, LogsResourceWithRawResponse, AsyncLogsResourceWithRawResponse, LogsResourceWithStreamingResponse, AsyncLogsResourceWithStreamingResponse

__all__ = ["HistoryResource", "AsyncHistoryResource"]

class HistoryResource(SyncAPIResource):
    @cached_property
    def logs(self) -> LogsResource:
        return LogsResource(self._client)

    @cached_property
    def with_raw_response(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self)

class AsyncHistoryResource(AsyncAPIResource):
    @cached_property
    def logs(self) -> AsyncLogsResource:
        return AsyncLogsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self)

class HistoryResourceWithRawResponse:
    def __init__(self, history: HistoryResource) -> None:
        self._history = history

    @cached_property
    def logs(self) -> LogsResourceWithRawResponse:
        return LogsResourceWithRawResponse(self._history.logs)

class AsyncHistoryResourceWithRawResponse:
    def __init__(self, history: AsyncHistoryResource) -> None:
        self._history = history

    @cached_property
    def logs(self) -> AsyncLogsResourceWithRawResponse:
        return AsyncLogsResourceWithRawResponse(self._history.logs)

class HistoryResourceWithStreamingResponse:
    def __init__(self, history: HistoryResource) -> None:
        self._history = history

    @cached_property
    def logs(self) -> LogsResourceWithStreamingResponse:
        return LogsResourceWithStreamingResponse(self._history.logs)

class AsyncHistoryResourceWithStreamingResponse:
    def __init__(self, history: AsyncHistoryResource) -> None:
        self._history = history

    @cached_property
    def logs(self) -> AsyncLogsResourceWithStreamingResponse:
        return AsyncLogsResourceWithStreamingResponse(self._history.logs)