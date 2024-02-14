# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .tops.tops import Tops, AsyncTops

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
from .tops import (
    Tops,
    AsyncTops,
    TopsWithRawResponse,
    AsyncTopsWithRawResponse,
    TopsWithStreamingResponse,
    AsyncTopsWithStreamingResponse,
)
from ...._wrappers import ResultWrapper

__all__ = ["VerifiedBots", "AsyncVerifiedBots"]


class VerifiedBots(SyncAPIResource):
    @cached_property
    def tops(self) -> Tops:
        return Tops(self._client)

    @cached_property
    def with_raw_response(self) -> VerifiedBotsWithRawResponse:
        return VerifiedBotsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VerifiedBotsWithStreamingResponse:
        return VerifiedBotsWithStreamingResponse(self)


class AsyncVerifiedBots(AsyncAPIResource):
    @cached_property
    def tops(self) -> AsyncTops:
        return AsyncTops(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVerifiedBotsWithRawResponse:
        return AsyncVerifiedBotsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVerifiedBotsWithStreamingResponse:
        return AsyncVerifiedBotsWithStreamingResponse(self)


class VerifiedBotsWithRawResponse:
    def __init__(self, verified_bots: VerifiedBots) -> None:
        self._verified_bots = verified_bots

    @cached_property
    def tops(self) -> TopsWithRawResponse:
        return TopsWithRawResponse(self._verified_bots.tops)


class AsyncVerifiedBotsWithRawResponse:
    def __init__(self, verified_bots: AsyncVerifiedBots) -> None:
        self._verified_bots = verified_bots

    @cached_property
    def tops(self) -> AsyncTopsWithRawResponse:
        return AsyncTopsWithRawResponse(self._verified_bots.tops)


class VerifiedBotsWithStreamingResponse:
    def __init__(self, verified_bots: VerifiedBots) -> None:
        self._verified_bots = verified_bots

    @cached_property
    def tops(self) -> TopsWithStreamingResponse:
        return TopsWithStreamingResponse(self._verified_bots.tops)


class AsyncVerifiedBotsWithStreamingResponse:
    def __init__(self, verified_bots: AsyncVerifiedBots) -> None:
        self._verified_bots = verified_bots

    @cached_property
    def tops(self) -> AsyncTopsWithStreamingResponse:
        return AsyncTopsWithStreamingResponse(self._verified_bots.tops)
