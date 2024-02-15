# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.radar.bgp import (
    RouteMoasResponse,
    RouteStatsResponse,
    RoutePfx2asResponse,
    route_moas_params,
    route_stats_params,
    route_pfx2as_params,
)

__all__ = ["Routes", "AsyncRoutes"]


class Routes(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RoutesWithRawResponse:
        return RoutesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoutesWithStreamingResponse:
        return RoutesWithStreamingResponse(self)

    def moas(
        self,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteMoasResponse:
        """
        List all Multi-origin AS (MOAS) prefixes on the global routing tables.

        Args:
          format: Format results are returned in.

          invalid_only: Lookup only RPKI invalid MOASes

          origin: Lookup MOASes originated by the given ASN

          prefix: Lookup MOASes by prefix

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/bgp/routes/moas",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "format": format,
                        "invalid_only": invalid_only,
                        "origin": origin,
                        "prefix": prefix,
                    },
                    route_moas_params.RouteMoasParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RouteMoasResponse], ResultWrapper[RouteMoasResponse]),
        )

    def pfx2as(
        self,
        *,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        origin: int | NotGiven = NOT_GIVEN,
        prefix: str | NotGiven = NOT_GIVEN,
        rpki_status: Literal["VALID", "INVALID", "UNKNOWN"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoutePfx2asResponse:
        """
        Lookup prefix-to-origin mapping on global routing tables.

        Args:
          format: Format results are returned in.

          origin: Lookup prefixes originated by the given ASN

          prefix: Lookup origins of the given prefix

          rpki_status: Return only results with matching rpki status: valid, invalid or unknown

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/bgp/routes/pfx2as",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "format": format,
                        "origin": origin,
                        "prefix": prefix,
                        "rpki_status": rpki_status,
                    },
                    route_pfx2as_params.RoutePfx2asParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RoutePfx2asResponse], ResultWrapper[RoutePfx2asResponse]),
        )

    def stats(
        self,
        *,
        asn: int | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteStatsResponse:
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
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asn": asn,
                        "format": format,
                        "location": location,
                    },
                    route_stats_params.RouteStatsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RouteStatsResponse], ResultWrapper[RouteStatsResponse]),
        )


class AsyncRoutes(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRoutesWithRawResponse:
        return AsyncRoutesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoutesWithStreamingResponse:
        return AsyncRoutesWithStreamingResponse(self)

    async def moas(
        self,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteMoasResponse:
        """
        List all Multi-origin AS (MOAS) prefixes on the global routing tables.

        Args:
          format: Format results are returned in.

          invalid_only: Lookup only RPKI invalid MOASes

          origin: Lookup MOASes originated by the given ASN

          prefix: Lookup MOASes by prefix

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/bgp/routes/moas",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "format": format,
                        "invalid_only": invalid_only,
                        "origin": origin,
                        "prefix": prefix,
                    },
                    route_moas_params.RouteMoasParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RouteMoasResponse], ResultWrapper[RouteMoasResponse]),
        )

    async def pfx2as(
        self,
        *,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        origin: int | NotGiven = NOT_GIVEN,
        prefix: str | NotGiven = NOT_GIVEN,
        rpki_status: Literal["VALID", "INVALID", "UNKNOWN"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoutePfx2asResponse:
        """
        Lookup prefix-to-origin mapping on global routing tables.

        Args:
          format: Format results are returned in.

          origin: Lookup prefixes originated by the given ASN

          prefix: Lookup origins of the given prefix

          rpki_status: Return only results with matching rpki status: valid, invalid or unknown

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/bgp/routes/pfx2as",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "format": format,
                        "origin": origin,
                        "prefix": prefix,
                        "rpki_status": rpki_status,
                    },
                    route_pfx2as_params.RoutePfx2asParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RoutePfx2asResponse], ResultWrapper[RoutePfx2asResponse]),
        )

    async def stats(
        self,
        *,
        asn: int | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteStatsResponse:
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
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asn": asn,
                        "format": format,
                        "location": location,
                    },
                    route_stats_params.RouteStatsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RouteStatsResponse], ResultWrapper[RouteStatsResponse]),
        )


class RoutesWithRawResponse:
    def __init__(self, routes: Routes) -> None:
        self._routes = routes

        self.moas = to_raw_response_wrapper(
            routes.moas,
        )
        self.pfx2as = to_raw_response_wrapper(
            routes.pfx2as,
        )
        self.stats = to_raw_response_wrapper(
            routes.stats,
        )


class AsyncRoutesWithRawResponse:
    def __init__(self, routes: AsyncRoutes) -> None:
        self._routes = routes

        self.moas = async_to_raw_response_wrapper(
            routes.moas,
        )
        self.pfx2as = async_to_raw_response_wrapper(
            routes.pfx2as,
        )
        self.stats = async_to_raw_response_wrapper(
            routes.stats,
        )


class RoutesWithStreamingResponse:
    def __init__(self, routes: Routes) -> None:
        self._routes = routes

        self.moas = to_streamed_response_wrapper(
            routes.moas,
        )
        self.pfx2as = to_streamed_response_wrapper(
            routes.pfx2as,
        )
        self.stats = to_streamed_response_wrapper(
            routes.stats,
        )


class AsyncRoutesWithStreamingResponse:
    def __init__(self, routes: AsyncRoutes) -> None:
        self._routes = routes

        self.moas = async_to_streamed_response_wrapper(
            routes.moas,
        )
        self.pfx2as = async_to_streamed_response_wrapper(
            routes.pfx2as,
        )
        self.stats = async_to_streamed_response_wrapper(
            routes.stats,
        )
