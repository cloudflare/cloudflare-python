# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.radar.bgp import LeakEventsResponse, leak_events_params

__all__ = ["Leaks", "AsyncLeaks"]


class Leaks(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LeaksWithRawResponse:
        return LeaksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LeaksWithStreamingResponse:
        return LeaksWithStreamingResponse(self)

    def events(
        self,
        *,
        date_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        date_range: Literal[
            "1d",
            "2d",
            "7d",
            "14d",
            "28d",
            "12w",
            "24w",
            "52w",
            "1dControl",
            "2dControl",
            "7dControl",
            "14dControl",
            "28dControl",
            "12wControl",
            "24wControl",
        ]
        | NotGiven = NOT_GIVEN,
        date_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        event_id: int | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        involved_asn: int | NotGiven = NOT_GIVEN,
        involved_country: str | NotGiven = NOT_GIVEN,
        leak_asn: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort_by: Literal["ID", "LEAKS", "PEERS", "PREFIXES", "ORIGINS", "TIME"] | NotGiven = NOT_GIVEN,
        sort_order: Literal["ASC", "DESC"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LeakEventsResponse:
        """
        Get the BGP route leak events (Beta).

        Args:
          date_end: End of the date range (inclusive).

          date_range: Shorthand date ranges for the last X days - use when you don't need specific
              start and end dates.

          date_start: Start of the date range (inclusive).

          event_id: The unique identifier of a event

          format: Format results are returned in.

          involved_asn: ASN that is causing or affected by a route leak event

          involved_country: Country code of a involved ASN in a route leak event

          leak_asn: The leaking AS of a route leak event

          page: Current page number, starting from 1

          per_page: Number of entries per page

          sort_by: Sort events by field

          sort_order: Sort order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/bgp/leaks/events",
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
                        "involved_asn": involved_asn,
                        "involved_country": involved_country,
                        "leak_asn": leak_asn,
                        "page": page,
                        "per_page": per_page,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                    },
                    leak_events_params.LeakEventsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LeakEventsResponse], ResultWrapper[LeakEventsResponse]),
        )


class AsyncLeaks(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLeaksWithRawResponse:
        return AsyncLeaksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLeaksWithStreamingResponse:
        return AsyncLeaksWithStreamingResponse(self)

    async def events(
        self,
        *,
        date_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        date_range: Literal[
            "1d",
            "2d",
            "7d",
            "14d",
            "28d",
            "12w",
            "24w",
            "52w",
            "1dControl",
            "2dControl",
            "7dControl",
            "14dControl",
            "28dControl",
            "12wControl",
            "24wControl",
        ]
        | NotGiven = NOT_GIVEN,
        date_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        event_id: int | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        involved_asn: int | NotGiven = NOT_GIVEN,
        involved_country: str | NotGiven = NOT_GIVEN,
        leak_asn: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort_by: Literal["ID", "LEAKS", "PEERS", "PREFIXES", "ORIGINS", "TIME"] | NotGiven = NOT_GIVEN,
        sort_order: Literal["ASC", "DESC"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LeakEventsResponse:
        """
        Get the BGP route leak events (Beta).

        Args:
          date_end: End of the date range (inclusive).

          date_range: Shorthand date ranges for the last X days - use when you don't need specific
              start and end dates.

          date_start: Start of the date range (inclusive).

          event_id: The unique identifier of a event

          format: Format results are returned in.

          involved_asn: ASN that is causing or affected by a route leak event

          involved_country: Country code of a involved ASN in a route leak event

          leak_asn: The leaking AS of a route leak event

          page: Current page number, starting from 1

          per_page: Number of entries per page

          sort_by: Sort events by field

          sort_order: Sort order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/bgp/leaks/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "event_id": event_id,
                        "format": format,
                        "involved_asn": involved_asn,
                        "involved_country": involved_country,
                        "leak_asn": leak_asn,
                        "page": page,
                        "per_page": per_page,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                    },
                    leak_events_params.LeakEventsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LeakEventsResponse], ResultWrapper[LeakEventsResponse]),
        )


class LeaksWithRawResponse:
    def __init__(self, leaks: Leaks) -> None:
        self._leaks = leaks

        self.events = to_raw_response_wrapper(
            leaks.events,
        )


class AsyncLeaksWithRawResponse:
    def __init__(self, leaks: AsyncLeaks) -> None:
        self._leaks = leaks

        self.events = async_to_raw_response_wrapper(
            leaks.events,
        )


class LeaksWithStreamingResponse:
    def __init__(self, leaks: Leaks) -> None:
        self._leaks = leaks

        self.events = to_streamed_response_wrapper(
            leaks.events,
        )


class AsyncLeaksWithStreamingResponse:
    def __init__(self, leaks: AsyncLeaks) -> None:
        self._leaks = leaks

        self.events = async_to_streamed_response_wrapper(
            leaks.events,
        )
