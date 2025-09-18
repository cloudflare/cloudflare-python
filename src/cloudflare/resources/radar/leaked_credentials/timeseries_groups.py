# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
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
from ...._base_client import make_request_options
from ....types.radar.leaked_credentials import timeseries_group_bot_class_params, timeseries_group_compromised_params
from ....types.radar.leaked_credentials.timeseries_group_bot_class_response import TimeseriesGroupBotClassResponse
from ....types.radar.leaked_credentials.timeseries_group_compromised_response import TimeseriesGroupCompromisedResponse

__all__ = ["TimeseriesGroupsResource", "AsyncTimeseriesGroupsResource"]


class TimeseriesGroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TimeseriesGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TimeseriesGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TimeseriesGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TimeseriesGroupsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    def bot_class(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        compromised: List[Literal["CLEAN", "COMPROMISED"]] | Omit = omit,
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
    ) -> TimeseriesGroupBotClassResponse:
        """
        Retrieves the distribution of HTTP authentication requests by bot class over
        time.

        Args:
          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          compromised: Filters results by compromised credential status (clean vs. compromised).

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/leaked_credential_checks/timeseries_groups/bot_class",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "compromised": compromised,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "name": name,
                    },
                    timeseries_group_bot_class_params.TimeseriesGroupBotClassParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupBotClassResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupBotClassResponse], ResultWrapper[TimeseriesGroupBotClassResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    def compromised(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | Omit = omit,
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
    ) -> TimeseriesGroupCompromisedResponse:
        """
        Retrieves the distribution of HTTP authentication requests by compromised
        credential status over time.

        Args:
          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          bot_class: Filters results by bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/leaked_credential_checks/timeseries_groups/compromised",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "bot_class": bot_class,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "name": name,
                    },
                    timeseries_group_compromised_params.TimeseriesGroupCompromisedParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupCompromisedResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupCompromisedResponse], ResultWrapper[TimeseriesGroupCompromisedResponse]),
        )


class AsyncTimeseriesGroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTimeseriesGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTimeseriesGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTimeseriesGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTimeseriesGroupsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    async def bot_class(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        compromised: List[Literal["CLEAN", "COMPROMISED"]] | Omit = omit,
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
    ) -> TimeseriesGroupBotClassResponse:
        """
        Retrieves the distribution of HTTP authentication requests by bot class over
        time.

        Args:
          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          compromised: Filters results by compromised credential status (clean vs. compromised).

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/leaked_credential_checks/timeseries_groups/bot_class",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "compromised": compromised,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "name": name,
                    },
                    timeseries_group_bot_class_params.TimeseriesGroupBotClassParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupBotClassResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupBotClassResponse], ResultWrapper[TimeseriesGroupBotClassResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    async def compromised(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | Omit = omit,
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
    ) -> TimeseriesGroupCompromisedResponse:
        """
        Retrieves the distribution of HTTP authentication requests by compromised
        credential status over time.

        Args:
          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          bot_class: Filters results by bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/leaked_credential_checks/timeseries_groups/compromised",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "bot_class": bot_class,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "name": name,
                    },
                    timeseries_group_compromised_params.TimeseriesGroupCompromisedParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupCompromisedResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupCompromisedResponse], ResultWrapper[TimeseriesGroupCompromisedResponse]),
        )


class TimeseriesGroupsResourceWithRawResponse:
    def __init__(self, timeseries_groups: TimeseriesGroupsResource) -> None:
        self._timeseries_groups = timeseries_groups

        self.bot_class = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                timeseries_groups.bot_class,  # pyright: ignore[reportDeprecated],
            )
        )
        self.compromised = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                timeseries_groups.compromised,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncTimeseriesGroupsResourceWithRawResponse:
    def __init__(self, timeseries_groups: AsyncTimeseriesGroupsResource) -> None:
        self._timeseries_groups = timeseries_groups

        self.bot_class = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                timeseries_groups.bot_class,  # pyright: ignore[reportDeprecated],
            )
        )
        self.compromised = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                timeseries_groups.compromised,  # pyright: ignore[reportDeprecated],
            )
        )


class TimeseriesGroupsResourceWithStreamingResponse:
    def __init__(self, timeseries_groups: TimeseriesGroupsResource) -> None:
        self._timeseries_groups = timeseries_groups

        self.bot_class = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                timeseries_groups.bot_class,  # pyright: ignore[reportDeprecated],
            )
        )
        self.compromised = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                timeseries_groups.compromised,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncTimeseriesGroupsResourceWithStreamingResponse:
    def __init__(self, timeseries_groups: AsyncTimeseriesGroupsResource) -> None:
        self._timeseries_groups = timeseries_groups

        self.bot_class = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                timeseries_groups.bot_class,  # pyright: ignore[reportDeprecated],
            )
        )
        self.compromised = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                timeseries_groups.compromised,  # pyright: ignore[reportDeprecated],
            )
        )
