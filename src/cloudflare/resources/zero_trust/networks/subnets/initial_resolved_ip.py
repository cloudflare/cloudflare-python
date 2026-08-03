# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import make_request_options
from .....types.zero_trust.networks.subnets import initial_resolved_ip_update_params
from .....types.zero_trust.networks.subnets.subnet import Subnet

__all__ = ["InitialResolvedIPResource", "AsyncInitialResolvedIPResource"]


class InitialResolvedIPResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InitialResolvedIPResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return InitialResolvedIPResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InitialResolvedIPResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return InitialResolvedIPResourceWithStreamingResponse(self)

    def update(
        self,
        address_family: Literal["v4", "v6"],
        *,
        account_id: str,
        comment: str | Omit = omit,
        name: str | Omit = omit,
        network: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Subnet:
        """
        Updates the CIDR for the account's default gateway ephemeral subnet of the given
        address family. The new CIDR must not conflict with existing private routes in
        the account.

        Args:
          account_id: Cloudflare account ID

          address_family: IP address family, either `v4` (IPv4) or `v6` (IPv6)

          comment: An optional description of the subnet.

          name: A user-friendly name for the subnet.

          network: The private IPv4 or IPv6 range defining the subnet, in CIDR notation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not address_family:
            raise ValueError(f"Expected a non-empty value for `address_family` but received {address_family!r}")
        return self._put(
            path_template(
                "/accounts/{account_id}/zerotrust/subnets/initial_resolved_ip/{address_family}",
                account_id=account_id,
                address_family=address_family,
            ),
            body=maybe_transform(
                {
                    "comment": comment,
                    "name": name,
                    "network": network,
                },
                initial_resolved_ip_update_params.InitialResolvedIPUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Subnet]._unwrapper,
            ),
            cast_to=cast(Type[Subnet], ResultWrapper[Subnet]),
        )

    def get(
        self,
        address_family: Literal["v4", "v6"],
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Subnet:
        """
        Returns the account's default gateway ephemeral subnet for the given address
        family.

        Args:
          account_id: Cloudflare account ID

          address_family: IP address family, either `v4` (IPv4) or `v6` (IPv6)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not address_family:
            raise ValueError(f"Expected a non-empty value for `address_family` but received {address_family!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/zerotrust/subnets/initial_resolved_ip/{address_family}",
                account_id=account_id,
                address_family=address_family,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Subnet]._unwrapper,
            ),
            cast_to=cast(Type[Subnet], ResultWrapper[Subnet]),
        )


class AsyncInitialResolvedIPResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInitialResolvedIPResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInitialResolvedIPResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInitialResolvedIPResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncInitialResolvedIPResourceWithStreamingResponse(self)

    async def update(
        self,
        address_family: Literal["v4", "v6"],
        *,
        account_id: str,
        comment: str | Omit = omit,
        name: str | Omit = omit,
        network: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Subnet:
        """
        Updates the CIDR for the account's default gateway ephemeral subnet of the given
        address family. The new CIDR must not conflict with existing private routes in
        the account.

        Args:
          account_id: Cloudflare account ID

          address_family: IP address family, either `v4` (IPv4) or `v6` (IPv6)

          comment: An optional description of the subnet.

          name: A user-friendly name for the subnet.

          network: The private IPv4 or IPv6 range defining the subnet, in CIDR notation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not address_family:
            raise ValueError(f"Expected a non-empty value for `address_family` but received {address_family!r}")
        return await self._put(
            path_template(
                "/accounts/{account_id}/zerotrust/subnets/initial_resolved_ip/{address_family}",
                account_id=account_id,
                address_family=address_family,
            ),
            body=await async_maybe_transform(
                {
                    "comment": comment,
                    "name": name,
                    "network": network,
                },
                initial_resolved_ip_update_params.InitialResolvedIPUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Subnet]._unwrapper,
            ),
            cast_to=cast(Type[Subnet], ResultWrapper[Subnet]),
        )

    async def get(
        self,
        address_family: Literal["v4", "v6"],
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Subnet:
        """
        Returns the account's default gateway ephemeral subnet for the given address
        family.

        Args:
          account_id: Cloudflare account ID

          address_family: IP address family, either `v4` (IPv4) or `v6` (IPv6)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not address_family:
            raise ValueError(f"Expected a non-empty value for `address_family` but received {address_family!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/zerotrust/subnets/initial_resolved_ip/{address_family}",
                account_id=account_id,
                address_family=address_family,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Subnet]._unwrapper,
            ),
            cast_to=cast(Type[Subnet], ResultWrapper[Subnet]),
        )


class InitialResolvedIPResourceWithRawResponse:
    def __init__(self, initial_resolved_ip: InitialResolvedIPResource) -> None:
        self._initial_resolved_ip = initial_resolved_ip

        self.update = to_raw_response_wrapper(
            initial_resolved_ip.update,
        )
        self.get = to_raw_response_wrapper(
            initial_resolved_ip.get,
        )


class AsyncInitialResolvedIPResourceWithRawResponse:
    def __init__(self, initial_resolved_ip: AsyncInitialResolvedIPResource) -> None:
        self._initial_resolved_ip = initial_resolved_ip

        self.update = async_to_raw_response_wrapper(
            initial_resolved_ip.update,
        )
        self.get = async_to_raw_response_wrapper(
            initial_resolved_ip.get,
        )


class InitialResolvedIPResourceWithStreamingResponse:
    def __init__(self, initial_resolved_ip: InitialResolvedIPResource) -> None:
        self._initial_resolved_ip = initial_resolved_ip

        self.update = to_streamed_response_wrapper(
            initial_resolved_ip.update,
        )
        self.get = to_streamed_response_wrapper(
            initial_resolved_ip.get,
        )


class AsyncInitialResolvedIPResourceWithStreamingResponse:
    def __init__(self, initial_resolved_ip: AsyncInitialResolvedIPResource) -> None:
        self._initial_resolved_ip = initial_resolved_ip

        self.update = async_to_streamed_response_wrapper(
            initial_resolved_ip.update,
        )
        self.get = async_to_streamed_response_wrapper(
            initial_resolved_ip.get,
        )
