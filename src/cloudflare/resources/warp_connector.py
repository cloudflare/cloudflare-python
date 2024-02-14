# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types import (
    WarpConnectorCreateResponse,
    WarpConnectorUpdateResponse,
    WarpConnectorListResponse,
    WarpConnectorDeleteResponse,
    WarpConnectorGetResponse,
)

from typing import Type, Optional, Union

from datetime import datetime

from .._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from .._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ..types import shared_params
from ..types import warp_connector_create_params
from ..types import warp_connector_update_params
from ..types import warp_connector_list_params
from ..types import warp_connector_delete_params
from .._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["WarpConnector", "AsyncWarpConnector"]


class WarpConnector(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WarpConnectorWithRawResponse:
        return WarpConnectorWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WarpConnectorWithStreamingResponse:
        return WarpConnectorWithStreamingResponse(self)

    def create(
        self,
        account_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WarpConnectorCreateResponse:
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
            WarpConnectorCreateResponse,
            self._post(
                f"/accounts/{account_id}/warp_connector",
                body=maybe_transform({"name": name}, warp_connector_create_params.WarpConnectorCreateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[WarpConnectorCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

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
    ) -> WarpConnectorUpdateResponse:
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
            WarpConnectorUpdateResponse,
            self._patch(
                f"/accounts/{account_id}/warp_connector/{tunnel_id}",
                body=maybe_transform(
                    {
                        "name": name,
                        "tunnel_secret": tunnel_secret,
                    },
                    warp_connector_update_params.WarpConnectorUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[WarpConnectorUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
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
    ) -> Optional[WarpConnectorListResponse]:
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
        return self._get(
            f"/accounts/{account_id}/warp_connector",
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
                    warp_connector_list_params.WarpConnectorListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[WarpConnectorListResponse]], ResultWrapper[WarpConnectorListResponse]),
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
    ) -> WarpConnectorDeleteResponse:
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
            WarpConnectorDeleteResponse,
            self._delete(
                f"/accounts/{account_id}/warp_connector/{tunnel_id}",
                body=maybe_transform(body, warp_connector_delete_params.WarpConnectorDeleteParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[WarpConnectorDeleteResponse]
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
    ) -> WarpConnectorGetResponse:
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
            WarpConnectorGetResponse,
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
                    Any, ResultWrapper[WarpConnectorGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncWarpConnector(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWarpConnectorWithRawResponse:
        return AsyncWarpConnectorWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWarpConnectorWithStreamingResponse:
        return AsyncWarpConnectorWithStreamingResponse(self)

    async def create(
        self,
        account_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WarpConnectorCreateResponse:
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
            WarpConnectorCreateResponse,
            await self._post(
                f"/accounts/{account_id}/warp_connector",
                body=maybe_transform({"name": name}, warp_connector_create_params.WarpConnectorCreateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[WarpConnectorCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

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
    ) -> WarpConnectorUpdateResponse:
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
            WarpConnectorUpdateResponse,
            await self._patch(
                f"/accounts/{account_id}/warp_connector/{tunnel_id}",
                body=maybe_transform(
                    {
                        "name": name,
                        "tunnel_secret": tunnel_secret,
                    },
                    warp_connector_update_params.WarpConnectorUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[WarpConnectorUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def list(
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
    ) -> Optional[WarpConnectorListResponse]:
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
        return await self._get(
            f"/accounts/{account_id}/warp_connector",
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
                    warp_connector_list_params.WarpConnectorListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[WarpConnectorListResponse]], ResultWrapper[WarpConnectorListResponse]),
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
    ) -> WarpConnectorDeleteResponse:
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
            WarpConnectorDeleteResponse,
            await self._delete(
                f"/accounts/{account_id}/warp_connector/{tunnel_id}",
                body=maybe_transform(body, warp_connector_delete_params.WarpConnectorDeleteParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[WarpConnectorDeleteResponse]
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
    ) -> WarpConnectorGetResponse:
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
            WarpConnectorGetResponse,
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
                    Any, ResultWrapper[WarpConnectorGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class WarpConnectorWithRawResponse:
    def __init__(self, warp_connector: WarpConnector) -> None:
        self._warp_connector = warp_connector

        self.create = to_raw_response_wrapper(
            warp_connector.create,
        )
        self.update = to_raw_response_wrapper(
            warp_connector.update,
        )
        self.list = to_raw_response_wrapper(
            warp_connector.list,
        )
        self.delete = to_raw_response_wrapper(
            warp_connector.delete,
        )
        self.get = to_raw_response_wrapper(
            warp_connector.get,
        )


class AsyncWarpConnectorWithRawResponse:
    def __init__(self, warp_connector: AsyncWarpConnector) -> None:
        self._warp_connector = warp_connector

        self.create = async_to_raw_response_wrapper(
            warp_connector.create,
        )
        self.update = async_to_raw_response_wrapper(
            warp_connector.update,
        )
        self.list = async_to_raw_response_wrapper(
            warp_connector.list,
        )
        self.delete = async_to_raw_response_wrapper(
            warp_connector.delete,
        )
        self.get = async_to_raw_response_wrapper(
            warp_connector.get,
        )


class WarpConnectorWithStreamingResponse:
    def __init__(self, warp_connector: WarpConnector) -> None:
        self._warp_connector = warp_connector

        self.create = to_streamed_response_wrapper(
            warp_connector.create,
        )
        self.update = to_streamed_response_wrapper(
            warp_connector.update,
        )
        self.list = to_streamed_response_wrapper(
            warp_connector.list,
        )
        self.delete = to_streamed_response_wrapper(
            warp_connector.delete,
        )
        self.get = to_streamed_response_wrapper(
            warp_connector.get,
        )


class AsyncWarpConnectorWithStreamingResponse:
    def __init__(self, warp_connector: AsyncWarpConnector) -> None:
        self._warp_connector = warp_connector

        self.create = async_to_streamed_response_wrapper(
            warp_connector.create,
        )
        self.update = async_to_streamed_response_wrapper(
            warp_connector.update,
        )
        self.list = async_to_streamed_response_wrapper(
            warp_connector.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            warp_connector.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            warp_connector.get,
        )
