# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Iterable, Optional, cast

import httpx

from .ips import (
    IPsResource,
    AsyncIPsResource,
    IPsResourceWithRawResponse,
    AsyncIPsResourceWithRawResponse,
    IPsResourceWithStreamingResponse,
    AsyncIPsResourceWithStreamingResponse,
)
from .zones import (
    ZonesResource,
    AsyncZonesResource,
    ZonesResourceWithRawResponse,
    AsyncZonesResourceWithRawResponse,
    ZonesResourceWithStreamingResponse,
    AsyncZonesResourceWithStreamingResponse,
)
from .accounts import (
    AccountsResource,
    AsyncAccountsResource,
    AccountsResourceWithRawResponse,
    AsyncAccountsResourceWithRawResponse,
    AccountsResourceWithStreamingResponse,
    AsyncAccountsResourceWithStreamingResponse,
)
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
from ....types.addressing import address_map_edit_params, address_map_create_params
from ....types.addressing.address_map import AddressMap
from ....types.addressing.address_map_get_response import AddressMapGetResponse
from ....types.addressing.address_map_create_response import AddressMapCreateResponse
from ....types.addressing.address_map_delete_response import AddressMapDeleteResponse

__all__ = ["AddressMapsResource", "AsyncAddressMapsResource"]


class AddressMapsResource(SyncAPIResource):
    @cached_property
    def accounts(self) -> AccountsResource:
        return AccountsResource(self._client)

    @cached_property
    def ips(self) -> IPsResource:
        return IPsResource(self._client)

    @cached_property
    def zones(self) -> ZonesResource:
        return ZonesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AddressMapsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AddressMapsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AddressMapsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AddressMapsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        enabled: Optional[bool] | NotGiven = NOT_GIVEN,
        ips: List[str] | NotGiven = NOT_GIVEN,
        memberships: Iterable[address_map_create_params.Membership] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AddressMapCreateResponse]:
        """
        Create a new address map under the account.

        Args:
          account_id: Identifier of a Cloudflare account.

          description: An optional description field which may be used to describe the types of IPs or
              zones on the map.

          enabled: Whether the Address Map is enabled or not. Cloudflare's DNS will not respond
              with IP addresses on an Address Map until the map is enabled.

          memberships: Zones and Accounts which will be assigned IPs on this Address Map. A zone
              membership will take priority over an account membership.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/addressing/address_maps",
            body=maybe_transform(
                {
                    "description": description,
                    "enabled": enabled,
                    "ips": ips,
                    "memberships": memberships,
                },
                address_map_create_params.AddressMapCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AddressMapCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AddressMapCreateResponse]], ResultWrapper[AddressMapCreateResponse]),
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
    ) -> SyncSinglePage[AddressMap]:
        """
        List all address maps owned by the account.

        Args:
          account_id: Identifier of a Cloudflare account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/addressing/address_maps",
            page=SyncSinglePage[AddressMap],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=AddressMap,
        )

    def delete(
        self,
        address_map_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressMapDeleteResponse:
        """Delete a particular address map owned by the account.

        An Address Map must be
        disabled before it can be deleted.

        Args:
          account_id: Identifier of a Cloudflare account.

          address_map_id: Identifier of an Address Map.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not address_map_id:
            raise ValueError(f"Expected a non-empty value for `address_map_id` but received {address_map_id!r}")
        return self._delete(
            f"/accounts/{account_id}/addressing/address_maps/{address_map_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressMapDeleteResponse,
        )

    def edit(
        self,
        address_map_id: str,
        *,
        account_id: str,
        default_sni: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        enabled: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AddressMap]:
        """
        Modify properties of an address map owned by the account.

        Args:
          account_id: Identifier of a Cloudflare account.

          address_map_id: Identifier of an Address Map.

          default_sni: If you have legacy TLS clients which do not send the TLS server name indicator,
              then you can specify one default SNI on the map. If Cloudflare receives a TLS
              handshake from a client without an SNI, it will respond with the default SNI on
              those IPs. The default SNI can be any valid zone or subdomain owned by the
              account.

          description: An optional description field which may be used to describe the types of IPs or
              zones on the map.

          enabled: Whether the Address Map is enabled or not. Cloudflare's DNS will not respond
              with IP addresses on an Address Map until the map is enabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not address_map_id:
            raise ValueError(f"Expected a non-empty value for `address_map_id` but received {address_map_id!r}")
        return self._patch(
            f"/accounts/{account_id}/addressing/address_maps/{address_map_id}",
            body=maybe_transform(
                {
                    "default_sni": default_sni,
                    "description": description,
                    "enabled": enabled,
                },
                address_map_edit_params.AddressMapEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AddressMap]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AddressMap]], ResultWrapper[AddressMap]),
        )

    def get(
        self,
        address_map_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AddressMapGetResponse]:
        """
        Show a particular address map owned by the account.

        Args:
          account_id: Identifier of a Cloudflare account.

          address_map_id: Identifier of an Address Map.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not address_map_id:
            raise ValueError(f"Expected a non-empty value for `address_map_id` but received {address_map_id!r}")
        return self._get(
            f"/accounts/{account_id}/addressing/address_maps/{address_map_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AddressMapGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AddressMapGetResponse]], ResultWrapper[AddressMapGetResponse]),
        )


class AsyncAddressMapsResource(AsyncAPIResource):
    @cached_property
    def accounts(self) -> AsyncAccountsResource:
        return AsyncAccountsResource(self._client)

    @cached_property
    def ips(self) -> AsyncIPsResource:
        return AsyncIPsResource(self._client)

    @cached_property
    def zones(self) -> AsyncZonesResource:
        return AsyncZonesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAddressMapsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAddressMapsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAddressMapsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAddressMapsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        enabled: Optional[bool] | NotGiven = NOT_GIVEN,
        ips: List[str] | NotGiven = NOT_GIVEN,
        memberships: Iterable[address_map_create_params.Membership] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AddressMapCreateResponse]:
        """
        Create a new address map under the account.

        Args:
          account_id: Identifier of a Cloudflare account.

          description: An optional description field which may be used to describe the types of IPs or
              zones on the map.

          enabled: Whether the Address Map is enabled or not. Cloudflare's DNS will not respond
              with IP addresses on an Address Map until the map is enabled.

          memberships: Zones and Accounts which will be assigned IPs on this Address Map. A zone
              membership will take priority over an account membership.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/addressing/address_maps",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "enabled": enabled,
                    "ips": ips,
                    "memberships": memberships,
                },
                address_map_create_params.AddressMapCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AddressMapCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AddressMapCreateResponse]], ResultWrapper[AddressMapCreateResponse]),
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
    ) -> AsyncPaginator[AddressMap, AsyncSinglePage[AddressMap]]:
        """
        List all address maps owned by the account.

        Args:
          account_id: Identifier of a Cloudflare account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/addressing/address_maps",
            page=AsyncSinglePage[AddressMap],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=AddressMap,
        )

    async def delete(
        self,
        address_map_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressMapDeleteResponse:
        """Delete a particular address map owned by the account.

        An Address Map must be
        disabled before it can be deleted.

        Args:
          account_id: Identifier of a Cloudflare account.

          address_map_id: Identifier of an Address Map.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not address_map_id:
            raise ValueError(f"Expected a non-empty value for `address_map_id` but received {address_map_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/addressing/address_maps/{address_map_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressMapDeleteResponse,
        )

    async def edit(
        self,
        address_map_id: str,
        *,
        account_id: str,
        default_sni: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        enabled: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AddressMap]:
        """
        Modify properties of an address map owned by the account.

        Args:
          account_id: Identifier of a Cloudflare account.

          address_map_id: Identifier of an Address Map.

          default_sni: If you have legacy TLS clients which do not send the TLS server name indicator,
              then you can specify one default SNI on the map. If Cloudflare receives a TLS
              handshake from a client without an SNI, it will respond with the default SNI on
              those IPs. The default SNI can be any valid zone or subdomain owned by the
              account.

          description: An optional description field which may be used to describe the types of IPs or
              zones on the map.

          enabled: Whether the Address Map is enabled or not. Cloudflare's DNS will not respond
              with IP addresses on an Address Map until the map is enabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not address_map_id:
            raise ValueError(f"Expected a non-empty value for `address_map_id` but received {address_map_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/addressing/address_maps/{address_map_id}",
            body=await async_maybe_transform(
                {
                    "default_sni": default_sni,
                    "description": description,
                    "enabled": enabled,
                },
                address_map_edit_params.AddressMapEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AddressMap]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AddressMap]], ResultWrapper[AddressMap]),
        )

    async def get(
        self,
        address_map_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AddressMapGetResponse]:
        """
        Show a particular address map owned by the account.

        Args:
          account_id: Identifier of a Cloudflare account.

          address_map_id: Identifier of an Address Map.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not address_map_id:
            raise ValueError(f"Expected a non-empty value for `address_map_id` but received {address_map_id!r}")
        return await self._get(
            f"/accounts/{account_id}/addressing/address_maps/{address_map_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AddressMapGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AddressMapGetResponse]], ResultWrapper[AddressMapGetResponse]),
        )


class AddressMapsResourceWithRawResponse:
    def __init__(self, address_maps: AddressMapsResource) -> None:
        self._address_maps = address_maps

        self.create = to_raw_response_wrapper(
            address_maps.create,
        )
        self.list = to_raw_response_wrapper(
            address_maps.list,
        )
        self.delete = to_raw_response_wrapper(
            address_maps.delete,
        )
        self.edit = to_raw_response_wrapper(
            address_maps.edit,
        )
        self.get = to_raw_response_wrapper(
            address_maps.get,
        )

    @cached_property
    def accounts(self) -> AccountsResourceWithRawResponse:
        return AccountsResourceWithRawResponse(self._address_maps.accounts)

    @cached_property
    def ips(self) -> IPsResourceWithRawResponse:
        return IPsResourceWithRawResponse(self._address_maps.ips)

    @cached_property
    def zones(self) -> ZonesResourceWithRawResponse:
        return ZonesResourceWithRawResponse(self._address_maps.zones)


class AsyncAddressMapsResourceWithRawResponse:
    def __init__(self, address_maps: AsyncAddressMapsResource) -> None:
        self._address_maps = address_maps

        self.create = async_to_raw_response_wrapper(
            address_maps.create,
        )
        self.list = async_to_raw_response_wrapper(
            address_maps.list,
        )
        self.delete = async_to_raw_response_wrapper(
            address_maps.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            address_maps.edit,
        )
        self.get = async_to_raw_response_wrapper(
            address_maps.get,
        )

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithRawResponse:
        return AsyncAccountsResourceWithRawResponse(self._address_maps.accounts)

    @cached_property
    def ips(self) -> AsyncIPsResourceWithRawResponse:
        return AsyncIPsResourceWithRawResponse(self._address_maps.ips)

    @cached_property
    def zones(self) -> AsyncZonesResourceWithRawResponse:
        return AsyncZonesResourceWithRawResponse(self._address_maps.zones)


class AddressMapsResourceWithStreamingResponse:
    def __init__(self, address_maps: AddressMapsResource) -> None:
        self._address_maps = address_maps

        self.create = to_streamed_response_wrapper(
            address_maps.create,
        )
        self.list = to_streamed_response_wrapper(
            address_maps.list,
        )
        self.delete = to_streamed_response_wrapper(
            address_maps.delete,
        )
        self.edit = to_streamed_response_wrapper(
            address_maps.edit,
        )
        self.get = to_streamed_response_wrapper(
            address_maps.get,
        )

    @cached_property
    def accounts(self) -> AccountsResourceWithStreamingResponse:
        return AccountsResourceWithStreamingResponse(self._address_maps.accounts)

    @cached_property
    def ips(self) -> IPsResourceWithStreamingResponse:
        return IPsResourceWithStreamingResponse(self._address_maps.ips)

    @cached_property
    def zones(self) -> ZonesResourceWithStreamingResponse:
        return ZonesResourceWithStreamingResponse(self._address_maps.zones)


class AsyncAddressMapsResourceWithStreamingResponse:
    def __init__(self, address_maps: AsyncAddressMapsResource) -> None:
        self._address_maps = address_maps

        self.create = async_to_streamed_response_wrapper(
            address_maps.create,
        )
        self.list = async_to_streamed_response_wrapper(
            address_maps.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            address_maps.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            address_maps.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            address_maps.get,
        )

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithStreamingResponse:
        return AsyncAccountsResourceWithStreamingResponse(self._address_maps.accounts)

    @cached_property
    def ips(self) -> AsyncIPsResourceWithStreamingResponse:
        return AsyncIPsResourceWithStreamingResponse(self._address_maps.ips)

    @cached_property
    def zones(self) -> AsyncZonesResourceWithStreamingResponse:
        return AsyncZonesResourceWithStreamingResponse(self._address_maps.zones)
