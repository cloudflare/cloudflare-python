# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .origin import Origin, AsyncOrigin

from ......._compat import cached_property

from .target import Target, AsyncTarget

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ......._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ......._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ......._resource import SyncAPIResource, AsyncAPIResource
from ......._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from .......types import shared_params
from .origin import (
    Origin,
    AsyncOrigin,
    OriginWithRawResponse,
    AsyncOriginWithRawResponse,
    OriginWithStreamingResponse,
    AsyncOriginWithStreamingResponse,
)
from .target import (
    Target,
    AsyncTarget,
    TargetWithRawResponse,
    AsyncTargetWithRawResponse,
    TargetWithStreamingResponse,
    AsyncTargetWithStreamingResponse,
)
from ......._wrappers import ResultWrapper

__all__ = ["Locations", "AsyncLocations"]


class Locations(SyncAPIResource):
    @cached_property
    def origin(self) -> Origin:
        return Origin(self._client)

    @cached_property
    def target(self) -> Target:
        return Target(self._client)

    @cached_property
    def with_raw_response(self) -> LocationsWithRawResponse:
        return LocationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LocationsWithStreamingResponse:
        return LocationsWithStreamingResponse(self)


class AsyncLocations(AsyncAPIResource):
    @cached_property
    def origin(self) -> AsyncOrigin:
        return AsyncOrigin(self._client)

    @cached_property
    def target(self) -> AsyncTarget:
        return AsyncTarget(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLocationsWithRawResponse:
        return AsyncLocationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLocationsWithStreamingResponse:
        return AsyncLocationsWithStreamingResponse(self)


class LocationsWithRawResponse:
    def __init__(self, locations: Locations) -> None:
        self._locations = locations

    @cached_property
    def origin(self) -> OriginWithRawResponse:
        return OriginWithRawResponse(self._locations.origin)

    @cached_property
    def target(self) -> TargetWithRawResponse:
        return TargetWithRawResponse(self._locations.target)


class AsyncLocationsWithRawResponse:
    def __init__(self, locations: AsyncLocations) -> None:
        self._locations = locations

    @cached_property
    def origin(self) -> AsyncOriginWithRawResponse:
        return AsyncOriginWithRawResponse(self._locations.origin)

    @cached_property
    def target(self) -> AsyncTargetWithRawResponse:
        return AsyncTargetWithRawResponse(self._locations.target)


class LocationsWithStreamingResponse:
    def __init__(self, locations: Locations) -> None:
        self._locations = locations

    @cached_property
    def origin(self) -> OriginWithStreamingResponse:
        return OriginWithStreamingResponse(self._locations.origin)

    @cached_property
    def target(self) -> TargetWithStreamingResponse:
        return TargetWithStreamingResponse(self._locations.target)


class AsyncLocationsWithStreamingResponse:
    def __init__(self, locations: AsyncLocations) -> None:
        self._locations = locations

    @cached_property
    def origin(self) -> AsyncOriginWithStreamingResponse:
        return AsyncOriginWithStreamingResponse(self._locations.origin)

    @cached_property
    def target(self) -> AsyncTargetWithStreamingResponse:
        return AsyncTargetWithStreamingResponse(self._locations.target)
