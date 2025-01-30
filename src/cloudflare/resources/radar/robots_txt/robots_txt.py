# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .top.top import (
    TopResource,
    AsyncTopResource,
    TopResourceWithRawResponse,
    AsyncTopResourceWithRawResponse,
    TopResourceWithStreamingResponse,
    AsyncTopResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["RobotsTXTResource", "AsyncRobotsTXTResource"]


class RobotsTXTResource(SyncAPIResource):
    @cached_property
    def top(self) -> TopResource:
        return TopResource(self._client)

    @cached_property
    def with_raw_response(self) -> RobotsTXTResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RobotsTXTResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RobotsTXTResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RobotsTXTResourceWithStreamingResponse(self)


class AsyncRobotsTXTResource(AsyncAPIResource):
    @cached_property
    def top(self) -> AsyncTopResource:
        return AsyncTopResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRobotsTXTResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRobotsTXTResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRobotsTXTResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
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
