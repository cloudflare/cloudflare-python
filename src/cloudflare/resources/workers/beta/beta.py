# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .workers.workers import (
    WorkersResource,
    AsyncWorkersResource,
    WorkersResourceWithRawResponse,
    AsyncWorkersResourceWithRawResponse,
    WorkersResourceWithStreamingResponse,
    AsyncWorkersResourceWithStreamingResponse,
)

__all__ = ["BetaResource", "AsyncBetaResource"]


class BetaResource(SyncAPIResource):
    @cached_property
    def workers(self) -> WorkersResource:
        return WorkersResource(self._client)

    @cached_property
    def with_raw_response(self) -> BetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return BetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return BetaResourceWithStreamingResponse(self)


class AsyncBetaResource(AsyncAPIResource):
    @cached_property
    def workers(self) -> AsyncWorkersResource:
        return AsyncWorkersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncBetaResourceWithStreamingResponse(self)


class BetaResourceWithRawResponse:
    def __init__(self, beta: BetaResource) -> None:
        self._beta = beta

    @cached_property
    def workers(self) -> WorkersResourceWithRawResponse:
        return WorkersResourceWithRawResponse(self._beta.workers)


class AsyncBetaResourceWithRawResponse:
    def __init__(self, beta: AsyncBetaResource) -> None:
        self._beta = beta

    @cached_property
    def workers(self) -> AsyncWorkersResourceWithRawResponse:
        return AsyncWorkersResourceWithRawResponse(self._beta.workers)


class BetaResourceWithStreamingResponse:
    def __init__(self, beta: BetaResource) -> None:
        self._beta = beta

    @cached_property
    def workers(self) -> WorkersResourceWithStreamingResponse:
        return WorkersResourceWithStreamingResponse(self._beta.workers)


class AsyncBetaResourceWithStreamingResponse:
    def __init__(self, beta: AsyncBetaResource) -> None:
        self._beta = beta

    @cached_property
    def workers(self) -> AsyncWorkersResourceWithStreamingResponse:
        return AsyncWorkersResourceWithStreamingResponse(self._beta.workers)
