# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.magic_transit.gre_tunnel_create_response import GRETunnelCreateResponse

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from ..._base_client import make_request_options

from typing import Type

from ...types.magic_transit.gre_tunnel_update_response import GRETunnelUpdateResponse

from ...types.magic_transit.health_check_param import HealthCheckParam

from ...types.magic_transit.gre_tunnel_list_response import GRETunnelListResponse

from ...types.magic_transit.gre_tunnel_delete_response import GRETunnelDeleteResponse

from ...types.magic_transit.gre_tunnel_get_response import GRETunnelGetResponse

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from ...types.magic_transit import gre_tunnel_create_params
from ...types.magic_transit import gre_tunnel_update_params
from ...types.magic_transit import HealthCheck
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

__all__ = ["GRETunnelsResource", "AsyncGRETunnelsResource"]

class GRETunnelsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GRETunnelsResourceWithRawResponse:
        return GRETunnelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GRETunnelsResourceWithStreamingResponse:
        return GRETunnelsResourceWithStreamingResponse(self)

    def create(self,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> GRETunnelCreateResponse:
        """Creates new GRE tunnels.

        Use `?validate_only=true` as an optional query
        parameter to only run validation without persisting changes.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._post(
            f"/accounts/{account_id}/magic/gre_tunnels",
            body=maybe_transform(body, gre_tunnel_create_params.GRETunnelCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[GRETunnelCreateResponse]._unwrapper),
            cast_to=cast(Type[GRETunnelCreateResponse], ResultWrapper[GRETunnelCreateResponse]),
        )

    def update(self,
    gre_tunnel_id: str,
    *,
    account_id: str,
    cloudflare_gre_endpoint: str,
    customer_gre_endpoint: str,
    interface_address: str,
    name: str,
    description: str | NotGiven = NOT_GIVEN,
    health_check: HealthCheckParam | NotGiven = NOT_GIVEN,
    mtu: int | NotGiven = NOT_GIVEN,
    ttl: int | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> GRETunnelUpdateResponse:
        """Updates a specific GRE tunnel.

        Use `?validate_only=true` as an optional query
        parameter to only run validation without persisting changes.

        Args:
          account_id: Identifier

          gre_tunnel_id: Identifier

          cloudflare_gre_endpoint: The IP address assigned to the Cloudflare side of the GRE tunnel.

          customer_gre_endpoint: The IP address assigned to the customer side of the GRE tunnel.

          interface_address: A 31-bit prefix (/31 in CIDR notation) supporting two hosts, one for each side
              of the tunnel. Select the subnet from the following private IP space:
              10.0.0.0–10.255.255.255, 172.16.0.0–172.31.255.255, 192.168.0.0–192.168.255.255.

          name: The name of the tunnel. The name cannot contain spaces or special characters,
              must be 15 characters or less, and cannot share a name with another GRE tunnel.

          description: An optional description of the GRE tunnel.

          mtu: Maximum Transmission Unit (MTU) in bytes for the GRE tunnel. The minimum value
              is 576.

          ttl: Time To Live (TTL) in number of hops of the GRE tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not gre_tunnel_id:
          raise ValueError(
            f'Expected a non-empty value for `gre_tunnel_id` but received {gre_tunnel_id!r}'
          )
        return self._put(
            f"/accounts/{account_id}/magic/gre_tunnels/{gre_tunnel_id}",
            body=maybe_transform({
                "cloudflare_gre_endpoint": cloudflare_gre_endpoint,
                "customer_gre_endpoint": customer_gre_endpoint,
                "interface_address": interface_address,
                "name": name,
                "description": description,
                "health_check": health_check,
                "mtu": mtu,
                "ttl": ttl,
            }, gre_tunnel_update_params.GRETunnelUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[GRETunnelUpdateResponse]._unwrapper),
            cast_to=cast(Type[GRETunnelUpdateResponse], ResultWrapper[GRETunnelUpdateResponse]),
        )

    def list(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> GRETunnelListResponse:
        """
        Lists GRE tunnels associated with an account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get(
            f"/accounts/{account_id}/magic/gre_tunnels",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[GRETunnelListResponse]._unwrapper),
            cast_to=cast(Type[GRETunnelListResponse], ResultWrapper[GRETunnelListResponse]),
        )

    def delete(self,
    gre_tunnel_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> GRETunnelDeleteResponse:
        """Disables and removes a specific static GRE tunnel.

        Use `?validate_only=true` as
        an optional query parameter to only run validation without persisting changes.

        Args:
          account_id: Identifier

          gre_tunnel_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not gre_tunnel_id:
          raise ValueError(
            f'Expected a non-empty value for `gre_tunnel_id` but received {gre_tunnel_id!r}'
          )
        return self._delete(
            f"/accounts/{account_id}/magic/gre_tunnels/{gre_tunnel_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[GRETunnelDeleteResponse]._unwrapper),
            cast_to=cast(Type[GRETunnelDeleteResponse], ResultWrapper[GRETunnelDeleteResponse]),
        )

    def get(self,
    gre_tunnel_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> GRETunnelGetResponse:
        """
        Lists informtion for a specific GRE tunnel.

        Args:
          account_id: Identifier

          gre_tunnel_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not gre_tunnel_id:
          raise ValueError(
            f'Expected a non-empty value for `gre_tunnel_id` but received {gre_tunnel_id!r}'
          )
        return self._get(
            f"/accounts/{account_id}/magic/gre_tunnels/{gre_tunnel_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[GRETunnelGetResponse]._unwrapper),
            cast_to=cast(Type[GRETunnelGetResponse], ResultWrapper[GRETunnelGetResponse]),
        )

class AsyncGRETunnelsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGRETunnelsResourceWithRawResponse:
        return AsyncGRETunnelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGRETunnelsResourceWithStreamingResponse:
        return AsyncGRETunnelsResourceWithStreamingResponse(self)

    async def create(self,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> GRETunnelCreateResponse:
        """Creates new GRE tunnels.

        Use `?validate_only=true` as an optional query
        parameter to only run validation without persisting changes.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return await self._post(
            f"/accounts/{account_id}/magic/gre_tunnels",
            body=await async_maybe_transform(body, gre_tunnel_create_params.GRETunnelCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[GRETunnelCreateResponse]._unwrapper),
            cast_to=cast(Type[GRETunnelCreateResponse], ResultWrapper[GRETunnelCreateResponse]),
        )

    async def update(self,
    gre_tunnel_id: str,
    *,
    account_id: str,
    cloudflare_gre_endpoint: str,
    customer_gre_endpoint: str,
    interface_address: str,
    name: str,
    description: str | NotGiven = NOT_GIVEN,
    health_check: HealthCheckParam | NotGiven = NOT_GIVEN,
    mtu: int | NotGiven = NOT_GIVEN,
    ttl: int | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> GRETunnelUpdateResponse:
        """Updates a specific GRE tunnel.

        Use `?validate_only=true` as an optional query
        parameter to only run validation without persisting changes.

        Args:
          account_id: Identifier

          gre_tunnel_id: Identifier

          cloudflare_gre_endpoint: The IP address assigned to the Cloudflare side of the GRE tunnel.

          customer_gre_endpoint: The IP address assigned to the customer side of the GRE tunnel.

          interface_address: A 31-bit prefix (/31 in CIDR notation) supporting two hosts, one for each side
              of the tunnel. Select the subnet from the following private IP space:
              10.0.0.0–10.255.255.255, 172.16.0.0–172.31.255.255, 192.168.0.0–192.168.255.255.

          name: The name of the tunnel. The name cannot contain spaces or special characters,
              must be 15 characters or less, and cannot share a name with another GRE tunnel.

          description: An optional description of the GRE tunnel.

          mtu: Maximum Transmission Unit (MTU) in bytes for the GRE tunnel. The minimum value
              is 576.

          ttl: Time To Live (TTL) in number of hops of the GRE tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not gre_tunnel_id:
          raise ValueError(
            f'Expected a non-empty value for `gre_tunnel_id` but received {gre_tunnel_id!r}'
          )
        return await self._put(
            f"/accounts/{account_id}/magic/gre_tunnels/{gre_tunnel_id}",
            body=await async_maybe_transform({
                "cloudflare_gre_endpoint": cloudflare_gre_endpoint,
                "customer_gre_endpoint": customer_gre_endpoint,
                "interface_address": interface_address,
                "name": name,
                "description": description,
                "health_check": health_check,
                "mtu": mtu,
                "ttl": ttl,
            }, gre_tunnel_update_params.GRETunnelUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[GRETunnelUpdateResponse]._unwrapper),
            cast_to=cast(Type[GRETunnelUpdateResponse], ResultWrapper[GRETunnelUpdateResponse]),
        )

    async def list(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> GRETunnelListResponse:
        """
        Lists GRE tunnels associated with an account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return await self._get(
            f"/accounts/{account_id}/magic/gre_tunnels",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[GRETunnelListResponse]._unwrapper),
            cast_to=cast(Type[GRETunnelListResponse], ResultWrapper[GRETunnelListResponse]),
        )

    async def delete(self,
    gre_tunnel_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> GRETunnelDeleteResponse:
        """Disables and removes a specific static GRE tunnel.

        Use `?validate_only=true` as
        an optional query parameter to only run validation without persisting changes.

        Args:
          account_id: Identifier

          gre_tunnel_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not gre_tunnel_id:
          raise ValueError(
            f'Expected a non-empty value for `gre_tunnel_id` but received {gre_tunnel_id!r}'
          )
        return await self._delete(
            f"/accounts/{account_id}/magic/gre_tunnels/{gre_tunnel_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[GRETunnelDeleteResponse]._unwrapper),
            cast_to=cast(Type[GRETunnelDeleteResponse], ResultWrapper[GRETunnelDeleteResponse]),
        )

    async def get(self,
    gre_tunnel_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> GRETunnelGetResponse:
        """
        Lists informtion for a specific GRE tunnel.

        Args:
          account_id: Identifier

          gre_tunnel_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not gre_tunnel_id:
          raise ValueError(
            f'Expected a non-empty value for `gre_tunnel_id` but received {gre_tunnel_id!r}'
          )
        return await self._get(
            f"/accounts/{account_id}/magic/gre_tunnels/{gre_tunnel_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[GRETunnelGetResponse]._unwrapper),
            cast_to=cast(Type[GRETunnelGetResponse], ResultWrapper[GRETunnelGetResponse]),
        )

class GRETunnelsResourceWithRawResponse:
    def __init__(self, gre_tunnels: GRETunnelsResource) -> None:
        self._gre_tunnels = gre_tunnels

        self.create = to_raw_response_wrapper(
            gre_tunnels.create,
        )
        self.update = to_raw_response_wrapper(
            gre_tunnels.update,
        )
        self.list = to_raw_response_wrapper(
            gre_tunnels.list,
        )
        self.delete = to_raw_response_wrapper(
            gre_tunnels.delete,
        )
        self.get = to_raw_response_wrapper(
            gre_tunnels.get,
        )

class AsyncGRETunnelsResourceWithRawResponse:
    def __init__(self, gre_tunnels: AsyncGRETunnelsResource) -> None:
        self._gre_tunnels = gre_tunnels

        self.create = async_to_raw_response_wrapper(
            gre_tunnels.create,
        )
        self.update = async_to_raw_response_wrapper(
            gre_tunnels.update,
        )
        self.list = async_to_raw_response_wrapper(
            gre_tunnels.list,
        )
        self.delete = async_to_raw_response_wrapper(
            gre_tunnels.delete,
        )
        self.get = async_to_raw_response_wrapper(
            gre_tunnels.get,
        )

class GRETunnelsResourceWithStreamingResponse:
    def __init__(self, gre_tunnels: GRETunnelsResource) -> None:
        self._gre_tunnels = gre_tunnels

        self.create = to_streamed_response_wrapper(
            gre_tunnels.create,
        )
        self.update = to_streamed_response_wrapper(
            gre_tunnels.update,
        )
        self.list = to_streamed_response_wrapper(
            gre_tunnels.list,
        )
        self.delete = to_streamed_response_wrapper(
            gre_tunnels.delete,
        )
        self.get = to_streamed_response_wrapper(
            gre_tunnels.get,
        )

class AsyncGRETunnelsResourceWithStreamingResponse:
    def __init__(self, gre_tunnels: AsyncGRETunnelsResource) -> None:
        self._gre_tunnels = gre_tunnels

        self.create = async_to_streamed_response_wrapper(
            gre_tunnels.create,
        )
        self.update = async_to_streamed_response_wrapper(
            gre_tunnels.update,
        )
        self.list = async_to_streamed_response_wrapper(
            gre_tunnels.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            gre_tunnels.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            gre_tunnels.get,
        )