# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .indexes.indexes import IndexesResource, AsyncIndexesResource

from ..._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from .indexes import (
    IndexesResource,
    AsyncIndexesResource,
    IndexesResourceWithRawResponse,
    AsyncIndexesResourceWithRawResponse,
    IndexesResourceWithStreamingResponse,
    AsyncIndexesResourceWithStreamingResponse,
)

__all__ = ["VectorizeResource", "AsyncVectorizeResource"]


class VectorizeResource(SyncAPIResource):
    @cached_property
    def indexes(self) -> IndexesResource:
        return IndexesResource(self._client)

    @cached_property
    def with_raw_response(self) -> VectorizeResourceWithRawResponse:
        return VectorizeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VectorizeResourceWithStreamingResponse:
        return VectorizeResourceWithStreamingResponse(self)


class AsyncVectorizeResource(AsyncAPIResource):
    @cached_property
    def indexes(self) -> AsyncIndexesResource:
        return AsyncIndexesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVectorizeResourceWithRawResponse:
        return AsyncVectorizeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVectorizeResourceWithStreamingResponse:
        return AsyncVectorizeResourceWithStreamingResponse(self)


class VectorizeResourceWithRawResponse:
    def __init__(self, vectorize: VectorizeResource) -> None:
        self._vectorize = vectorize

    @cached_property
    def indexes(self) -> IndexesResourceWithRawResponse:
        return IndexesResourceWithRawResponse(self._vectorize.indexes)


class AsyncVectorizeResourceWithRawResponse:
    def __init__(self, vectorize: AsyncVectorizeResource) -> None:
        self._vectorize = vectorize

    @cached_property
    def indexes(self) -> AsyncIndexesResourceWithRawResponse:
        return AsyncIndexesResourceWithRawResponse(self._vectorize.indexes)


class VectorizeResourceWithStreamingResponse:
    def __init__(self, vectorize: VectorizeResource) -> None:
        self._vectorize = vectorize

    @cached_property
    def indexes(self) -> IndexesResourceWithStreamingResponse:
        return IndexesResourceWithStreamingResponse(self._vectorize.indexes)


class AsyncVectorizeResourceWithStreamingResponse:
    def __init__(self, vectorize: AsyncVectorizeResource) -> None:
        self._vectorize = vectorize

    @cached_property
    def indexes(self) -> AsyncIndexesResourceWithStreamingResponse:
        return AsyncIndexesResourceWithStreamingResponse(self._vectorize.indexes)
