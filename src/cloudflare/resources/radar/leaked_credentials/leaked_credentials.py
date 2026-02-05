# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .summary import (
    SummaryResource,
    AsyncSummaryResource,
    SummaryResourceWithRawResponse,
    AsyncSummaryResourceWithRawResponse,
    SummaryResourceWithStreamingResponse,
    AsyncSummaryResourceWithStreamingResponse,
)
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
from ....types.radar import leaked_credential_summary_v2_params, leaked_credential_timeseries_groups_v2_params
from ...._base_client import make_request_options
from .timeseries_groups import (
    TimeseriesGroupsResource,
    AsyncTimeseriesGroupsResource,
    TimeseriesGroupsResourceWithRawResponse,
    AsyncTimeseriesGroupsResourceWithRawResponse,
    TimeseriesGroupsResourceWithStreamingResponse,
    AsyncTimeseriesGroupsResourceWithStreamingResponse,
)
from ....types.radar.leaked_credential_summary_v2_response import LeakedCredentialSummaryV2Response
from ....types.radar.leaked_credential_timeseries_groups_v2_response import LeakedCredentialTimeseriesGroupsV2Response

__all__ = ["LeakedCredentialsResource", "AsyncLeakedCredentialsResource"]


class LeakedCredentialsResource(SyncAPIResource):
    @cached_property
    def summary(self) -> SummaryResource:
        return SummaryResource(self._client)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResource:
        return TimeseriesGroupsResource(self._client)

    @cached_property
    def with_raw_response(self) -> LeakedCredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return LeakedCredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LeakedCredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return LeakedCredentialsResourceWithStreamingResponse(self)

    def summary_v2(
        self,
        dimension: Literal["COMPROMISED", "BOT_CLASS"],
        *,
        asn: SequenceNotStr[str] | Omit = omit,
        bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | Omit = omit,
        compromised: List[Literal["CLEAN", "COMPROMISED"]] | Omit = omit,
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
    ) -> LeakedCredentialSummaryV2Response:
        """
        Retrieves an aggregated summary of HTTP authentication requests grouped by the
        specified dimension.

        Args:
          dimension: Specifies the attribute by which to group the results.

          asn: Filters results by Autonomous System. Specify one or more Autonomous System
              Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from
              results. For example, `-174, 3356` excludes results from AS174, but includes
              results from AS3356.

          bot_class: Filters results by bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          compromised: Filters results by compromised credential status (clean vs. compromised).

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
            f"/radar/leaked_credential_checks/summary/{dimension}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asn": asn,
                        "bot_class": bot_class,
                        "compromised": compromised,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "limit_per_group": limit_per_group,
                        "location": location,
                        "name": name,
                    },
                    leaked_credential_summary_v2_params.LeakedCredentialSummaryV2Params,
                ),
                post_parser=ResultWrapper[LeakedCredentialSummaryV2Response]._unwrapper,
            ),
            cast_to=cast(Type[LeakedCredentialSummaryV2Response], ResultWrapper[LeakedCredentialSummaryV2Response]),
        )

    def timeseries_groups_v2(
        self,
        dimension: Literal["COMPROMISED", "BOT_CLASS"],
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        asn: SequenceNotStr[str] | Omit = omit,
        bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | Omit = omit,
        check_result: List[
            Literal[
                "CLEAN",
                "USERNAME_LEAKED",
                "USERNAME_PASSWORD_SIMILAR",
                "USERNAME_AND_PASSWORD_LEAKED",
                "PASSWORD_LEAKED",
            ]
        ]
        | Omit = omit,
        compromised: List[Literal["CLEAN", "COMPROMISED"]] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        limit_per_group: int | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        normalization: Literal["PERCENTAGE_CHANGE", "MIN0_MAX"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LeakedCredentialTimeseriesGroupsV2Response:
        """
        Retrieves the distribution of HTTP authentication requests, grouped by the
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

          bot_class: Filters results by bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          check_result: Filters results by leaked credential check result.

          compromised: Filters results by compromised credential status (clean vs. compromised).

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

          normalization: Normalization method applied to the results. Refer to
              [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return self._get(
            f"/radar/leaked_credential_checks/timeseries_groups/{dimension}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "asn": asn,
                        "bot_class": bot_class,
                        "check_result": check_result,
                        "compromised": compromised,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "limit_per_group": limit_per_group,
                        "location": location,
                        "name": name,
                        "normalization": normalization,
                    },
                    leaked_credential_timeseries_groups_v2_params.LeakedCredentialTimeseriesGroupsV2Params,
                ),
                post_parser=ResultWrapper[LeakedCredentialTimeseriesGroupsV2Response]._unwrapper,
            ),
            cast_to=cast(
                Type[LeakedCredentialTimeseriesGroupsV2Response],
                ResultWrapper[LeakedCredentialTimeseriesGroupsV2Response],
            ),
        )


class AsyncLeakedCredentialsResource(AsyncAPIResource):
    @cached_property
    def summary(self) -> AsyncSummaryResource:
        return AsyncSummaryResource(self._client)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResource:
        return AsyncTimeseriesGroupsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLeakedCredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLeakedCredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLeakedCredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncLeakedCredentialsResourceWithStreamingResponse(self)

    async def summary_v2(
        self,
        dimension: Literal["COMPROMISED", "BOT_CLASS"],
        *,
        asn: SequenceNotStr[str] | Omit = omit,
        bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | Omit = omit,
        compromised: List[Literal["CLEAN", "COMPROMISED"]] | Omit = omit,
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
    ) -> LeakedCredentialSummaryV2Response:
        """
        Retrieves an aggregated summary of HTTP authentication requests grouped by the
        specified dimension.

        Args:
          dimension: Specifies the attribute by which to group the results.

          asn: Filters results by Autonomous System. Specify one or more Autonomous System
              Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from
              results. For example, `-174, 3356` excludes results from AS174, but includes
              results from AS3356.

          bot_class: Filters results by bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          compromised: Filters results by compromised credential status (clean vs. compromised).

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
            f"/radar/leaked_credential_checks/summary/{dimension}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asn": asn,
                        "bot_class": bot_class,
                        "compromised": compromised,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "limit_per_group": limit_per_group,
                        "location": location,
                        "name": name,
                    },
                    leaked_credential_summary_v2_params.LeakedCredentialSummaryV2Params,
                ),
                post_parser=ResultWrapper[LeakedCredentialSummaryV2Response]._unwrapper,
            ),
            cast_to=cast(Type[LeakedCredentialSummaryV2Response], ResultWrapper[LeakedCredentialSummaryV2Response]),
        )

    async def timeseries_groups_v2(
        self,
        dimension: Literal["COMPROMISED", "BOT_CLASS"],
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        asn: SequenceNotStr[str] | Omit = omit,
        bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | Omit = omit,
        check_result: List[
            Literal[
                "CLEAN",
                "USERNAME_LEAKED",
                "USERNAME_PASSWORD_SIMILAR",
                "USERNAME_AND_PASSWORD_LEAKED",
                "PASSWORD_LEAKED",
            ]
        ]
        | Omit = omit,
        compromised: List[Literal["CLEAN", "COMPROMISED"]] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        limit_per_group: int | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        normalization: Literal["PERCENTAGE_CHANGE", "MIN0_MAX"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LeakedCredentialTimeseriesGroupsV2Response:
        """
        Retrieves the distribution of HTTP authentication requests, grouped by the
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

          bot_class: Filters results by bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          check_result: Filters results by leaked credential check result.

          compromised: Filters results by compromised credential status (clean vs. compromised).

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

          normalization: Normalization method applied to the results. Refer to
              [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return await self._get(
            f"/radar/leaked_credential_checks/timeseries_groups/{dimension}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "asn": asn,
                        "bot_class": bot_class,
                        "check_result": check_result,
                        "compromised": compromised,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "limit_per_group": limit_per_group,
                        "location": location,
                        "name": name,
                        "normalization": normalization,
                    },
                    leaked_credential_timeseries_groups_v2_params.LeakedCredentialTimeseriesGroupsV2Params,
                ),
                post_parser=ResultWrapper[LeakedCredentialTimeseriesGroupsV2Response]._unwrapper,
            ),
            cast_to=cast(
                Type[LeakedCredentialTimeseriesGroupsV2Response],
                ResultWrapper[LeakedCredentialTimeseriesGroupsV2Response],
            ),
        )


class LeakedCredentialsResourceWithRawResponse:
    def __init__(self, leaked_credentials: LeakedCredentialsResource) -> None:
        self._leaked_credentials = leaked_credentials

        self.summary_v2 = to_raw_response_wrapper(
            leaked_credentials.summary_v2,
        )
        self.timeseries_groups_v2 = to_raw_response_wrapper(
            leaked_credentials.timeseries_groups_v2,
        )

    @cached_property
    def summary(self) -> SummaryResourceWithRawResponse:
        return SummaryResourceWithRawResponse(self._leaked_credentials.summary)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResourceWithRawResponse:
        return TimeseriesGroupsResourceWithRawResponse(self._leaked_credentials.timeseries_groups)


class AsyncLeakedCredentialsResourceWithRawResponse:
    def __init__(self, leaked_credentials: AsyncLeakedCredentialsResource) -> None:
        self._leaked_credentials = leaked_credentials

        self.summary_v2 = async_to_raw_response_wrapper(
            leaked_credentials.summary_v2,
        )
        self.timeseries_groups_v2 = async_to_raw_response_wrapper(
            leaked_credentials.timeseries_groups_v2,
        )

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithRawResponse:
        return AsyncSummaryResourceWithRawResponse(self._leaked_credentials.summary)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResourceWithRawResponse:
        return AsyncTimeseriesGroupsResourceWithRawResponse(self._leaked_credentials.timeseries_groups)


class LeakedCredentialsResourceWithStreamingResponse:
    def __init__(self, leaked_credentials: LeakedCredentialsResource) -> None:
        self._leaked_credentials = leaked_credentials

        self.summary_v2 = to_streamed_response_wrapper(
            leaked_credentials.summary_v2,
        )
        self.timeseries_groups_v2 = to_streamed_response_wrapper(
            leaked_credentials.timeseries_groups_v2,
        )

    @cached_property
    def summary(self) -> SummaryResourceWithStreamingResponse:
        return SummaryResourceWithStreamingResponse(self._leaked_credentials.summary)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResourceWithStreamingResponse:
        return TimeseriesGroupsResourceWithStreamingResponse(self._leaked_credentials.timeseries_groups)


class AsyncLeakedCredentialsResourceWithStreamingResponse:
    def __init__(self, leaked_credentials: AsyncLeakedCredentialsResource) -> None:
        self._leaked_credentials = leaked_credentials

        self.summary_v2 = async_to_streamed_response_wrapper(
            leaked_credentials.summary_v2,
        )
        self.timeseries_groups_v2 = async_to_streamed_response_wrapper(
            leaked_credentials.timeseries_groups_v2,
        )

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithStreamingResponse:
        return AsyncSummaryResourceWithStreamingResponse(self._leaked_credentials.summary)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResourceWithStreamingResponse:
        return AsyncTimeseriesGroupsResourceWithStreamingResponse(self._leaked_credentials.timeseries_groups)
