# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .bytimes import Bytimes, AsyncBytimes

from ....._compat import cached_property

from .summaries import Summaries, AsyncSummaries

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
from .bytimes import (
    Bytimes,
    AsyncBytimes,
    BytimesWithRawResponse,
    AsyncBytimesWithRawResponse,
    BytimesWithStreamingResponse,
    AsyncBytimesWithStreamingResponse,
)
from .summaries import (
    Summaries,
    AsyncSummaries,
    SummariesWithRawResponse,
    AsyncSummariesWithRawResponse,
    SummariesWithStreamingResponse,
    AsyncSummariesWithStreamingResponse,
)
from ....._wrappers import ResultWrapper

__all__ = ["Events", "AsyncEvents"]


class Events(SyncAPIResource):
    @cached_property
    def bytimes(self) -> Bytimes:
        return Bytimes(self._client)

    @cached_property
    def summaries(self) -> Summaries:
        return Summaries(self._client)

    @cached_property
    def with_raw_response(self) -> EventsWithRawResponse:
        return EventsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsWithStreamingResponse:
        return EventsWithStreamingResponse(self)


class AsyncEvents(AsyncAPIResource):
    @cached_property
    def bytimes(self) -> AsyncBytimes:
        return AsyncBytimes(self._client)

    @cached_property
    def summaries(self) -> AsyncSummaries:
        return AsyncSummaries(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEventsWithRawResponse:
        return AsyncEventsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsWithStreamingResponse:
        return AsyncEventsWithStreamingResponse(self)


class EventsWithRawResponse:
    def __init__(self, events: Events) -> None:
        self._events = events

    @cached_property
    def bytimes(self) -> BytimesWithRawResponse:
        return BytimesWithRawResponse(self._events.bytimes)

    @cached_property
    def summaries(self) -> SummariesWithRawResponse:
        return SummariesWithRawResponse(self._events.summaries)


class AsyncEventsWithRawResponse:
    def __init__(self, events: AsyncEvents) -> None:
        self._events = events

    @cached_property
    def bytimes(self) -> AsyncBytimesWithRawResponse:
        return AsyncBytimesWithRawResponse(self._events.bytimes)

    @cached_property
    def summaries(self) -> AsyncSummariesWithRawResponse:
        return AsyncSummariesWithRawResponse(self._events.summaries)


class EventsWithStreamingResponse:
    def __init__(self, events: Events) -> None:
        self._events = events

    @cached_property
    def bytimes(self) -> BytimesWithStreamingResponse:
        return BytimesWithStreamingResponse(self._events.bytimes)

    @cached_property
    def summaries(self) -> SummariesWithStreamingResponse:
        return SummariesWithStreamingResponse(self._events.summaries)


class AsyncEventsWithStreamingResponse:
    def __init__(self, events: AsyncEvents) -> None:
        self._events = events

    @cached_property
    def bytimes(self) -> AsyncBytimesWithStreamingResponse:
        return AsyncBytimesWithStreamingResponse(self._events.bytimes)

    @cached_property
    def summaries(self) -> AsyncSummariesWithStreamingResponse:
        return AsyncSummariesWithStreamingResponse(self._events.summaries)
