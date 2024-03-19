# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .total_tls import (
    TotalTLS,
    AsyncTotalTLS,
    TotalTLSWithRawResponse,
    AsyncTotalTLSWithRawResponse,
    TotalTLSWithStreamingResponse,
    AsyncTotalTLSWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ACM", "AsyncACM"]


class ACM(SyncAPIResource):
    @cached_property
    def total_tls(self) -> TotalTLS:
        return TotalTLS(self._client)

    @cached_property
    def with_raw_response(self) -> ACMWithRawResponse:
        return ACMWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ACMWithStreamingResponse:
        return ACMWithStreamingResponse(self)


class AsyncACM(AsyncAPIResource):
    @cached_property
    def total_tls(self) -> AsyncTotalTLS:
        return AsyncTotalTLS(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncACMWithRawResponse:
        return AsyncACMWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncACMWithStreamingResponse:
        return AsyncACMWithStreamingResponse(self)


class ACMWithRawResponse:
    def __init__(self, acm: ACM) -> None:
        self._acm = acm

    @cached_property
    def total_tls(self) -> TotalTLSWithRawResponse:
        return TotalTLSWithRawResponse(self._acm.total_tls)


class AsyncACMWithRawResponse:
    def __init__(self, acm: AsyncACM) -> None:
        self._acm = acm

    @cached_property
    def total_tls(self) -> AsyncTotalTLSWithRawResponse:
        return AsyncTotalTLSWithRawResponse(self._acm.total_tls)


class ACMWithStreamingResponse:
    def __init__(self, acm: ACM) -> None:
        self._acm = acm

    @cached_property
    def total_tls(self) -> TotalTLSWithStreamingResponse:
        return TotalTLSWithStreamingResponse(self._acm.total_tls)


class AsyncACMWithStreamingResponse:
    def __init__(self, acm: AsyncACM) -> None:
        self._acm = acm

    @cached_property
    def total_tls(self) -> AsyncTotalTLSWithStreamingResponse:
        return AsyncTotalTLSWithStreamingResponse(self._acm.total_tls)
