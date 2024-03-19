# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .top import (
    Top,
    AsyncTop,
    TopWithRawResponse,
    AsyncTopWithRawResponse,
    TopWithStreamingResponse,
    AsyncTopWithStreamingResponse,
)
from .leaks import (
    Leaks,
    AsyncLeaks,
    LeaksWithRawResponse,
    AsyncLeaksWithRawResponse,
    LeaksWithStreamingResponse,
    AsyncLeaksWithStreamingResponse,
)
from .routes import (
    Routes,
    AsyncRoutes,
    RoutesWithRawResponse,
    AsyncRoutesWithRawResponse,
    RoutesWithStreamingResponse,
    AsyncRoutesWithStreamingResponse,
)
from .hijacks import (
    Hijacks,
    AsyncHijacks,
    HijacksWithRawResponse,
    AsyncHijacksWithRawResponse,
    HijacksWithStreamingResponse,
    AsyncHijacksWithStreamingResponse,
)
from .top.top import Top, AsyncTop
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
from ....types.radar import BGPTimeseriesResponse, bgp_timeseries_params
from ...._base_client import (
    make_request_options,
)

__all__ = ["BGP", "AsyncBGP"]


class BGP(SyncAPIResource):
    @cached_property
    def leaks(self) -> Leaks:
        return Leaks(self._client)

    @cached_property
    def top(self) -> Top:
        return Top(self._client)

    @cached_property
    def hijacks(self) -> Hijacks:
        return Hijacks(self._client)

    @cached_property
    def routes(self) -> Routes:
        return Routes(self._client)

    @cached_property
    def with_raw_response(self) -> BGPWithRawResponse:
        return BGPWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BGPWithStreamingResponse:
        return BGPWithStreamingResponse(self)

    def timeseries(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        asn: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[
            Literal[
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
        ]
        | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        prefix: List[str] | NotGiven = NOT_GIVEN,
        update_type: List[Literal["ANNOUNCEMENT", "WITHDRAWAL"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BGPTimeseriesResponse:
        """Gets BGP updates change over time.

        Raw values are returned. When requesting
        updates of an autonomous system (AS), only BGP updates of type announcement are
        returned.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          name: Array of names that will be used to name the series in responses.

          prefix: Array of BGP network prefixes.

          update_type: Array of BGP update types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/bgp/timeseries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "asn": asn,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "name": name,
                        "prefix": prefix,
                        "update_type": update_type,
                    },
                    bgp_timeseries_params.BGPTimeseriesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[BGPTimeseriesResponse], ResultWrapper[BGPTimeseriesResponse]),
        )


class AsyncBGP(AsyncAPIResource):
    @cached_property
    def leaks(self) -> AsyncLeaks:
        return AsyncLeaks(self._client)

    @cached_property
    def top(self) -> AsyncTop:
        return AsyncTop(self._client)

    @cached_property
    def hijacks(self) -> AsyncHijacks:
        return AsyncHijacks(self._client)

    @cached_property
    def routes(self) -> AsyncRoutes:
        return AsyncRoutes(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBGPWithRawResponse:
        return AsyncBGPWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBGPWithStreamingResponse:
        return AsyncBGPWithStreamingResponse(self)

    async def timeseries(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        asn: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[
            Literal[
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
        ]
        | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        prefix: List[str] | NotGiven = NOT_GIVEN,
        update_type: List[Literal["ANNOUNCEMENT", "WITHDRAWAL"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BGPTimeseriesResponse:
        """Gets BGP updates change over time.

        Raw values are returned. When requesting
        updates of an autonomous system (AS), only BGP updates of type announcement are
        returned.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          name: Array of names that will be used to name the series in responses.

          prefix: Array of BGP network prefixes.

          update_type: Array of BGP update types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/bgp/timeseries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "asn": asn,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "name": name,
                        "prefix": prefix,
                        "update_type": update_type,
                    },
                    bgp_timeseries_params.BGPTimeseriesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[BGPTimeseriesResponse], ResultWrapper[BGPTimeseriesResponse]),
        )


class BGPWithRawResponse:
    def __init__(self, bgp: BGP) -> None:
        self._bgp = bgp

        self.timeseries = to_raw_response_wrapper(
            bgp.timeseries,
        )

    @cached_property
    def leaks(self) -> LeaksWithRawResponse:
        return LeaksWithRawResponse(self._bgp.leaks)

    @cached_property
    def top(self) -> TopWithRawResponse:
        return TopWithRawResponse(self._bgp.top)

    @cached_property
    def hijacks(self) -> HijacksWithRawResponse:
        return HijacksWithRawResponse(self._bgp.hijacks)

    @cached_property
    def routes(self) -> RoutesWithRawResponse:
        return RoutesWithRawResponse(self._bgp.routes)


class AsyncBGPWithRawResponse:
    def __init__(self, bgp: AsyncBGP) -> None:
        self._bgp = bgp

        self.timeseries = async_to_raw_response_wrapper(
            bgp.timeseries,
        )

    @cached_property
    def leaks(self) -> AsyncLeaksWithRawResponse:
        return AsyncLeaksWithRawResponse(self._bgp.leaks)

    @cached_property
    def top(self) -> AsyncTopWithRawResponse:
        return AsyncTopWithRawResponse(self._bgp.top)

    @cached_property
    def hijacks(self) -> AsyncHijacksWithRawResponse:
        return AsyncHijacksWithRawResponse(self._bgp.hijacks)

    @cached_property
    def routes(self) -> AsyncRoutesWithRawResponse:
        return AsyncRoutesWithRawResponse(self._bgp.routes)


class BGPWithStreamingResponse:
    def __init__(self, bgp: BGP) -> None:
        self._bgp = bgp

        self.timeseries = to_streamed_response_wrapper(
            bgp.timeseries,
        )

    @cached_property
    def leaks(self) -> LeaksWithStreamingResponse:
        return LeaksWithStreamingResponse(self._bgp.leaks)

    @cached_property
    def top(self) -> TopWithStreamingResponse:
        return TopWithStreamingResponse(self._bgp.top)

    @cached_property
    def hijacks(self) -> HijacksWithStreamingResponse:
        return HijacksWithStreamingResponse(self._bgp.hijacks)

    @cached_property
    def routes(self) -> RoutesWithStreamingResponse:
        return RoutesWithStreamingResponse(self._bgp.routes)


class AsyncBGPWithStreamingResponse:
    def __init__(self, bgp: AsyncBGP) -> None:
        self._bgp = bgp

        self.timeseries = async_to_streamed_response_wrapper(
            bgp.timeseries,
        )

    @cached_property
    def leaks(self) -> AsyncLeaksWithStreamingResponse:
        return AsyncLeaksWithStreamingResponse(self._bgp.leaks)

    @cached_property
    def top(self) -> AsyncTopWithStreamingResponse:
        return AsyncTopWithStreamingResponse(self._bgp.top)

    @cached_property
    def hijacks(self) -> AsyncHijacksWithStreamingResponse:
        return AsyncHijacksWithStreamingResponse(self._bgp.hijacks)

    @cached_property
    def routes(self) -> AsyncRoutesWithStreamingResponse:
        return AsyncRoutesWithStreamingResponse(self._bgp.routes)
