# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .top import (
    Top,
    AsyncTop,
    TopWithRawResponse,
    AsyncTopWithRawResponse,
    TopWithStreamingResponse,
    AsyncTopWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["DNS", "AsyncDNS"]


class DNS(SyncAPIResource):
    @cached_property
    def top(self) -> Top:
        return Top(self._client)

    @cached_property
    def with_raw_response(self) -> DNSWithRawResponse:
        return DNSWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DNSWithStreamingResponse:
        return DNSWithStreamingResponse(self)


class AsyncDNS(AsyncAPIResource):
    @cached_property
    def top(self) -> AsyncTop:
        return AsyncTop(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDNSWithRawResponse:
        return AsyncDNSWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDNSWithStreamingResponse:
        return AsyncDNSWithStreamingResponse(self)


class DNSWithRawResponse:
    def __init__(self, dns: DNS) -> None:
        self._dns = dns

    @cached_property
    def top(self) -> TopWithRawResponse:
        return TopWithRawResponse(self._dns.top)


class AsyncDNSWithRawResponse:
    def __init__(self, dns: AsyncDNS) -> None:
        self._dns = dns

    @cached_property
    def top(self) -> AsyncTopWithRawResponse:
        return AsyncTopWithRawResponse(self._dns.top)


class DNSWithStreamingResponse:
    def __init__(self, dns: DNS) -> None:
        self._dns = dns

    @cached_property
    def top(self) -> TopWithStreamingResponse:
        return TopWithStreamingResponse(self._dns.top)


class AsyncDNSWithStreamingResponse:
    def __init__(self, dns: AsyncDNS) -> None:
        self._dns = dns

    @cached_property
    def top(self) -> AsyncTopWithStreamingResponse:
        return AsyncTopWithStreamingResponse(self._dns.top)
