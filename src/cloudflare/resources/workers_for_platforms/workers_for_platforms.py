# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .dispatch.dispatch import Dispatch, AsyncDispatch

from ..._compat import cached_property

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
from .dispatch import (
    Dispatch,
    AsyncDispatch,
    DispatchWithRawResponse,
    AsyncDispatchWithRawResponse,
    DispatchWithStreamingResponse,
    AsyncDispatchWithStreamingResponse,
)
from ..._wrappers import ResultWrapper

__all__ = ["WorkersForPlatforms", "AsyncWorkersForPlatforms"]


class WorkersForPlatforms(SyncAPIResource):
    @cached_property
    def dispatch(self) -> Dispatch:
        return Dispatch(self._client)

    @cached_property
    def with_raw_response(self) -> WorkersForPlatformsWithRawResponse:
        return WorkersForPlatformsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkersForPlatformsWithStreamingResponse:
        return WorkersForPlatformsWithStreamingResponse(self)


class AsyncWorkersForPlatforms(AsyncAPIResource):
    @cached_property
    def dispatch(self) -> AsyncDispatch:
        return AsyncDispatch(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWorkersForPlatformsWithRawResponse:
        return AsyncWorkersForPlatformsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkersForPlatformsWithStreamingResponse:
        return AsyncWorkersForPlatformsWithStreamingResponse(self)


class WorkersForPlatformsWithRawResponse:
    def __init__(self, workers_for_platforms: WorkersForPlatforms) -> None:
        self._workers_for_platforms = workers_for_platforms

    @cached_property
    def dispatch(self) -> DispatchWithRawResponse:
        return DispatchWithRawResponse(self._workers_for_platforms.dispatch)


class AsyncWorkersForPlatformsWithRawResponse:
    def __init__(self, workers_for_platforms: AsyncWorkersForPlatforms) -> None:
        self._workers_for_platforms = workers_for_platforms

    @cached_property
    def dispatch(self) -> AsyncDispatchWithRawResponse:
        return AsyncDispatchWithRawResponse(self._workers_for_platforms.dispatch)


class WorkersForPlatformsWithStreamingResponse:
    def __init__(self, workers_for_platforms: WorkersForPlatforms) -> None:
        self._workers_for_platforms = workers_for_platforms

    @cached_property
    def dispatch(self) -> DispatchWithStreamingResponse:
        return DispatchWithStreamingResponse(self._workers_for_platforms.dispatch)


class AsyncWorkersForPlatformsWithStreamingResponse:
    def __init__(self, workers_for_platforms: AsyncWorkersForPlatforms) -> None:
        self._workers_for_platforms = workers_for_platforms

    @cached_property
    def dispatch(self) -> AsyncDispatchWithStreamingResponse:
        return AsyncDispatchWithStreamingResponse(self._workers_for_platforms.dispatch)
