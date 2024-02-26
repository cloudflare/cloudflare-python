# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .reports import (
    Reports,
    AsyncReports,
    ReportsWithRawResponse,
    AsyncReportsWithRawResponse,
    ReportsWithStreamingResponse,
    AsyncReportsWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .reports.reports import Reports, AsyncReports

__all__ = ["DNSAnalytics", "AsyncDNSAnalytics"]


class DNSAnalytics(SyncAPIResource):
    @cached_property
    def reports(self) -> Reports:
        return Reports(self._client)

    @cached_property
    def with_raw_response(self) -> DNSAnalyticsWithRawResponse:
        return DNSAnalyticsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DNSAnalyticsWithStreamingResponse:
        return DNSAnalyticsWithStreamingResponse(self)


class AsyncDNSAnalytics(AsyncAPIResource):
    @cached_property
    def reports(self) -> AsyncReports:
        return AsyncReports(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDNSAnalyticsWithRawResponse:
        return AsyncDNSAnalyticsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDNSAnalyticsWithStreamingResponse:
        return AsyncDNSAnalyticsWithStreamingResponse(self)


class DNSAnalyticsWithRawResponse:
    def __init__(self, dns_analytics: DNSAnalytics) -> None:
        self._dns_analytics = dns_analytics

    @cached_property
    def reports(self) -> ReportsWithRawResponse:
        return ReportsWithRawResponse(self._dns_analytics.reports)


class AsyncDNSAnalyticsWithRawResponse:
    def __init__(self, dns_analytics: AsyncDNSAnalytics) -> None:
        self._dns_analytics = dns_analytics

    @cached_property
    def reports(self) -> AsyncReportsWithRawResponse:
        return AsyncReportsWithRawResponse(self._dns_analytics.reports)


class DNSAnalyticsWithStreamingResponse:
    def __init__(self, dns_analytics: DNSAnalytics) -> None:
        self._dns_analytics = dns_analytics

    @cached_property
    def reports(self) -> ReportsWithStreamingResponse:
        return ReportsWithStreamingResponse(self._dns_analytics.reports)


class AsyncDNSAnalyticsWithStreamingResponse:
    def __init__(self, dns_analytics: AsyncDNSAnalytics) -> None:
        self._dns_analytics = dns_analytics

    @cached_property
    def reports(self) -> AsyncReportsWithStreamingResponse:
        return AsyncReportsWithStreamingResponse(self._dns_analytics.reports)
