# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .timeseries import Timeseries, AsyncTimeseries

from ...._compat import cached_property

from .tops.tops import Tops, AsyncTops

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from .timeseries import (
    Timeseries,
    AsyncTimeseries,
    TimeseriesWithRawResponse,
    AsyncTimeseriesWithRawResponse,
    TimeseriesWithStreamingResponse,
    AsyncTimeseriesWithStreamingResponse,
)
from .tops import (
    Tops,
    AsyncTops,
    TopsWithRawResponse,
    AsyncTopsWithRawResponse,
    TopsWithStreamingResponse,
    AsyncTopsWithStreamingResponse,
)
from ...._wrappers import ResultWrapper

__all__ = ["Netflows", "AsyncNetflows"]


class Netflows(SyncAPIResource):
    @cached_property
    def timeseries(self) -> Timeseries:
        return Timeseries(self._client)

    @cached_property
    def tops(self) -> Tops:
        return Tops(self._client)

    @cached_property
    def with_raw_response(self) -> NetflowsWithRawResponse:
        return NetflowsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NetflowsWithStreamingResponse:
        return NetflowsWithStreamingResponse(self)


class AsyncNetflows(AsyncAPIResource):
    @cached_property
    def timeseries(self) -> AsyncTimeseries:
        return AsyncTimeseries(self._client)

    @cached_property
    def tops(self) -> AsyncTops:
        return AsyncTops(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNetflowsWithRawResponse:
        return AsyncNetflowsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNetflowsWithStreamingResponse:
        return AsyncNetflowsWithStreamingResponse(self)


class NetflowsWithRawResponse:
    def __init__(self, netflows: Netflows) -> None:
        self._netflows = netflows

    @cached_property
    def timeseries(self) -> TimeseriesWithRawResponse:
        return TimeseriesWithRawResponse(self._netflows.timeseries)

    @cached_property
    def tops(self) -> TopsWithRawResponse:
        return TopsWithRawResponse(self._netflows.tops)


class AsyncNetflowsWithRawResponse:
    def __init__(self, netflows: AsyncNetflows) -> None:
        self._netflows = netflows

    @cached_property
    def timeseries(self) -> AsyncTimeseriesWithRawResponse:
        return AsyncTimeseriesWithRawResponse(self._netflows.timeseries)

    @cached_property
    def tops(self) -> AsyncTopsWithRawResponse:
        return AsyncTopsWithRawResponse(self._netflows.tops)


class NetflowsWithStreamingResponse:
    def __init__(self, netflows: Netflows) -> None:
        self._netflows = netflows

    @cached_property
    def timeseries(self) -> TimeseriesWithStreamingResponse:
        return TimeseriesWithStreamingResponse(self._netflows.timeseries)

    @cached_property
    def tops(self) -> TopsWithStreamingResponse:
        return TopsWithStreamingResponse(self._netflows.tops)


class AsyncNetflowsWithStreamingResponse:
    def __init__(self, netflows: AsyncNetflows) -> None:
        self._netflows = netflows

    @cached_property
    def timeseries(self) -> AsyncTimeseriesWithStreamingResponse:
        return AsyncTimeseriesWithStreamingResponse(self._netflows.timeseries)

    @cached_property
    def tops(self) -> AsyncTopsWithStreamingResponse:
        return AsyncTopsWithStreamingResponse(self._netflows.tops)
