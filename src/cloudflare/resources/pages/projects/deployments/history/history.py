# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .logs import (
    LogsResource,
    AsyncLogsResource,
    LogsResourceWithRawResponse,
    AsyncLogsResourceWithRawResponse,
    LogsResourceWithStreamingResponse,
    AsyncLogsResourceWithStreamingResponse,
)
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource

__all__ = ["HistoryResource", "AsyncHistoryResource"]


class HistoryResource(SyncAPIResource):
    @cached_property
    def logs(self) -> LogsResource:
        return LogsResource(self._client)

    @cached_property
    def with_raw_response(self) -> HistoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return HistoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HistoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return HistoryResourceWithStreamingResponse(self)


class AsyncHistoryResource(AsyncAPIResource):
    @cached_property
    def logs(self) -> AsyncLogsResource:
        return AsyncLogsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHistoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHistoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHistoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncHistoryResourceWithStreamingResponse(self)


class HistoryResourceWithRawResponse:
    def __init__(self, history: HistoryResource) -> None:
        self._history = history

    @cached_property
    def logs(self) -> LogsResourceWithRawResponse:
        return LogsResourceWithRawResponse(self._history.logs)


class AsyncHistoryResourceWithRawResponse:
    def __init__(self, history: AsyncHistoryResource) -> None:
        self._history = history

    @cached_property
    def logs(self) -> AsyncLogsResourceWithRawResponse:
        return AsyncLogsResourceWithRawResponse(self._history.logs)


class HistoryResourceWithStreamingResponse:
    def __init__(self, history: HistoryResource) -> None:
        self._history = history

    @cached_property
    def logs(self) -> LogsResourceWithStreamingResponse:
        return LogsResourceWithStreamingResponse(self._history.logs)


class AsyncHistoryResourceWithStreamingResponse:
    def __init__(self, history: AsyncHistoryResource) -> None:
        self._history = history

    @cached_property
    def logs(self) -> AsyncLogsResourceWithStreamingResponse:
        return AsyncLogsResourceWithStreamingResponse(self._history.logs)
