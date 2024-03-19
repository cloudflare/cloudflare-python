# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast

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
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.zero_trust import SeatEditResponse, seat_edit_params

__all__ = ["Seats", "AsyncSeats"]


class Seats(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SeatsWithRawResponse:
        return SeatsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SeatsWithStreamingResponse:
        return SeatsWithStreamingResponse(self)

    def edit(
        self,
        identifier: str,
        *,
        body: Iterable[seat_edit_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SeatEditResponse]:
        """
        Removes a user from a Zero Trust seat when both `access_seat` and `gateway_seat`
        are set to false.

        Args:
          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._patch(
            f"/accounts/{identifier}/access/seats",
            body=maybe_transform(body, seat_edit_params.SeatEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SeatEditResponse]], ResultWrapper[SeatEditResponse]),
        )


class AsyncSeats(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSeatsWithRawResponse:
        return AsyncSeatsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSeatsWithStreamingResponse:
        return AsyncSeatsWithStreamingResponse(self)

    async def edit(
        self,
        identifier: str,
        *,
        body: Iterable[seat_edit_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SeatEditResponse]:
        """
        Removes a user from a Zero Trust seat when both `access_seat` and `gateway_seat`
        are set to false.

        Args:
          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._patch(
            f"/accounts/{identifier}/access/seats",
            body=await async_maybe_transform(body, seat_edit_params.SeatEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SeatEditResponse]], ResultWrapper[SeatEditResponse]),
        )


class SeatsWithRawResponse:
    def __init__(self, seats: Seats) -> None:
        self._seats = seats

        self.edit = to_raw_response_wrapper(
            seats.edit,
        )


class AsyncSeatsWithRawResponse:
    def __init__(self, seats: AsyncSeats) -> None:
        self._seats = seats

        self.edit = async_to_raw_response_wrapper(
            seats.edit,
        )


class SeatsWithStreamingResponse:
    def __init__(self, seats: Seats) -> None:
        self._seats = seats

        self.edit = to_streamed_response_wrapper(
            seats.edit,
        )


class AsyncSeatsWithStreamingResponse:
    def __init__(self, seats: AsyncSeats) -> None:
        self._seats = seats

        self.edit = async_to_streamed_response_wrapper(
            seats.edit,
        )
