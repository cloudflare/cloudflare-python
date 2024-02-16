# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .statuses import Statuses, AsyncStatuses

from ....._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from .....types import shared_params
from .statuses import (
    Statuses,
    AsyncStatuses,
    StatusesWithRawResponse,
    AsyncStatusesWithRawResponse,
    StatusesWithStreamingResponse,
    AsyncStatusesWithStreamingResponse,
)
from ....._wrappers import ResultWrapper

__all__ = ["BGPs", "AsyncBGPs"]


class BGPs(SyncAPIResource):
    @cached_property
    def statuses(self) -> Statuses:
        return Statuses(self._client)

    @cached_property
    def with_raw_response(self) -> BGPsWithRawResponse:
        return BGPsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BGPsWithStreamingResponse:
        return BGPsWithStreamingResponse(self)


class AsyncBGPs(AsyncAPIResource):
    @cached_property
    def statuses(self) -> AsyncStatuses:
        return AsyncStatuses(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBGPsWithRawResponse:
        return AsyncBGPsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBGPsWithStreamingResponse:
        return AsyncBGPsWithStreamingResponse(self)


class BGPsWithRawResponse:
    def __init__(self, bgps: BGPs) -> None:
        self._bgps = bgps

    @cached_property
    def statuses(self) -> StatusesWithRawResponse:
        return StatusesWithRawResponse(self._bgps.statuses)


class AsyncBGPsWithRawResponse:
    def __init__(self, bgps: AsyncBGPs) -> None:
        self._bgps = bgps

    @cached_property
    def statuses(self) -> AsyncStatusesWithRawResponse:
        return AsyncStatusesWithRawResponse(self._bgps.statuses)


class BGPsWithStreamingResponse:
    def __init__(self, bgps: BGPs) -> None:
        self._bgps = bgps

    @cached_property
    def statuses(self) -> StatusesWithStreamingResponse:
        return StatusesWithStreamingResponse(self._bgps.statuses)


class AsyncBGPsWithStreamingResponse:
    def __init__(self, bgps: AsyncBGPs) -> None:
        self._bgps = bgps

    @cached_property
    def statuses(self) -> AsyncStatusesWithStreamingResponse:
        return AsyncStatusesWithStreamingResponse(self._bgps.statuses)
