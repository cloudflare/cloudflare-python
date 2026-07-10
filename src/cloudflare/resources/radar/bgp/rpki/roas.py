# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
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
from .....types.radar.bgp.rpki import roa_timeseries_params
from .....types.radar.bgp.rpki.roa_timeseries_response import RoaTimeseriesResponse

__all__ = ["RoasResource", "AsyncRoasResource"]


class RoasResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RoasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RoasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RoasResourceWithStreamingResponse(self)

    def timeseries(
        self,
        *,
        asn: SequenceNotStr[str] | Omit = omit,
        date_end: Union[str, datetime] | Omit = omit,
        date_start: Union[str, datetime] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        metric: Literal[
            "validPfxsRatio",
            "validPfxsV4Ratio",
            "validPfxsV6Ratio",
            "validIpsRatio",
            "validIpsV4Ratio",
            "validIpsV6Ratio",
        ]
        | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoaTimeseriesResponse:
        """
        Retrieves RPKI ROA (Route Origin Authorization) validation ratios over time.
        Returns the selected metric as a time series. Supports filtering by ASN or
        location (country code) — multiple values of the same filter type produce one
        series per value. If no ASN or location is specified, returns the global
        aggregate.

        Args:
          asn: Filters results by Autonomous System Number. Specify one or more ASNs. Multiple
              values generate one series per ASN.

          date_end: End of the date range (inclusive).

          date_start: Start of the date range (inclusive).

          format: Format in which results will be returned.

          location: Filters results by location. Specify a comma-separated list of alpha-2 location
              codes.

          metric: Which RPKI ROA validation metric to return. validPfxsRatio = ratio of RPKI-valid
              prefixes (IPv4+IPv6 combined). validPfxsV4Ratio / validPfxsV6Ratio = same, split
              by IP version. validIpsRatio = ratio of RPKI-valid address space (IPv4 /24s +
              IPv6 /48s). validIpsV4Ratio / validIpsV6Ratio = same, split by IP version.

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/bgp/rpki/roas/timeseries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asn": asn,
                        "date_end": date_end,
                        "date_start": date_start,
                        "format": format,
                        "location": location,
                        "metric": metric,
                        "name": name,
                    },
                    roa_timeseries_params.RoaTimeseriesParams,
                ),
                post_parser=ResultWrapper[RoaTimeseriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[RoaTimeseriesResponse], ResultWrapper[RoaTimeseriesResponse]),
        )


class AsyncRoasResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRoasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRoasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRoasResourceWithStreamingResponse(self)

    async def timeseries(
        self,
        *,
        asn: SequenceNotStr[str] | Omit = omit,
        date_end: Union[str, datetime] | Omit = omit,
        date_start: Union[str, datetime] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        metric: Literal[
            "validPfxsRatio",
            "validPfxsV4Ratio",
            "validPfxsV6Ratio",
            "validIpsRatio",
            "validIpsV4Ratio",
            "validIpsV6Ratio",
        ]
        | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoaTimeseriesResponse:
        """
        Retrieves RPKI ROA (Route Origin Authorization) validation ratios over time.
        Returns the selected metric as a time series. Supports filtering by ASN or
        location (country code) — multiple values of the same filter type produce one
        series per value. If no ASN or location is specified, returns the global
        aggregate.

        Args:
          asn: Filters results by Autonomous System Number. Specify one or more ASNs. Multiple
              values generate one series per ASN.

          date_end: End of the date range (inclusive).

          date_start: Start of the date range (inclusive).

          format: Format in which results will be returned.

          location: Filters results by location. Specify a comma-separated list of alpha-2 location
              codes.

          metric: Which RPKI ROA validation metric to return. validPfxsRatio = ratio of RPKI-valid
              prefixes (IPv4+IPv6 combined). validPfxsV4Ratio / validPfxsV6Ratio = same, split
              by IP version. validIpsRatio = ratio of RPKI-valid address space (IPv4 /24s +
              IPv6 /48s). validIpsV4Ratio / validIpsV6Ratio = same, split by IP version.

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/bgp/rpki/roas/timeseries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asn": asn,
                        "date_end": date_end,
                        "date_start": date_start,
                        "format": format,
                        "location": location,
                        "metric": metric,
                        "name": name,
                    },
                    roa_timeseries_params.RoaTimeseriesParams,
                ),
                post_parser=ResultWrapper[RoaTimeseriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[RoaTimeseriesResponse], ResultWrapper[RoaTimeseriesResponse]),
        )


class RoasResourceWithRawResponse:
    def __init__(self, roas: RoasResource) -> None:
        self._roas = roas

        self.timeseries = to_raw_response_wrapper(
            roas.timeseries,
        )


class AsyncRoasResourceWithRawResponse:
    def __init__(self, roas: AsyncRoasResource) -> None:
        self._roas = roas

        self.timeseries = async_to_raw_response_wrapper(
            roas.timeseries,
        )


class RoasResourceWithStreamingResponse:
    def __init__(self, roas: RoasResource) -> None:
        self._roas = roas

        self.timeseries = to_streamed_response_wrapper(
            roas.timeseries,
        )


class AsyncRoasResourceWithStreamingResponse:
    def __init__(self, roas: AsyncRoasResource) -> None:
        self._roas = roas

        self.timeseries = async_to_streamed_response_wrapper(
            roas.timeseries,
        )
