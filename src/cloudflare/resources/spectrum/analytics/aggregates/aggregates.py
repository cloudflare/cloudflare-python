# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .currents import (
    CurrentsResource,
    AsyncCurrentsResource,
    CurrentsResourceWithRawResponse,
    AsyncCurrentsResourceWithRawResponse,
    CurrentsResourceWithStreamingResponse,
    AsyncCurrentsResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["AggregatesResource", "AsyncAggregatesResource"]


class AggregatesResource(SyncAPIResource):
    @cached_property
    def currents(self) -> CurrentsResource:
        return CurrentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AggregatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AggregatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AggregatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AggregatesResourceWithStreamingResponse(self)


class AsyncAggregatesResource(AsyncAPIResource):
    @cached_property
    def currents(self) -> AsyncCurrentsResource:
        return AsyncCurrentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAggregatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAggregatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAggregatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAggregatesResourceWithStreamingResponse(self)


class AggregatesResourceWithRawResponse:
    def __init__(self, aggregates: AggregatesResource) -> None:
        self._aggregates = aggregates

    @cached_property
    def currents(self) -> CurrentsResourceWithRawResponse:
        return CurrentsResourceWithRawResponse(self._aggregates.currents)


class AsyncAggregatesResourceWithRawResponse:
    def __init__(self, aggregates: AsyncAggregatesResource) -> None:
        self._aggregates = aggregates

    @cached_property
    def currents(self) -> AsyncCurrentsResourceWithRawResponse:
        return AsyncCurrentsResourceWithRawResponse(self._aggregates.currents)


class AggregatesResourceWithStreamingResponse:
    def __init__(self, aggregates: AggregatesResource) -> None:
        self._aggregates = aggregates

    @cached_property
    def currents(self) -> CurrentsResourceWithStreamingResponse:
        return CurrentsResourceWithStreamingResponse(self._aggregates.currents)


class AsyncAggregatesResourceWithStreamingResponse:
    def __init__(self, aggregates: AsyncAggregatesResource) -> None:
        self._aggregates = aggregates

    @cached_property
    def currents(self) -> AsyncCurrentsResourceWithStreamingResponse:
        return AsyncCurrentsResourceWithStreamingResponse(self._aggregates.currents)
