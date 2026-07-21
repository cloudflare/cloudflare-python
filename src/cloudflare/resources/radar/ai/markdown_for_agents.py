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
from ....types.radar.ai import markdown_for_agent_summary_params, markdown_for_agent_timeseries_params
from ....types.radar.ai.markdown_for_agent_summary_response import MarkdownForAgentSummaryResponse
from ....types.radar.ai.markdown_for_agent_timeseries_response import MarkdownForAgentTimeseriesResponse

__all__ = ["MarkdownForAgentsResource", "AsyncMarkdownForAgentsResource"]


class MarkdownForAgentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MarkdownForAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return MarkdownForAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MarkdownForAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return MarkdownForAgentsResourceWithStreamingResponse(self)

    def summary(
        self,
        *,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarkdownForAgentSummaryResponse:
        """
        Retrieves the overall median HTML-to-markdown reduction ratio for AI agent
        requests over the given date range.

        Args:
          date_end: End of the date range (inclusive). Alternative to `dateRange`; provide together
              with `dateStart`. When requesting comparison series, every series must resolve
              to the same duration as the main series. Each `dateStart`/`dateEnd` is floored
              to the nearest 15 minutes before evaluation, so windows whose durations match
              only before alignment may be rejected.

          date_range: Filters results by relative date range ending at the current time, with each
              value producing a separate series. Use `<n>d` for days (up to `364d`) or `<n>w`
              for weeks (up to `52w`). Append `control` to request the equivalent previous
              period for comparison: the comparison window is shifted back by the current
              window's length rounded up to a whole number of weeks, so it keeps the same
              weekday alignment and does not overlap the current window (e.g. `7dcontrol`
              covers days -14 to -7, `10dcontrol` covers days -24 to -14). For example, pass
              `7d` and `7dcontrol` to compare this week with the previous week. All series
              must resolve to the same duration as the main series; relative ranges (including
              `control`) satisfy this automatically. Use this parameter or set specific start
              and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range. Alternative to `dateRange`; provide together with
              `dateEnd`. When requesting comparison series, every series must resolve to the
              same duration as the main series. Each `dateStart`/`dateEnd` is floored to the
              nearest 15 minutes before evaluation, so windows whose durations match only
              before alignment may be rejected.

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/ai/markdown_for_agents/summary",
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
                        "name": name,
                    },
                    markdown_for_agent_summary_params.MarkdownForAgentSummaryParams,
                ),
                post_parser=ResultWrapper[MarkdownForAgentSummaryResponse]._unwrapper,
            ),
            cast_to=cast(Type[MarkdownForAgentSummaryResponse], ResultWrapper[MarkdownForAgentSummaryResponse]),
        )

    def timeseries(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarkdownForAgentTimeseriesResponse:
        """
        Retrieves the median HTML-to-markdown reduction ratio over time for AI agent
        requests.

        Args:
          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).
              When omitted, the interval is auto-selected from the requested date range; finer
              intervals are only available for shorter ranges. If the requested interval is
              too granular for the date range, the request is rejected.

          date_end: End of the date range (inclusive). Alternative to `dateRange`; provide together
              with `dateStart`. When requesting comparison series, every series must resolve
              to the same duration as the main series. Each `dateStart`/`dateEnd` is floored
              to the nearest 15 minutes before evaluation, so windows whose durations match
              only before alignment may be rejected.

          date_range: Filters results by relative date range ending at the current time, with each
              value producing a separate series. Use `<n>d` for days (up to `364d`) or `<n>w`
              for weeks (up to `52w`). Append `control` to request the equivalent previous
              period for comparison: the comparison window is shifted back by the current
              window's length rounded up to a whole number of weeks, so it keeps the same
              weekday alignment and does not overlap the current window (e.g. `7dcontrol`
              covers days -14 to -7, `10dcontrol` covers days -24 to -14). For example, pass
              `7d` and `7dcontrol` to compare this week with the previous week. All series
              must resolve to the same duration as the main series; relative ranges (including
              `control`) satisfy this automatically. Use this parameter or set specific start
              and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range. Alternative to `dateRange`; provide together with
              `dateEnd`. When requesting comparison series, every series must resolve to the
              same duration as the main series. Each `dateStart`/`dateEnd` is floored to the
              nearest 15 minutes before evaluation, so windows whose durations match only
              before alignment may be rejected.

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/ai/markdown_for_agents/timeseries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "name": name,
                    },
                    markdown_for_agent_timeseries_params.MarkdownForAgentTimeseriesParams,
                ),
                post_parser=ResultWrapper[MarkdownForAgentTimeseriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[MarkdownForAgentTimeseriesResponse], ResultWrapper[MarkdownForAgentTimeseriesResponse]),
        )


class AsyncMarkdownForAgentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMarkdownForAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMarkdownForAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMarkdownForAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncMarkdownForAgentsResourceWithStreamingResponse(self)

    async def summary(
        self,
        *,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarkdownForAgentSummaryResponse:
        """
        Retrieves the overall median HTML-to-markdown reduction ratio for AI agent
        requests over the given date range.

        Args:
          date_end: End of the date range (inclusive). Alternative to `dateRange`; provide together
              with `dateStart`. When requesting comparison series, every series must resolve
              to the same duration as the main series. Each `dateStart`/`dateEnd` is floored
              to the nearest 15 minutes before evaluation, so windows whose durations match
              only before alignment may be rejected.

          date_range: Filters results by relative date range ending at the current time, with each
              value producing a separate series. Use `<n>d` for days (up to `364d`) or `<n>w`
              for weeks (up to `52w`). Append `control` to request the equivalent previous
              period for comparison: the comparison window is shifted back by the current
              window's length rounded up to a whole number of weeks, so it keeps the same
              weekday alignment and does not overlap the current window (e.g. `7dcontrol`
              covers days -14 to -7, `10dcontrol` covers days -24 to -14). For example, pass
              `7d` and `7dcontrol` to compare this week with the previous week. All series
              must resolve to the same duration as the main series; relative ranges (including
              `control`) satisfy this automatically. Use this parameter or set specific start
              and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range. Alternative to `dateRange`; provide together with
              `dateEnd`. When requesting comparison series, every series must resolve to the
              same duration as the main series. Each `dateStart`/`dateEnd` is floored to the
              nearest 15 minutes before evaluation, so windows whose durations match only
              before alignment may be rejected.

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/ai/markdown_for_agents/summary",
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
                        "name": name,
                    },
                    markdown_for_agent_summary_params.MarkdownForAgentSummaryParams,
                ),
                post_parser=ResultWrapper[MarkdownForAgentSummaryResponse]._unwrapper,
            ),
            cast_to=cast(Type[MarkdownForAgentSummaryResponse], ResultWrapper[MarkdownForAgentSummaryResponse]),
        )

    async def timeseries(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarkdownForAgentTimeseriesResponse:
        """
        Retrieves the median HTML-to-markdown reduction ratio over time for AI agent
        requests.

        Args:
          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).
              When omitted, the interval is auto-selected from the requested date range; finer
              intervals are only available for shorter ranges. If the requested interval is
              too granular for the date range, the request is rejected.

          date_end: End of the date range (inclusive). Alternative to `dateRange`; provide together
              with `dateStart`. When requesting comparison series, every series must resolve
              to the same duration as the main series. Each `dateStart`/`dateEnd` is floored
              to the nearest 15 minutes before evaluation, so windows whose durations match
              only before alignment may be rejected.

          date_range: Filters results by relative date range ending at the current time, with each
              value producing a separate series. Use `<n>d` for days (up to `364d`) or `<n>w`
              for weeks (up to `52w`). Append `control` to request the equivalent previous
              period for comparison: the comparison window is shifted back by the current
              window's length rounded up to a whole number of weeks, so it keeps the same
              weekday alignment and does not overlap the current window (e.g. `7dcontrol`
              covers days -14 to -7, `10dcontrol` covers days -24 to -14). For example, pass
              `7d` and `7dcontrol` to compare this week with the previous week. All series
              must resolve to the same duration as the main series; relative ranges (including
              `control`) satisfy this automatically. Use this parameter or set specific start
              and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range. Alternative to `dateRange`; provide together with
              `dateEnd`. When requesting comparison series, every series must resolve to the
              same duration as the main series. Each `dateStart`/`dateEnd` is floored to the
              nearest 15 minutes before evaluation, so windows whose durations match only
              before alignment may be rejected.

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/ai/markdown_for_agents/timeseries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "name": name,
                    },
                    markdown_for_agent_timeseries_params.MarkdownForAgentTimeseriesParams,
                ),
                post_parser=ResultWrapper[MarkdownForAgentTimeseriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[MarkdownForAgentTimeseriesResponse], ResultWrapper[MarkdownForAgentTimeseriesResponse]),
        )


class MarkdownForAgentsResourceWithRawResponse:
    def __init__(self, markdown_for_agents: MarkdownForAgentsResource) -> None:
        self._markdown_for_agents = markdown_for_agents

        self.summary = to_raw_response_wrapper(
            markdown_for_agents.summary,
        )
        self.timeseries = to_raw_response_wrapper(
            markdown_for_agents.timeseries,
        )


class AsyncMarkdownForAgentsResourceWithRawResponse:
    def __init__(self, markdown_for_agents: AsyncMarkdownForAgentsResource) -> None:
        self._markdown_for_agents = markdown_for_agents

        self.summary = async_to_raw_response_wrapper(
            markdown_for_agents.summary,
        )
        self.timeseries = async_to_raw_response_wrapper(
            markdown_for_agents.timeseries,
        )


class MarkdownForAgentsResourceWithStreamingResponse:
    def __init__(self, markdown_for_agents: MarkdownForAgentsResource) -> None:
        self._markdown_for_agents = markdown_for_agents

        self.summary = to_streamed_response_wrapper(
            markdown_for_agents.summary,
        )
        self.timeseries = to_streamed_response_wrapper(
            markdown_for_agents.timeseries,
        )


class AsyncMarkdownForAgentsResourceWithStreamingResponse:
    def __init__(self, markdown_for_agents: AsyncMarkdownForAgentsResource) -> None:
        self._markdown_for_agents = markdown_for_agents

        self.summary = async_to_streamed_response_wrapper(
            markdown_for_agents.summary,
        )
        self.timeseries = async_to_streamed_response_wrapper(
            markdown_for_agents.timeseries,
        )
