# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .leaks.leaks import LeaksResource, AsyncLeaksResource

from ...._compat import cached_property

from .top.top import TopResource, AsyncTopResource

from .hijacks.hijacks import HijacksResource, AsyncHijacksResource

from .routes import RoutesResource, AsyncRoutesResource

from .ips import IPsResource, AsyncIPsResource

from ....types.radar.bgp_timeseries_response import BGPTimeseriesResponse

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from ...._base_client import make_request_options

from typing import Type, List, Union

from typing_extensions import Literal

from datetime import datetime

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.radar import bgp_timeseries_params
from .leaks import (
    LeaksResource,
    AsyncLeaksResource,
    LeaksResourceWithRawResponse,
    AsyncLeaksResourceWithRawResponse,
    LeaksResourceWithStreamingResponse,
    AsyncLeaksResourceWithStreamingResponse,
)
from .top import (
    TopResource,
    AsyncTopResource,
    TopResourceWithRawResponse,
    AsyncTopResourceWithRawResponse,
    TopResourceWithStreamingResponse,
    AsyncTopResourceWithStreamingResponse,
)
from .hijacks import (
    HijacksResource,
    AsyncHijacksResource,
    HijacksResourceWithRawResponse,
    AsyncHijacksResourceWithRawResponse,
    HijacksResourceWithStreamingResponse,
    AsyncHijacksResourceWithStreamingResponse,
)
from .routes import (
    RoutesResource,
    AsyncRoutesResource,
    RoutesResourceWithRawResponse,
    AsyncRoutesResourceWithRawResponse,
    RoutesResourceWithStreamingResponse,
    AsyncRoutesResourceWithStreamingResponse,
)
from .ips import (
    IPsResource,
    AsyncIPsResource,
    IPsResourceWithRawResponse,
    AsyncIPsResourceWithRawResponse,
    IPsResourceWithStreamingResponse,
    AsyncIPsResourceWithStreamingResponse,
)
from typing import cast
from typing import cast

__all__ = ["BGPResource", "AsyncBGPResource"]


class BGPResource(SyncAPIResource):
    @cached_property
    def leaks(self) -> LeaksResource:
        return LeaksResource(self._client)

    @cached_property
    def top(self) -> TopResource:
        return TopResource(self._client)

    @cached_property
    def hijacks(self) -> HijacksResource:
        return HijacksResource(self._client)

    @cached_property
    def routes(self) -> RoutesResource:
        return RoutesResource(self._client)

    @cached_property
    def ips(self) -> IPsResource:
        return IPsResource(self._client)

    @cached_property
    def with_raw_response(self) -> BGPResourceWithRawResponse:
        return BGPResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BGPResourceWithStreamingResponse:
        return BGPResourceWithStreamingResponse(self)

    def timeseries(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        asn: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        prefix: List[str] | NotGiven = NOT_GIVEN,
        update_type: List[Literal["ANNOUNCEMENT", "WITHDRAWAL"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BGPTimeseriesResponse:
        """Gets BGP updates change over time.

        Raw values are returned. When requesting
        updates of an autonomous system (AS), only BGP updates of type announcement are
        returned.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          name: Array of names that will be used to name the series in responses.

          prefix: Array of BGP network prefixes.

          update_type: Array of BGP update types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/bgp/timeseries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "asn": asn,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "name": name,
                        "prefix": prefix,
                        "update_type": update_type,
                    },
                    bgp_timeseries_params.BGPTimeseriesParams,
                ),
                post_parser=ResultWrapper[BGPTimeseriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[BGPTimeseriesResponse], ResultWrapper[BGPTimeseriesResponse]),
        )


class AsyncBGPResource(AsyncAPIResource):
    @cached_property
    def leaks(self) -> AsyncLeaksResource:
        return AsyncLeaksResource(self._client)

    @cached_property
    def top(self) -> AsyncTopResource:
        return AsyncTopResource(self._client)

    @cached_property
    def hijacks(self) -> AsyncHijacksResource:
        return AsyncHijacksResource(self._client)

    @cached_property
    def routes(self) -> AsyncRoutesResource:
        return AsyncRoutesResource(self._client)

    @cached_property
    def ips(self) -> AsyncIPsResource:
        return AsyncIPsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBGPResourceWithRawResponse:
        return AsyncBGPResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBGPResourceWithStreamingResponse:
        return AsyncBGPResourceWithStreamingResponse(self)

    async def timeseries(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        asn: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        prefix: List[str] | NotGiven = NOT_GIVEN,
        update_type: List[Literal["ANNOUNCEMENT", "WITHDRAWAL"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BGPTimeseriesResponse:
        """Gets BGP updates change over time.

        Raw values are returned. When requesting
        updates of an autonomous system (AS), only BGP updates of type announcement are
        returned.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          name: Array of names that will be used to name the series in responses.

          prefix: Array of BGP network prefixes.

          update_type: Array of BGP update types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/bgp/timeseries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "asn": asn,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "name": name,
                        "prefix": prefix,
                        "update_type": update_type,
                    },
                    bgp_timeseries_params.BGPTimeseriesParams,
                ),
                post_parser=ResultWrapper[BGPTimeseriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[BGPTimeseriesResponse], ResultWrapper[BGPTimeseriesResponse]),
        )


class BGPResourceWithRawResponse:
    def __init__(self, bgp: BGPResource) -> None:
        self._bgp = bgp

        self.timeseries = to_raw_response_wrapper(
            bgp.timeseries,
        )

    @cached_property
    def leaks(self) -> LeaksResourceWithRawResponse:
        return LeaksResourceWithRawResponse(self._bgp.leaks)

    @cached_property
    def top(self) -> TopResourceWithRawResponse:
        return TopResourceWithRawResponse(self._bgp.top)

    @cached_property
    def hijacks(self) -> HijacksResourceWithRawResponse:
        return HijacksResourceWithRawResponse(self._bgp.hijacks)

    @cached_property
    def routes(self) -> RoutesResourceWithRawResponse:
        return RoutesResourceWithRawResponse(self._bgp.routes)

    @cached_property
    def ips(self) -> IPsResourceWithRawResponse:
        return IPsResourceWithRawResponse(self._bgp.ips)


class AsyncBGPResourceWithRawResponse:
    def __init__(self, bgp: AsyncBGPResource) -> None:
        self._bgp = bgp

        self.timeseries = async_to_raw_response_wrapper(
            bgp.timeseries,
        )

    @cached_property
    def leaks(self) -> AsyncLeaksResourceWithRawResponse:
        return AsyncLeaksResourceWithRawResponse(self._bgp.leaks)

    @cached_property
    def top(self) -> AsyncTopResourceWithRawResponse:
        return AsyncTopResourceWithRawResponse(self._bgp.top)

    @cached_property
    def hijacks(self) -> AsyncHijacksResourceWithRawResponse:
        return AsyncHijacksResourceWithRawResponse(self._bgp.hijacks)

    @cached_property
    def routes(self) -> AsyncRoutesResourceWithRawResponse:
        return AsyncRoutesResourceWithRawResponse(self._bgp.routes)

    @cached_property
    def ips(self) -> AsyncIPsResourceWithRawResponse:
        return AsyncIPsResourceWithRawResponse(self._bgp.ips)


class BGPResourceWithStreamingResponse:
    def __init__(self, bgp: BGPResource) -> None:
        self._bgp = bgp

        self.timeseries = to_streamed_response_wrapper(
            bgp.timeseries,
        )

    @cached_property
    def leaks(self) -> LeaksResourceWithStreamingResponse:
        return LeaksResourceWithStreamingResponse(self._bgp.leaks)

    @cached_property
    def top(self) -> TopResourceWithStreamingResponse:
        return TopResourceWithStreamingResponse(self._bgp.top)

    @cached_property
    def hijacks(self) -> HijacksResourceWithStreamingResponse:
        return HijacksResourceWithStreamingResponse(self._bgp.hijacks)

    @cached_property
    def routes(self) -> RoutesResourceWithStreamingResponse:
        return RoutesResourceWithStreamingResponse(self._bgp.routes)

    @cached_property
    def ips(self) -> IPsResourceWithStreamingResponse:
        return IPsResourceWithStreamingResponse(self._bgp.ips)


class AsyncBGPResourceWithStreamingResponse:
    def __init__(self, bgp: AsyncBGPResource) -> None:
        self._bgp = bgp

        self.timeseries = async_to_streamed_response_wrapper(
            bgp.timeseries,
        )

    @cached_property
    def leaks(self) -> AsyncLeaksResourceWithStreamingResponse:
        return AsyncLeaksResourceWithStreamingResponse(self._bgp.leaks)

    @cached_property
    def top(self) -> AsyncTopResourceWithStreamingResponse:
        return AsyncTopResourceWithStreamingResponse(self._bgp.top)

    @cached_property
    def hijacks(self) -> AsyncHijacksResourceWithStreamingResponse:
        return AsyncHijacksResourceWithStreamingResponse(self._bgp.hijacks)

    @cached_property
    def routes(self) -> AsyncRoutesResourceWithStreamingResponse:
        return AsyncRoutesResourceWithStreamingResponse(self._bgp.routes)

    @cached_property
    def ips(self) -> AsyncIPsResourceWithStreamingResponse:
        return AsyncIPsResourceWithStreamingResponse(self._bgp.ips)
