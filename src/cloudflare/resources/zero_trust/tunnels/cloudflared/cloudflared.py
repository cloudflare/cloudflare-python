# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Union, cast
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
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
from .configurations import (
    ConfigurationsResource,
    AsyncConfigurationsResource,
    ConfigurationsResourceWithRawResponse,
    AsyncConfigurationsResourceWithRawResponse,
    ConfigurationsResourceWithStreamingResponse,
    AsyncConfigurationsResourceWithStreamingResponse,
)
from ....._base_client import AsyncPaginator, make_request_options
from .....types.zero_trust.tunnels import cloudflared_edit_params, cloudflared_list_params, cloudflared_create_params
from .....types.zero_trust.tunnels.cloudflared_get_response import CloudflaredGetResponse
from .....types.zero_trust.tunnels.cloudflared_edit_response import CloudflaredEditResponse
from .....types.zero_trust.tunnels.cloudflared_list_response import CloudflaredListResponse
from .....types.zero_trust.tunnels.cloudflared_create_response import CloudflaredCreateResponse
from .....types.zero_trust.tunnels.cloudflared_delete_response import CloudflaredDeleteResponse

__all__ = ["CloudflaredResource", "AsyncCloudflaredResource"]


class CloudflaredResource(SyncAPIResource):
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
    def with_raw_response(self) -> CloudflaredResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CloudflaredResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CloudflaredResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CloudflaredResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        config_src: Literal["local", "cloudflare"] | NotGiven = NOT_GIVEN,
        tunnel_secret: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CloudflaredCreateResponse:
        """
        Creates a new Cloudflare Tunnel in an account.

        Args:
          account_id: Cloudflare account ID

          name: A user-friendly name for a tunnel.

          config_src: Indicates if this is a locally or remotely configured tunnel. If `local`, manage
              the tunnel using a YAML file on the origin machine. If `cloudflare`, manage the
              tunnel on the Zero Trust dashboard.

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
            CloudflaredCreateResponse,
            self._post(
                f"/accounts/{account_id}/cfd_tunnel",
                body=maybe_transform(
                    {
                        "name": name,
                        "config_src": config_src,
                        "tunnel_secret": tunnel_secret,
                    },
                    cloudflared_create_params.CloudflaredCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[CloudflaredCreateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CloudflaredCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        account_id: str,
        exclude_prefix: str | NotGiven = NOT_GIVEN,
        existed_at: str | NotGiven = NOT_GIVEN,
        include_prefix: str | NotGiven = NOT_GIVEN,
        is_deleted: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        status: Literal["inactive", "degraded", "healthy", "down"] | NotGiven = NOT_GIVEN,
        uuid: str | NotGiven = NOT_GIVEN,
        was_active_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        was_inactive_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[CloudflaredListResponse]:
        """
        Lists and filters Cloudflare Tunnels in an account.

        Args:
          account_id: Cloudflare account ID

          existed_at: If provided, include only resources that were created (and not deleted) before
              this time. URL encoded.

          is_deleted: If `true`, only include deleted tunnels. If `false`, exclude deleted tunnels. If
              empty, all tunnels will be included.

          name: A user-friendly name for a tunnel.

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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/cfd_tunnel",
            page=SyncV4PagePaginationArray[CloudflaredListResponse],
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
                    cloudflared_list_params.CloudflaredListParams,
                ),
            ),
            model=cast(Any, CloudflaredListResponse),  # Union types cannot be passed in as arguments in the type system
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
    ) -> CloudflaredDeleteResponse:
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
            CloudflaredDeleteResponse,
            self._delete(
                f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[CloudflaredDeleteResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CloudflaredDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> CloudflaredEditResponse:
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
            CloudflaredEditResponse,
            self._patch(
                f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}",
                body=maybe_transform(
                    {
                        "name": name,
                        "tunnel_secret": tunnel_secret,
                    },
                    cloudflared_edit_params.CloudflaredEditParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[CloudflaredEditResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CloudflaredEditResponse]
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
    ) -> CloudflaredGetResponse:
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
            CloudflaredGetResponse,
            self._get(
                f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[CloudflaredGetResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CloudflaredGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncCloudflaredResource(AsyncAPIResource):
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
    def with_raw_response(self) -> AsyncCloudflaredResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCloudflaredResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCloudflaredResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCloudflaredResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        config_src: Literal["local", "cloudflare"] | NotGiven = NOT_GIVEN,
        tunnel_secret: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CloudflaredCreateResponse:
        """
        Creates a new Cloudflare Tunnel in an account.

        Args:
          account_id: Cloudflare account ID

          name: A user-friendly name for a tunnel.

          config_src: Indicates if this is a locally or remotely configured tunnel. If `local`, manage
              the tunnel using a YAML file on the origin machine. If `cloudflare`, manage the
              tunnel on the Zero Trust dashboard.

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
            CloudflaredCreateResponse,
            await self._post(
                f"/accounts/{account_id}/cfd_tunnel",
                body=await async_maybe_transform(
                    {
                        "name": name,
                        "config_src": config_src,
                        "tunnel_secret": tunnel_secret,
                    },
                    cloudflared_create_params.CloudflaredCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[CloudflaredCreateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CloudflaredCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        account_id: str,
        exclude_prefix: str | NotGiven = NOT_GIVEN,
        existed_at: str | NotGiven = NOT_GIVEN,
        include_prefix: str | NotGiven = NOT_GIVEN,
        is_deleted: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        status: Literal["inactive", "degraded", "healthy", "down"] | NotGiven = NOT_GIVEN,
        uuid: str | NotGiven = NOT_GIVEN,
        was_active_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        was_inactive_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CloudflaredListResponse, AsyncV4PagePaginationArray[CloudflaredListResponse]]:
        """
        Lists and filters Cloudflare Tunnels in an account.

        Args:
          account_id: Cloudflare account ID

          existed_at: If provided, include only resources that were created (and not deleted) before
              this time. URL encoded.

          is_deleted: If `true`, only include deleted tunnels. If `false`, exclude deleted tunnels. If
              empty, all tunnels will be included.

          name: A user-friendly name for a tunnel.

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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/cfd_tunnel",
            page=AsyncV4PagePaginationArray[CloudflaredListResponse],
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
                    cloudflared_list_params.CloudflaredListParams,
                ),
            ),
            model=cast(Any, CloudflaredListResponse),  # Union types cannot be passed in as arguments in the type system
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
    ) -> CloudflaredDeleteResponse:
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
            CloudflaredDeleteResponse,
            await self._delete(
                f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[CloudflaredDeleteResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CloudflaredDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> CloudflaredEditResponse:
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
            CloudflaredEditResponse,
            await self._patch(
                f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}",
                body=await async_maybe_transform(
                    {
                        "name": name,
                        "tunnel_secret": tunnel_secret,
                    },
                    cloudflared_edit_params.CloudflaredEditParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[CloudflaredEditResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CloudflaredEditResponse]
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
    ) -> CloudflaredGetResponse:
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
            CloudflaredGetResponse,
            await self._get(
                f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[CloudflaredGetResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CloudflaredGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class CloudflaredResourceWithRawResponse:
    def __init__(self, cloudflared: CloudflaredResource) -> None:
        self._cloudflared = cloudflared

        self.create = to_raw_response_wrapper(
            cloudflared.create,
        )
        self.list = to_raw_response_wrapper(
            cloudflared.list,
        )
        self.delete = to_raw_response_wrapper(
            cloudflared.delete,
        )
        self.edit = to_raw_response_wrapper(
            cloudflared.edit,
        )
        self.get = to_raw_response_wrapper(
            cloudflared.get,
        )

    @cached_property
    def configurations(self) -> ConfigurationsResourceWithRawResponse:
        return ConfigurationsResourceWithRawResponse(self._cloudflared.configurations)

    @cached_property
    def connections(self) -> ConnectionsResourceWithRawResponse:
        return ConnectionsResourceWithRawResponse(self._cloudflared.connections)

    @cached_property
    def token(self) -> TokenResourceWithRawResponse:
        return TokenResourceWithRawResponse(self._cloudflared.token)

    @cached_property
    def connectors(self) -> ConnectorsResourceWithRawResponse:
        return ConnectorsResourceWithRawResponse(self._cloudflared.connectors)

    @cached_property
    def management(self) -> ManagementResourceWithRawResponse:
        return ManagementResourceWithRawResponse(self._cloudflared.management)


class AsyncCloudflaredResourceWithRawResponse:
    def __init__(self, cloudflared: AsyncCloudflaredResource) -> None:
        self._cloudflared = cloudflared

        self.create = async_to_raw_response_wrapper(
            cloudflared.create,
        )
        self.list = async_to_raw_response_wrapper(
            cloudflared.list,
        )
        self.delete = async_to_raw_response_wrapper(
            cloudflared.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            cloudflared.edit,
        )
        self.get = async_to_raw_response_wrapper(
            cloudflared.get,
        )

    @cached_property
    def configurations(self) -> AsyncConfigurationsResourceWithRawResponse:
        return AsyncConfigurationsResourceWithRawResponse(self._cloudflared.configurations)

    @cached_property
    def connections(self) -> AsyncConnectionsResourceWithRawResponse:
        return AsyncConnectionsResourceWithRawResponse(self._cloudflared.connections)

    @cached_property
    def token(self) -> AsyncTokenResourceWithRawResponse:
        return AsyncTokenResourceWithRawResponse(self._cloudflared.token)

    @cached_property
    def connectors(self) -> AsyncConnectorsResourceWithRawResponse:
        return AsyncConnectorsResourceWithRawResponse(self._cloudflared.connectors)

    @cached_property
    def management(self) -> AsyncManagementResourceWithRawResponse:
        return AsyncManagementResourceWithRawResponse(self._cloudflared.management)


class CloudflaredResourceWithStreamingResponse:
    def __init__(self, cloudflared: CloudflaredResource) -> None:
        self._cloudflared = cloudflared

        self.create = to_streamed_response_wrapper(
            cloudflared.create,
        )
        self.list = to_streamed_response_wrapper(
            cloudflared.list,
        )
        self.delete = to_streamed_response_wrapper(
            cloudflared.delete,
        )
        self.edit = to_streamed_response_wrapper(
            cloudflared.edit,
        )
        self.get = to_streamed_response_wrapper(
            cloudflared.get,
        )

    @cached_property
    def configurations(self) -> ConfigurationsResourceWithStreamingResponse:
        return ConfigurationsResourceWithStreamingResponse(self._cloudflared.configurations)

    @cached_property
    def connections(self) -> ConnectionsResourceWithStreamingResponse:
        return ConnectionsResourceWithStreamingResponse(self._cloudflared.connections)

    @cached_property
    def token(self) -> TokenResourceWithStreamingResponse:
        return TokenResourceWithStreamingResponse(self._cloudflared.token)

    @cached_property
    def connectors(self) -> ConnectorsResourceWithStreamingResponse:
        return ConnectorsResourceWithStreamingResponse(self._cloudflared.connectors)

    @cached_property
    def management(self) -> ManagementResourceWithStreamingResponse:
        return ManagementResourceWithStreamingResponse(self._cloudflared.management)


class AsyncCloudflaredResourceWithStreamingResponse:
    def __init__(self, cloudflared: AsyncCloudflaredResource) -> None:
        self._cloudflared = cloudflared

        self.create = async_to_streamed_response_wrapper(
            cloudflared.create,
        )
        self.list = async_to_streamed_response_wrapper(
            cloudflared.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            cloudflared.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            cloudflared.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            cloudflared.get,
        )

    @cached_property
    def configurations(self) -> AsyncConfigurationsResourceWithStreamingResponse:
        return AsyncConfigurationsResourceWithStreamingResponse(self._cloudflared.configurations)

    @cached_property
    def connections(self) -> AsyncConnectionsResourceWithStreamingResponse:
        return AsyncConnectionsResourceWithStreamingResponse(self._cloudflared.connections)

    @cached_property
    def token(self) -> AsyncTokenResourceWithStreamingResponse:
        return AsyncTokenResourceWithStreamingResponse(self._cloudflared.token)

    @cached_property
    def connectors(self) -> AsyncConnectorsResourceWithStreamingResponse:
        return AsyncConnectorsResourceWithStreamingResponse(self._cloudflared.connectors)

    @cached_property
    def management(self) -> AsyncManagementResourceWithStreamingResponse:
        return AsyncManagementResourceWithStreamingResponse(self._cloudflared.management)
