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

__all__ = ["Statuses", "AsyncStatuses"]


class Statuses(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StatusesWithRawResponse:
        return StatusesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatusesWithStreamingResponse:
        return StatusesWithStreamingResponse(self)

    def secondary_dns_primary_zone_get_outgoing_zone_transfer_status(
        self,
        zone_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Get primary zone transfer status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/zones/{zone_id}/secondary_dns/outgoing/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )


class AsyncStatuses(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStatusesWithRawResponse:
        return AsyncStatusesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatusesWithStreamingResponse:
        return AsyncStatusesWithStreamingResponse(self)

    async def secondary_dns_primary_zone_get_outgoing_zone_transfer_status(
        self,
        zone_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Get primary zone transfer status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/zones/{zone_id}/secondary_dns/outgoing/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )


class StatusesWithRawResponse:
    def __init__(self, statuses: Statuses) -> None:
        self._statuses = statuses

        self.secondary_dns_primary_zone_get_outgoing_zone_transfer_status = to_raw_response_wrapper(
            statuses.secondary_dns_primary_zone_get_outgoing_zone_transfer_status,
        )


class AsyncStatusesWithRawResponse:
    def __init__(self, statuses: AsyncStatuses) -> None:
        self._statuses = statuses

        self.secondary_dns_primary_zone_get_outgoing_zone_transfer_status = async_to_raw_response_wrapper(
            statuses.secondary_dns_primary_zone_get_outgoing_zone_transfer_status,
        )


class StatusesWithStreamingResponse:
    def __init__(self, statuses: Statuses) -> None:
        self._statuses = statuses

        self.secondary_dns_primary_zone_get_outgoing_zone_transfer_status = to_streamed_response_wrapper(
            statuses.secondary_dns_primary_zone_get_outgoing_zone_transfer_status,
        )


class AsyncStatusesWithStreamingResponse:
    def __init__(self, statuses: AsyncStatuses) -> None:
        self._statuses = statuses

        self.secondary_dns_primary_zone_get_outgoing_zone_transfer_status = async_to_streamed_response_wrapper(
            statuses.secondary_dns_primary_zone_get_outgoing_zone_transfer_status,
        )
