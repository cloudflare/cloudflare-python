# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .analytics import Analytics, AsyncAnalytics

from ..._compat import cached_property

from .kv.kv import Kv, AsyncKv

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
from .analytics import (
    Analytics,
    AsyncAnalytics,
    AnalyticsWithRawResponse,
    AsyncAnalyticsWithRawResponse,
    AnalyticsWithStreamingResponse,
    AsyncAnalyticsWithStreamingResponse,
)
from .kv import (
    Kv,
    AsyncKv,
    KvWithRawResponse,
    AsyncKvWithRawResponse,
    KvWithStreamingResponse,
    AsyncKvWithStreamingResponse,
)
from ..._wrappers import ResultWrapper

__all__ = ["Storage", "AsyncStorage"]


class Storage(SyncAPIResource):
    @cached_property
    def analytics(self) -> Analytics:
        return Analytics(self._client)

    @cached_property
    def kv(self) -> Kv:
        return Kv(self._client)

    @cached_property
    def with_raw_response(self) -> StorageWithRawResponse:
        return StorageWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StorageWithStreamingResponse:
        return StorageWithStreamingResponse(self)


class AsyncStorage(AsyncAPIResource):
    @cached_property
    def analytics(self) -> AsyncAnalytics:
        return AsyncAnalytics(self._client)

    @cached_property
    def kv(self) -> AsyncKv:
        return AsyncKv(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncStorageWithRawResponse:
        return AsyncStorageWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStorageWithStreamingResponse:
        return AsyncStorageWithStreamingResponse(self)


class StorageWithRawResponse:
    def __init__(self, storage: Storage) -> None:
        self._storage = storage

    @cached_property
    def analytics(self) -> AnalyticsWithRawResponse:
        return AnalyticsWithRawResponse(self._storage.analytics)

    @cached_property
    def kv(self) -> KvWithRawResponse:
        return KvWithRawResponse(self._storage.kv)


class AsyncStorageWithRawResponse:
    def __init__(self, storage: AsyncStorage) -> None:
        self._storage = storage

    @cached_property
    def analytics(self) -> AsyncAnalyticsWithRawResponse:
        return AsyncAnalyticsWithRawResponse(self._storage.analytics)

    @cached_property
    def kv(self) -> AsyncKvWithRawResponse:
        return AsyncKvWithRawResponse(self._storage.kv)


class StorageWithStreamingResponse:
    def __init__(self, storage: Storage) -> None:
        self._storage = storage

    @cached_property
    def analytics(self) -> AnalyticsWithStreamingResponse:
        return AnalyticsWithStreamingResponse(self._storage.analytics)

    @cached_property
    def kv(self) -> KvWithStreamingResponse:
        return KvWithStreamingResponse(self._storage.kv)


class AsyncStorageWithStreamingResponse:
    def __init__(self, storage: AsyncStorage) -> None:
        self._storage = storage

    @cached_property
    def analytics(self) -> AsyncAnalyticsWithStreamingResponse:
        return AsyncAnalyticsWithStreamingResponse(self._storage.analytics)

    @cached_property
    def kv(self) -> AsyncKvWithStreamingResponse:
        return AsyncKvWithStreamingResponse(self._storage.kv)
