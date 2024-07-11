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
from .locations import (
    LocationsResource,
    AsyncLocationsResource,
    LocationsResourceWithRawResponse,
    AsyncLocationsResourceWithRawResponse,
    LocationsResourceWithStreamingResponse,
    AsyncLocationsResourceWithStreamingResponse,
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
from ....types.radar import traffic_anomaly_get_params
from ...._base_client import make_request_options
from ....types.radar.traffic_anomaly_get_response import TrafficAnomalyGetResponse

__all__ = ["TrafficAnomaliesResource", "AsyncTrafficAnomaliesResource"]


class TrafficAnomaliesResource(SyncAPIResource):
    @cached_property
    def locations(self) -> LocationsResource:
        return LocationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TrafficAnomaliesResourceWithRawResponse:
        return TrafficAnomaliesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrafficAnomaliesResourceWithStreamingResponse:
        return TrafficAnomaliesResourceWithStreamingResponse(self)

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
        status: Literal["VERIFIED", "UNVERIFIED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrafficAnomalyGetResponse:
        """
        Internet traffic anomalies are signals that might point to an outage, These
        alerts are automatically detected by Radar and then manually verified by our
        team. This endpoint returns the latest alerts.

        Args:
          asn: Single ASN as integer.

          date_end: End of the date range (inclusive).

          date_range: Shorthand date ranges for the last X days - use when you don't need specific
              start and end dates.

          date_start: Start of the date range (inclusive).

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          location: Location Alpha2 code.

          offset: Number of objects to skip before grabbing results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/traffic_anomalies",
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
                        "status": status,
                    },
                    traffic_anomaly_get_params.TrafficAnomalyGetParams,
                ),
                post_parser=ResultWrapper[TrafficAnomalyGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[TrafficAnomalyGetResponse], ResultWrapper[TrafficAnomalyGetResponse]),
        )


class AsyncTrafficAnomaliesResource(AsyncAPIResource):
    @cached_property
    def locations(self) -> AsyncLocationsResource:
        return AsyncLocationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTrafficAnomaliesResourceWithRawResponse:
        return AsyncTrafficAnomaliesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrafficAnomaliesResourceWithStreamingResponse:
        return AsyncTrafficAnomaliesResourceWithStreamingResponse(self)

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
        status: Literal["VERIFIED", "UNVERIFIED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrafficAnomalyGetResponse:
        """
        Internet traffic anomalies are signals that might point to an outage, These
        alerts are automatically detected by Radar and then manually verified by our
        team. This endpoint returns the latest alerts.

        Args:
          asn: Single ASN as integer.

          date_end: End of the date range (inclusive).

          date_range: Shorthand date ranges for the last X days - use when you don't need specific
              start and end dates.

          date_start: Start of the date range (inclusive).

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          location: Location Alpha2 code.

          offset: Number of objects to skip before grabbing results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/traffic_anomalies",
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
                        "status": status,
                    },
                    traffic_anomaly_get_params.TrafficAnomalyGetParams,
                ),
                post_parser=ResultWrapper[TrafficAnomalyGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[TrafficAnomalyGetResponse], ResultWrapper[TrafficAnomalyGetResponse]),
        )


class TrafficAnomaliesResourceWithRawResponse:
    def __init__(self, traffic_anomalies: TrafficAnomaliesResource) -> None:
        self._traffic_anomalies = traffic_anomalies

        self.get = to_raw_response_wrapper(
            traffic_anomalies.get,
        )

    @cached_property
    def locations(self) -> LocationsResourceWithRawResponse:
        return LocationsResourceWithRawResponse(self._traffic_anomalies.locations)


class AsyncTrafficAnomaliesResourceWithRawResponse:
    def __init__(self, traffic_anomalies: AsyncTrafficAnomaliesResource) -> None:
        self._traffic_anomalies = traffic_anomalies

        self.get = async_to_raw_response_wrapper(
            traffic_anomalies.get,
        )

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithRawResponse:
        return AsyncLocationsResourceWithRawResponse(self._traffic_anomalies.locations)


class TrafficAnomaliesResourceWithStreamingResponse:
    def __init__(self, traffic_anomalies: TrafficAnomaliesResource) -> None:
        self._traffic_anomalies = traffic_anomalies

        self.get = to_streamed_response_wrapper(
            traffic_anomalies.get,
        )

    @cached_property
    def locations(self) -> LocationsResourceWithStreamingResponse:
        return LocationsResourceWithStreamingResponse(self._traffic_anomalies.locations)


class AsyncTrafficAnomaliesResourceWithStreamingResponse:
    def __init__(self, traffic_anomalies: AsyncTrafficAnomaliesResource) -> None:
        self._traffic_anomalies = traffic_anomalies

        self.get = async_to_streamed_response_wrapper(
            traffic_anomalies.get,
        )

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithStreamingResponse:
        return AsyncLocationsResourceWithStreamingResponse(self._traffic_anomalies.locations)
