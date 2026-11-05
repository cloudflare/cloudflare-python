# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .streams.streams import (
    StreamsResource,
    AsyncStreamsResource,
    StreamsResourceWithRawResponse,
    AsyncStreamsResourceWithRawResponse,
    StreamsResourceWithStreamingResponse,
    AsyncStreamsResourceWithStreamingResponse,
)

__all__ = ["K2Resource", "AsyncK2Resource"]


class K2Resource(SyncAPIResource):
    @cached_property
    def streams(self) -> StreamsResource:
        return StreamsResource(self._client)

    @cached_property
    def with_raw_response(self) -> K2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return K2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> K2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return K2ResourceWithStreamingResponse(self)


class AsyncK2Resource(AsyncAPIResource):
    @cached_property
    def streams(self) -> AsyncStreamsResource:
        return AsyncStreamsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncK2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncK2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncK2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncK2ResourceWithStreamingResponse(self)


class K2ResourceWithRawResponse:
    def __init__(self, k2: K2Resource) -> None:
        self._k2 = k2

    @cached_property
    def streams(self) -> StreamsResourceWithRawResponse:
        return StreamsResourceWithRawResponse(self._k2.streams)


class AsyncK2ResourceWithRawResponse:
    def __init__(self, k2: AsyncK2Resource) -> None:
        self._k2 = k2

    @cached_property
    def streams(self) -> AsyncStreamsResourceWithRawResponse:
        return AsyncStreamsResourceWithRawResponse(self._k2.streams)


class K2ResourceWithStreamingResponse:
    def __init__(self, k2: K2Resource) -> None:
        self._k2 = k2

    @cached_property
    def streams(self) -> StreamsResourceWithStreamingResponse:
        return StreamsResourceWithStreamingResponse(self._k2.streams)


class AsyncK2ResourceWithStreamingResponse:
    def __init__(self, k2: AsyncK2Resource) -> None:
        self._k2 = k2

    @cached_property
    def streams(self) -> AsyncStreamsResourceWithStreamingResponse:
        return AsyncStreamsResourceWithStreamingResponse(self._k2.streams)
