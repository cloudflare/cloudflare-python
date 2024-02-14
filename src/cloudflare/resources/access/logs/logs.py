# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .access_requests import AccessRequests, AsyncAccessRequests

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
from .access_requests import (
    AccessRequests,
    AsyncAccessRequests,
    AccessRequestsWithRawResponse,
    AsyncAccessRequestsWithRawResponse,
    AccessRequestsWithStreamingResponse,
    AsyncAccessRequestsWithStreamingResponse,
)
from ...._wrappers import ResultWrapper

__all__ = ["Logs", "AsyncLogs"]


class Logs(SyncAPIResource):
    @cached_property
    def access_requests(self) -> AccessRequests:
        return AccessRequests(self._client)

    @cached_property
    def with_raw_response(self) -> LogsWithRawResponse:
        return LogsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogsWithStreamingResponse:
        return LogsWithStreamingResponse(self)


class AsyncLogs(AsyncAPIResource):
    @cached_property
    def access_requests(self) -> AsyncAccessRequests:
        return AsyncAccessRequests(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLogsWithRawResponse:
        return AsyncLogsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogsWithStreamingResponse:
        return AsyncLogsWithStreamingResponse(self)


class LogsWithRawResponse:
    def __init__(self, logs: Logs) -> None:
        self._logs = logs

    @cached_property
    def access_requests(self) -> AccessRequestsWithRawResponse:
        return AccessRequestsWithRawResponse(self._logs.access_requests)


class AsyncLogsWithRawResponse:
    def __init__(self, logs: AsyncLogs) -> None:
        self._logs = logs

    @cached_property
    def access_requests(self) -> AsyncAccessRequestsWithRawResponse:
        return AsyncAccessRequestsWithRawResponse(self._logs.access_requests)


class LogsWithStreamingResponse:
    def __init__(self, logs: Logs) -> None:
        self._logs = logs

    @cached_property
    def access_requests(self) -> AccessRequestsWithStreamingResponse:
        return AccessRequestsWithStreamingResponse(self._logs.access_requests)


class AsyncLogsWithStreamingResponse:
    def __init__(self, logs: AsyncLogs) -> None:
        self._logs = logs

    @cached_property
    def access_requests(self) -> AsyncAccessRequestsWithStreamingResponse:
        return AsyncAccessRequestsWithStreamingResponse(self._logs.access_requests)
