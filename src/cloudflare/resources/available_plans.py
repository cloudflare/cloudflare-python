# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..types import AvailablePlanListResponse, BillSubsAPIAvailableRatePlan
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

__all__ = ["AvailablePlans", "AsyncAvailablePlans"]


class AvailablePlans(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AvailablePlansWithRawResponse:
        return AvailablePlansWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AvailablePlansWithStreamingResponse:
        return AvailablePlansWithStreamingResponse(self)

    def list(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AvailablePlanListResponse]:
        """
        Lists available plans the zone can subscribe to.

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
            f"/zones/{zone_identifier}/available_plans",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AvailablePlanListResponse]], ResultWrapper[AvailablePlanListResponse]),
        )

    def get(
        self,
        plan_identifier: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillSubsAPIAvailableRatePlan:
        """
        Details of the available plan that the zone can subscribe to.

        Args:
          zone_identifier: Identifier

          plan_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not plan_identifier:
            raise ValueError(f"Expected a non-empty value for `plan_identifier` but received {plan_identifier!r}")
        return self._get(
            f"/zones/{zone_identifier}/available_plans/{plan_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[BillSubsAPIAvailableRatePlan], ResultWrapper[BillSubsAPIAvailableRatePlan]),
        )


class AsyncAvailablePlans(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAvailablePlansWithRawResponse:
        return AsyncAvailablePlansWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAvailablePlansWithStreamingResponse:
        return AsyncAvailablePlansWithStreamingResponse(self)

    async def list(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AvailablePlanListResponse]:
        """
        Lists available plans the zone can subscribe to.

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
            f"/zones/{zone_identifier}/available_plans",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AvailablePlanListResponse]], ResultWrapper[AvailablePlanListResponse]),
        )

    async def get(
        self,
        plan_identifier: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillSubsAPIAvailableRatePlan:
        """
        Details of the available plan that the zone can subscribe to.

        Args:
          zone_identifier: Identifier

          plan_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not plan_identifier:
            raise ValueError(f"Expected a non-empty value for `plan_identifier` but received {plan_identifier!r}")
        return await self._get(
            f"/zones/{zone_identifier}/available_plans/{plan_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[BillSubsAPIAvailableRatePlan], ResultWrapper[BillSubsAPIAvailableRatePlan]),
        )


class AvailablePlansWithRawResponse:
    def __init__(self, available_plans: AvailablePlans) -> None:
        self._available_plans = available_plans

        self.list = to_raw_response_wrapper(
            available_plans.list,
        )
        self.get = to_raw_response_wrapper(
            available_plans.get,
        )


class AsyncAvailablePlansWithRawResponse:
    def __init__(self, available_plans: AsyncAvailablePlans) -> None:
        self._available_plans = available_plans

        self.list = async_to_raw_response_wrapper(
            available_plans.list,
        )
        self.get = async_to_raw_response_wrapper(
            available_plans.get,
        )


class AvailablePlansWithStreamingResponse:
    def __init__(self, available_plans: AvailablePlans) -> None:
        self._available_plans = available_plans

        self.list = to_streamed_response_wrapper(
            available_plans.list,
        )
        self.get = to_streamed_response_wrapper(
            available_plans.get,
        )


class AsyncAvailablePlansWithStreamingResponse:
    def __init__(self, available_plans: AsyncAvailablePlans) -> None:
        self._available_plans = available_plans

        self.list = async_to_streamed_response_wrapper(
            available_plans.list,
        )
        self.get = async_to_streamed_response_wrapper(
            available_plans.get,
        )
