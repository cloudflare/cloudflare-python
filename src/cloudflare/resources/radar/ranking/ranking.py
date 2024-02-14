# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .timeseries_groups import TimeseriesGroups, AsyncTimeseriesGroups

from ...._compat import cached_property

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
from .timeseries_groups import (
    TimeseriesGroups,
    AsyncTimeseriesGroups,
    TimeseriesGroupsWithRawResponse,
    AsyncTimeseriesGroupsWithRawResponse,
    TimeseriesGroupsWithStreamingResponse,
    AsyncTimeseriesGroupsWithStreamingResponse,
)
from ...._wrappers import ResultWrapper

__all__ = ["Ranking", "AsyncRanking"]


class Ranking(SyncAPIResource):
    @cached_property
    def timeseries_groups(self) -> TimeseriesGroups:
        return TimeseriesGroups(self._client)

    @cached_property
    def with_raw_response(self) -> RankingWithRawResponse:
        return RankingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RankingWithStreamingResponse:
        return RankingWithStreamingResponse(self)


class AsyncRanking(AsyncAPIResource):
    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroups:
        return AsyncTimeseriesGroups(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRankingWithRawResponse:
        return AsyncRankingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRankingWithStreamingResponse:
        return AsyncRankingWithStreamingResponse(self)


class RankingWithRawResponse:
    def __init__(self, ranking: Ranking) -> None:
        self._ranking = ranking

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsWithRawResponse:
        return TimeseriesGroupsWithRawResponse(self._ranking.timeseries_groups)


class AsyncRankingWithRawResponse:
    def __init__(self, ranking: AsyncRanking) -> None:
        self._ranking = ranking

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsWithRawResponse:
        return AsyncTimeseriesGroupsWithRawResponse(self._ranking.timeseries_groups)


class RankingWithStreamingResponse:
    def __init__(self, ranking: Ranking) -> None:
        self._ranking = ranking

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsWithStreamingResponse:
        return TimeseriesGroupsWithStreamingResponse(self._ranking.timeseries_groups)


class AsyncRankingWithStreamingResponse:
    def __init__(self, ranking: AsyncRanking) -> None:
        self._ranking = ranking

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsWithStreamingResponse:
        return AsyncTimeseriesGroupsWithStreamingResponse(self._ranking.timeseries_groups)
