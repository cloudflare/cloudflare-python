# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, Type, Optional, cast

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
from ...types.cfd_tunnels import (
    ConnectionDeleteResponse,
    ConnectionCloudflareTunnelListCloudflareTunnelConnectionsResponse,
    connection_delete_params,
)

__all__ = ["Connections", "AsyncConnections"]


class Connections(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConnectionsWithRawResponse:
        return ConnectionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectionsWithStreamingResponse:
        return ConnectionsWithStreamingResponse(self)

    def delete(
        self,
        tunnel_id: str,
        *,
        account_id: str,
        body: object,
        client_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectionDeleteResponse:
        """
        Removes a connection (aka Cloudflare Tunnel Connector) from a Cloudflare Tunnel
        independently of its current state. If no connector id (client_id) is provided
        all connectors will be removed. We recommend running this command after rotating
        tokens.

        Args:
          account_id: Cloudflare account ID

          tunnel_id: UUID of the tunnel.

          client_id: UUID of the Cloudflare Tunnel Connector to disconnect.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_id:
            raise ValueError(f"Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}")
        return cast(
            ConnectionDeleteResponse,
            self._delete(
                f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}/connections",
                body=maybe_transform(body, connection_delete_params.ConnectionDeleteParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform({"client_id": client_id}, connection_delete_params.ConnectionDeleteParams),
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ConnectionDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def cloudflare_tunnel_list_cloudflare_tunnel_connections(
        self,
        tunnel_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConnectionCloudflareTunnelListCloudflareTunnelConnectionsResponse]:
        """
        Fetches connection details for a Cloudflare Tunnel.

        Args:
          account_id: Cloudflare account ID

          tunnel_id: UUID of the tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_id:
            raise ValueError(f"Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}")
        return self._get(
            f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}/connections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ConnectionCloudflareTunnelListCloudflareTunnelConnectionsResponse]],
                ResultWrapper[ConnectionCloudflareTunnelListCloudflareTunnelConnectionsResponse],
            ),
        )


class AsyncConnections(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConnectionsWithRawResponse:
        return AsyncConnectionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectionsWithStreamingResponse:
        return AsyncConnectionsWithStreamingResponse(self)

    async def delete(
        self,
        tunnel_id: str,
        *,
        account_id: str,
        body: object,
        client_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectionDeleteResponse:
        """
        Removes a connection (aka Cloudflare Tunnel Connector) from a Cloudflare Tunnel
        independently of its current state. If no connector id (client_id) is provided
        all connectors will be removed. We recommend running this command after rotating
        tokens.

        Args:
          account_id: Cloudflare account ID

          tunnel_id: UUID of the tunnel.

          client_id: UUID of the Cloudflare Tunnel Connector to disconnect.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_id:
            raise ValueError(f"Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}")
        return cast(
            ConnectionDeleteResponse,
            await self._delete(
                f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}/connections",
                body=maybe_transform(body, connection_delete_params.ConnectionDeleteParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform({"client_id": client_id}, connection_delete_params.ConnectionDeleteParams),
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ConnectionDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def cloudflare_tunnel_list_cloudflare_tunnel_connections(
        self,
        tunnel_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConnectionCloudflareTunnelListCloudflareTunnelConnectionsResponse]:
        """
        Fetches connection details for a Cloudflare Tunnel.

        Args:
          account_id: Cloudflare account ID

          tunnel_id: UUID of the tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_id:
            raise ValueError(f"Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}")
        return await self._get(
            f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}/connections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ConnectionCloudflareTunnelListCloudflareTunnelConnectionsResponse]],
                ResultWrapper[ConnectionCloudflareTunnelListCloudflareTunnelConnectionsResponse],
            ),
        )


class ConnectionsWithRawResponse:
    def __init__(self, connections: Connections) -> None:
        self._connections = connections

        self.delete = to_raw_response_wrapper(
            connections.delete,
        )
        self.cloudflare_tunnel_list_cloudflare_tunnel_connections = to_raw_response_wrapper(
            connections.cloudflare_tunnel_list_cloudflare_tunnel_connections,
        )


class AsyncConnectionsWithRawResponse:
    def __init__(self, connections: AsyncConnections) -> None:
        self._connections = connections

        self.delete = async_to_raw_response_wrapper(
            connections.delete,
        )
        self.cloudflare_tunnel_list_cloudflare_tunnel_connections = async_to_raw_response_wrapper(
            connections.cloudflare_tunnel_list_cloudflare_tunnel_connections,
        )


class ConnectionsWithStreamingResponse:
    def __init__(self, connections: Connections) -> None:
        self._connections = connections

        self.delete = to_streamed_response_wrapper(
            connections.delete,
        )
        self.cloudflare_tunnel_list_cloudflare_tunnel_connections = to_streamed_response_wrapper(
            connections.cloudflare_tunnel_list_cloudflare_tunnel_connections,
        )


class AsyncConnectionsWithStreamingResponse:
    def __init__(self, connections: AsyncConnections) -> None:
        self._connections = connections

        self.delete = async_to_streamed_response_wrapper(
            connections.delete,
        )
        self.cloudflare_tunnel_list_cloudflare_tunnel_connections = async_to_streamed_response_wrapper(
            connections.cloudflare_tunnel_list_cloudflare_tunnel_connections,
        )
