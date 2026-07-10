# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .query import (
    QueryResource,
    AsyncQueryResource,
    QueryResourceWithRawResponse,
    AsyncQueryResourceWithRawResponse,
    QueryResourceWithStreamingResponse,
    AsyncQueryResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .datasets.datasets import (
    DatasetsResource,
    AsyncDatasetsResource,
    DatasetsResourceWithRawResponse,
    AsyncDatasetsResourceWithRawResponse,
    DatasetsResourceWithStreamingResponse,
    AsyncDatasetsResourceWithStreamingResponse,
)

__all__ = ["LogExplorerResource", "AsyncLogExplorerResource"]


class LogExplorerResource(SyncAPIResource):
    @cached_property
    def query(self) -> QueryResource:
        return QueryResource(self._client)

    @cached_property
    def datasets(self) -> DatasetsResource:
        return DatasetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> LogExplorerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return LogExplorerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogExplorerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return LogExplorerResourceWithStreamingResponse(self)


class AsyncLogExplorerResource(AsyncAPIResource):
    @cached_property
    def query(self) -> AsyncQueryResource:
        return AsyncQueryResource(self._client)

    @cached_property
    def datasets(self) -> AsyncDatasetsResource:
        return AsyncDatasetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLogExplorerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLogExplorerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogExplorerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncLogExplorerResourceWithStreamingResponse(self)


class LogExplorerResourceWithRawResponse:
    def __init__(self, log_explorer: LogExplorerResource) -> None:
        self._log_explorer = log_explorer

    @cached_property
    def query(self) -> QueryResourceWithRawResponse:
        return QueryResourceWithRawResponse(self._log_explorer.query)

    @cached_property
    def datasets(self) -> DatasetsResourceWithRawResponse:
        return DatasetsResourceWithRawResponse(self._log_explorer.datasets)


class AsyncLogExplorerResourceWithRawResponse:
    def __init__(self, log_explorer: AsyncLogExplorerResource) -> None:
        self._log_explorer = log_explorer

    @cached_property
    def query(self) -> AsyncQueryResourceWithRawResponse:
        return AsyncQueryResourceWithRawResponse(self._log_explorer.query)

    @cached_property
    def datasets(self) -> AsyncDatasetsResourceWithRawResponse:
        return AsyncDatasetsResourceWithRawResponse(self._log_explorer.datasets)


class LogExplorerResourceWithStreamingResponse:
    def __init__(self, log_explorer: LogExplorerResource) -> None:
        self._log_explorer = log_explorer

    @cached_property
    def query(self) -> QueryResourceWithStreamingResponse:
        return QueryResourceWithStreamingResponse(self._log_explorer.query)

    @cached_property
    def datasets(self) -> DatasetsResourceWithStreamingResponse:
        return DatasetsResourceWithStreamingResponse(self._log_explorer.datasets)


class AsyncLogExplorerResourceWithStreamingResponse:
    def __init__(self, log_explorer: AsyncLogExplorerResource) -> None:
        self._log_explorer = log_explorer

    @cached_property
    def query(self) -> AsyncQueryResourceWithStreamingResponse:
        return AsyncQueryResourceWithStreamingResponse(self._log_explorer.query)

    @cached_property
    def datasets(self) -> AsyncDatasetsResourceWithStreamingResponse:
        return AsyncDatasetsResourceWithStreamingResponse(self._log_explorer.datasets)
