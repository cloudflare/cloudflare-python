# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .bgp_prefixes import BGPPrefixes, AsyncBGPPrefixes

from ...._compat import cached_property

from .bindings import Bindings, AsyncBindings

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
from .bgp_prefixes import (
    BGPPrefixes,
    AsyncBGPPrefixes,
    BGPPrefixesWithRawResponse,
    AsyncBGPPrefixesWithRawResponse,
    BGPPrefixesWithStreamingResponse,
    AsyncBGPPrefixesWithStreamingResponse,
)
from .bindings import (
    Bindings,
    AsyncBindings,
    BindingsWithRawResponse,
    AsyncBindingsWithRawResponse,
    BindingsWithStreamingResponse,
    AsyncBindingsWithStreamingResponse,
)
from ...._wrappers import ResultWrapper

__all__ = ["Prefixes", "AsyncPrefixes"]


class Prefixes(SyncAPIResource):
    @cached_property
    def bgp_prefixes(self) -> BGPPrefixes:
        return BGPPrefixes(self._client)

    @cached_property
    def bindings(self) -> Bindings:
        return Bindings(self._client)

    @cached_property
    def with_raw_response(self) -> PrefixesWithRawResponse:
        return PrefixesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrefixesWithStreamingResponse:
        return PrefixesWithStreamingResponse(self)


class AsyncPrefixes(AsyncAPIResource):
    @cached_property
    def bgp_prefixes(self) -> AsyncBGPPrefixes:
        return AsyncBGPPrefixes(self._client)

    @cached_property
    def bindings(self) -> AsyncBindings:
        return AsyncBindings(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPrefixesWithRawResponse:
        return AsyncPrefixesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrefixesWithStreamingResponse:
        return AsyncPrefixesWithStreamingResponse(self)


class PrefixesWithRawResponse:
    def __init__(self, prefixes: Prefixes) -> None:
        self._prefixes = prefixes

    @cached_property
    def bgp_prefixes(self) -> BGPPrefixesWithRawResponse:
        return BGPPrefixesWithRawResponse(self._prefixes.bgp_prefixes)

    @cached_property
    def bindings(self) -> BindingsWithRawResponse:
        return BindingsWithRawResponse(self._prefixes.bindings)


class AsyncPrefixesWithRawResponse:
    def __init__(self, prefixes: AsyncPrefixes) -> None:
        self._prefixes = prefixes

    @cached_property
    def bgp_prefixes(self) -> AsyncBGPPrefixesWithRawResponse:
        return AsyncBGPPrefixesWithRawResponse(self._prefixes.bgp_prefixes)

    @cached_property
    def bindings(self) -> AsyncBindingsWithRawResponse:
        return AsyncBindingsWithRawResponse(self._prefixes.bindings)


class PrefixesWithStreamingResponse:
    def __init__(self, prefixes: Prefixes) -> None:
        self._prefixes = prefixes

    @cached_property
    def bgp_prefixes(self) -> BGPPrefixesWithStreamingResponse:
        return BGPPrefixesWithStreamingResponse(self._prefixes.bgp_prefixes)

    @cached_property
    def bindings(self) -> BindingsWithStreamingResponse:
        return BindingsWithStreamingResponse(self._prefixes.bindings)


class AsyncPrefixesWithStreamingResponse:
    def __init__(self, prefixes: AsyncPrefixes) -> None:
        self._prefixes = prefixes

    @cached_property
    def bgp_prefixes(self) -> AsyncBGPPrefixesWithStreamingResponse:
        return AsyncBGPPrefixesWithStreamingResponse(self._prefixes.bgp_prefixes)

    @cached_property
    def bindings(self) -> AsyncBindingsWithStreamingResponse:
        return AsyncBindingsWithStreamingResponse(self._prefixes.bindings)
