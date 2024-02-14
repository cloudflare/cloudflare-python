# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .databases import Databases, AsyncDatabases

from ..._compat import cached_property

from .database import Database, AsyncDatabase

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
from .databases import (
    Databases,
    AsyncDatabases,
    DatabasesWithRawResponse,
    AsyncDatabasesWithRawResponse,
    DatabasesWithStreamingResponse,
    AsyncDatabasesWithStreamingResponse,
)
from .database import (
    Database,
    AsyncDatabase,
    DatabaseWithRawResponse,
    AsyncDatabaseWithRawResponse,
    DatabaseWithStreamingResponse,
    AsyncDatabaseWithStreamingResponse,
)
from ..._wrappers import ResultWrapper

__all__ = ["D1", "AsyncD1"]


class D1(SyncAPIResource):
    @cached_property
    def databases(self) -> Databases:
        return Databases(self._client)

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
    def databases(self) -> AsyncDatabases:
        return AsyncDatabases(self._client)

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
    def databases(self) -> DatabasesWithRawResponse:
        return DatabasesWithRawResponse(self._d1.databases)

    @cached_property
    def database(self) -> DatabaseWithRawResponse:
        return DatabaseWithRawResponse(self._d1.database)


class AsyncD1WithRawResponse:
    def __init__(self, d1: AsyncD1) -> None:
        self._d1 = d1

    @cached_property
    def databases(self) -> AsyncDatabasesWithRawResponse:
        return AsyncDatabasesWithRawResponse(self._d1.databases)

    @cached_property
    def database(self) -> AsyncDatabaseWithRawResponse:
        return AsyncDatabaseWithRawResponse(self._d1.database)


class D1WithStreamingResponse:
    def __init__(self, d1: D1) -> None:
        self._d1 = d1

    @cached_property
    def databases(self) -> DatabasesWithStreamingResponse:
        return DatabasesWithStreamingResponse(self._d1.databases)

    @cached_property
    def database(self) -> DatabaseWithStreamingResponse:
        return DatabaseWithStreamingResponse(self._d1.database)


class AsyncD1WithStreamingResponse:
    def __init__(self, d1: AsyncD1) -> None:
        self._d1 = d1

    @cached_property
    def databases(self) -> AsyncDatabasesWithStreamingResponse:
        return AsyncDatabasesWithStreamingResponse(self._d1.databases)

    @cached_property
    def database(self) -> AsyncDatabaseWithStreamingResponse:
        return AsyncDatabaseWithStreamingResponse(self._d1.database)
