# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .scim.scim import (
    SCIMResource,
    AsyncSCIMResource,
    SCIMResourceWithRawResponse,
    AsyncSCIMResourceWithRawResponse,
    SCIMResourceWithStreamingResponse,
    AsyncSCIMResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from .access_requests import (
    AccessRequestsResource,
    AsyncAccessRequestsResource,
    AccessRequestsResourceWithRawResponse,
    AsyncAccessRequestsResourceWithRawResponse,
    AccessRequestsResourceWithStreamingResponse,
    AsyncAccessRequestsResourceWithStreamingResponse,
)

__all__ = ["LogsResource", "AsyncLogsResource"]


class LogsResource(SyncAPIResource):
    @cached_property
    def access_requests(self) -> AccessRequestsResource:
        return AccessRequestsResource(self._client)

    @cached_property
    def scim(self) -> SCIMResource:
        return SCIMResource(self._client)

    @cached_property
    def with_raw_response(self) -> LogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return LogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return LogsResourceWithStreamingResponse(self)


class AsyncLogsResource(AsyncAPIResource):
    @cached_property
    def access_requests(self) -> AsyncAccessRequestsResource:
        return AsyncAccessRequestsResource(self._client)

    @cached_property
    def scim(self) -> AsyncSCIMResource:
        return AsyncSCIMResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncLogsResourceWithStreamingResponse(self)


class LogsResourceWithRawResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

    @cached_property
    def access_requests(self) -> AccessRequestsResourceWithRawResponse:
        return AccessRequestsResourceWithRawResponse(self._logs.access_requests)

    @cached_property
    def scim(self) -> SCIMResourceWithRawResponse:
        return SCIMResourceWithRawResponse(self._logs.scim)


class AsyncLogsResourceWithRawResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

    @cached_property
    def access_requests(self) -> AsyncAccessRequestsResourceWithRawResponse:
        return AsyncAccessRequestsResourceWithRawResponse(self._logs.access_requests)

    @cached_property
    def scim(self) -> AsyncSCIMResourceWithRawResponse:
        return AsyncSCIMResourceWithRawResponse(self._logs.scim)


class LogsResourceWithStreamingResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

    @cached_property
    def access_requests(self) -> AccessRequestsResourceWithStreamingResponse:
        return AccessRequestsResourceWithStreamingResponse(self._logs.access_requests)

    @cached_property
    def scim(self) -> SCIMResourceWithStreamingResponse:
        return SCIMResourceWithStreamingResponse(self._logs.scim)


class AsyncLogsResourceWithStreamingResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

    @cached_property
    def access_requests(self) -> AsyncAccessRequestsResourceWithStreamingResponse:
        return AsyncAccessRequestsResourceWithStreamingResponse(self._logs.access_requests)

    @cached_property
    def scim(self) -> AsyncSCIMResourceWithStreamingResponse:
        return AsyncSCIMResourceWithStreamingResponse(self._logs.scim)
