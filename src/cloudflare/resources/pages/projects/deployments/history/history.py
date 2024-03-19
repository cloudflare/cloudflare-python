# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .logs import (
    Logs,
    AsyncLogs,
    LogsWithRawResponse,
    AsyncLogsWithRawResponse,
    LogsWithStreamingResponse,
    AsyncLogsWithStreamingResponse,
)
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource

__all__ = ["History", "AsyncHistory"]


class History(SyncAPIResource):
    @cached_property
    def logs(self) -> Logs:
        return Logs(self._client)

    @cached_property
    def with_raw_response(self) -> HistoryWithRawResponse:
        return HistoryWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HistoryWithStreamingResponse:
        return HistoryWithStreamingResponse(self)


class AsyncHistory(AsyncAPIResource):
    @cached_property
    def logs(self) -> AsyncLogs:
        return AsyncLogs(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHistoryWithRawResponse:
        return AsyncHistoryWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHistoryWithStreamingResponse:
        return AsyncHistoryWithStreamingResponse(self)


class HistoryWithRawResponse:
    def __init__(self, history: History) -> None:
        self._history = history

    @cached_property
    def logs(self) -> LogsWithRawResponse:
        return LogsWithRawResponse(self._history.logs)


class AsyncHistoryWithRawResponse:
    def __init__(self, history: AsyncHistory) -> None:
        self._history = history

    @cached_property
    def logs(self) -> AsyncLogsWithRawResponse:
        return AsyncLogsWithRawResponse(self._history.logs)


class HistoryWithStreamingResponse:
    def __init__(self, history: History) -> None:
        self._history = history

    @cached_property
    def logs(self) -> LogsWithStreamingResponse:
        return LogsWithStreamingResponse(self._history.logs)


class AsyncHistoryWithStreamingResponse:
    def __init__(self, history: AsyncHistory) -> None:
        self._history = history

    @cached_property
    def logs(self) -> AsyncLogsWithStreamingResponse:
        return AsyncLogsWithStreamingResponse(self._history.logs)
