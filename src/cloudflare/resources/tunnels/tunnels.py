# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Union, Optional, cast
from datetime import datetime

import httpx

from ...types import (
    TunnelGetResponse,
    TunnelDeleteResponse,
    TunnelArgoTunnelListArgoTunnelsResponse,
    TunnelArgoTunnelCreateAnArgoTunnelResponse,
    tunnel_delete_params,
    tunnel_argo_tunnel_list_argo_tunnels_params,
    tunnel_argo_tunnel_create_an_argo_tunnel_params,
)
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
from .connections import (
    Connections,
    AsyncConnections,
    ConnectionsWithRawResponse,
    AsyncConnectionsWithRawResponse,
    ConnectionsWithStreamingResponse,
    AsyncConnectionsWithStreamingResponse,
)
from ..._base_client import (
    make_request_options,
)

__all__ = ["Tunnels", "AsyncTunnels"]


class Tunnels(SyncAPIResource):
    @cached_property
    def connections(self) -> Connections:
        return Connections(self._client)

    @cached_property
    def with_raw_response(self) -> TunnelsWithRawResponse:
        return TunnelsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TunnelsWithStreamingResponse:
        return TunnelsWithStreamingResponse(self)

    def delete(
        self,
        tunnel_id: str,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TunnelDeleteResponse:
        """
        Deletes an Argo Tunnel from an account.

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
        return self._delete(
            f"/accounts/{account_id}/tunnels/{tunnel_id}",
            body=maybe_transform(body, tunnel_delete_params.TunnelDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TunnelDeleteResponse], ResultWrapper[TunnelDeleteResponse]),
        )

    def argo_tunnel_create_an_argo_tunnel(
        self,
        account_id: str,
        *,
        name: str,
        tunnel_secret: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TunnelArgoTunnelCreateAnArgoTunnelResponse:
        """
        Creates a new Argo Tunnel in an account.

        Args:
          account_id: Cloudflare account ID

          name: A user-friendly name for the tunnel.

          tunnel_secret: Sets the password required to run the tunnel. Must be at least 32 bytes and
              encoded as a base64 string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/tunnels",
            body=maybe_transform(
                {
                    "name": name,
                    "tunnel_secret": tunnel_secret,
                },
                tunnel_argo_tunnel_create_an_argo_tunnel_params.TunnelArgoTunnelCreateAnArgoTunnelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[TunnelArgoTunnelCreateAnArgoTunnelResponse],
                ResultWrapper[TunnelArgoTunnelCreateAnArgoTunnelResponse],
            ),
        )

    def argo_tunnel_list_argo_tunnels(
        self,
        account_id: str,
        *,
        exclude_prefix: str | NotGiven = NOT_GIVEN,
        existed_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        include_prefix: str | NotGiven = NOT_GIVEN,
        is_deleted: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        tun_types: str | NotGiven = NOT_GIVEN,
        was_active_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        was_inactive_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TunnelArgoTunnelListArgoTunnelsResponse]:
        """
        Lists and filters all types of Tunnels in an account.

        Args:
          account_id: Cloudflare account ID

          existed_at: If provided, include only tunnels that were created (and not deleted) before
              this time.

          is_deleted: If `true`, only include deleted tunnels. If `false`, exclude deleted tunnels. If
              empty, all tunnels will be included.

          name: A user-friendly name for the tunnel.

          page: Page number of paginated results.

          per_page: Number of results to display.

          tun_types: The types of tunnels to filter separated by a comma.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/tunnels",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "exclude_prefix": exclude_prefix,
                        "existed_at": existed_at,
                        "include_prefix": include_prefix,
                        "is_deleted": is_deleted,
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                        "tun_types": tun_types,
                        "was_active_at": was_active_at,
                        "was_inactive_at": was_inactive_at,
                    },
                    tunnel_argo_tunnel_list_argo_tunnels_params.TunnelArgoTunnelListArgoTunnelsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[TunnelArgoTunnelListArgoTunnelsResponse]],
                ResultWrapper[TunnelArgoTunnelListArgoTunnelsResponse],
            ),
        )

    def get(
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
    ) -> TunnelGetResponse:
        """
        Fetches a single Argo Tunnel.

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
            f"/accounts/{account_id}/tunnels/{tunnel_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TunnelGetResponse], ResultWrapper[TunnelGetResponse]),
        )


class AsyncTunnels(AsyncAPIResource):
    @cached_property
    def connections(self) -> AsyncConnections:
        return AsyncConnections(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTunnelsWithRawResponse:
        return AsyncTunnelsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTunnelsWithStreamingResponse:
        return AsyncTunnelsWithStreamingResponse(self)

    async def delete(
        self,
        tunnel_id: str,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TunnelDeleteResponse:
        """
        Deletes an Argo Tunnel from an account.

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
        return await self._delete(
            f"/accounts/{account_id}/tunnels/{tunnel_id}",
            body=maybe_transform(body, tunnel_delete_params.TunnelDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TunnelDeleteResponse], ResultWrapper[TunnelDeleteResponse]),
        )

    async def argo_tunnel_create_an_argo_tunnel(
        self,
        account_id: str,
        *,
        name: str,
        tunnel_secret: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TunnelArgoTunnelCreateAnArgoTunnelResponse:
        """
        Creates a new Argo Tunnel in an account.

        Args:
          account_id: Cloudflare account ID

          name: A user-friendly name for the tunnel.

          tunnel_secret: Sets the password required to run the tunnel. Must be at least 32 bytes and
              encoded as a base64 string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/tunnels",
            body=maybe_transform(
                {
                    "name": name,
                    "tunnel_secret": tunnel_secret,
                },
                tunnel_argo_tunnel_create_an_argo_tunnel_params.TunnelArgoTunnelCreateAnArgoTunnelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[TunnelArgoTunnelCreateAnArgoTunnelResponse],
                ResultWrapper[TunnelArgoTunnelCreateAnArgoTunnelResponse],
            ),
        )

    async def argo_tunnel_list_argo_tunnels(
        self,
        account_id: str,
        *,
        exclude_prefix: str | NotGiven = NOT_GIVEN,
        existed_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        include_prefix: str | NotGiven = NOT_GIVEN,
        is_deleted: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        tun_types: str | NotGiven = NOT_GIVEN,
        was_active_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        was_inactive_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TunnelArgoTunnelListArgoTunnelsResponse]:
        """
        Lists and filters all types of Tunnels in an account.

        Args:
          account_id: Cloudflare account ID

          existed_at: If provided, include only tunnels that were created (and not deleted) before
              this time.

          is_deleted: If `true`, only include deleted tunnels. If `false`, exclude deleted tunnels. If
              empty, all tunnels will be included.

          name: A user-friendly name for the tunnel.

          page: Page number of paginated results.

          per_page: Number of results to display.

          tun_types: The types of tunnels to filter separated by a comma.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/tunnels",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "exclude_prefix": exclude_prefix,
                        "existed_at": existed_at,
                        "include_prefix": include_prefix,
                        "is_deleted": is_deleted,
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                        "tun_types": tun_types,
                        "was_active_at": was_active_at,
                        "was_inactive_at": was_inactive_at,
                    },
                    tunnel_argo_tunnel_list_argo_tunnels_params.TunnelArgoTunnelListArgoTunnelsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[TunnelArgoTunnelListArgoTunnelsResponse]],
                ResultWrapper[TunnelArgoTunnelListArgoTunnelsResponse],
            ),
        )

    async def get(
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
    ) -> TunnelGetResponse:
        """
        Fetches a single Argo Tunnel.

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
            f"/accounts/{account_id}/tunnels/{tunnel_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TunnelGetResponse], ResultWrapper[TunnelGetResponse]),
        )


class TunnelsWithRawResponse:
    def __init__(self, tunnels: Tunnels) -> None:
        self._tunnels = tunnels

        self.delete = to_raw_response_wrapper(
            tunnels.delete,
        )
        self.argo_tunnel_create_an_argo_tunnel = to_raw_response_wrapper(
            tunnels.argo_tunnel_create_an_argo_tunnel,
        )
        self.argo_tunnel_list_argo_tunnels = to_raw_response_wrapper(
            tunnels.argo_tunnel_list_argo_tunnels,
        )
        self.get = to_raw_response_wrapper(
            tunnels.get,
        )

    @cached_property
    def connections(self) -> ConnectionsWithRawResponse:
        return ConnectionsWithRawResponse(self._tunnels.connections)


class AsyncTunnelsWithRawResponse:
    def __init__(self, tunnels: AsyncTunnels) -> None:
        self._tunnels = tunnels

        self.delete = async_to_raw_response_wrapper(
            tunnels.delete,
        )
        self.argo_tunnel_create_an_argo_tunnel = async_to_raw_response_wrapper(
            tunnels.argo_tunnel_create_an_argo_tunnel,
        )
        self.argo_tunnel_list_argo_tunnels = async_to_raw_response_wrapper(
            tunnels.argo_tunnel_list_argo_tunnels,
        )
        self.get = async_to_raw_response_wrapper(
            tunnels.get,
        )

    @cached_property
    def connections(self) -> AsyncConnectionsWithRawResponse:
        return AsyncConnectionsWithRawResponse(self._tunnels.connections)


class TunnelsWithStreamingResponse:
    def __init__(self, tunnels: Tunnels) -> None:
        self._tunnels = tunnels

        self.delete = to_streamed_response_wrapper(
            tunnels.delete,
        )
        self.argo_tunnel_create_an_argo_tunnel = to_streamed_response_wrapper(
            tunnels.argo_tunnel_create_an_argo_tunnel,
        )
        self.argo_tunnel_list_argo_tunnels = to_streamed_response_wrapper(
            tunnels.argo_tunnel_list_argo_tunnels,
        )
        self.get = to_streamed_response_wrapper(
            tunnels.get,
        )

    @cached_property
    def connections(self) -> ConnectionsWithStreamingResponse:
        return ConnectionsWithStreamingResponse(self._tunnels.connections)


class AsyncTunnelsWithStreamingResponse:
    def __init__(self, tunnels: AsyncTunnels) -> None:
        self._tunnels = tunnels

        self.delete = async_to_streamed_response_wrapper(
            tunnels.delete,
        )
        self.argo_tunnel_create_an_argo_tunnel = async_to_streamed_response_wrapper(
            tunnels.argo_tunnel_create_an_argo_tunnel,
        )
        self.argo_tunnel_list_argo_tunnels = async_to_streamed_response_wrapper(
            tunnels.argo_tunnel_list_argo_tunnels,
        )
        self.get = async_to_streamed_response_wrapper(
            tunnels.get,
        )

    @cached_property
    def connections(self) -> AsyncConnectionsWithStreamingResponse:
        return AsyncConnectionsWithStreamingResponse(self._tunnels.connections)
