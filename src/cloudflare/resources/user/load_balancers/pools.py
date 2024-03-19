# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Type, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
from ....types.user.load_balancers import (
    PoolListResponse,
    LoadBalancingPool,
    PoolDeleteResponse,
    PoolHealthResponse,
    PoolPreviewResponse,
    PoolReferencesResponse,
    pool_edit_params,
    pool_list_params,
    pool_create_params,
    pool_update_params,
    pool_preview_params,
)

__all__ = ["Pools", "AsyncPools"]


class Pools(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PoolsWithRawResponse:
        return PoolsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PoolsWithStreamingResponse:
        return PoolsWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        origins: Iterable[pool_create_params.Origin],
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
        load_shedding: pool_create_params.LoadShedding | NotGiven = NOT_GIVEN,
        longitude: float | NotGiven = NOT_GIVEN,
        minimum_origins: int | NotGiven = NOT_GIVEN,
        monitor: object | NotGiven = NOT_GIVEN,
        notification_email: str | NotGiven = NOT_GIVEN,
        notification_filter: Optional[pool_create_params.NotificationFilter] | NotGiven = NOT_GIVEN,
        origin_steering: pool_create_params.OriginSteering | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancingPool:
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
                pool_create_params.PoolCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LoadBalancingPool], ResultWrapper[LoadBalancingPool]),
        )

    def update(
        self,
        pool_id: str,
        *,
        name: str,
        origins: Iterable[pool_update_params.Origin],
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
        load_shedding: pool_update_params.LoadShedding | NotGiven = NOT_GIVEN,
        longitude: float | NotGiven = NOT_GIVEN,
        minimum_origins: int | NotGiven = NOT_GIVEN,
        monitor: object | NotGiven = NOT_GIVEN,
        notification_email: str | NotGiven = NOT_GIVEN,
        notification_filter: Optional[pool_update_params.NotificationFilter] | NotGiven = NOT_GIVEN,
        origin_steering: pool_update_params.OriginSteering | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancingPool:
        """Modify a configured pool.

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
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return self._put(
            f"/user/load_balancers/pools/{pool_id}",
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
                pool_update_params.PoolUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LoadBalancingPool], ResultWrapper[LoadBalancingPool]),
        )

    def list(
        self,
        *,
        monitor: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PoolListResponse]:
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
                query=maybe_transform({"monitor": monitor}, pool_list_params.PoolListParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PoolListResponse]], ResultWrapper[PoolListResponse]),
        )

    def delete(
        self,
        pool_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PoolDeleteResponse:
        """
        Delete a configured pool.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return self._delete(
            f"/user/load_balancers/pools/{pool_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PoolDeleteResponse], ResultWrapper[PoolDeleteResponse]),
        )

    def edit(
        self,
        pool_id: str,
        *,
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
        load_shedding: pool_edit_params.LoadShedding | NotGiven = NOT_GIVEN,
        longitude: float | NotGiven = NOT_GIVEN,
        minimum_origins: int | NotGiven = NOT_GIVEN,
        monitor: object | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        notification_email: str | NotGiven = NOT_GIVEN,
        notification_filter: Optional[pool_edit_params.NotificationFilter] | NotGiven = NOT_GIVEN,
        origin_steering: pool_edit_params.OriginSteering | NotGiven = NOT_GIVEN,
        origins: Iterable[pool_edit_params.Origin] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancingPool:
        """
        Apply changes to an existing pool, overwriting the supplied properties.

        Args:
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

          name: A short name (tag) for the pool. Only alphanumeric characters, hyphens, and
              underscores are allowed.

          notification_email: This field is now deprecated. It has been moved to Cloudflare's Centralized
              Notification service
              https://developers.cloudflare.com/fundamentals/notifications/. The email address
              to send health status notifications to. This can be an individual mailbox or a
              mailing list. Multiple emails can be supplied as a comma delimited list.

          notification_filter: Filter pool and origin health notifications by resource type or health status.
              Use null to reset.

          origin_steering: Configures origin steering for the pool. Controls how origins are selected for
              new sessions and traffic without session affinity.

          origins: The list of origins within this pool. Traffic directed at this pool is balanced
              across all currently healthy origins, provided the pool itself is healthy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return self._patch(
            f"/user/load_balancers/pools/{pool_id}",
            body=maybe_transform(
                {
                    "check_regions": check_regions,
                    "description": description,
                    "enabled": enabled,
                    "latitude": latitude,
                    "load_shedding": load_shedding,
                    "longitude": longitude,
                    "minimum_origins": minimum_origins,
                    "monitor": monitor,
                    "name": name,
                    "notification_email": notification_email,
                    "notification_filter": notification_filter,
                    "origin_steering": origin_steering,
                    "origins": origins,
                },
                pool_edit_params.PoolEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LoadBalancingPool], ResultWrapper[LoadBalancingPool]),
        )

    def get(
        self,
        pool_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancingPool:
        """
        Fetch a single configured pool.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return self._get(
            f"/user/load_balancers/pools/{pool_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LoadBalancingPool], ResultWrapper[LoadBalancingPool]),
        )

    def health(
        self,
        pool_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PoolHealthResponse:
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
            PoolHealthResponse,
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
                    Any, ResultWrapper[PoolHealthResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def preview(
        self,
        pool_id: str,
        *,
        expected_codes: str,
        allow_insecure: bool | NotGiven = NOT_GIVEN,
        consecutive_down: int | NotGiven = NOT_GIVEN,
        consecutive_up: int | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        expected_body: str | NotGiven = NOT_GIVEN,
        follow_redirects: bool | NotGiven = NOT_GIVEN,
        header: object | NotGiven = NOT_GIVEN,
        interval: int | NotGiven = NOT_GIVEN,
        method: str | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        port: int | NotGiven = NOT_GIVEN,
        probe_zone: str | NotGiven = NOT_GIVEN,
        retries: int | NotGiven = NOT_GIVEN,
        load_balancer_monitor_timeout: int | NotGiven = NOT_GIVEN,
        type: Literal["http", "https", "tcp", "udp_icmp", "icmp_ping", "smtp"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PoolPreviewResponse:
        """Preview pool health using provided monitor details.

        The returned preview_id can
        be used in the preview endpoint to retrieve the results.

        Args:
          expected_codes: The expected HTTP response code or code range of the health check. This
              parameter is only valid for HTTP and HTTPS monitors.

          allow_insecure: Do not validate the certificate when monitor use HTTPS. This parameter is
              currently only valid for HTTP and HTTPS monitors.

          consecutive_down: To be marked unhealthy the monitored origin must fail this healthcheck N
              consecutive times.

          consecutive_up: To be marked healthy the monitored origin must pass this healthcheck N
              consecutive times.

          description: Object description.

          expected_body: A case-insensitive sub-string to look for in the response body. If this string
              is not found, the origin will be marked as unhealthy. This parameter is only
              valid for HTTP and HTTPS monitors.

          follow_redirects: Follow redirects if returned by the origin. This parameter is only valid for
              HTTP and HTTPS monitors.

          header: The HTTP request headers to send in the health check. It is recommended you set
              a Host header by default. The User-Agent header cannot be overridden. This
              parameter is only valid for HTTP and HTTPS monitors.

          interval: The interval between each health check. Shorter intervals may improve failover
              time, but will increase load on the origins as we check from multiple locations.

          method: The method to use for the health check. This defaults to 'GET' for HTTP/HTTPS
              based checks and 'connection_established' for TCP based health checks.

          path: The endpoint path you want to conduct a health check against. This parameter is
              only valid for HTTP and HTTPS monitors.

          port: The port number to connect to for the health check. Required for TCP, UDP, and
              SMTP checks. HTTP and HTTPS checks should only define the port when using a
              non-standard port (HTTP: default 80, HTTPS: default 443).

          probe_zone: Assign this monitor to emulate the specified zone while probing. This parameter
              is only valid for HTTP and HTTPS monitors.

          retries: The number of retries to attempt in case of a timeout before marking the origin
              as unhealthy. Retries are attempted immediately.

          load_balancer_monitor_timeout: The timeout (in seconds) before marking the health check as failed.

          type: The protocol to use for the health check. Currently supported protocols are
              'HTTP','HTTPS', 'TCP', 'ICMP-PING', 'UDP-ICMP', and 'SMTP'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return self._post(
            f"/user/load_balancers/pools/{pool_id}/preview",
            body=maybe_transform(
                {
                    "expected_codes": expected_codes,
                    "allow_insecure": allow_insecure,
                    "consecutive_down": consecutive_down,
                    "consecutive_up": consecutive_up,
                    "description": description,
                    "expected_body": expected_body,
                    "follow_redirects": follow_redirects,
                    "header": header,
                    "interval": interval,
                    "method": method,
                    "path": path,
                    "port": port,
                    "probe_zone": probe_zone,
                    "retries": retries,
                    "timeout": load_balancer_monitor_timeout,
                    "type": type,
                },
                pool_preview_params.PoolPreviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PoolPreviewResponse], ResultWrapper[PoolPreviewResponse]),
        )

    def references(
        self,
        pool_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PoolReferencesResponse]:
        """
        Get the list of resources that reference the provided pool.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return self._get(
            f"/user/load_balancers/pools/{pool_id}/references",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PoolReferencesResponse]], ResultWrapper[PoolReferencesResponse]),
        )


class AsyncPools(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPoolsWithRawResponse:
        return AsyncPoolsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPoolsWithStreamingResponse:
        return AsyncPoolsWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        origins: Iterable[pool_create_params.Origin],
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
        load_shedding: pool_create_params.LoadShedding | NotGiven = NOT_GIVEN,
        longitude: float | NotGiven = NOT_GIVEN,
        minimum_origins: int | NotGiven = NOT_GIVEN,
        monitor: object | NotGiven = NOT_GIVEN,
        notification_email: str | NotGiven = NOT_GIVEN,
        notification_filter: Optional[pool_create_params.NotificationFilter] | NotGiven = NOT_GIVEN,
        origin_steering: pool_create_params.OriginSteering | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancingPool:
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
            body=await async_maybe_transform(
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
                pool_create_params.PoolCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LoadBalancingPool], ResultWrapper[LoadBalancingPool]),
        )

    async def update(
        self,
        pool_id: str,
        *,
        name: str,
        origins: Iterable[pool_update_params.Origin],
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
        load_shedding: pool_update_params.LoadShedding | NotGiven = NOT_GIVEN,
        longitude: float | NotGiven = NOT_GIVEN,
        minimum_origins: int | NotGiven = NOT_GIVEN,
        monitor: object | NotGiven = NOT_GIVEN,
        notification_email: str | NotGiven = NOT_GIVEN,
        notification_filter: Optional[pool_update_params.NotificationFilter] | NotGiven = NOT_GIVEN,
        origin_steering: pool_update_params.OriginSteering | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancingPool:
        """Modify a configured pool.

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
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return await self._put(
            f"/user/load_balancers/pools/{pool_id}",
            body=await async_maybe_transform(
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
                pool_update_params.PoolUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LoadBalancingPool], ResultWrapper[LoadBalancingPool]),
        )

    async def list(
        self,
        *,
        monitor: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PoolListResponse]:
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
                query=await async_maybe_transform({"monitor": monitor}, pool_list_params.PoolListParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PoolListResponse]], ResultWrapper[PoolListResponse]),
        )

    async def delete(
        self,
        pool_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PoolDeleteResponse:
        """
        Delete a configured pool.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return await self._delete(
            f"/user/load_balancers/pools/{pool_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PoolDeleteResponse], ResultWrapper[PoolDeleteResponse]),
        )

    async def edit(
        self,
        pool_id: str,
        *,
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
        load_shedding: pool_edit_params.LoadShedding | NotGiven = NOT_GIVEN,
        longitude: float | NotGiven = NOT_GIVEN,
        minimum_origins: int | NotGiven = NOT_GIVEN,
        monitor: object | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        notification_email: str | NotGiven = NOT_GIVEN,
        notification_filter: Optional[pool_edit_params.NotificationFilter] | NotGiven = NOT_GIVEN,
        origin_steering: pool_edit_params.OriginSteering | NotGiven = NOT_GIVEN,
        origins: Iterable[pool_edit_params.Origin] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancingPool:
        """
        Apply changes to an existing pool, overwriting the supplied properties.

        Args:
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

          name: A short name (tag) for the pool. Only alphanumeric characters, hyphens, and
              underscores are allowed.

          notification_email: This field is now deprecated. It has been moved to Cloudflare's Centralized
              Notification service
              https://developers.cloudflare.com/fundamentals/notifications/. The email address
              to send health status notifications to. This can be an individual mailbox or a
              mailing list. Multiple emails can be supplied as a comma delimited list.

          notification_filter: Filter pool and origin health notifications by resource type or health status.
              Use null to reset.

          origin_steering: Configures origin steering for the pool. Controls how origins are selected for
              new sessions and traffic without session affinity.

          origins: The list of origins within this pool. Traffic directed at this pool is balanced
              across all currently healthy origins, provided the pool itself is healthy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return await self._patch(
            f"/user/load_balancers/pools/{pool_id}",
            body=await async_maybe_transform(
                {
                    "check_regions": check_regions,
                    "description": description,
                    "enabled": enabled,
                    "latitude": latitude,
                    "load_shedding": load_shedding,
                    "longitude": longitude,
                    "minimum_origins": minimum_origins,
                    "monitor": monitor,
                    "name": name,
                    "notification_email": notification_email,
                    "notification_filter": notification_filter,
                    "origin_steering": origin_steering,
                    "origins": origins,
                },
                pool_edit_params.PoolEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LoadBalancingPool], ResultWrapper[LoadBalancingPool]),
        )

    async def get(
        self,
        pool_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancingPool:
        """
        Fetch a single configured pool.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return await self._get(
            f"/user/load_balancers/pools/{pool_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LoadBalancingPool], ResultWrapper[LoadBalancingPool]),
        )

    async def health(
        self,
        pool_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PoolHealthResponse:
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
            PoolHealthResponse,
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
                    Any, ResultWrapper[PoolHealthResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def preview(
        self,
        pool_id: str,
        *,
        expected_codes: str,
        allow_insecure: bool | NotGiven = NOT_GIVEN,
        consecutive_down: int | NotGiven = NOT_GIVEN,
        consecutive_up: int | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        expected_body: str | NotGiven = NOT_GIVEN,
        follow_redirects: bool | NotGiven = NOT_GIVEN,
        header: object | NotGiven = NOT_GIVEN,
        interval: int | NotGiven = NOT_GIVEN,
        method: str | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        port: int | NotGiven = NOT_GIVEN,
        probe_zone: str | NotGiven = NOT_GIVEN,
        retries: int | NotGiven = NOT_GIVEN,
        load_balancer_monitor_timeout: int | NotGiven = NOT_GIVEN,
        type: Literal["http", "https", "tcp", "udp_icmp", "icmp_ping", "smtp"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PoolPreviewResponse:
        """Preview pool health using provided monitor details.

        The returned preview_id can
        be used in the preview endpoint to retrieve the results.

        Args:
          expected_codes: The expected HTTP response code or code range of the health check. This
              parameter is only valid for HTTP and HTTPS monitors.

          allow_insecure: Do not validate the certificate when monitor use HTTPS. This parameter is
              currently only valid for HTTP and HTTPS monitors.

          consecutive_down: To be marked unhealthy the monitored origin must fail this healthcheck N
              consecutive times.

          consecutive_up: To be marked healthy the monitored origin must pass this healthcheck N
              consecutive times.

          description: Object description.

          expected_body: A case-insensitive sub-string to look for in the response body. If this string
              is not found, the origin will be marked as unhealthy. This parameter is only
              valid for HTTP and HTTPS monitors.

          follow_redirects: Follow redirects if returned by the origin. This parameter is only valid for
              HTTP and HTTPS monitors.

          header: The HTTP request headers to send in the health check. It is recommended you set
              a Host header by default. The User-Agent header cannot be overridden. This
              parameter is only valid for HTTP and HTTPS monitors.

          interval: The interval between each health check. Shorter intervals may improve failover
              time, but will increase load on the origins as we check from multiple locations.

          method: The method to use for the health check. This defaults to 'GET' for HTTP/HTTPS
              based checks and 'connection_established' for TCP based health checks.

          path: The endpoint path you want to conduct a health check against. This parameter is
              only valid for HTTP and HTTPS monitors.

          port: The port number to connect to for the health check. Required for TCP, UDP, and
              SMTP checks. HTTP and HTTPS checks should only define the port when using a
              non-standard port (HTTP: default 80, HTTPS: default 443).

          probe_zone: Assign this monitor to emulate the specified zone while probing. This parameter
              is only valid for HTTP and HTTPS monitors.

          retries: The number of retries to attempt in case of a timeout before marking the origin
              as unhealthy. Retries are attempted immediately.

          load_balancer_monitor_timeout: The timeout (in seconds) before marking the health check as failed.

          type: The protocol to use for the health check. Currently supported protocols are
              'HTTP','HTTPS', 'TCP', 'ICMP-PING', 'UDP-ICMP', and 'SMTP'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return await self._post(
            f"/user/load_balancers/pools/{pool_id}/preview",
            body=await async_maybe_transform(
                {
                    "expected_codes": expected_codes,
                    "allow_insecure": allow_insecure,
                    "consecutive_down": consecutive_down,
                    "consecutive_up": consecutive_up,
                    "description": description,
                    "expected_body": expected_body,
                    "follow_redirects": follow_redirects,
                    "header": header,
                    "interval": interval,
                    "method": method,
                    "path": path,
                    "port": port,
                    "probe_zone": probe_zone,
                    "retries": retries,
                    "timeout": load_balancer_monitor_timeout,
                    "type": type,
                },
                pool_preview_params.PoolPreviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PoolPreviewResponse], ResultWrapper[PoolPreviewResponse]),
        )

    async def references(
        self,
        pool_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PoolReferencesResponse]:
        """
        Get the list of resources that reference the provided pool.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return await self._get(
            f"/user/load_balancers/pools/{pool_id}/references",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PoolReferencesResponse]], ResultWrapper[PoolReferencesResponse]),
        )


class PoolsWithRawResponse:
    def __init__(self, pools: Pools) -> None:
        self._pools = pools

        self.create = to_raw_response_wrapper(
            pools.create,
        )
        self.update = to_raw_response_wrapper(
            pools.update,
        )
        self.list = to_raw_response_wrapper(
            pools.list,
        )
        self.delete = to_raw_response_wrapper(
            pools.delete,
        )
        self.edit = to_raw_response_wrapper(
            pools.edit,
        )
        self.get = to_raw_response_wrapper(
            pools.get,
        )
        self.health = to_raw_response_wrapper(
            pools.health,
        )
        self.preview = to_raw_response_wrapper(
            pools.preview,
        )
        self.references = to_raw_response_wrapper(
            pools.references,
        )


class AsyncPoolsWithRawResponse:
    def __init__(self, pools: AsyncPools) -> None:
        self._pools = pools

        self.create = async_to_raw_response_wrapper(
            pools.create,
        )
        self.update = async_to_raw_response_wrapper(
            pools.update,
        )
        self.list = async_to_raw_response_wrapper(
            pools.list,
        )
        self.delete = async_to_raw_response_wrapper(
            pools.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            pools.edit,
        )
        self.get = async_to_raw_response_wrapper(
            pools.get,
        )
        self.health = async_to_raw_response_wrapper(
            pools.health,
        )
        self.preview = async_to_raw_response_wrapper(
            pools.preview,
        )
        self.references = async_to_raw_response_wrapper(
            pools.references,
        )


class PoolsWithStreamingResponse:
    def __init__(self, pools: Pools) -> None:
        self._pools = pools

        self.create = to_streamed_response_wrapper(
            pools.create,
        )
        self.update = to_streamed_response_wrapper(
            pools.update,
        )
        self.list = to_streamed_response_wrapper(
            pools.list,
        )
        self.delete = to_streamed_response_wrapper(
            pools.delete,
        )
        self.edit = to_streamed_response_wrapper(
            pools.edit,
        )
        self.get = to_streamed_response_wrapper(
            pools.get,
        )
        self.health = to_streamed_response_wrapper(
            pools.health,
        )
        self.preview = to_streamed_response_wrapper(
            pools.preview,
        )
        self.references = to_streamed_response_wrapper(
            pools.references,
        )


class AsyncPoolsWithStreamingResponse:
    def __init__(self, pools: AsyncPools) -> None:
        self._pools = pools

        self.create = async_to_streamed_response_wrapper(
            pools.create,
        )
        self.update = async_to_streamed_response_wrapper(
            pools.update,
        )
        self.list = async_to_streamed_response_wrapper(
            pools.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            pools.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            pools.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            pools.get,
        )
        self.health = async_to_streamed_response_wrapper(
            pools.health,
        )
        self.preview = async_to_streamed_response_wrapper(
            pools.preview,
        )
        self.references = async_to_streamed_response_wrapper(
            pools.references,
        )
