# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .dispatch.dispatch import (
    DispatchResource,
    AsyncDispatchResource,
    DispatchResourceWithRawResponse,
    AsyncDispatchResourceWithRawResponse,
    DispatchResourceWithStreamingResponse,
    AsyncDispatchResourceWithStreamingResponse,
)

__all__ = ["WorkersForPlatformsResource", "AsyncWorkersForPlatformsResource"]


class WorkersForPlatformsResource(SyncAPIResource):
    @cached_property
    def dispatch(self) -> DispatchResource:
        return DispatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> WorkersForPlatformsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return WorkersForPlatformsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkersForPlatformsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return WorkersForPlatformsResourceWithStreamingResponse(self)


class AsyncWorkersForPlatformsResource(AsyncAPIResource):
    @cached_property
    def dispatch(self) -> AsyncDispatchResource:
        return AsyncDispatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWorkersForPlatformsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkersForPlatformsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkersForPlatformsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
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
