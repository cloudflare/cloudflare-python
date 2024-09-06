# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .database import DatabaseResource, AsyncDatabaseResource

from ..._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from .database import (
    DatabaseResource,
    AsyncDatabaseResource,
    DatabaseResourceWithRawResponse,
    AsyncDatabaseResourceWithRawResponse,
    DatabaseResourceWithStreamingResponse,
    AsyncDatabaseResourceWithStreamingResponse,
)

__all__ = ["D1Resource", "AsyncD1Resource"]


class D1Resource(SyncAPIResource):
    @cached_property
    def database(self) -> DatabaseResource:
        return DatabaseResource(self._client)

    @cached_property
    def with_raw_response(self) -> D1ResourceWithRawResponse:
        return D1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> D1ResourceWithStreamingResponse:
        return D1ResourceWithStreamingResponse(self)


class AsyncD1Resource(AsyncAPIResource):
    @cached_property
    def database(self) -> AsyncDatabaseResource:
        return AsyncDatabaseResource(self._client)

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
    def database(self) -> DatabaseResourceWithRawResponse:
        return DatabaseResourceWithRawResponse(self._d1.database)


class AsyncD1ResourceWithRawResponse:
    def __init__(self, d1: AsyncD1Resource) -> None:
        self._d1 = d1

    @cached_property
    def database(self) -> AsyncDatabaseResourceWithRawResponse:
        return AsyncDatabaseResourceWithRawResponse(self._d1.database)


class D1ResourceWithStreamingResponse:
    def __init__(self, d1: D1Resource) -> None:
        self._d1 = d1

    @cached_property
    def database(self) -> DatabaseResourceWithStreamingResponse:
        return DatabaseResourceWithStreamingResponse(self._d1.database)


class AsyncD1ResourceWithStreamingResponse:
    def __init__(self, d1: AsyncD1Resource) -> None:
        self._d1 = d1

    @cached_property
    def database(self) -> AsyncDatabaseResourceWithStreamingResponse:
        return AsyncDatabaseResourceWithStreamingResponse(self._d1.database)
