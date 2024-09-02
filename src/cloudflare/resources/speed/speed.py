# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .schedule import ScheduleResource, AsyncScheduleResource

from ..._compat import cached_property

from .availabilities import AvailabilitiesResource, AsyncAvailabilitiesResource

from .pages.pages import PagesResource, AsyncPagesResource

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from .schedule import (
    ScheduleResource,
    AsyncScheduleResource,
    ScheduleResourceWithRawResponse,
    AsyncScheduleResourceWithRawResponse,
    ScheduleResourceWithStreamingResponse,
    AsyncScheduleResourceWithStreamingResponse,
)
from .availabilities import (
    AvailabilitiesResource,
    AsyncAvailabilitiesResource,
    AvailabilitiesResourceWithRawResponse,
    AsyncAvailabilitiesResourceWithRawResponse,
    AvailabilitiesResourceWithStreamingResponse,
    AsyncAvailabilitiesResourceWithStreamingResponse,
)
from .pages import (
    PagesResource,
    AsyncPagesResource,
    PagesResourceWithRawResponse,
    AsyncPagesResourceWithRawResponse,
    PagesResourceWithStreamingResponse,
    AsyncPagesResourceWithStreamingResponse,
)

__all__ = ["SpeedResource", "AsyncSpeedResource"]


class SpeedResource(SyncAPIResource):
    @cached_property
    def schedule(self) -> ScheduleResource:
        return ScheduleResource(self._client)

    @cached_property
    def availabilities(self) -> AvailabilitiesResource:
        return AvailabilitiesResource(self._client)

    @cached_property
    def pages(self) -> PagesResource:
        return PagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> SpeedResourceWithRawResponse:
        return SpeedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpeedResourceWithStreamingResponse:
        return SpeedResourceWithStreamingResponse(self)


class AsyncSpeedResource(AsyncAPIResource):
    @cached_property
    def schedule(self) -> AsyncScheduleResource:
        return AsyncScheduleResource(self._client)

    @cached_property
    def availabilities(self) -> AsyncAvailabilitiesResource:
        return AsyncAvailabilitiesResource(self._client)

    @cached_property
    def pages(self) -> AsyncPagesResource:
        return AsyncPagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSpeedResourceWithRawResponse:
        return AsyncSpeedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpeedResourceWithStreamingResponse:
        return AsyncSpeedResourceWithStreamingResponse(self)


class SpeedResourceWithRawResponse:
    def __init__(self, speed: SpeedResource) -> None:
        self._speed = speed

    @cached_property
    def schedule(self) -> ScheduleResourceWithRawResponse:
        return ScheduleResourceWithRawResponse(self._speed.schedule)

    @cached_property
    def availabilities(self) -> AvailabilitiesResourceWithRawResponse:
        return AvailabilitiesResourceWithRawResponse(self._speed.availabilities)

    @cached_property
    def pages(self) -> PagesResourceWithRawResponse:
        return PagesResourceWithRawResponse(self._speed.pages)


class AsyncSpeedResourceWithRawResponse:
    def __init__(self, speed: AsyncSpeedResource) -> None:
        self._speed = speed

    @cached_property
    def schedule(self) -> AsyncScheduleResourceWithRawResponse:
        return AsyncScheduleResourceWithRawResponse(self._speed.schedule)

    @cached_property
    def availabilities(self) -> AsyncAvailabilitiesResourceWithRawResponse:
        return AsyncAvailabilitiesResourceWithRawResponse(self._speed.availabilities)

    @cached_property
    def pages(self) -> AsyncPagesResourceWithRawResponse:
        return AsyncPagesResourceWithRawResponse(self._speed.pages)


class SpeedResourceWithStreamingResponse:
    def __init__(self, speed: SpeedResource) -> None:
        self._speed = speed

    @cached_property
    def schedule(self) -> ScheduleResourceWithStreamingResponse:
        return ScheduleResourceWithStreamingResponse(self._speed.schedule)

    @cached_property
    def availabilities(self) -> AvailabilitiesResourceWithStreamingResponse:
        return AvailabilitiesResourceWithStreamingResponse(self._speed.availabilities)

    @cached_property
    def pages(self) -> PagesResourceWithStreamingResponse:
        return PagesResourceWithStreamingResponse(self._speed.pages)


class AsyncSpeedResourceWithStreamingResponse:
    def __init__(self, speed: AsyncSpeedResource) -> None:
        self._speed = speed

    @cached_property
    def schedule(self) -> AsyncScheduleResourceWithStreamingResponse:
        return AsyncScheduleResourceWithStreamingResponse(self._speed.schedule)

    @cached_property
    def availabilities(self) -> AsyncAvailabilitiesResourceWithStreamingResponse:
        return AsyncAvailabilitiesResourceWithStreamingResponse(self._speed.availabilities)

    @cached_property
    def pages(self) -> AsyncPagesResourceWithStreamingResponse:
        return AsyncPagesResourceWithStreamingResponse(self._speed.pages)
