# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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

__all__ = ["Status", "AsyncStatus"]


class Status(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StatusWithRawResponse:
        return StatusWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatusWithStreamingResponse:
        return StatusWithStreamingResponse(self)

    def get(
        self,
        *,
        zone_id: str,
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
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
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


class AsyncStatus(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStatusWithRawResponse:
        return AsyncStatusWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatusWithStreamingResponse:
        return AsyncStatusWithStreamingResponse(self)

    async def get(
        self,
        *,
        zone_id: str,
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
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
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


class StatusWithRawResponse:
    def __init__(self, status: Status) -> None:
        self._status = status

        self.get = to_raw_response_wrapper(
            status.get,
        )


class AsyncStatusWithRawResponse:
    def __init__(self, status: AsyncStatus) -> None:
        self._status = status

        self.get = async_to_raw_response_wrapper(
            status.get,
        )


class StatusWithStreamingResponse:
    def __init__(self, status: Status) -> None:
        self._status = status

        self.get = to_streamed_response_wrapper(
            status.get,
        )


class AsyncStatusWithStreamingResponse:
    def __init__(self, status: AsyncStatus) -> None:
        self._status = status

        self.get = async_to_streamed_response_wrapper(
            status.get,
        )
