# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, cast
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
from ...._base_client import make_request_options
from ....types.radar.bots import web_crawler_summary_params, web_crawler_timeseries_groups_params
from ....types.radar.bots.web_crawler_summary_response import WebCrawlerSummaryResponse
from ....types.radar.bots.web_crawler_timeseries_groups_response import WebCrawlerTimeseriesGroupsResponse

__all__ = ["WebCrawlersResource", "AsyncWebCrawlersResource"]


class WebCrawlersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WebCrawlersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return WebCrawlersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebCrawlersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return WebCrawlersResourceWithStreamingResponse(self)

    def summary(
        self,
        dimension: Literal["USER_AGENT", "REFERER", "CRAWL_REFER_RATIO", "VERTICAL", "INDUSTRY"],
        *,
        bot_operator: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        industry: SequenceNotStr[str] | Omit = omit,
        limit_per_group: int | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        vertical: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebCrawlerSummaryResponse:
        """
        Retrieves an aggregated summary of HTTP requests from crawlers, grouped by the
        specified dimension.

        Args:
          dimension: Specifies the attribute by which to group the results.

          bot_operator: Filters results by bot operator.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          industry: Filters results by industry.

          limit_per_group: Limits the number of objects per group to the top items within the specified
              time range. When item count exceeds the limit, extra items appear grouped under
              an "other" category.

          name: Array of names used to label the series in the response.

          vertical: Filters results by vertical.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return self._get(
            f"/radar/bots/crawlers/summary/{dimension}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "bot_operator": bot_operator,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "industry": industry,
                        "limit_per_group": limit_per_group,
                        "name": name,
                        "vertical": vertical,
                    },
                    web_crawler_summary_params.WebCrawlerSummaryParams,
                ),
                post_parser=ResultWrapper[WebCrawlerSummaryResponse]._unwrapper,
            ),
            cast_to=cast(Type[WebCrawlerSummaryResponse], ResultWrapper[WebCrawlerSummaryResponse]),
        )

    def timeseries_groups(
        self,
        dimension: Literal["USER_AGENT", "REFERER", "CRAWL_REFER_RATIO", "VERTICAL", "INDUSTRY"],
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        bot_operator: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        industry: SequenceNotStr[str] | Omit = omit,
        limit_per_group: int | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        vertical: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebCrawlerTimeseriesGroupsResponse:
        """
        Retrieves the distribution of HTTP requests from crawlers, grouped by chosen the
        specified dimension over time.

        Args:
          dimension: Specifies the attribute by which to group the results.

          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          bot_operator: Filters results by bot operator.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          industry: Filters results by industry.

          limit_per_group: Limits the number of objects per group to the top items within the specified
              time range. When item count exceeds the limit, extra items appear grouped under
              an "other" category.

          name: Array of names used to label the series in the response.

          vertical: Filters results by vertical.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return self._get(
            f"/radar/bots/crawlers/timeseries_groups/{dimension}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "bot_operator": bot_operator,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "industry": industry,
                        "limit_per_group": limit_per_group,
                        "name": name,
                        "vertical": vertical,
                    },
                    web_crawler_timeseries_groups_params.WebCrawlerTimeseriesGroupsParams,
                ),
                post_parser=ResultWrapper[WebCrawlerTimeseriesGroupsResponse]._unwrapper,
            ),
            cast_to=cast(Type[WebCrawlerTimeseriesGroupsResponse], ResultWrapper[WebCrawlerTimeseriesGroupsResponse]),
        )


class AsyncWebCrawlersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWebCrawlersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWebCrawlersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebCrawlersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncWebCrawlersResourceWithStreamingResponse(self)

    async def summary(
        self,
        dimension: Literal["USER_AGENT", "REFERER", "CRAWL_REFER_RATIO", "VERTICAL", "INDUSTRY"],
        *,
        bot_operator: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        industry: SequenceNotStr[str] | Omit = omit,
        limit_per_group: int | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        vertical: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebCrawlerSummaryResponse:
        """
        Retrieves an aggregated summary of HTTP requests from crawlers, grouped by the
        specified dimension.

        Args:
          dimension: Specifies the attribute by which to group the results.

          bot_operator: Filters results by bot operator.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          industry: Filters results by industry.

          limit_per_group: Limits the number of objects per group to the top items within the specified
              time range. When item count exceeds the limit, extra items appear grouped under
              an "other" category.

          name: Array of names used to label the series in the response.

          vertical: Filters results by vertical.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return await self._get(
            f"/radar/bots/crawlers/summary/{dimension}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "bot_operator": bot_operator,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "industry": industry,
                        "limit_per_group": limit_per_group,
                        "name": name,
                        "vertical": vertical,
                    },
                    web_crawler_summary_params.WebCrawlerSummaryParams,
                ),
                post_parser=ResultWrapper[WebCrawlerSummaryResponse]._unwrapper,
            ),
            cast_to=cast(Type[WebCrawlerSummaryResponse], ResultWrapper[WebCrawlerSummaryResponse]),
        )

    async def timeseries_groups(
        self,
        dimension: Literal["USER_AGENT", "REFERER", "CRAWL_REFER_RATIO", "VERTICAL", "INDUSTRY"],
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        bot_operator: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        industry: SequenceNotStr[str] | Omit = omit,
        limit_per_group: int | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        vertical: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebCrawlerTimeseriesGroupsResponse:
        """
        Retrieves the distribution of HTTP requests from crawlers, grouped by chosen the
        specified dimension over time.

        Args:
          dimension: Specifies the attribute by which to group the results.

          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          bot_operator: Filters results by bot operator.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          industry: Filters results by industry.

          limit_per_group: Limits the number of objects per group to the top items within the specified
              time range. When item count exceeds the limit, extra items appear grouped under
              an "other" category.

          name: Array of names used to label the series in the response.

          vertical: Filters results by vertical.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return await self._get(
            f"/radar/bots/crawlers/timeseries_groups/{dimension}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "bot_operator": bot_operator,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "industry": industry,
                        "limit_per_group": limit_per_group,
                        "name": name,
                        "vertical": vertical,
                    },
                    web_crawler_timeseries_groups_params.WebCrawlerTimeseriesGroupsParams,
                ),
                post_parser=ResultWrapper[WebCrawlerTimeseriesGroupsResponse]._unwrapper,
            ),
            cast_to=cast(Type[WebCrawlerTimeseriesGroupsResponse], ResultWrapper[WebCrawlerTimeseriesGroupsResponse]),
        )


class WebCrawlersResourceWithRawResponse:
    def __init__(self, web_crawlers: WebCrawlersResource) -> None:
        self._web_crawlers = web_crawlers

        self.summary = to_raw_response_wrapper(
            web_crawlers.summary,
        )
        self.timeseries_groups = to_raw_response_wrapper(
            web_crawlers.timeseries_groups,
        )


class AsyncWebCrawlersResourceWithRawResponse:
    def __init__(self, web_crawlers: AsyncWebCrawlersResource) -> None:
        self._web_crawlers = web_crawlers

        self.summary = async_to_raw_response_wrapper(
            web_crawlers.summary,
        )
        self.timeseries_groups = async_to_raw_response_wrapper(
            web_crawlers.timeseries_groups,
        )


class WebCrawlersResourceWithStreamingResponse:
    def __init__(self, web_crawlers: WebCrawlersResource) -> None:
        self._web_crawlers = web_crawlers

        self.summary = to_streamed_response_wrapper(
            web_crawlers.summary,
        )
        self.timeseries_groups = to_streamed_response_wrapper(
            web_crawlers.timeseries_groups,
        )


class AsyncWebCrawlersResourceWithStreamingResponse:
    def __init__(self, web_crawlers: AsyncWebCrawlersResource) -> None:
        self._web_crawlers = web_crawlers

        self.summary = async_to_streamed_response_wrapper(
            web_crawlers.summary,
        )
        self.timeseries_groups = async_to_streamed_response_wrapper(
            web_crawlers.timeseries_groups,
        )
