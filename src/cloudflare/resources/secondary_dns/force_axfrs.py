# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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

__all__ = ["ForceAxfrs", "AsyncForceAxfrs"]


class ForceAxfrs(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ForceAxfrsWithRawResponse:
        return ForceAxfrsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ForceAxfrsWithStreamingResponse:
        return ForceAxfrsWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Sends AXFR zone transfer request to primary nameserver(s).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/zones/{zone_id}/secondary_dns/force_axfr",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )


class AsyncForceAxfrs(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncForceAxfrsWithRawResponse:
        return AsyncForceAxfrsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncForceAxfrsWithStreamingResponse:
        return AsyncForceAxfrsWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Sends AXFR zone transfer request to primary nameserver(s).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/zones/{zone_id}/secondary_dns/force_axfr",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )


class ForceAxfrsWithRawResponse:
    def __init__(self, force_axfrs: ForceAxfrs) -> None:
        self._force_axfrs = force_axfrs

        self.create = to_raw_response_wrapper(
            force_axfrs.create,
        )


class AsyncForceAxfrsWithRawResponse:
    def __init__(self, force_axfrs: AsyncForceAxfrs) -> None:
        self._force_axfrs = force_axfrs

        self.create = async_to_raw_response_wrapper(
            force_axfrs.create,
        )


class ForceAxfrsWithStreamingResponse:
    def __init__(self, force_axfrs: ForceAxfrs) -> None:
        self._force_axfrs = force_axfrs

        self.create = to_streamed_response_wrapper(
            force_axfrs.create,
        )


class AsyncForceAxfrsWithStreamingResponse:
    def __init__(self, force_axfrs: AsyncForceAxfrs) -> None:
        self._force_axfrs = force_axfrs

        self.create = async_to_streamed_response_wrapper(
            force_axfrs.create,
        )
