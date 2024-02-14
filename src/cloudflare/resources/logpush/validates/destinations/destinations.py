# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .exists import Exists, AsyncExists

from ....._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from .....types import shared_params
from .exists import (
    Exists,
    AsyncExists,
    ExistsWithRawResponse,
    AsyncExistsWithRawResponse,
    ExistsWithStreamingResponse,
    AsyncExistsWithStreamingResponse,
)
from ....._wrappers import ResultWrapper

__all__ = ["Destinations", "AsyncDestinations"]


class Destinations(SyncAPIResource):
    @cached_property
    def exists(self) -> Exists:
        return Exists(self._client)

    @cached_property
    def with_raw_response(self) -> DestinationsWithRawResponse:
        return DestinationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DestinationsWithStreamingResponse:
        return DestinationsWithStreamingResponse(self)


class AsyncDestinations(AsyncAPIResource):
    @cached_property
    def exists(self) -> AsyncExists:
        return AsyncExists(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDestinationsWithRawResponse:
        return AsyncDestinationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDestinationsWithStreamingResponse:
        return AsyncDestinationsWithStreamingResponse(self)


class DestinationsWithRawResponse:
    def __init__(self, destinations: Destinations) -> None:
        self._destinations = destinations

    @cached_property
    def exists(self) -> ExistsWithRawResponse:
        return ExistsWithRawResponse(self._destinations.exists)


class AsyncDestinationsWithRawResponse:
    def __init__(self, destinations: AsyncDestinations) -> None:
        self._destinations = destinations

    @cached_property
    def exists(self) -> AsyncExistsWithRawResponse:
        return AsyncExistsWithRawResponse(self._destinations.exists)


class DestinationsWithStreamingResponse:
    def __init__(self, destinations: Destinations) -> None:
        self._destinations = destinations

    @cached_property
    def exists(self) -> ExistsWithStreamingResponse:
        return ExistsWithStreamingResponse(self._destinations.exists)


class AsyncDestinationsWithStreamingResponse:
    def __init__(self, destinations: AsyncDestinations) -> None:
        self._destinations = destinations

    @cached_property
    def exists(self) -> AsyncExistsWithStreamingResponse:
        return AsyncExistsWithStreamingResponse(self._destinations.exists)
