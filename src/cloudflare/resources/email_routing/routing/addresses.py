# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

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
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.email_routing.routing import (
    AddressGetResponse,
    AddressCreateResponse,
    AddressDeleteResponse,
    AddressEmailRoutingDestinationAddressesListDestinationAddressesResponse,
    address_create_params,
    address_email_routing_destination_addresses_list_destination_addresses_params,
)

__all__ = ["Addresses", "AsyncAddresses"]


class Addresses(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AddressesWithRawResponse:
        return AddressesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AddressesWithStreamingResponse:
        return AddressesWithStreamingResponse(self)

    def create(
        self,
        account_identifier: str,
        *,
        email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressCreateResponse:
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
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._post(
            f"/accounts/{account_identifier}/email/routing/addresses",
            body=maybe_transform({"email": email}, address_create_params.AddressCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AddressCreateResponse], ResultWrapper[AddressCreateResponse]),
        )

    def delete(
        self,
        destination_address_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressDeleteResponse:
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
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not destination_address_identifier:
            raise ValueError(
                f"Expected a non-empty value for `destination_address_identifier` but received {destination_address_identifier!r}"
            )
        return self._delete(
            f"/accounts/{account_identifier}/email/routing/addresses/{destination_address_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AddressDeleteResponse], ResultWrapper[AddressDeleteResponse]),
        )

    def email_routing_destination_addresses_list_destination_addresses(
        self,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AddressEmailRoutingDestinationAddressesListDestinationAddressesResponse]:
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
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._get(
            f"/accounts/{account_identifier}/email/routing/addresses",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "page": page,
                        "per_page": per_page,
                        "verified": verified,
                    },
                    address_email_routing_destination_addresses_list_destination_addresses_params.AddressEmailRoutingDestinationAddressesListDestinationAddressesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[AddressEmailRoutingDestinationAddressesListDestinationAddressesResponse]],
                ResultWrapper[AddressEmailRoutingDestinationAddressesListDestinationAddressesResponse],
            ),
        )

    def get(
        self,
        destination_address_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressGetResponse:
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
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not destination_address_identifier:
            raise ValueError(
                f"Expected a non-empty value for `destination_address_identifier` but received {destination_address_identifier!r}"
            )
        return self._get(
            f"/accounts/{account_identifier}/email/routing/addresses/{destination_address_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AddressGetResponse], ResultWrapper[AddressGetResponse]),
        )


class AsyncAddresses(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAddressesWithRawResponse:
        return AsyncAddressesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAddressesWithStreamingResponse:
        return AsyncAddressesWithStreamingResponse(self)

    async def create(
        self,
        account_identifier: str,
        *,
        email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressCreateResponse:
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
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._post(
            f"/accounts/{account_identifier}/email/routing/addresses",
            body=await async_maybe_transform({"email": email}, address_create_params.AddressCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AddressCreateResponse], ResultWrapper[AddressCreateResponse]),
        )

    async def delete(
        self,
        destination_address_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressDeleteResponse:
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
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not destination_address_identifier:
            raise ValueError(
                f"Expected a non-empty value for `destination_address_identifier` but received {destination_address_identifier!r}"
            )
        return await self._delete(
            f"/accounts/{account_identifier}/email/routing/addresses/{destination_address_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AddressDeleteResponse], ResultWrapper[AddressDeleteResponse]),
        )

    async def email_routing_destination_addresses_list_destination_addresses(
        self,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AddressEmailRoutingDestinationAddressesListDestinationAddressesResponse]:
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
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._get(
            f"/accounts/{account_identifier}/email/routing/addresses",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "direction": direction,
                        "page": page,
                        "per_page": per_page,
                        "verified": verified,
                    },
                    address_email_routing_destination_addresses_list_destination_addresses_params.AddressEmailRoutingDestinationAddressesListDestinationAddressesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[AddressEmailRoutingDestinationAddressesListDestinationAddressesResponse]],
                ResultWrapper[AddressEmailRoutingDestinationAddressesListDestinationAddressesResponse],
            ),
        )

    async def get(
        self,
        destination_address_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressGetResponse:
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
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not destination_address_identifier:
            raise ValueError(
                f"Expected a non-empty value for `destination_address_identifier` but received {destination_address_identifier!r}"
            )
        return await self._get(
            f"/accounts/{account_identifier}/email/routing/addresses/{destination_address_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AddressGetResponse], ResultWrapper[AddressGetResponse]),
        )


class AddressesWithRawResponse:
    def __init__(self, addresses: Addresses) -> None:
        self._addresses = addresses

        self.create = to_raw_response_wrapper(
            addresses.create,
        )
        self.delete = to_raw_response_wrapper(
            addresses.delete,
        )
        self.email_routing_destination_addresses_list_destination_addresses = to_raw_response_wrapper(
            addresses.email_routing_destination_addresses_list_destination_addresses,
        )
        self.get = to_raw_response_wrapper(
            addresses.get,
        )


class AsyncAddressesWithRawResponse:
    def __init__(self, addresses: AsyncAddresses) -> None:
        self._addresses = addresses

        self.create = async_to_raw_response_wrapper(
            addresses.create,
        )
        self.delete = async_to_raw_response_wrapper(
            addresses.delete,
        )
        self.email_routing_destination_addresses_list_destination_addresses = async_to_raw_response_wrapper(
            addresses.email_routing_destination_addresses_list_destination_addresses,
        )
        self.get = async_to_raw_response_wrapper(
            addresses.get,
        )


class AddressesWithStreamingResponse:
    def __init__(self, addresses: Addresses) -> None:
        self._addresses = addresses

        self.create = to_streamed_response_wrapper(
            addresses.create,
        )
        self.delete = to_streamed_response_wrapper(
            addresses.delete,
        )
        self.email_routing_destination_addresses_list_destination_addresses = to_streamed_response_wrapper(
            addresses.email_routing_destination_addresses_list_destination_addresses,
        )
        self.get = to_streamed_response_wrapper(
            addresses.get,
        )


class AsyncAddressesWithStreamingResponse:
    def __init__(self, addresses: AsyncAddresses) -> None:
        self._addresses = addresses

        self.create = async_to_streamed_response_wrapper(
            addresses.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            addresses.delete,
        )
        self.email_routing_destination_addresses_list_destination_addresses = async_to_streamed_response_wrapper(
            addresses.email_routing_destination_addresses_list_destination_addresses,
        )
        self.get = async_to_streamed_response_wrapper(
            addresses.get,
        )
