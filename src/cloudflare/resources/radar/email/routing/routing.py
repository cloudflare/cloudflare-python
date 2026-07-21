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
from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import make_request_options
from .timeseries_groups import (
    TimeseriesGroupsResource,
    AsyncTimeseriesGroupsResource,
    TimeseriesGroupsResourceWithRawResponse,
    AsyncTimeseriesGroupsResourceWithRawResponse,
    TimeseriesGroupsResourceWithStreamingResponse,
    AsyncTimeseriesGroupsResourceWithStreamingResponse,
)
from .....types.radar.email import routing_summary_v2_params, routing_timeseries_groups_v2_params
from .....types.radar.email.routing_summary_v2_response import RoutingSummaryV2Response
from .....types.radar.email.routing_timeseries_groups_v2_response import RoutingTimeseriesGroupsV2Response

__all__ = ["RoutingResource", "AsyncRoutingResource"]


class RoutingResource(SyncAPIResource):
    @cached_property
    def summary(self) -> SummaryResource:
        return SummaryResource(self._client)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResource:
        return TimeseriesGroupsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RoutingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RoutingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoutingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RoutingResourceWithStreamingResponse(self)

    def summary_v2(
        self,
        dimension: Literal["IP_VERSION", "ENCRYPTED", "ARC", "DKIM", "DMARC", "SPF"],
        *,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        encrypted: List[Literal["ENCRYPTED", "NOT_ENCRYPTED"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
        limit_per_group: int | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoutingSummaryV2Response:
        """
        Retrieves the distribution of email routing metrics by the specified dimension.

        Args:
          dimension: Specifies the attribute by which to group the results.

          arc: Filters results by ARC (Authenticated Received Chain) validation.

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

          dkim: Filters results by DKIM (DomainKeys Identified Mail) validation status.

          dmarc: Filters results by DMARC (Domain-based Message Authentication, Reporting and
              Conformance) validation status.

          encrypted: Filters results by encryption status (encrypted vs. not-encrypted).

          format: Format in which results will be returned.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          limit_per_group: Limits the number of objects per group to the top items within the specified
              time range. When item count exceeds the limit, extra items appear grouped under
              an "other" category. Only supported on high-cardinality dimensions; otherwise
              the request is rejected. Minimum value is 2.

          name: Array of names used to label the series in the response.

          spf: Filters results by SPF (Sender Policy Framework) validation status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return self._get(
            path_template("/radar/email/routing/summary/{dimension}", dimension=dimension),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "encrypted": encrypted,
                        "format": format,
                        "ip_version": ip_version,
                        "limit_per_group": limit_per_group,
                        "name": name,
                        "spf": spf,
                    },
                    routing_summary_v2_params.RoutingSummaryV2Params,
                ),
                post_parser=ResultWrapper[RoutingSummaryV2Response]._unwrapper,
            ),
            cast_to=cast(Type[RoutingSummaryV2Response], ResultWrapper[RoutingSummaryV2Response]),
        )

    def timeseries_groups_v2(
        self,
        dimension: Literal["IP_VERSION", "ENCRYPTED", "ARC", "DKIM", "DMARC", "SPF"],
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        encrypted: List[Literal["ENCRYPTED", "NOT_ENCRYPTED"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
        limit_per_group: int | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoutingTimeseriesGroupsV2Response:
        """
        Retrieves the distribution of email routing metrics grouped by dimension over
        time.

        Args:
          dimension: Specifies the attribute by which to group the results.

          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).
              When omitted, the interval is auto-selected from the requested date range; finer
              intervals are only available for shorter ranges. If the requested interval is
              too granular for the date range, the request is rejected.

          arc: Filters results by ARC (Authenticated Received Chain) validation.

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

          dkim: Filters results by DKIM (DomainKeys Identified Mail) validation status.

          dmarc: Filters results by DMARC (Domain-based Message Authentication, Reporting and
              Conformance) validation status.

          encrypted: Filters results by encryption status (encrypted vs. not-encrypted).

          format: Format in which results will be returned.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          limit_per_group: Limits the number of objects per group to the top items within the specified
              time range. When item count exceeds the limit, extra items appear grouped under
              an "other" category. Only supported on high-cardinality dimensions; otherwise
              the request is rejected. Minimum value is 2.

          name: Array of names used to label the series in the response.

          spf: Filters results by SPF (Sender Policy Framework) validation status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return self._get(
            path_template("/radar/email/routing/timeseries_groups/{dimension}", dimension=dimension),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "encrypted": encrypted,
                        "format": format,
                        "ip_version": ip_version,
                        "limit_per_group": limit_per_group,
                        "name": name,
                        "spf": spf,
                    },
                    routing_timeseries_groups_v2_params.RoutingTimeseriesGroupsV2Params,
                ),
                post_parser=ResultWrapper[RoutingTimeseriesGroupsV2Response]._unwrapper,
            ),
            cast_to=cast(Type[RoutingTimeseriesGroupsV2Response], ResultWrapper[RoutingTimeseriesGroupsV2Response]),
        )


class AsyncRoutingResource(AsyncAPIResource):
    @cached_property
    def summary(self) -> AsyncSummaryResource:
        return AsyncSummaryResource(self._client)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResource:
        return AsyncTimeseriesGroupsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRoutingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRoutingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoutingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRoutingResourceWithStreamingResponse(self)

    async def summary_v2(
        self,
        dimension: Literal["IP_VERSION", "ENCRYPTED", "ARC", "DKIM", "DMARC", "SPF"],
        *,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        encrypted: List[Literal["ENCRYPTED", "NOT_ENCRYPTED"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
        limit_per_group: int | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoutingSummaryV2Response:
        """
        Retrieves the distribution of email routing metrics by the specified dimension.

        Args:
          dimension: Specifies the attribute by which to group the results.

          arc: Filters results by ARC (Authenticated Received Chain) validation.

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

          dkim: Filters results by DKIM (DomainKeys Identified Mail) validation status.

          dmarc: Filters results by DMARC (Domain-based Message Authentication, Reporting and
              Conformance) validation status.

          encrypted: Filters results by encryption status (encrypted vs. not-encrypted).

          format: Format in which results will be returned.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          limit_per_group: Limits the number of objects per group to the top items within the specified
              time range. When item count exceeds the limit, extra items appear grouped under
              an "other" category. Only supported on high-cardinality dimensions; otherwise
              the request is rejected. Minimum value is 2.

          name: Array of names used to label the series in the response.

          spf: Filters results by SPF (Sender Policy Framework) validation status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return await self._get(
            path_template("/radar/email/routing/summary/{dimension}", dimension=dimension),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "encrypted": encrypted,
                        "format": format,
                        "ip_version": ip_version,
                        "limit_per_group": limit_per_group,
                        "name": name,
                        "spf": spf,
                    },
                    routing_summary_v2_params.RoutingSummaryV2Params,
                ),
                post_parser=ResultWrapper[RoutingSummaryV2Response]._unwrapper,
            ),
            cast_to=cast(Type[RoutingSummaryV2Response], ResultWrapper[RoutingSummaryV2Response]),
        )

    async def timeseries_groups_v2(
        self,
        dimension: Literal["IP_VERSION", "ENCRYPTED", "ARC", "DKIM", "DMARC", "SPF"],
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        encrypted: List[Literal["ENCRYPTED", "NOT_ENCRYPTED"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
        limit_per_group: int | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoutingTimeseriesGroupsV2Response:
        """
        Retrieves the distribution of email routing metrics grouped by dimension over
        time.

        Args:
          dimension: Specifies the attribute by which to group the results.

          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).
              When omitted, the interval is auto-selected from the requested date range; finer
              intervals are only available for shorter ranges. If the requested interval is
              too granular for the date range, the request is rejected.

          arc: Filters results by ARC (Authenticated Received Chain) validation.

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

          dkim: Filters results by DKIM (DomainKeys Identified Mail) validation status.

          dmarc: Filters results by DMARC (Domain-based Message Authentication, Reporting and
              Conformance) validation status.

          encrypted: Filters results by encryption status (encrypted vs. not-encrypted).

          format: Format in which results will be returned.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          limit_per_group: Limits the number of objects per group to the top items within the specified
              time range. When item count exceeds the limit, extra items appear grouped under
              an "other" category. Only supported on high-cardinality dimensions; otherwise
              the request is rejected. Minimum value is 2.

          name: Array of names used to label the series in the response.

          spf: Filters results by SPF (Sender Policy Framework) validation status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return await self._get(
            path_template("/radar/email/routing/timeseries_groups/{dimension}", dimension=dimension),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "encrypted": encrypted,
                        "format": format,
                        "ip_version": ip_version,
                        "limit_per_group": limit_per_group,
                        "name": name,
                        "spf": spf,
                    },
                    routing_timeseries_groups_v2_params.RoutingTimeseriesGroupsV2Params,
                ),
                post_parser=ResultWrapper[RoutingTimeseriesGroupsV2Response]._unwrapper,
            ),
            cast_to=cast(Type[RoutingTimeseriesGroupsV2Response], ResultWrapper[RoutingTimeseriesGroupsV2Response]),
        )


class RoutingResourceWithRawResponse:
    def __init__(self, routing: RoutingResource) -> None:
        self._routing = routing

        self.summary_v2 = to_raw_response_wrapper(
            routing.summary_v2,
        )
        self.timeseries_groups_v2 = to_raw_response_wrapper(
            routing.timeseries_groups_v2,
        )

    @cached_property
    def summary(self) -> SummaryResourceWithRawResponse:
        return SummaryResourceWithRawResponse(self._routing.summary)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResourceWithRawResponse:
        return TimeseriesGroupsResourceWithRawResponse(self._routing.timeseries_groups)


class AsyncRoutingResourceWithRawResponse:
    def __init__(self, routing: AsyncRoutingResource) -> None:
        self._routing = routing

        self.summary_v2 = async_to_raw_response_wrapper(
            routing.summary_v2,
        )
        self.timeseries_groups_v2 = async_to_raw_response_wrapper(
            routing.timeseries_groups_v2,
        )

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithRawResponse:
        return AsyncSummaryResourceWithRawResponse(self._routing.summary)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResourceWithRawResponse:
        return AsyncTimeseriesGroupsResourceWithRawResponse(self._routing.timeseries_groups)


class RoutingResourceWithStreamingResponse:
    def __init__(self, routing: RoutingResource) -> None:
        self._routing = routing

        self.summary_v2 = to_streamed_response_wrapper(
            routing.summary_v2,
        )
        self.timeseries_groups_v2 = to_streamed_response_wrapper(
            routing.timeseries_groups_v2,
        )

    @cached_property
    def summary(self) -> SummaryResourceWithStreamingResponse:
        return SummaryResourceWithStreamingResponse(self._routing.summary)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResourceWithStreamingResponse:
        return TimeseriesGroupsResourceWithStreamingResponse(self._routing.timeseries_groups)


class AsyncRoutingResourceWithStreamingResponse:
    def __init__(self, routing: AsyncRoutingResource) -> None:
        self._routing = routing

        self.summary_v2 = async_to_streamed_response_wrapper(
            routing.summary_v2,
        )
        self.timeseries_groups_v2 = async_to_streamed_response_wrapper(
            routing.timeseries_groups_v2,
        )

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithStreamingResponse:
        return AsyncSummaryResourceWithStreamingResponse(self._routing.summary)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResourceWithStreamingResponse:
        return AsyncTimeseriesGroupsResourceWithStreamingResponse(self._routing.timeseries_groups)
