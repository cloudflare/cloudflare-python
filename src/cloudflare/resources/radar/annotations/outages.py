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
from ...._base_client import make_request_options
from ....types.radar.annotations import outage_get_params, outage_locations_params
from ....types.radar.annotations.outage_get_response import OutageGetResponse
from ....types.radar.annotations.outage_locations_response import OutageLocationsResponse

__all__ = ["OutagesResource", "AsyncOutagesResource"]


class OutagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OutagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return OutagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OutagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return OutagesResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        asn: int | NotGiven = NOT_GIVEN,
        date_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        date_range: str | NotGiven = NOT_GIVEN,
        date_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutageGetResponse:
        """
        Retrieves the latest Internet outages and anomalies.

        Args:
          asn: Single Autonomous System Number (ASN) as integer.

          date_end: End of the date range (inclusive).

          date_range: Shorthand date ranges for the last X days - use when you don't need specific
              start and end dates.

          date_start: Start of the date range (inclusive).

          format: Format in which results will be returned.

          limit: Limits the number of objects returned in the response.

          location: Location alpha-2 code.

          offset: Skips the specified number of objects before fetching the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/annotations/outages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asn": asn,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "limit": limit,
                        "location": location,
                        "offset": offset,
                    },
                    outage_get_params.OutageGetParams,
                ),
                post_parser=ResultWrapper[OutageGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[OutageGetResponse], ResultWrapper[OutageGetResponse]),
        )

    def locations(
        self,
        *,
        date_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        date_range: str | NotGiven = NOT_GIVEN,
        date_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutageLocationsResponse:
        """
        Retrieves the number of outages by location.

        Args:
          date_end: End of the date range (inclusive).

          date_range: Shorthand date ranges for the last X days - use when you don't need specific
              start and end dates.

          date_start: Start of the date range (inclusive).

          format: Format in which results will be returned.

          limit: Limits the number of objects returned in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/annotations/outages/locations",
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
                        "format": format,
                        "limit": limit,
                    },
                    outage_locations_params.OutageLocationsParams,
                ),
                post_parser=ResultWrapper[OutageLocationsResponse]._unwrapper,
            ),
            cast_to=cast(Type[OutageLocationsResponse], ResultWrapper[OutageLocationsResponse]),
        )


class AsyncOutagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOutagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOutagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOutagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncOutagesResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        asn: int | NotGiven = NOT_GIVEN,
        date_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        date_range: str | NotGiven = NOT_GIVEN,
        date_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutageGetResponse:
        """
        Retrieves the latest Internet outages and anomalies.

        Args:
          asn: Single Autonomous System Number (ASN) as integer.

          date_end: End of the date range (inclusive).

          date_range: Shorthand date ranges for the last X days - use when you don't need specific
              start and end dates.

          date_start: Start of the date range (inclusive).

          format: Format in which results will be returned.

          limit: Limits the number of objects returned in the response.

          location: Location alpha-2 code.

          offset: Skips the specified number of objects before fetching the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/annotations/outages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asn": asn,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "limit": limit,
                        "location": location,
                        "offset": offset,
                    },
                    outage_get_params.OutageGetParams,
                ),
                post_parser=ResultWrapper[OutageGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[OutageGetResponse], ResultWrapper[OutageGetResponse]),
        )

    async def locations(
        self,
        *,
        date_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        date_range: str | NotGiven = NOT_GIVEN,
        date_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutageLocationsResponse:
        """
        Retrieves the number of outages by location.

        Args:
          date_end: End of the date range (inclusive).

          date_range: Shorthand date ranges for the last X days - use when you don't need specific
              start and end dates.

          date_start: Start of the date range (inclusive).

          format: Format in which results will be returned.

          limit: Limits the number of objects returned in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/annotations/outages/locations",
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
                        "format": format,
                        "limit": limit,
                    },
                    outage_locations_params.OutageLocationsParams,
                ),
                post_parser=ResultWrapper[OutageLocationsResponse]._unwrapper,
            ),
            cast_to=cast(Type[OutageLocationsResponse], ResultWrapper[OutageLocationsResponse]),
        )


class OutagesResourceWithRawResponse:
    def __init__(self, outages: OutagesResource) -> None:
        self._outages = outages

        self.get = to_raw_response_wrapper(
            outages.get,
        )
        self.locations = to_raw_response_wrapper(
            outages.locations,
        )


class AsyncOutagesResourceWithRawResponse:
    def __init__(self, outages: AsyncOutagesResource) -> None:
        self._outages = outages

        self.get = async_to_raw_response_wrapper(
            outages.get,
        )
        self.locations = async_to_raw_response_wrapper(
            outages.locations,
        )


class OutagesResourceWithStreamingResponse:
    def __init__(self, outages: OutagesResource) -> None:
        self._outages = outages

        self.get = to_streamed_response_wrapper(
            outages.get,
        )
        self.locations = to_streamed_response_wrapper(
            outages.locations,
        )


class AsyncOutagesResourceWithStreamingResponse:
    def __init__(self, outages: AsyncOutagesResource) -> None:
        self._outages = outages

        self.get = async_to_streamed_response_wrapper(
            outages.get,
        )
        self.locations = async_to_streamed_response_wrapper(
            outages.locations,
        )
