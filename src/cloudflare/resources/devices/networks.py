# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.devices import (
    NetworkUpdateResponse,
    NetworkDeleteResponse,
    NetworkDeviceManagedNetworksCreateDeviceManagedNetworkResponse,
    NetworkDeviceManagedNetworksListDeviceManagedNetworksResponse,
    NetworkGetResponse,
    network_update_params,
    network_device_managed_networks_create_device_managed_network_params,
)

from typing import Type, Optional

from typing_extensions import Literal

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
from ...types.devices import network_update_params
from ...types.devices import network_device_managed_networks_create_device_managed_network_params
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

__all__ = ["Networks", "AsyncNetworks"]


class Networks(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NetworksWithRawResponse:
        return NetworksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NetworksWithStreamingResponse:
        return NetworksWithStreamingResponse(self)

    def update(
        self,
        uuid: str,
        *,
        identifier: object,
        config: network_update_params.Config | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        type: Literal["tls"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[NetworkUpdateResponse]:
        """
        Updates a configured device managed network.

        Args:
          uuid: API UUID.

          config: The configuration object containing information for the WARP client to detect
              the managed network.

          name: The name of the device managed network. This name must be unique.

          type: The type of device managed network.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._put(
            f"/accounts/{identifier}/devices/networks/{uuid}",
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[NetworkUpdateResponse]], ResultWrapper[NetworkUpdateResponse]),
        )

    def delete(
        self,
        uuid: str,
        *,
        identifier: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[NetworkDeleteResponse]:
        """
        Deletes a device managed network and fetches a list of the remaining device
        managed networks for an account.

        Args:
          uuid: API UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._delete(
            f"/accounts/{identifier}/devices/networks/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[NetworkDeleteResponse]], ResultWrapper[NetworkDeleteResponse]),
        )

    def device_managed_networks_create_device_managed_network(
        self,
        identifier: object,
        *,
        config: network_device_managed_networks_create_device_managed_network_params.Config,
        name: str,
        type: Literal["tls"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[NetworkDeviceManagedNetworksCreateDeviceManagedNetworkResponse]:
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
        return self._post(
            f"/accounts/{identifier}/devices/networks",
            body=maybe_transform(
                {
                    "config": config,
                    "name": name,
                    "type": type,
                },
                network_device_managed_networks_create_device_managed_network_params.NetworkDeviceManagedNetworksCreateDeviceManagedNetworkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[NetworkDeviceManagedNetworksCreateDeviceManagedNetworkResponse]],
                ResultWrapper[NetworkDeviceManagedNetworksCreateDeviceManagedNetworkResponse],
            ),
        )

    def device_managed_networks_list_device_managed_networks(
        self,
        identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[NetworkDeviceManagedNetworksListDeviceManagedNetworksResponse]:
        """
        Fetches a list of managed networks for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{identifier}/devices/networks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[NetworkDeviceManagedNetworksListDeviceManagedNetworksResponse]],
                ResultWrapper[NetworkDeviceManagedNetworksListDeviceManagedNetworksResponse],
            ),
        )

    def get(
        self,
        uuid: str,
        *,
        identifier: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[NetworkGetResponse]:
        """
        Fetches details for a single managed network.

        Args:
          uuid: API UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._get(
            f"/accounts/{identifier}/devices/networks/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[NetworkGetResponse]], ResultWrapper[NetworkGetResponse]),
        )


class AsyncNetworks(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNetworksWithRawResponse:
        return AsyncNetworksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNetworksWithStreamingResponse:
        return AsyncNetworksWithStreamingResponse(self)

    async def update(
        self,
        uuid: str,
        *,
        identifier: object,
        config: network_update_params.Config | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        type: Literal["tls"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[NetworkUpdateResponse]:
        """
        Updates a configured device managed network.

        Args:
          uuid: API UUID.

          config: The configuration object containing information for the WARP client to detect
              the managed network.

          name: The name of the device managed network. This name must be unique.

          type: The type of device managed network.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._put(
            f"/accounts/{identifier}/devices/networks/{uuid}",
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[NetworkUpdateResponse]], ResultWrapper[NetworkUpdateResponse]),
        )

    async def delete(
        self,
        uuid: str,
        *,
        identifier: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[NetworkDeleteResponse]:
        """
        Deletes a device managed network and fetches a list of the remaining device
        managed networks for an account.

        Args:
          uuid: API UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._delete(
            f"/accounts/{identifier}/devices/networks/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[NetworkDeleteResponse]], ResultWrapper[NetworkDeleteResponse]),
        )

    async def device_managed_networks_create_device_managed_network(
        self,
        identifier: object,
        *,
        config: network_device_managed_networks_create_device_managed_network_params.Config,
        name: str,
        type: Literal["tls"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[NetworkDeviceManagedNetworksCreateDeviceManagedNetworkResponse]:
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
        return await self._post(
            f"/accounts/{identifier}/devices/networks",
            body=maybe_transform(
                {
                    "config": config,
                    "name": name,
                    "type": type,
                },
                network_device_managed_networks_create_device_managed_network_params.NetworkDeviceManagedNetworksCreateDeviceManagedNetworkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[NetworkDeviceManagedNetworksCreateDeviceManagedNetworkResponse]],
                ResultWrapper[NetworkDeviceManagedNetworksCreateDeviceManagedNetworkResponse],
            ),
        )

    async def device_managed_networks_list_device_managed_networks(
        self,
        identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[NetworkDeviceManagedNetworksListDeviceManagedNetworksResponse]:
        """
        Fetches a list of managed networks for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{identifier}/devices/networks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[NetworkDeviceManagedNetworksListDeviceManagedNetworksResponse]],
                ResultWrapper[NetworkDeviceManagedNetworksListDeviceManagedNetworksResponse],
            ),
        )

    async def get(
        self,
        uuid: str,
        *,
        identifier: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[NetworkGetResponse]:
        """
        Fetches details for a single managed network.

        Args:
          uuid: API UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._get(
            f"/accounts/{identifier}/devices/networks/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[NetworkGetResponse]], ResultWrapper[NetworkGetResponse]),
        )


class NetworksWithRawResponse:
    def __init__(self, networks: Networks) -> None:
        self._networks = networks

        self.update = to_raw_response_wrapper(
            networks.update,
        )
        self.delete = to_raw_response_wrapper(
            networks.delete,
        )
        self.device_managed_networks_create_device_managed_network = to_raw_response_wrapper(
            networks.device_managed_networks_create_device_managed_network,
        )
        self.device_managed_networks_list_device_managed_networks = to_raw_response_wrapper(
            networks.device_managed_networks_list_device_managed_networks,
        )
        self.get = to_raw_response_wrapper(
            networks.get,
        )


class AsyncNetworksWithRawResponse:
    def __init__(self, networks: AsyncNetworks) -> None:
        self._networks = networks

        self.update = async_to_raw_response_wrapper(
            networks.update,
        )
        self.delete = async_to_raw_response_wrapper(
            networks.delete,
        )
        self.device_managed_networks_create_device_managed_network = async_to_raw_response_wrapper(
            networks.device_managed_networks_create_device_managed_network,
        )
        self.device_managed_networks_list_device_managed_networks = async_to_raw_response_wrapper(
            networks.device_managed_networks_list_device_managed_networks,
        )
        self.get = async_to_raw_response_wrapper(
            networks.get,
        )


class NetworksWithStreamingResponse:
    def __init__(self, networks: Networks) -> None:
        self._networks = networks

        self.update = to_streamed_response_wrapper(
            networks.update,
        )
        self.delete = to_streamed_response_wrapper(
            networks.delete,
        )
        self.device_managed_networks_create_device_managed_network = to_streamed_response_wrapper(
            networks.device_managed_networks_create_device_managed_network,
        )
        self.device_managed_networks_list_device_managed_networks = to_streamed_response_wrapper(
            networks.device_managed_networks_list_device_managed_networks,
        )
        self.get = to_streamed_response_wrapper(
            networks.get,
        )


class AsyncNetworksWithStreamingResponse:
    def __init__(self, networks: AsyncNetworks) -> None:
        self._networks = networks

        self.update = async_to_streamed_response_wrapper(
            networks.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            networks.delete,
        )
        self.device_managed_networks_create_device_managed_network = async_to_streamed_response_wrapper(
            networks.device_managed_networks_create_device_managed_network,
        )
        self.device_managed_networks_list_device_managed_networks = async_to_streamed_response_wrapper(
            networks.device_managed_networks_list_device_managed_networks,
        )
        self.get = async_to_streamed_response_wrapper(
            networks.get,
        )
