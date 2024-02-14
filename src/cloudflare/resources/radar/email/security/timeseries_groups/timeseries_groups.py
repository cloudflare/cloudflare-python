# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .arcs import Arcs, AsyncArcs

from ......_compat import cached_property

from .dkims import DKIMs, AsyncDKIMs

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ......_utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ......_types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ......types import shared_params
from .arcs import (
    Arcs,
    AsyncArcs,
    ArcsWithRawResponse,
    AsyncArcsWithRawResponse,
    ArcsWithStreamingResponse,
    AsyncArcsWithStreamingResponse,
)
from .dkims import (
    DKIMs,
    AsyncDKIMs,
    DKIMsWithRawResponse,
    AsyncDKIMsWithRawResponse,
    DKIMsWithStreamingResponse,
    AsyncDKIMsWithStreamingResponse,
)
from ......_wrappers import ResultWrapper

__all__ = ["TimeseriesGroups", "AsyncTimeseriesGroups"]


class TimeseriesGroups(SyncAPIResource):
    @cached_property
    def arcs(self) -> Arcs:
        return Arcs(self._client)

    @cached_property
    def dkims(self) -> DKIMs:
        return DKIMs(self._client)

    @cached_property
    def with_raw_response(self) -> TimeseriesGroupsWithRawResponse:
        return TimeseriesGroupsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TimeseriesGroupsWithStreamingResponse:
        return TimeseriesGroupsWithStreamingResponse(self)


class AsyncTimeseriesGroups(AsyncAPIResource):
    @cached_property
    def arcs(self) -> AsyncArcs:
        return AsyncArcs(self._client)

    @cached_property
    def dkims(self) -> AsyncDKIMs:
        return AsyncDKIMs(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTimeseriesGroupsWithRawResponse:
        return AsyncTimeseriesGroupsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTimeseriesGroupsWithStreamingResponse:
        return AsyncTimeseriesGroupsWithStreamingResponse(self)


class TimeseriesGroupsWithRawResponse:
    def __init__(self, timeseries_groups: TimeseriesGroups) -> None:
        self._timeseries_groups = timeseries_groups

    @cached_property
    def arcs(self) -> ArcsWithRawResponse:
        return ArcsWithRawResponse(self._timeseries_groups.arcs)

    @cached_property
    def dkims(self) -> DKIMsWithRawResponse:
        return DKIMsWithRawResponse(self._timeseries_groups.dkims)


class AsyncTimeseriesGroupsWithRawResponse:
    def __init__(self, timeseries_groups: AsyncTimeseriesGroups) -> None:
        self._timeseries_groups = timeseries_groups

    @cached_property
    def arcs(self) -> AsyncArcsWithRawResponse:
        return AsyncArcsWithRawResponse(self._timeseries_groups.arcs)

    @cached_property
    def dkims(self) -> AsyncDKIMsWithRawResponse:
        return AsyncDKIMsWithRawResponse(self._timeseries_groups.dkims)


class TimeseriesGroupsWithStreamingResponse:
    def __init__(self, timeseries_groups: TimeseriesGroups) -> None:
        self._timeseries_groups = timeseries_groups

    @cached_property
    def arcs(self) -> ArcsWithStreamingResponse:
        return ArcsWithStreamingResponse(self._timeseries_groups.arcs)

    @cached_property
    def dkims(self) -> DKIMsWithStreamingResponse:
        return DKIMsWithStreamingResponse(self._timeseries_groups.dkims)


class AsyncTimeseriesGroupsWithStreamingResponse:
    def __init__(self, timeseries_groups: AsyncTimeseriesGroups) -> None:
        self._timeseries_groups = timeseries_groups

    @cached_property
    def arcs(self) -> AsyncArcsWithStreamingResponse:
        return AsyncArcsWithStreamingResponse(self._timeseries_groups.arcs)

    @cached_property
    def dkims(self) -> AsyncDKIMsWithStreamingResponse:
        return AsyncDKIMsWithStreamingResponse(self._timeseries_groups.dkims)
