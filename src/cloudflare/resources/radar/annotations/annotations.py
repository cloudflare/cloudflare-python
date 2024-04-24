# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .outages import (
    OutagesResource,
    AsyncOutagesResource,
    OutagesResourceWithRawResponse,
    AsyncOutagesResourceWithRawResponse,
    OutagesResourceWithStreamingResponse,
    AsyncOutagesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["AnnotationsResource", "AsyncAnnotationsResource"]


class AnnotationsResource(SyncAPIResource):
    @cached_property
    def outages(self) -> OutagesResource:
        return OutagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AnnotationsResourceWithRawResponse:
        return AnnotationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnnotationsResourceWithStreamingResponse:
        return AnnotationsResourceWithStreamingResponse(self)


class AsyncAnnotationsResource(AsyncAPIResource):
    @cached_property
    def outages(self) -> AsyncOutagesResource:
        return AsyncOutagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAnnotationsResourceWithRawResponse:
        return AsyncAnnotationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnnotationsResourceWithStreamingResponse:
        return AsyncAnnotationsResourceWithStreamingResponse(self)


class AnnotationsResourceWithRawResponse:
    def __init__(self, annotations: AnnotationsResource) -> None:
        self._annotations = annotations

    @cached_property
    def outages(self) -> OutagesResourceWithRawResponse:
        return OutagesResourceWithRawResponse(self._annotations.outages)


class AsyncAnnotationsResourceWithRawResponse:
    def __init__(self, annotations: AsyncAnnotationsResource) -> None:
        self._annotations = annotations

    @cached_property
    def outages(self) -> AsyncOutagesResourceWithRawResponse:
        return AsyncOutagesResourceWithRawResponse(self._annotations.outages)


class AnnotationsResourceWithStreamingResponse:
    def __init__(self, annotations: AnnotationsResource) -> None:
        self._annotations = annotations

    @cached_property
    def outages(self) -> OutagesResourceWithStreamingResponse:
        return OutagesResourceWithStreamingResponse(self._annotations.outages)


class AsyncAnnotationsResourceWithStreamingResponse:
    def __init__(self, annotations: AsyncAnnotationsResource) -> None:
        self._annotations = annotations

    @cached_property
    def outages(self) -> AsyncOutagesResourceWithStreamingResponse:
        return AsyncOutagesResourceWithStreamingResponse(self._annotations.outages)
