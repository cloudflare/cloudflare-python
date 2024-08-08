# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .top import (
    TopResource,
    AsyncTopResource,
    TopResourceWithRawResponse,
    AsyncTopResourceWithRawResponse,
    TopResourceWithStreamingResponse,
    AsyncTopResourceWithStreamingResponse,
)
from .ases import (
    AsesResource,
    AsyncAsesResource,
    AsesResourceWithRawResponse,
    AsyncAsesResourceWithRawResponse,
    AsesResourceWithStreamingResponse,
    AsyncAsesResourceWithStreamingResponse,
)
from .summary import (
    SummaryResource,
    AsyncSummaryResource,
    SummaryResourceWithRawResponse,
    AsyncSummaryResourceWithRawResponse,
    SummaryResourceWithStreamingResponse,
    AsyncSummaryResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .ases.ases import AsesResource, AsyncAsesResource
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
from ....types.radar import http_timeseries_params
from ...._base_client import make_request_options
from .timeseries_groups import (
    TimeseriesGroupsResource,
    AsyncTimeseriesGroupsResource,
    TimeseriesGroupsResourceWithRawResponse,
    AsyncTimeseriesGroupsResourceWithRawResponse,
    TimeseriesGroupsResourceWithStreamingResponse,
    AsyncTimeseriesGroupsResourceWithStreamingResponse,
)
from .locations.locations import LocationsResource, AsyncLocationsResource
from ....types.radar.http_timeseries_response import HTTPTimeseriesResponse

__all__ = ["HTTPResource", "AsyncHTTPResource"]


class HTTPResource(SyncAPIResource):
    @cached_property
    def locations(self) -> LocationsResource:
        return LocationsResource(self._client)

    @cached_property
    def ases(self) -> AsesResource:
        return AsesResource(self._client)

    @cached_property
    def summary(self) -> SummaryResource:
        return SummaryResource(self._client)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResource:
        return TimeseriesGroupsResource(self._client)

    @cached_property
    def top(self) -> TopResource:
        return TopResource(self._client)

    @cached_property
    def with_raw_response(self) -> HTTPResourceWithRawResponse:
        return HTTPResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HTTPResourceWithStreamingResponse:
        return HTTPResourceWithStreamingResponse(self)

    def timeseries(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        normalization: Literal["PERCENTAGE_CHANGE", "MIN0_MAX"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HTTPTimeseriesResponse:
        """
        Get HTTP requests over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          normalization: Normalization method applied. Refer to
              [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/http/timeseries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "asn": asn,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "location": location,
                        "name": name,
                        "normalization": normalization,
                    },
                    http_timeseries_params.HTTPTimeseriesParams,
                ),
                post_parser=ResultWrapper[HTTPTimeseriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[HTTPTimeseriesResponse], ResultWrapper[HTTPTimeseriesResponse]),
        )


class AsyncHTTPResource(AsyncAPIResource):
    @cached_property
    def locations(self) -> AsyncLocationsResource:
        return AsyncLocationsResource(self._client)

    @cached_property
    def ases(self) -> AsyncAsesResource:
        return AsyncAsesResource(self._client)

    @cached_property
    def summary(self) -> AsyncSummaryResource:
        return AsyncSummaryResource(self._client)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResource:
        return AsyncTimeseriesGroupsResource(self._client)

    @cached_property
    def top(self) -> AsyncTopResource:
        return AsyncTopResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHTTPResourceWithRawResponse:
        return AsyncHTTPResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHTTPResourceWithStreamingResponse:
        return AsyncHTTPResourceWithStreamingResponse(self)

    async def timeseries(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        normalization: Literal["PERCENTAGE_CHANGE", "MIN0_MAX"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HTTPTimeseriesResponse:
        """
        Get HTTP requests over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          normalization: Normalization method applied. Refer to
              [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/http/timeseries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "asn": asn,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "location": location,
                        "name": name,
                        "normalization": normalization,
                    },
                    http_timeseries_params.HTTPTimeseriesParams,
                ),
                post_parser=ResultWrapper[HTTPTimeseriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[HTTPTimeseriesResponse], ResultWrapper[HTTPTimeseriesResponse]),
        )


class HTTPResourceWithRawResponse:
    def __init__(self, http: HTTPResource) -> None:
        self._http = http

        self.timeseries = to_raw_response_wrapper(
            http.timeseries,
        )

    @cached_property
    def locations(self) -> LocationsResourceWithRawResponse:
        return LocationsResourceWithRawResponse(self._http.locations)

    @cached_property
    def ases(self) -> AsesResourceWithRawResponse:
        return AsesResourceWithRawResponse(self._http.ases)

    @cached_property
    def summary(self) -> SummaryResourceWithRawResponse:
        return SummaryResourceWithRawResponse(self._http.summary)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResourceWithRawResponse:
        return TimeseriesGroupsResourceWithRawResponse(self._http.timeseries_groups)

    @cached_property
    def top(self) -> TopResourceWithRawResponse:
        return TopResourceWithRawResponse(self._http.top)


class AsyncHTTPResourceWithRawResponse:
    def __init__(self, http: AsyncHTTPResource) -> None:
        self._http = http

        self.timeseries = async_to_raw_response_wrapper(
            http.timeseries,
        )

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithRawResponse:
        return AsyncLocationsResourceWithRawResponse(self._http.locations)

    @cached_property
    def ases(self) -> AsyncAsesResourceWithRawResponse:
        return AsyncAsesResourceWithRawResponse(self._http.ases)

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithRawResponse:
        return AsyncSummaryResourceWithRawResponse(self._http.summary)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResourceWithRawResponse:
        return AsyncTimeseriesGroupsResourceWithRawResponse(self._http.timeseries_groups)

    @cached_property
    def top(self) -> AsyncTopResourceWithRawResponse:
        return AsyncTopResourceWithRawResponse(self._http.top)


class HTTPResourceWithStreamingResponse:
    def __init__(self, http: HTTPResource) -> None:
        self._http = http

        self.timeseries = to_streamed_response_wrapper(
            http.timeseries,
        )

    @cached_property
    def locations(self) -> LocationsResourceWithStreamingResponse:
        return LocationsResourceWithStreamingResponse(self._http.locations)

    @cached_property
    def ases(self) -> AsesResourceWithStreamingResponse:
        return AsesResourceWithStreamingResponse(self._http.ases)

    @cached_property
    def summary(self) -> SummaryResourceWithStreamingResponse:
        return SummaryResourceWithStreamingResponse(self._http.summary)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResourceWithStreamingResponse:
        return TimeseriesGroupsResourceWithStreamingResponse(self._http.timeseries_groups)

    @cached_property
    def top(self) -> TopResourceWithStreamingResponse:
        return TopResourceWithStreamingResponse(self._http.top)


class AsyncHTTPResourceWithStreamingResponse:
    def __init__(self, http: AsyncHTTPResource) -> None:
        self._http = http

        self.timeseries = async_to_streamed_response_wrapper(
            http.timeseries,
        )

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithStreamingResponse:
        return AsyncLocationsResourceWithStreamingResponse(self._http.locations)

    @cached_property
    def ases(self) -> AsyncAsesResourceWithStreamingResponse:
        return AsyncAsesResourceWithStreamingResponse(self._http.ases)

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithStreamingResponse:
        return AsyncSummaryResourceWithStreamingResponse(self._http.summary)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResourceWithStreamingResponse:
        return AsyncTimeseriesGroupsResourceWithStreamingResponse(self._http.timeseries_groups)

    @cached_property
    def top(self) -> AsyncTopResourceWithStreamingResponse:
        return AsyncTopResourceWithStreamingResponse(self._http.top)
