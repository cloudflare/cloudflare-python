# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .analytics import AnalyticsResource, AsyncAnalyticsResource

from ..._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from .analytics import AnalyticsResource, AsyncAnalyticsResource, AnalyticsResourceWithRawResponse, AsyncAnalyticsResourceWithRawResponse, AnalyticsResourceWithStreamingResponse, AsyncAnalyticsResourceWithStreamingResponse

__all__ = ["StorageResource", "AsyncStorageResource"]

class StorageResource(SyncAPIResource):
    @cached_property
    def analytics(self) -> AnalyticsResource:
        return AnalyticsResource(self._client)

    @cached_property
    def with_raw_response(self) -> StorageResourceWithRawResponse:
        return StorageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StorageResourceWithStreamingResponse:
        return StorageResourceWithStreamingResponse(self)

class AsyncStorageResource(AsyncAPIResource):
    @cached_property
    def analytics(self) -> AsyncAnalyticsResource:
        return AsyncAnalyticsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncStorageResourceWithRawResponse:
        return AsyncStorageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStorageResourceWithStreamingResponse:
        return AsyncStorageResourceWithStreamingResponse(self)

class StorageResourceWithRawResponse:
    def __init__(self, storage: StorageResource) -> None:
        self._storage = storage

    @cached_property
    def analytics(self) -> AnalyticsResourceWithRawResponse:
        return AnalyticsResourceWithRawResponse(self._storage.analytics)

class AsyncStorageResourceWithRawResponse:
    def __init__(self, storage: AsyncStorageResource) -> None:
        self._storage = storage

    @cached_property
    def analytics(self) -> AsyncAnalyticsResourceWithRawResponse:
        return AsyncAnalyticsResourceWithRawResponse(self._storage.analytics)

class StorageResourceWithStreamingResponse:
    def __init__(self, storage: StorageResource) -> None:
        self._storage = storage

    @cached_property
    def analytics(self) -> AnalyticsResourceWithStreamingResponse:
        return AnalyticsResourceWithStreamingResponse(self._storage.analytics)

class AsyncStorageResourceWithStreamingResponse:
    def __init__(self, storage: AsyncStorageResource) -> None:
        self._storage = storage

    @cached_property
    def analytics(self) -> AsyncAnalyticsResourceWithStreamingResponse:
        return AsyncAnalyticsResourceWithStreamingResponse(self._storage.analytics)