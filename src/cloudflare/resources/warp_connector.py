# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Union, cast
from datetime import datetime

import httpx

from ..types import (
    WARPConnectorGetResponse,
    WARPConnectorEditResponse,
    WARPConnectorListResponse,
    WARPConnectorTokenResponse,
    WARPConnectorCreateResponse,
    WARPConnectorDeleteResponse,
    warp_connector_edit_params,
    warp_connector_list_params,
    warp_connector_create_params,
    warp_connector_delete_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import ResultWrapper
from ..pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from .._base_client import (
    AsyncPaginator,
    make_request_options,
)

__all__ = ["WARPConnector", "AsyncWARPConnector"]


class WARPConnector(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WARPConnectorWithRawResponse:
        return WARPConnectorWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WARPConnectorWithStreamingResponse:
        return WARPConnectorWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WARPConnectorCreateResponse:
        """
        Creates a new Warp Connector Tunnel in an account.

        Args:
          account_id: Cloudflare account ID

          name: A user-friendly name for the tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            WARPConnectorCreateResponse,
            self._post(
                f"/accounts/{account_id}/warp_connector",
                body=maybe_transform({"name": name}, warp_connector_create_params.WARPConnectorCreateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[WARPConnectorCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
        was_active_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        was_inactive_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[WARPConnectorListResponse]:
        """
        Lists and filters Warp Connector Tunnels in an account.

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
        return self._get_api_list(
            f"/accounts/{account_id}/warp_connector",
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
                        "was_active_at": was_active_at,
                        "was_inactive_at": was_inactive_at,
                    },
                    warp_connector_list_params.WARPConnectorListParams,
                ),
            ),
            model=cast(
                Any, WARPConnectorListResponse
            ),  # Union types cannot be passed in as arguments in the type system
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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_id:
            raise ValueError(f"Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}")
        return cast(
            WARPConnectorDeleteResponse,
            self._delete(
                f"/accounts/{account_id}/warp_connector/{tunnel_id}",
                body=maybe_transform(body, warp_connector_delete_params.WARPConnectorDeleteParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[WARPConnectorDeleteResponse]
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
    ) -> WARPConnectorEditResponse:
        """
        Updates an existing Warp Connector Tunnel.

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
            WARPConnectorEditResponse,
            self._patch(
                f"/accounts/{account_id}/warp_connector/{tunnel_id}",
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
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[WARPConnectorEditResponse]
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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_id:
            raise ValueError(f"Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}")
        return cast(
            WARPConnectorGetResponse,
            self._get(
                f"/accounts/{account_id}/warp_connector/{tunnel_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[WARPConnectorGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def token(
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
    ) -> WARPConnectorTokenResponse:
        """
        Gets the token used to associate warp device with a specific Warp Connector
        tunnel.

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
            WARPConnectorTokenResponse,
            self._get(
                f"/accounts/{account_id}/warp_connector/{tunnel_id}/token",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[WARPConnectorTokenResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncWARPConnector(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWARPConnectorWithRawResponse:
        return AsyncWARPConnectorWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWARPConnectorWithStreamingResponse:
        return AsyncWARPConnectorWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WARPConnectorCreateResponse:
        """
        Creates a new Warp Connector Tunnel in an account.

        Args:
          account_id: Cloudflare account ID

          name: A user-friendly name for the tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            WARPConnectorCreateResponse,
            await self._post(
                f"/accounts/{account_id}/warp_connector",
                body=await async_maybe_transform(
                    {"name": name}, warp_connector_create_params.WARPConnectorCreateParams
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[WARPConnectorCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
        was_active_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        was_inactive_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[WARPConnectorListResponse, AsyncV4PagePaginationArray[WARPConnectorListResponse]]:
        """
        Lists and filters Warp Connector Tunnels in an account.

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
        return self._get_api_list(
            f"/accounts/{account_id}/warp_connector",
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
                        "was_active_at": was_active_at,
                        "was_inactive_at": was_inactive_at,
                    },
                    warp_connector_list_params.WARPConnectorListParams,
                ),
            ),
            model=cast(
                Any, WARPConnectorListResponse
            ),  # Union types cannot be passed in as arguments in the type system
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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_id:
            raise ValueError(f"Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}")
        return cast(
            WARPConnectorDeleteResponse,
            await self._delete(
                f"/accounts/{account_id}/warp_connector/{tunnel_id}",
                body=await async_maybe_transform(body, warp_connector_delete_params.WARPConnectorDeleteParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[WARPConnectorDeleteResponse]
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
    ) -> WARPConnectorEditResponse:
        """
        Updates an existing Warp Connector Tunnel.

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
            WARPConnectorEditResponse,
            await self._patch(
                f"/accounts/{account_id}/warp_connector/{tunnel_id}",
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
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[WARPConnectorEditResponse]
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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_id:
            raise ValueError(f"Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}")
        return cast(
            WARPConnectorGetResponse,
            await self._get(
                f"/accounts/{account_id}/warp_connector/{tunnel_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[WARPConnectorGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def token(
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
    ) -> WARPConnectorTokenResponse:
        """
        Gets the token used to associate warp device with a specific Warp Connector
        tunnel.

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
            WARPConnectorTokenResponse,
            await self._get(
                f"/accounts/{account_id}/warp_connector/{tunnel_id}/token",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[WARPConnectorTokenResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class WARPConnectorWithRawResponse:
    def __init__(self, warp_connector: WARPConnector) -> None:
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
        self.token = to_raw_response_wrapper(
            warp_connector.token,
        )


class AsyncWARPConnectorWithRawResponse:
    def __init__(self, warp_connector: AsyncWARPConnector) -> None:
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
        self.token = async_to_raw_response_wrapper(
            warp_connector.token,
        )


class WARPConnectorWithStreamingResponse:
    def __init__(self, warp_connector: WARPConnector) -> None:
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
        self.token = to_streamed_response_wrapper(
            warp_connector.token,
        )


class AsyncWARPConnectorWithStreamingResponse:
    def __init__(self, warp_connector: AsyncWARPConnector) -> None:
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
        self.token = async_to_streamed_response_wrapper(
            warp_connector.token,
        )
