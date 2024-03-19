# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .sippy import (
    Sippy,
    AsyncSippy,
    SippyWithRawResponse,
    AsyncSippyWithRawResponse,
    SippyWithStreamingResponse,
    AsyncSippyWithStreamingResponse,
)
from .buckets import (
    Buckets,
    AsyncBuckets,
    BucketsWithRawResponse,
    AsyncBucketsWithRawResponse,
    BucketsWithStreamingResponse,
    AsyncBucketsWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["R2", "AsyncR2"]


class R2(SyncAPIResource):
    @cached_property
    def buckets(self) -> Buckets:
        return Buckets(self._client)

    @cached_property
    def sippy(self) -> Sippy:
        return Sippy(self._client)

    @cached_property
    def with_raw_response(self) -> R2WithRawResponse:
        return R2WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> R2WithStreamingResponse:
        return R2WithStreamingResponse(self)


class AsyncR2(AsyncAPIResource):
    @cached_property
    def buckets(self) -> AsyncBuckets:
        return AsyncBuckets(self._client)

    @cached_property
    def sippy(self) -> AsyncSippy:
        return AsyncSippy(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncR2WithRawResponse:
        return AsyncR2WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncR2WithStreamingResponse:
        return AsyncR2WithStreamingResponse(self)


class R2WithRawResponse:
    def __init__(self, r2: R2) -> None:
        self._r2 = r2

    @cached_property
    def buckets(self) -> BucketsWithRawResponse:
        return BucketsWithRawResponse(self._r2.buckets)

    @cached_property
    def sippy(self) -> SippyWithRawResponse:
        return SippyWithRawResponse(self._r2.sippy)


class AsyncR2WithRawResponse:
    def __init__(self, r2: AsyncR2) -> None:
        self._r2 = r2

    @cached_property
    def buckets(self) -> AsyncBucketsWithRawResponse:
        return AsyncBucketsWithRawResponse(self._r2.buckets)

    @cached_property
    def sippy(self) -> AsyncSippyWithRawResponse:
        return AsyncSippyWithRawResponse(self._r2.sippy)


class R2WithStreamingResponse:
    def __init__(self, r2: R2) -> None:
        self._r2 = r2

    @cached_property
    def buckets(self) -> BucketsWithStreamingResponse:
        return BucketsWithStreamingResponse(self._r2.buckets)

    @cached_property
    def sippy(self) -> SippyWithStreamingResponse:
        return SippyWithStreamingResponse(self._r2.sippy)


class AsyncR2WithStreamingResponse:
    def __init__(self, r2: AsyncR2) -> None:
        self._r2 = r2

    @cached_property
    def buckets(self) -> AsyncBucketsWithStreamingResponse:
        return AsyncBucketsWithStreamingResponse(self._r2.buckets)

    @cached_property
    def sippy(self) -> AsyncSippyWithStreamingResponse:
        return AsyncSippyWithStreamingResponse(self._r2.sippy)
