# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .summary import SummaryResource, AsyncSummaryResource

from ....._compat import cached_property

from .timeseries_groups import TimeseriesGroupsResource, AsyncTimeseriesGroupsResource

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .summary import SummaryResource, AsyncSummaryResource, SummaryResourceWithRawResponse, AsyncSummaryResourceWithRawResponse, SummaryResourceWithStreamingResponse, AsyncSummaryResourceWithStreamingResponse
from .timeseries_groups import TimeseriesGroupsResource, AsyncTimeseriesGroupsResource, TimeseriesGroupsResourceWithRawResponse, AsyncTimeseriesGroupsResourceWithRawResponse, TimeseriesGroupsResourceWithStreamingResponse, AsyncTimeseriesGroupsResourceWithStreamingResponse

__all__ = ["RoutingResource", "AsyncRoutingResource"]

class RoutingResource(SyncAPIResource):
    @cached_property
    def summary(self) -> SummaryResource:
        return SummaryResource(self._client)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResource:
        return TimeseriesGroupsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RoutingResourceWithRawResponse:
        return RoutingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoutingResourceWithStreamingResponse:
        return RoutingResourceWithStreamingResponse(self)

class AsyncRoutingResource(AsyncAPIResource):
    @cached_property
    def summary(self) -> AsyncSummaryResource:
        return AsyncSummaryResource(self._client)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResource:
        return AsyncTimeseriesGroupsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRoutingResourceWithRawResponse:
        return AsyncRoutingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoutingResourceWithStreamingResponse:
        return AsyncRoutingResourceWithStreamingResponse(self)

class RoutingResourceWithRawResponse:
    def __init__(self, routing: RoutingResource) -> None:
        self._routing = routing

    @cached_property
    def summary(self) -> SummaryResourceWithRawResponse:
        return SummaryResourceWithRawResponse(self._routing.summary)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResourceWithRawResponse:
        return TimeseriesGroupsResourceWithRawResponse(self._routing.timeseries_groups)

class AsyncRoutingResourceWithRawResponse:
    def __init__(self, routing: AsyncRoutingResource) -> None:
        self._routing = routing

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithRawResponse:
        return AsyncSummaryResourceWithRawResponse(self._routing.summary)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResourceWithRawResponse:
        return AsyncTimeseriesGroupsResourceWithRawResponse(self._routing.timeseries_groups)

class RoutingResourceWithStreamingResponse:
    def __init__(self, routing: RoutingResource) -> None:
        self._routing = routing

    @cached_property
    def summary(self) -> SummaryResourceWithStreamingResponse:
        return SummaryResourceWithStreamingResponse(self._routing.summary)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResourceWithStreamingResponse:
        return TimeseriesGroupsResourceWithStreamingResponse(self._routing.timeseries_groups)

class AsyncRoutingResourceWithStreamingResponse:
    def __init__(self, routing: AsyncRoutingResource) -> None:
        self._routing = routing

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithStreamingResponse:
        return AsyncSummaryResourceWithStreamingResponse(self._routing.summary)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResourceWithStreamingResponse:
        return AsyncTimeseriesGroupsResourceWithStreamingResponse(self._routing.timeseries_groups)