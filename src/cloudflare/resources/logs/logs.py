# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .rayid import (
    RayID,
    AsyncRayID,
    RayIDWithRawResponse,
    AsyncRayIDWithRawResponse,
    RayIDWithStreamingResponse,
    AsyncRayIDWithStreamingResponse,
)
from .control import (
    Control,
    AsyncControl,
    ControlWithRawResponse,
    AsyncControlWithRawResponse,
    ControlWithStreamingResponse,
    AsyncControlWithStreamingResponse,
)
from .received import (
    Received,
    AsyncReceived,
    ReceivedWithRawResponse,
    AsyncReceivedWithRawResponse,
    ReceivedWithStreamingResponse,
    AsyncReceivedWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .control.control import Control, AsyncControl
from .received.received import Received, AsyncReceived

__all__ = ["Logs", "AsyncLogs"]


class Logs(SyncAPIResource):
    @cached_property
    def control(self) -> Control:
        return Control(self._client)

    @cached_property
    def rayid(self) -> RayID:
        return RayID(self._client)

    @cached_property
    def received(self) -> Received:
        return Received(self._client)

    @cached_property
    def with_raw_response(self) -> LogsWithRawResponse:
        return LogsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogsWithStreamingResponse:
        return LogsWithStreamingResponse(self)


class AsyncLogs(AsyncAPIResource):
    @cached_property
    def control(self) -> AsyncControl:
        return AsyncControl(self._client)

    @cached_property
    def rayid(self) -> AsyncRayID:
        return AsyncRayID(self._client)

    @cached_property
    def received(self) -> AsyncReceived:
        return AsyncReceived(self._client)

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
    def control(self) -> ControlWithRawResponse:
        return ControlWithRawResponse(self._logs.control)

    @cached_property
    def rayid(self) -> RayIDWithRawResponse:
        return RayIDWithRawResponse(self._logs.rayid)

    @cached_property
    def received(self) -> ReceivedWithRawResponse:
        return ReceivedWithRawResponse(self._logs.received)


class AsyncLogsWithRawResponse:
    def __init__(self, logs: AsyncLogs) -> None:
        self._logs = logs

    @cached_property
    def control(self) -> AsyncControlWithRawResponse:
        return AsyncControlWithRawResponse(self._logs.control)

    @cached_property
    def rayid(self) -> AsyncRayIDWithRawResponse:
        return AsyncRayIDWithRawResponse(self._logs.rayid)

    @cached_property
    def received(self) -> AsyncReceivedWithRawResponse:
        return AsyncReceivedWithRawResponse(self._logs.received)


class LogsWithStreamingResponse:
    def __init__(self, logs: Logs) -> None:
        self._logs = logs

    @cached_property
    def control(self) -> ControlWithStreamingResponse:
        return ControlWithStreamingResponse(self._logs.control)

    @cached_property
    def rayid(self) -> RayIDWithStreamingResponse:
        return RayIDWithStreamingResponse(self._logs.rayid)

    @cached_property
    def received(self) -> ReceivedWithStreamingResponse:
        return ReceivedWithStreamingResponse(self._logs.received)


class AsyncLogsWithStreamingResponse:
    def __init__(self, logs: AsyncLogs) -> None:
        self._logs = logs

    @cached_property
    def control(self) -> AsyncControlWithStreamingResponse:
        return AsyncControlWithStreamingResponse(self._logs.control)

    @cached_property
    def rayid(self) -> AsyncRayIDWithStreamingResponse:
        return AsyncRayIDWithStreamingResponse(self._logs.rayid)

    @cached_property
    def received(self) -> AsyncReceivedWithStreamingResponse:
        return AsyncReceivedWithStreamingResponse(self._logs.received)
