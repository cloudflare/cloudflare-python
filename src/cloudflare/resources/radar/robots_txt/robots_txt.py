# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .top import (
    TopResource,
    AsyncTopResource,
    TopResourceWithRawResponse,
    AsyncTopResourceWithRawResponse,
    TopResourceWithStreamingResponse,
    AsyncTopResourceWithStreamingResponse,
)
from .top.top import TopResource, AsyncTopResource
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["RobotsTXTResource", "AsyncRobotsTXTResource"]


class RobotsTXTResource(SyncAPIResource):
    @cached_property
    def top(self) -> TopResource:
        return TopResource(self._client)

    @cached_property
    def with_raw_response(self) -> RobotsTXTResourceWithRawResponse:
        return RobotsTXTResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RobotsTXTResourceWithStreamingResponse:
        return RobotsTXTResourceWithStreamingResponse(self)


class AsyncRobotsTXTResource(AsyncAPIResource):
    @cached_property
    def top(self) -> AsyncTopResource:
        return AsyncTopResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRobotsTXTResourceWithRawResponse:
        return AsyncRobotsTXTResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRobotsTXTResourceWithStreamingResponse:
        return AsyncRobotsTXTResourceWithStreamingResponse(self)


class RobotsTXTResourceWithRawResponse:
    def __init__(self, robots_txt: RobotsTXTResource) -> None:
        self._robots_txt = robots_txt

    @cached_property
    def top(self) -> TopResourceWithRawResponse:
        return TopResourceWithRawResponse(self._robots_txt.top)


class AsyncRobotsTXTResourceWithRawResponse:
    def __init__(self, robots_txt: AsyncRobotsTXTResource) -> None:
        self._robots_txt = robots_txt

    @cached_property
    def top(self) -> AsyncTopResourceWithRawResponse:
        return AsyncTopResourceWithRawResponse(self._robots_txt.top)


class RobotsTXTResourceWithStreamingResponse:
    def __init__(self, robots_txt: RobotsTXTResource) -> None:
        self._robots_txt = robots_txt

    @cached_property
    def top(self) -> TopResourceWithStreamingResponse:
        return TopResourceWithStreamingResponse(self._robots_txt.top)


class AsyncRobotsTXTResourceWithStreamingResponse:
    def __init__(self, robots_txt: AsyncRobotsTXTResource) -> None:
        self._robots_txt = robots_txt

    @cached_property
    def top(self) -> AsyncTopResourceWithStreamingResponse:
        return AsyncTopResourceWithStreamingResponse(self._robots_txt.top)
