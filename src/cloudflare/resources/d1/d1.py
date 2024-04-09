# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .database import (
    Database,
    AsyncDatabase,
    DatabaseWithRawResponse,
    AsyncDatabaseWithRawResponse,
    DatabaseWithStreamingResponse,
    AsyncDatabaseWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["D1Resource", "AsyncD1Resource"]


class D1Resource(SyncAPIResource):
    @cached_property
    def database(self) -> Database:
        return Database(self._client)

    @cached_property
    def with_raw_response(self) -> D1ResourceWithRawResponse:
        return D1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> D1ResourceWithStreamingResponse:
        return D1ResourceWithStreamingResponse(self)


class AsyncD1Resource(AsyncAPIResource):
    @cached_property
    def database(self) -> AsyncDatabase:
        return AsyncDatabase(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncD1ResourceWithRawResponse:
        return AsyncD1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncD1ResourceWithStreamingResponse:
        return AsyncD1ResourceWithStreamingResponse(self)


class D1ResourceWithRawResponse:
    def __init__(self, d1: D1Resource) -> None:
        self._d1 = d1

    @cached_property
    def database(self) -> DatabaseWithRawResponse:
        return DatabaseWithRawResponse(self._d1.database)


class AsyncD1ResourceWithRawResponse:
    def __init__(self, d1: AsyncD1Resource) -> None:
        self._d1 = d1

    @cached_property
    def database(self) -> AsyncDatabaseWithRawResponse:
        return AsyncDatabaseWithRawResponse(self._d1.database)


class D1ResourceWithStreamingResponse:
    def __init__(self, d1: D1Resource) -> None:
        self._d1 = d1

    @cached_property
    def database(self) -> DatabaseWithStreamingResponse:
        return DatabaseWithStreamingResponse(self._d1.database)


class AsyncD1ResourceWithStreamingResponse:
    def __init__(self, d1: AsyncD1Resource) -> None:
        self._d1 = d1

    @cached_property
    def database(self) -> AsyncDatabaseWithStreamingResponse:
        return AsyncDatabaseWithStreamingResponse(self._d1.database)
