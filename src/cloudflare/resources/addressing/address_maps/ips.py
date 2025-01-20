# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...._base_client import make_request_options
from ....types.addressing.address_maps import ip_update_params
from ....types.addressing.address_maps.ip_delete_response import IPDeleteResponse
from ....types.addressing.address_maps.ip_update_response import IPUpdateResponse

__all__ = ["IPsResource", "AsyncIPsResource"]


class IPsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IPsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return IPsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IPsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return IPsResourceWithStreamingResponse(self)

    def update(
        self,
        ip_address: str,
        *,
        account_id: str,
        address_map_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPUpdateResponse:
        """
        Add an IP from a prefix owned by the account to a particular address map.

        Args:
          account_id: Identifier of a Cloudflare account.

          address_map_id: Identifier of an Address Map.

          ip_address: An IPv4 or IPv6 address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not address_map_id:
            raise ValueError(f"Expected a non-empty value for `address_map_id` but received {address_map_id!r}")
        if not ip_address:
            raise ValueError(f"Expected a non-empty value for `ip_address` but received {ip_address!r}")
        return self._put(
            f"/accounts/{account_id}/addressing/address_maps/{address_map_id}/ips/{ip_address}",
            body=maybe_transform(body, ip_update_params.IPUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPUpdateResponse,
        )

    def delete(
        self,
        ip_address: str,
        *,
        account_id: str,
        address_map_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPDeleteResponse:
        """
        Remove an IP from a particular address map.

        Args:
          account_id: Identifier of a Cloudflare account.

          address_map_id: Identifier of an Address Map.

          ip_address: An IPv4 or IPv6 address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not address_map_id:
            raise ValueError(f"Expected a non-empty value for `address_map_id` but received {address_map_id!r}")
        if not ip_address:
            raise ValueError(f"Expected a non-empty value for `ip_address` but received {ip_address!r}")
        return self._delete(
            f"/accounts/{account_id}/addressing/address_maps/{address_map_id}/ips/{ip_address}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPDeleteResponse,
        )


class AsyncIPsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIPsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIPsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIPsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncIPsResourceWithStreamingResponse(self)

    async def update(
        self,
        ip_address: str,
        *,
        account_id: str,
        address_map_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPUpdateResponse:
        """
        Add an IP from a prefix owned by the account to a particular address map.

        Args:
          account_id: Identifier of a Cloudflare account.

          address_map_id: Identifier of an Address Map.

          ip_address: An IPv4 or IPv6 address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not address_map_id:
            raise ValueError(f"Expected a non-empty value for `address_map_id` but received {address_map_id!r}")
        if not ip_address:
            raise ValueError(f"Expected a non-empty value for `ip_address` but received {ip_address!r}")
        return await self._put(
            f"/accounts/{account_id}/addressing/address_maps/{address_map_id}/ips/{ip_address}",
            body=await async_maybe_transform(body, ip_update_params.IPUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPUpdateResponse,
        )

    async def delete(
        self,
        ip_address: str,
        *,
        account_id: str,
        address_map_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPDeleteResponse:
        """
        Remove an IP from a particular address map.

        Args:
          account_id: Identifier of a Cloudflare account.

          address_map_id: Identifier of an Address Map.

          ip_address: An IPv4 or IPv6 address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not address_map_id:
            raise ValueError(f"Expected a non-empty value for `address_map_id` but received {address_map_id!r}")
        if not ip_address:
            raise ValueError(f"Expected a non-empty value for `ip_address` but received {ip_address!r}")
        return await self._delete(
            f"/accounts/{account_id}/addressing/address_maps/{address_map_id}/ips/{ip_address}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPDeleteResponse,
        )


class IPsResourceWithRawResponse:
    def __init__(self, ips: IPsResource) -> None:
        self._ips = ips

        self.update = to_raw_response_wrapper(
            ips.update,
        )
        self.delete = to_raw_response_wrapper(
            ips.delete,
        )


class AsyncIPsResourceWithRawResponse:
    def __init__(self, ips: AsyncIPsResource) -> None:
        self._ips = ips

        self.update = async_to_raw_response_wrapper(
            ips.update,
        )
        self.delete = async_to_raw_response_wrapper(
            ips.delete,
        )


class IPsResourceWithStreamingResponse:
    def __init__(self, ips: IPsResource) -> None:
        self._ips = ips

        self.update = to_streamed_response_wrapper(
            ips.update,
        )
        self.delete = to_streamed_response_wrapper(
            ips.delete,
        )


class AsyncIPsResourceWithStreamingResponse:
    def __init__(self, ips: AsyncIPsResource) -> None:
        self._ips = ips

        self.update = async_to_streamed_response_wrapper(
            ips.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            ips.delete,
        )
