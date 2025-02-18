# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

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
from ...._base_client import AsyncPaginator, make_request_options
from ....types.zero_trust.networks import (
    virtual_network_edit_params,
    virtual_network_list_params,
    virtual_network_create_params,
)
from ....types.zero_trust.networks.virtual_network import VirtualNetwork

__all__ = ["VirtualNetworksResource", "AsyncVirtualNetworksResource"]


class VirtualNetworksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VirtualNetworksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return VirtualNetworksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VirtualNetworksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return VirtualNetworksResourceWithStreamingResponse(self)

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
    ) -> VirtualNetwork:
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
        return self._post(
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
                post_parser=ResultWrapper[VirtualNetwork]._unwrapper,
            ),
            cast_to=cast(Type[VirtualNetwork], ResultWrapper[VirtualNetwork]),
        )

    def list(
        self,
        *,
        account_id: str,
        id: str | NotGiven = NOT_GIVEN,
        is_default: bool | NotGiven = NOT_GIVEN,
        is_deleted: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
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

          id: UUID of the virtual network.

          is_default: If `true`, only include the default virtual network. If `false`, exclude the
              default virtual network. If empty, all virtual networks will be included.

          is_deleted: If `true`, only include deleted virtual networks. If `false`, exclude deleted
              virtual networks. If empty, all virtual networks will be included.

          name: A user-friendly name for the virtual network.

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
                        "id": id,
                        "is_default": is_default,
                        "is_deleted": is_deleted,
                        "name": name,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VirtualNetwork:
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
        return self._delete(
            f"/accounts/{account_id}/teamnet/virtual_networks/{virtual_network_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[VirtualNetwork]._unwrapper,
            ),
            cast_to=cast(Type[VirtualNetwork], ResultWrapper[VirtualNetwork]),
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
    ) -> VirtualNetwork:
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
        return self._patch(
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
                post_parser=ResultWrapper[VirtualNetwork]._unwrapper,
            ),
            cast_to=cast(Type[VirtualNetwork], ResultWrapper[VirtualNetwork]),
        )

    def get(
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
    ) -> VirtualNetwork:
        """
        Get a virtual network.

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
        return self._get(
            f"/accounts/{account_id}/teamnet/virtual_networks/{virtual_network_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[VirtualNetwork]._unwrapper,
            ),
            cast_to=cast(Type[VirtualNetwork], ResultWrapper[VirtualNetwork]),
        )


class AsyncVirtualNetworksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVirtualNetworksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVirtualNetworksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVirtualNetworksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncVirtualNetworksResourceWithStreamingResponse(self)

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
    ) -> VirtualNetwork:
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
        return await self._post(
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
                post_parser=ResultWrapper[VirtualNetwork]._unwrapper,
            ),
            cast_to=cast(Type[VirtualNetwork], ResultWrapper[VirtualNetwork]),
        )

    def list(
        self,
        *,
        account_id: str,
        id: str | NotGiven = NOT_GIVEN,
        is_default: bool | NotGiven = NOT_GIVEN,
        is_deleted: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
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

          id: UUID of the virtual network.

          is_default: If `true`, only include the default virtual network. If `false`, exclude the
              default virtual network. If empty, all virtual networks will be included.

          is_deleted: If `true`, only include deleted virtual networks. If `false`, exclude deleted
              virtual networks. If empty, all virtual networks will be included.

          name: A user-friendly name for the virtual network.

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
                        "id": id,
                        "is_default": is_default,
                        "is_deleted": is_deleted,
                        "name": name,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VirtualNetwork:
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
        return await self._delete(
            f"/accounts/{account_id}/teamnet/virtual_networks/{virtual_network_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[VirtualNetwork]._unwrapper,
            ),
            cast_to=cast(Type[VirtualNetwork], ResultWrapper[VirtualNetwork]),
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
    ) -> VirtualNetwork:
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
        return await self._patch(
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
                post_parser=ResultWrapper[VirtualNetwork]._unwrapper,
            ),
            cast_to=cast(Type[VirtualNetwork], ResultWrapper[VirtualNetwork]),
        )

    async def get(
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
    ) -> VirtualNetwork:
        """
        Get a virtual network.

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
        return await self._get(
            f"/accounts/{account_id}/teamnet/virtual_networks/{virtual_network_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[VirtualNetwork]._unwrapper,
            ),
            cast_to=cast(Type[VirtualNetwork], ResultWrapper[VirtualNetwork]),
        )


class VirtualNetworksResourceWithRawResponse:
    def __init__(self, virtual_networks: VirtualNetworksResource) -> None:
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
        self.get = to_raw_response_wrapper(
            virtual_networks.get,
        )


class AsyncVirtualNetworksResourceWithRawResponse:
    def __init__(self, virtual_networks: AsyncVirtualNetworksResource) -> None:
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
        self.get = async_to_raw_response_wrapper(
            virtual_networks.get,
        )


class VirtualNetworksResourceWithStreamingResponse:
    def __init__(self, virtual_networks: VirtualNetworksResource) -> None:
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
        self.get = to_streamed_response_wrapper(
            virtual_networks.get,
        )


class AsyncVirtualNetworksResourceWithStreamingResponse:
    def __init__(self, virtual_networks: AsyncVirtualNetworksResource) -> None:
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
        self.get = async_to_streamed_response_wrapper(
            virtual_networks.get,
        )
