# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .flags import Flags, AsyncFlags

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
from .flags import (
    Flags,
    AsyncFlags,
    FlagsWithRawResponse,
    AsyncFlagsWithRawResponse,
    FlagsWithStreamingResponse,
    AsyncFlagsWithStreamingResponse,
)
from ....._wrappers import ResultWrapper

__all__ = ["Retentions", "AsyncRetentions"]


class Retentions(SyncAPIResource):
    @cached_property
    def flags(self) -> Flags:
        return Flags(self._client)

    @cached_property
    def with_raw_response(self) -> RetentionsWithRawResponse:
        return RetentionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RetentionsWithStreamingResponse:
        return RetentionsWithStreamingResponse(self)


class AsyncRetentions(AsyncAPIResource):
    @cached_property
    def flags(self) -> AsyncFlags:
        return AsyncFlags(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRetentionsWithRawResponse:
        return AsyncRetentionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRetentionsWithStreamingResponse:
        return AsyncRetentionsWithStreamingResponse(self)


class RetentionsWithRawResponse:
    def __init__(self, retentions: Retentions) -> None:
        self._retentions = retentions

    @cached_property
    def flags(self) -> FlagsWithRawResponse:
        return FlagsWithRawResponse(self._retentions.flags)


class AsyncRetentionsWithRawResponse:
    def __init__(self, retentions: AsyncRetentions) -> None:
        self._retentions = retentions

    @cached_property
    def flags(self) -> AsyncFlagsWithRawResponse:
        return AsyncFlagsWithRawResponse(self._retentions.flags)


class RetentionsWithStreamingResponse:
    def __init__(self, retentions: Retentions) -> None:
        self._retentions = retentions

    @cached_property
    def flags(self) -> FlagsWithStreamingResponse:
        return FlagsWithStreamingResponse(self._retentions.flags)


class AsyncRetentionsWithStreamingResponse:
    def __init__(self, retentions: AsyncRetentions) -> None:
        self._retentions = retentions

    @cached_property
    def flags(self) -> AsyncFlagsWithStreamingResponse:
        return AsyncFlagsWithStreamingResponse(self._retentions.flags)
