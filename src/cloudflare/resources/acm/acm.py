# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .total_tls import (
    TotalTLSResource,
    AsyncTotalTLSResource,
    TotalTLSResourceWithRawResponse,
    AsyncTotalTLSResourceWithRawResponse,
    TotalTLSResourceWithStreamingResponse,
    AsyncTotalTLSResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ACMResource", "AsyncACMResource"]


class ACMResource(SyncAPIResource):
    @cached_property
    def total_tls(self) -> TotalTLSResource:
        return TotalTLSResource(self._client)

    @cached_property
    def with_raw_response(self) -> ACMResourceWithRawResponse:
        return ACMResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ACMResourceWithStreamingResponse:
        return ACMResourceWithStreamingResponse(self)


class AsyncACMResource(AsyncAPIResource):
    @cached_property
    def total_tls(self) -> AsyncTotalTLSResource:
        return AsyncTotalTLSResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncACMResourceWithRawResponse:
        return AsyncACMResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncACMResourceWithStreamingResponse:
        return AsyncACMResourceWithStreamingResponse(self)


class ACMResourceWithRawResponse:
    def __init__(self, acm: ACMResource) -> None:
        self._acm = acm

    @cached_property
    def total_tls(self) -> TotalTLSResourceWithRawResponse:
        return TotalTLSResourceWithRawResponse(self._acm.total_tls)


class AsyncACMResourceWithRawResponse:
    def __init__(self, acm: AsyncACMResource) -> None:
        self._acm = acm

    @cached_property
    def total_tls(self) -> AsyncTotalTLSResourceWithRawResponse:
        return AsyncTotalTLSResourceWithRawResponse(self._acm.total_tls)


class ACMResourceWithStreamingResponse:
    def __init__(self, acm: ACMResource) -> None:
        self._acm = acm

    @cached_property
    def total_tls(self) -> TotalTLSResourceWithStreamingResponse:
        return TotalTLSResourceWithStreamingResponse(self._acm.total_tls)


class AsyncACMResourceWithStreamingResponse:
    def __init__(self, acm: AsyncACMResource) -> None:
        self._acm = acm

    @cached_property
    def total_tls(self) -> AsyncTotalTLSResourceWithStreamingResponse:
        return AsyncTotalTLSResourceWithStreamingResponse(self._acm.total_tls)
