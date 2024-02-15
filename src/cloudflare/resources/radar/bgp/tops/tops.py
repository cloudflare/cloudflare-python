# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .ases import Ases, AsyncAses

from ....._compat import cached_property

from .prefixes import Prefixes, AsyncPrefixes

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
from .ases import (
    Ases,
    AsyncAses,
    AsesWithRawResponse,
    AsyncAsesWithRawResponse,
    AsesWithStreamingResponse,
    AsyncAsesWithStreamingResponse,
)
from .prefixes import (
    Prefixes,
    AsyncPrefixes,
    PrefixesWithRawResponse,
    AsyncPrefixesWithRawResponse,
    PrefixesWithStreamingResponse,
    AsyncPrefixesWithStreamingResponse,
)
from ....._wrappers import ResultWrapper

__all__ = ["Tops", "AsyncTops"]


class Tops(SyncAPIResource):
    @cached_property
    def ases(self) -> Ases:
        return Ases(self._client)

    @cached_property
    def prefixes(self) -> Prefixes:
        return Prefixes(self._client)

    @cached_property
    def with_raw_response(self) -> TopsWithRawResponse:
        return TopsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TopsWithStreamingResponse:
        return TopsWithStreamingResponse(self)


class AsyncTops(AsyncAPIResource):
    @cached_property
    def ases(self) -> AsyncAses:
        return AsyncAses(self._client)

    @cached_property
    def prefixes(self) -> AsyncPrefixes:
        return AsyncPrefixes(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTopsWithRawResponse:
        return AsyncTopsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTopsWithStreamingResponse:
        return AsyncTopsWithStreamingResponse(self)


class TopsWithRawResponse:
    def __init__(self, tops: Tops) -> None:
        self._tops = tops

    @cached_property
    def ases(self) -> AsesWithRawResponse:
        return AsesWithRawResponse(self._tops.ases)

    @cached_property
    def prefixes(self) -> PrefixesWithRawResponse:
        return PrefixesWithRawResponse(self._tops.prefixes)


class AsyncTopsWithRawResponse:
    def __init__(self, tops: AsyncTops) -> None:
        self._tops = tops

    @cached_property
    def ases(self) -> AsyncAsesWithRawResponse:
        return AsyncAsesWithRawResponse(self._tops.ases)

    @cached_property
    def prefixes(self) -> AsyncPrefixesWithRawResponse:
        return AsyncPrefixesWithRawResponse(self._tops.prefixes)


class TopsWithStreamingResponse:
    def __init__(self, tops: Tops) -> None:
        self._tops = tops

    @cached_property
    def ases(self) -> AsesWithStreamingResponse:
        return AsesWithStreamingResponse(self._tops.ases)

    @cached_property
    def prefixes(self) -> PrefixesWithStreamingResponse:
        return PrefixesWithStreamingResponse(self._tops.prefixes)


class AsyncTopsWithStreamingResponse:
    def __init__(self, tops: AsyncTops) -> None:
        self._tops = tops

    @cached_property
    def ases(self) -> AsyncAsesWithStreamingResponse:
        return AsyncAsesWithStreamingResponse(self._tops.ases)

    @cached_property
    def prefixes(self) -> AsyncPrefixesWithStreamingResponse:
        return AsyncPrefixesWithStreamingResponse(self._tops.prefixes)
