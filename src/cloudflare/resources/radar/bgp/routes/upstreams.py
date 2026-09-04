# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from .....types.radar.bgp.routes import upstream_timeseries_params
from .....types.radar.bgp.routes.upstream_timeseries_response import UpstreamTimeseriesResponse

__all__ = ["UpstreamsResource", "AsyncUpstreamsResource"]


class UpstreamsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UpstreamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return UpstreamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UpstreamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return UpstreamsResourceWithStreamingResponse(self)

    def timeseries(
        self,
        asn: int,
        *,
        date_end: Union[str, datetime] | Omit = omit,
        date_start: Union[str, datetime] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        ip_version: Literal["IPv4", "IPv6"] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UpstreamTimeseriesResponse:
        """
        Retrieves the share of an AS’s observed paths carried by each direct upstream
        over time, derived from RouteViews RIB snapshots across all collectors (the
        combined product). Each upstream ASN is returned as its own series of shares
        (0–1); the least-significant upstreams beyond the requested limit are grouped
        into an "OTHER" series. Series share a common set of timestamps.

        Args:
          asn: Single Autonomous System Number (ASN) as integer.

          date_end: End of the date range (inclusive). Alternative to `dateRange`; provide together
              with `dateStart`.

          date_start: Start of the date range (inclusive). Alternative to `dateRange`; provide
              together with `dateEnd`.

          format: Format in which results will be returned.

          ip_version: Address family of the observed paths. Defaults to IPv4.

          limit: Number of upstream ASNs to return as separate series, ranked by the first
              bucket. Remaining upstreams are grouped into an "OTHER" series. Defaults to 5.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/radar/bgp/routes/upstreams/{asn}/timeseries", asn=asn),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date_end": date_end,
                        "date_start": date_start,
                        "format": format,
                        "ip_version": ip_version,
                        "limit": limit,
                    },
                    upstream_timeseries_params.UpstreamTimeseriesParams,
                ),
                post_parser=ResultWrapper[UpstreamTimeseriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[UpstreamTimeseriesResponse], ResultWrapper[UpstreamTimeseriesResponse]),
        )


class AsyncUpstreamsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUpstreamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUpstreamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUpstreamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncUpstreamsResourceWithStreamingResponse(self)

    async def timeseries(
        self,
        asn: int,
        *,
        date_end: Union[str, datetime] | Omit = omit,
        date_start: Union[str, datetime] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        ip_version: Literal["IPv4", "IPv6"] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UpstreamTimeseriesResponse:
        """
        Retrieves the share of an AS’s observed paths carried by each direct upstream
        over time, derived from RouteViews RIB snapshots across all collectors (the
        combined product). Each upstream ASN is returned as its own series of shares
        (0–1); the least-significant upstreams beyond the requested limit are grouped
        into an "OTHER" series. Series share a common set of timestamps.

        Args:
          asn: Single Autonomous System Number (ASN) as integer.

          date_end: End of the date range (inclusive). Alternative to `dateRange`; provide together
              with `dateStart`.

          date_start: Start of the date range (inclusive). Alternative to `dateRange`; provide
              together with `dateEnd`.

          format: Format in which results will be returned.

          ip_version: Address family of the observed paths. Defaults to IPv4.

          limit: Number of upstream ASNs to return as separate series, ranked by the first
              bucket. Remaining upstreams are grouped into an "OTHER" series. Defaults to 5.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/radar/bgp/routes/upstreams/{asn}/timeseries", asn=asn),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date_end": date_end,
                        "date_start": date_start,
                        "format": format,
                        "ip_version": ip_version,
                        "limit": limit,
                    },
                    upstream_timeseries_params.UpstreamTimeseriesParams,
                ),
                post_parser=ResultWrapper[UpstreamTimeseriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[UpstreamTimeseriesResponse], ResultWrapper[UpstreamTimeseriesResponse]),
        )


class UpstreamsResourceWithRawResponse:
    def __init__(self, upstreams: UpstreamsResource) -> None:
        self._upstreams = upstreams

        self.timeseries = to_raw_response_wrapper(
            upstreams.timeseries,
        )


class AsyncUpstreamsResourceWithRawResponse:
    def __init__(self, upstreams: AsyncUpstreamsResource) -> None:
        self._upstreams = upstreams

        self.timeseries = async_to_raw_response_wrapper(
            upstreams.timeseries,
        )


class UpstreamsResourceWithStreamingResponse:
    def __init__(self, upstreams: UpstreamsResource) -> None:
        self._upstreams = upstreams

        self.timeseries = to_streamed_response_wrapper(
            upstreams.timeseries,
        )


class AsyncUpstreamsResourceWithStreamingResponse:
    def __init__(self, upstreams: AsyncUpstreamsResource) -> None:
        self._upstreams = upstreams

        self.timeseries = async_to_streamed_response_wrapper(
            upstreams.timeseries,
        )
