# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .indexes.indexes import (
    IndexesResource,
    AsyncIndexesResource,
    IndexesResourceWithRawResponse,
    AsyncIndexesResourceWithRawResponse,
    IndexesResourceWithStreamingResponse,
    AsyncIndexesResourceWithStreamingResponse,
)

__all__ = ["VectorizeResource", "AsyncVectorizeResource"]


class VectorizeResource(SyncAPIResource):
    @cached_property
    def indexes(self) -> IndexesResource:
        return IndexesResource(self._client)

    @cached_property
    def with_raw_response(self) -> VectorizeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return VectorizeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VectorizeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return VectorizeResourceWithStreamingResponse(self)


class AsyncVectorizeResource(AsyncAPIResource):
    @cached_property
    def indexes(self) -> AsyncIndexesResource:
        return AsyncIndexesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVectorizeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVectorizeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVectorizeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncVectorizeResourceWithStreamingResponse(self)


class VectorizeResourceWithRawResponse:
    def __init__(self, vectorize: VectorizeResource) -> None:
        self._vectorize = vectorize

    @cached_property
    def indexes(self) -> IndexesResourceWithRawResponse:
        return IndexesResourceWithRawResponse(self._vectorize.indexes)


class AsyncVectorizeResourceWithRawResponse:
    def __init__(self, vectorize: AsyncVectorizeResource) -> None:
        self._vectorize = vectorize

    @cached_property
    def indexes(self) -> AsyncIndexesResourceWithRawResponse:
        return AsyncIndexesResourceWithRawResponse(self._vectorize.indexes)


class VectorizeResourceWithStreamingResponse:
    def __init__(self, vectorize: VectorizeResource) -> None:
        self._vectorize = vectorize

    @cached_property
    def indexes(self) -> IndexesResourceWithStreamingResponse:
        return IndexesResourceWithStreamingResponse(self._vectorize.indexes)


class AsyncVectorizeResourceWithStreamingResponse:
    def __init__(self, vectorize: AsyncVectorizeResource) -> None:
        self._vectorize = vectorize

    @cached_property
    def indexes(self) -> AsyncIndexesResourceWithStreamingResponse:
        return AsyncIndexesResourceWithStreamingResponse(self._vectorize.indexes)
