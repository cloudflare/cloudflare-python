# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.magic_transit import (
    IPSECTunnelGetResponse,
    IPSECTunnelListResponse,
    IPSECTunnelCreateResponse,
    IPSECTunnelDeleteResponse,
    IPSECTunnelUpdateResponse,
    IPSECTunnelPSKGenerateResponse,
    ipsec_tunnel_create_params,
    ipsec_tunnel_update_params,
)

__all__ = ["IPSECTunnels", "AsyncIPSECTunnels"]


class IPSECTunnels(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IPSECTunnelsWithRawResponse:
        return IPSECTunnelsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IPSECTunnelsWithStreamingResponse:
        return IPSECTunnelsWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        cloudflare_endpoint: str,
        interface_address: str,
        name: str,
        customer_endpoint: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        health_check: ipsec_tunnel_create_params.HealthCheck | NotGiven = NOT_GIVEN,
        psk: str | NotGiven = NOT_GIVEN,
        replay_protection: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPSECTunnelCreateResponse:
        """Creates new IPsec tunnels associated with an account.

        Use `?validate_only=true`
        as an optional query parameter to only run validation without persisting
        changes.

        Args:
          account_id: Identifier

          cloudflare_endpoint: The IP address assigned to the Cloudflare side of the IPsec tunnel.

          interface_address: A 31-bit prefix (/31 in CIDR notation) supporting two hosts, one for each side
              of the tunnel. Select the subnet from the following private IP space:
              10.0.0.0–10.255.255.255, 172.16.0.0–172.31.255.255, 192.168.0.0–192.168.255.255.

          name: The name of the IPsec tunnel. The name cannot share a name with other tunnels.

          customer_endpoint: The IP address assigned to the customer side of the IPsec tunnel.

          description: An optional description forthe IPsec tunnel.

          psk: A randomly generated or provided string for use in the IPsec tunnel.

          replay_protection: If `true`, then IPsec replay protection will be supported in the
              Cloudflare-to-customer direction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/magic/ipsec_tunnels",
            body=maybe_transform(
                {
                    "cloudflare_endpoint": cloudflare_endpoint,
                    "interface_address": interface_address,
                    "name": name,
                    "customer_endpoint": customer_endpoint,
                    "description": description,
                    "health_check": health_check,
                    "psk": psk,
                    "replay_protection": replay_protection,
                },
                ipsec_tunnel_create_params.IPSECTunnelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IPSECTunnelCreateResponse], ResultWrapper[IPSECTunnelCreateResponse]),
        )

    def update(
        self,
        tunnel_identifier: str,
        *,
        account_id: str,
        cloudflare_endpoint: str,
        interface_address: str,
        name: str,
        customer_endpoint: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        health_check: ipsec_tunnel_update_params.HealthCheck | NotGiven = NOT_GIVEN,
        psk: str | NotGiven = NOT_GIVEN,
        replay_protection: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPSECTunnelUpdateResponse:
        """Updates a specific IPsec tunnel associated with an account.

        Use
        `?validate_only=true` as an optional query parameter to only run validation
        without persisting changes.

        Args:
          account_id: Identifier

          tunnel_identifier: Identifier

          cloudflare_endpoint: The IP address assigned to the Cloudflare side of the IPsec tunnel.

          interface_address: A 31-bit prefix (/31 in CIDR notation) supporting two hosts, one for each side
              of the tunnel. Select the subnet from the following private IP space:
              10.0.0.0–10.255.255.255, 172.16.0.0–172.31.255.255, 192.168.0.0–192.168.255.255.

          name: The name of the IPsec tunnel. The name cannot share a name with other tunnels.

          customer_endpoint: The IP address assigned to the customer side of the IPsec tunnel.

          description: An optional description forthe IPsec tunnel.

          psk: A randomly generated or provided string for use in the IPsec tunnel.

          replay_protection: If `true`, then IPsec replay protection will be supported in the
              Cloudflare-to-customer direction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_identifier:
            raise ValueError(f"Expected a non-empty value for `tunnel_identifier` but received {tunnel_identifier!r}")
        return self._put(
            f"/accounts/{account_id}/magic/ipsec_tunnels/{tunnel_identifier}",
            body=maybe_transform(
                {
                    "cloudflare_endpoint": cloudflare_endpoint,
                    "interface_address": interface_address,
                    "name": name,
                    "customer_endpoint": customer_endpoint,
                    "description": description,
                    "health_check": health_check,
                    "psk": psk,
                    "replay_protection": replay_protection,
                },
                ipsec_tunnel_update_params.IPSECTunnelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IPSECTunnelUpdateResponse], ResultWrapper[IPSECTunnelUpdateResponse]),
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
    ) -> IPSECTunnelListResponse:
        """
        Lists IPsec tunnels associated with an account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/magic/ipsec_tunnels",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IPSECTunnelListResponse], ResultWrapper[IPSECTunnelListResponse]),
        )

    def delete(
        self,
        tunnel_identifier: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPSECTunnelDeleteResponse:
        """
        Disables and removes a specific static IPsec Tunnel associated with an account.
        Use `?validate_only=true` as an optional query parameter to only run validation
        without persisting changes.

        Args:
          account_id: Identifier

          tunnel_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_identifier:
            raise ValueError(f"Expected a non-empty value for `tunnel_identifier` but received {tunnel_identifier!r}")
        return self._delete(
            f"/accounts/{account_id}/magic/ipsec_tunnels/{tunnel_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IPSECTunnelDeleteResponse], ResultWrapper[IPSECTunnelDeleteResponse]),
        )

    def get(
        self,
        tunnel_identifier: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPSECTunnelGetResponse:
        """
        Lists details for a specific IPsec tunnel.

        Args:
          account_id: Identifier

          tunnel_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_identifier:
            raise ValueError(f"Expected a non-empty value for `tunnel_identifier` but received {tunnel_identifier!r}")
        return self._get(
            f"/accounts/{account_id}/magic/ipsec_tunnels/{tunnel_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IPSECTunnelGetResponse], ResultWrapper[IPSECTunnelGetResponse]),
        )

    def psk_generate(
        self,
        tunnel_identifier: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPSECTunnelPSKGenerateResponse:
        """
        Generates a Pre Shared Key for a specific IPsec tunnel used in the IKE session.
        Use `?validate_only=true` as an optional query parameter to only run validation
        without persisting changes. After a PSK is generated, the PSK is immediately
        persisted to Cloudflare's edge and cannot be retrieved later. Note the PSK in a
        safe place.

        Args:
          account_id: Identifier

          tunnel_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_identifier:
            raise ValueError(f"Expected a non-empty value for `tunnel_identifier` but received {tunnel_identifier!r}")
        return self._post(
            f"/accounts/{account_id}/magic/ipsec_tunnels/{tunnel_identifier}/psk_generate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IPSECTunnelPSKGenerateResponse], ResultWrapper[IPSECTunnelPSKGenerateResponse]),
        )


class AsyncIPSECTunnels(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIPSECTunnelsWithRawResponse:
        return AsyncIPSECTunnelsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIPSECTunnelsWithStreamingResponse:
        return AsyncIPSECTunnelsWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        cloudflare_endpoint: str,
        interface_address: str,
        name: str,
        customer_endpoint: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        health_check: ipsec_tunnel_create_params.HealthCheck | NotGiven = NOT_GIVEN,
        psk: str | NotGiven = NOT_GIVEN,
        replay_protection: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPSECTunnelCreateResponse:
        """Creates new IPsec tunnels associated with an account.

        Use `?validate_only=true`
        as an optional query parameter to only run validation without persisting
        changes.

        Args:
          account_id: Identifier

          cloudflare_endpoint: The IP address assigned to the Cloudflare side of the IPsec tunnel.

          interface_address: A 31-bit prefix (/31 in CIDR notation) supporting two hosts, one for each side
              of the tunnel. Select the subnet from the following private IP space:
              10.0.0.0–10.255.255.255, 172.16.0.0–172.31.255.255, 192.168.0.0–192.168.255.255.

          name: The name of the IPsec tunnel. The name cannot share a name with other tunnels.

          customer_endpoint: The IP address assigned to the customer side of the IPsec tunnel.

          description: An optional description forthe IPsec tunnel.

          psk: A randomly generated or provided string for use in the IPsec tunnel.

          replay_protection: If `true`, then IPsec replay protection will be supported in the
              Cloudflare-to-customer direction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/magic/ipsec_tunnels",
            body=await async_maybe_transform(
                {
                    "cloudflare_endpoint": cloudflare_endpoint,
                    "interface_address": interface_address,
                    "name": name,
                    "customer_endpoint": customer_endpoint,
                    "description": description,
                    "health_check": health_check,
                    "psk": psk,
                    "replay_protection": replay_protection,
                },
                ipsec_tunnel_create_params.IPSECTunnelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IPSECTunnelCreateResponse], ResultWrapper[IPSECTunnelCreateResponse]),
        )

    async def update(
        self,
        tunnel_identifier: str,
        *,
        account_id: str,
        cloudflare_endpoint: str,
        interface_address: str,
        name: str,
        customer_endpoint: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        health_check: ipsec_tunnel_update_params.HealthCheck | NotGiven = NOT_GIVEN,
        psk: str | NotGiven = NOT_GIVEN,
        replay_protection: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPSECTunnelUpdateResponse:
        """Updates a specific IPsec tunnel associated with an account.

        Use
        `?validate_only=true` as an optional query parameter to only run validation
        without persisting changes.

        Args:
          account_id: Identifier

          tunnel_identifier: Identifier

          cloudflare_endpoint: The IP address assigned to the Cloudflare side of the IPsec tunnel.

          interface_address: A 31-bit prefix (/31 in CIDR notation) supporting two hosts, one for each side
              of the tunnel. Select the subnet from the following private IP space:
              10.0.0.0–10.255.255.255, 172.16.0.0–172.31.255.255, 192.168.0.0–192.168.255.255.

          name: The name of the IPsec tunnel. The name cannot share a name with other tunnels.

          customer_endpoint: The IP address assigned to the customer side of the IPsec tunnel.

          description: An optional description forthe IPsec tunnel.

          psk: A randomly generated or provided string for use in the IPsec tunnel.

          replay_protection: If `true`, then IPsec replay protection will be supported in the
              Cloudflare-to-customer direction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_identifier:
            raise ValueError(f"Expected a non-empty value for `tunnel_identifier` but received {tunnel_identifier!r}")
        return await self._put(
            f"/accounts/{account_id}/magic/ipsec_tunnels/{tunnel_identifier}",
            body=await async_maybe_transform(
                {
                    "cloudflare_endpoint": cloudflare_endpoint,
                    "interface_address": interface_address,
                    "name": name,
                    "customer_endpoint": customer_endpoint,
                    "description": description,
                    "health_check": health_check,
                    "psk": psk,
                    "replay_protection": replay_protection,
                },
                ipsec_tunnel_update_params.IPSECTunnelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IPSECTunnelUpdateResponse], ResultWrapper[IPSECTunnelUpdateResponse]),
        )

    async def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPSECTunnelListResponse:
        """
        Lists IPsec tunnels associated with an account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/magic/ipsec_tunnels",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IPSECTunnelListResponse], ResultWrapper[IPSECTunnelListResponse]),
        )

    async def delete(
        self,
        tunnel_identifier: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPSECTunnelDeleteResponse:
        """
        Disables and removes a specific static IPsec Tunnel associated with an account.
        Use `?validate_only=true` as an optional query parameter to only run validation
        without persisting changes.

        Args:
          account_id: Identifier

          tunnel_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_identifier:
            raise ValueError(f"Expected a non-empty value for `tunnel_identifier` but received {tunnel_identifier!r}")
        return await self._delete(
            f"/accounts/{account_id}/magic/ipsec_tunnels/{tunnel_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IPSECTunnelDeleteResponse], ResultWrapper[IPSECTunnelDeleteResponse]),
        )

    async def get(
        self,
        tunnel_identifier: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPSECTunnelGetResponse:
        """
        Lists details for a specific IPsec tunnel.

        Args:
          account_id: Identifier

          tunnel_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_identifier:
            raise ValueError(f"Expected a non-empty value for `tunnel_identifier` but received {tunnel_identifier!r}")
        return await self._get(
            f"/accounts/{account_id}/magic/ipsec_tunnels/{tunnel_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IPSECTunnelGetResponse], ResultWrapper[IPSECTunnelGetResponse]),
        )

    async def psk_generate(
        self,
        tunnel_identifier: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPSECTunnelPSKGenerateResponse:
        """
        Generates a Pre Shared Key for a specific IPsec tunnel used in the IKE session.
        Use `?validate_only=true` as an optional query parameter to only run validation
        without persisting changes. After a PSK is generated, the PSK is immediately
        persisted to Cloudflare's edge and cannot be retrieved later. Note the PSK in a
        safe place.

        Args:
          account_id: Identifier

          tunnel_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tunnel_identifier:
            raise ValueError(f"Expected a non-empty value for `tunnel_identifier` but received {tunnel_identifier!r}")
        return await self._post(
            f"/accounts/{account_id}/magic/ipsec_tunnels/{tunnel_identifier}/psk_generate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IPSECTunnelPSKGenerateResponse], ResultWrapper[IPSECTunnelPSKGenerateResponse]),
        )


class IPSECTunnelsWithRawResponse:
    def __init__(self, ipsec_tunnels: IPSECTunnels) -> None:
        self._ipsec_tunnels = ipsec_tunnels

        self.create = to_raw_response_wrapper(
            ipsec_tunnels.create,
        )
        self.update = to_raw_response_wrapper(
            ipsec_tunnels.update,
        )
        self.list = to_raw_response_wrapper(
            ipsec_tunnels.list,
        )
        self.delete = to_raw_response_wrapper(
            ipsec_tunnels.delete,
        )
        self.get = to_raw_response_wrapper(
            ipsec_tunnels.get,
        )
        self.psk_generate = to_raw_response_wrapper(
            ipsec_tunnels.psk_generate,
        )


class AsyncIPSECTunnelsWithRawResponse:
    def __init__(self, ipsec_tunnels: AsyncIPSECTunnels) -> None:
        self._ipsec_tunnels = ipsec_tunnels

        self.create = async_to_raw_response_wrapper(
            ipsec_tunnels.create,
        )
        self.update = async_to_raw_response_wrapper(
            ipsec_tunnels.update,
        )
        self.list = async_to_raw_response_wrapper(
            ipsec_tunnels.list,
        )
        self.delete = async_to_raw_response_wrapper(
            ipsec_tunnels.delete,
        )
        self.get = async_to_raw_response_wrapper(
            ipsec_tunnels.get,
        )
        self.psk_generate = async_to_raw_response_wrapper(
            ipsec_tunnels.psk_generate,
        )


class IPSECTunnelsWithStreamingResponse:
    def __init__(self, ipsec_tunnels: IPSECTunnels) -> None:
        self._ipsec_tunnels = ipsec_tunnels

        self.create = to_streamed_response_wrapper(
            ipsec_tunnels.create,
        )
        self.update = to_streamed_response_wrapper(
            ipsec_tunnels.update,
        )
        self.list = to_streamed_response_wrapper(
            ipsec_tunnels.list,
        )
        self.delete = to_streamed_response_wrapper(
            ipsec_tunnels.delete,
        )
        self.get = to_streamed_response_wrapper(
            ipsec_tunnels.get,
        )
        self.psk_generate = to_streamed_response_wrapper(
            ipsec_tunnels.psk_generate,
        )


class AsyncIPSECTunnelsWithStreamingResponse:
    def __init__(self, ipsec_tunnels: AsyncIPSECTunnels) -> None:
        self._ipsec_tunnels = ipsec_tunnels

        self.create = async_to_streamed_response_wrapper(
            ipsec_tunnels.create,
        )
        self.update = async_to_streamed_response_wrapper(
            ipsec_tunnels.update,
        )
        self.list = async_to_streamed_response_wrapper(
            ipsec_tunnels.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            ipsec_tunnels.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            ipsec_tunnels.get,
        )
        self.psk_generate = async_to_streamed_response_wrapper(
            ipsec_tunnels.psk_generate,
        )
