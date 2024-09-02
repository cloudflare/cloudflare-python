# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .events import EventsResource, AsyncEventsResource

from ....._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .events import (
    EventsResource,
    AsyncEventsResource,
    EventsResourceWithRawResponse,
    AsyncEventsResourceWithRawResponse,
    EventsResourceWithStreamingResponse,
    AsyncEventsResourceWithStreamingResponse,
)

__all__ = ["LeaksResource", "AsyncLeaksResource"]


class LeaksResource(SyncAPIResource):
    @cached_property
    def events(self) -> EventsResource:
        return EventsResource(self._client)

    @cached_property
    def with_raw_response(self) -> LeaksResourceWithRawResponse:
        return LeaksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LeaksResourceWithStreamingResponse:
        return LeaksResourceWithStreamingResponse(self)


class AsyncLeaksResource(AsyncAPIResource):
    @cached_property
    def events(self) -> AsyncEventsResource:
        return AsyncEventsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLeaksResourceWithRawResponse:
        return AsyncLeaksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLeaksResourceWithStreamingResponse:
        return AsyncLeaksResourceWithStreamingResponse(self)


class LeaksResourceWithRawResponse:
    def __init__(self, leaks: LeaksResource) -> None:
        self._leaks = leaks

    @cached_property
    def events(self) -> EventsResourceWithRawResponse:
        return EventsResourceWithRawResponse(self._leaks.events)


class AsyncLeaksResourceWithRawResponse:
    def __init__(self, leaks: AsyncLeaksResource) -> None:
        self._leaks = leaks

    @cached_property
    def events(self) -> AsyncEventsResourceWithRawResponse:
        return AsyncEventsResourceWithRawResponse(self._leaks.events)


class LeaksResourceWithStreamingResponse:
    def __init__(self, leaks: LeaksResource) -> None:
        self._leaks = leaks

    @cached_property
    def events(self) -> EventsResourceWithStreamingResponse:
        return EventsResourceWithStreamingResponse(self._leaks.events)


class AsyncLeaksResourceWithStreamingResponse:
    def __init__(self, leaks: AsyncLeaksResource) -> None:
        self._leaks = leaks

    @cached_property
    def events(self) -> AsyncEventsResourceWithStreamingResponse:
        return AsyncEventsResourceWithStreamingResponse(self._leaks.events)
