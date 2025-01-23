# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
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
from ..._base_client import make_request_options
from ...types.network_interconnects import slot_list_params
from ...types.network_interconnects.slot_get_response import SlotGetResponse
from ...types.network_interconnects.slot_list_response import SlotListResponse

__all__ = ["SlotsResource", "AsyncSlotsResource"]


class SlotsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SlotsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SlotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SlotsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SlotsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        address_contains: Optional[str] | NotGiven = NOT_GIVEN,
        cursor: Optional[int] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        occupied: Optional[bool] | NotGiven = NOT_GIVEN,
        site: Optional[str] | NotGiven = NOT_GIVEN,
        speed: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SlotListResponse:
        """
        Retrieve a list of all slots matching the specified parameters

        Args:
          account_id: Customer account tag

          address_contains: If specified, only show slots with the given text in their address field

          occupied: If specified, only show slots with a specific occupied/unoccupied state

          site: If specified, only show slots located at the given site

          speed: If specified, only show slots that support the given speed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/cni/slots",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "address_contains": address_contains,
                        "cursor": cursor,
                        "limit": limit,
                        "occupied": occupied,
                        "site": site,
                        "speed": speed,
                    },
                    slot_list_params.SlotListParams,
                ),
            ),
            cast_to=SlotListResponse,
        )

    def get(
        self,
        slot: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SlotGetResponse:
        """
        Get information about the specified slot

        Args:
          account_id: Customer account tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not slot:
            raise ValueError(f"Expected a non-empty value for `slot` but received {slot!r}")
        return self._get(
            f"/accounts/{account_id}/cni/slots/{slot}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SlotGetResponse,
        )


class AsyncSlotsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSlotsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSlotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSlotsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSlotsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        account_id: str,
        address_contains: Optional[str] | NotGiven = NOT_GIVEN,
        cursor: Optional[int] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        occupied: Optional[bool] | NotGiven = NOT_GIVEN,
        site: Optional[str] | NotGiven = NOT_GIVEN,
        speed: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SlotListResponse:
        """
        Retrieve a list of all slots matching the specified parameters

        Args:
          account_id: Customer account tag

          address_contains: If specified, only show slots with the given text in their address field

          occupied: If specified, only show slots with a specific occupied/unoccupied state

          site: If specified, only show slots located at the given site

          speed: If specified, only show slots that support the given speed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/cni/slots",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "address_contains": address_contains,
                        "cursor": cursor,
                        "limit": limit,
                        "occupied": occupied,
                        "site": site,
                        "speed": speed,
                    },
                    slot_list_params.SlotListParams,
                ),
            ),
            cast_to=SlotListResponse,
        )

    async def get(
        self,
        slot: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SlotGetResponse:
        """
        Get information about the specified slot

        Args:
          account_id: Customer account tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not slot:
            raise ValueError(f"Expected a non-empty value for `slot` but received {slot!r}")
        return await self._get(
            f"/accounts/{account_id}/cni/slots/{slot}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SlotGetResponse,
        )


class SlotsResourceWithRawResponse:
    def __init__(self, slots: SlotsResource) -> None:
        self._slots = slots

        self.list = to_raw_response_wrapper(
            slots.list,
        )
        self.get = to_raw_response_wrapper(
            slots.get,
        )


class AsyncSlotsResourceWithRawResponse:
    def __init__(self, slots: AsyncSlotsResource) -> None:
        self._slots = slots

        self.list = async_to_raw_response_wrapper(
            slots.list,
        )
        self.get = async_to_raw_response_wrapper(
            slots.get,
        )


class SlotsResourceWithStreamingResponse:
    def __init__(self, slots: SlotsResource) -> None:
        self._slots = slots

        self.list = to_streamed_response_wrapper(
            slots.list,
        )
        self.get = to_streamed_response_wrapper(
            slots.get,
        )


class AsyncSlotsResourceWithStreamingResponse:
    def __init__(self, slots: AsyncSlotsResource) -> None:
        self._slots = slots

        self.list = async_to_streamed_response_wrapper(
            slots.list,
        )
        self.get = async_to_streamed_response_wrapper(
            slots.get,
        )
