# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.teamnets import (
    VirtualNetworkUpdateResponse,
    VirtualNetworkDeleteResponse,
    VirtualNetworkTunnelVirtualNetworkCreateAVirtualNetworkResponse,
    VirtualNetworkTunnelVirtualNetworkListVirtualNetworksResponse,
)

from typing import Type, Optional

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.teamnets import virtual_network_update_params
from ...types.teamnets import virtual_network_tunnel_virtual_network_create_a_virtual_network_params
from ...types.teamnets import virtual_network_tunnel_virtual_network_list_virtual_networks_params
from ..._wrappers import ResultWrapper
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

__all__ = ["VirtualNetworks", "AsyncVirtualNetworks"]


class VirtualNetworks(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VirtualNetworksWithRawResponse:
        return VirtualNetworksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VirtualNetworksWithStreamingResponse:
        return VirtualNetworksWithStreamingResponse(self)

    def update(
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
    ) -> VirtualNetworkUpdateResponse:
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
            VirtualNetworkUpdateResponse,
            self._patch(
                f"/accounts/{account_id}/teamnet/virtual_networks/{virtual_network_id}",
                body=maybe_transform(
                    {
                        "comment": comment,
                        "is_default_network": is_default_network,
                        "name": name,
                    },
                    virtual_network_update_params.VirtualNetworkUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[VirtualNetworkUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def delete(
        self,
        virtual_network_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VirtualNetworkDeleteResponse:
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
            VirtualNetworkDeleteResponse,
            self._delete(
                f"/accounts/{account_id}/teamnet/virtual_networks/{virtual_network_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[VirtualNetworkDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def tunnel_virtual_network_create_a_virtual_network(
        self,
        account_id: str,
        *,
        name: str,
        comment: str | NotGiven = NOT_GIVEN,
        is_default: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VirtualNetworkTunnelVirtualNetworkCreateAVirtualNetworkResponse:
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
            VirtualNetworkTunnelVirtualNetworkCreateAVirtualNetworkResponse,
            self._post(
                f"/accounts/{account_id}/teamnet/virtual_networks",
                body=maybe_transform(
                    {
                        "name": name,
                        "comment": comment,
                        "is_default": is_default,
                    },
                    virtual_network_tunnel_virtual_network_create_a_virtual_network_params.VirtualNetworkTunnelVirtualNetworkCreateAVirtualNetworkParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[VirtualNetworkTunnelVirtualNetworkCreateAVirtualNetworkResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def tunnel_virtual_network_list_virtual_networks(
        self,
        account_id: str,
        *,
        is_default: object | NotGiven = NOT_GIVEN,
        is_deleted: object | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        vnet_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[VirtualNetworkTunnelVirtualNetworkListVirtualNetworksResponse]:
        """
        Lists and filters virtual networks in an account.

        Args:
          account_id: Cloudflare account ID

          is_default: If `true`, only include the default virtual network. If `false`, exclude the
              default virtual network. If empty, all virtual networks will be included.

          is_deleted: If `true`, only include deleted virtual networks. If `false`, exclude deleted
              virtual networks. If empty, all virtual networks will be included.

          name: A user-friendly name for the virtual network.

          vnet_name: A user-friendly name for the virtual network.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/teamnet/virtual_networks",
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
                        "vnet_name": vnet_name,
                    },
                    virtual_network_tunnel_virtual_network_list_virtual_networks_params.VirtualNetworkTunnelVirtualNetworkListVirtualNetworksParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[VirtualNetworkTunnelVirtualNetworkListVirtualNetworksResponse]],
                ResultWrapper[VirtualNetworkTunnelVirtualNetworkListVirtualNetworksResponse],
            ),
        )


class AsyncVirtualNetworks(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVirtualNetworksWithRawResponse:
        return AsyncVirtualNetworksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVirtualNetworksWithStreamingResponse:
        return AsyncVirtualNetworksWithStreamingResponse(self)

    async def update(
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
    ) -> VirtualNetworkUpdateResponse:
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
            VirtualNetworkUpdateResponse,
            await self._patch(
                f"/accounts/{account_id}/teamnet/virtual_networks/{virtual_network_id}",
                body=maybe_transform(
                    {
                        "comment": comment,
                        "is_default_network": is_default_network,
                        "name": name,
                    },
                    virtual_network_update_params.VirtualNetworkUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[VirtualNetworkUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def delete(
        self,
        virtual_network_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VirtualNetworkDeleteResponse:
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
            VirtualNetworkDeleteResponse,
            await self._delete(
                f"/accounts/{account_id}/teamnet/virtual_networks/{virtual_network_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[VirtualNetworkDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def tunnel_virtual_network_create_a_virtual_network(
        self,
        account_id: str,
        *,
        name: str,
        comment: str | NotGiven = NOT_GIVEN,
        is_default: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VirtualNetworkTunnelVirtualNetworkCreateAVirtualNetworkResponse:
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
            VirtualNetworkTunnelVirtualNetworkCreateAVirtualNetworkResponse,
            await self._post(
                f"/accounts/{account_id}/teamnet/virtual_networks",
                body=maybe_transform(
                    {
                        "name": name,
                        "comment": comment,
                        "is_default": is_default,
                    },
                    virtual_network_tunnel_virtual_network_create_a_virtual_network_params.VirtualNetworkTunnelVirtualNetworkCreateAVirtualNetworkParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[VirtualNetworkTunnelVirtualNetworkCreateAVirtualNetworkResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def tunnel_virtual_network_list_virtual_networks(
        self,
        account_id: str,
        *,
        is_default: object | NotGiven = NOT_GIVEN,
        is_deleted: object | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        vnet_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[VirtualNetworkTunnelVirtualNetworkListVirtualNetworksResponse]:
        """
        Lists and filters virtual networks in an account.

        Args:
          account_id: Cloudflare account ID

          is_default: If `true`, only include the default virtual network. If `false`, exclude the
              default virtual network. If empty, all virtual networks will be included.

          is_deleted: If `true`, only include deleted virtual networks. If `false`, exclude deleted
              virtual networks. If empty, all virtual networks will be included.

          name: A user-friendly name for the virtual network.

          vnet_name: A user-friendly name for the virtual network.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/teamnet/virtual_networks",
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
                        "vnet_name": vnet_name,
                    },
                    virtual_network_tunnel_virtual_network_list_virtual_networks_params.VirtualNetworkTunnelVirtualNetworkListVirtualNetworksParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[VirtualNetworkTunnelVirtualNetworkListVirtualNetworksResponse]],
                ResultWrapper[VirtualNetworkTunnelVirtualNetworkListVirtualNetworksResponse],
            ),
        )


class VirtualNetworksWithRawResponse:
    def __init__(self, virtual_networks: VirtualNetworks) -> None:
        self._virtual_networks = virtual_networks

        self.update = to_raw_response_wrapper(
            virtual_networks.update,
        )
        self.delete = to_raw_response_wrapper(
            virtual_networks.delete,
        )
        self.tunnel_virtual_network_create_a_virtual_network = to_raw_response_wrapper(
            virtual_networks.tunnel_virtual_network_create_a_virtual_network,
        )
        self.tunnel_virtual_network_list_virtual_networks = to_raw_response_wrapper(
            virtual_networks.tunnel_virtual_network_list_virtual_networks,
        )


class AsyncVirtualNetworksWithRawResponse:
    def __init__(self, virtual_networks: AsyncVirtualNetworks) -> None:
        self._virtual_networks = virtual_networks

        self.update = async_to_raw_response_wrapper(
            virtual_networks.update,
        )
        self.delete = async_to_raw_response_wrapper(
            virtual_networks.delete,
        )
        self.tunnel_virtual_network_create_a_virtual_network = async_to_raw_response_wrapper(
            virtual_networks.tunnel_virtual_network_create_a_virtual_network,
        )
        self.tunnel_virtual_network_list_virtual_networks = async_to_raw_response_wrapper(
            virtual_networks.tunnel_virtual_network_list_virtual_networks,
        )


class VirtualNetworksWithStreamingResponse:
    def __init__(self, virtual_networks: VirtualNetworks) -> None:
        self._virtual_networks = virtual_networks

        self.update = to_streamed_response_wrapper(
            virtual_networks.update,
        )
        self.delete = to_streamed_response_wrapper(
            virtual_networks.delete,
        )
        self.tunnel_virtual_network_create_a_virtual_network = to_streamed_response_wrapper(
            virtual_networks.tunnel_virtual_network_create_a_virtual_network,
        )
        self.tunnel_virtual_network_list_virtual_networks = to_streamed_response_wrapper(
            virtual_networks.tunnel_virtual_network_list_virtual_networks,
        )


class AsyncVirtualNetworksWithStreamingResponse:
    def __init__(self, virtual_networks: AsyncVirtualNetworks) -> None:
        self._virtual_networks = virtual_networks

        self.update = async_to_streamed_response_wrapper(
            virtual_networks.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            virtual_networks.delete,
        )
        self.tunnel_virtual_network_create_a_virtual_network = async_to_streamed_response_wrapper(
            virtual_networks.tunnel_virtual_network_create_a_virtual_network,
        )
        self.tunnel_virtual_network_list_virtual_networks = async_to_streamed_response_wrapper(
            virtual_networks.tunnel_virtual_network_list_virtual_networks,
        )
