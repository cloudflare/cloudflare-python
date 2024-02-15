# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, Type, Union, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .tokens import (
    Tokens,
    AsyncTokens,
    TokensWithRawResponse,
    AsyncTokensWithRawResponse,
    TokensWithStreamingResponse,
    AsyncTokensWithStreamingResponse,
)
from ...types import (
    CfdTunnelGetResponse,
    CfdTunnelDeleteResponse,
    CfdTunnelUpdateResponse,
    CfdTunnelCloudflareTunnelListCloudflareTunnelsResponse,
    CfdTunnelCloudflareTunnelCreateACloudflareTunnelResponse,
    cfd_tunnel_delete_params,
    cfd_tunnel_update_params,
    cfd_tunnel_cloudflare_tunnel_list_cloudflare_tunnels_params,
    cfd_tunnel_cloudflare_tunnel_create_a_cloudflare_tunnel_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
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
from .configurations import (
    Configurations,
    AsyncConfigurations,
    ConfigurationsWithRawResponse,
    AsyncConfigurationsWithRawResponse,
    ConfigurationsWithStreamingResponse,
    AsyncConfigurationsWithStreamingResponse,
)

__all__ = ["CfdTunnels", "AsyncCfdTunnels"]


class CfdTunnels(SyncAPIResource):
    @cached_property
    def configurations(self) -> Configurations:
        return Configurations(self._client)

    @cached_property
    def connections(self) -> Connections:
        return Connections(self._client)

    @cached_property
    def tokens(self) -> Tokens:
        return Tokens(self._client)

    @cached_property
    def connectors(self) -> Connectors:
        return Connectors(self._client)

    @cached_property
    def management(self) -> Management:
        return Management(self._client)

    @cached_property
    def with_raw_response(self) -> CfdTunnelsWithRawResponse:
        return CfdTunnelsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CfdTunnelsWithStreamingResponse:
        return CfdTunnelsWithStreamingResponse(self)

    def update(
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
    ) -> CfdTunnelUpdateResponse:
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
            CfdTunnelUpdateResponse,
            self._patch(
                f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}",
                body=maybe_transform(
                    {
                        "name": name,
                        "tunnel_secret": tunnel_secret,
                    },
                    cfd_tunnel_update_params.CfdTunnelUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CfdTunnelUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> CfdTunnelDeleteResponse:
        """
        Deletes a Cloudflare Tunnel from an account.

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
        return cast(
            CfdTunnelDeleteResponse,
            self._delete(
                f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}",
                body=maybe_transform(body, cfd_tunnel_delete_params.CfdTunnelDeleteParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CfdTunnelDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def cloudflare_tunnel_create_a_cloudflare_tunnel(
        self,
        account_id: str,
        *,
        name: str,
        config_src: Literal["local", "cloudflare"] | NotGiven = NOT_GIVEN,
        tunnel_secret: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CfdTunnelCloudflareTunnelCreateACloudflareTunnelResponse:
        """
        Creates a new Cloudflare Tunnel in an account.

        Args:
          account_id: Cloudflare account ID

          name: A user-friendly name for the tunnel.

          config_src: Indicates if this is a locally or remotely configured tunnel. If `local`, manage
              the tunnel using a YAML file on the origin machine. If `cloudflare`, manage the
              tunnel on the Zero Trust dashboard or using the
              [Cloudflare Tunnel configuration](https://api.cloudflare.com/#cloudflare-tunnel-configuration-properties)
              endpoint.

          tunnel_secret: Sets the password required to run a locally-managed tunnel. Must be at least 32
              bytes and encoded as a base64 string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            CfdTunnelCloudflareTunnelCreateACloudflareTunnelResponse,
            self._post(
                f"/accounts/{account_id}/cfd_tunnel",
                body=maybe_transform(
                    {
                        "name": name,
                        "config_src": config_src,
                        "tunnel_secret": tunnel_secret,
                    },
                    cfd_tunnel_cloudflare_tunnel_create_a_cloudflare_tunnel_params.CfdTunnelCloudflareTunnelCreateACloudflareTunnelParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CfdTunnelCloudflareTunnelCreateACloudflareTunnelResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def cloudflare_tunnel_list_cloudflare_tunnels(
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
        was_active_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        was_inactive_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CfdTunnelCloudflareTunnelListCloudflareTunnelsResponse]:
        """
        Lists and filters Cloudflare Tunnels in an account.

        Args:
          account_id: Cloudflare account ID

          existed_at: If provided, include only tunnels that were created (and not deleted) before
              this time.

          is_deleted: If `true`, only include deleted tunnels. If `false`, exclude deleted tunnels. If
              empty, all tunnels will be included.

          name: A user-friendly name for the tunnel.

          page: Page number of paginated results.

          per_page: Number of results to display.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/cfd_tunnel",
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
                        "was_active_at": was_active_at,
                        "was_inactive_at": was_inactive_at,
                    },
                    cfd_tunnel_cloudflare_tunnel_list_cloudflare_tunnels_params.CfdTunnelCloudflareTunnelListCloudflareTunnelsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[CfdTunnelCloudflareTunnelListCloudflareTunnelsResponse]],
                ResultWrapper[CfdTunnelCloudflareTunnelListCloudflareTunnelsResponse],
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
    ) -> CfdTunnelGetResponse:
        """
        Fetches a single Cloudflare Tunnel.

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
        return cast(
            CfdTunnelGetResponse,
            self._get(
                f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CfdTunnelGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncCfdTunnels(AsyncAPIResource):
    @cached_property
    def configurations(self) -> AsyncConfigurations:
        return AsyncConfigurations(self._client)

    @cached_property
    def connections(self) -> AsyncConnections:
        return AsyncConnections(self._client)

    @cached_property
    def tokens(self) -> AsyncTokens:
        return AsyncTokens(self._client)

    @cached_property
    def connectors(self) -> AsyncConnectors:
        return AsyncConnectors(self._client)

    @cached_property
    def management(self) -> AsyncManagement:
        return AsyncManagement(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCfdTunnelsWithRawResponse:
        return AsyncCfdTunnelsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCfdTunnelsWithStreamingResponse:
        return AsyncCfdTunnelsWithStreamingResponse(self)

    async def update(
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
    ) -> CfdTunnelUpdateResponse:
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
            CfdTunnelUpdateResponse,
            await self._patch(
                f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}",
                body=maybe_transform(
                    {
                        "name": name,
                        "tunnel_secret": tunnel_secret,
                    },
                    cfd_tunnel_update_params.CfdTunnelUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CfdTunnelUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> CfdTunnelDeleteResponse:
        """
        Deletes a Cloudflare Tunnel from an account.

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
        return cast(
            CfdTunnelDeleteResponse,
            await self._delete(
                f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}",
                body=maybe_transform(body, cfd_tunnel_delete_params.CfdTunnelDeleteParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CfdTunnelDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def cloudflare_tunnel_create_a_cloudflare_tunnel(
        self,
        account_id: str,
        *,
        name: str,
        config_src: Literal["local", "cloudflare"] | NotGiven = NOT_GIVEN,
        tunnel_secret: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CfdTunnelCloudflareTunnelCreateACloudflareTunnelResponse:
        """
        Creates a new Cloudflare Tunnel in an account.

        Args:
          account_id: Cloudflare account ID

          name: A user-friendly name for the tunnel.

          config_src: Indicates if this is a locally or remotely configured tunnel. If `local`, manage
              the tunnel using a YAML file on the origin machine. If `cloudflare`, manage the
              tunnel on the Zero Trust dashboard or using the
              [Cloudflare Tunnel configuration](https://api.cloudflare.com/#cloudflare-tunnel-configuration-properties)
              endpoint.

          tunnel_secret: Sets the password required to run a locally-managed tunnel. Must be at least 32
              bytes and encoded as a base64 string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            CfdTunnelCloudflareTunnelCreateACloudflareTunnelResponse,
            await self._post(
                f"/accounts/{account_id}/cfd_tunnel",
                body=maybe_transform(
                    {
                        "name": name,
                        "config_src": config_src,
                        "tunnel_secret": tunnel_secret,
                    },
                    cfd_tunnel_cloudflare_tunnel_create_a_cloudflare_tunnel_params.CfdTunnelCloudflareTunnelCreateACloudflareTunnelParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CfdTunnelCloudflareTunnelCreateACloudflareTunnelResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def cloudflare_tunnel_list_cloudflare_tunnels(
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
        was_active_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        was_inactive_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CfdTunnelCloudflareTunnelListCloudflareTunnelsResponse]:
        """
        Lists and filters Cloudflare Tunnels in an account.

        Args:
          account_id: Cloudflare account ID

          existed_at: If provided, include only tunnels that were created (and not deleted) before
              this time.

          is_deleted: If `true`, only include deleted tunnels. If `false`, exclude deleted tunnels. If
              empty, all tunnels will be included.

          name: A user-friendly name for the tunnel.

          page: Page number of paginated results.

          per_page: Number of results to display.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/cfd_tunnel",
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
                        "was_active_at": was_active_at,
                        "was_inactive_at": was_inactive_at,
                    },
                    cfd_tunnel_cloudflare_tunnel_list_cloudflare_tunnels_params.CfdTunnelCloudflareTunnelListCloudflareTunnelsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[CfdTunnelCloudflareTunnelListCloudflareTunnelsResponse]],
                ResultWrapper[CfdTunnelCloudflareTunnelListCloudflareTunnelsResponse],
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
    ) -> CfdTunnelGetResponse:
        """
        Fetches a single Cloudflare Tunnel.

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
        return cast(
            CfdTunnelGetResponse,
            await self._get(
                f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CfdTunnelGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class CfdTunnelsWithRawResponse:
    def __init__(self, cfd_tunnels: CfdTunnels) -> None:
        self._cfd_tunnels = cfd_tunnels

        self.update = to_raw_response_wrapper(
            cfd_tunnels.update,
        )
        self.delete = to_raw_response_wrapper(
            cfd_tunnels.delete,
        )
        self.cloudflare_tunnel_create_a_cloudflare_tunnel = to_raw_response_wrapper(
            cfd_tunnels.cloudflare_tunnel_create_a_cloudflare_tunnel,
        )
        self.cloudflare_tunnel_list_cloudflare_tunnels = to_raw_response_wrapper(
            cfd_tunnels.cloudflare_tunnel_list_cloudflare_tunnels,
        )
        self.get = to_raw_response_wrapper(
            cfd_tunnels.get,
        )

    @cached_property
    def configurations(self) -> ConfigurationsWithRawResponse:
        return ConfigurationsWithRawResponse(self._cfd_tunnels.configurations)

    @cached_property
    def connections(self) -> ConnectionsWithRawResponse:
        return ConnectionsWithRawResponse(self._cfd_tunnels.connections)

    @cached_property
    def tokens(self) -> TokensWithRawResponse:
        return TokensWithRawResponse(self._cfd_tunnels.tokens)

    @cached_property
    def connectors(self) -> ConnectorsWithRawResponse:
        return ConnectorsWithRawResponse(self._cfd_tunnels.connectors)

    @cached_property
    def management(self) -> ManagementWithRawResponse:
        return ManagementWithRawResponse(self._cfd_tunnels.management)


class AsyncCfdTunnelsWithRawResponse:
    def __init__(self, cfd_tunnels: AsyncCfdTunnels) -> None:
        self._cfd_tunnels = cfd_tunnels

        self.update = async_to_raw_response_wrapper(
            cfd_tunnels.update,
        )
        self.delete = async_to_raw_response_wrapper(
            cfd_tunnels.delete,
        )
        self.cloudflare_tunnel_create_a_cloudflare_tunnel = async_to_raw_response_wrapper(
            cfd_tunnels.cloudflare_tunnel_create_a_cloudflare_tunnel,
        )
        self.cloudflare_tunnel_list_cloudflare_tunnels = async_to_raw_response_wrapper(
            cfd_tunnels.cloudflare_tunnel_list_cloudflare_tunnels,
        )
        self.get = async_to_raw_response_wrapper(
            cfd_tunnels.get,
        )

    @cached_property
    def configurations(self) -> AsyncConfigurationsWithRawResponse:
        return AsyncConfigurationsWithRawResponse(self._cfd_tunnels.configurations)

    @cached_property
    def connections(self) -> AsyncConnectionsWithRawResponse:
        return AsyncConnectionsWithRawResponse(self._cfd_tunnels.connections)

    @cached_property
    def tokens(self) -> AsyncTokensWithRawResponse:
        return AsyncTokensWithRawResponse(self._cfd_tunnels.tokens)

    @cached_property
    def connectors(self) -> AsyncConnectorsWithRawResponse:
        return AsyncConnectorsWithRawResponse(self._cfd_tunnels.connectors)

    @cached_property
    def management(self) -> AsyncManagementWithRawResponse:
        return AsyncManagementWithRawResponse(self._cfd_tunnels.management)


class CfdTunnelsWithStreamingResponse:
    def __init__(self, cfd_tunnels: CfdTunnels) -> None:
        self._cfd_tunnels = cfd_tunnels

        self.update = to_streamed_response_wrapper(
            cfd_tunnels.update,
        )
        self.delete = to_streamed_response_wrapper(
            cfd_tunnels.delete,
        )
        self.cloudflare_tunnel_create_a_cloudflare_tunnel = to_streamed_response_wrapper(
            cfd_tunnels.cloudflare_tunnel_create_a_cloudflare_tunnel,
        )
        self.cloudflare_tunnel_list_cloudflare_tunnels = to_streamed_response_wrapper(
            cfd_tunnels.cloudflare_tunnel_list_cloudflare_tunnels,
        )
        self.get = to_streamed_response_wrapper(
            cfd_tunnels.get,
        )

    @cached_property
    def configurations(self) -> ConfigurationsWithStreamingResponse:
        return ConfigurationsWithStreamingResponse(self._cfd_tunnels.configurations)

    @cached_property
    def connections(self) -> ConnectionsWithStreamingResponse:
        return ConnectionsWithStreamingResponse(self._cfd_tunnels.connections)

    @cached_property
    def tokens(self) -> TokensWithStreamingResponse:
        return TokensWithStreamingResponse(self._cfd_tunnels.tokens)

    @cached_property
    def connectors(self) -> ConnectorsWithStreamingResponse:
        return ConnectorsWithStreamingResponse(self._cfd_tunnels.connectors)

    @cached_property
    def management(self) -> ManagementWithStreamingResponse:
        return ManagementWithStreamingResponse(self._cfd_tunnels.management)


class AsyncCfdTunnelsWithStreamingResponse:
    def __init__(self, cfd_tunnels: AsyncCfdTunnels) -> None:
        self._cfd_tunnels = cfd_tunnels

        self.update = async_to_streamed_response_wrapper(
            cfd_tunnels.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            cfd_tunnels.delete,
        )
        self.cloudflare_tunnel_create_a_cloudflare_tunnel = async_to_streamed_response_wrapper(
            cfd_tunnels.cloudflare_tunnel_create_a_cloudflare_tunnel,
        )
        self.cloudflare_tunnel_list_cloudflare_tunnels = async_to_streamed_response_wrapper(
            cfd_tunnels.cloudflare_tunnel_list_cloudflare_tunnels,
        )
        self.get = async_to_streamed_response_wrapper(
            cfd_tunnels.get,
        )

    @cached_property
    def configurations(self) -> AsyncConfigurationsWithStreamingResponse:
        return AsyncConfigurationsWithStreamingResponse(self._cfd_tunnels.configurations)

    @cached_property
    def connections(self) -> AsyncConnectionsWithStreamingResponse:
        return AsyncConnectionsWithStreamingResponse(self._cfd_tunnels.connections)

    @cached_property
    def tokens(self) -> AsyncTokensWithStreamingResponse:
        return AsyncTokensWithStreamingResponse(self._cfd_tunnels.tokens)

    @cached_property
    def connectors(self) -> AsyncConnectorsWithStreamingResponse:
        return AsyncConnectorsWithStreamingResponse(self._cfd_tunnels.connectors)

    @cached_property
    def management(self) -> AsyncManagementWithStreamingResponse:
        return AsyncManagementWithStreamingResponse(self._cfd_tunnels.management)
