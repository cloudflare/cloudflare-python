# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.radar.bgp.route_ases_response import RouteAsesResponse

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from ...._base_client import make_request_options

from typing import Type

from typing_extensions import Literal

from ....types.radar.bgp.route_moas_response import RouteMoasResponse

from ....types.radar.bgp.route_pfx2as_response import RoutePfx2asResponse

from ....types.radar.bgp.route_stats_response import RouteStatsResponse

from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.radar.bgp import route_ases_params
from ....types.radar.bgp import route_moas_params
from ....types.radar.bgp import route_pfx2as_params
from ....types.radar.bgp import route_stats_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["RoutesResource", "AsyncRoutesResource"]

class RoutesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RoutesResourceWithRawResponse:
        return RoutesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoutesResourceWithStreamingResponse:
        return RoutesResourceWithStreamingResponse(self)

    def ases(self,
    *,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    limit: int | NotGiven = NOT_GIVEN,
    location: str | NotGiven = NOT_GIVEN,
    sort_by: Literal["cone", "pfxs", "ipv4", "ipv6", "rpki_valid", "rpki_invalid", "rpki_unknown"] | NotGiven = NOT_GIVEN,
    sort_order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RouteAsesResponse:
        """
        List all ASes on current global routing tables with routing statistics

        Args:
          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          location: Location Alpha2 code.

          sort_by: Return order results by given type

          sort_order: Sort by value ascending or descending

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/bgp/routes/ases",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "format": format,
                "limit": limit,
                "location": location,
                "sort_by": sort_by,
                "sort_order": sort_order,
            }, route_ases_params.RouteAsesParams), post_parser=ResultWrapper[RouteAsesResponse]._unwrapper),
            cast_to=cast(Type[RouteAsesResponse], ResultWrapper[RouteAsesResponse]),
        )

    def moas(self,
    *,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    invalid_only: bool | NotGiven = NOT_GIVEN,
    origin: int | NotGiven = NOT_GIVEN,
    prefix: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RouteMoasResponse:
        """
        List all Multi-origin AS (MOAS) prefixes on the global routing tables.

        Args:
          format: Format results are returned in.

          invalid_only: Lookup only RPKI invalid MOASes

          origin: Lookup MOASes originated by the given ASN

          prefix: Network prefix, IPv4 or IPv6.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/bgp/routes/moas",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "format": format,
                "invalid_only": invalid_only,
                "origin": origin,
                "prefix": prefix,
            }, route_moas_params.RouteMoasParams), post_parser=ResultWrapper[RouteMoasResponse]._unwrapper),
            cast_to=cast(Type[RouteMoasResponse], ResultWrapper[RouteMoasResponse]),
        )

    def pfx2as(self,
    *,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    longest_prefix_match: bool | NotGiven = NOT_GIVEN,
    origin: int | NotGiven = NOT_GIVEN,
    prefix: str | NotGiven = NOT_GIVEN,
    rpki_status: Literal["VALID", "INVALID", "UNKNOWN"] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RoutePfx2asResponse:
        """
        Lookup prefix-to-ASN mapping on global routing tables.

        Args:
          format: Format results are returned in.

          longest_prefix_match: Return only results with the longest prefix match for the given prefix. For
              example, specify a /32 prefix to lookup the origin ASN for an IPv4 address.

          origin: Lookup prefixes originated by the given ASN

          prefix: Network prefix, IPv4 or IPv6.

          rpki_status: Return only results with matching rpki status: valid, invalid or unknown

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/bgp/routes/pfx2as",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "format": format,
                "longest_prefix_match": longest_prefix_match,
                "origin": origin,
                "prefix": prefix,
                "rpki_status": rpki_status,
            }, route_pfx2as_params.RoutePfx2asParams), post_parser=ResultWrapper[RoutePfx2asResponse]._unwrapper),
            cast_to=cast(Type[RoutePfx2asResponse], ResultWrapper[RoutePfx2asResponse]),
        )

    def stats(self,
    *,
    asn: int | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    location: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RouteStatsResponse:
        """
        Get the BGP routing table stats (Beta).

        Args:
          asn: Single ASN as integer.

          format: Format results are returned in.

          location: Location Alpha2 code.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/bgp/routes/stats",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "asn": asn,
                "format": format,
                "location": location,
            }, route_stats_params.RouteStatsParams), post_parser=ResultWrapper[RouteStatsResponse]._unwrapper),
            cast_to=cast(Type[RouteStatsResponse], ResultWrapper[RouteStatsResponse]),
        )

class AsyncRoutesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRoutesResourceWithRawResponse:
        return AsyncRoutesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoutesResourceWithStreamingResponse:
        return AsyncRoutesResourceWithStreamingResponse(self)

    async def ases(self,
    *,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    limit: int | NotGiven = NOT_GIVEN,
    location: str | NotGiven = NOT_GIVEN,
    sort_by: Literal["cone", "pfxs", "ipv4", "ipv6", "rpki_valid", "rpki_invalid", "rpki_unknown"] | NotGiven = NOT_GIVEN,
    sort_order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RouteAsesResponse:
        """
        List all ASes on current global routing tables with routing statistics

        Args:
          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          location: Location Alpha2 code.

          sort_by: Return order results by given type

          sort_order: Sort by value ascending or descending

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/bgp/routes/ases",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "format": format,
                "limit": limit,
                "location": location,
                "sort_by": sort_by,
                "sort_order": sort_order,
            }, route_ases_params.RouteAsesParams), post_parser=ResultWrapper[RouteAsesResponse]._unwrapper),
            cast_to=cast(Type[RouteAsesResponse], ResultWrapper[RouteAsesResponse]),
        )

    async def moas(self,
    *,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    invalid_only: bool | NotGiven = NOT_GIVEN,
    origin: int | NotGiven = NOT_GIVEN,
    prefix: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RouteMoasResponse:
        """
        List all Multi-origin AS (MOAS) prefixes on the global routing tables.

        Args:
          format: Format results are returned in.

          invalid_only: Lookup only RPKI invalid MOASes

          origin: Lookup MOASes originated by the given ASN

          prefix: Network prefix, IPv4 or IPv6.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/bgp/routes/moas",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "format": format,
                "invalid_only": invalid_only,
                "origin": origin,
                "prefix": prefix,
            }, route_moas_params.RouteMoasParams), post_parser=ResultWrapper[RouteMoasResponse]._unwrapper),
            cast_to=cast(Type[RouteMoasResponse], ResultWrapper[RouteMoasResponse]),
        )

    async def pfx2as(self,
    *,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    longest_prefix_match: bool | NotGiven = NOT_GIVEN,
    origin: int | NotGiven = NOT_GIVEN,
    prefix: str | NotGiven = NOT_GIVEN,
    rpki_status: Literal["VALID", "INVALID", "UNKNOWN"] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RoutePfx2asResponse:
        """
        Lookup prefix-to-ASN mapping on global routing tables.

        Args:
          format: Format results are returned in.

          longest_prefix_match: Return only results with the longest prefix match for the given prefix. For
              example, specify a /32 prefix to lookup the origin ASN for an IPv4 address.

          origin: Lookup prefixes originated by the given ASN

          prefix: Network prefix, IPv4 or IPv6.

          rpki_status: Return only results with matching rpki status: valid, invalid or unknown

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/bgp/routes/pfx2as",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "format": format,
                "longest_prefix_match": longest_prefix_match,
                "origin": origin,
                "prefix": prefix,
                "rpki_status": rpki_status,
            }, route_pfx2as_params.RoutePfx2asParams), post_parser=ResultWrapper[RoutePfx2asResponse]._unwrapper),
            cast_to=cast(Type[RoutePfx2asResponse], ResultWrapper[RoutePfx2asResponse]),
        )

    async def stats(self,
    *,
    asn: int | NotGiven = NOT_GIVEN,
    format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
    location: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RouteStatsResponse:
        """
        Get the BGP routing table stats (Beta).

        Args:
          asn: Single ASN as integer.

          format: Format results are returned in.

          location: Location Alpha2 code.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/bgp/routes/stats",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "asn": asn,
                "format": format,
                "location": location,
            }, route_stats_params.RouteStatsParams), post_parser=ResultWrapper[RouteStatsResponse]._unwrapper),
            cast_to=cast(Type[RouteStatsResponse], ResultWrapper[RouteStatsResponse]),
        )

class RoutesResourceWithRawResponse:
    def __init__(self, routes: RoutesResource) -> None:
        self._routes = routes

        self.ases = to_raw_response_wrapper(
            routes.ases,
        )
        self.moas = to_raw_response_wrapper(
            routes.moas,
        )
        self.pfx2as = to_raw_response_wrapper(
            routes.pfx2as,
        )
        self.stats = to_raw_response_wrapper(
            routes.stats,
        )

class AsyncRoutesResourceWithRawResponse:
    def __init__(self, routes: AsyncRoutesResource) -> None:
        self._routes = routes

        self.ases = async_to_raw_response_wrapper(
            routes.ases,
        )
        self.moas = async_to_raw_response_wrapper(
            routes.moas,
        )
        self.pfx2as = async_to_raw_response_wrapper(
            routes.pfx2as,
        )
        self.stats = async_to_raw_response_wrapper(
            routes.stats,
        )

class RoutesResourceWithStreamingResponse:
    def __init__(self, routes: RoutesResource) -> None:
        self._routes = routes

        self.ases = to_streamed_response_wrapper(
            routes.ases,
        )
        self.moas = to_streamed_response_wrapper(
            routes.moas,
        )
        self.pfx2as = to_streamed_response_wrapper(
            routes.pfx2as,
        )
        self.stats = to_streamed_response_wrapper(
            routes.stats,
        )

class AsyncRoutesResourceWithStreamingResponse:
    def __init__(self, routes: AsyncRoutesResource) -> None:
        self._routes = routes

        self.ases = async_to_streamed_response_wrapper(
            routes.ases,
        )
        self.moas = async_to_streamed_response_wrapper(
            routes.moas,
        )
        self.pfx2as = async_to_streamed_response_wrapper(
            routes.pfx2as,
        )
        self.stats = async_to_streamed_response_wrapper(
            routes.stats,
        )