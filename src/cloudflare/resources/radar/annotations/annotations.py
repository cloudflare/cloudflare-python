# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .outages.outages import Outages, AsyncOutages

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
from .outages import (
    Outages,
    AsyncOutages,
    OutagesWithRawResponse,
    AsyncOutagesWithRawResponse,
    OutagesWithStreamingResponse,
    AsyncOutagesWithStreamingResponse,
)
from ...._wrappers import ResultWrapper

__all__ = ["Annotations", "AsyncAnnotations"]


class Annotations(SyncAPIResource):
    @cached_property
    def outages(self) -> Outages:
        return Outages(self._client)

    @cached_property
    def with_raw_response(self) -> AnnotationsWithRawResponse:
        return AnnotationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnnotationsWithStreamingResponse:
        return AnnotationsWithStreamingResponse(self)


class AsyncAnnotations(AsyncAPIResource):
    @cached_property
    def outages(self) -> AsyncOutages:
        return AsyncOutages(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAnnotationsWithRawResponse:
        return AsyncAnnotationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnnotationsWithStreamingResponse:
        return AsyncAnnotationsWithStreamingResponse(self)


class AnnotationsWithRawResponse:
    def __init__(self, annotations: Annotations) -> None:
        self._annotations = annotations

    @cached_property
    def outages(self) -> OutagesWithRawResponse:
        return OutagesWithRawResponse(self._annotations.outages)


class AsyncAnnotationsWithRawResponse:
    def __init__(self, annotations: AsyncAnnotations) -> None:
        self._annotations = annotations

    @cached_property
    def outages(self) -> AsyncOutagesWithRawResponse:
        return AsyncOutagesWithRawResponse(self._annotations.outages)


class AnnotationsWithStreamingResponse:
    def __init__(self, annotations: Annotations) -> None:
        self._annotations = annotations

    @cached_property
    def outages(self) -> OutagesWithStreamingResponse:
        return OutagesWithStreamingResponse(self._annotations.outages)


class AsyncAnnotationsWithStreamingResponse:
    def __init__(self, annotations: AsyncAnnotations) -> None:
        self._annotations = annotations

    @cached_property
    def outages(self) -> AsyncOutagesWithStreamingResponse:
        return AsyncOutagesWithStreamingResponse(self._annotations.outages)
