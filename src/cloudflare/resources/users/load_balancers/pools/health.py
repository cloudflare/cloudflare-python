# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, cast

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import (
    make_request_options,
)
from .....types.users.load_balancers.pools import HealthLoadBalancerPoolsPoolHealthDetailsResponse

__all__ = ["Health", "AsyncHealth"]


class Health(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HealthWithRawResponse:
        return HealthWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HealthWithStreamingResponse:
        return HealthWithStreamingResponse(self)

    def load_balancer_pools_pool_health_details(
        self,
        pool_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HealthLoadBalancerPoolsPoolHealthDetailsResponse:
        """
        Fetch the latest pool health status for a single pool.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return cast(
            HealthLoadBalancerPoolsPoolHealthDetailsResponse,
            self._get(
                f"/user/load_balancers/pools/{pool_id}/health",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[HealthLoadBalancerPoolsPoolHealthDetailsResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncHealth(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHealthWithRawResponse:
        return AsyncHealthWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHealthWithStreamingResponse:
        return AsyncHealthWithStreamingResponse(self)

    async def load_balancer_pools_pool_health_details(
        self,
        pool_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HealthLoadBalancerPoolsPoolHealthDetailsResponse:
        """
        Fetch the latest pool health status for a single pool.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return cast(
            HealthLoadBalancerPoolsPoolHealthDetailsResponse,
            await self._get(
                f"/user/load_balancers/pools/{pool_id}/health",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[HealthLoadBalancerPoolsPoolHealthDetailsResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class HealthWithRawResponse:
    def __init__(self, health: Health) -> None:
        self._health = health

        self.load_balancer_pools_pool_health_details = to_raw_response_wrapper(
            health.load_balancer_pools_pool_health_details,
        )


class AsyncHealthWithRawResponse:
    def __init__(self, health: AsyncHealth) -> None:
        self._health = health

        self.load_balancer_pools_pool_health_details = async_to_raw_response_wrapper(
            health.load_balancer_pools_pool_health_details,
        )


class HealthWithStreamingResponse:
    def __init__(self, health: Health) -> None:
        self._health = health

        self.load_balancer_pools_pool_health_details = to_streamed_response_wrapper(
            health.load_balancer_pools_pool_health_details,
        )


class AsyncHealthWithStreamingResponse:
    def __init__(self, health: AsyncHealth) -> None:
        self._health = health

        self.load_balancer_pools_pool_health_details = async_to_streamed_response_wrapper(
            health.load_balancer_pools_pool_health_details,
        )
