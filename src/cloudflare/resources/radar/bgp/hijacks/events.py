# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncV4PagePagination, AsyncV4PagePagination
from ....._base_client import AsyncPaginator, make_request_options
from .....types.radar.bgp.hijacks import event_list_params
from .....types.radar.bgp.hijacks.event_list_response import EventListResponse

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return EventsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        date_end: Union[str, datetime] | Omit = omit,
        date_range: str | Omit = omit,
        date_start: Union[str, datetime] | Omit = omit,
        event_id: int | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        hijacker_asn: int | Omit = omit,
        involved_asn: int | Omit = omit,
        involved_country: str | Omit = omit,
        max_confidence: int | Omit = omit,
        min_confidence: int | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        prefix: str | Omit = omit,
        sort_by: Literal["ID", "TIME", "CONFIDENCE"] | Omit = omit,
        sort_order: Literal["ASC", "DESC"] | Omit = omit,
        victim_asn: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePagination[EventListResponse]:
        """
        Retrieves the BGP hijack events.

        Args:
          date_end: End of the date range (inclusive).

          date_range: Filters results by date range.

          date_start: Start of the date range (inclusive).

          event_id: The unique identifier of a event.

          format: Format in which results will be returned.

          hijacker_asn: The potential hijacker AS of a BGP hijack event.

          involved_asn: The potential hijacker or victim AS of a BGP hijack event.

          involved_country: The country code of the potential hijacker or victim AS of a BGP hijack event.

          max_confidence: Filters events by maximum confidence score (1-4 low, 5-7 mid, 8+ high).

          min_confidence: Filters events by minimum confidence score (1-4 low, 5-7 mid, 8+ high).

          page: Current page number, starting from 1.

          per_page: Number of entries per page.

          sort_by: Sorts results by the specified field.

          sort_order: Sort order.

          victim_asn: The potential victim AS of a BGP hijack event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/radar/bgp/hijacks/events",
            page=SyncV4PagePagination[EventListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
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
                    },
                    event_list_params.EventListParams,
                ),
            ),
            model=EventListResponse,
        )


class AsyncEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncEventsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        date_end: Union[str, datetime] | Omit = omit,
        date_range: str | Omit = omit,
        date_start: Union[str, datetime] | Omit = omit,
        event_id: int | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        hijacker_asn: int | Omit = omit,
        involved_asn: int | Omit = omit,
        involved_country: str | Omit = omit,
        max_confidence: int | Omit = omit,
        min_confidence: int | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        prefix: str | Omit = omit,
        sort_by: Literal["ID", "TIME", "CONFIDENCE"] | Omit = omit,
        sort_order: Literal["ASC", "DESC"] | Omit = omit,
        victim_asn: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[EventListResponse, AsyncV4PagePagination[EventListResponse]]:
        """
        Retrieves the BGP hijack events.

        Args:
          date_end: End of the date range (inclusive).

          date_range: Filters results by date range.

          date_start: Start of the date range (inclusive).

          event_id: The unique identifier of a event.

          format: Format in which results will be returned.

          hijacker_asn: The potential hijacker AS of a BGP hijack event.

          involved_asn: The potential hijacker or victim AS of a BGP hijack event.

          involved_country: The country code of the potential hijacker or victim AS of a BGP hijack event.

          max_confidence: Filters events by maximum confidence score (1-4 low, 5-7 mid, 8+ high).

          min_confidence: Filters events by minimum confidence score (1-4 low, 5-7 mid, 8+ high).

          page: Current page number, starting from 1.

          per_page: Number of entries per page.

          sort_by: Sorts results by the specified field.

          sort_order: Sort order.

          victim_asn: The potential victim AS of a BGP hijack event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/radar/bgp/hijacks/events",
            page=AsyncV4PagePagination[EventListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
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
                    },
                    event_list_params.EventListParams,
                ),
            ),
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
