# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .ips import IPsResource, AsyncIPsResource

from ....._compat import cached_property

from .networks import NetworksResource, AsyncNetworksResource

from .....types.zero_trust.networks.route import Route

from ....._wrappers import ResultWrapper

from ....._utils import maybe_transform, async_maybe_transform

from ....._base_client import make_request_options, AsyncPaginator

from typing import Type, Union

from .....types.zero_trust.networks.teamnet import Teamnet

from .....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray

from datetime import datetime

from ....._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .....types.zero_trust.networks import route_create_params
from .....types.zero_trust.networks import route_list_params
from .....types.zero_trust.networks import route_edit_params
from .ips import IPsResource, AsyncIPsResource, IPsResourceWithRawResponse, AsyncIPsResourceWithRawResponse, IPsResourceWithStreamingResponse, AsyncIPsResourceWithStreamingResponse
from .networks import NetworksResource, AsyncNetworksResource, NetworksResourceWithRawResponse, AsyncNetworksResourceWithRawResponse, NetworksResourceWithStreamingResponse, AsyncNetworksResourceWithStreamingResponse
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["RoutesResource", "AsyncRoutesResource"]

class RoutesResource(SyncAPIResource):
    @cached_property
    def ips(self) -> IPsResource:
        return IPsResource(self._client)

    @cached_property
    def networks(self) -> NetworksResource:
        return NetworksResource(self._client)

    @cached_property
    def with_raw_response(self) -> RoutesResourceWithRawResponse:
        return RoutesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoutesResourceWithStreamingResponse:
        return RoutesResourceWithStreamingResponse(self)

    def create(self,
    *,
    account_id: str,
    network: str,
    tunnel_id: str,
    comment: str | NotGiven = NOT_GIVEN,
    virtual_network_id: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Route:
        """
        Routes a private network through a Cloudflare Tunnel.

        Args:
          account_id: Cloudflare account ID

          network: The private IPv4 or IPv6 range connected by the route, in CIDR notation.

          tunnel_id: UUID of the tunnel.

          comment: Optional remark describing the route.

          virtual_network_id: UUID of the virtual network.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._post(
            f"/accounts/{account_id}/teamnet/routes",
            body=maybe_transform({
                "network": network,
                "tunnel_id": tunnel_id,
                "comment": comment,
                "virtual_network_id": virtual_network_id,
            }, route_create_params.RouteCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Route]._unwrapper),
            cast_to=cast(Type[Route], ResultWrapper[Route]),
        )

    def list(self,
    *,
    account_id: str,
    comment: str | NotGiven = NOT_GIVEN,
    existed_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
    is_deleted: bool | NotGiven = NOT_GIVEN,
    network_subset: str | NotGiven = NOT_GIVEN,
    network_superset: str | NotGiven = NOT_GIVEN,
    page: float | NotGiven = NOT_GIVEN,
    per_page: float | NotGiven = NOT_GIVEN,
    route_id: str | NotGiven = NOT_GIVEN,
    tun_types: str | NotGiven = NOT_GIVEN,
    tunnel_id: str | NotGiven = NOT_GIVEN,
    virtual_network_id: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> SyncV4PagePaginationArray[Teamnet]:
        """
        Lists and filters private network routes in an account.

        Args:
          account_id: Cloudflare account ID

          comment: Optional remark describing the route.

          existed_at: If provided, include only tunnels that were created (and not deleted) before
              this time.

          is_deleted: If `true`, only include deleted routes. If `false`, exclude deleted routes. If
              empty, all routes will be included.

          network_subset: If set, only list routes that are contained within this IP range.

          network_superset: If set, only list routes that contain this IP range.

          page: Page number of paginated results.

          per_page: Number of results to display.

          route_id: UUID of the route.

          tun_types: The types of tunnels to filter separated by a comma.

          tunnel_id: UUID of the tunnel.

          virtual_network_id: UUID of the virtual network.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get_api_list(
            f"/accounts/{account_id}/teamnet/routes",
            page = SyncV4PagePaginationArray[Teamnet],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "comment": comment,
                "existed_at": existed_at,
                "is_deleted": is_deleted,
                "network_subset": network_subset,
                "network_superset": network_superset,
                "page": page,
                "per_page": per_page,
                "route_id": route_id,
                "tun_types": tun_types,
                "tunnel_id": tunnel_id,
                "virtual_network_id": virtual_network_id,
            }, route_list_params.RouteListParams)),
            model=Teamnet,
        )

    def delete(self,
    route_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Route:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not route_id:
          raise ValueError(
            f'Expected a non-empty value for `route_id` but received {route_id!r}'
          )
        return self._delete(
            f"/accounts/{account_id}/teamnet/routes/{route_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Route]._unwrapper),
            cast_to=cast(Type[Route], ResultWrapper[Route]),
        )

    def edit(self,
    route_id: str,
    *,
    account_id: str,
    comment: str | NotGiven = NOT_GIVEN,
    network: str | NotGiven = NOT_GIVEN,
    tunnel_id: str | NotGiven = NOT_GIVEN,
    virtual_network_id: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Route:
        """Updates an existing private network route in an account.

        The fields that are
        meant to be updated should be provided in the body of the request.

        Args:
          account_id: Cloudflare account ID

          route_id: UUID of the route.

          comment: Optional remark describing the route.

          network: The private IPv4 or IPv6 range connected by the route, in CIDR notation.

          tunnel_id: UUID of the tunnel.

          virtual_network_id: UUID of the virtual network.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not route_id:
          raise ValueError(
            f'Expected a non-empty value for `route_id` but received {route_id!r}'
          )
        return self._patch(
            f"/accounts/{account_id}/teamnet/routes/{route_id}",
            body=maybe_transform({
                "comment": comment,
                "network": network,
                "tunnel_id": tunnel_id,
                "virtual_network_id": virtual_network_id,
            }, route_edit_params.RouteEditParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Route]._unwrapper),
            cast_to=cast(Type[Route], ResultWrapper[Route]),
        )

class AsyncRoutesResource(AsyncAPIResource):
    @cached_property
    def ips(self) -> AsyncIPsResource:
        return AsyncIPsResource(self._client)

    @cached_property
    def networks(self) -> AsyncNetworksResource:
        return AsyncNetworksResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRoutesResourceWithRawResponse:
        return AsyncRoutesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoutesResourceWithStreamingResponse:
        return AsyncRoutesResourceWithStreamingResponse(self)

    async def create(self,
    *,
    account_id: str,
    network: str,
    tunnel_id: str,
    comment: str | NotGiven = NOT_GIVEN,
    virtual_network_id: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Route:
        """
        Routes a private network through a Cloudflare Tunnel.

        Args:
          account_id: Cloudflare account ID

          network: The private IPv4 or IPv6 range connected by the route, in CIDR notation.

          tunnel_id: UUID of the tunnel.

          comment: Optional remark describing the route.

          virtual_network_id: UUID of the virtual network.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return await self._post(
            f"/accounts/{account_id}/teamnet/routes",
            body=await async_maybe_transform({
                "network": network,
                "tunnel_id": tunnel_id,
                "comment": comment,
                "virtual_network_id": virtual_network_id,
            }, route_create_params.RouteCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Route]._unwrapper),
            cast_to=cast(Type[Route], ResultWrapper[Route]),
        )

    def list(self,
    *,
    account_id: str,
    comment: str | NotGiven = NOT_GIVEN,
    existed_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
    is_deleted: bool | NotGiven = NOT_GIVEN,
    network_subset: str | NotGiven = NOT_GIVEN,
    network_superset: str | NotGiven = NOT_GIVEN,
    page: float | NotGiven = NOT_GIVEN,
    per_page: float | NotGiven = NOT_GIVEN,
    route_id: str | NotGiven = NOT_GIVEN,
    tun_types: str | NotGiven = NOT_GIVEN,
    tunnel_id: str | NotGiven = NOT_GIVEN,
    virtual_network_id: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AsyncPaginator[Teamnet, AsyncV4PagePaginationArray[Teamnet]]:
        """
        Lists and filters private network routes in an account.

        Args:
          account_id: Cloudflare account ID

          comment: Optional remark describing the route.

          existed_at: If provided, include only tunnels that were created (and not deleted) before
              this time.

          is_deleted: If `true`, only include deleted routes. If `false`, exclude deleted routes. If
              empty, all routes will be included.

          network_subset: If set, only list routes that are contained within this IP range.

          network_superset: If set, only list routes that contain this IP range.

          page: Page number of paginated results.

          per_page: Number of results to display.

          route_id: UUID of the route.

          tun_types: The types of tunnels to filter separated by a comma.

          tunnel_id: UUID of the tunnel.

          virtual_network_id: UUID of the virtual network.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get_api_list(
            f"/accounts/{account_id}/teamnet/routes",
            page = AsyncV4PagePaginationArray[Teamnet],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "comment": comment,
                "existed_at": existed_at,
                "is_deleted": is_deleted,
                "network_subset": network_subset,
                "network_superset": network_superset,
                "page": page,
                "per_page": per_page,
                "route_id": route_id,
                "tun_types": tun_types,
                "tunnel_id": tunnel_id,
                "virtual_network_id": virtual_network_id,
            }, route_list_params.RouteListParams)),
            model=Teamnet,
        )

    async def delete(self,
    route_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Route:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not route_id:
          raise ValueError(
            f'Expected a non-empty value for `route_id` but received {route_id!r}'
          )
        return await self._delete(
            f"/accounts/{account_id}/teamnet/routes/{route_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Route]._unwrapper),
            cast_to=cast(Type[Route], ResultWrapper[Route]),
        )

    async def edit(self,
    route_id: str,
    *,
    account_id: str,
    comment: str | NotGiven = NOT_GIVEN,
    network: str | NotGiven = NOT_GIVEN,
    tunnel_id: str | NotGiven = NOT_GIVEN,
    virtual_network_id: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Route:
        """Updates an existing private network route in an account.

        The fields that are
        meant to be updated should be provided in the body of the request.

        Args:
          account_id: Cloudflare account ID

          route_id: UUID of the route.

          comment: Optional remark describing the route.

          network: The private IPv4 or IPv6 range connected by the route, in CIDR notation.

          tunnel_id: UUID of the tunnel.

          virtual_network_id: UUID of the virtual network.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not route_id:
          raise ValueError(
            f'Expected a non-empty value for `route_id` but received {route_id!r}'
          )
        return await self._patch(
            f"/accounts/{account_id}/teamnet/routes/{route_id}",
            body=await async_maybe_transform({
                "comment": comment,
                "network": network,
                "tunnel_id": tunnel_id,
                "virtual_network_id": virtual_network_id,
            }, route_edit_params.RouteEditParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Route]._unwrapper),
            cast_to=cast(Type[Route], ResultWrapper[Route]),
        )

class RoutesResourceWithRawResponse:
    def __init__(self, routes: RoutesResource) -> None:
        self._routes = routes

        self.create = to_raw_response_wrapper(
            routes.create,
        )
        self.list = to_raw_response_wrapper(
            routes.list,
        )
        self.delete = to_raw_response_wrapper(
            routes.delete,
        )
        self.edit = to_raw_response_wrapper(
            routes.edit,
        )

    @cached_property
    def ips(self) -> IPsResourceWithRawResponse:
        return IPsResourceWithRawResponse(self._routes.ips)

    @cached_property
    def networks(self) -> NetworksResourceWithRawResponse:
        return NetworksResourceWithRawResponse(self._routes.networks)

class AsyncRoutesResourceWithRawResponse:
    def __init__(self, routes: AsyncRoutesResource) -> None:
        self._routes = routes

        self.create = async_to_raw_response_wrapper(
            routes.create,
        )
        self.list = async_to_raw_response_wrapper(
            routes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            routes.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            routes.edit,
        )

    @cached_property
    def ips(self) -> AsyncIPsResourceWithRawResponse:
        return AsyncIPsResourceWithRawResponse(self._routes.ips)

    @cached_property
    def networks(self) -> AsyncNetworksResourceWithRawResponse:
        return AsyncNetworksResourceWithRawResponse(self._routes.networks)

class RoutesResourceWithStreamingResponse:
    def __init__(self, routes: RoutesResource) -> None:
        self._routes = routes

        self.create = to_streamed_response_wrapper(
            routes.create,
        )
        self.list = to_streamed_response_wrapper(
            routes.list,
        )
        self.delete = to_streamed_response_wrapper(
            routes.delete,
        )
        self.edit = to_streamed_response_wrapper(
            routes.edit,
        )

    @cached_property
    def ips(self) -> IPsResourceWithStreamingResponse:
        return IPsResourceWithStreamingResponse(self._routes.ips)

    @cached_property
    def networks(self) -> NetworksResourceWithStreamingResponse:
        return NetworksResourceWithStreamingResponse(self._routes.networks)

class AsyncRoutesResourceWithStreamingResponse:
    def __init__(self, routes: AsyncRoutesResource) -> None:
        self._routes = routes

        self.create = async_to_streamed_response_wrapper(
            routes.create,
        )
        self.list = async_to_streamed_response_wrapper(
            routes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            routes.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            routes.edit,
        )

    @cached_property
    def ips(self) -> AsyncIPsResourceWithStreamingResponse:
        return AsyncIPsResourceWithStreamingResponse(self._routes.ips)

    @cached_property
    def networks(self) -> AsyncNetworksResourceWithStreamingResponse:
        return AsyncNetworksResourceWithStreamingResponse(self._routes.networks)