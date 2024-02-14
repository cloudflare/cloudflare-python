# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .validates import Validates, AsyncValidates

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
from .validates import (
    Validates,
    AsyncValidates,
    ValidatesWithRawResponse,
    AsyncValidatesWithRawResponse,
    ValidatesWithStreamingResponse,
    AsyncValidatesWithStreamingResponse,
)
from ...._wrappers import ResultWrapper

__all__ = ["Patterns", "AsyncPatterns"]


class Patterns(SyncAPIResource):
    @cached_property
    def validates(self) -> Validates:
        return Validates(self._client)

    @cached_property
    def with_raw_response(self) -> PatternsWithRawResponse:
        return PatternsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PatternsWithStreamingResponse:
        return PatternsWithStreamingResponse(self)


class AsyncPatterns(AsyncAPIResource):
    @cached_property
    def validates(self) -> AsyncValidates:
        return AsyncValidates(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPatternsWithRawResponse:
        return AsyncPatternsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPatternsWithStreamingResponse:
        return AsyncPatternsWithStreamingResponse(self)


class PatternsWithRawResponse:
    def __init__(self, patterns: Patterns) -> None:
        self._patterns = patterns

    @cached_property
    def validates(self) -> ValidatesWithRawResponse:
        return ValidatesWithRawResponse(self._patterns.validates)


class AsyncPatternsWithRawResponse:
    def __init__(self, patterns: AsyncPatterns) -> None:
        self._patterns = patterns

    @cached_property
    def validates(self) -> AsyncValidatesWithRawResponse:
        return AsyncValidatesWithRawResponse(self._patterns.validates)


class PatternsWithStreamingResponse:
    def __init__(self, patterns: Patterns) -> None:
        self._patterns = patterns

    @cached_property
    def validates(self) -> ValidatesWithStreamingResponse:
        return ValidatesWithStreamingResponse(self._patterns.validates)


class AsyncPatternsWithStreamingResponse:
    def __init__(self, patterns: AsyncPatterns) -> None:
        self._patterns = patterns

    @cached_property
    def validates(self) -> AsyncValidatesWithStreamingResponse:
        return AsyncValidatesWithStreamingResponse(self._patterns.validates)
