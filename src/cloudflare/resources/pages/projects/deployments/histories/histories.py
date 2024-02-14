# File generated from our OpenAPI spec by Stainless.

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

__all__ = ["Histories", "AsyncHistories"]


class Histories(SyncAPIResource):
    @cached_property
    def logs(self) -> Logs:
        return Logs(self._client)

    @cached_property
    def with_raw_response(self) -> HistoriesWithRawResponse:
        return HistoriesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HistoriesWithStreamingResponse:
        return HistoriesWithStreamingResponse(self)


class AsyncHistories(AsyncAPIResource):
    @cached_property
    def logs(self) -> AsyncLogs:
        return AsyncLogs(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHistoriesWithRawResponse:
        return AsyncHistoriesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHistoriesWithStreamingResponse:
        return AsyncHistoriesWithStreamingResponse(self)


class HistoriesWithRawResponse:
    def __init__(self, histories: Histories) -> None:
        self._histories = histories

    @cached_property
    def logs(self) -> LogsWithRawResponse:
        return LogsWithRawResponse(self._histories.logs)


class AsyncHistoriesWithRawResponse:
    def __init__(self, histories: AsyncHistories) -> None:
        self._histories = histories

    @cached_property
    def logs(self) -> AsyncLogsWithRawResponse:
        return AsyncLogsWithRawResponse(self._histories.logs)


class HistoriesWithStreamingResponse:
    def __init__(self, histories: Histories) -> None:
        self._histories = histories

    @cached_property
    def logs(self) -> LogsWithStreamingResponse:
        return LogsWithStreamingResponse(self._histories.logs)


class AsyncHistoriesWithStreamingResponse:
    def __init__(self, histories: AsyncHistories) -> None:
        self._histories = histories

    @cached_property
    def logs(self) -> AsyncLogsWithStreamingResponse:
        return AsyncLogsWithStreamingResponse(self._histories.logs)
