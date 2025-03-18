# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...._base_client import AsyncPaginator, make_request_options
from ....types.zero_trust import tunnel_list_params
from .cloudflared.cloudflared import (
    CloudflaredResource,
    AsyncCloudflaredResource,
    CloudflaredResourceWithRawResponse,
    AsyncCloudflaredResourceWithRawResponse,
    CloudflaredResourceWithStreamingResponse,
    AsyncCloudflaredResourceWithStreamingResponse,
)
from .warp_connector.warp_connector import (
    WARPConnectorResource,
    AsyncWARPConnectorResource,
    WARPConnectorResourceWithRawResponse,
    AsyncWARPConnectorResourceWithRawResponse,
    WARPConnectorResourceWithStreamingResponse,
    AsyncWARPConnectorResourceWithStreamingResponse,
)
from ....types.zero_trust.tunnel_list_response import TunnelListResponse

__all__ = ["TunnelsResource", "AsyncTunnelsResource"]


class TunnelsResource(SyncAPIResource):
    @cached_property
    def cloudflared(self) -> CloudflaredResource:
        return CloudflaredResource(self._client)

    @cached_property
    def warp_connector(self) -> WARPConnectorResource:
        return WARPConnectorResource(self._client)

    @cached_property
    def with_raw_response(self) -> TunnelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TunnelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TunnelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TunnelsResourceWithStreamingResponse(self)

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
        tun_types: List[Literal["cfd_tunnel", "warp_connector", "warp", "magic", "ip_sec", "gre", "cni"]]
        | NotGiven = NOT_GIVEN,
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

          tun_types: The types of tunnels to filter by, separated by commas.

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
                        "status": status,
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


class AsyncTunnelsResource(AsyncAPIResource):
    @cached_property
    def cloudflared(self) -> AsyncCloudflaredResource:
        return AsyncCloudflaredResource(self._client)

    @cached_property
    def warp_connector(self) -> AsyncWARPConnectorResource:
        return AsyncWARPConnectorResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTunnelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTunnelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTunnelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTunnelsResourceWithStreamingResponse(self)

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
        tun_types: List[Literal["cfd_tunnel", "warp_connector", "warp", "magic", "ip_sec", "gre", "cni"]]
        | NotGiven = NOT_GIVEN,
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

          tun_types: The types of tunnels to filter by, separated by commas.

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
                        "status": status,
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


class TunnelsResourceWithRawResponse:
    def __init__(self, tunnels: TunnelsResource) -> None:
        self._tunnels = tunnels

        self.list = to_raw_response_wrapper(
            tunnels.list,
        )

    @cached_property
    def cloudflared(self) -> CloudflaredResourceWithRawResponse:
        return CloudflaredResourceWithRawResponse(self._tunnels.cloudflared)

    @cached_property
    def warp_connector(self) -> WARPConnectorResourceWithRawResponse:
        return WARPConnectorResourceWithRawResponse(self._tunnels.warp_connector)


class AsyncTunnelsResourceWithRawResponse:
    def __init__(self, tunnels: AsyncTunnelsResource) -> None:
        self._tunnels = tunnels

        self.list = async_to_raw_response_wrapper(
            tunnels.list,
        )

    @cached_property
    def cloudflared(self) -> AsyncCloudflaredResourceWithRawResponse:
        return AsyncCloudflaredResourceWithRawResponse(self._tunnels.cloudflared)

    @cached_property
    def warp_connector(self) -> AsyncWARPConnectorResourceWithRawResponse:
        return AsyncWARPConnectorResourceWithRawResponse(self._tunnels.warp_connector)


class TunnelsResourceWithStreamingResponse:
    def __init__(self, tunnels: TunnelsResource) -> None:
        self._tunnels = tunnels

        self.list = to_streamed_response_wrapper(
            tunnels.list,
        )

    @cached_property
    def cloudflared(self) -> CloudflaredResourceWithStreamingResponse:
        return CloudflaredResourceWithStreamingResponse(self._tunnels.cloudflared)

    @cached_property
    def warp_connector(self) -> WARPConnectorResourceWithStreamingResponse:
        return WARPConnectorResourceWithStreamingResponse(self._tunnels.warp_connector)


class AsyncTunnelsResourceWithStreamingResponse:
    def __init__(self, tunnels: AsyncTunnelsResource) -> None:
        self._tunnels = tunnels

        self.list = async_to_streamed_response_wrapper(
            tunnels.list,
        )

    @cached_property
    def cloudflared(self) -> AsyncCloudflaredResourceWithStreamingResponse:
        return AsyncCloudflaredResourceWithStreamingResponse(self._tunnels.cloudflared)

    @cached_property
    def warp_connector(self) -> AsyncWARPConnectorResourceWithStreamingResponse:
        return AsyncWARPConnectorResourceWithStreamingResponse(self._tunnels.warp_connector)
