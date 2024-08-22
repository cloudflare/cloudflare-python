# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.magic_transit.sites.lan_create_response import LANCreateResponse

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from ...._base_client import make_request_options, AsyncPaginator

from typing import Type, Iterable

from ....types.magic_transit.sites.nat_param import NatParam

from ....types.magic_transit.sites.routed_subnet_param import RoutedSubnetParam

from ....types.magic_transit.sites.lan_static_addressing_param import LANStaticAddressingParam

from ....types.magic_transit.sites.lan import LAN

from ....pagination import SyncSinglePage, AsyncSinglePage

from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.magic_transit.sites import lan_create_params
from ....types.magic_transit.sites import lan_update_params
from ....types.magic_transit.sites import lan_edit_params
from ....types.magic_transit.sites import Nat
from ....types.magic_transit.sites import LANStaticAddressing
from ....types.magic_transit.sites import Nat
from ....types.magic_transit.sites import LANStaticAddressing
from ....types.magic_transit.sites import Nat
from ....types.magic_transit.sites import LANStaticAddressing
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

__all__ = ["LANsResource", "AsyncLANsResource"]

class LANsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LANsResourceWithRawResponse:
        return LANsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LANsResourceWithStreamingResponse:
        return LANsResourceWithStreamingResponse(self)

    def create(self,
    site_id: str,
    *,
    account_id: str,
    physport: int,
    vlan_tag: int,
    ha_link: bool | NotGiven = NOT_GIVEN,
    name: str | NotGiven = NOT_GIVEN,
    nat: NatParam | NotGiven = NOT_GIVEN,
    routed_subnets: Iterable[RoutedSubnetParam] | NotGiven = NOT_GIVEN,
    static_addressing: LANStaticAddressingParam | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> LANCreateResponse:
        """Creates a new Site LAN.

        If the site is in high availability mode,
        static_addressing is required along with secondary and virtual address.

        Args:
          account_id: Identifier

          site_id: Identifier

          vlan_tag: VLAN port number.

          ha_link: mark true to use this LAN for HA probing. only works for site with HA turned on.
              only one LAN can be set as the ha_link.

          static_addressing: If the site is not configured in high availability mode, this configuration is
              optional (if omitted, use DHCP). However, if in high availability mode,
              static_address is required along with secondary and virtual address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not site_id:
          raise ValueError(
            f'Expected a non-empty value for `site_id` but received {site_id!r}'
          )
        return self._post(
            f"/accounts/{account_id}/magic/sites/{site_id}/lans",
            body=maybe_transform({
                "physport": physport,
                "vlan_tag": vlan_tag,
                "ha_link": ha_link,
                "name": name,
                "nat": nat,
                "routed_subnets": routed_subnets,
                "static_addressing": static_addressing,
            }, lan_create_params.LANCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[LANCreateResponse]._unwrapper),
            cast_to=cast(Type[LANCreateResponse], ResultWrapper[LANCreateResponse]),
        )

    def update(self,
    lan_id: str,
    *,
    account_id: str,
    site_id: str,
    name: str | NotGiven = NOT_GIVEN,
    nat: NatParam | NotGiven = NOT_GIVEN,
    physport: int | NotGiven = NOT_GIVEN,
    routed_subnets: Iterable[RoutedSubnetParam] | NotGiven = NOT_GIVEN,
    static_addressing: LANStaticAddressingParam | NotGiven = NOT_GIVEN,
    vlan_tag: int | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> LAN:
        """
        Update a specific Site LAN.

        Args:
          account_id: Identifier

          site_id: Identifier

          lan_id: Identifier

          static_addressing: If the site is not configured in high availability mode, this configuration is
              optional (if omitted, use DHCP). However, if in high availability mode,
              static_address is required along with secondary and virtual address.

          vlan_tag: VLAN port number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not site_id:
          raise ValueError(
            f'Expected a non-empty value for `site_id` but received {site_id!r}'
          )
        if not lan_id:
          raise ValueError(
            f'Expected a non-empty value for `lan_id` but received {lan_id!r}'
          )
        return self._put(
            f"/accounts/{account_id}/magic/sites/{site_id}/lans/{lan_id}",
            body=maybe_transform({
                "name": name,
                "nat": nat,
                "physport": physport,
                "routed_subnets": routed_subnets,
                "static_addressing": static_addressing,
                "vlan_tag": vlan_tag,
            }, lan_update_params.LANUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[LAN]._unwrapper),
            cast_to=cast(Type[LAN], ResultWrapper[LAN]),
        )

    def list(self,
    site_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> SyncSinglePage[LAN]:
        """
        Lists Site LANs associated with an account.

        Args:
          account_id: Identifier

          site_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not site_id:
          raise ValueError(
            f'Expected a non-empty value for `site_id` but received {site_id!r}'
          )
        return self._get_api_list(
            f"/accounts/{account_id}/magic/sites/{site_id}/lans",
            page = SyncSinglePage[LAN],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            model=LAN,
        )

    def delete(self,
    lan_id: str,
    *,
    account_id: str,
    site_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> LAN:
        """
        Remove a specific Site LAN.

        Args:
          account_id: Identifier

          site_id: Identifier

          lan_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not site_id:
          raise ValueError(
            f'Expected a non-empty value for `site_id` but received {site_id!r}'
          )
        if not lan_id:
          raise ValueError(
            f'Expected a non-empty value for `lan_id` but received {lan_id!r}'
          )
        return self._delete(
            f"/accounts/{account_id}/magic/sites/{site_id}/lans/{lan_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[LAN]._unwrapper),
            cast_to=cast(Type[LAN], ResultWrapper[LAN]),
        )

    def edit(self,
    lan_id: str,
    *,
    account_id: str,
    site_id: str,
    name: str | NotGiven = NOT_GIVEN,
    nat: NatParam | NotGiven = NOT_GIVEN,
    physport: int | NotGiven = NOT_GIVEN,
    routed_subnets: Iterable[RoutedSubnetParam] | NotGiven = NOT_GIVEN,
    static_addressing: LANStaticAddressingParam | NotGiven = NOT_GIVEN,
    vlan_tag: int | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> LAN:
        """
        Patch a specific Site LAN.

        Args:
          account_id: Identifier

          site_id: Identifier

          lan_id: Identifier

          static_addressing: If the site is not configured in high availability mode, this configuration is
              optional (if omitted, use DHCP). However, if in high availability mode,
              static_address is required along with secondary and virtual address.

          vlan_tag: VLAN port number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not site_id:
          raise ValueError(
            f'Expected a non-empty value for `site_id` but received {site_id!r}'
          )
        if not lan_id:
          raise ValueError(
            f'Expected a non-empty value for `lan_id` but received {lan_id!r}'
          )
        return self._patch(
            f"/accounts/{account_id}/magic/sites/{site_id}/lans/{lan_id}",
            body=maybe_transform({
                "name": name,
                "nat": nat,
                "physport": physport,
                "routed_subnets": routed_subnets,
                "static_addressing": static_addressing,
                "vlan_tag": vlan_tag,
            }, lan_edit_params.LANEditParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[LAN]._unwrapper),
            cast_to=cast(Type[LAN], ResultWrapper[LAN]),
        )

    def get(self,
    lan_id: str,
    *,
    account_id: str,
    site_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> LAN:
        """
        Get a specific Site LAN.

        Args:
          account_id: Identifier

          site_id: Identifier

          lan_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not site_id:
          raise ValueError(
            f'Expected a non-empty value for `site_id` but received {site_id!r}'
          )
        if not lan_id:
          raise ValueError(
            f'Expected a non-empty value for `lan_id` but received {lan_id!r}'
          )
        return self._get(
            f"/accounts/{account_id}/magic/sites/{site_id}/lans/{lan_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[LAN]._unwrapper),
            cast_to=cast(Type[LAN], ResultWrapper[LAN]),
        )

class AsyncLANsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLANsResourceWithRawResponse:
        return AsyncLANsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLANsResourceWithStreamingResponse:
        return AsyncLANsResourceWithStreamingResponse(self)

    async def create(self,
    site_id: str,
    *,
    account_id: str,
    physport: int,
    vlan_tag: int,
    ha_link: bool | NotGiven = NOT_GIVEN,
    name: str | NotGiven = NOT_GIVEN,
    nat: NatParam | NotGiven = NOT_GIVEN,
    routed_subnets: Iterable[RoutedSubnetParam] | NotGiven = NOT_GIVEN,
    static_addressing: LANStaticAddressingParam | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> LANCreateResponse:
        """Creates a new Site LAN.

        If the site is in high availability mode,
        static_addressing is required along with secondary and virtual address.

        Args:
          account_id: Identifier

          site_id: Identifier

          vlan_tag: VLAN port number.

          ha_link: mark true to use this LAN for HA probing. only works for site with HA turned on.
              only one LAN can be set as the ha_link.

          static_addressing: If the site is not configured in high availability mode, this configuration is
              optional (if omitted, use DHCP). However, if in high availability mode,
              static_address is required along with secondary and virtual address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not site_id:
          raise ValueError(
            f'Expected a non-empty value for `site_id` but received {site_id!r}'
          )
        return await self._post(
            f"/accounts/{account_id}/magic/sites/{site_id}/lans",
            body=await async_maybe_transform({
                "physport": physport,
                "vlan_tag": vlan_tag,
                "ha_link": ha_link,
                "name": name,
                "nat": nat,
                "routed_subnets": routed_subnets,
                "static_addressing": static_addressing,
            }, lan_create_params.LANCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[LANCreateResponse]._unwrapper),
            cast_to=cast(Type[LANCreateResponse], ResultWrapper[LANCreateResponse]),
        )

    async def update(self,
    lan_id: str,
    *,
    account_id: str,
    site_id: str,
    name: str | NotGiven = NOT_GIVEN,
    nat: NatParam | NotGiven = NOT_GIVEN,
    physport: int | NotGiven = NOT_GIVEN,
    routed_subnets: Iterable[RoutedSubnetParam] | NotGiven = NOT_GIVEN,
    static_addressing: LANStaticAddressingParam | NotGiven = NOT_GIVEN,
    vlan_tag: int | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> LAN:
        """
        Update a specific Site LAN.

        Args:
          account_id: Identifier

          site_id: Identifier

          lan_id: Identifier

          static_addressing: If the site is not configured in high availability mode, this configuration is
              optional (if omitted, use DHCP). However, if in high availability mode,
              static_address is required along with secondary and virtual address.

          vlan_tag: VLAN port number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not site_id:
          raise ValueError(
            f'Expected a non-empty value for `site_id` but received {site_id!r}'
          )
        if not lan_id:
          raise ValueError(
            f'Expected a non-empty value for `lan_id` but received {lan_id!r}'
          )
        return await self._put(
            f"/accounts/{account_id}/magic/sites/{site_id}/lans/{lan_id}",
            body=await async_maybe_transform({
                "name": name,
                "nat": nat,
                "physport": physport,
                "routed_subnets": routed_subnets,
                "static_addressing": static_addressing,
                "vlan_tag": vlan_tag,
            }, lan_update_params.LANUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[LAN]._unwrapper),
            cast_to=cast(Type[LAN], ResultWrapper[LAN]),
        )

    def list(self,
    site_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AsyncPaginator[LAN, AsyncSinglePage[LAN]]:
        """
        Lists Site LANs associated with an account.

        Args:
          account_id: Identifier

          site_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not site_id:
          raise ValueError(
            f'Expected a non-empty value for `site_id` but received {site_id!r}'
          )
        return self._get_api_list(
            f"/accounts/{account_id}/magic/sites/{site_id}/lans",
            page = AsyncSinglePage[LAN],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            model=LAN,
        )

    async def delete(self,
    lan_id: str,
    *,
    account_id: str,
    site_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> LAN:
        """
        Remove a specific Site LAN.

        Args:
          account_id: Identifier

          site_id: Identifier

          lan_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not site_id:
          raise ValueError(
            f'Expected a non-empty value for `site_id` but received {site_id!r}'
          )
        if not lan_id:
          raise ValueError(
            f'Expected a non-empty value for `lan_id` but received {lan_id!r}'
          )
        return await self._delete(
            f"/accounts/{account_id}/magic/sites/{site_id}/lans/{lan_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[LAN]._unwrapper),
            cast_to=cast(Type[LAN], ResultWrapper[LAN]),
        )

    async def edit(self,
    lan_id: str,
    *,
    account_id: str,
    site_id: str,
    name: str | NotGiven = NOT_GIVEN,
    nat: NatParam | NotGiven = NOT_GIVEN,
    physport: int | NotGiven = NOT_GIVEN,
    routed_subnets: Iterable[RoutedSubnetParam] | NotGiven = NOT_GIVEN,
    static_addressing: LANStaticAddressingParam | NotGiven = NOT_GIVEN,
    vlan_tag: int | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> LAN:
        """
        Patch a specific Site LAN.

        Args:
          account_id: Identifier

          site_id: Identifier

          lan_id: Identifier

          static_addressing: If the site is not configured in high availability mode, this configuration is
              optional (if omitted, use DHCP). However, if in high availability mode,
              static_address is required along with secondary and virtual address.

          vlan_tag: VLAN port number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not site_id:
          raise ValueError(
            f'Expected a non-empty value for `site_id` but received {site_id!r}'
          )
        if not lan_id:
          raise ValueError(
            f'Expected a non-empty value for `lan_id` but received {lan_id!r}'
          )
        return await self._patch(
            f"/accounts/{account_id}/magic/sites/{site_id}/lans/{lan_id}",
            body=await async_maybe_transform({
                "name": name,
                "nat": nat,
                "physport": physport,
                "routed_subnets": routed_subnets,
                "static_addressing": static_addressing,
                "vlan_tag": vlan_tag,
            }, lan_edit_params.LANEditParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[LAN]._unwrapper),
            cast_to=cast(Type[LAN], ResultWrapper[LAN]),
        )

    async def get(self,
    lan_id: str,
    *,
    account_id: str,
    site_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> LAN:
        """
        Get a specific Site LAN.

        Args:
          account_id: Identifier

          site_id: Identifier

          lan_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not site_id:
          raise ValueError(
            f'Expected a non-empty value for `site_id` but received {site_id!r}'
          )
        if not lan_id:
          raise ValueError(
            f'Expected a non-empty value for `lan_id` but received {lan_id!r}'
          )
        return await self._get(
            f"/accounts/{account_id}/magic/sites/{site_id}/lans/{lan_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[LAN]._unwrapper),
            cast_to=cast(Type[LAN], ResultWrapper[LAN]),
        )

class LANsResourceWithRawResponse:
    def __init__(self, lans: LANsResource) -> None:
        self._lans = lans

        self.create = to_raw_response_wrapper(
            lans.create,
        )
        self.update = to_raw_response_wrapper(
            lans.update,
        )
        self.list = to_raw_response_wrapper(
            lans.list,
        )
        self.delete = to_raw_response_wrapper(
            lans.delete,
        )
        self.edit = to_raw_response_wrapper(
            lans.edit,
        )
        self.get = to_raw_response_wrapper(
            lans.get,
        )

class AsyncLANsResourceWithRawResponse:
    def __init__(self, lans: AsyncLANsResource) -> None:
        self._lans = lans

        self.create = async_to_raw_response_wrapper(
            lans.create,
        )
        self.update = async_to_raw_response_wrapper(
            lans.update,
        )
        self.list = async_to_raw_response_wrapper(
            lans.list,
        )
        self.delete = async_to_raw_response_wrapper(
            lans.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            lans.edit,
        )
        self.get = async_to_raw_response_wrapper(
            lans.get,
        )

class LANsResourceWithStreamingResponse:
    def __init__(self, lans: LANsResource) -> None:
        self._lans = lans

        self.create = to_streamed_response_wrapper(
            lans.create,
        )
        self.update = to_streamed_response_wrapper(
            lans.update,
        )
        self.list = to_streamed_response_wrapper(
            lans.list,
        )
        self.delete = to_streamed_response_wrapper(
            lans.delete,
        )
        self.edit = to_streamed_response_wrapper(
            lans.edit,
        )
        self.get = to_streamed_response_wrapper(
            lans.get,
        )

class AsyncLANsResourceWithStreamingResponse:
    def __init__(self, lans: AsyncLANsResource) -> None:
        self._lans = lans

        self.create = async_to_streamed_response_wrapper(
            lans.create,
        )
        self.update = async_to_streamed_response_wrapper(
            lans.update,
        )
        self.list = async_to_streamed_response_wrapper(
            lans.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            lans.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            lans.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            lans.get,
        )