# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .traces import (
    TracesResource,
    AsyncTracesResource,
    TracesResourceWithRawResponse,
    AsyncTracesResourceWithRawResponse,
    TracesResourceWithStreamingResponse,
    AsyncTracesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["RequestTracersResource", "AsyncRequestTracersResource"]


class RequestTracersResource(SyncAPIResource):
    @cached_property
    def traces(self) -> TracesResource:
        return TracesResource(self._client)

    @cached_property
    def with_raw_response(self) -> RequestTracersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RequestTracersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RequestTracersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RequestTracersResourceWithStreamingResponse(self)


class AsyncRequestTracersResource(AsyncAPIResource):
    @cached_property
    def traces(self) -> AsyncTracesResource:
        return AsyncTracesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRequestTracersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRequestTracersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRequestTracersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRequestTracersResourceWithStreamingResponse(self)


class RequestTracersResourceWithRawResponse:
    def __init__(self, request_tracers: RequestTracersResource) -> None:
        self._request_tracers = request_tracers

    @cached_property
    def traces(self) -> TracesResourceWithRawResponse:
        return TracesResourceWithRawResponse(self._request_tracers.traces)


class AsyncRequestTracersResourceWithRawResponse:
    def __init__(self, request_tracers: AsyncRequestTracersResource) -> None:
        self._request_tracers = request_tracers

    @cached_property
    def traces(self) -> AsyncTracesResourceWithRawResponse:
        return AsyncTracesResourceWithRawResponse(self._request_tracers.traces)


class RequestTracersResourceWithStreamingResponse:
    def __init__(self, request_tracers: RequestTracersResource) -> None:
        self._request_tracers = request_tracers

    @cached_property
    def traces(self) -> TracesResourceWithStreamingResponse:
        return TracesResourceWithStreamingResponse(self._request_tracers.traces)


class AsyncRequestTracersResourceWithStreamingResponse:
    def __init__(self, request_tracers: AsyncRequestTracersResource) -> None:
        self._request_tracers = request_tracers

    @cached_property
    def traces(self) -> AsyncTracesResourceWithStreamingResponse:
        return AsyncTracesResourceWithStreamingResponse(self._request_tracers.traces)
