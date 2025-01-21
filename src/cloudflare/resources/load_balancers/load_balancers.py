# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Type, Iterable, cast

import httpx

from .regions import (
    RegionsResource,
    AsyncRegionsResource,
    RegionsResourceWithRawResponse,
    AsyncRegionsResourceWithRawResponse,
    RegionsResourceWithStreamingResponse,
    AsyncRegionsResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .previews import (
    PreviewsResource,
    AsyncPreviewsResource,
    PreviewsResourceWithRawResponse,
    AsyncPreviewsResourceWithRawResponse,
    PreviewsResourceWithStreamingResponse,
    AsyncPreviewsResourceWithStreamingResponse,
)
from .searches import (
    SearchesResource,
    AsyncSearchesResource,
    SearchesResourceWithRawResponse,
    AsyncSearchesResourceWithRawResponse,
    SearchesResourceWithStreamingResponse,
    AsyncSearchesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from .pools.pools import (
    PoolsResource,
    AsyncPoolsResource,
    PoolsResourceWithRawResponse,
    AsyncPoolsResourceWithRawResponse,
    PoolsResourceWithStreamingResponse,
    AsyncPoolsResourceWithStreamingResponse,
)
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options
from .monitors.monitors import (
    MonitorsResource,
    AsyncMonitorsResource,
    MonitorsResourceWithRawResponse,
    AsyncMonitorsResourceWithRawResponse,
    MonitorsResourceWithStreamingResponse,
    AsyncMonitorsResourceWithStreamingResponse,
)
from ...types.load_balancers import (
    SteeringPolicy,
    SessionAffinity,
    load_balancer_edit_params,
    load_balancer_create_params,
    load_balancer_update_params,
)
from ...types.load_balancers.rules_param import RulesParam
from ...types.load_balancers.default_pools import DefaultPools
from ...types.load_balancers.load_balancer import LoadBalancer
from ...types.load_balancers.steering_policy import SteeringPolicy
from ...types.load_balancers.session_affinity import SessionAffinity
from ...types.load_balancers.random_steering_param import RandomSteeringParam
from ...types.load_balancers.adaptive_routing_param import AdaptiveRoutingParam
from ...types.load_balancers.location_strategy_param import LocationStrategyParam
from ...types.load_balancers.load_balancer_delete_response import LoadBalancerDeleteResponse
from ...types.load_balancers.session_affinity_attributes_param import SessionAffinityAttributesParam

__all__ = ["LoadBalancersResource", "AsyncLoadBalancersResource"]


class LoadBalancersResource(SyncAPIResource):
    @cached_property
    def monitors(self) -> MonitorsResource:
        return MonitorsResource(self._client)

    @cached_property
    def pools(self) -> PoolsResource:
        return PoolsResource(self._client)

    @cached_property
    def previews(self) -> PreviewsResource:
        return PreviewsResource(self._client)

    @cached_property
    def regions(self) -> RegionsResource:
        return RegionsResource(self._client)

    @cached_property
    def searches(self) -> SearchesResource:
        return SearchesResource(self._client)

    @cached_property
    def with_raw_response(self) -> LoadBalancersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return LoadBalancersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LoadBalancersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return LoadBalancersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        default_pools: List[DefaultPools],
        fallback_pool: str,
        name: str,
        adaptive_routing: AdaptiveRoutingParam | NotGiven = NOT_GIVEN,
        country_pools: Dict[str, List[str]] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        location_strategy: LocationStrategyParam | NotGiven = NOT_GIVEN,
        networks: List[str] | NotGiven = NOT_GIVEN,
        pop_pools: Dict[str, List[str]] | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        random_steering: RandomSteeringParam | NotGiven = NOT_GIVEN,
        region_pools: Dict[str, List[str]] | NotGiven = NOT_GIVEN,
        rules: Iterable[RulesParam] | NotGiven = NOT_GIVEN,
        session_affinity: SessionAffinity | NotGiven = NOT_GIVEN,
        session_affinity_attributes: SessionAffinityAttributesParam | NotGiven = NOT_GIVEN,
        session_affinity_ttl: float | NotGiven = NOT_GIVEN,
        steering_policy: SteeringPolicy | NotGiven = NOT_GIVEN,
        ttl: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancer:
        """
        Create a new load balancer.

        Args:
          default_pools: A list of pool IDs ordered by their failover priority. Pools defined here are
              used by default, or when region_pools are not configured for a given region.

          fallback_pool: The pool ID to use when all other pools are detected as unhealthy.

          name: The DNS hostname to associate with your Load Balancer. If this hostname already
              exists as a DNS record in Cloudflare's DNS, the Load Balancer will take
              precedence and the DNS record will not be used.

          adaptive_routing: Controls features that modify the routing of requests to pools and origins in
              response to dynamic conditions, such as during the interval between active
              health monitoring requests. For example, zero-downtime failover occurs
              immediately when an origin becomes unavailable due to HTTP 521, 522, or 523
              response codes. If there is another healthy origin in the same pool, the request
              is retried once against this alternate origin.

          country_pools: A mapping of country codes to a list of pool IDs (ordered by their failover
              priority) for the given country. Any country not explicitly defined will fall
              back to using the corresponding region_pool mapping if it exists else to
              default_pools.

          description: Object description.

          location_strategy: Controls location-based steering for non-proxied requests. See `steering_policy`
              to learn how steering is affected.

          networks: List of networks where Load Balancer or Pool is enabled.

          pop_pools: (Enterprise only): A mapping of Cloudflare PoP identifiers to a list of pool IDs
              (ordered by their failover priority) for the PoP (datacenter). Any PoPs not
              explicitly defined will fall back to using the corresponding country_pool, then
              region_pool mapping if it exists else to default_pools.

          proxied: Whether the hostname should be gray clouded (false) or orange clouded (true).

          random_steering: Configures pool weights.

              - `steering_policy="random"`: A random pool is selected with probability
                proportional to pool weights.
              - `steering_policy="least_outstanding_requests"`: Use pool weights to scale each
                pool's outstanding requests.
              - `steering_policy="least_connections"`: Use pool weights to scale each pool's
                open connections.

          region_pools: A mapping of region codes to a list of pool IDs (ordered by their failover
              priority) for the given region. Any regions not explicitly defined will fall
              back to using default_pools.

          rules: BETA Field Not General Access: A list of rules for this load balancer to
              execute.

          session_affinity: Specifies the type of session affinity the load balancer should use unless
              specified as `"none"`. The supported types are:

              - `"cookie"`: On the first request to a proxied load balancer, a cookie is
                generated, encoding information of which origin the request will be forwarded
                to. Subsequent requests, by the same client to the same load balancer, will be
                sent to the origin server the cookie encodes, for the duration of the cookie
                and as long as the origin server remains healthy. If the cookie has expired or
                the origin server is unhealthy, then a new origin server is calculated and
                used.
              - `"ip_cookie"`: Behaves the same as `"cookie"` except the initial origin
                selection is stable and based on the client's ip address.
              - `"header"`: On the first request to a proxied load balancer, a session key
                based on the configured HTTP headers (see
                `session_affinity_attributes.headers`) is generated, encoding the request
                headers used for storing in the load balancer session state which origin the
                request will be forwarded to. Subsequent requests to the load balancer with
                the same headers will be sent to the same origin server, for the duration of
                the session and as long as the origin server remains healthy. If the session
                has been idle for the duration of `session_affinity_ttl` seconds or the origin
                server is unhealthy, then a new origin server is calculated and used. See
                `headers` in `session_affinity_attributes` for additional required
                configuration.

          session_affinity_attributes: Configures attributes for session affinity.

          session_affinity_ttl: Time, in seconds, until a client's session expires after being created. Once the
              expiry time has been reached, subsequent requests may get sent to a different
              origin server. The accepted ranges per `session_affinity` policy are:

              - `"cookie"` / `"ip_cookie"`: The current default of 23 hours will be used
                unless explicitly set. The accepted range of values is between [1800, 604800].
              - `"header"`: The current default of 1800 seconds will be used unless explicitly
                set. The accepted range of values is between [30, 3600]. Note: With session
                affinity by header, sessions only expire after they haven't been used for the
                number of seconds specified.

          steering_policy: Steering Policy for this load balancer.

              - `"off"`: Use `default_pools`.
              - `"geo"`: Use `region_pools`/`country_pools`/`pop_pools`. For non-proxied
                requests, the country for `country_pools` is determined by
                `location_strategy`.
              - `"random"`: Select a pool randomly.
              - `"dynamic_latency"`: Use round trip time to select the closest pool in
                default_pools (requires pool health checks).
              - `"proximity"`: Use the pools' latitude and longitude to select the closest
                pool using the Cloudflare PoP location for proxied requests or the location
                determined by `location_strategy` for non-proxied requests.
              - `"least_outstanding_requests"`: Select a pool by taking into consideration
                `random_steering` weights, as well as each pool's number of outstanding
                requests. Pools with more pending requests are weighted proportionately less
                relative to others.
              - `"least_connections"`: Select a pool by taking into consideration
                `random_steering` weights, as well as each pool's number of open connections.
                Pools with more open connections are weighted proportionately less relative to
                others. Supported for HTTP/1 and HTTP/2 connections.
              - `""`: Will map to `"geo"` if you use
                `region_pools`/`country_pools`/`pop_pools` otherwise `"off"`.

          ttl: Time to live (TTL) of the DNS entry for the IP address returned by this load
              balancer. This only applies to gray-clouded (unproxied) load balancers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/load_balancers",
            body=maybe_transform(
                {
                    "default_pools": default_pools,
                    "fallback_pool": fallback_pool,
                    "name": name,
                    "adaptive_routing": adaptive_routing,
                    "country_pools": country_pools,
                    "description": description,
                    "location_strategy": location_strategy,
                    "networks": networks,
                    "pop_pools": pop_pools,
                    "proxied": proxied,
                    "random_steering": random_steering,
                    "region_pools": region_pools,
                    "rules": rules,
                    "session_affinity": session_affinity,
                    "session_affinity_attributes": session_affinity_attributes,
                    "session_affinity_ttl": session_affinity_ttl,
                    "steering_policy": steering_policy,
                    "ttl": ttl,
                },
                load_balancer_create_params.LoadBalancerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[LoadBalancer]._unwrapper,
            ),
            cast_to=cast(Type[LoadBalancer], ResultWrapper[LoadBalancer]),
        )

    def update(
        self,
        load_balancer_id: str,
        *,
        zone_id: str,
        default_pools: List[DefaultPools],
        fallback_pool: str,
        name: str,
        adaptive_routing: AdaptiveRoutingParam | NotGiven = NOT_GIVEN,
        country_pools: Dict[str, List[str]] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        location_strategy: LocationStrategyParam | NotGiven = NOT_GIVEN,
        networks: List[str] | NotGiven = NOT_GIVEN,
        pop_pools: Dict[str, List[str]] | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        random_steering: RandomSteeringParam | NotGiven = NOT_GIVEN,
        region_pools: Dict[str, List[str]] | NotGiven = NOT_GIVEN,
        rules: Iterable[RulesParam] | NotGiven = NOT_GIVEN,
        session_affinity: SessionAffinity | NotGiven = NOT_GIVEN,
        session_affinity_attributes: SessionAffinityAttributesParam | NotGiven = NOT_GIVEN,
        session_affinity_ttl: float | NotGiven = NOT_GIVEN,
        steering_policy: SteeringPolicy | NotGiven = NOT_GIVEN,
        ttl: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancer:
        """
        Update a configured load balancer.

        Args:
          default_pools: A list of pool IDs ordered by their failover priority. Pools defined here are
              used by default, or when region_pools are not configured for a given region.

          fallback_pool: The pool ID to use when all other pools are detected as unhealthy.

          name: The DNS hostname to associate with your Load Balancer. If this hostname already
              exists as a DNS record in Cloudflare's DNS, the Load Balancer will take
              precedence and the DNS record will not be used.

          adaptive_routing: Controls features that modify the routing of requests to pools and origins in
              response to dynamic conditions, such as during the interval between active
              health monitoring requests. For example, zero-downtime failover occurs
              immediately when an origin becomes unavailable due to HTTP 521, 522, or 523
              response codes. If there is another healthy origin in the same pool, the request
              is retried once against this alternate origin.

          country_pools: A mapping of country codes to a list of pool IDs (ordered by their failover
              priority) for the given country. Any country not explicitly defined will fall
              back to using the corresponding region_pool mapping if it exists else to
              default_pools.

          description: Object description.

          enabled: Whether to enable (the default) this load balancer.

          location_strategy: Controls location-based steering for non-proxied requests. See `steering_policy`
              to learn how steering is affected.

          networks: List of networks where Load Balancer or Pool is enabled.

          pop_pools: (Enterprise only): A mapping of Cloudflare PoP identifiers to a list of pool IDs
              (ordered by their failover priority) for the PoP (datacenter). Any PoPs not
              explicitly defined will fall back to using the corresponding country_pool, then
              region_pool mapping if it exists else to default_pools.

          proxied: Whether the hostname should be gray clouded (false) or orange clouded (true).

          random_steering: Configures pool weights.

              - `steering_policy="random"`: A random pool is selected with probability
                proportional to pool weights.
              - `steering_policy="least_outstanding_requests"`: Use pool weights to scale each
                pool's outstanding requests.
              - `steering_policy="least_connections"`: Use pool weights to scale each pool's
                open connections.

          region_pools: A mapping of region codes to a list of pool IDs (ordered by their failover
              priority) for the given region. Any regions not explicitly defined will fall
              back to using default_pools.

          rules: BETA Field Not General Access: A list of rules for this load balancer to
              execute.

          session_affinity: Specifies the type of session affinity the load balancer should use unless
              specified as `"none"`. The supported types are:

              - `"cookie"`: On the first request to a proxied load balancer, a cookie is
                generated, encoding information of which origin the request will be forwarded
                to. Subsequent requests, by the same client to the same load balancer, will be
                sent to the origin server the cookie encodes, for the duration of the cookie
                and as long as the origin server remains healthy. If the cookie has expired or
                the origin server is unhealthy, then a new origin server is calculated and
                used.
              - `"ip_cookie"`: Behaves the same as `"cookie"` except the initial origin
                selection is stable and based on the client's ip address.
              - `"header"`: On the first request to a proxied load balancer, a session key
                based on the configured HTTP headers (see
                `session_affinity_attributes.headers`) is generated, encoding the request
                headers used for storing in the load balancer session state which origin the
                request will be forwarded to. Subsequent requests to the load balancer with
                the same headers will be sent to the same origin server, for the duration of
                the session and as long as the origin server remains healthy. If the session
                has been idle for the duration of `session_affinity_ttl` seconds or the origin
                server is unhealthy, then a new origin server is calculated and used. See
                `headers` in `session_affinity_attributes` for additional required
                configuration.

          session_affinity_attributes: Configures attributes for session affinity.

          session_affinity_ttl: Time, in seconds, until a client's session expires after being created. Once the
              expiry time has been reached, subsequent requests may get sent to a different
              origin server. The accepted ranges per `session_affinity` policy are:

              - `"cookie"` / `"ip_cookie"`: The current default of 23 hours will be used
                unless explicitly set. The accepted range of values is between [1800, 604800].
              - `"header"`: The current default of 1800 seconds will be used unless explicitly
                set. The accepted range of values is between [30, 3600]. Note: With session
                affinity by header, sessions only expire after they haven't been used for the
                number of seconds specified.

          steering_policy: Steering Policy for this load balancer.

              - `"off"`: Use `default_pools`.
              - `"geo"`: Use `region_pools`/`country_pools`/`pop_pools`. For non-proxied
                requests, the country for `country_pools` is determined by
                `location_strategy`.
              - `"random"`: Select a pool randomly.
              - `"dynamic_latency"`: Use round trip time to select the closest pool in
                default_pools (requires pool health checks).
              - `"proximity"`: Use the pools' latitude and longitude to select the closest
                pool using the Cloudflare PoP location for proxied requests or the location
                determined by `location_strategy` for non-proxied requests.
              - `"least_outstanding_requests"`: Select a pool by taking into consideration
                `random_steering` weights, as well as each pool's number of outstanding
                requests. Pools with more pending requests are weighted proportionately less
                relative to others.
              - `"least_connections"`: Select a pool by taking into consideration
                `random_steering` weights, as well as each pool's number of open connections.
                Pools with more open connections are weighted proportionately less relative to
                others. Supported for HTTP/1 and HTTP/2 connections.
              - `""`: Will map to `"geo"` if you use
                `region_pools`/`country_pools`/`pop_pools` otherwise `"off"`.

          ttl: Time to live (TTL) of the DNS entry for the IP address returned by this load
              balancer. This only applies to gray-clouded (unproxied) load balancers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not load_balancer_id:
            raise ValueError(f"Expected a non-empty value for `load_balancer_id` but received {load_balancer_id!r}")
        return self._put(
            f"/zones/{zone_id}/load_balancers/{load_balancer_id}",
            body=maybe_transform(
                {
                    "default_pools": default_pools,
                    "fallback_pool": fallback_pool,
                    "name": name,
                    "adaptive_routing": adaptive_routing,
                    "country_pools": country_pools,
                    "description": description,
                    "enabled": enabled,
                    "location_strategy": location_strategy,
                    "networks": networks,
                    "pop_pools": pop_pools,
                    "proxied": proxied,
                    "random_steering": random_steering,
                    "region_pools": region_pools,
                    "rules": rules,
                    "session_affinity": session_affinity,
                    "session_affinity_attributes": session_affinity_attributes,
                    "session_affinity_ttl": session_affinity_ttl,
                    "steering_policy": steering_policy,
                    "ttl": ttl,
                },
                load_balancer_update_params.LoadBalancerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[LoadBalancer]._unwrapper,
            ),
            cast_to=cast(Type[LoadBalancer], ResultWrapper[LoadBalancer]),
        )

    def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[LoadBalancer]:
        """
        List configured load balancers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/load_balancers",
            page=SyncSinglePage[LoadBalancer],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=LoadBalancer,
        )

    def delete(
        self,
        load_balancer_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancerDeleteResponse:
        """
        Delete a configured load balancer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not load_balancer_id:
            raise ValueError(f"Expected a non-empty value for `load_balancer_id` but received {load_balancer_id!r}")
        return self._delete(
            f"/zones/{zone_id}/load_balancers/{load_balancer_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[LoadBalancerDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[LoadBalancerDeleteResponse], ResultWrapper[LoadBalancerDeleteResponse]),
        )

    def edit(
        self,
        load_balancer_id: str,
        *,
        zone_id: str,
        adaptive_routing: AdaptiveRoutingParam | NotGiven = NOT_GIVEN,
        country_pools: Dict[str, List[str]] | NotGiven = NOT_GIVEN,
        default_pools: List[DefaultPools] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        fallback_pool: str | NotGiven = NOT_GIVEN,
        location_strategy: LocationStrategyParam | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        pop_pools: Dict[str, List[str]] | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        random_steering: RandomSteeringParam | NotGiven = NOT_GIVEN,
        region_pools: Dict[str, List[str]] | NotGiven = NOT_GIVEN,
        rules: Iterable[RulesParam] | NotGiven = NOT_GIVEN,
        session_affinity: SessionAffinity | NotGiven = NOT_GIVEN,
        session_affinity_attributes: SessionAffinityAttributesParam | NotGiven = NOT_GIVEN,
        session_affinity_ttl: float | NotGiven = NOT_GIVEN,
        steering_policy: SteeringPolicy | NotGiven = NOT_GIVEN,
        ttl: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancer:
        """
        Apply changes to an existing load balancer, overwriting the supplied properties.

        Args:
          adaptive_routing: Controls features that modify the routing of requests to pools and origins in
              response to dynamic conditions, such as during the interval between active
              health monitoring requests. For example, zero-downtime failover occurs
              immediately when an origin becomes unavailable due to HTTP 521, 522, or 523
              response codes. If there is another healthy origin in the same pool, the request
              is retried once against this alternate origin.

          country_pools: A mapping of country codes to a list of pool IDs (ordered by their failover
              priority) for the given country. Any country not explicitly defined will fall
              back to using the corresponding region_pool mapping if it exists else to
              default_pools.

          default_pools: A list of pool IDs ordered by their failover priority. Pools defined here are
              used by default, or when region_pools are not configured for a given region.

          description: Object description.

          enabled: Whether to enable (the default) this load balancer.

          fallback_pool: The pool ID to use when all other pools are detected as unhealthy.

          location_strategy: Controls location-based steering for non-proxied requests. See `steering_policy`
              to learn how steering is affected.

          name: The DNS hostname to associate with your Load Balancer. If this hostname already
              exists as a DNS record in Cloudflare's DNS, the Load Balancer will take
              precedence and the DNS record will not be used.

          pop_pools: (Enterprise only): A mapping of Cloudflare PoP identifiers to a list of pool IDs
              (ordered by their failover priority) for the PoP (datacenter). Any PoPs not
              explicitly defined will fall back to using the corresponding country_pool, then
              region_pool mapping if it exists else to default_pools.

          proxied: Whether the hostname should be gray clouded (false) or orange clouded (true).

          random_steering: Configures pool weights.

              - `steering_policy="random"`: A random pool is selected with probability
                proportional to pool weights.
              - `steering_policy="least_outstanding_requests"`: Use pool weights to scale each
                pool's outstanding requests.
              - `steering_policy="least_connections"`: Use pool weights to scale each pool's
                open connections.

          region_pools: A mapping of region codes to a list of pool IDs (ordered by their failover
              priority) for the given region. Any regions not explicitly defined will fall
              back to using default_pools.

          rules: BETA Field Not General Access: A list of rules for this load balancer to
              execute.

          session_affinity: Specifies the type of session affinity the load balancer should use unless
              specified as `"none"`. The supported types are:

              - `"cookie"`: On the first request to a proxied load balancer, a cookie is
                generated, encoding information of which origin the request will be forwarded
                to. Subsequent requests, by the same client to the same load balancer, will be
                sent to the origin server the cookie encodes, for the duration of the cookie
                and as long as the origin server remains healthy. If the cookie has expired or
                the origin server is unhealthy, then a new origin server is calculated and
                used.
              - `"ip_cookie"`: Behaves the same as `"cookie"` except the initial origin
                selection is stable and based on the client's ip address.
              - `"header"`: On the first request to a proxied load balancer, a session key
                based on the configured HTTP headers (see
                `session_affinity_attributes.headers`) is generated, encoding the request
                headers used for storing in the load balancer session state which origin the
                request will be forwarded to. Subsequent requests to the load balancer with
                the same headers will be sent to the same origin server, for the duration of
                the session and as long as the origin server remains healthy. If the session
                has been idle for the duration of `session_affinity_ttl` seconds or the origin
                server is unhealthy, then a new origin server is calculated and used. See
                `headers` in `session_affinity_attributes` for additional required
                configuration.

          session_affinity_attributes: Configures attributes for session affinity.

          session_affinity_ttl: Time, in seconds, until a client's session expires after being created. Once the
              expiry time has been reached, subsequent requests may get sent to a different
              origin server. The accepted ranges per `session_affinity` policy are:

              - `"cookie"` / `"ip_cookie"`: The current default of 23 hours will be used
                unless explicitly set. The accepted range of values is between [1800, 604800].
              - `"header"`: The current default of 1800 seconds will be used unless explicitly
                set. The accepted range of values is between [30, 3600]. Note: With session
                affinity by header, sessions only expire after they haven't been used for the
                number of seconds specified.

          steering_policy: Steering Policy for this load balancer.

              - `"off"`: Use `default_pools`.
              - `"geo"`: Use `region_pools`/`country_pools`/`pop_pools`. For non-proxied
                requests, the country for `country_pools` is determined by
                `location_strategy`.
              - `"random"`: Select a pool randomly.
              - `"dynamic_latency"`: Use round trip time to select the closest pool in
                default_pools (requires pool health checks).
              - `"proximity"`: Use the pools' latitude and longitude to select the closest
                pool using the Cloudflare PoP location for proxied requests or the location
                determined by `location_strategy` for non-proxied requests.
              - `"least_outstanding_requests"`: Select a pool by taking into consideration
                `random_steering` weights, as well as each pool's number of outstanding
                requests. Pools with more pending requests are weighted proportionately less
                relative to others.
              - `"least_connections"`: Select a pool by taking into consideration
                `random_steering` weights, as well as each pool's number of open connections.
                Pools with more open connections are weighted proportionately less relative to
                others. Supported for HTTP/1 and HTTP/2 connections.
              - `""`: Will map to `"geo"` if you use
                `region_pools`/`country_pools`/`pop_pools` otherwise `"off"`.

          ttl: Time to live (TTL) of the DNS entry for the IP address returned by this load
              balancer. This only applies to gray-clouded (unproxied) load balancers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not load_balancer_id:
            raise ValueError(f"Expected a non-empty value for `load_balancer_id` but received {load_balancer_id!r}")
        return self._patch(
            f"/zones/{zone_id}/load_balancers/{load_balancer_id}",
            body=maybe_transform(
                {
                    "adaptive_routing": adaptive_routing,
                    "country_pools": country_pools,
                    "default_pools": default_pools,
                    "description": description,
                    "enabled": enabled,
                    "fallback_pool": fallback_pool,
                    "location_strategy": location_strategy,
                    "name": name,
                    "pop_pools": pop_pools,
                    "proxied": proxied,
                    "random_steering": random_steering,
                    "region_pools": region_pools,
                    "rules": rules,
                    "session_affinity": session_affinity,
                    "session_affinity_attributes": session_affinity_attributes,
                    "session_affinity_ttl": session_affinity_ttl,
                    "steering_policy": steering_policy,
                    "ttl": ttl,
                },
                load_balancer_edit_params.LoadBalancerEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[LoadBalancer]._unwrapper,
            ),
            cast_to=cast(Type[LoadBalancer], ResultWrapper[LoadBalancer]),
        )

    def get(
        self,
        load_balancer_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancer:
        """
        Fetch a single configured load balancer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not load_balancer_id:
            raise ValueError(f"Expected a non-empty value for `load_balancer_id` but received {load_balancer_id!r}")
        return self._get(
            f"/zones/{zone_id}/load_balancers/{load_balancer_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[LoadBalancer]._unwrapper,
            ),
            cast_to=cast(Type[LoadBalancer], ResultWrapper[LoadBalancer]),
        )


class AsyncLoadBalancersResource(AsyncAPIResource):
    @cached_property
    def monitors(self) -> AsyncMonitorsResource:
        return AsyncMonitorsResource(self._client)

    @cached_property
    def pools(self) -> AsyncPoolsResource:
        return AsyncPoolsResource(self._client)

    @cached_property
    def previews(self) -> AsyncPreviewsResource:
        return AsyncPreviewsResource(self._client)

    @cached_property
    def regions(self) -> AsyncRegionsResource:
        return AsyncRegionsResource(self._client)

    @cached_property
    def searches(self) -> AsyncSearchesResource:
        return AsyncSearchesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLoadBalancersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLoadBalancersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLoadBalancersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncLoadBalancersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        default_pools: List[DefaultPools],
        fallback_pool: str,
        name: str,
        adaptive_routing: AdaptiveRoutingParam | NotGiven = NOT_GIVEN,
        country_pools: Dict[str, List[str]] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        location_strategy: LocationStrategyParam | NotGiven = NOT_GIVEN,
        networks: List[str] | NotGiven = NOT_GIVEN,
        pop_pools: Dict[str, List[str]] | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        random_steering: RandomSteeringParam | NotGiven = NOT_GIVEN,
        region_pools: Dict[str, List[str]] | NotGiven = NOT_GIVEN,
        rules: Iterable[RulesParam] | NotGiven = NOT_GIVEN,
        session_affinity: SessionAffinity | NotGiven = NOT_GIVEN,
        session_affinity_attributes: SessionAffinityAttributesParam | NotGiven = NOT_GIVEN,
        session_affinity_ttl: float | NotGiven = NOT_GIVEN,
        steering_policy: SteeringPolicy | NotGiven = NOT_GIVEN,
        ttl: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancer:
        """
        Create a new load balancer.

        Args:
          default_pools: A list of pool IDs ordered by their failover priority. Pools defined here are
              used by default, or when region_pools are not configured for a given region.

          fallback_pool: The pool ID to use when all other pools are detected as unhealthy.

          name: The DNS hostname to associate with your Load Balancer. If this hostname already
              exists as a DNS record in Cloudflare's DNS, the Load Balancer will take
              precedence and the DNS record will not be used.

          adaptive_routing: Controls features that modify the routing of requests to pools and origins in
              response to dynamic conditions, such as during the interval between active
              health monitoring requests. For example, zero-downtime failover occurs
              immediately when an origin becomes unavailable due to HTTP 521, 522, or 523
              response codes. If there is another healthy origin in the same pool, the request
              is retried once against this alternate origin.

          country_pools: A mapping of country codes to a list of pool IDs (ordered by their failover
              priority) for the given country. Any country not explicitly defined will fall
              back to using the corresponding region_pool mapping if it exists else to
              default_pools.

          description: Object description.

          location_strategy: Controls location-based steering for non-proxied requests. See `steering_policy`
              to learn how steering is affected.

          networks: List of networks where Load Balancer or Pool is enabled.

          pop_pools: (Enterprise only): A mapping of Cloudflare PoP identifiers to a list of pool IDs
              (ordered by their failover priority) for the PoP (datacenter). Any PoPs not
              explicitly defined will fall back to using the corresponding country_pool, then
              region_pool mapping if it exists else to default_pools.

          proxied: Whether the hostname should be gray clouded (false) or orange clouded (true).

          random_steering: Configures pool weights.

              - `steering_policy="random"`: A random pool is selected with probability
                proportional to pool weights.
              - `steering_policy="least_outstanding_requests"`: Use pool weights to scale each
                pool's outstanding requests.
              - `steering_policy="least_connections"`: Use pool weights to scale each pool's
                open connections.

          region_pools: A mapping of region codes to a list of pool IDs (ordered by their failover
              priority) for the given region. Any regions not explicitly defined will fall
              back to using default_pools.

          rules: BETA Field Not General Access: A list of rules for this load balancer to
              execute.

          session_affinity: Specifies the type of session affinity the load balancer should use unless
              specified as `"none"`. The supported types are:

              - `"cookie"`: On the first request to a proxied load balancer, a cookie is
                generated, encoding information of which origin the request will be forwarded
                to. Subsequent requests, by the same client to the same load balancer, will be
                sent to the origin server the cookie encodes, for the duration of the cookie
                and as long as the origin server remains healthy. If the cookie has expired or
                the origin server is unhealthy, then a new origin server is calculated and
                used.
              - `"ip_cookie"`: Behaves the same as `"cookie"` except the initial origin
                selection is stable and based on the client's ip address.
              - `"header"`: On the first request to a proxied load balancer, a session key
                based on the configured HTTP headers (see
                `session_affinity_attributes.headers`) is generated, encoding the request
                headers used for storing in the load balancer session state which origin the
                request will be forwarded to. Subsequent requests to the load balancer with
                the same headers will be sent to the same origin server, for the duration of
                the session and as long as the origin server remains healthy. If the session
                has been idle for the duration of `session_affinity_ttl` seconds or the origin
                server is unhealthy, then a new origin server is calculated and used. See
                `headers` in `session_affinity_attributes` for additional required
                configuration.

          session_affinity_attributes: Configures attributes for session affinity.

          session_affinity_ttl: Time, in seconds, until a client's session expires after being created. Once the
              expiry time has been reached, subsequent requests may get sent to a different
              origin server. The accepted ranges per `session_affinity` policy are:

              - `"cookie"` / `"ip_cookie"`: The current default of 23 hours will be used
                unless explicitly set. The accepted range of values is between [1800, 604800].
              - `"header"`: The current default of 1800 seconds will be used unless explicitly
                set. The accepted range of values is between [30, 3600]. Note: With session
                affinity by header, sessions only expire after they haven't been used for the
                number of seconds specified.

          steering_policy: Steering Policy for this load balancer.

              - `"off"`: Use `default_pools`.
              - `"geo"`: Use `region_pools`/`country_pools`/`pop_pools`. For non-proxied
                requests, the country for `country_pools` is determined by
                `location_strategy`.
              - `"random"`: Select a pool randomly.
              - `"dynamic_latency"`: Use round trip time to select the closest pool in
                default_pools (requires pool health checks).
              - `"proximity"`: Use the pools' latitude and longitude to select the closest
                pool using the Cloudflare PoP location for proxied requests or the location
                determined by `location_strategy` for non-proxied requests.
              - `"least_outstanding_requests"`: Select a pool by taking into consideration
                `random_steering` weights, as well as each pool's number of outstanding
                requests. Pools with more pending requests are weighted proportionately less
                relative to others.
              - `"least_connections"`: Select a pool by taking into consideration
                `random_steering` weights, as well as each pool's number of open connections.
                Pools with more open connections are weighted proportionately less relative to
                others. Supported for HTTP/1 and HTTP/2 connections.
              - `""`: Will map to `"geo"` if you use
                `region_pools`/`country_pools`/`pop_pools` otherwise `"off"`.

          ttl: Time to live (TTL) of the DNS entry for the IP address returned by this load
              balancer. This only applies to gray-clouded (unproxied) load balancers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/load_balancers",
            body=await async_maybe_transform(
                {
                    "default_pools": default_pools,
                    "fallback_pool": fallback_pool,
                    "name": name,
                    "adaptive_routing": adaptive_routing,
                    "country_pools": country_pools,
                    "description": description,
                    "location_strategy": location_strategy,
                    "networks": networks,
                    "pop_pools": pop_pools,
                    "proxied": proxied,
                    "random_steering": random_steering,
                    "region_pools": region_pools,
                    "rules": rules,
                    "session_affinity": session_affinity,
                    "session_affinity_attributes": session_affinity_attributes,
                    "session_affinity_ttl": session_affinity_ttl,
                    "steering_policy": steering_policy,
                    "ttl": ttl,
                },
                load_balancer_create_params.LoadBalancerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[LoadBalancer]._unwrapper,
            ),
            cast_to=cast(Type[LoadBalancer], ResultWrapper[LoadBalancer]),
        )

    async def update(
        self,
        load_balancer_id: str,
        *,
        zone_id: str,
        default_pools: List[DefaultPools],
        fallback_pool: str,
        name: str,
        adaptive_routing: AdaptiveRoutingParam | NotGiven = NOT_GIVEN,
        country_pools: Dict[str, List[str]] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        location_strategy: LocationStrategyParam | NotGiven = NOT_GIVEN,
        networks: List[str] | NotGiven = NOT_GIVEN,
        pop_pools: Dict[str, List[str]] | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        random_steering: RandomSteeringParam | NotGiven = NOT_GIVEN,
        region_pools: Dict[str, List[str]] | NotGiven = NOT_GIVEN,
        rules: Iterable[RulesParam] | NotGiven = NOT_GIVEN,
        session_affinity: SessionAffinity | NotGiven = NOT_GIVEN,
        session_affinity_attributes: SessionAffinityAttributesParam | NotGiven = NOT_GIVEN,
        session_affinity_ttl: float | NotGiven = NOT_GIVEN,
        steering_policy: SteeringPolicy | NotGiven = NOT_GIVEN,
        ttl: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancer:
        """
        Update a configured load balancer.

        Args:
          default_pools: A list of pool IDs ordered by their failover priority. Pools defined here are
              used by default, or when region_pools are not configured for a given region.

          fallback_pool: The pool ID to use when all other pools are detected as unhealthy.

          name: The DNS hostname to associate with your Load Balancer. If this hostname already
              exists as a DNS record in Cloudflare's DNS, the Load Balancer will take
              precedence and the DNS record will not be used.

          adaptive_routing: Controls features that modify the routing of requests to pools and origins in
              response to dynamic conditions, such as during the interval between active
              health monitoring requests. For example, zero-downtime failover occurs
              immediately when an origin becomes unavailable due to HTTP 521, 522, or 523
              response codes. If there is another healthy origin in the same pool, the request
              is retried once against this alternate origin.

          country_pools: A mapping of country codes to a list of pool IDs (ordered by their failover
              priority) for the given country. Any country not explicitly defined will fall
              back to using the corresponding region_pool mapping if it exists else to
              default_pools.

          description: Object description.

          enabled: Whether to enable (the default) this load balancer.

          location_strategy: Controls location-based steering for non-proxied requests. See `steering_policy`
              to learn how steering is affected.

          networks: List of networks where Load Balancer or Pool is enabled.

          pop_pools: (Enterprise only): A mapping of Cloudflare PoP identifiers to a list of pool IDs
              (ordered by their failover priority) for the PoP (datacenter). Any PoPs not
              explicitly defined will fall back to using the corresponding country_pool, then
              region_pool mapping if it exists else to default_pools.

          proxied: Whether the hostname should be gray clouded (false) or orange clouded (true).

          random_steering: Configures pool weights.

              - `steering_policy="random"`: A random pool is selected with probability
                proportional to pool weights.
              - `steering_policy="least_outstanding_requests"`: Use pool weights to scale each
                pool's outstanding requests.
              - `steering_policy="least_connections"`: Use pool weights to scale each pool's
                open connections.

          region_pools: A mapping of region codes to a list of pool IDs (ordered by their failover
              priority) for the given region. Any regions not explicitly defined will fall
              back to using default_pools.

          rules: BETA Field Not General Access: A list of rules for this load balancer to
              execute.

          session_affinity: Specifies the type of session affinity the load balancer should use unless
              specified as `"none"`. The supported types are:

              - `"cookie"`: On the first request to a proxied load balancer, a cookie is
                generated, encoding information of which origin the request will be forwarded
                to. Subsequent requests, by the same client to the same load balancer, will be
                sent to the origin server the cookie encodes, for the duration of the cookie
                and as long as the origin server remains healthy. If the cookie has expired or
                the origin server is unhealthy, then a new origin server is calculated and
                used.
              - `"ip_cookie"`: Behaves the same as `"cookie"` except the initial origin
                selection is stable and based on the client's ip address.
              - `"header"`: On the first request to a proxied load balancer, a session key
                based on the configured HTTP headers (see
                `session_affinity_attributes.headers`) is generated, encoding the request
                headers used for storing in the load balancer session state which origin the
                request will be forwarded to. Subsequent requests to the load balancer with
                the same headers will be sent to the same origin server, for the duration of
                the session and as long as the origin server remains healthy. If the session
                has been idle for the duration of `session_affinity_ttl` seconds or the origin
                server is unhealthy, then a new origin server is calculated and used. See
                `headers` in `session_affinity_attributes` for additional required
                configuration.

          session_affinity_attributes: Configures attributes for session affinity.

          session_affinity_ttl: Time, in seconds, until a client's session expires after being created. Once the
              expiry time has been reached, subsequent requests may get sent to a different
              origin server. The accepted ranges per `session_affinity` policy are:

              - `"cookie"` / `"ip_cookie"`: The current default of 23 hours will be used
                unless explicitly set. The accepted range of values is between [1800, 604800].
              - `"header"`: The current default of 1800 seconds will be used unless explicitly
                set. The accepted range of values is between [30, 3600]. Note: With session
                affinity by header, sessions only expire after they haven't been used for the
                number of seconds specified.

          steering_policy: Steering Policy for this load balancer.

              - `"off"`: Use `default_pools`.
              - `"geo"`: Use `region_pools`/`country_pools`/`pop_pools`. For non-proxied
                requests, the country for `country_pools` is determined by
                `location_strategy`.
              - `"random"`: Select a pool randomly.
              - `"dynamic_latency"`: Use round trip time to select the closest pool in
                default_pools (requires pool health checks).
              - `"proximity"`: Use the pools' latitude and longitude to select the closest
                pool using the Cloudflare PoP location for proxied requests or the location
                determined by `location_strategy` for non-proxied requests.
              - `"least_outstanding_requests"`: Select a pool by taking into consideration
                `random_steering` weights, as well as each pool's number of outstanding
                requests. Pools with more pending requests are weighted proportionately less
                relative to others.
              - `"least_connections"`: Select a pool by taking into consideration
                `random_steering` weights, as well as each pool's number of open connections.
                Pools with more open connections are weighted proportionately less relative to
                others. Supported for HTTP/1 and HTTP/2 connections.
              - `""`: Will map to `"geo"` if you use
                `region_pools`/`country_pools`/`pop_pools` otherwise `"off"`.

          ttl: Time to live (TTL) of the DNS entry for the IP address returned by this load
              balancer. This only applies to gray-clouded (unproxied) load balancers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not load_balancer_id:
            raise ValueError(f"Expected a non-empty value for `load_balancer_id` but received {load_balancer_id!r}")
        return await self._put(
            f"/zones/{zone_id}/load_balancers/{load_balancer_id}",
            body=await async_maybe_transform(
                {
                    "default_pools": default_pools,
                    "fallback_pool": fallback_pool,
                    "name": name,
                    "adaptive_routing": adaptive_routing,
                    "country_pools": country_pools,
                    "description": description,
                    "enabled": enabled,
                    "location_strategy": location_strategy,
                    "networks": networks,
                    "pop_pools": pop_pools,
                    "proxied": proxied,
                    "random_steering": random_steering,
                    "region_pools": region_pools,
                    "rules": rules,
                    "session_affinity": session_affinity,
                    "session_affinity_attributes": session_affinity_attributes,
                    "session_affinity_ttl": session_affinity_ttl,
                    "steering_policy": steering_policy,
                    "ttl": ttl,
                },
                load_balancer_update_params.LoadBalancerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[LoadBalancer]._unwrapper,
            ),
            cast_to=cast(Type[LoadBalancer], ResultWrapper[LoadBalancer]),
        )

    def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[LoadBalancer, AsyncSinglePage[LoadBalancer]]:
        """
        List configured load balancers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/load_balancers",
            page=AsyncSinglePage[LoadBalancer],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=LoadBalancer,
        )

    async def delete(
        self,
        load_balancer_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancerDeleteResponse:
        """
        Delete a configured load balancer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not load_balancer_id:
            raise ValueError(f"Expected a non-empty value for `load_balancer_id` but received {load_balancer_id!r}")
        return await self._delete(
            f"/zones/{zone_id}/load_balancers/{load_balancer_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[LoadBalancerDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[LoadBalancerDeleteResponse], ResultWrapper[LoadBalancerDeleteResponse]),
        )

    async def edit(
        self,
        load_balancer_id: str,
        *,
        zone_id: str,
        adaptive_routing: AdaptiveRoutingParam | NotGiven = NOT_GIVEN,
        country_pools: Dict[str, List[str]] | NotGiven = NOT_GIVEN,
        default_pools: List[DefaultPools] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        fallback_pool: str | NotGiven = NOT_GIVEN,
        location_strategy: LocationStrategyParam | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        pop_pools: Dict[str, List[str]] | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        random_steering: RandomSteeringParam | NotGiven = NOT_GIVEN,
        region_pools: Dict[str, List[str]] | NotGiven = NOT_GIVEN,
        rules: Iterable[RulesParam] | NotGiven = NOT_GIVEN,
        session_affinity: SessionAffinity | NotGiven = NOT_GIVEN,
        session_affinity_attributes: SessionAffinityAttributesParam | NotGiven = NOT_GIVEN,
        session_affinity_ttl: float | NotGiven = NOT_GIVEN,
        steering_policy: SteeringPolicy | NotGiven = NOT_GIVEN,
        ttl: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancer:
        """
        Apply changes to an existing load balancer, overwriting the supplied properties.

        Args:
          adaptive_routing: Controls features that modify the routing of requests to pools and origins in
              response to dynamic conditions, such as during the interval between active
              health monitoring requests. For example, zero-downtime failover occurs
              immediately when an origin becomes unavailable due to HTTP 521, 522, or 523
              response codes. If there is another healthy origin in the same pool, the request
              is retried once against this alternate origin.

          country_pools: A mapping of country codes to a list of pool IDs (ordered by their failover
              priority) for the given country. Any country not explicitly defined will fall
              back to using the corresponding region_pool mapping if it exists else to
              default_pools.

          default_pools: A list of pool IDs ordered by their failover priority. Pools defined here are
              used by default, or when region_pools are not configured for a given region.

          description: Object description.

          enabled: Whether to enable (the default) this load balancer.

          fallback_pool: The pool ID to use when all other pools are detected as unhealthy.

          location_strategy: Controls location-based steering for non-proxied requests. See `steering_policy`
              to learn how steering is affected.

          name: The DNS hostname to associate with your Load Balancer. If this hostname already
              exists as a DNS record in Cloudflare's DNS, the Load Balancer will take
              precedence and the DNS record will not be used.

          pop_pools: (Enterprise only): A mapping of Cloudflare PoP identifiers to a list of pool IDs
              (ordered by their failover priority) for the PoP (datacenter). Any PoPs not
              explicitly defined will fall back to using the corresponding country_pool, then
              region_pool mapping if it exists else to default_pools.

          proxied: Whether the hostname should be gray clouded (false) or orange clouded (true).

          random_steering: Configures pool weights.

              - `steering_policy="random"`: A random pool is selected with probability
                proportional to pool weights.
              - `steering_policy="least_outstanding_requests"`: Use pool weights to scale each
                pool's outstanding requests.
              - `steering_policy="least_connections"`: Use pool weights to scale each pool's
                open connections.

          region_pools: A mapping of region codes to a list of pool IDs (ordered by their failover
              priority) for the given region. Any regions not explicitly defined will fall
              back to using default_pools.

          rules: BETA Field Not General Access: A list of rules for this load balancer to
              execute.

          session_affinity: Specifies the type of session affinity the load balancer should use unless
              specified as `"none"`. The supported types are:

              - `"cookie"`: On the first request to a proxied load balancer, a cookie is
                generated, encoding information of which origin the request will be forwarded
                to. Subsequent requests, by the same client to the same load balancer, will be
                sent to the origin server the cookie encodes, for the duration of the cookie
                and as long as the origin server remains healthy. If the cookie has expired or
                the origin server is unhealthy, then a new origin server is calculated and
                used.
              - `"ip_cookie"`: Behaves the same as `"cookie"` except the initial origin
                selection is stable and based on the client's ip address.
              - `"header"`: On the first request to a proxied load balancer, a session key
                based on the configured HTTP headers (see
                `session_affinity_attributes.headers`) is generated, encoding the request
                headers used for storing in the load balancer session state which origin the
                request will be forwarded to. Subsequent requests to the load balancer with
                the same headers will be sent to the same origin server, for the duration of
                the session and as long as the origin server remains healthy. If the session
                has been idle for the duration of `session_affinity_ttl` seconds or the origin
                server is unhealthy, then a new origin server is calculated and used. See
                `headers` in `session_affinity_attributes` for additional required
                configuration.

          session_affinity_attributes: Configures attributes for session affinity.

          session_affinity_ttl: Time, in seconds, until a client's session expires after being created. Once the
              expiry time has been reached, subsequent requests may get sent to a different
              origin server. The accepted ranges per `session_affinity` policy are:

              - `"cookie"` / `"ip_cookie"`: The current default of 23 hours will be used
                unless explicitly set. The accepted range of values is between [1800, 604800].
              - `"header"`: The current default of 1800 seconds will be used unless explicitly
                set. The accepted range of values is between [30, 3600]. Note: With session
                affinity by header, sessions only expire after they haven't been used for the
                number of seconds specified.

          steering_policy: Steering Policy for this load balancer.

              - `"off"`: Use `default_pools`.
              - `"geo"`: Use `region_pools`/`country_pools`/`pop_pools`. For non-proxied
                requests, the country for `country_pools` is determined by
                `location_strategy`.
              - `"random"`: Select a pool randomly.
              - `"dynamic_latency"`: Use round trip time to select the closest pool in
                default_pools (requires pool health checks).
              - `"proximity"`: Use the pools' latitude and longitude to select the closest
                pool using the Cloudflare PoP location for proxied requests or the location
                determined by `location_strategy` for non-proxied requests.
              - `"least_outstanding_requests"`: Select a pool by taking into consideration
                `random_steering` weights, as well as each pool's number of outstanding
                requests. Pools with more pending requests are weighted proportionately less
                relative to others.
              - `"least_connections"`: Select a pool by taking into consideration
                `random_steering` weights, as well as each pool's number of open connections.
                Pools with more open connections are weighted proportionately less relative to
                others. Supported for HTTP/1 and HTTP/2 connections.
              - `""`: Will map to `"geo"` if you use
                `region_pools`/`country_pools`/`pop_pools` otherwise `"off"`.

          ttl: Time to live (TTL) of the DNS entry for the IP address returned by this load
              balancer. This only applies to gray-clouded (unproxied) load balancers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not load_balancer_id:
            raise ValueError(f"Expected a non-empty value for `load_balancer_id` but received {load_balancer_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/load_balancers/{load_balancer_id}",
            body=await async_maybe_transform(
                {
                    "adaptive_routing": adaptive_routing,
                    "country_pools": country_pools,
                    "default_pools": default_pools,
                    "description": description,
                    "enabled": enabled,
                    "fallback_pool": fallback_pool,
                    "location_strategy": location_strategy,
                    "name": name,
                    "pop_pools": pop_pools,
                    "proxied": proxied,
                    "random_steering": random_steering,
                    "region_pools": region_pools,
                    "rules": rules,
                    "session_affinity": session_affinity,
                    "session_affinity_attributes": session_affinity_attributes,
                    "session_affinity_ttl": session_affinity_ttl,
                    "steering_policy": steering_policy,
                    "ttl": ttl,
                },
                load_balancer_edit_params.LoadBalancerEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[LoadBalancer]._unwrapper,
            ),
            cast_to=cast(Type[LoadBalancer], ResultWrapper[LoadBalancer]),
        )

    async def get(
        self,
        load_balancer_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancer:
        """
        Fetch a single configured load balancer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not load_balancer_id:
            raise ValueError(f"Expected a non-empty value for `load_balancer_id` but received {load_balancer_id!r}")
        return await self._get(
            f"/zones/{zone_id}/load_balancers/{load_balancer_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[LoadBalancer]._unwrapper,
            ),
            cast_to=cast(Type[LoadBalancer], ResultWrapper[LoadBalancer]),
        )


class LoadBalancersResourceWithRawResponse:
    def __init__(self, load_balancers: LoadBalancersResource) -> None:
        self._load_balancers = load_balancers

        self.create = to_raw_response_wrapper(
            load_balancers.create,
        )
        self.update = to_raw_response_wrapper(
            load_balancers.update,
        )
        self.list = to_raw_response_wrapper(
            load_balancers.list,
        )
        self.delete = to_raw_response_wrapper(
            load_balancers.delete,
        )
        self.edit = to_raw_response_wrapper(
            load_balancers.edit,
        )
        self.get = to_raw_response_wrapper(
            load_balancers.get,
        )

    @cached_property
    def monitors(self) -> MonitorsResourceWithRawResponse:
        return MonitorsResourceWithRawResponse(self._load_balancers.monitors)

    @cached_property
    def pools(self) -> PoolsResourceWithRawResponse:
        return PoolsResourceWithRawResponse(self._load_balancers.pools)

    @cached_property
    def previews(self) -> PreviewsResourceWithRawResponse:
        return PreviewsResourceWithRawResponse(self._load_balancers.previews)

    @cached_property
    def regions(self) -> RegionsResourceWithRawResponse:
        return RegionsResourceWithRawResponse(self._load_balancers.regions)

    @cached_property
    def searches(self) -> SearchesResourceWithRawResponse:
        return SearchesResourceWithRawResponse(self._load_balancers.searches)


class AsyncLoadBalancersResourceWithRawResponse:
    def __init__(self, load_balancers: AsyncLoadBalancersResource) -> None:
        self._load_balancers = load_balancers

        self.create = async_to_raw_response_wrapper(
            load_balancers.create,
        )
        self.update = async_to_raw_response_wrapper(
            load_balancers.update,
        )
        self.list = async_to_raw_response_wrapper(
            load_balancers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            load_balancers.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            load_balancers.edit,
        )
        self.get = async_to_raw_response_wrapper(
            load_balancers.get,
        )

    @cached_property
    def monitors(self) -> AsyncMonitorsResourceWithRawResponse:
        return AsyncMonitorsResourceWithRawResponse(self._load_balancers.monitors)

    @cached_property
    def pools(self) -> AsyncPoolsResourceWithRawResponse:
        return AsyncPoolsResourceWithRawResponse(self._load_balancers.pools)

    @cached_property
    def previews(self) -> AsyncPreviewsResourceWithRawResponse:
        return AsyncPreviewsResourceWithRawResponse(self._load_balancers.previews)

    @cached_property
    def regions(self) -> AsyncRegionsResourceWithRawResponse:
        return AsyncRegionsResourceWithRawResponse(self._load_balancers.regions)

    @cached_property
    def searches(self) -> AsyncSearchesResourceWithRawResponse:
        return AsyncSearchesResourceWithRawResponse(self._load_balancers.searches)


class LoadBalancersResourceWithStreamingResponse:
    def __init__(self, load_balancers: LoadBalancersResource) -> None:
        self._load_balancers = load_balancers

        self.create = to_streamed_response_wrapper(
            load_balancers.create,
        )
        self.update = to_streamed_response_wrapper(
            load_balancers.update,
        )
        self.list = to_streamed_response_wrapper(
            load_balancers.list,
        )
        self.delete = to_streamed_response_wrapper(
            load_balancers.delete,
        )
        self.edit = to_streamed_response_wrapper(
            load_balancers.edit,
        )
        self.get = to_streamed_response_wrapper(
            load_balancers.get,
        )

    @cached_property
    def monitors(self) -> MonitorsResourceWithStreamingResponse:
        return MonitorsResourceWithStreamingResponse(self._load_balancers.monitors)

    @cached_property
    def pools(self) -> PoolsResourceWithStreamingResponse:
        return PoolsResourceWithStreamingResponse(self._load_balancers.pools)

    @cached_property
    def previews(self) -> PreviewsResourceWithStreamingResponse:
        return PreviewsResourceWithStreamingResponse(self._load_balancers.previews)

    @cached_property
    def regions(self) -> RegionsResourceWithStreamingResponse:
        return RegionsResourceWithStreamingResponse(self._load_balancers.regions)

    @cached_property
    def searches(self) -> SearchesResourceWithStreamingResponse:
        return SearchesResourceWithStreamingResponse(self._load_balancers.searches)


class AsyncLoadBalancersResourceWithStreamingResponse:
    def __init__(self, load_balancers: AsyncLoadBalancersResource) -> None:
        self._load_balancers = load_balancers

        self.create = async_to_streamed_response_wrapper(
            load_balancers.create,
        )
        self.update = async_to_streamed_response_wrapper(
            load_balancers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            load_balancers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            load_balancers.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            load_balancers.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            load_balancers.get,
        )

    @cached_property
    def monitors(self) -> AsyncMonitorsResourceWithStreamingResponse:
        return AsyncMonitorsResourceWithStreamingResponse(self._load_balancers.monitors)

    @cached_property
    def pools(self) -> AsyncPoolsResourceWithStreamingResponse:
        return AsyncPoolsResourceWithStreamingResponse(self._load_balancers.pools)

    @cached_property
    def previews(self) -> AsyncPreviewsResourceWithStreamingResponse:
        return AsyncPreviewsResourceWithStreamingResponse(self._load_balancers.previews)

    @cached_property
    def regions(self) -> AsyncRegionsResourceWithStreamingResponse:
        return AsyncRegionsResourceWithStreamingResponse(self._load_balancers.regions)

    @cached_property
    def searches(self) -> AsyncSearchesResourceWithStreamingResponse:
        return AsyncSearchesResourceWithStreamingResponse(self._load_balancers.searches)
