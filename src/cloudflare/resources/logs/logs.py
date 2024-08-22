# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .rayid import (
    RayIDResource,
    AsyncRayIDResource,
    RayIDResourceWithRawResponse,
    AsyncRayIDResourceWithRawResponse,
    RayIDResourceWithStreamingResponse,
    AsyncRayIDResourceWithStreamingResponse,
)
from .control import (
    ControlResource,
    AsyncControlResource,
    ControlResourceWithRawResponse,
    AsyncControlResourceWithRawResponse,
    ControlResourceWithStreamingResponse,
    AsyncControlResourceWithStreamingResponse,
)
from .received import (
    ReceivedResource,
    AsyncReceivedResource,
    ReceivedResourceWithRawResponse,
    AsyncReceivedResourceWithRawResponse,
    ReceivedResourceWithStreamingResponse,
    AsyncReceivedResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .control.control import ControlResource, AsyncControlResource
from .received.received import ReceivedResource, AsyncReceivedResource

__all__ = ["LogsResource", "AsyncLogsResource"]


class LogsResource(SyncAPIResource):
    @cached_property
    def control(self) -> ControlResource:
        return ControlResource(self._client)

    @cached_property
    def rayid(self) -> RayIDResource:
        return RayIDResource(self._client)

    @cached_property
    def received(self) -> ReceivedResource:
        return ReceivedResource(self._client)

    @cached_property
    def with_raw_response(self) -> LogsResourceWithRawResponse:
        return LogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogsResourceWithStreamingResponse:
        return LogsResourceWithStreamingResponse(self)


class AsyncLogsResource(AsyncAPIResource):
    @cached_property
    def control(self) -> AsyncControlResource:
        return AsyncControlResource(self._client)

    @cached_property
    def rayid(self) -> AsyncRayIDResource:
        return AsyncRayIDResource(self._client)

    @cached_property
    def received(self) -> AsyncReceivedResource:
        return AsyncReceivedResource(self._client)

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
    def control(self) -> ControlResourceWithRawResponse:
        return ControlResourceWithRawResponse(self._logs.control)

    @cached_property
    def rayid(self) -> RayIDResourceWithRawResponse:
        return RayIDResourceWithRawResponse(self._logs.rayid)

    @cached_property
    def received(self) -> ReceivedResourceWithRawResponse:
        return ReceivedResourceWithRawResponse(self._logs.received)


class AsyncLogsResourceWithRawResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

    @cached_property
    def control(self) -> AsyncControlResourceWithRawResponse:
        return AsyncControlResourceWithRawResponse(self._logs.control)

    @cached_property
    def rayid(self) -> AsyncRayIDResourceWithRawResponse:
        return AsyncRayIDResourceWithRawResponse(self._logs.rayid)

    @cached_property
    def received(self) -> AsyncReceivedResourceWithRawResponse:
        return AsyncReceivedResourceWithRawResponse(self._logs.received)


class LogsResourceWithStreamingResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

    @cached_property
    def control(self) -> ControlResourceWithStreamingResponse:
        return ControlResourceWithStreamingResponse(self._logs.control)

    @cached_property
    def rayid(self) -> RayIDResourceWithStreamingResponse:
        return RayIDResourceWithStreamingResponse(self._logs.rayid)

    @cached_property
    def received(self) -> ReceivedResourceWithStreamingResponse:
        return ReceivedResourceWithStreamingResponse(self._logs.received)


class AsyncLogsResourceWithStreamingResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

    @cached_property
    def control(self) -> AsyncControlResourceWithStreamingResponse:
        return AsyncControlResourceWithStreamingResponse(self._logs.control)

    @cached_property
    def rayid(self) -> AsyncRayIDResourceWithStreamingResponse:
        return AsyncRayIDResourceWithStreamingResponse(self._logs.rayid)

    @cached_property
    def received(self) -> AsyncReceivedResourceWithStreamingResponse:
        return AsyncReceivedResourceWithStreamingResponse(self._logs.received)
