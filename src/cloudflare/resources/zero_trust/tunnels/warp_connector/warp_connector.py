# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .token import (
    TokenResource,
    AsyncTokenResource,
    TokenResourceWithRawResponse,
    AsyncTokenResourceWithRawResponse,
    TokenResourceWithStreamingResponse,
    AsyncTokenResourceWithStreamingResponse,
)
from .failover import (
    FailoverResource,
    AsyncFailoverResource,
    FailoverResourceWithRawResponse,
    AsyncFailoverResourceWithRawResponse,
    FailoverResourceWithStreamingResponse,
    AsyncFailoverResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from .connectors import (
    ConnectorsResource,
    AsyncConnectorsResource,
    ConnectorsResourceWithRawResponse,
    AsyncConnectorsResourceWithRawResponse,
    ConnectorsResourceWithStreamingResponse,
    AsyncConnectorsResourceWithStreamingResponse,
)
from ....._compat import cached_property
from .connections import (
    ConnectionsResource,
    AsyncConnectionsResource,
    ConnectionsResourceWithRawResponse,
    AsyncConnectionsResourceWithRawResponse,
    ConnectionsResourceWithStreamingResponse,
    AsyncConnectionsResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from .....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ....._base_client import AsyncPaginator, make_request_options
from .....types.zero_trust.tunnels import (
    warp_connector_edit_params,
    warp_connector_list_params,
    warp_connector_create_params,
)
from .....types.zero_trust.tunnels.warp_connector_get_response import WARPConnectorGetResponse
from .....types.zero_trust.tunnels.warp_connector_edit_response import WARPConnectorEditResponse
from .....types.zero_trust.tunnels.warp_connector_list_response import WARPConnectorListResponse
from .....types.zero_trust.tunnels.warp_connector_create_response import WARPConnectorCreateResponse
from .....types.zero_trust.tunnels.warp_connector_delete_response import WARPConnectorDeleteResponse

__all__ = ["WARPConnectorResource", "AsyncWARPConnectorResource"]


class WARPConnectorResource(SyncAPIResource):
    @cached_property
    def token(self) -> TokenResource:
        return TokenResource(self._client)

    @cached_property
    def connections(self) -> ConnectionsResource:
        return ConnectionsResource(self._client)

    @cached_property
    def connectors(self) -> ConnectorsResource:
        return ConnectorsResource(self._client)

    @cached_property
    def failover(self) -> FailoverResource:
        return FailoverResource(self._client)

    @cached_property
    def with_raw_response(self) -> WARPConnectorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return WARPConnectorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WARPConnectorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return WARPConnectorResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str | None = None,
        name: str,
        ha: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WARPConnectorCreateResponse:
        """
        Creates a new Warp Connector Tunnel in an account.

        Args:
          account_id: Cloudflare account ID

          name: A user-friendly name for a tunnel.

          ha: Indicates that the tunnel will be created to be highly available. If omitted,
              defaults to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/warp_connector", account_id=account_id),
            body=maybe_transform(
                {
                    "name": name,
                    "ha": ha,
                },
                warp_connector_create_params.WARPConnectorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WARPConnectorCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[WARPConnectorCreateResponse], ResultWrapper[WARPConnectorCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str | None = None,
        exclude_prefix: str | Omit = omit,
        existed_at: str | Omit = omit,
        include_prefix: str | Omit = omit,
        is_deleted: bool | Omit = omit,
        name: str | Omit = omit,
        page: float | Omit = omit,
        per_page: float | Omit = omit,
        status: Literal["inactive", "degraded", "healthy", "down"] | Omit = omit,
        uuid: str | Omit = omit,
        was_active_at: Union[str, datetime] | Omit = omit,
        was_inactive_at: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[WARPConnectorListResponse]:
        """
        Lists and filters Warp Connector Tunnels in an account.

        Args:
          account_id: Cloudflare account ID

          existed_at: If provided, include only resources that were created (and not deleted) before
              this time. URL encoded.

          is_deleted: If `true`, only include deleted tunnels. If `false`, exclude deleted tunnels. If
              empty, all tunnels will be included.

          name: A user-friendly name for the tunnel.

          page: Page number of paginated results.

          per_page: Number of results to display.

          status: The status of the tunnel. Valid values are `inactive` (tunnel has never been
              run), `degraded` (tunnel is active and able to serve traffic but in an unhealthy
              state), `healthy` (tunnel is active and able to serve traffic), or `down`
              (tunnel can not serve traffic as it has no connections to the Cloudflare Edge).

          uuid: UUID of the tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/warp_connector", account_id=account_id),
            page=SyncV4PagePaginationArray[WARPConnectorListResponse],
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
                        "status": status,
                        "uuid": uuid,
                        "was_active_at": was_active_at,
                        "was_inactive_at": was_inactive_at,
                    },
                    warp_connector_list_params.WARPConnectorListParams,
                ),
            ),
            model=WARPConnectorListResponse,
        )

    def delete(
        self,
        tunnel_id: str,
        *,
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WARPConnectorDeleteResponse:
        """
        Deletes a Warp Connector Tunnel from an account.

        Args:
          account_id: Cloudflare account ID

          tunnel_id: UUID of the tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_id:
            raise ValueError(f"Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/warp_connector/{tunnel_id}", account_id=account_id, tunnel_id=tunnel_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WARPConnectorDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[WARPConnectorDeleteResponse], ResultWrapper[WARPConnectorDeleteResponse]),
        )

    def edit(
        self,
        tunnel_id: str,
        *,
        account_id: str | None = None,
        name: str | Omit = omit,
        tunnel_secret: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WARPConnectorEditResponse:
        """
        Updates an existing Warp Connector Tunnel.

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
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_id:
            raise ValueError(f"Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}")
        return self._patch(
            path_template(
                "/accounts/{account_id}/warp_connector/{tunnel_id}", account_id=account_id, tunnel_id=tunnel_id
            ),
            body=maybe_transform(
                {
                    "name": name,
                    "tunnel_secret": tunnel_secret,
                },
                warp_connector_edit_params.WARPConnectorEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WARPConnectorEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[WARPConnectorEditResponse], ResultWrapper[WARPConnectorEditResponse]),
        )

    def get(
        self,
        tunnel_id: str,
        *,
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WARPConnectorGetResponse:
        """
        Fetches a single Warp Connector Tunnel.

        Args:
          account_id: Cloudflare account ID

          tunnel_id: UUID of the tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_id:
            raise ValueError(f"Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/warp_connector/{tunnel_id}", account_id=account_id, tunnel_id=tunnel_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WARPConnectorGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[WARPConnectorGetResponse], ResultWrapper[WARPConnectorGetResponse]),
        )


class AsyncWARPConnectorResource(AsyncAPIResource):
    @cached_property
    def token(self) -> AsyncTokenResource:
        return AsyncTokenResource(self._client)

    @cached_property
    def connections(self) -> AsyncConnectionsResource:
        return AsyncConnectionsResource(self._client)

    @cached_property
    def connectors(self) -> AsyncConnectorsResource:
        return AsyncConnectorsResource(self._client)

    @cached_property
    def failover(self) -> AsyncFailoverResource:
        return AsyncFailoverResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWARPConnectorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWARPConnectorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWARPConnectorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncWARPConnectorResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str | None = None,
        name: str,
        ha: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WARPConnectorCreateResponse:
        """
        Creates a new Warp Connector Tunnel in an account.

        Args:
          account_id: Cloudflare account ID

          name: A user-friendly name for a tunnel.

          ha: Indicates that the tunnel will be created to be highly available. If omitted,
              defaults to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/warp_connector", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "ha": ha,
                },
                warp_connector_create_params.WARPConnectorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WARPConnectorCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[WARPConnectorCreateResponse], ResultWrapper[WARPConnectorCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str | None = None,
        exclude_prefix: str | Omit = omit,
        existed_at: str | Omit = omit,
        include_prefix: str | Omit = omit,
        is_deleted: bool | Omit = omit,
        name: str | Omit = omit,
        page: float | Omit = omit,
        per_page: float | Omit = omit,
        status: Literal["inactive", "degraded", "healthy", "down"] | Omit = omit,
        uuid: str | Omit = omit,
        was_active_at: Union[str, datetime] | Omit = omit,
        was_inactive_at: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WARPConnectorListResponse, AsyncV4PagePaginationArray[WARPConnectorListResponse]]:
        """
        Lists and filters Warp Connector Tunnels in an account.

        Args:
          account_id: Cloudflare account ID

          existed_at: If provided, include only resources that were created (and not deleted) before
              this time. URL encoded.

          is_deleted: If `true`, only include deleted tunnels. If `false`, exclude deleted tunnels. If
              empty, all tunnels will be included.

          name: A user-friendly name for the tunnel.

          page: Page number of paginated results.

          per_page: Number of results to display.

          status: The status of the tunnel. Valid values are `inactive` (tunnel has never been
              run), `degraded` (tunnel is active and able to serve traffic but in an unhealthy
              state), `healthy` (tunnel is active and able to serve traffic), or `down`
              (tunnel can not serve traffic as it has no connections to the Cloudflare Edge).

          uuid: UUID of the tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/warp_connector", account_id=account_id),
            page=AsyncV4PagePaginationArray[WARPConnectorListResponse],
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
                        "status": status,
                        "uuid": uuid,
                        "was_active_at": was_active_at,
                        "was_inactive_at": was_inactive_at,
                    },
                    warp_connector_list_params.WARPConnectorListParams,
                ),
            ),
            model=WARPConnectorListResponse,
        )

    async def delete(
        self,
        tunnel_id: str,
        *,
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WARPConnectorDeleteResponse:
        """
        Deletes a Warp Connector Tunnel from an account.

        Args:
          account_id: Cloudflare account ID

          tunnel_id: UUID of the tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_id:
            raise ValueError(f"Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/warp_connector/{tunnel_id}", account_id=account_id, tunnel_id=tunnel_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WARPConnectorDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[WARPConnectorDeleteResponse], ResultWrapper[WARPConnectorDeleteResponse]),
        )

    async def edit(
        self,
        tunnel_id: str,
        *,
        account_id: str | None = None,
        name: str | Omit = omit,
        tunnel_secret: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WARPConnectorEditResponse:
        """
        Updates an existing Warp Connector Tunnel.

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
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_id:
            raise ValueError(f"Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}")
        return await self._patch(
            path_template(
                "/accounts/{account_id}/warp_connector/{tunnel_id}", account_id=account_id, tunnel_id=tunnel_id
            ),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "tunnel_secret": tunnel_secret,
                },
                warp_connector_edit_params.WARPConnectorEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WARPConnectorEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[WARPConnectorEditResponse], ResultWrapper[WARPConnectorEditResponse]),
        )

    async def get(
        self,
        tunnel_id: str,
        *,
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WARPConnectorGetResponse:
        """
        Fetches a single Warp Connector Tunnel.

        Args:
          account_id: Cloudflare account ID

          tunnel_id: UUID of the tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_id:
            raise ValueError(f"Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/warp_connector/{tunnel_id}", account_id=account_id, tunnel_id=tunnel_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WARPConnectorGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[WARPConnectorGetResponse], ResultWrapper[WARPConnectorGetResponse]),
        )


class WARPConnectorResourceWithRawResponse:
    def __init__(self, warp_connector: WARPConnectorResource) -> None:
        self._warp_connector = warp_connector

        self.create = to_raw_response_wrapper(
            warp_connector.create,
        )
        self.list = to_raw_response_wrapper(
            warp_connector.list,
        )
        self.delete = to_raw_response_wrapper(
            warp_connector.delete,
        )
        self.edit = to_raw_response_wrapper(
            warp_connector.edit,
        )
        self.get = to_raw_response_wrapper(
            warp_connector.get,
        )

    @cached_property
    def token(self) -> TokenResourceWithRawResponse:
        return TokenResourceWithRawResponse(self._warp_connector.token)

    @cached_property
    def connections(self) -> ConnectionsResourceWithRawResponse:
        return ConnectionsResourceWithRawResponse(self._warp_connector.connections)

    @cached_property
    def connectors(self) -> ConnectorsResourceWithRawResponse:
        return ConnectorsResourceWithRawResponse(self._warp_connector.connectors)

    @cached_property
    def failover(self) -> FailoverResourceWithRawResponse:
        return FailoverResourceWithRawResponse(self._warp_connector.failover)


class AsyncWARPConnectorResourceWithRawResponse:
    def __init__(self, warp_connector: AsyncWARPConnectorResource) -> None:
        self._warp_connector = warp_connector

        self.create = async_to_raw_response_wrapper(
            warp_connector.create,
        )
        self.list = async_to_raw_response_wrapper(
            warp_connector.list,
        )
        self.delete = async_to_raw_response_wrapper(
            warp_connector.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            warp_connector.edit,
        )
        self.get = async_to_raw_response_wrapper(
            warp_connector.get,
        )

    @cached_property
    def token(self) -> AsyncTokenResourceWithRawResponse:
        return AsyncTokenResourceWithRawResponse(self._warp_connector.token)

    @cached_property
    def connections(self) -> AsyncConnectionsResourceWithRawResponse:
        return AsyncConnectionsResourceWithRawResponse(self._warp_connector.connections)

    @cached_property
    def connectors(self) -> AsyncConnectorsResourceWithRawResponse:
        return AsyncConnectorsResourceWithRawResponse(self._warp_connector.connectors)

    @cached_property
    def failover(self) -> AsyncFailoverResourceWithRawResponse:
        return AsyncFailoverResourceWithRawResponse(self._warp_connector.failover)


class WARPConnectorResourceWithStreamingResponse:
    def __init__(self, warp_connector: WARPConnectorResource) -> None:
        self._warp_connector = warp_connector

        self.create = to_streamed_response_wrapper(
            warp_connector.create,
        )
        self.list = to_streamed_response_wrapper(
            warp_connector.list,
        )
        self.delete = to_streamed_response_wrapper(
            warp_connector.delete,
        )
        self.edit = to_streamed_response_wrapper(
            warp_connector.edit,
        )
        self.get = to_streamed_response_wrapper(
            warp_connector.get,
        )

    @cached_property
    def token(self) -> TokenResourceWithStreamingResponse:
        return TokenResourceWithStreamingResponse(self._warp_connector.token)

    @cached_property
    def connections(self) -> ConnectionsResourceWithStreamingResponse:
        return ConnectionsResourceWithStreamingResponse(self._warp_connector.connections)

    @cached_property
    def connectors(self) -> ConnectorsResourceWithStreamingResponse:
        return ConnectorsResourceWithStreamingResponse(self._warp_connector.connectors)

    @cached_property
    def failover(self) -> FailoverResourceWithStreamingResponse:
        return FailoverResourceWithStreamingResponse(self._warp_connector.failover)


class AsyncWARPConnectorResourceWithStreamingResponse:
    def __init__(self, warp_connector: AsyncWARPConnectorResource) -> None:
        self._warp_connector = warp_connector

        self.create = async_to_streamed_response_wrapper(
            warp_connector.create,
        )
        self.list = async_to_streamed_response_wrapper(
            warp_connector.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            warp_connector.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            warp_connector.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            warp_connector.get,
        )

    @cached_property
    def token(self) -> AsyncTokenResourceWithStreamingResponse:
        return AsyncTokenResourceWithStreamingResponse(self._warp_connector.token)

    @cached_property
    def connections(self) -> AsyncConnectionsResourceWithStreamingResponse:
        return AsyncConnectionsResourceWithStreamingResponse(self._warp_connector.connections)

    @cached_property
    def connectors(self) -> AsyncConnectorsResourceWithStreamingResponse:
        return AsyncConnectorsResourceWithStreamingResponse(self._warp_connector.connectors)

    @cached_property
    def failover(self) -> AsyncFailoverResourceWithStreamingResponse:
        return AsyncFailoverResourceWithStreamingResponse(self._warp_connector.failover)
