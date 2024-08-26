# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .top import TopResource, AsyncTopResource

from ...._compat import cached_property

from .summary import SummaryResource, AsyncSummaryResource

from .timeseries_groups import TimeseriesGroupsResource, AsyncTimeseriesGroupsResource

from ....types.radar.dns_timeseries_response import DNSTimeseriesResponse

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from ...._base_client import make_request_options

from typing import Type, List, Union

from typing_extensions import Literal

from datetime import datetime

from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.radar import dns_timeseries_params
from .top import TopResource, AsyncTopResource, TopResourceWithRawResponse, AsyncTopResourceWithRawResponse, TopResourceWithStreamingResponse, AsyncTopResourceWithStreamingResponse
from .summary import SummaryResource, AsyncSummaryResource, SummaryResourceWithRawResponse, AsyncSummaryResourceWithRawResponse, SummaryResourceWithStreamingResponse, AsyncSummaryResourceWithStreamingResponse
from .timeseries_groups import TimeseriesGroupsResource, AsyncTimeseriesGroupsResource, TimeseriesGroupsResourceWithRawResponse, AsyncTimeseriesGroupsResourceWithRawResponse, TimeseriesGroupsResourceWithStreamingResponse, AsyncTimeseriesGroupsResourceWithStreamingResponse
from typing import cast
from typing import cast

__all__ = ["DNSResource", "AsyncDNSResource"]

class DNSResource(SyncAPIResource):
    @cached_property
    def top(self) -> TopResource:
        return TopResource(self._client)

    @cached_property
    def summary(self) -> SummaryResource:
        return SummaryResource(self._client)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResource:
        return TimeseriesGroupsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DNSResourceWithRawResponse:
        return DNSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DNSResourceWithStreamingResponse:
        return DNSResourceWithStreamingResponse(self)

    def timeseries(self,
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
    tld: List[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> DNSTimeseriesResponse:
        """
        Get DNS queries change over time.

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

          tld: Filter for ccTLD.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/dns/timeseries",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "agg_interval": agg_interval,
                "asn": asn,
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "format": format,
                "location": location,
                "name": name,
                "tld": tld,
            }, dns_timeseries_params.DNSTimeseriesParams), post_parser=ResultWrapper[DNSTimeseriesResponse]._unwrapper),
            cast_to=cast(Type[DNSTimeseriesResponse], ResultWrapper[DNSTimeseriesResponse]),
        )

class AsyncDNSResource(AsyncAPIResource):
    @cached_property
    def top(self) -> AsyncTopResource:
        return AsyncTopResource(self._client)

    @cached_property
    def summary(self) -> AsyncSummaryResource:
        return AsyncSummaryResource(self._client)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResource:
        return AsyncTimeseriesGroupsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDNSResourceWithRawResponse:
        return AsyncDNSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDNSResourceWithStreamingResponse:
        return AsyncDNSResourceWithStreamingResponse(self)

    async def timeseries(self,
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
    tld: List[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> DNSTimeseriesResponse:
        """
        Get DNS queries change over time.

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

          tld: Filter for ccTLD.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/dns/timeseries",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "agg_interval": agg_interval,
                "asn": asn,
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "format": format,
                "location": location,
                "name": name,
                "tld": tld,
            }, dns_timeseries_params.DNSTimeseriesParams), post_parser=ResultWrapper[DNSTimeseriesResponse]._unwrapper),
            cast_to=cast(Type[DNSTimeseriesResponse], ResultWrapper[DNSTimeseriesResponse]),
        )

class DNSResourceWithRawResponse:
    def __init__(self, dns: DNSResource) -> None:
        self._dns = dns

        self.timeseries = to_raw_response_wrapper(
            dns.timeseries,
        )

    @cached_property
    def top(self) -> TopResourceWithRawResponse:
        return TopResourceWithRawResponse(self._dns.top)

    @cached_property
    def summary(self) -> SummaryResourceWithRawResponse:
        return SummaryResourceWithRawResponse(self._dns.summary)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResourceWithRawResponse:
        return TimeseriesGroupsResourceWithRawResponse(self._dns.timeseries_groups)

class AsyncDNSResourceWithRawResponse:
    def __init__(self, dns: AsyncDNSResource) -> None:
        self._dns = dns

        self.timeseries = async_to_raw_response_wrapper(
            dns.timeseries,
        )

    @cached_property
    def top(self) -> AsyncTopResourceWithRawResponse:
        return AsyncTopResourceWithRawResponse(self._dns.top)

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithRawResponse:
        return AsyncSummaryResourceWithRawResponse(self._dns.summary)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResourceWithRawResponse:
        return AsyncTimeseriesGroupsResourceWithRawResponse(self._dns.timeseries_groups)

class DNSResourceWithStreamingResponse:
    def __init__(self, dns: DNSResource) -> None:
        self._dns = dns

        self.timeseries = to_streamed_response_wrapper(
            dns.timeseries,
        )

    @cached_property
    def top(self) -> TopResourceWithStreamingResponse:
        return TopResourceWithStreamingResponse(self._dns.top)

    @cached_property
    def summary(self) -> SummaryResourceWithStreamingResponse:
        return SummaryResourceWithStreamingResponse(self._dns.summary)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResourceWithStreamingResponse:
        return TimeseriesGroupsResourceWithStreamingResponse(self._dns.timeseries_groups)

class AsyncDNSResourceWithStreamingResponse:
    def __init__(self, dns: AsyncDNSResource) -> None:
        self._dns = dns

        self.timeseries = async_to_streamed_response_wrapper(
            dns.timeseries,
        )

    @cached_property
    def top(self) -> AsyncTopResourceWithStreamingResponse:
        return AsyncTopResourceWithStreamingResponse(self._dns.top)

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithStreamingResponse:
        return AsyncSummaryResourceWithStreamingResponse(self._dns.summary)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResourceWithStreamingResponse:
        return AsyncTimeseriesGroupsResourceWithStreamingResponse(self._dns.timeseries_groups)