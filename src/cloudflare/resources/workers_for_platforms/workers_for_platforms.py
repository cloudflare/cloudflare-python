# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .dispatch import (
    DispatchResource,
    AsyncDispatchResource,
    DispatchResourceWithRawResponse,
    AsyncDispatchResourceWithRawResponse,
    DispatchResourceWithStreamingResponse,
    AsyncDispatchResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .dispatch.dispatch import DispatchResource, AsyncDispatchResource

__all__ = ["WorkersForPlatformsResource", "AsyncWorkersForPlatformsResource"]


class WorkersForPlatformsResource(SyncAPIResource):
    @cached_property
    def dispatch(self) -> DispatchResource:
        return DispatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> WorkersForPlatformsResourceWithRawResponse:
        return WorkersForPlatformsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkersForPlatformsResourceWithStreamingResponse:
        return WorkersForPlatformsResourceWithStreamingResponse(self)


class AsyncWorkersForPlatformsResource(AsyncAPIResource):
    @cached_property
    def dispatch(self) -> AsyncDispatchResource:
        return AsyncDispatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWorkersForPlatformsResourceWithRawResponse:
        return AsyncWorkersForPlatformsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkersForPlatformsResourceWithStreamingResponse:
        return AsyncWorkersForPlatformsResourceWithStreamingResponse(self)


class WorkersForPlatformsResourceWithRawResponse:
    def __init__(self, workers_for_platforms: WorkersForPlatformsResource) -> None:
        self._workers_for_platforms = workers_for_platforms

    @cached_property
    def dispatch(self) -> DispatchResourceWithRawResponse:
        return DispatchResourceWithRawResponse(self._workers_for_platforms.dispatch)


class AsyncWorkersForPlatformsResourceWithRawResponse:
    def __init__(self, workers_for_platforms: AsyncWorkersForPlatformsResource) -> None:
        self._workers_for_platforms = workers_for_platforms

    @cached_property
    def dispatch(self) -> AsyncDispatchResourceWithRawResponse:
        return AsyncDispatchResourceWithRawResponse(self._workers_for_platforms.dispatch)


class WorkersForPlatformsResourceWithStreamingResponse:
    def __init__(self, workers_for_platforms: WorkersForPlatformsResource) -> None:
        self._workers_for_platforms = workers_for_platforms

    @cached_property
    def dispatch(self) -> DispatchResourceWithStreamingResponse:
        return DispatchResourceWithStreamingResponse(self._workers_for_platforms.dispatch)


class AsyncWorkersForPlatformsResourceWithStreamingResponse:
    def __init__(self, workers_for_platforms: AsyncWorkersForPlatformsResource) -> None:
        self._workers_for_platforms = workers_for_platforms

    @cached_property
    def dispatch(self) -> AsyncDispatchResourceWithStreamingResponse:
        return AsyncDispatchResourceWithStreamingResponse(self._workers_for_platforms.dispatch)
