# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, cast

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
from ...._base_client import make_request_options
from ....types.magic_cloud_networking.on_ramps import address_space_edit_params, address_space_update_params
from ....types.magic_cloud_networking.on_ramps.address_space_edit_response import AddressSpaceEditResponse
from ....types.magic_cloud_networking.on_ramps.address_space_list_response import AddressSpaceListResponse
from ....types.magic_cloud_networking.on_ramps.address_space_update_response import AddressSpaceUpdateResponse

__all__ = ["AddressSpacesResource", "AsyncAddressSpacesResource"]


class AddressSpacesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AddressSpacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AddressSpacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AddressSpacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AddressSpacesResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        account_id: str,
        prefixes: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressSpaceUpdateResponse:
        """
        Update the Magic WAN Address Space (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._put(
            f"/accounts/{account_id}/magic/cloud/onramps/magic_wan_address_space",
            body=maybe_transform({"prefixes": prefixes}, address_space_update_params.AddressSpaceUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AddressSpaceUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[AddressSpaceUpdateResponse], ResultWrapper[AddressSpaceUpdateResponse]),
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
    ) -> AddressSpaceListResponse:
        """
        Read the Magic WAN Address Space (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/magic/cloud/onramps/magic_wan_address_space",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AddressSpaceListResponse]._unwrapper,
            ),
            cast_to=cast(Type[AddressSpaceListResponse], ResultWrapper[AddressSpaceListResponse]),
        )

    def edit(
        self,
        *,
        account_id: str,
        prefixes: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressSpaceEditResponse:
        """
        Update the Magic WAN Address Space (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._patch(
            f"/accounts/{account_id}/magic/cloud/onramps/magic_wan_address_space",
            body=maybe_transform({"prefixes": prefixes}, address_space_edit_params.AddressSpaceEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AddressSpaceEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[AddressSpaceEditResponse], ResultWrapper[AddressSpaceEditResponse]),
        )


class AsyncAddressSpacesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAddressSpacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAddressSpacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAddressSpacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAddressSpacesResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        account_id: str,
        prefixes: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressSpaceUpdateResponse:
        """
        Update the Magic WAN Address Space (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._put(
            f"/accounts/{account_id}/magic/cloud/onramps/magic_wan_address_space",
            body=await async_maybe_transform(
                {"prefixes": prefixes}, address_space_update_params.AddressSpaceUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AddressSpaceUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[AddressSpaceUpdateResponse], ResultWrapper[AddressSpaceUpdateResponse]),
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
    ) -> AddressSpaceListResponse:
        """
        Read the Magic WAN Address Space (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/magic/cloud/onramps/magic_wan_address_space",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AddressSpaceListResponse]._unwrapper,
            ),
            cast_to=cast(Type[AddressSpaceListResponse], ResultWrapper[AddressSpaceListResponse]),
        )

    async def edit(
        self,
        *,
        account_id: str,
        prefixes: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressSpaceEditResponse:
        """
        Update the Magic WAN Address Space (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/magic/cloud/onramps/magic_wan_address_space",
            body=await async_maybe_transform({"prefixes": prefixes}, address_space_edit_params.AddressSpaceEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AddressSpaceEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[AddressSpaceEditResponse], ResultWrapper[AddressSpaceEditResponse]),
        )


class AddressSpacesResourceWithRawResponse:
    def __init__(self, address_spaces: AddressSpacesResource) -> None:
        self._address_spaces = address_spaces

        self.update = to_raw_response_wrapper(
            address_spaces.update,
        )
        self.list = to_raw_response_wrapper(
            address_spaces.list,
        )
        self.edit = to_raw_response_wrapper(
            address_spaces.edit,
        )


class AsyncAddressSpacesResourceWithRawResponse:
    def __init__(self, address_spaces: AsyncAddressSpacesResource) -> None:
        self._address_spaces = address_spaces

        self.update = async_to_raw_response_wrapper(
            address_spaces.update,
        )
        self.list = async_to_raw_response_wrapper(
            address_spaces.list,
        )
        self.edit = async_to_raw_response_wrapper(
            address_spaces.edit,
        )


class AddressSpacesResourceWithStreamingResponse:
    def __init__(self, address_spaces: AddressSpacesResource) -> None:
        self._address_spaces = address_spaces

        self.update = to_streamed_response_wrapper(
            address_spaces.update,
        )
        self.list = to_streamed_response_wrapper(
            address_spaces.list,
        )
        self.edit = to_streamed_response_wrapper(
            address_spaces.edit,
        )


class AsyncAddressSpacesResourceWithStreamingResponse:
    def __init__(self, address_spaces: AsyncAddressSpacesResource) -> None:
        self._address_spaces = address_spaces

        self.update = async_to_streamed_response_wrapper(
            address_spaces.update,
        )
        self.list = async_to_streamed_response_wrapper(
            address_spaces.list,
        )
        self.edit = async_to_streamed_response_wrapper(
            address_spaces.edit,
        )
