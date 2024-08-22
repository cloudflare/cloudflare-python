# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.email_routing.address import Address

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type

from ..._base_client import make_request_options, AsyncPaginator

from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray

from typing_extensions import Literal

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from ...types.email_routing import address_create_params
from ...types.email_routing import address_list_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["AddressesResource", "AsyncAddressesResource"]

class AddressesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AddressesResourceWithRawResponse:
        return AddressesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AddressesResourceWithStreamingResponse:
        return AddressesResourceWithStreamingResponse(self)

    def create(self,
    account_identifier: str,
    *,
    email: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[Address]:
        """Create a destination address to forward your emails to.

        Destination addresses
        need to be verified before they can be used.

        Args:
          account_identifier: Identifier

          email: The contact email address of the user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
          raise ValueError(
            f'Expected a non-empty value for `account_identifier` but received {account_identifier!r}'
          )
        return self._post(
            f"/accounts/{account_identifier}/email/routing/addresses",
            body=maybe_transform({
                "email": email
            }, address_create_params.AddressCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[Address]]._unwrapper),
            cast_to=cast(Type[Optional[Address]], ResultWrapper[Address]),
        )

    def list(self,
    account_identifier: str,
    *,
    direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
    page: float | NotGiven = NOT_GIVEN,
    per_page: float | NotGiven = NOT_GIVEN,
    verified: Literal[True, False] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> SyncV4PagePaginationArray[Address]:
        """
        Lists existing destination addresses.

        Args:
          account_identifier: Identifier

          direction: Sorts results in an ascending or descending order.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          verified: Filter by verified destination addresses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
          raise ValueError(
            f'Expected a non-empty value for `account_identifier` but received {account_identifier!r}'
          )
        return self._get_api_list(
            f"/accounts/{account_identifier}/email/routing/addresses",
            page = SyncV4PagePaginationArray[Address],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "direction": direction,
                "page": page,
                "per_page": per_page,
                "verified": verified,
            }, address_list_params.AddressListParams)),
            model=Address,
        )

    def delete(self,
    destination_address_identifier: str,
    *,
    account_identifier: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[Address]:
        """
        Deletes a specific destination address.

        Args:
          account_identifier: Identifier

          destination_address_identifier: Destination address identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
          raise ValueError(
            f'Expected a non-empty value for `account_identifier` but received {account_identifier!r}'
          )
        if not destination_address_identifier:
          raise ValueError(
            f'Expected a non-empty value for `destination_address_identifier` but received {destination_address_identifier!r}'
          )
        return self._delete(
            f"/accounts/{account_identifier}/email/routing/addresses/{destination_address_identifier}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[Address]]._unwrapper),
            cast_to=cast(Type[Optional[Address]], ResultWrapper[Address]),
        )

    def get(self,
    destination_address_identifier: str,
    *,
    account_identifier: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[Address]:
        """
        Gets information for a specific destination email already created.

        Args:
          account_identifier: Identifier

          destination_address_identifier: Destination address identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
          raise ValueError(
            f'Expected a non-empty value for `account_identifier` but received {account_identifier!r}'
          )
        if not destination_address_identifier:
          raise ValueError(
            f'Expected a non-empty value for `destination_address_identifier` but received {destination_address_identifier!r}'
          )
        return self._get(
            f"/accounts/{account_identifier}/email/routing/addresses/{destination_address_identifier}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[Address]]._unwrapper),
            cast_to=cast(Type[Optional[Address]], ResultWrapper[Address]),
        )

class AsyncAddressesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAddressesResourceWithRawResponse:
        return AsyncAddressesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAddressesResourceWithStreamingResponse:
        return AsyncAddressesResourceWithStreamingResponse(self)

    async def create(self,
    account_identifier: str,
    *,
    email: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[Address]:
        """Create a destination address to forward your emails to.

        Destination addresses
        need to be verified before they can be used.

        Args:
          account_identifier: Identifier

          email: The contact email address of the user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
          raise ValueError(
            f'Expected a non-empty value for `account_identifier` but received {account_identifier!r}'
          )
        return await self._post(
            f"/accounts/{account_identifier}/email/routing/addresses",
            body=await async_maybe_transform({
                "email": email
            }, address_create_params.AddressCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[Address]]._unwrapper),
            cast_to=cast(Type[Optional[Address]], ResultWrapper[Address]),
        )

    def list(self,
    account_identifier: str,
    *,
    direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
    page: float | NotGiven = NOT_GIVEN,
    per_page: float | NotGiven = NOT_GIVEN,
    verified: Literal[True, False] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AsyncPaginator[Address, AsyncV4PagePaginationArray[Address]]:
        """
        Lists existing destination addresses.

        Args:
          account_identifier: Identifier

          direction: Sorts results in an ascending or descending order.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          verified: Filter by verified destination addresses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
          raise ValueError(
            f'Expected a non-empty value for `account_identifier` but received {account_identifier!r}'
          )
        return self._get_api_list(
            f"/accounts/{account_identifier}/email/routing/addresses",
            page = AsyncV4PagePaginationArray[Address],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "direction": direction,
                "page": page,
                "per_page": per_page,
                "verified": verified,
            }, address_list_params.AddressListParams)),
            model=Address,
        )

    async def delete(self,
    destination_address_identifier: str,
    *,
    account_identifier: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[Address]:
        """
        Deletes a specific destination address.

        Args:
          account_identifier: Identifier

          destination_address_identifier: Destination address identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
          raise ValueError(
            f'Expected a non-empty value for `account_identifier` but received {account_identifier!r}'
          )
        if not destination_address_identifier:
          raise ValueError(
            f'Expected a non-empty value for `destination_address_identifier` but received {destination_address_identifier!r}'
          )
        return await self._delete(
            f"/accounts/{account_identifier}/email/routing/addresses/{destination_address_identifier}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[Address]]._unwrapper),
            cast_to=cast(Type[Optional[Address]], ResultWrapper[Address]),
        )

    async def get(self,
    destination_address_identifier: str,
    *,
    account_identifier: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[Address]:
        """
        Gets information for a specific destination email already created.

        Args:
          account_identifier: Identifier

          destination_address_identifier: Destination address identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
          raise ValueError(
            f'Expected a non-empty value for `account_identifier` but received {account_identifier!r}'
          )
        if not destination_address_identifier:
          raise ValueError(
            f'Expected a non-empty value for `destination_address_identifier` but received {destination_address_identifier!r}'
          )
        return await self._get(
            f"/accounts/{account_identifier}/email/routing/addresses/{destination_address_identifier}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[Address]]._unwrapper),
            cast_to=cast(Type[Optional[Address]], ResultWrapper[Address]),
        )

class AddressesResourceWithRawResponse:
    def __init__(self, addresses: AddressesResource) -> None:
        self._addresses = addresses

        self.create = to_raw_response_wrapper(
            addresses.create,
        )
        self.list = to_raw_response_wrapper(
            addresses.list,
        )
        self.delete = to_raw_response_wrapper(
            addresses.delete,
        )
        self.get = to_raw_response_wrapper(
            addresses.get,
        )

class AsyncAddressesResourceWithRawResponse:
    def __init__(self, addresses: AsyncAddressesResource) -> None:
        self._addresses = addresses

        self.create = async_to_raw_response_wrapper(
            addresses.create,
        )
        self.list = async_to_raw_response_wrapper(
            addresses.list,
        )
        self.delete = async_to_raw_response_wrapper(
            addresses.delete,
        )
        self.get = async_to_raw_response_wrapper(
            addresses.get,
        )

class AddressesResourceWithStreamingResponse:
    def __init__(self, addresses: AddressesResource) -> None:
        self._addresses = addresses

        self.create = to_streamed_response_wrapper(
            addresses.create,
        )
        self.list = to_streamed_response_wrapper(
            addresses.list,
        )
        self.delete = to_streamed_response_wrapper(
            addresses.delete,
        )
        self.get = to_streamed_response_wrapper(
            addresses.get,
        )

class AsyncAddressesResourceWithStreamingResponse:
    def __init__(self, addresses: AsyncAddressesResource) -> None:
        self._addresses = addresses

        self.create = async_to_streamed_response_wrapper(
            addresses.create,
        )
        self.list = async_to_streamed_response_wrapper(
            addresses.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            addresses.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            addresses.get,
        )