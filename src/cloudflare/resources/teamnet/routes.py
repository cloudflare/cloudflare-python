# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.teamnet import (
    RouteEditResponse,
    RouteCreateResponse,
    RouteDeleteResponse,
    route_edit_params,
    route_create_params,
)

__all__ = ["Routes", "AsyncRoutes"]


class Routes(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RoutesWithRawResponse:
        return RoutesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoutesWithStreamingResponse:
        return RoutesWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        ip_network: str,
        comment: str | NotGiven = NOT_GIVEN,
        virtual_network_id: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteCreateResponse:
        """
        Routes a private network through a Cloudflare Tunnel.

        Args:
          account_id: Cloudflare account ID

          ip_network: The private IPv4 or IPv6 range connected by the route, in CIDR notation.

          comment: Optional remark describing the route.

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
        return self._post(
            f"/accounts/{account_id}/teamnet/routes",
            body=maybe_transform(
                {
                    "ip_network": ip_network,
                    "comment": comment,
                    "virtual_network_id": virtual_network_id,
                },
                route_create_params.RouteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RouteCreateResponse], ResultWrapper[RouteCreateResponse]),
        )

    def delete(
        self,
        route_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteDeleteResponse:
        """
        Deletes a private network route from an account.

        Args:
          account_id: Cloudflare account ID

          route_id: UUID of the route.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not route_id:
            raise ValueError(f"Expected a non-empty value for `route_id` but received {route_id!r}")
        return self._delete(
            f"/accounts/{account_id}/teamnet/routes/{route_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RouteDeleteResponse], ResultWrapper[RouteDeleteResponse]),
        )

    def edit(
        self,
        route_id: str,
        *,
        account_id: str,
        comment: str | NotGiven = NOT_GIVEN,
        network: str | NotGiven = NOT_GIVEN,
        tun_type: Literal["cfd_tunnel", "warp_connector", "ip_sec", "gre", "cni"] | NotGiven = NOT_GIVEN,
        tunnel_id: object | NotGiven = NOT_GIVEN,
        virtual_network_id: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteEditResponse:
        """Updates an existing private network route in an account.

        The fields that are
        meant to be updated should be provided in the body of the request.

        Args:
          account_id: Cloudflare account ID

          route_id: UUID of the route.

          comment: Optional remark describing the route.

          network: The private IPv4 or IPv6 range connected by the route, in CIDR notation.

          tun_type: The type of tunnel.

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
        if not route_id:
            raise ValueError(f"Expected a non-empty value for `route_id` but received {route_id!r}")
        return self._patch(
            f"/accounts/{account_id}/teamnet/routes/{route_id}",
            body=maybe_transform(
                {
                    "comment": comment,
                    "network": network,
                    "tun_type": tun_type,
                    "tunnel_id": tunnel_id,
                    "virtual_network_id": virtual_network_id,
                },
                route_edit_params.RouteEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RouteEditResponse], ResultWrapper[RouteEditResponse]),
        )


class AsyncRoutes(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRoutesWithRawResponse:
        return AsyncRoutesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoutesWithStreamingResponse:
        return AsyncRoutesWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        ip_network: str,
        comment: str | NotGiven = NOT_GIVEN,
        virtual_network_id: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteCreateResponse:
        """
        Routes a private network through a Cloudflare Tunnel.

        Args:
          account_id: Cloudflare account ID

          ip_network: The private IPv4 or IPv6 range connected by the route, in CIDR notation.

          comment: Optional remark describing the route.

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
        return await self._post(
            f"/accounts/{account_id}/teamnet/routes",
            body=maybe_transform(
                {
                    "ip_network": ip_network,
                    "comment": comment,
                    "virtual_network_id": virtual_network_id,
                },
                route_create_params.RouteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RouteCreateResponse], ResultWrapper[RouteCreateResponse]),
        )

    async def delete(
        self,
        route_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteDeleteResponse:
        """
        Deletes a private network route from an account.

        Args:
          account_id: Cloudflare account ID

          route_id: UUID of the route.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not route_id:
            raise ValueError(f"Expected a non-empty value for `route_id` but received {route_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/teamnet/routes/{route_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RouteDeleteResponse], ResultWrapper[RouteDeleteResponse]),
        )

    async def edit(
        self,
        route_id: str,
        *,
        account_id: str,
        comment: str | NotGiven = NOT_GIVEN,
        network: str | NotGiven = NOT_GIVEN,
        tun_type: Literal["cfd_tunnel", "warp_connector", "ip_sec", "gre", "cni"] | NotGiven = NOT_GIVEN,
        tunnel_id: object | NotGiven = NOT_GIVEN,
        virtual_network_id: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteEditResponse:
        """Updates an existing private network route in an account.

        The fields that are
        meant to be updated should be provided in the body of the request.

        Args:
          account_id: Cloudflare account ID

          route_id: UUID of the route.

          comment: Optional remark describing the route.

          network: The private IPv4 or IPv6 range connected by the route, in CIDR notation.

          tun_type: The type of tunnel.

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
        if not route_id:
            raise ValueError(f"Expected a non-empty value for `route_id` but received {route_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/teamnet/routes/{route_id}",
            body=maybe_transform(
                {
                    "comment": comment,
                    "network": network,
                    "tun_type": tun_type,
                    "tunnel_id": tunnel_id,
                    "virtual_network_id": virtual_network_id,
                },
                route_edit_params.RouteEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RouteEditResponse], ResultWrapper[RouteEditResponse]),
        )


class RoutesWithRawResponse:
    def __init__(self, routes: Routes) -> None:
        self._routes = routes

        self.create = to_raw_response_wrapper(
            routes.create,
        )
        self.delete = to_raw_response_wrapper(
            routes.delete,
        )
        self.edit = to_raw_response_wrapper(
            routes.edit,
        )


class AsyncRoutesWithRawResponse:
    def __init__(self, routes: AsyncRoutes) -> None:
        self._routes = routes

        self.create = async_to_raw_response_wrapper(
            routes.create,
        )
        self.delete = async_to_raw_response_wrapper(
            routes.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            routes.edit,
        )


class RoutesWithStreamingResponse:
    def __init__(self, routes: Routes) -> None:
        self._routes = routes

        self.create = to_streamed_response_wrapper(
            routes.create,
        )
        self.delete = to_streamed_response_wrapper(
            routes.delete,
        )
        self.edit = to_streamed_response_wrapper(
            routes.edit,
        )


class AsyncRoutesWithStreamingResponse:
    def __init__(self, routes: AsyncRoutes) -> None:
        self._routes = routes

        self.create = async_to_streamed_response_wrapper(
            routes.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            routes.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            routes.edit,
        )
