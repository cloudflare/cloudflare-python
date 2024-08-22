# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .reports.reports import ReportsResource, AsyncReportsResource

from ....._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .reports import ReportsResource, AsyncReportsResource, ReportsResourceWithRawResponse, AsyncReportsResourceWithRawResponse, ReportsResourceWithStreamingResponse, AsyncReportsResourceWithStreamingResponse

__all__ = ["AnalyticsResource", "AsyncAnalyticsResource"]

class AnalyticsResource(SyncAPIResource):
    @cached_property
    def reports(self) -> ReportsResource:
        return ReportsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AnalyticsResourceWithRawResponse:
        return AnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalyticsResourceWithStreamingResponse:
        return AnalyticsResourceWithStreamingResponse(self)

class AsyncAnalyticsResource(AsyncAPIResource):
    @cached_property
    def reports(self) -> AsyncReportsResource:
        return AsyncReportsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAnalyticsResourceWithRawResponse:
        return AsyncAnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalyticsResourceWithStreamingResponse:
        return AsyncAnalyticsResourceWithStreamingResponse(self)

class AnalyticsResourceWithRawResponse:
    def __init__(self, analytics: AnalyticsResource) -> None:
        self._analytics = analytics

    @cached_property
    def reports(self) -> ReportsResourceWithRawResponse:
        return ReportsResourceWithRawResponse(self._analytics.reports)

class AsyncAnalyticsResourceWithRawResponse:
    def __init__(self, analytics: AsyncAnalyticsResource) -> None:
        self._analytics = analytics

    @cached_property
    def reports(self) -> AsyncReportsResourceWithRawResponse:
        return AsyncReportsResourceWithRawResponse(self._analytics.reports)

class AnalyticsResourceWithStreamingResponse:
    def __init__(self, analytics: AnalyticsResource) -> None:
        self._analytics = analytics

    @cached_property
    def reports(self) -> ReportsResourceWithStreamingResponse:
        return ReportsResourceWithStreamingResponse(self._analytics.reports)

class AsyncAnalyticsResourceWithStreamingResponse:
    def __init__(self, analytics: AsyncAnalyticsResource) -> None:
        self._analytics = analytics

    @cached_property
    def reports(self) -> AsyncReportsResourceWithStreamingResponse:
        return AsyncReportsResourceWithStreamingResponse(self._analytics.reports)