# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ....types.shared import UnnamedSchemaRef65e3c8c1a9c4638ec25cdbbaca7165c1
from ....types.zero_trust.networks import (
    VirtualNetwork,
    virtual_network_edit_params,
    virtual_network_list_params,
    virtual_network_create_params,
    virtual_network_delete_params,
)

__all__ = ["VirtualNetworks", "AsyncVirtualNetworks"]


class VirtualNetworks(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VirtualNetworksWithRawResponse:
        return VirtualNetworksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VirtualNetworksWithStreamingResponse:
        return VirtualNetworksWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        comment: str | NotGiven = NOT_GIVEN,
        is_default: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[UnnamedSchemaRef65e3c8c1a9c4638ec25cdbbaca7165c1]:
        """
        Adds a new virtual network to an account.

        Args:
          account_id: Cloudflare account ID

          name: A user-friendly name for the virtual network.

          comment: Optional remark describing the virtual network.

          is_default: If `true`, this virtual network is the default for the account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            Optional[UnnamedSchemaRef65e3c8c1a9c4638ec25cdbbaca7165c1],
            self._post(
                f"/accounts/{account_id}/teamnet/virtual_networks",
                body=maybe_transform(
                    {
                        "name": name,
                        "comment": comment,
                        "is_default": is_default,
                    },
                    virtual_network_create_params.VirtualNetworkCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[UnnamedSchemaRef65e3c8c1a9c4638ec25cdbbaca7165c1]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        account_id: str,
        is_default: object | NotGiven = NOT_GIVEN,
        is_deleted: object | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        vnet_id: str | NotGiven = NOT_GIVEN,
        vnet_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[VirtualNetwork]:
        """
        Lists and filters virtual networks in an account.

        Args:
          account_id: Cloudflare account ID

          is_default: If `true`, only include the default virtual network. If `false`, exclude the
              default virtual network. If empty, all virtual networks will be included.

          is_deleted: If `true`, only include deleted virtual networks. If `false`, exclude deleted
              virtual networks. If empty, all virtual networks will be included.

          name: A user-friendly name for the virtual network.

          vnet_id: UUID of the virtual network.

          vnet_name: A user-friendly name for the virtual network.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/teamnet/virtual_networks",
            page=SyncSinglePage[VirtualNetwork],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "is_default": is_default,
                        "is_deleted": is_deleted,
                        "name": name,
                        "vnet_id": vnet_id,
                        "vnet_name": vnet_name,
                    },
                    virtual_network_list_params.VirtualNetworkListParams,
                ),
            ),
            model=VirtualNetwork,
        )

    def delete(
        self,
        virtual_network_id: str,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[UnnamedSchemaRef65e3c8c1a9c4638ec25cdbbaca7165c1]:
        """
        Deletes an existing virtual network.

        Args:
          account_id: Cloudflare account ID

          virtual_network_id: UUID of the virtual network.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not virtual_network_id:
            raise ValueError(f"Expected a non-empty value for `virtual_network_id` but received {virtual_network_id!r}")
        return cast(
            Optional[UnnamedSchemaRef65e3c8c1a9c4638ec25cdbbaca7165c1],
            self._delete(
                f"/accounts/{account_id}/teamnet/virtual_networks/{virtual_network_id}",
                body=maybe_transform(body, virtual_network_delete_params.VirtualNetworkDeleteParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[UnnamedSchemaRef65e3c8c1a9c4638ec25cdbbaca7165c1]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def edit(
        self,
        virtual_network_id: str,
        *,
        account_id: str,
        comment: str | NotGiven = NOT_GIVEN,
        is_default_network: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[UnnamedSchemaRef65e3c8c1a9c4638ec25cdbbaca7165c1]:
        """
        Updates an existing virtual network.

        Args:
          account_id: Cloudflare account ID

          virtual_network_id: UUID of the virtual network.

          comment: Optional remark describing the virtual network.

          is_default_network: If `true`, this virtual network is the default for the account.

          name: A user-friendly name for the virtual network.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not virtual_network_id:
            raise ValueError(f"Expected a non-empty value for `virtual_network_id` but received {virtual_network_id!r}")
        return cast(
            Optional[UnnamedSchemaRef65e3c8c1a9c4638ec25cdbbaca7165c1],
            self._patch(
                f"/accounts/{account_id}/teamnet/virtual_networks/{virtual_network_id}",
                body=maybe_transform(
                    {
                        "comment": comment,
                        "is_default_network": is_default_network,
                        "name": name,
                    },
                    virtual_network_edit_params.VirtualNetworkEditParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[UnnamedSchemaRef65e3c8c1a9c4638ec25cdbbaca7165c1]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncVirtualNetworks(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVirtualNetworksWithRawResponse:
        return AsyncVirtualNetworksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVirtualNetworksWithStreamingResponse:
        return AsyncVirtualNetworksWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        comment: str | NotGiven = NOT_GIVEN,
        is_default: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[UnnamedSchemaRef65e3c8c1a9c4638ec25cdbbaca7165c1]:
        """
        Adds a new virtual network to an account.

        Args:
          account_id: Cloudflare account ID

          name: A user-friendly name for the virtual network.

          comment: Optional remark describing the virtual network.

          is_default: If `true`, this virtual network is the default for the account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            Optional[UnnamedSchemaRef65e3c8c1a9c4638ec25cdbbaca7165c1],
            await self._post(
                f"/accounts/{account_id}/teamnet/virtual_networks",
                body=await async_maybe_transform(
                    {
                        "name": name,
                        "comment": comment,
                        "is_default": is_default,
                    },
                    virtual_network_create_params.VirtualNetworkCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[UnnamedSchemaRef65e3c8c1a9c4638ec25cdbbaca7165c1]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        account_id: str,
        is_default: object | NotGiven = NOT_GIVEN,
        is_deleted: object | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        vnet_id: str | NotGiven = NOT_GIVEN,
        vnet_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[VirtualNetwork, AsyncSinglePage[VirtualNetwork]]:
        """
        Lists and filters virtual networks in an account.

        Args:
          account_id: Cloudflare account ID

          is_default: If `true`, only include the default virtual network. If `false`, exclude the
              default virtual network. If empty, all virtual networks will be included.

          is_deleted: If `true`, only include deleted virtual networks. If `false`, exclude deleted
              virtual networks. If empty, all virtual networks will be included.

          name: A user-friendly name for the virtual network.

          vnet_id: UUID of the virtual network.

          vnet_name: A user-friendly name for the virtual network.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/teamnet/virtual_networks",
            page=AsyncSinglePage[VirtualNetwork],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "is_default": is_default,
                        "is_deleted": is_deleted,
                        "name": name,
                        "vnet_id": vnet_id,
                        "vnet_name": vnet_name,
                    },
                    virtual_network_list_params.VirtualNetworkListParams,
                ),
            ),
            model=VirtualNetwork,
        )

    async def delete(
        self,
        virtual_network_id: str,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[UnnamedSchemaRef65e3c8c1a9c4638ec25cdbbaca7165c1]:
        """
        Deletes an existing virtual network.

        Args:
          account_id: Cloudflare account ID

          virtual_network_id: UUID of the virtual network.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not virtual_network_id:
            raise ValueError(f"Expected a non-empty value for `virtual_network_id` but received {virtual_network_id!r}")
        return cast(
            Optional[UnnamedSchemaRef65e3c8c1a9c4638ec25cdbbaca7165c1],
            await self._delete(
                f"/accounts/{account_id}/teamnet/virtual_networks/{virtual_network_id}",
                body=await async_maybe_transform(body, virtual_network_delete_params.VirtualNetworkDeleteParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[UnnamedSchemaRef65e3c8c1a9c4638ec25cdbbaca7165c1]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def edit(
        self,
        virtual_network_id: str,
        *,
        account_id: str,
        comment: str | NotGiven = NOT_GIVEN,
        is_default_network: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[UnnamedSchemaRef65e3c8c1a9c4638ec25cdbbaca7165c1]:
        """
        Updates an existing virtual network.

        Args:
          account_id: Cloudflare account ID

          virtual_network_id: UUID of the virtual network.

          comment: Optional remark describing the virtual network.

          is_default_network: If `true`, this virtual network is the default for the account.

          name: A user-friendly name for the virtual network.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not virtual_network_id:
            raise ValueError(f"Expected a non-empty value for `virtual_network_id` but received {virtual_network_id!r}")
        return cast(
            Optional[UnnamedSchemaRef65e3c8c1a9c4638ec25cdbbaca7165c1],
            await self._patch(
                f"/accounts/{account_id}/teamnet/virtual_networks/{virtual_network_id}",
                body=await async_maybe_transform(
                    {
                        "comment": comment,
                        "is_default_network": is_default_network,
                        "name": name,
                    },
                    virtual_network_edit_params.VirtualNetworkEditParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[UnnamedSchemaRef65e3c8c1a9c4638ec25cdbbaca7165c1]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class VirtualNetworksWithRawResponse:
    def __init__(self, virtual_networks: VirtualNetworks) -> None:
        self._virtual_networks = virtual_networks

        self.create = to_raw_response_wrapper(
            virtual_networks.create,
        )
        self.list = to_raw_response_wrapper(
            virtual_networks.list,
        )
        self.delete = to_raw_response_wrapper(
            virtual_networks.delete,
        )
        self.edit = to_raw_response_wrapper(
            virtual_networks.edit,
        )


class AsyncVirtualNetworksWithRawResponse:
    def __init__(self, virtual_networks: AsyncVirtualNetworks) -> None:
        self._virtual_networks = virtual_networks

        self.create = async_to_raw_response_wrapper(
            virtual_networks.create,
        )
        self.list = async_to_raw_response_wrapper(
            virtual_networks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            virtual_networks.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            virtual_networks.edit,
        )


class VirtualNetworksWithStreamingResponse:
    def __init__(self, virtual_networks: VirtualNetworks) -> None:
        self._virtual_networks = virtual_networks

        self.create = to_streamed_response_wrapper(
            virtual_networks.create,
        )
        self.list = to_streamed_response_wrapper(
            virtual_networks.list,
        )
        self.delete = to_streamed_response_wrapper(
            virtual_networks.delete,
        )
        self.edit = to_streamed_response_wrapper(
            virtual_networks.edit,
        )


class AsyncVirtualNetworksWithStreamingResponse:
    def __init__(self, virtual_networks: AsyncVirtualNetworks) -> None:
        self._virtual_networks = virtual_networks

        self.create = async_to_streamed_response_wrapper(
            virtual_networks.create,
        )
        self.list = async_to_streamed_response_wrapper(
            virtual_networks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            virtual_networks.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            virtual_networks.edit,
        )
