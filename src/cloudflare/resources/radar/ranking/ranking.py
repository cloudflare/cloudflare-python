# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, cast
from datetime import date, datetime
from typing_extensions import Literal

import httpx

from .domain import (
    DomainResource,
    AsyncDomainResource,
    DomainResourceWithRawResponse,
    AsyncDomainResourceWithRawResponse,
    DomainResourceWithStreamingResponse,
    AsyncDomainResourceWithStreamingResponse,
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
from ....types.radar import ranking_top_params, ranking_timeseries_groups_params
from ...._base_client import make_request_options
from .internet_services import (
    InternetServicesResource,
    AsyncInternetServicesResource,
    InternetServicesResourceWithRawResponse,
    AsyncInternetServicesResourceWithRawResponse,
    InternetServicesResourceWithStreamingResponse,
    AsyncInternetServicesResourceWithStreamingResponse,
)
from ....types.radar.ranking_top_response import RankingTopResponse
from ....types.radar.ranking_timeseries_groups_response import RankingTimeseriesGroupsResponse

__all__ = ["RankingResource", "AsyncRankingResource"]


class RankingResource(SyncAPIResource):
    @cached_property
    def domain(self) -> DomainResource:
        return DomainResource(self._client)

    @cached_property
    def internet_services(self) -> InternetServicesResource:
        return InternetServicesResource(self._client)

    @cached_property
    def with_raw_response(self) -> RankingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RankingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RankingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RankingResourceWithStreamingResponse(self)

    def timeseries_groups(
        self,
        *,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        domain_category: List[str] | NotGiven = NOT_GIVEN,
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
        """
        Retrieves domains rank over time.

        Args:
          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          domain_category: Filters results by domain category.

          domains: Comma-separated list of domain names.

          format: Format in which results will be returned.

          limit: Limits the number of objects returned in the response.

          location: Comma-separated list of locations (alpha-2 codes).

          name: Array of names used to label the series in the response.

          ranking_type: Ranking type.

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
                        "domain_category": domain_category,
                        "domains": domains,
                        "format": format,
                        "limit": limit,
                        "location": location,
                        "name": name,
                        "ranking_type": ranking_type,
                    },
                    ranking_timeseries_groups_params.RankingTimeseriesGroupsParams,
                ),
                post_parser=ResultWrapper[RankingTimeseriesGroupsResponse]._unwrapper,
            ),
            cast_to=cast(Type[RankingTimeseriesGroupsResponse], ResultWrapper[RankingTimeseriesGroupsResponse]),
        )

    def top(
        self,
        *,
        date: List[Union[str, date]] | NotGiven = NOT_GIVEN,
        domain_category: List[str] | NotGiven = NOT_GIVEN,
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
        """Retrieves the top or trending domains based on their rank.

        Popular domains are
        domains of broad appeal based on how people use the Internet. Trending domains
        are domains that are generating a surge in interest. For more information on top
        domains, see https://blog.cloudflare.com/radar-domain-rankings/.

        Args:
          date: Array of dates to filter the results.

          domain_category: Filters results by domain category.

          format: Format in which results will be returned.

          limit: Limits the number of objects returned in the response.

          location: Comma-separated list of locations (alpha-2 codes).

          name: Array of names used to label the series in the response.

          ranking_type: Ranking type.

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
                        "domain_category": domain_category,
                        "format": format,
                        "limit": limit,
                        "location": location,
                        "name": name,
                        "ranking_type": ranking_type,
                    },
                    ranking_top_params.RankingTopParams,
                ),
                post_parser=ResultWrapper[RankingTopResponse]._unwrapper,
            ),
            cast_to=cast(Type[RankingTopResponse], ResultWrapper[RankingTopResponse]),
        )


class AsyncRankingResource(AsyncAPIResource):
    @cached_property
    def domain(self) -> AsyncDomainResource:
        return AsyncDomainResource(self._client)

    @cached_property
    def internet_services(self) -> AsyncInternetServicesResource:
        return AsyncInternetServicesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRankingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRankingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRankingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRankingResourceWithStreamingResponse(self)

    async def timeseries_groups(
        self,
        *,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        domain_category: List[str] | NotGiven = NOT_GIVEN,
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
        """
        Retrieves domains rank over time.

        Args:
          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          domain_category: Filters results by domain category.

          domains: Comma-separated list of domain names.

          format: Format in which results will be returned.

          limit: Limits the number of objects returned in the response.

          location: Comma-separated list of locations (alpha-2 codes).

          name: Array of names used to label the series in the response.

          ranking_type: Ranking type.

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
                        "domain_category": domain_category,
                        "domains": domains,
                        "format": format,
                        "limit": limit,
                        "location": location,
                        "name": name,
                        "ranking_type": ranking_type,
                    },
                    ranking_timeseries_groups_params.RankingTimeseriesGroupsParams,
                ),
                post_parser=ResultWrapper[RankingTimeseriesGroupsResponse]._unwrapper,
            ),
            cast_to=cast(Type[RankingTimeseriesGroupsResponse], ResultWrapper[RankingTimeseriesGroupsResponse]),
        )

    async def top(
        self,
        *,
        date: List[Union[str, date]] | NotGiven = NOT_GIVEN,
        domain_category: List[str] | NotGiven = NOT_GIVEN,
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
        """Retrieves the top or trending domains based on their rank.

        Popular domains are
        domains of broad appeal based on how people use the Internet. Trending domains
        are domains that are generating a surge in interest. For more information on top
        domains, see https://blog.cloudflare.com/radar-domain-rankings/.

        Args:
          date: Array of dates to filter the results.

          domain_category: Filters results by domain category.

          format: Format in which results will be returned.

          limit: Limits the number of objects returned in the response.

          location: Comma-separated list of locations (alpha-2 codes).

          name: Array of names used to label the series in the response.

          ranking_type: Ranking type.

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
                        "domain_category": domain_category,
                        "format": format,
                        "limit": limit,
                        "location": location,
                        "name": name,
                        "ranking_type": ranking_type,
                    },
                    ranking_top_params.RankingTopParams,
                ),
                post_parser=ResultWrapper[RankingTopResponse]._unwrapper,
            ),
            cast_to=cast(Type[RankingTopResponse], ResultWrapper[RankingTopResponse]),
        )


class RankingResourceWithRawResponse:
    def __init__(self, ranking: RankingResource) -> None:
        self._ranking = ranking

        self.timeseries_groups = to_raw_response_wrapper(
            ranking.timeseries_groups,
        )
        self.top = to_raw_response_wrapper(
            ranking.top,
        )

    @cached_property
    def domain(self) -> DomainResourceWithRawResponse:
        return DomainResourceWithRawResponse(self._ranking.domain)

    @cached_property
    def internet_services(self) -> InternetServicesResourceWithRawResponse:
        return InternetServicesResourceWithRawResponse(self._ranking.internet_services)


class AsyncRankingResourceWithRawResponse:
    def __init__(self, ranking: AsyncRankingResource) -> None:
        self._ranking = ranking

        self.timeseries_groups = async_to_raw_response_wrapper(
            ranking.timeseries_groups,
        )
        self.top = async_to_raw_response_wrapper(
            ranking.top,
        )

    @cached_property
    def domain(self) -> AsyncDomainResourceWithRawResponse:
        return AsyncDomainResourceWithRawResponse(self._ranking.domain)

    @cached_property
    def internet_services(self) -> AsyncInternetServicesResourceWithRawResponse:
        return AsyncInternetServicesResourceWithRawResponse(self._ranking.internet_services)


class RankingResourceWithStreamingResponse:
    def __init__(self, ranking: RankingResource) -> None:
        self._ranking = ranking

        self.timeseries_groups = to_streamed_response_wrapper(
            ranking.timeseries_groups,
        )
        self.top = to_streamed_response_wrapper(
            ranking.top,
        )

    @cached_property
    def domain(self) -> DomainResourceWithStreamingResponse:
        return DomainResourceWithStreamingResponse(self._ranking.domain)

    @cached_property
    def internet_services(self) -> InternetServicesResourceWithStreamingResponse:
        return InternetServicesResourceWithStreamingResponse(self._ranking.internet_services)


class AsyncRankingResourceWithStreamingResponse:
    def __init__(self, ranking: AsyncRankingResource) -> None:
        self._ranking = ranking

        self.timeseries_groups = async_to_streamed_response_wrapper(
            ranking.timeseries_groups,
        )
        self.top = async_to_streamed_response_wrapper(
            ranking.top,
        )

    @cached_property
    def domain(self) -> AsyncDomainResourceWithStreamingResponse:
        return AsyncDomainResourceWithStreamingResponse(self._ranking.domain)

    @cached_property
    def internet_services(self) -> AsyncInternetServicesResourceWithStreamingResponse:
        return AsyncInternetServicesResourceWithStreamingResponse(self._ranking.internet_services)
