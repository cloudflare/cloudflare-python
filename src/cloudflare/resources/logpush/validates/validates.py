# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .destinations.destinations import Destinations, AsyncDestinations

from ...._compat import cached_property

from .origins import Origins, AsyncOrigins

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
from .destinations import (
    Destinations,
    AsyncDestinations,
    DestinationsWithRawResponse,
    AsyncDestinationsWithRawResponse,
    DestinationsWithStreamingResponse,
    AsyncDestinationsWithStreamingResponse,
)
from .origins import (
    Origins,
    AsyncOrigins,
    OriginsWithRawResponse,
    AsyncOriginsWithRawResponse,
    OriginsWithStreamingResponse,
    AsyncOriginsWithStreamingResponse,
)
from ...._wrappers import ResultWrapper

__all__ = ["Validates", "AsyncValidates"]


class Validates(SyncAPIResource):
    @cached_property
    def destinations(self) -> Destinations:
        return Destinations(self._client)

    @cached_property
    def origins(self) -> Origins:
        return Origins(self._client)

    @cached_property
    def with_raw_response(self) -> ValidatesWithRawResponse:
        return ValidatesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ValidatesWithStreamingResponse:
        return ValidatesWithStreamingResponse(self)


class AsyncValidates(AsyncAPIResource):
    @cached_property
    def destinations(self) -> AsyncDestinations:
        return AsyncDestinations(self._client)

    @cached_property
    def origins(self) -> AsyncOrigins:
        return AsyncOrigins(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncValidatesWithRawResponse:
        return AsyncValidatesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncValidatesWithStreamingResponse:
        return AsyncValidatesWithStreamingResponse(self)


class ValidatesWithRawResponse:
    def __init__(self, validates: Validates) -> None:
        self._validates = validates

    @cached_property
    def destinations(self) -> DestinationsWithRawResponse:
        return DestinationsWithRawResponse(self._validates.destinations)

    @cached_property
    def origins(self) -> OriginsWithRawResponse:
        return OriginsWithRawResponse(self._validates.origins)


class AsyncValidatesWithRawResponse:
    def __init__(self, validates: AsyncValidates) -> None:
        self._validates = validates

    @cached_property
    def destinations(self) -> AsyncDestinationsWithRawResponse:
        return AsyncDestinationsWithRawResponse(self._validates.destinations)

    @cached_property
    def origins(self) -> AsyncOriginsWithRawResponse:
        return AsyncOriginsWithRawResponse(self._validates.origins)


class ValidatesWithStreamingResponse:
    def __init__(self, validates: Validates) -> None:
        self._validates = validates

    @cached_property
    def destinations(self) -> DestinationsWithStreamingResponse:
        return DestinationsWithStreamingResponse(self._validates.destinations)

    @cached_property
    def origins(self) -> OriginsWithStreamingResponse:
        return OriginsWithStreamingResponse(self._validates.origins)


class AsyncValidatesWithStreamingResponse:
    def __init__(self, validates: AsyncValidates) -> None:
        self._validates = validates

    @cached_property
    def destinations(self) -> AsyncDestinationsWithStreamingResponse:
        return AsyncDestinationsWithStreamingResponse(self._validates.destinations)

    @cached_property
    def origins(self) -> AsyncOriginsWithStreamingResponse:
        return AsyncOriginsWithStreamingResponse(self._validates.origins)
