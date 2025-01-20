# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    is_given,
    maybe_transform,
    strip_not_given,
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
from ..._base_client import make_request_options
from ...types.magic_transit import (
    ipsec_tunnel_create_params,
    ipsec_tunnel_update_params,
    ipsec_tunnel_bulk_update_params,
    ipsec_tunnel_psk_generate_params,
)
from ...types.magic_transit.ipsec_tunnel_get_response import IPSECTunnelGetResponse
from ...types.magic_transit.ipsec_tunnel_list_response import IPSECTunnelListResponse
from ...types.magic_transit.ipsec_tunnel_create_response import IPSECTunnelCreateResponse
from ...types.magic_transit.ipsec_tunnel_delete_response import IPSECTunnelDeleteResponse
from ...types.magic_transit.ipsec_tunnel_update_response import IPSECTunnelUpdateResponse
from ...types.magic_transit.ipsec_tunnel_bulk_update_response import IPSECTunnelBulkUpdateResponse
from ...types.magic_transit.ipsec_tunnel_psk_generate_response import IPSECTunnelPSKGenerateResponse

__all__ = ["IPSECTunnelsResource", "AsyncIPSECTunnelsResource"]


class IPSECTunnelsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IPSECTunnelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return IPSECTunnelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IPSECTunnelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return IPSECTunnelsResourceWithStreamingResponse(self)

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
        x_magic_new_hc_target: bool | NotGiven = NOT_GIVEN,
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

          customer_endpoint: The IP address assigned to the customer side of the IPsec tunnel. Not required,
              but must be set for proactive traceroutes to work.

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
        extra_headers = {
            **strip_not_given(
                {
                    "x-magic-new-hc-target": ("true" if x_magic_new_hc_target else "false")
                    if is_given(x_magic_new_hc_target)
                    else NOT_GIVEN
                }
            ),
            **(extra_headers or {}),
        }
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
                post_parser=ResultWrapper[IPSECTunnelCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[IPSECTunnelCreateResponse], ResultWrapper[IPSECTunnelCreateResponse]),
        )

    def update(
        self,
        ipsec_tunnel_id: str,
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
        x_magic_new_hc_target: bool | NotGiven = NOT_GIVEN,
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

          ipsec_tunnel_id: Identifier

          cloudflare_endpoint: The IP address assigned to the Cloudflare side of the IPsec tunnel.

          interface_address: A 31-bit prefix (/31 in CIDR notation) supporting two hosts, one for each side
              of the tunnel. Select the subnet from the following private IP space:
              10.0.0.0–10.255.255.255, 172.16.0.0–172.31.255.255, 192.168.0.0–192.168.255.255.

          name: The name of the IPsec tunnel. The name cannot share a name with other tunnels.

          customer_endpoint: The IP address assigned to the customer side of the IPsec tunnel. Not required,
              but must be set for proactive traceroutes to work.

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
        if not ipsec_tunnel_id:
            raise ValueError(f"Expected a non-empty value for `ipsec_tunnel_id` but received {ipsec_tunnel_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "x-magic-new-hc-target": ("true" if x_magic_new_hc_target else "false")
                    if is_given(x_magic_new_hc_target)
                    else NOT_GIVEN
                }
            ),
            **(extra_headers or {}),
        }
        return self._put(
            f"/accounts/{account_id}/magic/ipsec_tunnels/{ipsec_tunnel_id}",
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
                post_parser=ResultWrapper[IPSECTunnelUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[IPSECTunnelUpdateResponse], ResultWrapper[IPSECTunnelUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        x_magic_new_hc_target: bool | NotGiven = NOT_GIVEN,
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
        extra_headers = {
            **strip_not_given(
                {
                    "x-magic-new-hc-target": ("true" if x_magic_new_hc_target else "false")
                    if is_given(x_magic_new_hc_target)
                    else NOT_GIVEN
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            f"/accounts/{account_id}/magic/ipsec_tunnels",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[IPSECTunnelListResponse]._unwrapper,
            ),
            cast_to=cast(Type[IPSECTunnelListResponse], ResultWrapper[IPSECTunnelListResponse]),
        )

    def delete(
        self,
        ipsec_tunnel_id: str,
        *,
        account_id: str,
        x_magic_new_hc_target: bool | NotGiven = NOT_GIVEN,
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

          ipsec_tunnel_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not ipsec_tunnel_id:
            raise ValueError(f"Expected a non-empty value for `ipsec_tunnel_id` but received {ipsec_tunnel_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "x-magic-new-hc-target": ("true" if x_magic_new_hc_target else "false")
                    if is_given(x_magic_new_hc_target)
                    else NOT_GIVEN
                }
            ),
            **(extra_headers or {}),
        }
        return self._delete(
            f"/accounts/{account_id}/magic/ipsec_tunnels/{ipsec_tunnel_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[IPSECTunnelDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[IPSECTunnelDeleteResponse], ResultWrapper[IPSECTunnelDeleteResponse]),
        )

    def bulk_update(
        self,
        *,
        account_id: str,
        body: object,
        x_magic_new_hc_target: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPSECTunnelBulkUpdateResponse:
        """Update multiple IPsec tunnels associated with an account.

        Use
        `?validate_only=true` as an optional query parameter to only run validation
        without persisting changes.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "x-magic-new-hc-target": ("true" if x_magic_new_hc_target else "false")
                    if is_given(x_magic_new_hc_target)
                    else NOT_GIVEN
                }
            ),
            **(extra_headers or {}),
        }
        return self._put(
            f"/accounts/{account_id}/magic/ipsec_tunnels",
            body=maybe_transform(body, ipsec_tunnel_bulk_update_params.IPSECTunnelBulkUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[IPSECTunnelBulkUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[IPSECTunnelBulkUpdateResponse], ResultWrapper[IPSECTunnelBulkUpdateResponse]),
        )

    def get(
        self,
        ipsec_tunnel_id: str,
        *,
        account_id: str,
        x_magic_new_hc_target: bool | NotGiven = NOT_GIVEN,
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

          ipsec_tunnel_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not ipsec_tunnel_id:
            raise ValueError(f"Expected a non-empty value for `ipsec_tunnel_id` but received {ipsec_tunnel_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "x-magic-new-hc-target": ("true" if x_magic_new_hc_target else "false")
                    if is_given(x_magic_new_hc_target)
                    else NOT_GIVEN
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            f"/accounts/{account_id}/magic/ipsec_tunnels/{ipsec_tunnel_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[IPSECTunnelGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[IPSECTunnelGetResponse], ResultWrapper[IPSECTunnelGetResponse]),
        )

    def psk_generate(
        self,
        ipsec_tunnel_id: str,
        *,
        account_id: str,
        body: object,
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

          ipsec_tunnel_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not ipsec_tunnel_id:
            raise ValueError(f"Expected a non-empty value for `ipsec_tunnel_id` but received {ipsec_tunnel_id!r}")
        return self._post(
            f"/accounts/{account_id}/magic/ipsec_tunnels/{ipsec_tunnel_id}/psk_generate",
            body=maybe_transform(body, ipsec_tunnel_psk_generate_params.IPSECTunnelPSKGenerateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[IPSECTunnelPSKGenerateResponse]._unwrapper,
            ),
            cast_to=cast(Type[IPSECTunnelPSKGenerateResponse], ResultWrapper[IPSECTunnelPSKGenerateResponse]),
        )


class AsyncIPSECTunnelsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIPSECTunnelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIPSECTunnelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIPSECTunnelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncIPSECTunnelsResourceWithStreamingResponse(self)

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
        x_magic_new_hc_target: bool | NotGiven = NOT_GIVEN,
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

          customer_endpoint: The IP address assigned to the customer side of the IPsec tunnel. Not required,
              but must be set for proactive traceroutes to work.

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
        extra_headers = {
            **strip_not_given(
                {
                    "x-magic-new-hc-target": ("true" if x_magic_new_hc_target else "false")
                    if is_given(x_magic_new_hc_target)
                    else NOT_GIVEN
                }
            ),
            **(extra_headers or {}),
        }
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
                post_parser=ResultWrapper[IPSECTunnelCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[IPSECTunnelCreateResponse], ResultWrapper[IPSECTunnelCreateResponse]),
        )

    async def update(
        self,
        ipsec_tunnel_id: str,
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
        x_magic_new_hc_target: bool | NotGiven = NOT_GIVEN,
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

          ipsec_tunnel_id: Identifier

          cloudflare_endpoint: The IP address assigned to the Cloudflare side of the IPsec tunnel.

          interface_address: A 31-bit prefix (/31 in CIDR notation) supporting two hosts, one for each side
              of the tunnel. Select the subnet from the following private IP space:
              10.0.0.0–10.255.255.255, 172.16.0.0–172.31.255.255, 192.168.0.0–192.168.255.255.

          name: The name of the IPsec tunnel. The name cannot share a name with other tunnels.

          customer_endpoint: The IP address assigned to the customer side of the IPsec tunnel. Not required,
              but must be set for proactive traceroutes to work.

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
        if not ipsec_tunnel_id:
            raise ValueError(f"Expected a non-empty value for `ipsec_tunnel_id` but received {ipsec_tunnel_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "x-magic-new-hc-target": ("true" if x_magic_new_hc_target else "false")
                    if is_given(x_magic_new_hc_target)
                    else NOT_GIVEN
                }
            ),
            **(extra_headers or {}),
        }
        return await self._put(
            f"/accounts/{account_id}/magic/ipsec_tunnels/{ipsec_tunnel_id}",
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
                post_parser=ResultWrapper[IPSECTunnelUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[IPSECTunnelUpdateResponse], ResultWrapper[IPSECTunnelUpdateResponse]),
        )

    async def list(
        self,
        *,
        account_id: str,
        x_magic_new_hc_target: bool | NotGiven = NOT_GIVEN,
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
        extra_headers = {
            **strip_not_given(
                {
                    "x-magic-new-hc-target": ("true" if x_magic_new_hc_target else "false")
                    if is_given(x_magic_new_hc_target)
                    else NOT_GIVEN
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            f"/accounts/{account_id}/magic/ipsec_tunnels",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[IPSECTunnelListResponse]._unwrapper,
            ),
            cast_to=cast(Type[IPSECTunnelListResponse], ResultWrapper[IPSECTunnelListResponse]),
        )

    async def delete(
        self,
        ipsec_tunnel_id: str,
        *,
        account_id: str,
        x_magic_new_hc_target: bool | NotGiven = NOT_GIVEN,
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

          ipsec_tunnel_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not ipsec_tunnel_id:
            raise ValueError(f"Expected a non-empty value for `ipsec_tunnel_id` but received {ipsec_tunnel_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "x-magic-new-hc-target": ("true" if x_magic_new_hc_target else "false")
                    if is_given(x_magic_new_hc_target)
                    else NOT_GIVEN
                }
            ),
            **(extra_headers or {}),
        }
        return await self._delete(
            f"/accounts/{account_id}/magic/ipsec_tunnels/{ipsec_tunnel_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[IPSECTunnelDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[IPSECTunnelDeleteResponse], ResultWrapper[IPSECTunnelDeleteResponse]),
        )

    async def bulk_update(
        self,
        *,
        account_id: str,
        body: object,
        x_magic_new_hc_target: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPSECTunnelBulkUpdateResponse:
        """Update multiple IPsec tunnels associated with an account.

        Use
        `?validate_only=true` as an optional query parameter to only run validation
        without persisting changes.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "x-magic-new-hc-target": ("true" if x_magic_new_hc_target else "false")
                    if is_given(x_magic_new_hc_target)
                    else NOT_GIVEN
                }
            ),
            **(extra_headers or {}),
        }
        return await self._put(
            f"/accounts/{account_id}/magic/ipsec_tunnels",
            body=await async_maybe_transform(body, ipsec_tunnel_bulk_update_params.IPSECTunnelBulkUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[IPSECTunnelBulkUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[IPSECTunnelBulkUpdateResponse], ResultWrapper[IPSECTunnelBulkUpdateResponse]),
        )

    async def get(
        self,
        ipsec_tunnel_id: str,
        *,
        account_id: str,
        x_magic_new_hc_target: bool | NotGiven = NOT_GIVEN,
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

          ipsec_tunnel_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not ipsec_tunnel_id:
            raise ValueError(f"Expected a non-empty value for `ipsec_tunnel_id` but received {ipsec_tunnel_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "x-magic-new-hc-target": ("true" if x_magic_new_hc_target else "false")
                    if is_given(x_magic_new_hc_target)
                    else NOT_GIVEN
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            f"/accounts/{account_id}/magic/ipsec_tunnels/{ipsec_tunnel_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[IPSECTunnelGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[IPSECTunnelGetResponse], ResultWrapper[IPSECTunnelGetResponse]),
        )

    async def psk_generate(
        self,
        ipsec_tunnel_id: str,
        *,
        account_id: str,
        body: object,
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

          ipsec_tunnel_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not ipsec_tunnel_id:
            raise ValueError(f"Expected a non-empty value for `ipsec_tunnel_id` but received {ipsec_tunnel_id!r}")
        return await self._post(
            f"/accounts/{account_id}/magic/ipsec_tunnels/{ipsec_tunnel_id}/psk_generate",
            body=await async_maybe_transform(body, ipsec_tunnel_psk_generate_params.IPSECTunnelPSKGenerateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[IPSECTunnelPSKGenerateResponse]._unwrapper,
            ),
            cast_to=cast(Type[IPSECTunnelPSKGenerateResponse], ResultWrapper[IPSECTunnelPSKGenerateResponse]),
        )


class IPSECTunnelsResourceWithRawResponse:
    def __init__(self, ipsec_tunnels: IPSECTunnelsResource) -> None:
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
        self.bulk_update = to_raw_response_wrapper(
            ipsec_tunnels.bulk_update,
        )
        self.get = to_raw_response_wrapper(
            ipsec_tunnels.get,
        )
        self.psk_generate = to_raw_response_wrapper(
            ipsec_tunnels.psk_generate,
        )


class AsyncIPSECTunnelsResourceWithRawResponse:
    def __init__(self, ipsec_tunnels: AsyncIPSECTunnelsResource) -> None:
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
        self.bulk_update = async_to_raw_response_wrapper(
            ipsec_tunnels.bulk_update,
        )
        self.get = async_to_raw_response_wrapper(
            ipsec_tunnels.get,
        )
        self.psk_generate = async_to_raw_response_wrapper(
            ipsec_tunnels.psk_generate,
        )


class IPSECTunnelsResourceWithStreamingResponse:
    def __init__(self, ipsec_tunnels: IPSECTunnelsResource) -> None:
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
        self.bulk_update = to_streamed_response_wrapper(
            ipsec_tunnels.bulk_update,
        )
        self.get = to_streamed_response_wrapper(
            ipsec_tunnels.get,
        )
        self.psk_generate = to_streamed_response_wrapper(
            ipsec_tunnels.psk_generate,
        )


class AsyncIPSECTunnelsResourceWithStreamingResponse:
    def __init__(self, ipsec_tunnels: AsyncIPSECTunnelsResource) -> None:
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
        self.bulk_update = async_to_streamed_response_wrapper(
            ipsec_tunnels.bulk_update,
        )
        self.get = async_to_streamed_response_wrapper(
            ipsec_tunnels.get,
        )
        self.psk_generate = async_to_streamed_response_wrapper(
            ipsec_tunnels.psk_generate,
        )
