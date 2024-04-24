# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .sippy import (
    SippyResource,
    AsyncSippyResource,
    SippyResourceWithRawResponse,
    AsyncSippyResourceWithRawResponse,
    SippyResourceWithStreamingResponse,
    AsyncSippyResourceWithStreamingResponse,
)
from .buckets import (
    BucketsResource,
    AsyncBucketsResource,
    BucketsResourceWithRawResponse,
    AsyncBucketsResourceWithRawResponse,
    BucketsResourceWithStreamingResponse,
    AsyncBucketsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["R2Resource", "AsyncR2Resource"]


class R2Resource(SyncAPIResource):
    @cached_property
    def buckets(self) -> BucketsResource:
        return BucketsResource(self._client)

    @cached_property
    def sippy(self) -> SippyResource:
        return SippyResource(self._client)

    @cached_property
    def with_raw_response(self) -> R2ResourceWithRawResponse:
        return R2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> R2ResourceWithStreamingResponse:
        return R2ResourceWithStreamingResponse(self)


class AsyncR2Resource(AsyncAPIResource):
    @cached_property
    def buckets(self) -> AsyncBucketsResource:
        return AsyncBucketsResource(self._client)

    @cached_property
    def sippy(self) -> AsyncSippyResource:
        return AsyncSippyResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncR2ResourceWithRawResponse:
        return AsyncR2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncR2ResourceWithStreamingResponse:
        return AsyncR2ResourceWithStreamingResponse(self)


class R2ResourceWithRawResponse:
    def __init__(self, r2: R2Resource) -> None:
        self._r2 = r2

    @cached_property
    def buckets(self) -> BucketsResourceWithRawResponse:
        return BucketsResourceWithRawResponse(self._r2.buckets)

    @cached_property
    def sippy(self) -> SippyResourceWithRawResponse:
        return SippyResourceWithRawResponse(self._r2.sippy)


class AsyncR2ResourceWithRawResponse:
    def __init__(self, r2: AsyncR2Resource) -> None:
        self._r2 = r2

    @cached_property
    def buckets(self) -> AsyncBucketsResourceWithRawResponse:
        return AsyncBucketsResourceWithRawResponse(self._r2.buckets)

    @cached_property
    def sippy(self) -> AsyncSippyResourceWithRawResponse:
        return AsyncSippyResourceWithRawResponse(self._r2.sippy)


class R2ResourceWithStreamingResponse:
    def __init__(self, r2: R2Resource) -> None:
        self._r2 = r2

    @cached_property
    def buckets(self) -> BucketsResourceWithStreamingResponse:
        return BucketsResourceWithStreamingResponse(self._r2.buckets)

    @cached_property
    def sippy(self) -> SippyResourceWithStreamingResponse:
        return SippyResourceWithStreamingResponse(self._r2.sippy)


class AsyncR2ResourceWithStreamingResponse:
    def __init__(self, r2: AsyncR2Resource) -> None:
        self._r2 = r2

    @cached_property
    def buckets(self) -> AsyncBucketsResourceWithStreamingResponse:
        return AsyncBucketsResourceWithStreamingResponse(self._r2.buckets)

    @cached_property
    def sippy(self) -> AsyncSippyResourceWithStreamingResponse:
        return AsyncSippyResourceWithStreamingResponse(self._r2.sippy)
