# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .analytics import (
    Analytics,
    AsyncAnalytics,
    AnalyticsWithRawResponse,
    AsyncAnalyticsWithRawResponse,
    AnalyticsWithStreamingResponse,
    AsyncAnalyticsWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Storage", "AsyncStorage"]


class Storage(SyncAPIResource):
    @cached_property
    def analytics(self) -> Analytics:
        return Analytics(self._client)

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


class AsyncStorageWithRawResponse:
    def __init__(self, storage: AsyncStorage) -> None:
        self._storage = storage

    @cached_property
    def analytics(self) -> AsyncAnalyticsWithRawResponse:
        return AsyncAnalyticsWithRawResponse(self._storage.analytics)


class StorageWithStreamingResponse:
    def __init__(self, storage: Storage) -> None:
        self._storage = storage

    @cached_property
    def analytics(self) -> AnalyticsWithStreamingResponse:
        return AnalyticsWithStreamingResponse(self._storage.analytics)


class AsyncStorageWithStreamingResponse:
    def __init__(self, storage: AsyncStorage) -> None:
        self._storage = storage

    @cached_property
    def analytics(self) -> AsyncAnalyticsWithStreamingResponse:
        return AsyncAnalyticsWithStreamingResponse(self._storage.analytics)
