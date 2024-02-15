# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from .ips import (
    IPs,
    AsyncIPs,
    IPsWithRawResponse,
    AsyncIPsWithRawResponse,
    IPsWithStreamingResponse,
    AsyncIPsWithStreamingResponse,
)
from .networks import (
    Networks,
    AsyncNetworks,
    NetworksWithRawResponse,
    AsyncNetworksWithRawResponse,
    NetworksWithStreamingResponse,
    AsyncNetworksWithStreamingResponse,
)
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
from ....types.teamnets import RouteTunnelRouteListTunnelRoutesResponse, route_tunnel_route_list_tunnel_routes_params

__all__ = ["Routes", "AsyncRoutes"]


class Routes(SyncAPIResource):
    @cached_property
    def ips(self) -> IPs:
        return IPs(self._client)

    @cached_property
    def networks(self) -> Networks:
        return Networks(self._client)

    @cached_property
    def with_raw_response(self) -> RoutesWithRawResponse:
        return RoutesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoutesWithStreamingResponse:
        return RoutesWithStreamingResponse(self)

    def tunnel_route_list_tunnel_routes(
        self,
        account_id: str,
        *,
        comment: str | NotGiven = NOT_GIVEN,
        existed_at: object | NotGiven = NOT_GIVEN,
        is_deleted: object | NotGiven = NOT_GIVEN,
        network_subset: object | NotGiven = NOT_GIVEN,
        network_superset: object | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        tun_types: str | NotGiven = NOT_GIVEN,
        tunnel_id: object | NotGiven = NOT_GIVEN,
        virtual_network_id: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RouteTunnelRouteListTunnelRoutesResponse]:
        """
        Lists and filters private network routes in an account.

        Args:
          account_id: Cloudflare account ID

          comment: Optional remark describing the route.

          existed_at: If provided, include only routes that were created (and not deleted) before this
              time.

          is_deleted: If `true`, only include deleted routes. If `false`, exclude deleted routes. If
              empty, all routes will be included.

          network_subset: If set, only list routes that are contained within this IP range.

          network_superset: If set, only list routes that contain this IP range.

          page: Page number of paginated results.

          per_page: Number of results to display.

          tun_types: The types of tunnels to filter separated by a comma.

          tunnel_id: UUID of the Cloudflare Tunnel serving the route.

          virtual_network_id: UUID of the Tunnel Virtual Network this route belongs to. If no virtual networks
              are configured, the route is assigned to the default virtual network of the
              account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/teamnet/routes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "comment": comment,
                        "existed_at": existed_at,
                        "is_deleted": is_deleted,
                        "network_subset": network_subset,
                        "network_superset": network_superset,
                        "page": page,
                        "per_page": per_page,
                        "tun_types": tun_types,
                        "tunnel_id": tunnel_id,
                        "virtual_network_id": virtual_network_id,
                    },
                    route_tunnel_route_list_tunnel_routes_params.RouteTunnelRouteListTunnelRoutesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RouteTunnelRouteListTunnelRoutesResponse]],
                ResultWrapper[RouteTunnelRouteListTunnelRoutesResponse],
            ),
        )


class AsyncRoutes(AsyncAPIResource):
    @cached_property
    def ips(self) -> AsyncIPs:
        return AsyncIPs(self._client)

    @cached_property
    def networks(self) -> AsyncNetworks:
        return AsyncNetworks(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRoutesWithRawResponse:
        return AsyncRoutesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoutesWithStreamingResponse:
        return AsyncRoutesWithStreamingResponse(self)

    async def tunnel_route_list_tunnel_routes(
        self,
        account_id: str,
        *,
        comment: str | NotGiven = NOT_GIVEN,
        existed_at: object | NotGiven = NOT_GIVEN,
        is_deleted: object | NotGiven = NOT_GIVEN,
        network_subset: object | NotGiven = NOT_GIVEN,
        network_superset: object | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        tun_types: str | NotGiven = NOT_GIVEN,
        tunnel_id: object | NotGiven = NOT_GIVEN,
        virtual_network_id: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RouteTunnelRouteListTunnelRoutesResponse]:
        """
        Lists and filters private network routes in an account.

        Args:
          account_id: Cloudflare account ID

          comment: Optional remark describing the route.

          existed_at: If provided, include only routes that were created (and not deleted) before this
              time.

          is_deleted: If `true`, only include deleted routes. If `false`, exclude deleted routes. If
              empty, all routes will be included.

          network_subset: If set, only list routes that are contained within this IP range.

          network_superset: If set, only list routes that contain this IP range.

          page: Page number of paginated results.

          per_page: Number of results to display.

          tun_types: The types of tunnels to filter separated by a comma.

          tunnel_id: UUID of the Cloudflare Tunnel serving the route.

          virtual_network_id: UUID of the Tunnel Virtual Network this route belongs to. If no virtual networks
              are configured, the route is assigned to the default virtual network of the
              account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/teamnet/routes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "comment": comment,
                        "existed_at": existed_at,
                        "is_deleted": is_deleted,
                        "network_subset": network_subset,
                        "network_superset": network_superset,
                        "page": page,
                        "per_page": per_page,
                        "tun_types": tun_types,
                        "tunnel_id": tunnel_id,
                        "virtual_network_id": virtual_network_id,
                    },
                    route_tunnel_route_list_tunnel_routes_params.RouteTunnelRouteListTunnelRoutesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RouteTunnelRouteListTunnelRoutesResponse]],
                ResultWrapper[RouteTunnelRouteListTunnelRoutesResponse],
            ),
        )


class RoutesWithRawResponse:
    def __init__(self, routes: Routes) -> None:
        self._routes = routes

        self.tunnel_route_list_tunnel_routes = to_raw_response_wrapper(
            routes.tunnel_route_list_tunnel_routes,
        )

    @cached_property
    def ips(self) -> IPsWithRawResponse:
        return IPsWithRawResponse(self._routes.ips)

    @cached_property
    def networks(self) -> NetworksWithRawResponse:
        return NetworksWithRawResponse(self._routes.networks)


class AsyncRoutesWithRawResponse:
    def __init__(self, routes: AsyncRoutes) -> None:
        self._routes = routes

        self.tunnel_route_list_tunnel_routes = async_to_raw_response_wrapper(
            routes.tunnel_route_list_tunnel_routes,
        )

    @cached_property
    def ips(self) -> AsyncIPsWithRawResponse:
        return AsyncIPsWithRawResponse(self._routes.ips)

    @cached_property
    def networks(self) -> AsyncNetworksWithRawResponse:
        return AsyncNetworksWithRawResponse(self._routes.networks)


class RoutesWithStreamingResponse:
    def __init__(self, routes: Routes) -> None:
        self._routes = routes

        self.tunnel_route_list_tunnel_routes = to_streamed_response_wrapper(
            routes.tunnel_route_list_tunnel_routes,
        )

    @cached_property
    def ips(self) -> IPsWithStreamingResponse:
        return IPsWithStreamingResponse(self._routes.ips)

    @cached_property
    def networks(self) -> NetworksWithStreamingResponse:
        return NetworksWithStreamingResponse(self._routes.networks)


class AsyncRoutesWithStreamingResponse:
    def __init__(self, routes: AsyncRoutes) -> None:
        self._routes = routes

        self.tunnel_route_list_tunnel_routes = async_to_streamed_response_wrapper(
            routes.tunnel_route_list_tunnel_routes,
        )

    @cached_property
    def ips(self) -> AsyncIPsWithStreamingResponse:
        return AsyncIPsWithStreamingResponse(self._routes.ips)

    @cached_property
    def networks(self) -> AsyncNetworksWithStreamingResponse:
        return AsyncNetworksWithStreamingResponse(self._routes.networks)
