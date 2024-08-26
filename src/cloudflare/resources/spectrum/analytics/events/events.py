# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .bytimes import BytimesResource, AsyncBytimesResource

from ....._compat import cached_property

from .summaries import SummariesResource, AsyncSummariesResource

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .bytimes import BytimesResource, AsyncBytimesResource, BytimesResourceWithRawResponse, AsyncBytimesResourceWithRawResponse, BytimesResourceWithStreamingResponse, AsyncBytimesResourceWithStreamingResponse
from .summaries import SummariesResource, AsyncSummariesResource, SummariesResourceWithRawResponse, AsyncSummariesResourceWithRawResponse, SummariesResourceWithStreamingResponse, AsyncSummariesResourceWithStreamingResponse

__all__ = ["EventsResource", "AsyncEventsResource"]

class EventsResource(SyncAPIResource):
    @cached_property
    def bytimes(self) -> BytimesResource:
        return BytimesResource(self._client)

    @cached_property
    def summaries(self) -> SummariesResource:
        return SummariesResource(self._client)

    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        return EventsResourceWithStreamingResponse(self)

class AsyncEventsResource(AsyncAPIResource):
    @cached_property
    def bytimes(self) -> AsyncBytimesResource:
        return AsyncBytimesResource(self._client)

    @cached_property
    def summaries(self) -> AsyncSummariesResource:
        return AsyncSummariesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        return AsyncEventsResourceWithStreamingResponse(self)

class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

    @cached_property
    def bytimes(self) -> BytimesResourceWithRawResponse:
        return BytimesResourceWithRawResponse(self._events.bytimes)

    @cached_property
    def summaries(self) -> SummariesResourceWithRawResponse:
        return SummariesResourceWithRawResponse(self._events.summaries)

class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

    @cached_property
    def bytimes(self) -> AsyncBytimesResourceWithRawResponse:
        return AsyncBytimesResourceWithRawResponse(self._events.bytimes)

    @cached_property
    def summaries(self) -> AsyncSummariesResourceWithRawResponse:
        return AsyncSummariesResourceWithRawResponse(self._events.summaries)

class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

    @cached_property
    def bytimes(self) -> BytimesResourceWithStreamingResponse:
        return BytimesResourceWithStreamingResponse(self._events.bytimes)

    @cached_property
    def summaries(self) -> SummariesResourceWithStreamingResponse:
        return SummariesResourceWithStreamingResponse(self._events.summaries)

class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

    @cached_property
    def bytimes(self) -> AsyncBytimesResourceWithStreamingResponse:
        return AsyncBytimesResourceWithStreamingResponse(self._events.bytimes)

    @cached_property
    def summaries(self) -> AsyncSummariesResourceWithStreamingResponse:
        return AsyncSummariesResourceWithStreamingResponse(self._events.summaries)