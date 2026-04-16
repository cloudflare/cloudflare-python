# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from .....types.zero_trust.networks.subnets import warp_edit_params, warp_create_params
from .....types.zero_trust.networks.subnets.subnet import Subnet
from .....types.zero_trust.networks.subnets.warp_delete_response import WARPDeleteResponse

__all__ = ["WARPResource", "AsyncWARPResource"]


class WARPResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WARPResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return WARPResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WARPResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return WARPResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str | None = None,
        name: str,
        network: str,
        comment: str | Omit = omit,
        is_default_network: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Subnet:
        """Create a WARP IP assignment subnet.

        Currently, only IPv4 subnets can be created.

        **Network constraints:**

        - The network must be within one of the following private IP ranges:
          - `10.0.0.0/8` (RFC 1918)
          - `172.16.0.0/12` (RFC 1918)
          - `192.168.0.0/16` (RFC 1918)
          - `100.64.0.0/10` (RFC 6598 - CGNAT)
        - The subnet must have a prefix length of `/24` or larger (e.g., `/16`, `/20`,
          `/24` are valid; `/25`, `/28` are not)

        Args:
          account_id: Cloudflare account ID

          name: A user-friendly name for the subnet.

          network: The private IPv4 or IPv6 range defining the subnet, in CIDR notation.

          comment: An optional description of the subnet.

          is_default_network: If `true`, this is the default subnet for the account. There can only be one
              default subnet per account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/zerotrust/subnets/warp", account_id=account_id),
            body=maybe_transform(
                {
                    "name": name,
                    "network": network,
                    "comment": comment,
                    "is_default_network": is_default_network,
                },
                warp_create_params.WARPCreateParams,
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

    def delete(
        self,
        subnet_id: str,
        *,
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[WARPDeleteResponse]:
        """Delete a WARP IP assignment subnet.

        This operation is idempotent - deleting an
        already-deleted or non-existent subnet will return success with a null result.

        Args:
          account_id: Cloudflare account ID

          subnet_id: The UUID of the subnet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not subnet_id:
            raise ValueError(f"Expected a non-empty value for `subnet_id` but received {subnet_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/zerotrust/subnets/warp/{subnet_id}", account_id=account_id, subnet_id=subnet_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[WARPDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[WARPDeleteResponse]], ResultWrapper[WARPDeleteResponse]),
        )

    def edit(
        self,
        subnet_id: str,
        *,
        account_id: str | None = None,
        comment: str | Omit = omit,
        is_default_network: bool | Omit = omit,
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
        Updates a WARP IP assignment subnet.

        **Update constraints:**

        - The `network` field cannot be modified for WARP subnets. Only `name`,
          `comment`, and `is_default_network` can be updated.
        - IPv6 subnets cannot be updated

        Args:
          account_id: Cloudflare account ID

          subnet_id: The UUID of the subnet.

          comment: An optional description of the subnet.

          is_default_network: If `true`, this is the default subnet for the account. There can only be one
              default subnet per account.

          name: A user-friendly name for the subnet.

          network: The private IPv4 or IPv6 range defining the subnet, in CIDR notation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not subnet_id:
            raise ValueError(f"Expected a non-empty value for `subnet_id` but received {subnet_id!r}")
        return self._patch(
            path_template(
                "/accounts/{account_id}/zerotrust/subnets/warp/{subnet_id}", account_id=account_id, subnet_id=subnet_id
            ),
            body=maybe_transform(
                {
                    "comment": comment,
                    "is_default_network": is_default_network,
                    "name": name,
                    "network": network,
                },
                warp_edit_params.WARPEditParams,
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
        subnet_id: str,
        *,
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Subnet:
        """
        Get a WARP IP assignment subnet.

        Args:
          account_id: Cloudflare account ID

          subnet_id: The UUID of the subnet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not subnet_id:
            raise ValueError(f"Expected a non-empty value for `subnet_id` but received {subnet_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/zerotrust/subnets/warp/{subnet_id}", account_id=account_id, subnet_id=subnet_id
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


class AsyncWARPResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWARPResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWARPResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWARPResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncWARPResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str | None = None,
        name: str,
        network: str,
        comment: str | Omit = omit,
        is_default_network: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Subnet:
        """Create a WARP IP assignment subnet.

        Currently, only IPv4 subnets can be created.

        **Network constraints:**

        - The network must be within one of the following private IP ranges:
          - `10.0.0.0/8` (RFC 1918)
          - `172.16.0.0/12` (RFC 1918)
          - `192.168.0.0/16` (RFC 1918)
          - `100.64.0.0/10` (RFC 6598 - CGNAT)
        - The subnet must have a prefix length of `/24` or larger (e.g., `/16`, `/20`,
          `/24` are valid; `/25`, `/28` are not)

        Args:
          account_id: Cloudflare account ID

          name: A user-friendly name for the subnet.

          network: The private IPv4 or IPv6 range defining the subnet, in CIDR notation.

          comment: An optional description of the subnet.

          is_default_network: If `true`, this is the default subnet for the account. There can only be one
              default subnet per account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/zerotrust/subnets/warp", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "network": network,
                    "comment": comment,
                    "is_default_network": is_default_network,
                },
                warp_create_params.WARPCreateParams,
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

    async def delete(
        self,
        subnet_id: str,
        *,
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[WARPDeleteResponse]:
        """Delete a WARP IP assignment subnet.

        This operation is idempotent - deleting an
        already-deleted or non-existent subnet will return success with a null result.

        Args:
          account_id: Cloudflare account ID

          subnet_id: The UUID of the subnet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not subnet_id:
            raise ValueError(f"Expected a non-empty value for `subnet_id` but received {subnet_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/zerotrust/subnets/warp/{subnet_id}", account_id=account_id, subnet_id=subnet_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[WARPDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[WARPDeleteResponse]], ResultWrapper[WARPDeleteResponse]),
        )

    async def edit(
        self,
        subnet_id: str,
        *,
        account_id: str | None = None,
        comment: str | Omit = omit,
        is_default_network: bool | Omit = omit,
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
        Updates a WARP IP assignment subnet.

        **Update constraints:**

        - The `network` field cannot be modified for WARP subnets. Only `name`,
          `comment`, and `is_default_network` can be updated.
        - IPv6 subnets cannot be updated

        Args:
          account_id: Cloudflare account ID

          subnet_id: The UUID of the subnet.

          comment: An optional description of the subnet.

          is_default_network: If `true`, this is the default subnet for the account. There can only be one
              default subnet per account.

          name: A user-friendly name for the subnet.

          network: The private IPv4 or IPv6 range defining the subnet, in CIDR notation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not subnet_id:
            raise ValueError(f"Expected a non-empty value for `subnet_id` but received {subnet_id!r}")
        return await self._patch(
            path_template(
                "/accounts/{account_id}/zerotrust/subnets/warp/{subnet_id}", account_id=account_id, subnet_id=subnet_id
            ),
            body=await async_maybe_transform(
                {
                    "comment": comment,
                    "is_default_network": is_default_network,
                    "name": name,
                    "network": network,
                },
                warp_edit_params.WARPEditParams,
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
        subnet_id: str,
        *,
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Subnet:
        """
        Get a WARP IP assignment subnet.

        Args:
          account_id: Cloudflare account ID

          subnet_id: The UUID of the subnet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not subnet_id:
            raise ValueError(f"Expected a non-empty value for `subnet_id` but received {subnet_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/zerotrust/subnets/warp/{subnet_id}", account_id=account_id, subnet_id=subnet_id
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


class WARPResourceWithRawResponse:
    def __init__(self, warp: WARPResource) -> None:
        self._warp = warp

        self.create = to_raw_response_wrapper(
            warp.create,
        )
        self.delete = to_raw_response_wrapper(
            warp.delete,
        )
        self.edit = to_raw_response_wrapper(
            warp.edit,
        )
        self.get = to_raw_response_wrapper(
            warp.get,
        )


class AsyncWARPResourceWithRawResponse:
    def __init__(self, warp: AsyncWARPResource) -> None:
        self._warp = warp

        self.create = async_to_raw_response_wrapper(
            warp.create,
        )
        self.delete = async_to_raw_response_wrapper(
            warp.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            warp.edit,
        )
        self.get = async_to_raw_response_wrapper(
            warp.get,
        )


class WARPResourceWithStreamingResponse:
    def __init__(self, warp: WARPResource) -> None:
        self._warp = warp

        self.create = to_streamed_response_wrapper(
            warp.create,
        )
        self.delete = to_streamed_response_wrapper(
            warp.delete,
        )
        self.edit = to_streamed_response_wrapper(
            warp.edit,
        )
        self.get = to_streamed_response_wrapper(
            warp.get,
        )


class AsyncWARPResourceWithStreamingResponse:
    def __init__(self, warp: AsyncWARPResource) -> None:
        self._warp = warp

        self.create = async_to_streamed_response_wrapper(
            warp.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            warp.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            warp.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            warp.get,
        )
