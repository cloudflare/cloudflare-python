# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .colo import Colo, AsyncColo

from ..._compat import cached_property

from .dashboards import Dashboards, AsyncDashboards

from .latencies.latencies import Latencies, AsyncLatencies

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from .colo import (
    Colo,
    AsyncColo,
    ColoWithRawResponse,
    AsyncColoWithRawResponse,
    ColoWithStreamingResponse,
    AsyncColoWithStreamingResponse,
)
from .dashboards import (
    Dashboards,
    AsyncDashboards,
    DashboardsWithRawResponse,
    AsyncDashboardsWithRawResponse,
    DashboardsWithStreamingResponse,
    AsyncDashboardsWithStreamingResponse,
)
from .latencies import (
    Latencies,
    AsyncLatencies,
    LatenciesWithRawResponse,
    AsyncLatenciesWithRawResponse,
    LatenciesWithStreamingResponse,
    AsyncLatenciesWithStreamingResponse,
)
from ..._wrappers import ResultWrapper

__all__ = ["Analytics", "AsyncAnalytics"]


class Analytics(SyncAPIResource):
    @cached_property
    def colo(self) -> Colo:
        return Colo(self._client)

    @cached_property
    def dashboards(self) -> Dashboards:
        return Dashboards(self._client)

    @cached_property
    def latencies(self) -> Latencies:
        return Latencies(self._client)

    @cached_property
    def with_raw_response(self) -> AnalyticsWithRawResponse:
        return AnalyticsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalyticsWithStreamingResponse:
        return AnalyticsWithStreamingResponse(self)


class AsyncAnalytics(AsyncAPIResource):
    @cached_property
    def colo(self) -> AsyncColo:
        return AsyncColo(self._client)

    @cached_property
    def dashboards(self) -> AsyncDashboards:
        return AsyncDashboards(self._client)

    @cached_property
    def latencies(self) -> AsyncLatencies:
        return AsyncLatencies(self._client)

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
    def colo(self) -> ColoWithRawResponse:
        return ColoWithRawResponse(self._analytics.colo)

    @cached_property
    def dashboards(self) -> DashboardsWithRawResponse:
        return DashboardsWithRawResponse(self._analytics.dashboards)

    @cached_property
    def latencies(self) -> LatenciesWithRawResponse:
        return LatenciesWithRawResponse(self._analytics.latencies)


class AsyncAnalyticsWithRawResponse:
    def __init__(self, analytics: AsyncAnalytics) -> None:
        self._analytics = analytics

    @cached_property
    def colo(self) -> AsyncColoWithRawResponse:
        return AsyncColoWithRawResponse(self._analytics.colo)

    @cached_property
    def dashboards(self) -> AsyncDashboardsWithRawResponse:
        return AsyncDashboardsWithRawResponse(self._analytics.dashboards)

    @cached_property
    def latencies(self) -> AsyncLatenciesWithRawResponse:
        return AsyncLatenciesWithRawResponse(self._analytics.latencies)


class AnalyticsWithStreamingResponse:
    def __init__(self, analytics: Analytics) -> None:
        self._analytics = analytics

    @cached_property
    def colo(self) -> ColoWithStreamingResponse:
        return ColoWithStreamingResponse(self._analytics.colo)

    @cached_property
    def dashboards(self) -> DashboardsWithStreamingResponse:
        return DashboardsWithStreamingResponse(self._analytics.dashboards)

    @cached_property
    def latencies(self) -> LatenciesWithStreamingResponse:
        return LatenciesWithStreamingResponse(self._analytics.latencies)


class AsyncAnalyticsWithStreamingResponse:
    def __init__(self, analytics: AsyncAnalytics) -> None:
        self._analytics = analytics

    @cached_property
    def colo(self) -> AsyncColoWithStreamingResponse:
        return AsyncColoWithStreamingResponse(self._analytics.colo)

    @cached_property
    def dashboards(self) -> AsyncDashboardsWithStreamingResponse:
        return AsyncDashboardsWithStreamingResponse(self._analytics.dashboards)

    @cached_property
    def latencies(self) -> AsyncLatenciesWithStreamingResponse:
        return AsyncLatenciesWithStreamingResponse(self._analytics.latencies)
