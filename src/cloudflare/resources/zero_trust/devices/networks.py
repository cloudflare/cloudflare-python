# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

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
from ....types.zero_trust.devices import network_create_params, network_update_params
from ....types.zero_trust.devices.device_network import DeviceNetwork

__all__ = ["NetworksResource", "AsyncNetworksResource"]


class NetworksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NetworksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return NetworksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NetworksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return NetworksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        config: network_create_params.Config,
        name: str,
        type: Literal["tls"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DeviceNetwork]:
        """
        Creates a new device managed network.

        Args:
          config: The configuration object containing information for the WARP client to detect
              the managed network.

          name: The name of the device managed network. This name must be unique.

          type: The type of device managed network.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/devices/networks",
            body=maybe_transform(
                {
                    "config": config,
                    "name": name,
                    "type": type,
                },
                network_create_params.NetworkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DeviceNetwork]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DeviceNetwork]], ResultWrapper[DeviceNetwork]),
        )

    def update(
        self,
        network_id: str,
        *,
        account_id: str,
        config: network_update_params.Config | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        type: Literal["tls"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DeviceNetwork]:
        """
        Updates a configured device managed network.

        Args:
          network_id: API UUID.

          config: The configuration object containing information for the WARP client to detect
              the managed network.

          name: The name of the device managed network. This name must be unique.

          type: The type of device managed network.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not network_id:
            raise ValueError(f"Expected a non-empty value for `network_id` but received {network_id!r}")
        return self._put(
            f"/accounts/{account_id}/devices/networks/{network_id}",
            body=maybe_transform(
                {
                    "config": config,
                    "name": name,
                    "type": type,
                },
                network_update_params.NetworkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DeviceNetwork]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DeviceNetwork]], ResultWrapper[DeviceNetwork]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[DeviceNetwork]:
        """
        Fetches a list of managed networks for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/devices/networks",
            page=SyncSinglePage[DeviceNetwork],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=DeviceNetwork,
        )

    def delete(
        self,
        network_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[DeviceNetwork]:
        """
        Deletes a device managed network and fetches a list of the remaining device
        managed networks for an account.

        Args:
          network_id: API UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not network_id:
            raise ValueError(f"Expected a non-empty value for `network_id` but received {network_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/devices/networks/{network_id}",
            page=SyncSinglePage[DeviceNetwork],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=DeviceNetwork,
            method="delete",
        )

    def get(
        self,
        network_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DeviceNetwork]:
        """
        Fetches details for a single managed network.

        Args:
          network_id: API UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not network_id:
            raise ValueError(f"Expected a non-empty value for `network_id` but received {network_id!r}")
        return self._get(
            f"/accounts/{account_id}/devices/networks/{network_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DeviceNetwork]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DeviceNetwork]], ResultWrapper[DeviceNetwork]),
        )


class AsyncNetworksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNetworksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNetworksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNetworksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncNetworksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        config: network_create_params.Config,
        name: str,
        type: Literal["tls"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DeviceNetwork]:
        """
        Creates a new device managed network.

        Args:
          config: The configuration object containing information for the WARP client to detect
              the managed network.

          name: The name of the device managed network. This name must be unique.

          type: The type of device managed network.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/devices/networks",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "name": name,
                    "type": type,
                },
                network_create_params.NetworkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DeviceNetwork]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DeviceNetwork]], ResultWrapper[DeviceNetwork]),
        )

    async def update(
        self,
        network_id: str,
        *,
        account_id: str,
        config: network_update_params.Config | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        type: Literal["tls"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DeviceNetwork]:
        """
        Updates a configured device managed network.

        Args:
          network_id: API UUID.

          config: The configuration object containing information for the WARP client to detect
              the managed network.

          name: The name of the device managed network. This name must be unique.

          type: The type of device managed network.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not network_id:
            raise ValueError(f"Expected a non-empty value for `network_id` but received {network_id!r}")
        return await self._put(
            f"/accounts/{account_id}/devices/networks/{network_id}",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "name": name,
                    "type": type,
                },
                network_update_params.NetworkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DeviceNetwork]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DeviceNetwork]], ResultWrapper[DeviceNetwork]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[DeviceNetwork, AsyncSinglePage[DeviceNetwork]]:
        """
        Fetches a list of managed networks for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/devices/networks",
            page=AsyncSinglePage[DeviceNetwork],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=DeviceNetwork,
        )

    def delete(
        self,
        network_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[DeviceNetwork, AsyncSinglePage[DeviceNetwork]]:
        """
        Deletes a device managed network and fetches a list of the remaining device
        managed networks for an account.

        Args:
          network_id: API UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not network_id:
            raise ValueError(f"Expected a non-empty value for `network_id` but received {network_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/devices/networks/{network_id}",
            page=AsyncSinglePage[DeviceNetwork],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=DeviceNetwork,
            method="delete",
        )

    async def get(
        self,
        network_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DeviceNetwork]:
        """
        Fetches details for a single managed network.

        Args:
          network_id: API UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not network_id:
            raise ValueError(f"Expected a non-empty value for `network_id` but received {network_id!r}")
        return await self._get(
            f"/accounts/{account_id}/devices/networks/{network_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DeviceNetwork]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DeviceNetwork]], ResultWrapper[DeviceNetwork]),
        )


class NetworksResourceWithRawResponse:
    def __init__(self, networks: NetworksResource) -> None:
        self._networks = networks

        self.create = to_raw_response_wrapper(
            networks.create,
        )
        self.update = to_raw_response_wrapper(
            networks.update,
        )
        self.list = to_raw_response_wrapper(
            networks.list,
        )
        self.delete = to_raw_response_wrapper(
            networks.delete,
        )
        self.get = to_raw_response_wrapper(
            networks.get,
        )


class AsyncNetworksResourceWithRawResponse:
    def __init__(self, networks: AsyncNetworksResource) -> None:
        self._networks = networks

        self.create = async_to_raw_response_wrapper(
            networks.create,
        )
        self.update = async_to_raw_response_wrapper(
            networks.update,
        )
        self.list = async_to_raw_response_wrapper(
            networks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            networks.delete,
        )
        self.get = async_to_raw_response_wrapper(
            networks.get,
        )


class NetworksResourceWithStreamingResponse:
    def __init__(self, networks: NetworksResource) -> None:
        self._networks = networks

        self.create = to_streamed_response_wrapper(
            networks.create,
        )
        self.update = to_streamed_response_wrapper(
            networks.update,
        )
        self.list = to_streamed_response_wrapper(
            networks.list,
        )
        self.delete = to_streamed_response_wrapper(
            networks.delete,
        )
        self.get = to_streamed_response_wrapper(
            networks.get,
        )


class AsyncNetworksResourceWithStreamingResponse:
    def __init__(self, networks: AsyncNetworksResource) -> None:
        self._networks = networks

        self.create = async_to_streamed_response_wrapper(
            networks.create,
        )
        self.update = async_to_streamed_response_wrapper(
            networks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            networks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            networks.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            networks.get,
        )
