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
from ....types.radar.traffic_anomalies import location_get_params
from ....types.radar.traffic_anomalies.location_get_response import LocationGetResponse

__all__ = ["LocationsResource", "AsyncLocationsResource"]


class LocationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LocationsResourceWithRawResponse:
        return LocationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LocationsResourceWithStreamingResponse:
        return LocationsResourceWithStreamingResponse(self)

    def get(
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
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: Literal["VERIFIED", "UNVERIFIED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LocationGetResponse:
        """
        Internet traffic anomalies are signals that might point to an outage, These
        alerts are automatically detected by Radar and then manually verified by our
        team. This endpoint returns the sum of alerts grouped by location.

        Args:
          date_end: End of the date range (inclusive).

          date_range: Shorthand date ranges for the last X days - use when you don't need specific
              start and end dates.

          date_start: Start of the date range (inclusive).

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/traffic_anomalies/locations",
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
                        "status": status,
                    },
                    location_get_params.LocationGetParams,
                ),
                post_parser=ResultWrapper[LocationGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[LocationGetResponse], ResultWrapper[LocationGetResponse]),
        )


class AsyncLocationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLocationsResourceWithRawResponse:
        return AsyncLocationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLocationsResourceWithStreamingResponse:
        return AsyncLocationsResourceWithStreamingResponse(self)

    async def get(
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
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: Literal["VERIFIED", "UNVERIFIED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LocationGetResponse:
        """
        Internet traffic anomalies are signals that might point to an outage, These
        alerts are automatically detected by Radar and then manually verified by our
        team. This endpoint returns the sum of alerts grouped by location.

        Args:
          date_end: End of the date range (inclusive).

          date_range: Shorthand date ranges for the last X days - use when you don't need specific
              start and end dates.

          date_start: Start of the date range (inclusive).

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/traffic_anomalies/locations",
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
                        "status": status,
                    },
                    location_get_params.LocationGetParams,
                ),
                post_parser=ResultWrapper[LocationGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[LocationGetResponse], ResultWrapper[LocationGetResponse]),
        )


class LocationsResourceWithRawResponse:
    def __init__(self, locations: LocationsResource) -> None:
        self._locations = locations

        self.get = to_raw_response_wrapper(
            locations.get,
        )


class AsyncLocationsResourceWithRawResponse:
    def __init__(self, locations: AsyncLocationsResource) -> None:
        self._locations = locations

        self.get = async_to_raw_response_wrapper(
            locations.get,
        )


class LocationsResourceWithStreamingResponse:
    def __init__(self, locations: LocationsResource) -> None:
        self._locations = locations

        self.get = to_streamed_response_wrapper(
            locations.get,
        )


class AsyncLocationsResourceWithStreamingResponse:
    def __init__(self, locations: AsyncLocationsResource) -> None:
        self._locations = locations

        self.get = async_to_streamed_response_wrapper(
            locations.get,
        )
