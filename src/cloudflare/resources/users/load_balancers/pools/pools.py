# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Type, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform
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
from .....types.users.load_balancers import (
    PoolLoadBalancerPoolsListPoolsResponse,
    PoolLoadBalancerPoolsCreatePoolResponse,
    PoolLoadBalancerPoolsPatchPoolsResponse,
    pool_load_balancer_pools_list_pools_params,
    pool_load_balancer_pools_create_pool_params,
    pool_load_balancer_pools_patch_pools_params,
)

__all__ = ["Pools", "AsyncPools"]


class Pools(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PoolsWithRawResponse:
        return PoolsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PoolsWithStreamingResponse:
        return PoolsWithStreamingResponse(self)

    def load_balancer_pools_create_pool(
        self,
        *,
        name: str,
        origins: Iterable[pool_load_balancer_pools_create_pool_params.Origin],
        check_regions: Optional[
            List[
                Literal[
                    "WNAM",
                    "ENAM",
                    "WEU",
                    "EEU",
                    "NSAM",
                    "SSAM",
                    "OC",
                    "ME",
                    "NAF",
                    "SAF",
                    "SAS",
                    "SEAS",
                    "NEAS",
                    "ALL_REGIONS",
                ]
            ]
        ]
        | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        latitude: float | NotGiven = NOT_GIVEN,
        load_shedding: pool_load_balancer_pools_create_pool_params.LoadShedding | NotGiven = NOT_GIVEN,
        longitude: float | NotGiven = NOT_GIVEN,
        minimum_origins: int | NotGiven = NOT_GIVEN,
        monitor: object | NotGiven = NOT_GIVEN,
        notification_email: str | NotGiven = NOT_GIVEN,
        notification_filter: Optional[pool_load_balancer_pools_create_pool_params.NotificationFilter]
        | NotGiven = NOT_GIVEN,
        origin_steering: pool_load_balancer_pools_create_pool_params.OriginSteering | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PoolLoadBalancerPoolsCreatePoolResponse:
        """Create a new pool.

        Args:
          name: A short name (tag) for the pool.

        Only alphanumeric characters, hyphens, and
              underscores are allowed.

          origins: The list of origins within this pool. Traffic directed at this pool is balanced
              across all currently healthy origins, provided the pool itself is healthy.

          check_regions: A list of regions from which to run health checks. Null means every Cloudflare
              data center.

          description: A human-readable description of the pool.

          enabled: Whether to enable (the default) or disable this pool. Disabled pools will not
              receive traffic and are excluded from health checks. Disabling a pool will cause
              any load balancers using it to failover to the next pool (if any).

          latitude: The latitude of the data center containing the origins used in this pool in
              decimal degrees. If this is set, longitude must also be set.

          load_shedding: Configures load shedding policies and percentages for the pool.

          longitude: The longitude of the data center containing the origins used in this pool in
              decimal degrees. If this is set, latitude must also be set.

          minimum_origins: The minimum number of origins that must be healthy for this pool to serve
              traffic. If the number of healthy origins falls below this number, the pool will
              be marked unhealthy and will failover to the next available pool.

          monitor: The ID of the Monitor to use for checking the health of origins within this
              pool.

          notification_email: This field is now deprecated. It has been moved to Cloudflare's Centralized
              Notification service
              https://developers.cloudflare.com/fundamentals/notifications/. The email address
              to send health status notifications to. This can be an individual mailbox or a
              mailing list. Multiple emails can be supplied as a comma delimited list.

          notification_filter: Filter pool and origin health notifications by resource type or health status.
              Use null to reset.

          origin_steering: Configures origin steering for the pool. Controls how origins are selected for
              new sessions and traffic without session affinity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/user/load_balancers/pools",
            body=maybe_transform(
                {
                    "name": name,
                    "origins": origins,
                    "check_regions": check_regions,
                    "description": description,
                    "enabled": enabled,
                    "latitude": latitude,
                    "load_shedding": load_shedding,
                    "longitude": longitude,
                    "minimum_origins": minimum_origins,
                    "monitor": monitor,
                    "notification_email": notification_email,
                    "notification_filter": notification_filter,
                    "origin_steering": origin_steering,
                },
                pool_load_balancer_pools_create_pool_params.PoolLoadBalancerPoolsCreatePoolParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[PoolLoadBalancerPoolsCreatePoolResponse], ResultWrapper[PoolLoadBalancerPoolsCreatePoolResponse]
            ),
        )

    def load_balancer_pools_list_pools(
        self,
        *,
        monitor: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PoolLoadBalancerPoolsListPoolsResponse]:
        """
        List configured pools.

        Args:
          monitor: The ID of the Monitor to use for checking the health of origins within this
              pool.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/user/load_balancers/pools",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"monitor": monitor},
                    pool_load_balancer_pools_list_pools_params.PoolLoadBalancerPoolsListPoolsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[PoolLoadBalancerPoolsListPoolsResponse]],
                ResultWrapper[PoolLoadBalancerPoolsListPoolsResponse],
            ),
        )

    def load_balancer_pools_patch_pools(
        self,
        *,
        notification_email: Literal['""'] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PoolLoadBalancerPoolsPatchPoolsResponse]:
        """Apply changes to a number of existing pools, overwriting the supplied
        properties.

        Pools are ordered by ascending `name`. Returns the list of affected
        pools. Supports the standard pagination query parameters, either
        `limit`/`offset` or `per_page`/`page`.

        Args:
          notification_email: The email address to send health status notifications to. This field is now
              deprecated in favor of Cloudflare Notifications for Load Balancing, so only
              resetting this field with an empty string `""` is accepted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/user/load_balancers/pools",
            body=maybe_transform(
                {"notification_email": notification_email},
                pool_load_balancer_pools_patch_pools_params.PoolLoadBalancerPoolsPatchPoolsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[PoolLoadBalancerPoolsPatchPoolsResponse]],
                ResultWrapper[PoolLoadBalancerPoolsPatchPoolsResponse],
            ),
        )


class AsyncPools(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPoolsWithRawResponse:
        return AsyncPoolsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPoolsWithStreamingResponse:
        return AsyncPoolsWithStreamingResponse(self)

    async def load_balancer_pools_create_pool(
        self,
        *,
        name: str,
        origins: Iterable[pool_load_balancer_pools_create_pool_params.Origin],
        check_regions: Optional[
            List[
                Literal[
                    "WNAM",
                    "ENAM",
                    "WEU",
                    "EEU",
                    "NSAM",
                    "SSAM",
                    "OC",
                    "ME",
                    "NAF",
                    "SAF",
                    "SAS",
                    "SEAS",
                    "NEAS",
                    "ALL_REGIONS",
                ]
            ]
        ]
        | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        latitude: float | NotGiven = NOT_GIVEN,
        load_shedding: pool_load_balancer_pools_create_pool_params.LoadShedding | NotGiven = NOT_GIVEN,
        longitude: float | NotGiven = NOT_GIVEN,
        minimum_origins: int | NotGiven = NOT_GIVEN,
        monitor: object | NotGiven = NOT_GIVEN,
        notification_email: str | NotGiven = NOT_GIVEN,
        notification_filter: Optional[pool_load_balancer_pools_create_pool_params.NotificationFilter]
        | NotGiven = NOT_GIVEN,
        origin_steering: pool_load_balancer_pools_create_pool_params.OriginSteering | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PoolLoadBalancerPoolsCreatePoolResponse:
        """Create a new pool.

        Args:
          name: A short name (tag) for the pool.

        Only alphanumeric characters, hyphens, and
              underscores are allowed.

          origins: The list of origins within this pool. Traffic directed at this pool is balanced
              across all currently healthy origins, provided the pool itself is healthy.

          check_regions: A list of regions from which to run health checks. Null means every Cloudflare
              data center.

          description: A human-readable description of the pool.

          enabled: Whether to enable (the default) or disable this pool. Disabled pools will not
              receive traffic and are excluded from health checks. Disabling a pool will cause
              any load balancers using it to failover to the next pool (if any).

          latitude: The latitude of the data center containing the origins used in this pool in
              decimal degrees. If this is set, longitude must also be set.

          load_shedding: Configures load shedding policies and percentages for the pool.

          longitude: The longitude of the data center containing the origins used in this pool in
              decimal degrees. If this is set, latitude must also be set.

          minimum_origins: The minimum number of origins that must be healthy for this pool to serve
              traffic. If the number of healthy origins falls below this number, the pool will
              be marked unhealthy and will failover to the next available pool.

          monitor: The ID of the Monitor to use for checking the health of origins within this
              pool.

          notification_email: This field is now deprecated. It has been moved to Cloudflare's Centralized
              Notification service
              https://developers.cloudflare.com/fundamentals/notifications/. The email address
              to send health status notifications to. This can be an individual mailbox or a
              mailing list. Multiple emails can be supplied as a comma delimited list.

          notification_filter: Filter pool and origin health notifications by resource type or health status.
              Use null to reset.

          origin_steering: Configures origin steering for the pool. Controls how origins are selected for
              new sessions and traffic without session affinity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/user/load_balancers/pools",
            body=maybe_transform(
                {
                    "name": name,
                    "origins": origins,
                    "check_regions": check_regions,
                    "description": description,
                    "enabled": enabled,
                    "latitude": latitude,
                    "load_shedding": load_shedding,
                    "longitude": longitude,
                    "minimum_origins": minimum_origins,
                    "monitor": monitor,
                    "notification_email": notification_email,
                    "notification_filter": notification_filter,
                    "origin_steering": origin_steering,
                },
                pool_load_balancer_pools_create_pool_params.PoolLoadBalancerPoolsCreatePoolParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[PoolLoadBalancerPoolsCreatePoolResponse], ResultWrapper[PoolLoadBalancerPoolsCreatePoolResponse]
            ),
        )

    async def load_balancer_pools_list_pools(
        self,
        *,
        monitor: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PoolLoadBalancerPoolsListPoolsResponse]:
        """
        List configured pools.

        Args:
          monitor: The ID of the Monitor to use for checking the health of origins within this
              pool.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/user/load_balancers/pools",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"monitor": monitor},
                    pool_load_balancer_pools_list_pools_params.PoolLoadBalancerPoolsListPoolsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[PoolLoadBalancerPoolsListPoolsResponse]],
                ResultWrapper[PoolLoadBalancerPoolsListPoolsResponse],
            ),
        )

    async def load_balancer_pools_patch_pools(
        self,
        *,
        notification_email: Literal['""'] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PoolLoadBalancerPoolsPatchPoolsResponse]:
        """Apply changes to a number of existing pools, overwriting the supplied
        properties.

        Pools are ordered by ascending `name`. Returns the list of affected
        pools. Supports the standard pagination query parameters, either
        `limit`/`offset` or `per_page`/`page`.

        Args:
          notification_email: The email address to send health status notifications to. This field is now
              deprecated in favor of Cloudflare Notifications for Load Balancing, so only
              resetting this field with an empty string `""` is accepted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/user/load_balancers/pools",
            body=maybe_transform(
                {"notification_email": notification_email},
                pool_load_balancer_pools_patch_pools_params.PoolLoadBalancerPoolsPatchPoolsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[PoolLoadBalancerPoolsPatchPoolsResponse]],
                ResultWrapper[PoolLoadBalancerPoolsPatchPoolsResponse],
            ),
        )


class PoolsWithRawResponse:
    def __init__(self, pools: Pools) -> None:
        self._pools = pools

        self.load_balancer_pools_create_pool = to_raw_response_wrapper(
            pools.load_balancer_pools_create_pool,
        )
        self.load_balancer_pools_list_pools = to_raw_response_wrapper(
            pools.load_balancer_pools_list_pools,
        )
        self.load_balancer_pools_patch_pools = to_raw_response_wrapper(
            pools.load_balancer_pools_patch_pools,
        )


class AsyncPoolsWithRawResponse:
    def __init__(self, pools: AsyncPools) -> None:
        self._pools = pools

        self.load_balancer_pools_create_pool = async_to_raw_response_wrapper(
            pools.load_balancer_pools_create_pool,
        )
        self.load_balancer_pools_list_pools = async_to_raw_response_wrapper(
            pools.load_balancer_pools_list_pools,
        )
        self.load_balancer_pools_patch_pools = async_to_raw_response_wrapper(
            pools.load_balancer_pools_patch_pools,
        )


class PoolsWithStreamingResponse:
    def __init__(self, pools: Pools) -> None:
        self._pools = pools

        self.load_balancer_pools_create_pool = to_streamed_response_wrapper(
            pools.load_balancer_pools_create_pool,
        )
        self.load_balancer_pools_list_pools = to_streamed_response_wrapper(
            pools.load_balancer_pools_list_pools,
        )
        self.load_balancer_pools_patch_pools = to_streamed_response_wrapper(
            pools.load_balancer_pools_patch_pools,
        )


class AsyncPoolsWithStreamingResponse:
    def __init__(self, pools: AsyncPools) -> None:
        self._pools = pools

        self.load_balancer_pools_create_pool = async_to_streamed_response_wrapper(
            pools.load_balancer_pools_create_pool,
        )
        self.load_balancer_pools_list_pools = async_to_streamed_response_wrapper(
            pools.load_balancer_pools_list_pools,
        )
        self.load_balancer_pools_patch_pools = async_to_streamed_response_wrapper(
            pools.load_balancer_pools_patch_pools,
        )
