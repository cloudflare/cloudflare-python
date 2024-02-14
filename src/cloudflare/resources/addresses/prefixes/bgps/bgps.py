# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .statuses import (
    Statuses,
    AsyncStatuses,
    StatusesWithRawResponse,
    AsyncStatusesWithRawResponse,
    StatusesWithStreamingResponse,
    AsyncStatusesWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["BGPs", "AsyncBGPs"]


class BGPs(SyncAPIResource):
    @cached_property
    def statuses(self) -> Statuses:
        return Statuses(self._client)

    @cached_property
    def with_raw_response(self) -> BGPsWithRawResponse:
        return BGPsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BGPsWithStreamingResponse:
        return BGPsWithStreamingResponse(self)


class AsyncBGPs(AsyncAPIResource):
    @cached_property
    def statuses(self) -> AsyncStatuses:
        return AsyncStatuses(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBGPsWithRawResponse:
        return AsyncBGPsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBGPsWithStreamingResponse:
        return AsyncBGPsWithStreamingResponse(self)


class BGPsWithRawResponse:
    def __init__(self, bgps: BGPs) -> None:
        self._bgps = bgps

    @cached_property
    def statuses(self) -> StatusesWithRawResponse:
        return StatusesWithRawResponse(self._bgps.statuses)


class AsyncBGPsWithRawResponse:
    def __init__(self, bgps: AsyncBGPs) -> None:
        self._bgps = bgps

    @cached_property
    def statuses(self) -> AsyncStatusesWithRawResponse:
        return AsyncStatusesWithRawResponse(self._bgps.statuses)


class BGPsWithStreamingResponse:
    def __init__(self, bgps: BGPs) -> None:
        self._bgps = bgps

    @cached_property
    def statuses(self) -> StatusesWithStreamingResponse:
        return StatusesWithStreamingResponse(self._bgps.statuses)


class AsyncBGPsWithStreamingResponse:
    def __init__(self, bgps: AsyncBGPs) -> None:
        self._bgps = bgps

    @cached_property
    def statuses(self) -> AsyncStatusesWithStreamingResponse:
        return AsyncStatusesWithStreamingResponse(self._bgps.statuses)
