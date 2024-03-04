# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Type, Union, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .domain import (
    Domain,
    AsyncDomain,
    DomainWithRawResponse,
    AsyncDomainWithRawResponse,
    DomainWithStreamingResponse,
    AsyncDomainWithStreamingResponse,
)
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
from ....types.radar import (
    RankingTopResponse,
    RankingTimeseriesGroupsResponse,
    ranking_top_params,
    ranking_timeseries_groups_params,
)
from ...._base_client import (
    make_request_options,
)

__all__ = ["Ranking", "AsyncRanking"]


class Ranking(SyncAPIResource):
    @cached_property
    def domain(self) -> Domain:
        return Domain(self._client)

    @cached_property
    def with_raw_response(self) -> RankingWithRawResponse:
        return RankingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RankingWithStreamingResponse:
        return RankingWithStreamingResponse(self)

    def timeseries_groups(
        self,
        *,
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
        domains: List[str] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        ranking_type: Literal["POPULAR", "TRENDING_RISE", "TRENDING_STEADY"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RankingTimeseriesGroupsResponse:
        """Gets Domains Rank updates change over time.

        Raw values are returned.

        Args:
          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          domains: Array of comma separated list of domains names.

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          location: Array of locations (alpha-2 country codes).

          name: Array of names that will be used to name the series in responses.

          ranking_type: The ranking type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/ranking/timeseries_groups",
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
                        "domains": domains,
                        "format": format,
                        "limit": limit,
                        "location": location,
                        "name": name,
                        "ranking_type": ranking_type,
                    },
                    ranking_timeseries_groups_params.RankingTimeseriesGroupsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RankingTimeseriesGroupsResponse], ResultWrapper[RankingTimeseriesGroupsResponse]),
        )

    def top(
        self,
        *,
        date: List[Optional[str]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        ranking_type: Literal["POPULAR", "TRENDING_RISE", "TRENDING_STEADY"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RankingTopResponse:
        """Get top or trending domains based on their rank.

        Popular domains are domains of
        broad appeal based on how people use the Internet. Trending domains are domains
        that are generating a surge in interest. For more information on top domains,
        see https://blog.cloudflare.com/radar-domain-rankings/.

        Args:
          date: Array of dates to filter the ranking.

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          location: Array of locations (alpha-2 country codes).

          name: Array of names that will be used to name the series in responses.

          ranking_type: The ranking type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/ranking/top",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "format": format,
                        "limit": limit,
                        "location": location,
                        "name": name,
                        "ranking_type": ranking_type,
                    },
                    ranking_top_params.RankingTopParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RankingTopResponse], ResultWrapper[RankingTopResponse]),
        )


class AsyncRanking(AsyncAPIResource):
    @cached_property
    def domain(self) -> AsyncDomain:
        return AsyncDomain(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRankingWithRawResponse:
        return AsyncRankingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRankingWithStreamingResponse:
        return AsyncRankingWithStreamingResponse(self)

    async def timeseries_groups(
        self,
        *,
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
        domains: List[str] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        ranking_type: Literal["POPULAR", "TRENDING_RISE", "TRENDING_STEADY"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RankingTimeseriesGroupsResponse:
        """Gets Domains Rank updates change over time.

        Raw values are returned.

        Args:
          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          domains: Array of comma separated list of domains names.

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          location: Array of locations (alpha-2 country codes).

          name: Array of names that will be used to name the series in responses.

          ranking_type: The ranking type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/ranking/timeseries_groups",
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
                        "domains": domains,
                        "format": format,
                        "limit": limit,
                        "location": location,
                        "name": name,
                        "ranking_type": ranking_type,
                    },
                    ranking_timeseries_groups_params.RankingTimeseriesGroupsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RankingTimeseriesGroupsResponse], ResultWrapper[RankingTimeseriesGroupsResponse]),
        )

    async def top(
        self,
        *,
        date: List[Optional[str]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        ranking_type: Literal["POPULAR", "TRENDING_RISE", "TRENDING_STEADY"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RankingTopResponse:
        """Get top or trending domains based on their rank.

        Popular domains are domains of
        broad appeal based on how people use the Internet. Trending domains are domains
        that are generating a surge in interest. For more information on top domains,
        see https://blog.cloudflare.com/radar-domain-rankings/.

        Args:
          date: Array of dates to filter the ranking.

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          location: Array of locations (alpha-2 country codes).

          name: Array of names that will be used to name the series in responses.

          ranking_type: The ranking type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/ranking/top",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "format": format,
                        "limit": limit,
                        "location": location,
                        "name": name,
                        "ranking_type": ranking_type,
                    },
                    ranking_top_params.RankingTopParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RankingTopResponse], ResultWrapper[RankingTopResponse]),
        )


class RankingWithRawResponse:
    def __init__(self, ranking: Ranking) -> None:
        self._ranking = ranking

        self.timeseries_groups = to_raw_response_wrapper(
            ranking.timeseries_groups,
        )
        self.top = to_raw_response_wrapper(
            ranking.top,
        )

    @cached_property
    def domain(self) -> DomainWithRawResponse:
        return DomainWithRawResponse(self._ranking.domain)


class AsyncRankingWithRawResponse:
    def __init__(self, ranking: AsyncRanking) -> None:
        self._ranking = ranking

        self.timeseries_groups = async_to_raw_response_wrapper(
            ranking.timeseries_groups,
        )
        self.top = async_to_raw_response_wrapper(
            ranking.top,
        )

    @cached_property
    def domain(self) -> AsyncDomainWithRawResponse:
        return AsyncDomainWithRawResponse(self._ranking.domain)


class RankingWithStreamingResponse:
    def __init__(self, ranking: Ranking) -> None:
        self._ranking = ranking

        self.timeseries_groups = to_streamed_response_wrapper(
            ranking.timeseries_groups,
        )
        self.top = to_streamed_response_wrapper(
            ranking.top,
        )

    @cached_property
    def domain(self) -> DomainWithStreamingResponse:
        return DomainWithStreamingResponse(self._ranking.domain)


class AsyncRankingWithStreamingResponse:
    def __init__(self, ranking: AsyncRanking) -> None:
        self._ranking = ranking

        self.timeseries_groups = async_to_streamed_response_wrapper(
            ranking.timeseries_groups,
        )
        self.top = async_to_streamed_response_wrapper(
            ranking.top,
        )

    @cached_property
    def domain(self) -> AsyncDomainWithStreamingResponse:
        return AsyncDomainWithStreamingResponse(self._ranking.domain)
