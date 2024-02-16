# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .psk_generates import PskGenerates, AsyncPskGenerates

from ...._compat import cached_property

from ....types.magics import (
    IpsecTunnelUpdateResponse,
    IpsecTunnelDeleteResponse,
    IpsecTunnelGetResponse,
    IpsecTunnelMagicIPsecTunnelsCreateIPsecTunnelsResponse,
    IpsecTunnelMagicIPsecTunnelsListIPsecTunnelsResponse,
    IpsecTunnelMagicIPsecTunnelsUpdateMultipleIPsecTunnelsResponse,
)

from typing import Type

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ....types.magics import ipsec_tunnel_update_params
from ....types.magics import ipsec_tunnel_magic_i_psec_tunnels_create_i_psec_tunnels_params
from ....types.magics import ipsec_tunnel_magic_i_psec_tunnels_update_multiple_i_psec_tunnels_params
from .psk_generates import (
    PskGenerates,
    AsyncPskGenerates,
    PskGeneratesWithRawResponse,
    AsyncPskGeneratesWithRawResponse,
    PskGeneratesWithStreamingResponse,
    AsyncPskGeneratesWithStreamingResponse,
)
from ...._wrappers import ResultWrapper
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

__all__ = ["IpsecTunnels", "AsyncIpsecTunnels"]


class IpsecTunnels(SyncAPIResource):
    @cached_property
    def psk_generates(self) -> PskGenerates:
        return PskGenerates(self._client)

    @cached_property
    def with_raw_response(self) -> IpsecTunnelsWithRawResponse:
        return IpsecTunnelsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IpsecTunnelsWithStreamingResponse:
        return IpsecTunnelsWithStreamingResponse(self)

    def update(
        self,
        tunnel_identifier: str,
        *,
        account_identifier: str,
        cloudflare_endpoint: str,
        interface_address: str,
        name: str,
        customer_endpoint: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        psk: str | NotGiven = NOT_GIVEN,
        replay_protection: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IpsecTunnelUpdateResponse:
        """Updates a specific IPsec tunnel associated with an account.

        Use
        `?validate_only=true` as an optional query parameter to only run validation
        without persisting changes.

        Args:
          account_identifier: Identifier

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
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not tunnel_identifier:
            raise ValueError(f"Expected a non-empty value for `tunnel_identifier` but received {tunnel_identifier!r}")
        return self._put(
            f"/accounts/{account_identifier}/magic/ipsec_tunnels/{tunnel_identifier}",
            body=maybe_transform(
                {
                    "cloudflare_endpoint": cloudflare_endpoint,
                    "interface_address": interface_address,
                    "name": name,
                    "customer_endpoint": customer_endpoint,
                    "description": description,
                    "psk": psk,
                    "replay_protection": replay_protection,
                },
                ipsec_tunnel_update_params.IpsecTunnelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IpsecTunnelUpdateResponse], ResultWrapper[IpsecTunnelUpdateResponse]),
        )

    def delete(
        self,
        tunnel_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IpsecTunnelDeleteResponse:
        """
        Disables and removes a specific static IPsec Tunnel associated with an account.
        Use `?validate_only=true` as an optional query parameter to only run validation
        without persisting changes.

        Args:
          account_identifier: Identifier

          tunnel_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not tunnel_identifier:
            raise ValueError(f"Expected a non-empty value for `tunnel_identifier` but received {tunnel_identifier!r}")
        return self._delete(
            f"/accounts/{account_identifier}/magic/ipsec_tunnels/{tunnel_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IpsecTunnelDeleteResponse], ResultWrapper[IpsecTunnelDeleteResponse]),
        )

    def get(
        self,
        tunnel_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IpsecTunnelGetResponse:
        """
        Lists details for a specific IPsec tunnel.

        Args:
          account_identifier: Identifier

          tunnel_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not tunnel_identifier:
            raise ValueError(f"Expected a non-empty value for `tunnel_identifier` but received {tunnel_identifier!r}")
        return self._get(
            f"/accounts/{account_identifier}/magic/ipsec_tunnels/{tunnel_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IpsecTunnelGetResponse], ResultWrapper[IpsecTunnelGetResponse]),
        )

    def magic_i_psec_tunnels_create_i_psec_tunnels(
        self,
        account_identifier: str,
        *,
        cloudflare_endpoint: str,
        interface_address: str,
        name: str,
        customer_endpoint: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        psk: str | NotGiven = NOT_GIVEN,
        replay_protection: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IpsecTunnelMagicIPsecTunnelsCreateIPsecTunnelsResponse:
        """Creates new IPsec tunnels associated with an account.

        Use `?validate_only=true`
        as an optional query parameter to only run validation without persisting
        changes.

        Args:
          account_identifier: Identifier

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
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._post(
            f"/accounts/{account_identifier}/magic/ipsec_tunnels",
            body=maybe_transform(
                {
                    "cloudflare_endpoint": cloudflare_endpoint,
                    "interface_address": interface_address,
                    "name": name,
                    "customer_endpoint": customer_endpoint,
                    "description": description,
                    "psk": psk,
                    "replay_protection": replay_protection,
                },
                ipsec_tunnel_magic_i_psec_tunnels_create_i_psec_tunnels_params.IpsecTunnelMagicIPsecTunnelsCreateIPsecTunnelsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[IpsecTunnelMagicIPsecTunnelsCreateIPsecTunnelsResponse],
                ResultWrapper[IpsecTunnelMagicIPsecTunnelsCreateIPsecTunnelsResponse],
            ),
        )

    def magic_i_psec_tunnels_list_i_psec_tunnels(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IpsecTunnelMagicIPsecTunnelsListIPsecTunnelsResponse:
        """
        Lists IPsec tunnels associated with an account.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._get(
            f"/accounts/{account_identifier}/magic/ipsec_tunnels",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[IpsecTunnelMagicIPsecTunnelsListIPsecTunnelsResponse],
                ResultWrapper[IpsecTunnelMagicIPsecTunnelsListIPsecTunnelsResponse],
            ),
        )

    def magic_i_psec_tunnels_update_multiple_i_psec_tunnels(
        self,
        account_identifier: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IpsecTunnelMagicIPsecTunnelsUpdateMultipleIPsecTunnelsResponse:
        """Update multiple IPsec tunnels associated with an account.

        Use
        `?validate_only=true` as an optional query parameter to only run validation
        without persisting changes.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._put(
            f"/accounts/{account_identifier}/magic/ipsec_tunnels",
            body=maybe_transform(
                body,
                ipsec_tunnel_magic_i_psec_tunnels_update_multiple_i_psec_tunnels_params.IpsecTunnelMagicIPsecTunnelsUpdateMultipleIPsecTunnelsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[IpsecTunnelMagicIPsecTunnelsUpdateMultipleIPsecTunnelsResponse],
                ResultWrapper[IpsecTunnelMagicIPsecTunnelsUpdateMultipleIPsecTunnelsResponse],
            ),
        )


class AsyncIpsecTunnels(AsyncAPIResource):
    @cached_property
    def psk_generates(self) -> AsyncPskGenerates:
        return AsyncPskGenerates(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIpsecTunnelsWithRawResponse:
        return AsyncIpsecTunnelsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIpsecTunnelsWithStreamingResponse:
        return AsyncIpsecTunnelsWithStreamingResponse(self)

    async def update(
        self,
        tunnel_identifier: str,
        *,
        account_identifier: str,
        cloudflare_endpoint: str,
        interface_address: str,
        name: str,
        customer_endpoint: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        psk: str | NotGiven = NOT_GIVEN,
        replay_protection: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IpsecTunnelUpdateResponse:
        """Updates a specific IPsec tunnel associated with an account.

        Use
        `?validate_only=true` as an optional query parameter to only run validation
        without persisting changes.

        Args:
          account_identifier: Identifier

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
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not tunnel_identifier:
            raise ValueError(f"Expected a non-empty value for `tunnel_identifier` but received {tunnel_identifier!r}")
        return await self._put(
            f"/accounts/{account_identifier}/magic/ipsec_tunnels/{tunnel_identifier}",
            body=maybe_transform(
                {
                    "cloudflare_endpoint": cloudflare_endpoint,
                    "interface_address": interface_address,
                    "name": name,
                    "customer_endpoint": customer_endpoint,
                    "description": description,
                    "psk": psk,
                    "replay_protection": replay_protection,
                },
                ipsec_tunnel_update_params.IpsecTunnelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IpsecTunnelUpdateResponse], ResultWrapper[IpsecTunnelUpdateResponse]),
        )

    async def delete(
        self,
        tunnel_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IpsecTunnelDeleteResponse:
        """
        Disables and removes a specific static IPsec Tunnel associated with an account.
        Use `?validate_only=true` as an optional query parameter to only run validation
        without persisting changes.

        Args:
          account_identifier: Identifier

          tunnel_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not tunnel_identifier:
            raise ValueError(f"Expected a non-empty value for `tunnel_identifier` but received {tunnel_identifier!r}")
        return await self._delete(
            f"/accounts/{account_identifier}/magic/ipsec_tunnels/{tunnel_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IpsecTunnelDeleteResponse], ResultWrapper[IpsecTunnelDeleteResponse]),
        )

    async def get(
        self,
        tunnel_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IpsecTunnelGetResponse:
        """
        Lists details for a specific IPsec tunnel.

        Args:
          account_identifier: Identifier

          tunnel_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not tunnel_identifier:
            raise ValueError(f"Expected a non-empty value for `tunnel_identifier` but received {tunnel_identifier!r}")
        return await self._get(
            f"/accounts/{account_identifier}/magic/ipsec_tunnels/{tunnel_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IpsecTunnelGetResponse], ResultWrapper[IpsecTunnelGetResponse]),
        )

    async def magic_i_psec_tunnels_create_i_psec_tunnels(
        self,
        account_identifier: str,
        *,
        cloudflare_endpoint: str,
        interface_address: str,
        name: str,
        customer_endpoint: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        psk: str | NotGiven = NOT_GIVEN,
        replay_protection: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IpsecTunnelMagicIPsecTunnelsCreateIPsecTunnelsResponse:
        """Creates new IPsec tunnels associated with an account.

        Use `?validate_only=true`
        as an optional query parameter to only run validation without persisting
        changes.

        Args:
          account_identifier: Identifier

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
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._post(
            f"/accounts/{account_identifier}/magic/ipsec_tunnels",
            body=maybe_transform(
                {
                    "cloudflare_endpoint": cloudflare_endpoint,
                    "interface_address": interface_address,
                    "name": name,
                    "customer_endpoint": customer_endpoint,
                    "description": description,
                    "psk": psk,
                    "replay_protection": replay_protection,
                },
                ipsec_tunnel_magic_i_psec_tunnels_create_i_psec_tunnels_params.IpsecTunnelMagicIPsecTunnelsCreateIPsecTunnelsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[IpsecTunnelMagicIPsecTunnelsCreateIPsecTunnelsResponse],
                ResultWrapper[IpsecTunnelMagicIPsecTunnelsCreateIPsecTunnelsResponse],
            ),
        )

    async def magic_i_psec_tunnels_list_i_psec_tunnels(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IpsecTunnelMagicIPsecTunnelsListIPsecTunnelsResponse:
        """
        Lists IPsec tunnels associated with an account.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._get(
            f"/accounts/{account_identifier}/magic/ipsec_tunnels",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[IpsecTunnelMagicIPsecTunnelsListIPsecTunnelsResponse],
                ResultWrapper[IpsecTunnelMagicIPsecTunnelsListIPsecTunnelsResponse],
            ),
        )

    async def magic_i_psec_tunnels_update_multiple_i_psec_tunnels(
        self,
        account_identifier: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IpsecTunnelMagicIPsecTunnelsUpdateMultipleIPsecTunnelsResponse:
        """Update multiple IPsec tunnels associated with an account.

        Use
        `?validate_only=true` as an optional query parameter to only run validation
        without persisting changes.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._put(
            f"/accounts/{account_identifier}/magic/ipsec_tunnels",
            body=maybe_transform(
                body,
                ipsec_tunnel_magic_i_psec_tunnels_update_multiple_i_psec_tunnels_params.IpsecTunnelMagicIPsecTunnelsUpdateMultipleIPsecTunnelsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[IpsecTunnelMagicIPsecTunnelsUpdateMultipleIPsecTunnelsResponse],
                ResultWrapper[IpsecTunnelMagicIPsecTunnelsUpdateMultipleIPsecTunnelsResponse],
            ),
        )


class IpsecTunnelsWithRawResponse:
    def __init__(self, ipsec_tunnels: IpsecTunnels) -> None:
        self._ipsec_tunnels = ipsec_tunnels

        self.update = to_raw_response_wrapper(
            ipsec_tunnels.update,
        )
        self.delete = to_raw_response_wrapper(
            ipsec_tunnels.delete,
        )
        self.get = to_raw_response_wrapper(
            ipsec_tunnels.get,
        )
        self.magic_i_psec_tunnels_create_i_psec_tunnels = to_raw_response_wrapper(
            ipsec_tunnels.magic_i_psec_tunnels_create_i_psec_tunnels,
        )
        self.magic_i_psec_tunnels_list_i_psec_tunnels = to_raw_response_wrapper(
            ipsec_tunnels.magic_i_psec_tunnels_list_i_psec_tunnels,
        )
        self.magic_i_psec_tunnels_update_multiple_i_psec_tunnels = to_raw_response_wrapper(
            ipsec_tunnels.magic_i_psec_tunnels_update_multiple_i_psec_tunnels,
        )

    @cached_property
    def psk_generates(self) -> PskGeneratesWithRawResponse:
        return PskGeneratesWithRawResponse(self._ipsec_tunnels.psk_generates)


class AsyncIpsecTunnelsWithRawResponse:
    def __init__(self, ipsec_tunnels: AsyncIpsecTunnels) -> None:
        self._ipsec_tunnels = ipsec_tunnels

        self.update = async_to_raw_response_wrapper(
            ipsec_tunnels.update,
        )
        self.delete = async_to_raw_response_wrapper(
            ipsec_tunnels.delete,
        )
        self.get = async_to_raw_response_wrapper(
            ipsec_tunnels.get,
        )
        self.magic_i_psec_tunnels_create_i_psec_tunnels = async_to_raw_response_wrapper(
            ipsec_tunnels.magic_i_psec_tunnels_create_i_psec_tunnels,
        )
        self.magic_i_psec_tunnels_list_i_psec_tunnels = async_to_raw_response_wrapper(
            ipsec_tunnels.magic_i_psec_tunnels_list_i_psec_tunnels,
        )
        self.magic_i_psec_tunnels_update_multiple_i_psec_tunnels = async_to_raw_response_wrapper(
            ipsec_tunnels.magic_i_psec_tunnels_update_multiple_i_psec_tunnels,
        )

    @cached_property
    def psk_generates(self) -> AsyncPskGeneratesWithRawResponse:
        return AsyncPskGeneratesWithRawResponse(self._ipsec_tunnels.psk_generates)


class IpsecTunnelsWithStreamingResponse:
    def __init__(self, ipsec_tunnels: IpsecTunnels) -> None:
        self._ipsec_tunnels = ipsec_tunnels

        self.update = to_streamed_response_wrapper(
            ipsec_tunnels.update,
        )
        self.delete = to_streamed_response_wrapper(
            ipsec_tunnels.delete,
        )
        self.get = to_streamed_response_wrapper(
            ipsec_tunnels.get,
        )
        self.magic_i_psec_tunnels_create_i_psec_tunnels = to_streamed_response_wrapper(
            ipsec_tunnels.magic_i_psec_tunnels_create_i_psec_tunnels,
        )
        self.magic_i_psec_tunnels_list_i_psec_tunnels = to_streamed_response_wrapper(
            ipsec_tunnels.magic_i_psec_tunnels_list_i_psec_tunnels,
        )
        self.magic_i_psec_tunnels_update_multiple_i_psec_tunnels = to_streamed_response_wrapper(
            ipsec_tunnels.magic_i_psec_tunnels_update_multiple_i_psec_tunnels,
        )

    @cached_property
    def psk_generates(self) -> PskGeneratesWithStreamingResponse:
        return PskGeneratesWithStreamingResponse(self._ipsec_tunnels.psk_generates)


class AsyncIpsecTunnelsWithStreamingResponse:
    def __init__(self, ipsec_tunnels: AsyncIpsecTunnels) -> None:
        self._ipsec_tunnels = ipsec_tunnels

        self.update = async_to_streamed_response_wrapper(
            ipsec_tunnels.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            ipsec_tunnels.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            ipsec_tunnels.get,
        )
        self.magic_i_psec_tunnels_create_i_psec_tunnels = async_to_streamed_response_wrapper(
            ipsec_tunnels.magic_i_psec_tunnels_create_i_psec_tunnels,
        )
        self.magic_i_psec_tunnels_list_i_psec_tunnels = async_to_streamed_response_wrapper(
            ipsec_tunnels.magic_i_psec_tunnels_list_i_psec_tunnels,
        )
        self.magic_i_psec_tunnels_update_multiple_i_psec_tunnels = async_to_streamed_response_wrapper(
            ipsec_tunnels.magic_i_psec_tunnels_update_multiple_i_psec_tunnels,
        )

    @cached_property
    def psk_generates(self) -> AsyncPskGeneratesWithStreamingResponse:
        return AsyncPskGeneratesWithStreamingResponse(self._ipsec_tunnels.psk_generates)
