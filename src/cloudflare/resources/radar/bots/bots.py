# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from .web_crawlers import (
    WebCrawlersResource,
    AsyncWebCrawlersResource,
    WebCrawlersResourceWithRawResponse,
    AsyncWebCrawlersResourceWithRawResponse,
    WebCrawlersResourceWithStreamingResponse,
    AsyncWebCrawlersResourceWithStreamingResponse,
)
from ....types.radar import (
    bot_get_params,
    bot_list_params,
    bot_summary_params,
    bot_timeseries_params,
    bot_timeseries_groups_params,
)
from ...._base_client import make_request_options
from ....types.radar.bot_get_response import BotGetResponse
from ....types.radar.bot_list_response import BotListResponse
from ....types.radar.bot_summary_response import BotSummaryResponse
from ....types.radar.bot_timeseries_response import BotTimeseriesResponse
from ....types.radar.bot_timeseries_groups_response import BotTimeseriesGroupsResponse

__all__ = ["BotsResource", "AsyncBotsResource"]


class BotsResource(SyncAPIResource):
    @cached_property
    def web_crawlers(self) -> WebCrawlersResource:
        return WebCrawlersResource(self._client)

    @cached_property
    def with_raw_response(self) -> BotsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return BotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BotsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return BotsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        bot_category: Literal[
            "SEARCH_ENGINE_CRAWLER",
            "SEARCH_ENGINE_OPTIMIZATION",
            "MONITORING_AND_ANALYTICS",
            "ADVERTISING_AND_MARKETING",
            "SOCIAL_MEDIA_MARKETING",
            "PAGE_PREVIEW",
            "ACADEMIC_RESEARCH",
            "SECURITY",
            "ACCESSIBILITY",
            "WEBHOOKS",
            "FEED_FETCHER",
            "AI_CRAWLER",
            "AGGREGATOR",
            "AI_ASSISTANT",
            "AI_SEARCH",
            "ARCHIVER",
        ]
        | Omit = omit,
        bot_operator: str | Omit = omit,
        bot_verification_status: Literal["VERIFIED"] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        kind: Literal["AGENT", "BOT"] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BotListResponse:
        """
        Retrieves a list of bots.

        Args:
          bot_category: Filters results by bot category.

          bot_operator: Filters results by bot operator.

          bot_verification_status: Filters results by bot verification status.

          format: Format in which results will be returned.

          kind: Filters results by bot kind.

          limit: Limits the number of objects returned in the response.

          offset: Skips the specified number of objects before fetching the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/bots",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "bot_category": bot_category,
                        "bot_operator": bot_operator,
                        "bot_verification_status": bot_verification_status,
                        "format": format,
                        "kind": kind,
                        "limit": limit,
                        "offset": offset,
                    },
                    bot_list_params.BotListParams,
                ),
                post_parser=ResultWrapper[BotListResponse]._unwrapper,
            ),
            cast_to=cast(Type[BotListResponse], ResultWrapper[BotListResponse]),
        )

    def get(
        self,
        bot_slug: str,
        *,
        format: Literal["JSON", "CSV"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BotGetResponse:
        """
        Retrieves the requested bot information.

        Args:
          bot_slug: Bot slug.

          format: Format in which results will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bot_slug:
            raise ValueError(f"Expected a non-empty value for `bot_slug` but received {bot_slug!r}")
        return self._get(
            f"/radar/bots/{bot_slug}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"format": format}, bot_get_params.BotGetParams),
                post_parser=ResultWrapper[BotGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[BotGetResponse], ResultWrapper[BotGetResponse]),
        )

    def summary(
        self,
        dimension: Literal["BOT", "BOT_KIND", "BOT_OPERATOR", "BOT_CATEGORY"],
        *,
        asn: SequenceNotStr[str] | Omit = omit,
        bot: SequenceNotStr[str] | Omit = omit,
        bot_category: List[
            Literal[
                "SEARCH_ENGINE_CRAWLER",
                "SEARCH_ENGINE_OPTIMIZATION",
                "MONITORING_AND_ANALYTICS",
                "ADVERTISING_AND_MARKETING",
                "SOCIAL_MEDIA_MARKETING",
                "PAGE_PREVIEW",
                "ACADEMIC_RESEARCH",
                "SECURITY",
                "ACCESSIBILITY",
                "WEBHOOKS",
                "FEED_FETCHER",
                "AI_CRAWLER",
                "AGGREGATOR",
                "AI_ASSISTANT",
                "AI_SEARCH",
                "ARCHIVER",
            ]
        ]
        | Omit = omit,
        bot_kind: List[Literal["AGENT", "BOT"]] | Omit = omit,
        bot_operator: SequenceNotStr[str] | Omit = omit,
        bot_verification_status: List[Literal["VERIFIED"]] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        limit_per_group: int | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BotSummaryResponse:
        """
        Retrieves an aggregated summary of bots HTTP requests grouped by the specified
        dimension.

        Args:
          dimension: Specifies the attribute by which to group the results.

          asn: Filters results by Autonomous System. Specify one or more Autonomous System
              Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from
              results. For example, `-174, 3356` excludes results from AS174, but includes
              results from AS3356.

          bot: Filters results by bot name.

          bot_category: Filters results by bot category.

          bot_kind: Filters results by bot kind.

          bot_operator: Filters results by bot operator.

          bot_verification_status: Filters results by bot verification status (Verified vs. Unverified).

          continent: Filters results by continent. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude continents from results. For example, `-EU,NA`
              excludes results from EU, but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          limit_per_group: Limits the number of objects per group to the top items within the specified
              time range. When item count exceeds the limit, extra items appear grouped under
              an "other" category.

          location: Filters results by location. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude locations from results. For example, `-US,PT`
              excludes results from the US, but includes results from PT.

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return self._get(
            f"/radar/bots/summary/{dimension}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asn": asn,
                        "bot": bot,
                        "bot_category": bot_category,
                        "bot_kind": bot_kind,
                        "bot_operator": bot_operator,
                        "bot_verification_status": bot_verification_status,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "limit_per_group": limit_per_group,
                        "location": location,
                        "name": name,
                    },
                    bot_summary_params.BotSummaryParams,
                ),
                post_parser=ResultWrapper[BotSummaryResponse]._unwrapper,
            ),
            cast_to=cast(Type[BotSummaryResponse], ResultWrapper[BotSummaryResponse]),
        )

    def timeseries(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        asn: SequenceNotStr[str] | Omit = omit,
        bot: SequenceNotStr[str] | Omit = omit,
        bot_category: List[
            Literal[
                "SEARCH_ENGINE_CRAWLER",
                "SEARCH_ENGINE_OPTIMIZATION",
                "MONITORING_AND_ANALYTICS",
                "ADVERTISING_AND_MARKETING",
                "SOCIAL_MEDIA_MARKETING",
                "PAGE_PREVIEW",
                "ACADEMIC_RESEARCH",
                "SECURITY",
                "ACCESSIBILITY",
                "WEBHOOKS",
                "FEED_FETCHER",
                "AI_CRAWLER",
                "AGGREGATOR",
                "AI_ASSISTANT",
                "AI_SEARCH",
                "ARCHIVER",
            ]
        ]
        | Omit = omit,
        bot_kind: List[Literal["AGENT", "BOT"]] | Omit = omit,
        bot_operator: SequenceNotStr[str] | Omit = omit,
        bot_verification_status: List[Literal["VERIFIED"]] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BotTimeseriesResponse:
        """
        Retrieves bots HTTP request volume over time.

        Args:
          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Filters results by Autonomous System. Specify one or more Autonomous System
              Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from
              results. For example, `-174, 3356` excludes results from AS174, but includes
              results from AS3356.

          bot: Filters results by bot name.

          bot_category: Filters results by bot category.

          bot_kind: Filters results by bot kind.

          bot_operator: Filters results by bot operator.

          bot_verification_status: Filters results by bot verification status (Verified vs. Unverified).

          continent: Filters results by continent. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude continents from results. For example, `-EU,NA`
              excludes results from EU, but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          location: Filters results by location. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude locations from results. For example, `-US,PT`
              excludes results from the US, but includes results from PT.

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/bots/timeseries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "asn": asn,
                        "bot": bot,
                        "bot_category": bot_category,
                        "bot_kind": bot_kind,
                        "bot_operator": bot_operator,
                        "bot_verification_status": bot_verification_status,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "location": location,
                        "name": name,
                    },
                    bot_timeseries_params.BotTimeseriesParams,
                ),
                post_parser=ResultWrapper[BotTimeseriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[BotTimeseriesResponse], ResultWrapper[BotTimeseriesResponse]),
        )

    def timeseries_groups(
        self,
        dimension: Literal["BOT", "BOT_KIND", "BOT_OPERATOR", "BOT_CATEGORY"],
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        asn: SequenceNotStr[str] | Omit = omit,
        bot: SequenceNotStr[str] | Omit = omit,
        bot_category: List[
            Literal[
                "SEARCH_ENGINE_CRAWLER",
                "SEARCH_ENGINE_OPTIMIZATION",
                "MONITORING_AND_ANALYTICS",
                "ADVERTISING_AND_MARKETING",
                "SOCIAL_MEDIA_MARKETING",
                "PAGE_PREVIEW",
                "ACADEMIC_RESEARCH",
                "SECURITY",
                "ACCESSIBILITY",
                "WEBHOOKS",
                "FEED_FETCHER",
                "AI_CRAWLER",
                "AGGREGATOR",
                "AI_ASSISTANT",
                "AI_SEARCH",
                "ARCHIVER",
            ]
        ]
        | Omit = omit,
        bot_kind: List[Literal["AGENT", "BOT"]] | Omit = omit,
        bot_operator: SequenceNotStr[str] | Omit = omit,
        bot_verification_status: List[Literal["VERIFIED"]] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        limit_per_group: int | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BotTimeseriesGroupsResponse:
        """
        Retrieves the distribution of HTTP requests from bots, grouped by chosen the
        specified dimension over time.

        Args:
          dimension: Specifies the attribute by which to group the results.

          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Filters results by Autonomous System. Specify one or more Autonomous System
              Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from
              results. For example, `-174, 3356` excludes results from AS174, but includes
              results from AS3356.

          bot: Filters results by bot name.

          bot_category: Filters results by bot category.

          bot_kind: Filters results by bot kind.

          bot_operator: Filters results by bot operator.

          bot_verification_status: Filters results by bot verification status (Verified vs. Unverified).

          continent: Filters results by continent. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude continents from results. For example, `-EU,NA`
              excludes results from EU, but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          limit_per_group: Limits the number of objects per group to the top items within the specified
              time range. When item count exceeds the limit, extra items appear grouped under
              an "other" category.

          location: Filters results by location. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude locations from results. For example, `-US,PT`
              excludes results from the US, but includes results from PT.

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return self._get(
            f"/radar/bots/timeseries_groups/{dimension}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "asn": asn,
                        "bot": bot,
                        "bot_category": bot_category,
                        "bot_kind": bot_kind,
                        "bot_operator": bot_operator,
                        "bot_verification_status": bot_verification_status,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "limit_per_group": limit_per_group,
                        "location": location,
                        "name": name,
                    },
                    bot_timeseries_groups_params.BotTimeseriesGroupsParams,
                ),
                post_parser=ResultWrapper[BotTimeseriesGroupsResponse]._unwrapper,
            ),
            cast_to=cast(Type[BotTimeseriesGroupsResponse], ResultWrapper[BotTimeseriesGroupsResponse]),
        )


class AsyncBotsResource(AsyncAPIResource):
    @cached_property
    def web_crawlers(self) -> AsyncWebCrawlersResource:
        return AsyncWebCrawlersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBotsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBotsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncBotsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        bot_category: Literal[
            "SEARCH_ENGINE_CRAWLER",
            "SEARCH_ENGINE_OPTIMIZATION",
            "MONITORING_AND_ANALYTICS",
            "ADVERTISING_AND_MARKETING",
            "SOCIAL_MEDIA_MARKETING",
            "PAGE_PREVIEW",
            "ACADEMIC_RESEARCH",
            "SECURITY",
            "ACCESSIBILITY",
            "WEBHOOKS",
            "FEED_FETCHER",
            "AI_CRAWLER",
            "AGGREGATOR",
            "AI_ASSISTANT",
            "AI_SEARCH",
            "ARCHIVER",
        ]
        | Omit = omit,
        bot_operator: str | Omit = omit,
        bot_verification_status: Literal["VERIFIED"] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        kind: Literal["AGENT", "BOT"] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BotListResponse:
        """
        Retrieves a list of bots.

        Args:
          bot_category: Filters results by bot category.

          bot_operator: Filters results by bot operator.

          bot_verification_status: Filters results by bot verification status.

          format: Format in which results will be returned.

          kind: Filters results by bot kind.

          limit: Limits the number of objects returned in the response.

          offset: Skips the specified number of objects before fetching the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/bots",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "bot_category": bot_category,
                        "bot_operator": bot_operator,
                        "bot_verification_status": bot_verification_status,
                        "format": format,
                        "kind": kind,
                        "limit": limit,
                        "offset": offset,
                    },
                    bot_list_params.BotListParams,
                ),
                post_parser=ResultWrapper[BotListResponse]._unwrapper,
            ),
            cast_to=cast(Type[BotListResponse], ResultWrapper[BotListResponse]),
        )

    async def get(
        self,
        bot_slug: str,
        *,
        format: Literal["JSON", "CSV"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BotGetResponse:
        """
        Retrieves the requested bot information.

        Args:
          bot_slug: Bot slug.

          format: Format in which results will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bot_slug:
            raise ValueError(f"Expected a non-empty value for `bot_slug` but received {bot_slug!r}")
        return await self._get(
            f"/radar/bots/{bot_slug}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"format": format}, bot_get_params.BotGetParams),
                post_parser=ResultWrapper[BotGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[BotGetResponse], ResultWrapper[BotGetResponse]),
        )

    async def summary(
        self,
        dimension: Literal["BOT", "BOT_KIND", "BOT_OPERATOR", "BOT_CATEGORY"],
        *,
        asn: SequenceNotStr[str] | Omit = omit,
        bot: SequenceNotStr[str] | Omit = omit,
        bot_category: List[
            Literal[
                "SEARCH_ENGINE_CRAWLER",
                "SEARCH_ENGINE_OPTIMIZATION",
                "MONITORING_AND_ANALYTICS",
                "ADVERTISING_AND_MARKETING",
                "SOCIAL_MEDIA_MARKETING",
                "PAGE_PREVIEW",
                "ACADEMIC_RESEARCH",
                "SECURITY",
                "ACCESSIBILITY",
                "WEBHOOKS",
                "FEED_FETCHER",
                "AI_CRAWLER",
                "AGGREGATOR",
                "AI_ASSISTANT",
                "AI_SEARCH",
                "ARCHIVER",
            ]
        ]
        | Omit = omit,
        bot_kind: List[Literal["AGENT", "BOT"]] | Omit = omit,
        bot_operator: SequenceNotStr[str] | Omit = omit,
        bot_verification_status: List[Literal["VERIFIED"]] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        limit_per_group: int | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BotSummaryResponse:
        """
        Retrieves an aggregated summary of bots HTTP requests grouped by the specified
        dimension.

        Args:
          dimension: Specifies the attribute by which to group the results.

          asn: Filters results by Autonomous System. Specify one or more Autonomous System
              Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from
              results. For example, `-174, 3356` excludes results from AS174, but includes
              results from AS3356.

          bot: Filters results by bot name.

          bot_category: Filters results by bot category.

          bot_kind: Filters results by bot kind.

          bot_operator: Filters results by bot operator.

          bot_verification_status: Filters results by bot verification status (Verified vs. Unverified).

          continent: Filters results by continent. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude continents from results. For example, `-EU,NA`
              excludes results from EU, but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          limit_per_group: Limits the number of objects per group to the top items within the specified
              time range. When item count exceeds the limit, extra items appear grouped under
              an "other" category.

          location: Filters results by location. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude locations from results. For example, `-US,PT`
              excludes results from the US, but includes results from PT.

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return await self._get(
            f"/radar/bots/summary/{dimension}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asn": asn,
                        "bot": bot,
                        "bot_category": bot_category,
                        "bot_kind": bot_kind,
                        "bot_operator": bot_operator,
                        "bot_verification_status": bot_verification_status,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "limit_per_group": limit_per_group,
                        "location": location,
                        "name": name,
                    },
                    bot_summary_params.BotSummaryParams,
                ),
                post_parser=ResultWrapper[BotSummaryResponse]._unwrapper,
            ),
            cast_to=cast(Type[BotSummaryResponse], ResultWrapper[BotSummaryResponse]),
        )

    async def timeseries(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        asn: SequenceNotStr[str] | Omit = omit,
        bot: SequenceNotStr[str] | Omit = omit,
        bot_category: List[
            Literal[
                "SEARCH_ENGINE_CRAWLER",
                "SEARCH_ENGINE_OPTIMIZATION",
                "MONITORING_AND_ANALYTICS",
                "ADVERTISING_AND_MARKETING",
                "SOCIAL_MEDIA_MARKETING",
                "PAGE_PREVIEW",
                "ACADEMIC_RESEARCH",
                "SECURITY",
                "ACCESSIBILITY",
                "WEBHOOKS",
                "FEED_FETCHER",
                "AI_CRAWLER",
                "AGGREGATOR",
                "AI_ASSISTANT",
                "AI_SEARCH",
                "ARCHIVER",
            ]
        ]
        | Omit = omit,
        bot_kind: List[Literal["AGENT", "BOT"]] | Omit = omit,
        bot_operator: SequenceNotStr[str] | Omit = omit,
        bot_verification_status: List[Literal["VERIFIED"]] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BotTimeseriesResponse:
        """
        Retrieves bots HTTP request volume over time.

        Args:
          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Filters results by Autonomous System. Specify one or more Autonomous System
              Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from
              results. For example, `-174, 3356` excludes results from AS174, but includes
              results from AS3356.

          bot: Filters results by bot name.

          bot_category: Filters results by bot category.

          bot_kind: Filters results by bot kind.

          bot_operator: Filters results by bot operator.

          bot_verification_status: Filters results by bot verification status (Verified vs. Unverified).

          continent: Filters results by continent. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude continents from results. For example, `-EU,NA`
              excludes results from EU, but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          location: Filters results by location. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude locations from results. For example, `-US,PT`
              excludes results from the US, but includes results from PT.

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/bots/timeseries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "asn": asn,
                        "bot": bot,
                        "bot_category": bot_category,
                        "bot_kind": bot_kind,
                        "bot_operator": bot_operator,
                        "bot_verification_status": bot_verification_status,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "location": location,
                        "name": name,
                    },
                    bot_timeseries_params.BotTimeseriesParams,
                ),
                post_parser=ResultWrapper[BotTimeseriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[BotTimeseriesResponse], ResultWrapper[BotTimeseriesResponse]),
        )

    async def timeseries_groups(
        self,
        dimension: Literal["BOT", "BOT_KIND", "BOT_OPERATOR", "BOT_CATEGORY"],
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        asn: SequenceNotStr[str] | Omit = omit,
        bot: SequenceNotStr[str] | Omit = omit,
        bot_category: List[
            Literal[
                "SEARCH_ENGINE_CRAWLER",
                "SEARCH_ENGINE_OPTIMIZATION",
                "MONITORING_AND_ANALYTICS",
                "ADVERTISING_AND_MARKETING",
                "SOCIAL_MEDIA_MARKETING",
                "PAGE_PREVIEW",
                "ACADEMIC_RESEARCH",
                "SECURITY",
                "ACCESSIBILITY",
                "WEBHOOKS",
                "FEED_FETCHER",
                "AI_CRAWLER",
                "AGGREGATOR",
                "AI_ASSISTANT",
                "AI_SEARCH",
                "ARCHIVER",
            ]
        ]
        | Omit = omit,
        bot_kind: List[Literal["AGENT", "BOT"]] | Omit = omit,
        bot_operator: SequenceNotStr[str] | Omit = omit,
        bot_verification_status: List[Literal["VERIFIED"]] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        limit_per_group: int | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BotTimeseriesGroupsResponse:
        """
        Retrieves the distribution of HTTP requests from bots, grouped by chosen the
        specified dimension over time.

        Args:
          dimension: Specifies the attribute by which to group the results.

          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Filters results by Autonomous System. Specify one or more Autonomous System
              Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from
              results. For example, `-174, 3356` excludes results from AS174, but includes
              results from AS3356.

          bot: Filters results by bot name.

          bot_category: Filters results by bot category.

          bot_kind: Filters results by bot kind.

          bot_operator: Filters results by bot operator.

          bot_verification_status: Filters results by bot verification status (Verified vs. Unverified).

          continent: Filters results by continent. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude continents from results. For example, `-EU,NA`
              excludes results from EU, but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          limit_per_group: Limits the number of objects per group to the top items within the specified
              time range. When item count exceeds the limit, extra items appear grouped under
              an "other" category.

          location: Filters results by location. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude locations from results. For example, `-US,PT`
              excludes results from the US, but includes results from PT.

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return await self._get(
            f"/radar/bots/timeseries_groups/{dimension}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "asn": asn,
                        "bot": bot,
                        "bot_category": bot_category,
                        "bot_kind": bot_kind,
                        "bot_operator": bot_operator,
                        "bot_verification_status": bot_verification_status,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "limit_per_group": limit_per_group,
                        "location": location,
                        "name": name,
                    },
                    bot_timeseries_groups_params.BotTimeseriesGroupsParams,
                ),
                post_parser=ResultWrapper[BotTimeseriesGroupsResponse]._unwrapper,
            ),
            cast_to=cast(Type[BotTimeseriesGroupsResponse], ResultWrapper[BotTimeseriesGroupsResponse]),
        )


class BotsResourceWithRawResponse:
    def __init__(self, bots: BotsResource) -> None:
        self._bots = bots

        self.list = to_raw_response_wrapper(
            bots.list,
        )
        self.get = to_raw_response_wrapper(
            bots.get,
        )
        self.summary = to_raw_response_wrapper(
            bots.summary,
        )
        self.timeseries = to_raw_response_wrapper(
            bots.timeseries,
        )
        self.timeseries_groups = to_raw_response_wrapper(
            bots.timeseries_groups,
        )

    @cached_property
    def web_crawlers(self) -> WebCrawlersResourceWithRawResponse:
        return WebCrawlersResourceWithRawResponse(self._bots.web_crawlers)


class AsyncBotsResourceWithRawResponse:
    def __init__(self, bots: AsyncBotsResource) -> None:
        self._bots = bots

        self.list = async_to_raw_response_wrapper(
            bots.list,
        )
        self.get = async_to_raw_response_wrapper(
            bots.get,
        )
        self.summary = async_to_raw_response_wrapper(
            bots.summary,
        )
        self.timeseries = async_to_raw_response_wrapper(
            bots.timeseries,
        )
        self.timeseries_groups = async_to_raw_response_wrapper(
            bots.timeseries_groups,
        )

    @cached_property
    def web_crawlers(self) -> AsyncWebCrawlersResourceWithRawResponse:
        return AsyncWebCrawlersResourceWithRawResponse(self._bots.web_crawlers)


class BotsResourceWithStreamingResponse:
    def __init__(self, bots: BotsResource) -> None:
        self._bots = bots

        self.list = to_streamed_response_wrapper(
            bots.list,
        )
        self.get = to_streamed_response_wrapper(
            bots.get,
        )
        self.summary = to_streamed_response_wrapper(
            bots.summary,
        )
        self.timeseries = to_streamed_response_wrapper(
            bots.timeseries,
        )
        self.timeseries_groups = to_streamed_response_wrapper(
            bots.timeseries_groups,
        )

    @cached_property
    def web_crawlers(self) -> WebCrawlersResourceWithStreamingResponse:
        return WebCrawlersResourceWithStreamingResponse(self._bots.web_crawlers)


class AsyncBotsResourceWithStreamingResponse:
    def __init__(self, bots: AsyncBotsResource) -> None:
        self._bots = bots

        self.list = async_to_streamed_response_wrapper(
            bots.list,
        )
        self.get = async_to_streamed_response_wrapper(
            bots.get,
        )
        self.summary = async_to_streamed_response_wrapper(
            bots.summary,
        )
        self.timeseries = async_to_streamed_response_wrapper(
            bots.timeseries,
        )
        self.timeseries_groups = async_to_streamed_response_wrapper(
            bots.timeseries_groups,
        )

    @cached_property
    def web_crawlers(self) -> AsyncWebCrawlersResourceWithStreamingResponse:
        return AsyncWebCrawlersResourceWithStreamingResponse(self._bots.web_crawlers)
