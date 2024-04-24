# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Union, cast
from datetime import datetime

import httpx

from .token import (
    TokenResource,
    AsyncTokenResource,
    TokenResourceWithRawResponse,
    AsyncTokenResourceWithRawResponse,
    TokenResourceWithStreamingResponse,
    AsyncTokenResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from .connectors import (
    ConnectorsResource,
    AsyncConnectorsResource,
    ConnectorsResourceWithRawResponse,
    AsyncConnectorsResourceWithRawResponse,
    ConnectorsResourceWithStreamingResponse,
    AsyncConnectorsResourceWithStreamingResponse,
)
from .management import (
    ManagementResource,
    AsyncManagementResource,
    ManagementResourceWithRawResponse,
    AsyncManagementResourceWithRawResponse,
    ManagementResourceWithStreamingResponse,
    AsyncManagementResourceWithStreamingResponse,
)
from .connections import (
    ConnectionsResource,
    AsyncConnectionsResource,
    ConnectionsResourceWithRawResponse,
    AsyncConnectionsResourceWithRawResponse,
    ConnectionsResourceWithStreamingResponse,
    AsyncConnectionsResourceWithStreamingResponse,
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
    ConfigurationsResource,
    AsyncConfigurationsResource,
    ConfigurationsResourceWithRawResponse,
    AsyncConfigurationsResourceWithRawResponse,
    ConfigurationsResourceWithStreamingResponse,
    AsyncConfigurationsResourceWithStreamingResponse,
)
from ...._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ....types.zero_trust import tunnel_edit_params, tunnel_list_params, tunnel_create_params
from ....types.zero_trust.tunnel_get_response import TunnelGetResponse
from ....types.zero_trust.tunnel_edit_response import TunnelEditResponse
from ....types.zero_trust.tunnel_list_response import TunnelListResponse
from ....types.zero_trust.tunnel_create_response import TunnelCreateResponse
from ....types.zero_trust.tunnel_delete_response import TunnelDeleteResponse

__all__ = ["TunnelsResource", "AsyncTunnelsResource"]


class TunnelsResource(SyncAPIResource):
    @cached_property
    def configurations(self) -> ConfigurationsResource:
        return ConfigurationsResource(self._client)

    @cached_property
    def connections(self) -> ConnectionsResource:
        return ConnectionsResource(self._client)

    @cached_property
    def token(self) -> TokenResource:
        return TokenResource(self._client)

    @cached_property
    def connectors(self) -> ConnectorsResource:
        return ConnectorsResource(self._client)

    @cached_property
    def management(self) -> ManagementResource:
        return ManagementResource(self._client)

    @cached_property
    def with_raw_response(self) -> TunnelsResourceWithRawResponse:
        return TunnelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TunnelsResourceWithStreamingResponse:
        return TunnelsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        tunnel_secret: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TunnelCreateResponse:
        """
        Creates a new Argo Tunnel in an account.

        Args:
          account_id: Cloudflare account ID

          name: A user-friendly name for a tunnel.

          tunnel_secret: Sets the password required to run a locally-managed tunnel. Must be at least 32
              bytes and encoded as a base64 string.

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
                post_parser=ResultWrapper[TunnelCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[TunnelCreateResponse], ResultWrapper[TunnelCreateResponse]),
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
        uuid: str | NotGiven = NOT_GIVEN,
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

          uuid: UUID of the tunnel.

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
                        "uuid": uuid,
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
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TunnelDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[TunnelDeleteResponse], ResultWrapper[TunnelDeleteResponse]),
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

          name: A user-friendly name for a tunnel.

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
                    post_parser=ResultWrapper[TunnelEditResponse]._unwrapper,
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
                post_parser=ResultWrapper[TunnelGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[TunnelGetResponse], ResultWrapper[TunnelGetResponse]),
        )


class AsyncTunnelsResource(AsyncAPIResource):
    @cached_property
    def configurations(self) -> AsyncConfigurationsResource:
        return AsyncConfigurationsResource(self._client)

    @cached_property
    def connections(self) -> AsyncConnectionsResource:
        return AsyncConnectionsResource(self._client)

    @cached_property
    def token(self) -> AsyncTokenResource:
        return AsyncTokenResource(self._client)

    @cached_property
    def connectors(self) -> AsyncConnectorsResource:
        return AsyncConnectorsResource(self._client)

    @cached_property
    def management(self) -> AsyncManagementResource:
        return AsyncManagementResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTunnelsResourceWithRawResponse:
        return AsyncTunnelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTunnelsResourceWithStreamingResponse:
        return AsyncTunnelsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        tunnel_secret: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TunnelCreateResponse:
        """
        Creates a new Argo Tunnel in an account.

        Args:
          account_id: Cloudflare account ID

          name: A user-friendly name for a tunnel.

          tunnel_secret: Sets the password required to run a locally-managed tunnel. Must be at least 32
              bytes and encoded as a base64 string.

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
                post_parser=ResultWrapper[TunnelCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[TunnelCreateResponse], ResultWrapper[TunnelCreateResponse]),
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
        uuid: str | NotGiven = NOT_GIVEN,
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

          uuid: UUID of the tunnel.

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
                        "uuid": uuid,
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
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TunnelDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[TunnelDeleteResponse], ResultWrapper[TunnelDeleteResponse]),
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

          name: A user-friendly name for a tunnel.

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
                    post_parser=ResultWrapper[TunnelEditResponse]._unwrapper,
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
                post_parser=ResultWrapper[TunnelGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[TunnelGetResponse], ResultWrapper[TunnelGetResponse]),
        )


class TunnelsResourceWithRawResponse:
    def __init__(self, tunnels: TunnelsResource) -> None:
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
    def configurations(self) -> ConfigurationsResourceWithRawResponse:
        return ConfigurationsResourceWithRawResponse(self._tunnels.configurations)

    @cached_property
    def connections(self) -> ConnectionsResourceWithRawResponse:
        return ConnectionsResourceWithRawResponse(self._tunnels.connections)

    @cached_property
    def token(self) -> TokenResourceWithRawResponse:
        return TokenResourceWithRawResponse(self._tunnels.token)

    @cached_property
    def connectors(self) -> ConnectorsResourceWithRawResponse:
        return ConnectorsResourceWithRawResponse(self._tunnels.connectors)

    @cached_property
    def management(self) -> ManagementResourceWithRawResponse:
        return ManagementResourceWithRawResponse(self._tunnels.management)


class AsyncTunnelsResourceWithRawResponse:
    def __init__(self, tunnels: AsyncTunnelsResource) -> None:
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
    def configurations(self) -> AsyncConfigurationsResourceWithRawResponse:
        return AsyncConfigurationsResourceWithRawResponse(self._tunnels.configurations)

    @cached_property
    def connections(self) -> AsyncConnectionsResourceWithRawResponse:
        return AsyncConnectionsResourceWithRawResponse(self._tunnels.connections)

    @cached_property
    def token(self) -> AsyncTokenResourceWithRawResponse:
        return AsyncTokenResourceWithRawResponse(self._tunnels.token)

    @cached_property
    def connectors(self) -> AsyncConnectorsResourceWithRawResponse:
        return AsyncConnectorsResourceWithRawResponse(self._tunnels.connectors)

    @cached_property
    def management(self) -> AsyncManagementResourceWithRawResponse:
        return AsyncManagementResourceWithRawResponse(self._tunnels.management)


class TunnelsResourceWithStreamingResponse:
    def __init__(self, tunnels: TunnelsResource) -> None:
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
    def configurations(self) -> ConfigurationsResourceWithStreamingResponse:
        return ConfigurationsResourceWithStreamingResponse(self._tunnels.configurations)

    @cached_property
    def connections(self) -> ConnectionsResourceWithStreamingResponse:
        return ConnectionsResourceWithStreamingResponse(self._tunnels.connections)

    @cached_property
    def token(self) -> TokenResourceWithStreamingResponse:
        return TokenResourceWithStreamingResponse(self._tunnels.token)

    @cached_property
    def connectors(self) -> ConnectorsResourceWithStreamingResponse:
        return ConnectorsResourceWithStreamingResponse(self._tunnels.connectors)

    @cached_property
    def management(self) -> ManagementResourceWithStreamingResponse:
        return ManagementResourceWithStreamingResponse(self._tunnels.management)


class AsyncTunnelsResourceWithStreamingResponse:
    def __init__(self, tunnels: AsyncTunnelsResource) -> None:
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
    def configurations(self) -> AsyncConfigurationsResourceWithStreamingResponse:
        return AsyncConfigurationsResourceWithStreamingResponse(self._tunnels.configurations)

    @cached_property
    def connections(self) -> AsyncConnectionsResourceWithStreamingResponse:
        return AsyncConnectionsResourceWithStreamingResponse(self._tunnels.connections)

    @cached_property
    def token(self) -> AsyncTokenResourceWithStreamingResponse:
        return AsyncTokenResourceWithStreamingResponse(self._tunnels.token)

    @cached_property
    def connectors(self) -> AsyncConnectorsResourceWithStreamingResponse:
        return AsyncConnectorsResourceWithStreamingResponse(self._tunnels.connectors)

    @cached_property
    def management(self) -> AsyncManagementResourceWithStreamingResponse:
        return AsyncManagementResourceWithStreamingResponse(self._tunnels.management)
