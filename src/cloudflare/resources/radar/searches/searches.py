# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .globals import Globals, AsyncGlobals

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
from .globals import (
    Globals,
    AsyncGlobals,
    GlobalsWithRawResponse,
    AsyncGlobalsWithRawResponse,
    GlobalsWithStreamingResponse,
    AsyncGlobalsWithStreamingResponse,
)
from ...._wrappers import ResultWrapper

__all__ = ["Searches", "AsyncSearches"]


class Searches(SyncAPIResource):
    @cached_property
    def globals(self) -> Globals:
        return Globals(self._client)

    @cached_property
    def with_raw_response(self) -> SearchesWithRawResponse:
        return SearchesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchesWithStreamingResponse:
        return SearchesWithStreamingResponse(self)


class AsyncSearches(AsyncAPIResource):
    @cached_property
    def globals(self) -> AsyncGlobals:
        return AsyncGlobals(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSearchesWithRawResponse:
        return AsyncSearchesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchesWithStreamingResponse:
        return AsyncSearchesWithStreamingResponse(self)


class SearchesWithRawResponse:
    def __init__(self, searches: Searches) -> None:
        self._searches = searches

    @cached_property
    def globals(self) -> GlobalsWithRawResponse:
        return GlobalsWithRawResponse(self._searches.globals)


class AsyncSearchesWithRawResponse:
    def __init__(self, searches: AsyncSearches) -> None:
        self._searches = searches

    @cached_property
    def globals(self) -> AsyncGlobalsWithRawResponse:
        return AsyncGlobalsWithRawResponse(self._searches.globals)


class SearchesWithStreamingResponse:
    def __init__(self, searches: Searches) -> None:
        self._searches = searches

    @cached_property
    def globals(self) -> GlobalsWithStreamingResponse:
        return GlobalsWithStreamingResponse(self._searches.globals)


class AsyncSearchesWithStreamingResponse:
    def __init__(self, searches: AsyncSearches) -> None:
        self._searches = searches

    @cached_property
    def globals(self) -> AsyncGlobalsWithStreamingResponse:
        return AsyncGlobalsWithStreamingResponse(self._searches.globals)
