# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..types import AvailableRatePlanGetResponse
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import ResultWrapper
from .._base_client import (
    make_request_options,
)

__all__ = ["AvailableRatePlans", "AsyncAvailableRatePlans"]


class AvailableRatePlans(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AvailableRatePlansWithRawResponse:
        return AvailableRatePlansWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AvailableRatePlansWithStreamingResponse:
        return AvailableRatePlansWithStreamingResponse(self)

    def get(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AvailableRatePlanGetResponse]:
        """
        Lists all rate plans the zone can subscribe to.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._get(
            f"/zones/{zone_identifier}/available_rate_plans",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AvailableRatePlanGetResponse]], ResultWrapper[AvailableRatePlanGetResponse]),
        )


class AsyncAvailableRatePlans(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAvailableRatePlansWithRawResponse:
        return AsyncAvailableRatePlansWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAvailableRatePlansWithStreamingResponse:
        return AsyncAvailableRatePlansWithStreamingResponse(self)

    async def get(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AvailableRatePlanGetResponse]:
        """
        Lists all rate plans the zone can subscribe to.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._get(
            f"/zones/{zone_identifier}/available_rate_plans",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AvailableRatePlanGetResponse]], ResultWrapper[AvailableRatePlanGetResponse]),
        )


class AvailableRatePlansWithRawResponse:
    def __init__(self, available_rate_plans: AvailableRatePlans) -> None:
        self._available_rate_plans = available_rate_plans

        self.get = to_raw_response_wrapper(
            available_rate_plans.get,
        )


class AsyncAvailableRatePlansWithRawResponse:
    def __init__(self, available_rate_plans: AsyncAvailableRatePlans) -> None:
        self._available_rate_plans = available_rate_plans

        self.get = async_to_raw_response_wrapper(
            available_rate_plans.get,
        )


class AvailableRatePlansWithStreamingResponse:
    def __init__(self, available_rate_plans: AvailableRatePlans) -> None:
        self._available_rate_plans = available_rate_plans

        self.get = to_streamed_response_wrapper(
            available_rate_plans.get,
        )


class AsyncAvailableRatePlansWithStreamingResponse:
    def __init__(self, available_rate_plans: AsyncAvailableRatePlans) -> None:
        self._available_rate_plans = available_rate_plans

        self.get = async_to_streamed_response_wrapper(
            available_rate_plans.get,
        )
