# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import (
    make_request_options,
)
from .....types.zero_trust.networks import TunnelRoute
from .....types.zero_trust.networks.routes import network_create_params, network_delete_params

__all__ = ["Networks", "AsyncNetworks"]


class Networks(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NetworksWithRawResponse:
        return NetworksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NetworksWithStreamingResponse:
        return NetworksWithStreamingResponse(self)

    def create(
        self,
        ip_network_encoded: str,
        *,
        account_id: str,
        comment: str | NotGiven = NOT_GIVEN,
        virtual_network_id: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TunnelRoute:
        """Routes a private network through a Cloudflare Tunnel.

        The CIDR in
        `ip_network_encoded` must be written in URL-encoded format.

        Args:
          account_id: Cloudflare account ID

          ip_network_encoded: IP/CIDR range in URL-encoded format

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
        if not ip_network_encoded:
            raise ValueError(f"Expected a non-empty value for `ip_network_encoded` but received {ip_network_encoded!r}")
        return self._post(
            f"/accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}",
            body=maybe_transform(
                {
                    "comment": comment,
                    "virtual_network_id": virtual_network_id,
                },
                network_create_params.NetworkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TunnelRoute], ResultWrapper[TunnelRoute]),
        )

    def delete(
        self,
        ip_network_encoded: str,
        *,
        account_id: str,
        tun_type: Literal["cfd_tunnel", "warp_connector", "ip_sec", "gre", "cni"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TunnelRoute:
        """Deletes a private network route from an account.

        The CIDR in
        `ip_network_encoded` must be written in URL-encoded format. If no
        virtual_network_id is provided it will delete the route from the default vnet.
        If no tun_type is provided it will fetch the type from the tunnel_id or if that
        is missing it will assume Cloudflare Tunnel as default. If tunnel_id is provided
        it will delete the route from that tunnel, otherwise it will delete the route
        based on the vnet and tun_type.

        Args:
          account_id: Cloudflare account ID

          ip_network_encoded: IP/CIDR range in URL-encoded format

          tun_type: The type of tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not ip_network_encoded:
            raise ValueError(f"Expected a non-empty value for `ip_network_encoded` but received {ip_network_encoded!r}")
        return self._delete(
            f"/accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"tun_type": tun_type}, network_delete_params.NetworkDeleteParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TunnelRoute], ResultWrapper[TunnelRoute]),
        )

    def edit(
        self,
        ip_network_encoded: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TunnelRoute:
        """Updates an existing private network route in an account.

        The CIDR in
        `ip_network_encoded` must be written in URL-encoded format.

        Args:
          account_id: Cloudflare account ID

          ip_network_encoded: IP/CIDR range in URL-encoded format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not ip_network_encoded:
            raise ValueError(f"Expected a non-empty value for `ip_network_encoded` but received {ip_network_encoded!r}")
        return self._patch(
            f"/accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TunnelRoute], ResultWrapper[TunnelRoute]),
        )


class AsyncNetworks(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNetworksWithRawResponse:
        return AsyncNetworksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNetworksWithStreamingResponse:
        return AsyncNetworksWithStreamingResponse(self)

    async def create(
        self,
        ip_network_encoded: str,
        *,
        account_id: str,
        comment: str | NotGiven = NOT_GIVEN,
        virtual_network_id: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TunnelRoute:
        """Routes a private network through a Cloudflare Tunnel.

        The CIDR in
        `ip_network_encoded` must be written in URL-encoded format.

        Args:
          account_id: Cloudflare account ID

          ip_network_encoded: IP/CIDR range in URL-encoded format

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
        if not ip_network_encoded:
            raise ValueError(f"Expected a non-empty value for `ip_network_encoded` but received {ip_network_encoded!r}")
        return await self._post(
            f"/accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}",
            body=await async_maybe_transform(
                {
                    "comment": comment,
                    "virtual_network_id": virtual_network_id,
                },
                network_create_params.NetworkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TunnelRoute], ResultWrapper[TunnelRoute]),
        )

    async def delete(
        self,
        ip_network_encoded: str,
        *,
        account_id: str,
        tun_type: Literal["cfd_tunnel", "warp_connector", "ip_sec", "gre", "cni"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TunnelRoute:
        """Deletes a private network route from an account.

        The CIDR in
        `ip_network_encoded` must be written in URL-encoded format. If no
        virtual_network_id is provided it will delete the route from the default vnet.
        If no tun_type is provided it will fetch the type from the tunnel_id or if that
        is missing it will assume Cloudflare Tunnel as default. If tunnel_id is provided
        it will delete the route from that tunnel, otherwise it will delete the route
        based on the vnet and tun_type.

        Args:
          account_id: Cloudflare account ID

          ip_network_encoded: IP/CIDR range in URL-encoded format

          tun_type: The type of tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not ip_network_encoded:
            raise ValueError(f"Expected a non-empty value for `ip_network_encoded` but received {ip_network_encoded!r}")
        return await self._delete(
            f"/accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"tun_type": tun_type}, network_delete_params.NetworkDeleteParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TunnelRoute], ResultWrapper[TunnelRoute]),
        )

    async def edit(
        self,
        ip_network_encoded: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TunnelRoute:
        """Updates an existing private network route in an account.

        The CIDR in
        `ip_network_encoded` must be written in URL-encoded format.

        Args:
          account_id: Cloudflare account ID

          ip_network_encoded: IP/CIDR range in URL-encoded format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not ip_network_encoded:
            raise ValueError(f"Expected a non-empty value for `ip_network_encoded` but received {ip_network_encoded!r}")
        return await self._patch(
            f"/accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TunnelRoute], ResultWrapper[TunnelRoute]),
        )


class NetworksWithRawResponse:
    def __init__(self, networks: Networks) -> None:
        self._networks = networks

        self.create = to_raw_response_wrapper(
            networks.create,
        )
        self.delete = to_raw_response_wrapper(
            networks.delete,
        )
        self.edit = to_raw_response_wrapper(
            networks.edit,
        )


class AsyncNetworksWithRawResponse:
    def __init__(self, networks: AsyncNetworks) -> None:
        self._networks = networks

        self.create = async_to_raw_response_wrapper(
            networks.create,
        )
        self.delete = async_to_raw_response_wrapper(
            networks.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            networks.edit,
        )


class NetworksWithStreamingResponse:
    def __init__(self, networks: Networks) -> None:
        self._networks = networks

        self.create = to_streamed_response_wrapper(
            networks.create,
        )
        self.delete = to_streamed_response_wrapper(
            networks.delete,
        )
        self.edit = to_streamed_response_wrapper(
            networks.edit,
        )


class AsyncNetworksWithStreamingResponse:
    def __init__(self, networks: AsyncNetworks) -> None:
        self._networks = networks

        self.create = async_to_streamed_response_wrapper(
            networks.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            networks.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            networks.edit,
        )
