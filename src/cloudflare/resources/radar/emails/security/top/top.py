# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .ases.ases import Ases, AsyncAses

from ......_compat import cached_property

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
from .ases import (
    Ases,
    AsyncAses,
    AsesWithRawResponse,
    AsyncAsesWithRawResponse,
    AsesWithStreamingResponse,
    AsyncAsesWithStreamingResponse,
)
from ......_wrappers import ResultWrapper

__all__ = ["Top", "AsyncTop"]


class Top(SyncAPIResource):
    @cached_property
    def ases(self) -> Ases:
        return Ases(self._client)

    @cached_property
    def with_raw_response(self) -> TopWithRawResponse:
        return TopWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TopWithStreamingResponse:
        return TopWithStreamingResponse(self)


class AsyncTop(AsyncAPIResource):
    @cached_property
    def ases(self) -> AsyncAses:
        return AsyncAses(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTopWithRawResponse:
        return AsyncTopWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTopWithStreamingResponse:
        return AsyncTopWithStreamingResponse(self)


class TopWithRawResponse:
    def __init__(self, top: Top) -> None:
        self._top = top

    @cached_property
    def ases(self) -> AsesWithRawResponse:
        return AsesWithRawResponse(self._top.ases)


class AsyncTopWithRawResponse:
    def __init__(self, top: AsyncTop) -> None:
        self._top = top

    @cached_property
    def ases(self) -> AsyncAsesWithRawResponse:
        return AsyncAsesWithRawResponse(self._top.ases)


class TopWithStreamingResponse:
    def __init__(self, top: Top) -> None:
        self._top = top

    @cached_property
    def ases(self) -> AsesWithStreamingResponse:
        return AsesWithStreamingResponse(self._top.ases)


class AsyncTopWithStreamingResponse:
    def __init__(self, top: AsyncTop) -> None:
        self._top = top

    @cached_property
    def ases(self) -> AsyncAsesWithStreamingResponse:
        return AsyncAsesWithStreamingResponse(self._top.ases)
