# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .access_requests import AccessRequestsResource, AsyncAccessRequestsResource

from ....._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .access_requests import AccessRequestsResource, AsyncAccessRequestsResource, AccessRequestsResourceWithRawResponse, AsyncAccessRequestsResourceWithRawResponse, AccessRequestsResourceWithStreamingResponse, AsyncAccessRequestsResourceWithStreamingResponse

__all__ = ["LogsResource", "AsyncLogsResource"]

class LogsResource(SyncAPIResource):
    @cached_property
    def access_requests(self) -> AccessRequestsResource:
        return AccessRequestsResource(self._client)

    @cached_property
    def with_raw_response(self) -> LogsResourceWithRawResponse:
        return LogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogsResourceWithStreamingResponse:
        return LogsResourceWithStreamingResponse(self)

class AsyncLogsResource(AsyncAPIResource):
    @cached_property
    def access_requests(self) -> AsyncAccessRequestsResource:
        return AsyncAccessRequestsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLogsResourceWithRawResponse:
        return AsyncLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogsResourceWithStreamingResponse:
        return AsyncLogsResourceWithStreamingResponse(self)

class LogsResourceWithRawResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

    @cached_property
    def access_requests(self) -> AccessRequestsResourceWithRawResponse:
        return AccessRequestsResourceWithRawResponse(self._logs.access_requests)

class AsyncLogsResourceWithRawResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

    @cached_property
    def access_requests(self) -> AsyncAccessRequestsResourceWithRawResponse:
        return AsyncAccessRequestsResourceWithRawResponse(self._logs.access_requests)

class LogsResourceWithStreamingResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

    @cached_property
    def access_requests(self) -> AccessRequestsResourceWithStreamingResponse:
        return AccessRequestsResourceWithStreamingResponse(self._logs.access_requests)

class AsyncLogsResourceWithStreamingResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

    @cached_property
    def access_requests(self) -> AsyncAccessRequestsResourceWithStreamingResponse:
        return AsyncAccessRequestsResourceWithStreamingResponse(self._logs.access_requests)