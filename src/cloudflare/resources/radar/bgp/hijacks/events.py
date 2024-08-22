# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.radar.bgp.hijacks.event_list_response import EventListResponse

from .....pagination import SyncV4PagePagination, AsyncV4PagePagination

from ....._utils import maybe_transform

from ....._base_client import make_request_options, AsyncPaginator

from typing import Union

from datetime import datetime

from typing_extensions import Literal

from ....._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .....types.radar.bgp.hijacks import event_list_params

__all__ = ["EventsResource", "AsyncEventsResource"]

class EventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        return EventsResourceWithStreamingResponse(self)

    def list(self,
    *,
    date_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
    date_range: str | NotGiven = NOT_GIVEN,
    date_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
    event_id: int | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    hijacker_asn: int | NotGiven = NOT_GIVEN,
    involved_asn: int | NotGiven = NOT_GIVEN,
    involved_country: str | NotGiven = NOT_GIVEN,
    max_confidence: int | NotGiven = NOT_GIVEN,
    min_confidence: int | NotGiven = NOT_GIVEN,
    page: int | NotGiven = NOT_GIVEN,
    per_page: int | NotGiven = NOT_GIVEN,
    prefix: str | NotGiven = NOT_GIVEN,
    sort_by: Literal["ID", "TIME", "CONFIDENCE"] | NotGiven = NOT_GIVEN,
    sort_order: Literal["ASC", "DESC"] | NotGiven = NOT_GIVEN,
    victim_asn: int | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> SyncV4PagePagination[EventListResponse]:
        """Get the BGP hijack events.

        (Beta)

        Args:
          date_end: End of the date range (inclusive).

          date_range: Shorthand date ranges for the last X days - use when you don't need specific
              start and end dates.

          date_start: Start of the date range (inclusive).

          event_id: The unique identifier of a event

          format: Format results are returned in.

          hijacker_asn: The potential hijacker AS of a BGP hijack event

          involved_asn: The potential hijacker or victim AS of a BGP hijack event

          involved_country: The country code of the potential hijacker or victim AS of a BGP hijack event

          max_confidence: The maximum confidence score to filter events (1-4 low, 5-7 mid, 8+ high)

          min_confidence: The minimum confidence score to filter events (1-4 low, 5-7 mid, 8+ high)

          page: Current page number, starting from 1

          per_page: Number of entries per page

          prefix: Network prefix, IPv4 or IPv6.

          sort_by: Sort events by field

          sort_order: Sort order

          victim_asn: The potential victim AS of a BGP hijack event

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/radar/bgp/hijacks/events",
            page = SyncV4PagePagination[EventListResponse],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "event_id": event_id,
                "format": format,
                "hijacker_asn": hijacker_asn,
                "involved_asn": involved_asn,
                "involved_country": involved_country,
                "max_confidence": max_confidence,
                "min_confidence": min_confidence,
                "page": page,
                "per_page": per_page,
                "prefix": prefix,
                "sort_by": sort_by,
                "sort_order": sort_order,
                "victim_asn": victim_asn,
            }, event_list_params.EventListParams)),
            model=EventListResponse,
        )

class AsyncEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        return AsyncEventsResourceWithStreamingResponse(self)

    def list(self,
    *,
    date_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
    date_range: str | NotGiven = NOT_GIVEN,
    date_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
    event_id: int | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    hijacker_asn: int | NotGiven = NOT_GIVEN,
    involved_asn: int | NotGiven = NOT_GIVEN,
    involved_country: str | NotGiven = NOT_GIVEN,
    max_confidence: int | NotGiven = NOT_GIVEN,
    min_confidence: int | NotGiven = NOT_GIVEN,
    page: int | NotGiven = NOT_GIVEN,
    per_page: int | NotGiven = NOT_GIVEN,
    prefix: str | NotGiven = NOT_GIVEN,
    sort_by: Literal["ID", "TIME", "CONFIDENCE"] | NotGiven = NOT_GIVEN,
    sort_order: Literal["ASC", "DESC"] | NotGiven = NOT_GIVEN,
    victim_asn: int | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AsyncPaginator[EventListResponse, AsyncV4PagePagination[EventListResponse]]:
        """Get the BGP hijack events.

        (Beta)

        Args:
          date_end: End of the date range (inclusive).

          date_range: Shorthand date ranges for the last X days - use when you don't need specific
              start and end dates.

          date_start: Start of the date range (inclusive).

          event_id: The unique identifier of a event

          format: Format results are returned in.

          hijacker_asn: The potential hijacker AS of a BGP hijack event

          involved_asn: The potential hijacker or victim AS of a BGP hijack event

          involved_country: The country code of the potential hijacker or victim AS of a BGP hijack event

          max_confidence: The maximum confidence score to filter events (1-4 low, 5-7 mid, 8+ high)

          min_confidence: The minimum confidence score to filter events (1-4 low, 5-7 mid, 8+ high)

          page: Current page number, starting from 1

          per_page: Number of entries per page

          prefix: Network prefix, IPv4 or IPv6.

          sort_by: Sort events by field

          sort_order: Sort order

          victim_asn: The potential victim AS of a BGP hijack event

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/radar/bgp/hijacks/events",
            page = AsyncV4PagePagination[EventListResponse],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "event_id": event_id,
                "format": format,
                "hijacker_asn": hijacker_asn,
                "involved_asn": involved_asn,
                "involved_country": involved_country,
                "max_confidence": max_confidence,
                "min_confidence": min_confidence,
                "page": page,
                "per_page": per_page,
                "prefix": prefix,
                "sort_by": sort_by,
                "sort_order": sort_order,
                "victim_asn": victim_asn,
            }, event_list_params.EventListParams)),
            model=EventListResponse,
        )

class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.list = to_raw_response_wrapper(
            events.list,
        )

class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.list = async_to_raw_response_wrapper(
            events.list,
        )

class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.list = to_streamed_response_wrapper(
            events.list,
        )

class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.list = async_to_streamed_response_wrapper(
            events.list,
        )