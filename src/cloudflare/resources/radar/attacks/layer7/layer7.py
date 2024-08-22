# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .summary import SummaryResource, AsyncSummaryResource

from ....._compat import cached_property

from .timeseries_groups import TimeseriesGroupsResource, AsyncTimeseriesGroupsResource

from .top.top import TopResource, AsyncTopResource

from .....types.radar.attacks.layer7_timeseries_response import Layer7TimeseriesResponse

from ....._wrappers import ResultWrapper

from ....._utils import maybe_transform, async_maybe_transform

from ....._base_client import make_request_options

from typing import Type, List, Union

from typing_extensions import Literal

from datetime import datetime

from ....._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .....types.radar.attacks import layer7_timeseries_params
from .summary import SummaryResource, AsyncSummaryResource, SummaryResourceWithRawResponse, AsyncSummaryResourceWithRawResponse, SummaryResourceWithStreamingResponse, AsyncSummaryResourceWithStreamingResponse
from .timeseries_groups import TimeseriesGroupsResource, AsyncTimeseriesGroupsResource, TimeseriesGroupsResourceWithRawResponse, AsyncTimeseriesGroupsResourceWithRawResponse, TimeseriesGroupsResourceWithStreamingResponse, AsyncTimeseriesGroupsResourceWithStreamingResponse
from .top import TopResource, AsyncTopResource, TopResourceWithRawResponse, AsyncTopResourceWithRawResponse, TopResourceWithStreamingResponse, AsyncTopResourceWithStreamingResponse
from typing import cast
from typing import cast

__all__ = ["Layer7Resource", "AsyncLayer7Resource"]

class Layer7Resource(SyncAPIResource):
    @cached_property
    def summary(self) -> SummaryResource:
        return SummaryResource(self._client)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResource:
        return TimeseriesGroupsResource(self._client)

    @cached_property
    def top(self) -> TopResource:
        return TopResource(self._client)

    @cached_property
    def with_raw_response(self) -> Layer7ResourceWithRawResponse:
        return Layer7ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> Layer7ResourceWithStreamingResponse:
        return Layer7ResourceWithStreamingResponse(self)

    def timeseries(self,
    *,
    agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
    asn: List[str] | NotGiven = NOT_GIVEN,
    attack: List[Literal["DDOS", "WAF", "BOT_MANAGEMENT", "ACCESS_RULES", "IP_REPUTATION", "API_SHIELD", "DATA_LOSS_PREVENTION"]] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    date_range: List[str] | NotGiven = NOT_GIVEN,
    date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    http_method: List[Literal["GET", "POST", "DELETE", "PUT", "HEAD", "PURGE", "OPTIONS", "PROPFIND", "MKCOL", "PATCH", "ACL", "BCOPY", "BDELETE", "BMOVE", "BPROPFIND", "BPROPPATCH", "CHECKIN", "CHECKOUT", "CONNECT", "COPY", "LABEL", "LOCK", "MERGE", "MKACTIVITY", "MKWORKSPACE", "MOVE", "NOTIFY", "ORDERPATCH", "POLL", "PROPPATCH", "REPORT", "SEARCH", "SUBSCRIBE", "TRACE", "UNCHECKOUT", "UNLOCK", "UNSUBSCRIBE", "UPDATE", "VERSIONCONTROL", "BASELINECONTROL", "XMSENUMATTS", "RPC_OUT_DATA", "RPC_IN_DATA", "JSON", "COOK", "TRACK"]] | NotGiven = NOT_GIVEN,
    http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
    ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    mitigation_product: List[Literal["DDOS", "WAF", "BOT_MANAGEMENT", "ACCESS_RULES", "IP_REPUTATION", "API_SHIELD", "DATA_LOSS_PREVENTION"]] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    normalization: Literal["PERCENTAGE_CHANGE", "MIN0_MAX"] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Layer7TimeseriesResponse:
        """Get a timeseries of Layer 7 attacks.

        Values represent HTTP requests and are
        normalized using min-max by default.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          attack: This field is deprecated, please use the new `mitigationProduct`.

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          http_method: Filter for http method.

          http_version: Filter for http version.

          ip_version: Filter for ip version.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          mitigation_product: Array of L7 mitigation products.

          name: Array of names that will be used to name the series in responses.

          normalization: Normalization method applied. Refer to
              [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/attacks/layer7/timeseries",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "agg_interval": agg_interval,
                "asn": asn,
                "attack": attack,
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "format": format,
                "http_method": http_method,
                "http_version": http_version,
                "ip_version": ip_version,
                "location": location,
                "mitigation_product": mitigation_product,
                "name": name,
                "normalization": normalization,
            }, layer7_timeseries_params.Layer7TimeseriesParams), post_parser=ResultWrapper[Layer7TimeseriesResponse]._unwrapper),
            cast_to=cast(Type[Layer7TimeseriesResponse], ResultWrapper[Layer7TimeseriesResponse]),
        )

class AsyncLayer7Resource(AsyncAPIResource):
    @cached_property
    def summary(self) -> AsyncSummaryResource:
        return AsyncSummaryResource(self._client)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResource:
        return AsyncTimeseriesGroupsResource(self._client)

    @cached_property
    def top(self) -> AsyncTopResource:
        return AsyncTopResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLayer7ResourceWithRawResponse:
        return AsyncLayer7ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLayer7ResourceWithStreamingResponse:
        return AsyncLayer7ResourceWithStreamingResponse(self)

    async def timeseries(self,
    *,
    agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
    asn: List[str] | NotGiven = NOT_GIVEN,
    attack: List[Literal["DDOS", "WAF", "BOT_MANAGEMENT", "ACCESS_RULES", "IP_REPUTATION", "API_SHIELD", "DATA_LOSS_PREVENTION"]] | NotGiven = NOT_GIVEN,
    continent: List[str] | NotGiven = NOT_GIVEN,
    date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    date_range: List[str] | NotGiven = NOT_GIVEN,
    date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    http_method: List[Literal["GET", "POST", "DELETE", "PUT", "HEAD", "PURGE", "OPTIONS", "PROPFIND", "MKCOL", "PATCH", "ACL", "BCOPY", "BDELETE", "BMOVE", "BPROPFIND", "BPROPPATCH", "CHECKIN", "CHECKOUT", "CONNECT", "COPY", "LABEL", "LOCK", "MERGE", "MKACTIVITY", "MKWORKSPACE", "MOVE", "NOTIFY", "ORDERPATCH", "POLL", "PROPPATCH", "REPORT", "SEARCH", "SUBSCRIBE", "TRACE", "UNCHECKOUT", "UNLOCK", "UNSUBSCRIBE", "UPDATE", "VERSIONCONTROL", "BASELINECONTROL", "XMSENUMATTS", "RPC_OUT_DATA", "RPC_IN_DATA", "JSON", "COOK", "TRACK"]] | NotGiven = NOT_GIVEN,
    http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
    ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
    location: List[str] | NotGiven = NOT_GIVEN,
    mitigation_product: List[Literal["DDOS", "WAF", "BOT_MANAGEMENT", "ACCESS_RULES", "IP_REPUTATION", "API_SHIELD", "DATA_LOSS_PREVENTION"]] | NotGiven = NOT_GIVEN,
    name: List[str] | NotGiven = NOT_GIVEN,
    normalization: Literal["PERCENTAGE_CHANGE", "MIN0_MAX"] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Layer7TimeseriesResponse:
        """Get a timeseries of Layer 7 attacks.

        Values represent HTTP requests and are
        normalized using min-max by default.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          attack: This field is deprecated, please use the new `mitigationProduct`.

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          http_method: Filter for http method.

          http_version: Filter for http version.

          ip_version: Filter for ip version.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          mitigation_product: Array of L7 mitigation products.

          name: Array of names that will be used to name the series in responses.

          normalization: Normalization method applied. Refer to
              [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/attacks/layer7/timeseries",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "agg_interval": agg_interval,
                "asn": asn,
                "attack": attack,
                "continent": continent,
                "date_end": date_end,
                "date_range": date_range,
                "date_start": date_start,
                "format": format,
                "http_method": http_method,
                "http_version": http_version,
                "ip_version": ip_version,
                "location": location,
                "mitigation_product": mitigation_product,
                "name": name,
                "normalization": normalization,
            }, layer7_timeseries_params.Layer7TimeseriesParams), post_parser=ResultWrapper[Layer7TimeseriesResponse]._unwrapper),
            cast_to=cast(Type[Layer7TimeseriesResponse], ResultWrapper[Layer7TimeseriesResponse]),
        )

class Layer7ResourceWithRawResponse:
    def __init__(self, layer7: Layer7Resource) -> None:
        self._layer7 = layer7

        self.timeseries = to_raw_response_wrapper(
            layer7.timeseries,
        )

    @cached_property
    def summary(self) -> SummaryResourceWithRawResponse:
        return SummaryResourceWithRawResponse(self._layer7.summary)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResourceWithRawResponse:
        return TimeseriesGroupsResourceWithRawResponse(self._layer7.timeseries_groups)

    @cached_property
    def top(self) -> TopResourceWithRawResponse:
        return TopResourceWithRawResponse(self._layer7.top)

class AsyncLayer7ResourceWithRawResponse:
    def __init__(self, layer7: AsyncLayer7Resource) -> None:
        self._layer7 = layer7

        self.timeseries = async_to_raw_response_wrapper(
            layer7.timeseries,
        )

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithRawResponse:
        return AsyncSummaryResourceWithRawResponse(self._layer7.summary)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResourceWithRawResponse:
        return AsyncTimeseriesGroupsResourceWithRawResponse(self._layer7.timeseries_groups)

    @cached_property
    def top(self) -> AsyncTopResourceWithRawResponse:
        return AsyncTopResourceWithRawResponse(self._layer7.top)

class Layer7ResourceWithStreamingResponse:
    def __init__(self, layer7: Layer7Resource) -> None:
        self._layer7 = layer7

        self.timeseries = to_streamed_response_wrapper(
            layer7.timeseries,
        )

    @cached_property
    def summary(self) -> SummaryResourceWithStreamingResponse:
        return SummaryResourceWithStreamingResponse(self._layer7.summary)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResourceWithStreamingResponse:
        return TimeseriesGroupsResourceWithStreamingResponse(self._layer7.timeseries_groups)

    @cached_property
    def top(self) -> TopResourceWithStreamingResponse:
        return TopResourceWithStreamingResponse(self._layer7.top)

class AsyncLayer7ResourceWithStreamingResponse:
    def __init__(self, layer7: AsyncLayer7Resource) -> None:
        self._layer7 = layer7

        self.timeseries = async_to_streamed_response_wrapper(
            layer7.timeseries,
        )

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithStreamingResponse:
        return AsyncSummaryResourceWithStreamingResponse(self._layer7.summary)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResourceWithStreamingResponse:
        return AsyncTimeseriesGroupsResourceWithStreamingResponse(self._layer7.timeseries_groups)

    @cached_property
    def top(self) -> AsyncTopResourceWithStreamingResponse:
        return AsyncTopResourceWithStreamingResponse(self._layer7.top)