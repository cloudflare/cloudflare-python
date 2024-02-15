# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.access import SeatZeroTrustSeatsUpdateAUserSeatResponse, seat_zero_trust_seats_update_a_user_seat_params

from typing import Type, Optional, Iterable

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.access import seat_zero_trust_seats_update_a_user_seat_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Seats", "AsyncSeats"]


class Seats(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SeatsWithRawResponse:
        return SeatsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SeatsWithStreamingResponse:
        return SeatsWithStreamingResponse(self)

    def zero_trust_seats_update_a_user_seat(
        self,
        identifier: str,
        *,
        body: Iterable[seat_zero_trust_seats_update_a_user_seat_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SeatZeroTrustSeatsUpdateAUserSeatResponse]:
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
            body=maybe_transform(
                body, seat_zero_trust_seats_update_a_user_seat_params.SeatZeroTrustSeatsUpdateAUserSeatParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[SeatZeroTrustSeatsUpdateAUserSeatResponse]],
                ResultWrapper[SeatZeroTrustSeatsUpdateAUserSeatResponse],
            ),
        )


class AsyncSeats(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSeatsWithRawResponse:
        return AsyncSeatsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSeatsWithStreamingResponse:
        return AsyncSeatsWithStreamingResponse(self)

    async def zero_trust_seats_update_a_user_seat(
        self,
        identifier: str,
        *,
        body: Iterable[seat_zero_trust_seats_update_a_user_seat_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SeatZeroTrustSeatsUpdateAUserSeatResponse]:
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
            body=maybe_transform(
                body, seat_zero_trust_seats_update_a_user_seat_params.SeatZeroTrustSeatsUpdateAUserSeatParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[SeatZeroTrustSeatsUpdateAUserSeatResponse]],
                ResultWrapper[SeatZeroTrustSeatsUpdateAUserSeatResponse],
            ),
        )


class SeatsWithRawResponse:
    def __init__(self, seats: Seats) -> None:
        self._seats = seats

        self.zero_trust_seats_update_a_user_seat = to_raw_response_wrapper(
            seats.zero_trust_seats_update_a_user_seat,
        )


class AsyncSeatsWithRawResponse:
    def __init__(self, seats: AsyncSeats) -> None:
        self._seats = seats

        self.zero_trust_seats_update_a_user_seat = async_to_raw_response_wrapper(
            seats.zero_trust_seats_update_a_user_seat,
        )


class SeatsWithStreamingResponse:
    def __init__(self, seats: Seats) -> None:
        self._seats = seats

        self.zero_trust_seats_update_a_user_seat = to_streamed_response_wrapper(
            seats.zero_trust_seats_update_a_user_seat,
        )


class AsyncSeatsWithStreamingResponse:
    def __init__(self, seats: AsyncSeats) -> None:
        self._seats = seats

        self.zero_trust_seats_update_a_user_seat = async_to_streamed_response_wrapper(
            seats.zero_trust_seats_update_a_user_seat,
        )
