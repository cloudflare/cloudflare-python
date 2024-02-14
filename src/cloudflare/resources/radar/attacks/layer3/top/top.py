# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .attacks import Attacks, AsyncAttacks

from ......_compat import cached_property

from .industry import Industry, AsyncIndustry

from .locations.locations import Locations, AsyncLocations

from .vertical import Vertical, AsyncVertical

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ......_utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ......_types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ......types import shared_params
from .attacks import (
    Attacks,
    AsyncAttacks,
    AttacksWithRawResponse,
    AsyncAttacksWithRawResponse,
    AttacksWithStreamingResponse,
    AsyncAttacksWithStreamingResponse,
)
from .industry import (
    Industry,
    AsyncIndustry,
    IndustryWithRawResponse,
    AsyncIndustryWithRawResponse,
    IndustryWithStreamingResponse,
    AsyncIndustryWithStreamingResponse,
)
from .locations import (
    Locations,
    AsyncLocations,
    LocationsWithRawResponse,
    AsyncLocationsWithRawResponse,
    LocationsWithStreamingResponse,
    AsyncLocationsWithStreamingResponse,
)
from .vertical import (
    Vertical,
    AsyncVertical,
    VerticalWithRawResponse,
    AsyncVerticalWithRawResponse,
    VerticalWithStreamingResponse,
    AsyncVerticalWithStreamingResponse,
)
from ......_wrappers import ResultWrapper

__all__ = ["Top", "AsyncTop"]


class Top(SyncAPIResource):
    @cached_property
    def attacks(self) -> Attacks:
        return Attacks(self._client)

    @cached_property
    def industry(self) -> Industry:
        return Industry(self._client)

    @cached_property
    def locations(self) -> Locations:
        return Locations(self._client)

    @cached_property
    def vertical(self) -> Vertical:
        return Vertical(self._client)

    @cached_property
    def with_raw_response(self) -> TopWithRawResponse:
        return TopWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TopWithStreamingResponse:
        return TopWithStreamingResponse(self)


class AsyncTop(AsyncAPIResource):
    @cached_property
    def attacks(self) -> AsyncAttacks:
        return AsyncAttacks(self._client)

    @cached_property
    def industry(self) -> AsyncIndustry:
        return AsyncIndustry(self._client)

    @cached_property
    def locations(self) -> AsyncLocations:
        return AsyncLocations(self._client)

    @cached_property
    def vertical(self) -> AsyncVertical:
        return AsyncVertical(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTopWithRawResponse:
        return AsyncTopWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTopWithStreamingResponse:
        return AsyncTopWithStreamingResponse(self)


class TopWithRawResponse:
    def __init__(self, top: Top) -> None:
        self._top = top

    @cached_property
    def attacks(self) -> AttacksWithRawResponse:
        return AttacksWithRawResponse(self._top.attacks)

    @cached_property
    def industry(self) -> IndustryWithRawResponse:
        return IndustryWithRawResponse(self._top.industry)

    @cached_property
    def locations(self) -> LocationsWithRawResponse:
        return LocationsWithRawResponse(self._top.locations)

    @cached_property
    def vertical(self) -> VerticalWithRawResponse:
        return VerticalWithRawResponse(self._top.vertical)


class AsyncTopWithRawResponse:
    def __init__(self, top: AsyncTop) -> None:
        self._top = top

    @cached_property
    def attacks(self) -> AsyncAttacksWithRawResponse:
        return AsyncAttacksWithRawResponse(self._top.attacks)

    @cached_property
    def industry(self) -> AsyncIndustryWithRawResponse:
        return AsyncIndustryWithRawResponse(self._top.industry)

    @cached_property
    def locations(self) -> AsyncLocationsWithRawResponse:
        return AsyncLocationsWithRawResponse(self._top.locations)

    @cached_property
    def vertical(self) -> AsyncVerticalWithRawResponse:
        return AsyncVerticalWithRawResponse(self._top.vertical)


class TopWithStreamingResponse:
    def __init__(self, top: Top) -> None:
        self._top = top

    @cached_property
    def attacks(self) -> AttacksWithStreamingResponse:
        return AttacksWithStreamingResponse(self._top.attacks)

    @cached_property
    def industry(self) -> IndustryWithStreamingResponse:
        return IndustryWithStreamingResponse(self._top.industry)

    @cached_property
    def locations(self) -> LocationsWithStreamingResponse:
        return LocationsWithStreamingResponse(self._top.locations)

    @cached_property
    def vertical(self) -> VerticalWithStreamingResponse:
        return VerticalWithStreamingResponse(self._top.vertical)


class AsyncTopWithStreamingResponse:
    def __init__(self, top: AsyncTop) -> None:
        self._top = top

    @cached_property
    def attacks(self) -> AsyncAttacksWithStreamingResponse:
        return AsyncAttacksWithStreamingResponse(self._top.attacks)

    @cached_property
    def industry(self) -> AsyncIndustryWithStreamingResponse:
        return AsyncIndustryWithStreamingResponse(self._top.industry)

    @cached_property
    def locations(self) -> AsyncLocationsWithStreamingResponse:
        return AsyncLocationsWithStreamingResponse(self._top.locations)

    @cached_property
    def vertical(self) -> AsyncVerticalWithStreamingResponse:
        return AsyncVerticalWithStreamingResponse(self._top.vertical)
