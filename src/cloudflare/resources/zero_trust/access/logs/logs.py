# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from .access_requests import (
    AccessRequests,
    AsyncAccessRequests,
    AccessRequestsWithRawResponse,
    AsyncAccessRequestsWithRawResponse,
    AccessRequestsWithStreamingResponse,
    AsyncAccessRequestsWithStreamingResponse,
)

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
