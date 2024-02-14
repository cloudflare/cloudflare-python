# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .buckets import Buckets, AsyncBuckets

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
from .buckets import (
    Buckets,
    AsyncBuckets,
    BucketsWithRawResponse,
    AsyncBucketsWithRawResponse,
    BucketsWithStreamingResponse,
    AsyncBucketsWithStreamingResponse,
)
from ..._wrappers import ResultWrapper

__all__ = ["R2", "AsyncR2"]


class R2(SyncAPIResource):
    @cached_property
    def buckets(self) -> Buckets:
        return Buckets(self._client)

    @cached_property
    def with_raw_response(self) -> R2WithRawResponse:
        return R2WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> R2WithStreamingResponse:
        return R2WithStreamingResponse(self)


class AsyncR2(AsyncAPIResource):
    @cached_property
    def buckets(self) -> AsyncBuckets:
        return AsyncBuckets(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncR2WithRawResponse:
        return AsyncR2WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncR2WithStreamingResponse:
        return AsyncR2WithStreamingResponse(self)


class R2WithRawResponse:
    def __init__(self, r2: R2) -> None:
        self._r2 = r2

    @cached_property
    def buckets(self) -> BucketsWithRawResponse:
        return BucketsWithRawResponse(self._r2.buckets)


class AsyncR2WithRawResponse:
    def __init__(self, r2: AsyncR2) -> None:
        self._r2 = r2

    @cached_property
    def buckets(self) -> AsyncBucketsWithRawResponse:
        return AsyncBucketsWithRawResponse(self._r2.buckets)


class R2WithStreamingResponse:
    def __init__(self, r2: R2) -> None:
        self._r2 = r2

    @cached_property
    def buckets(self) -> BucketsWithStreamingResponse:
        return BucketsWithStreamingResponse(self._r2.buckets)


class AsyncR2WithStreamingResponse:
    def __init__(self, r2: AsyncR2) -> None:
        self._r2 = r2

    @cached_property
    def buckets(self) -> AsyncBucketsWithStreamingResponse:
        return AsyncBucketsWithStreamingResponse(self._r2.buckets)
