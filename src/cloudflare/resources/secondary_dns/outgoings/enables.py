# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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

__all__ = ["Enables", "AsyncEnables"]


class Enables(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EnablesWithRawResponse:
        return EnablesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnablesWithStreamingResponse:
        return EnablesWithStreamingResponse(self)

    def secondary_dns_primary_zone_enable_outgoing_zone_transfers(
        self,
        zone_identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Enable outgoing zone transfers for primary zone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/zones/{zone_identifier}/secondary_dns/outgoing/enable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )


class AsyncEnables(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEnablesWithRawResponse:
        return AsyncEnablesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnablesWithStreamingResponse:
        return AsyncEnablesWithStreamingResponse(self)

    async def secondary_dns_primary_zone_enable_outgoing_zone_transfers(
        self,
        zone_identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Enable outgoing zone transfers for primary zone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/zones/{zone_identifier}/secondary_dns/outgoing/enable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )


class EnablesWithRawResponse:
    def __init__(self, enables: Enables) -> None:
        self._enables = enables

        self.secondary_dns_primary_zone_enable_outgoing_zone_transfers = to_raw_response_wrapper(
            enables.secondary_dns_primary_zone_enable_outgoing_zone_transfers,
        )


class AsyncEnablesWithRawResponse:
    def __init__(self, enables: AsyncEnables) -> None:
        self._enables = enables

        self.secondary_dns_primary_zone_enable_outgoing_zone_transfers = async_to_raw_response_wrapper(
            enables.secondary_dns_primary_zone_enable_outgoing_zone_transfers,
        )


class EnablesWithStreamingResponse:
    def __init__(self, enables: Enables) -> None:
        self._enables = enables

        self.secondary_dns_primary_zone_enable_outgoing_zone_transfers = to_streamed_response_wrapper(
            enables.secondary_dns_primary_zone_enable_outgoing_zone_transfers,
        )


class AsyncEnablesWithStreamingResponse:
    def __init__(self, enables: AsyncEnables) -> None:
        self._enables = enables

        self.secondary_dns_primary_zone_enable_outgoing_zone_transfers = async_to_streamed_response_wrapper(
            enables.secondary_dns_primary_zone_enable_outgoing_zone_transfers,
        )
