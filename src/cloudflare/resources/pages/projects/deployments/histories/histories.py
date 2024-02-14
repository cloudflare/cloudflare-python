# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .logs import Logs, AsyncLogs

from ......_compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ......_utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ......_types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ......types import shared_params
from .logs import (
    Logs,
    AsyncLogs,
    LogsWithRawResponse,
    AsyncLogsWithRawResponse,
    LogsWithStreamingResponse,
    AsyncLogsWithStreamingResponse,
)
from ......_wrappers import ResultWrapper

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
