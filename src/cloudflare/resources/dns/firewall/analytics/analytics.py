# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .reports import (
    Reports,
    AsyncReports,
    ReportsWithRawResponse,
    AsyncReportsWithRawResponse,
    ReportsWithStreamingResponse,
    AsyncReportsWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from .reports.reports import Reports, AsyncReports

__all__ = ["Analytics", "AsyncAnalytics"]


class Analytics(SyncAPIResource):
    @cached_property
    def reports(self) -> Reports:
        return Reports(self._client)

    @cached_property
    def with_raw_response(self) -> AnalyticsWithRawResponse:
        return AnalyticsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalyticsWithStreamingResponse:
        return AnalyticsWithStreamingResponse(self)


class AsyncAnalytics(AsyncAPIResource):
    @cached_property
    def reports(self) -> AsyncReports:
        return AsyncReports(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAnalyticsWithRawResponse:
        return AsyncAnalyticsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalyticsWithStreamingResponse:
        return AsyncAnalyticsWithStreamingResponse(self)


class AnalyticsWithRawResponse:
    def __init__(self, analytics: Analytics) -> None:
        self._analytics = analytics

    @cached_property
    def reports(self) -> ReportsWithRawResponse:
        return ReportsWithRawResponse(self._analytics.reports)


class AsyncAnalyticsWithRawResponse:
    def __init__(self, analytics: AsyncAnalytics) -> None:
        self._analytics = analytics

    @cached_property
    def reports(self) -> AsyncReportsWithRawResponse:
        return AsyncReportsWithRawResponse(self._analytics.reports)


class AnalyticsWithStreamingResponse:
    def __init__(self, analytics: Analytics) -> None:
        self._analytics = analytics

    @cached_property
    def reports(self) -> ReportsWithStreamingResponse:
        return ReportsWithStreamingResponse(self._analytics.reports)


class AsyncAnalyticsWithStreamingResponse:
    def __init__(self, analytics: AsyncAnalytics) -> None:
        self._analytics = analytics

    @cached_property
    def reports(self) -> AsyncReportsWithStreamingResponse:
        return AsyncReportsWithStreamingResponse(self._analytics.reports)
