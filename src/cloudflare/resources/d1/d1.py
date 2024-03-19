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

__all__ = ["D1", "AsyncD1"]


class D1(SyncAPIResource):
    @cached_property
    def database(self) -> Database:
        return Database(self._client)

    @cached_property
    def with_raw_response(self) -> D1WithRawResponse:
        return D1WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> D1WithStreamingResponse:
        return D1WithStreamingResponse(self)


class AsyncD1(AsyncAPIResource):
    @cached_property
    def database(self) -> AsyncDatabase:
        return AsyncDatabase(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncD1WithRawResponse:
        return AsyncD1WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncD1WithStreamingResponse:
        return AsyncD1WithStreamingResponse(self)


class D1WithRawResponse:
    def __init__(self, d1: D1) -> None:
        self._d1 = d1

    @cached_property
    def database(self) -> DatabaseWithRawResponse:
        return DatabaseWithRawResponse(self._d1.database)


class AsyncD1WithRawResponse:
    def __init__(self, d1: AsyncD1) -> None:
        self._d1 = d1

    @cached_property
    def database(self) -> AsyncDatabaseWithRawResponse:
        return AsyncDatabaseWithRawResponse(self._d1.database)


class D1WithStreamingResponse:
    def __init__(self, d1: D1) -> None:
        self._d1 = d1

    @cached_property
    def database(self) -> DatabaseWithStreamingResponse:
        return DatabaseWithStreamingResponse(self._d1.database)


class AsyncD1WithStreamingResponse:
    def __init__(self, d1: AsyncD1) -> None:
        self._d1 = d1

    @cached_property
    def database(self) -> AsyncDatabaseWithStreamingResponse:
        return AsyncDatabaseWithStreamingResponse(self._d1.database)
