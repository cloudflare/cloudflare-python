# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .indexes import (
    Indexes,
    AsyncIndexes,
    IndexesWithRawResponse,
    AsyncIndexesWithRawResponse,
    IndexesWithStreamingResponse,
    AsyncIndexesWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Vectorize", "AsyncVectorize"]


class Vectorize(SyncAPIResource):
    @cached_property
    def indexes(self) -> Indexes:
        return Indexes(self._client)

    @cached_property
    def with_raw_response(self) -> VectorizeWithRawResponse:
        return VectorizeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VectorizeWithStreamingResponse:
        return VectorizeWithStreamingResponse(self)


class AsyncVectorize(AsyncAPIResource):
    @cached_property
    def indexes(self) -> AsyncIndexes:
        return AsyncIndexes(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVectorizeWithRawResponse:
        return AsyncVectorizeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVectorizeWithStreamingResponse:
        return AsyncVectorizeWithStreamingResponse(self)


class VectorizeWithRawResponse:
    def __init__(self, vectorize: Vectorize) -> None:
        self._vectorize = vectorize

    @cached_property
    def indexes(self) -> IndexesWithRawResponse:
        return IndexesWithRawResponse(self._vectorize.indexes)


class AsyncVectorizeWithRawResponse:
    def __init__(self, vectorize: AsyncVectorize) -> None:
        self._vectorize = vectorize

    @cached_property
    def indexes(self) -> AsyncIndexesWithRawResponse:
        return AsyncIndexesWithRawResponse(self._vectorize.indexes)


class VectorizeWithStreamingResponse:
    def __init__(self, vectorize: Vectorize) -> None:
        self._vectorize = vectorize

    @cached_property
    def indexes(self) -> IndexesWithStreamingResponse:
        return IndexesWithStreamingResponse(self._vectorize.indexes)


class AsyncVectorizeWithStreamingResponse:
    def __init__(self, vectorize: AsyncVectorize) -> None:
        self._vectorize = vectorize

    @cached_property
    def indexes(self) -> AsyncIndexesWithStreamingResponse:
        return AsyncIndexesWithStreamingResponse(self._vectorize.indexes)
