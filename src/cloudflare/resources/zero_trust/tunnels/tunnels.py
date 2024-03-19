# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Union, cast
from datetime import datetime

import httpx

from .token import (
    Token,
    AsyncToken,
    TokenWithRawResponse,
    AsyncTokenWithRawResponse,
    TokenWithStreamingResponse,
    AsyncTokenWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from .connectors import (
    Connectors,
    AsyncConnectors,
    ConnectorsWithRawResponse,
    AsyncConnectorsWithRawResponse,
    ConnectorsWithStreamingResponse,
    AsyncConnectorsWithStreamingResponse,
)
from .management import (
    Management,
    AsyncManagement,
    ManagementWithRawResponse,
    AsyncManagementWithRawResponse,
    ManagementWithStreamingResponse,
    AsyncManagementWithStreamingResponse,
)
from .connections import (
    Connections,
    AsyncConnections,
    ConnectionsWithRawResponse,
    AsyncConnectionsWithRawResponse,
    ConnectionsWithStreamingResponse,
    AsyncConnectionsWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from .configurations import (
    Configurations,
    AsyncConfigurations,
    ConfigurationsWithRawResponse,
    AsyncConfigurationsWithRawResponse,
    ConfigurationsWithStreamingResponse,
    AsyncConfigurationsWithStreamingResponse,
)
from ...._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ....types.zero_trust import (
    TunnelArgoTunnel,
    TunnelEditResponse,
    TunnelListResponse,
    tunnel_edit_params,
    tunnel_list_params,
    tunnel_create_params,
    tunnel_delete_params,
)

__all__ = ["Tunnels", "AsyncTunnels"]


class Tunnels(SyncAPIResource):
    @cached_property
    def configurations(self) -> Configurations:
        return Configurations(self._client)

    @cached_property
    def connections(self) -> Connections:
        return Connections(self._client)

    @cached_property
    def token(self) -> Token:
        return Token(self._client)

    @cached_property
    def connectors(self) -> Connectors:
        return Connectors(self._client)

    @cached_property
    def management(self) -> Management:
        return Management(self._client)

    @cached_property
    def with_raw_response(self) -> TunnelsWithRawResponse:
        return TunnelsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TunnelsWithStreamingResponse:
        return TunnelsWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        tunnel_secret: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TunnelArgoTunnel:
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
                tunnel_create_params.TunnelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TunnelArgoTunnel], ResultWrapper[TunnelArgoTunnel]),
        )

    def list(
        self,
        *,
        account_id: str,
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
    ) -> SyncV4PagePaginationArray[TunnelListResponse]:
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
        return self._get_api_list(
            f"/accounts/{account_id}/tunnels",
            page=SyncV4PagePaginationArray[TunnelListResponse],
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
                    tunnel_list_params.TunnelListParams,
                ),
            ),
            model=cast(Any, TunnelListResponse),  # Union types cannot be passed in as arguments in the type system
        )

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
    ) -> TunnelArgoTunnel:
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
            cast_to=cast(Type[TunnelArgoTunnel], ResultWrapper[TunnelArgoTunnel]),
        )

    def edit(
        self,
        tunnel_id: str,
        *,
        account_id: str,
        name: str | NotGiven = NOT_GIVEN,
        tunnel_secret: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TunnelEditResponse:
        """
        Updates an existing Cloudflare Tunnel.

        Args:
          account_id: Cloudflare account ID

          tunnel_id: UUID of the tunnel.

          name: A user-friendly name for the tunnel.

          tunnel_secret: Sets the password required to run a locally-managed tunnel. Must be at least 32
              bytes and encoded as a base64 string.

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
            TunnelEditResponse,
            self._patch(
                f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}",
                body=maybe_transform(
                    {
                        "name": name,
                        "tunnel_secret": tunnel_secret,
                    },
                    tunnel_edit_params.TunnelEditParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[TunnelEditResponse]
                ),  # Union types cannot be passed in as arguments in the type system
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
    ) -> TunnelArgoTunnel:
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
            cast_to=cast(Type[TunnelArgoTunnel], ResultWrapper[TunnelArgoTunnel]),
        )


class AsyncTunnels(AsyncAPIResource):
    @cached_property
    def configurations(self) -> AsyncConfigurations:
        return AsyncConfigurations(self._client)

    @cached_property
    def connections(self) -> AsyncConnections:
        return AsyncConnections(self._client)

    @cached_property
    def token(self) -> AsyncToken:
        return AsyncToken(self._client)

    @cached_property
    def connectors(self) -> AsyncConnectors:
        return AsyncConnectors(self._client)

    @cached_property
    def management(self) -> AsyncManagement:
        return AsyncManagement(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTunnelsWithRawResponse:
        return AsyncTunnelsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTunnelsWithStreamingResponse:
        return AsyncTunnelsWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        tunnel_secret: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TunnelArgoTunnel:
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
            body=await async_maybe_transform(
                {
                    "name": name,
                    "tunnel_secret": tunnel_secret,
                },
                tunnel_create_params.TunnelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TunnelArgoTunnel], ResultWrapper[TunnelArgoTunnel]),
        )

    def list(
        self,
        *,
        account_id: str,
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
    ) -> AsyncPaginator[TunnelListResponse, AsyncV4PagePaginationArray[TunnelListResponse]]:
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
        return self._get_api_list(
            f"/accounts/{account_id}/tunnels",
            page=AsyncV4PagePaginationArray[TunnelListResponse],
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
                    tunnel_list_params.TunnelListParams,
                ),
            ),
            model=cast(Any, TunnelListResponse),  # Union types cannot be passed in as arguments in the type system
        )

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
    ) -> TunnelArgoTunnel:
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
            body=await async_maybe_transform(body, tunnel_delete_params.TunnelDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TunnelArgoTunnel], ResultWrapper[TunnelArgoTunnel]),
        )

    async def edit(
        self,
        tunnel_id: str,
        *,
        account_id: str,
        name: str | NotGiven = NOT_GIVEN,
        tunnel_secret: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TunnelEditResponse:
        """
        Updates an existing Cloudflare Tunnel.

        Args:
          account_id: Cloudflare account ID

          tunnel_id: UUID of the tunnel.

          name: A user-friendly name for the tunnel.

          tunnel_secret: Sets the password required to run a locally-managed tunnel. Must be at least 32
              bytes and encoded as a base64 string.

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
            TunnelEditResponse,
            await self._patch(
                f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}",
                body=await async_maybe_transform(
                    {
                        "name": name,
                        "tunnel_secret": tunnel_secret,
                    },
                    tunnel_edit_params.TunnelEditParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[TunnelEditResponse]
                ),  # Union types cannot be passed in as arguments in the type system
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
    ) -> TunnelArgoTunnel:
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
            cast_to=cast(Type[TunnelArgoTunnel], ResultWrapper[TunnelArgoTunnel]),
        )


class TunnelsWithRawResponse:
    def __init__(self, tunnels: Tunnels) -> None:
        self._tunnels = tunnels

        self.create = to_raw_response_wrapper(
            tunnels.create,
        )
        self.list = to_raw_response_wrapper(
            tunnels.list,
        )
        self.delete = to_raw_response_wrapper(
            tunnels.delete,
        )
        self.edit = to_raw_response_wrapper(
            tunnels.edit,
        )
        self.get = to_raw_response_wrapper(
            tunnels.get,
        )

    @cached_property
    def configurations(self) -> ConfigurationsWithRawResponse:
        return ConfigurationsWithRawResponse(self._tunnels.configurations)

    @cached_property
    def connections(self) -> ConnectionsWithRawResponse:
        return ConnectionsWithRawResponse(self._tunnels.connections)

    @cached_property
    def token(self) -> TokenWithRawResponse:
        return TokenWithRawResponse(self._tunnels.token)

    @cached_property
    def connectors(self) -> ConnectorsWithRawResponse:
        return ConnectorsWithRawResponse(self._tunnels.connectors)

    @cached_property
    def management(self) -> ManagementWithRawResponse:
        return ManagementWithRawResponse(self._tunnels.management)


class AsyncTunnelsWithRawResponse:
    def __init__(self, tunnels: AsyncTunnels) -> None:
        self._tunnels = tunnels

        self.create = async_to_raw_response_wrapper(
            tunnels.create,
        )
        self.list = async_to_raw_response_wrapper(
            tunnels.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tunnels.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            tunnels.edit,
        )
        self.get = async_to_raw_response_wrapper(
            tunnels.get,
        )

    @cached_property
    def configurations(self) -> AsyncConfigurationsWithRawResponse:
        return AsyncConfigurationsWithRawResponse(self._tunnels.configurations)

    @cached_property
    def connections(self) -> AsyncConnectionsWithRawResponse:
        return AsyncConnectionsWithRawResponse(self._tunnels.connections)

    @cached_property
    def token(self) -> AsyncTokenWithRawResponse:
        return AsyncTokenWithRawResponse(self._tunnels.token)

    @cached_property
    def connectors(self) -> AsyncConnectorsWithRawResponse:
        return AsyncConnectorsWithRawResponse(self._tunnels.connectors)

    @cached_property
    def management(self) -> AsyncManagementWithRawResponse:
        return AsyncManagementWithRawResponse(self._tunnels.management)


class TunnelsWithStreamingResponse:
    def __init__(self, tunnels: Tunnels) -> None:
        self._tunnels = tunnels

        self.create = to_streamed_response_wrapper(
            tunnels.create,
        )
        self.list = to_streamed_response_wrapper(
            tunnels.list,
        )
        self.delete = to_streamed_response_wrapper(
            tunnels.delete,
        )
        self.edit = to_streamed_response_wrapper(
            tunnels.edit,
        )
        self.get = to_streamed_response_wrapper(
            tunnels.get,
        )

    @cached_property
    def configurations(self) -> ConfigurationsWithStreamingResponse:
        return ConfigurationsWithStreamingResponse(self._tunnels.configurations)

    @cached_property
    def connections(self) -> ConnectionsWithStreamingResponse:
        return ConnectionsWithStreamingResponse(self._tunnels.connections)

    @cached_property
    def token(self) -> TokenWithStreamingResponse:
        return TokenWithStreamingResponse(self._tunnels.token)

    @cached_property
    def connectors(self) -> ConnectorsWithStreamingResponse:
        return ConnectorsWithStreamingResponse(self._tunnels.connectors)

    @cached_property
    def management(self) -> ManagementWithStreamingResponse:
        return ManagementWithStreamingResponse(self._tunnels.management)


class AsyncTunnelsWithStreamingResponse:
    def __init__(self, tunnels: AsyncTunnels) -> None:
        self._tunnels = tunnels

        self.create = async_to_streamed_response_wrapper(
            tunnels.create,
        )
        self.list = async_to_streamed_response_wrapper(
            tunnels.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tunnels.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            tunnels.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            tunnels.get,
        )

    @cached_property
    def configurations(self) -> AsyncConfigurationsWithStreamingResponse:
        return AsyncConfigurationsWithStreamingResponse(self._tunnels.configurations)

    @cached_property
    def connections(self) -> AsyncConnectionsWithStreamingResponse:
        return AsyncConnectionsWithStreamingResponse(self._tunnels.connections)

    @cached_property
    def token(self) -> AsyncTokenWithStreamingResponse:
        return AsyncTokenWithStreamingResponse(self._tunnels.token)

    @cached_property
    def connectors(self) -> AsyncConnectorsWithStreamingResponse:
        return AsyncConnectorsWithStreamingResponse(self._tunnels.connectors)

    @cached_property
    def management(self) -> AsyncManagementWithStreamingResponse:
        return AsyncManagementWithStreamingResponse(self._tunnels.management)
