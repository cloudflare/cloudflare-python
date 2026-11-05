# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr
from .rules_param import RulesParam
from .default_pools import DefaultPools
from .steering_policy import SteeringPolicy
from .session_affinity import SessionAffinity
from .random_steering_param import RandomSteeringParam
from .adaptive_routing_param import AdaptiveRoutingParam
from .location_strategy_param import LocationStrategyParam
from .session_affinity_attributes_param import SessionAffinityAttributesParam

__all__ = [
    "LoadBalancerCreateParams",
    "PoolSet",
    "PoolSetFixedResponse",
    "PoolSetMatch",
    "PoolSetMatchTopology",
    "PoolSetOverrides",
]


class LoadBalancerCreateParams(TypedDict, total=False):
    default_pools: Required[SequenceNotStr[DefaultPools]]
    """A list of pool IDs ordered by their failover priority.

    Pools defined here are used by default, or when region_pools are not configured
    for a given region.
    """

    fallback_pool: Required[str]
    """The pool ID to use when all other pools are detected as unhealthy."""

    name: Required[str]
    """The DNS hostname to associate with your Load Balancer.

    If this hostname already exists as a DNS record in Cloudflare's DNS, the Load
    Balancer will take precedence and the DNS record will not be used.
    """

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    adaptive_routing: AdaptiveRoutingParam
    """
    Controls features that modify the routing of requests to pools and origins in
    response to dynamic conditions, such as during the interval between active
    health monitoring requests. For example, zero-downtime failover occurs
    immediately when an origin becomes unavailable due to HTTP 521, 522, or 523
    response codes. If there is another healthy origin in the same pool, the request
    is retried once against this alternate origin.
    """

    country_pools: Dict[str, SequenceNotStr[str]]
    """
    A mapping of country codes to a list of pool IDs (ordered by their failover
    priority) for the given country. Any country not explicitly defined will fall
    back to using the corresponding region_pool mapping if it exists else to
    default_pools.
    """

    description: str
    """Object description."""

    enabled: bool
    """Whether to enable (the default) this load balancer."""

    location_strategy: LocationStrategyParam
    """Controls location-based steering for non-proxied requests.

    See `steering_policy` to learn how steering is affected.
    """

    networks: SequenceNotStr[str]
    """List of networks where Load Balancer or Pool is enabled."""

    pool_sets: Iterable[PoolSet]
    """An optional list of pool sets, evaluated in array order with first match wins.

    Pool sets are independent from the standard steering fields (`region_pools` /
    `country_pools` / `pop_pools` / `default_pools` / `steering_policy` /
    `random_steering` / `fallback_pool` / `rules`). On a PATCH, an empty array
    (`pool_sets: []`) clears all pool sets, while omitting the field leaves existing
    pool sets unchanged.
    """

    pop_pools: Dict[str, SequenceNotStr[str]]
    """
    Enterprise only: A mapping of Cloudflare PoP identifiers to a list of pool IDs
    (ordered by their failover priority) for the PoP (datacenter). Any PoPs not
    explicitly defined will fall back to using the corresponding country_pool, then
    region_pool mapping if it exists else to default_pools.
    """

    proxied: bool
    """Whether the hostname should be gray clouded (false) or orange clouded (true)."""

    random_steering: RandomSteeringParam
    """Configures pool weights.

    - `steering_policy="random"`: A random pool is selected with probability
      proportional to pool weights.
    - `steering_policy="least_outstanding_requests"`: Use pool weights to scale each
      pool's outstanding requests.
    - `steering_policy="least_connections"`: Use pool weights to scale each pool's
      open connections.
    """

    region_pools: Dict[str, SequenceNotStr[str]]
    """
    A mapping of region codes to a list of pool IDs (ordered by their failover
    priority) for the given region. Any regions not explicitly defined will fall
    back to using default_pools.
    """

    rules: Iterable[RulesParam]
    """
    BETA Field Not General Access: A list of rules for this load balancer to
    execute.
    """

    session_affinity: SessionAffinity
    """
    Specifies the type of session affinity the load balancer should use unless
    specified as `"none"`. The supported types are: - `"cookie"`: On the first
    request to a proxied load balancer, a cookie is generated, encoding information
    of which origin the request will be forwarded to. Subsequent requests, by the
    same client to the same load balancer, will be sent to the origin server the
    cookie encodes, for the duration of the cookie and as long as the origin server
    remains healthy. If the cookie has expired or the origin server is unhealthy,
    then a new origin server is calculated and used. - `"ip_cookie"`: Behaves the
    same as `"cookie"` except the initial origin selection is stable and based on
    the client's ip address. - `"header"`: On the first request to a proxied load
    balancer, a session key based on the configured HTTP headers (see
    `session_affinity_attributes.headers`) is generated, encoding the request
    headers used for storing in the load balancer session state which origin the
    request will be forwarded to. Subsequent requests to the load balancer with the
    same headers will be sent to the same origin server, for the duration of the
    session and as long as the origin server remains healthy. If the session has
    been idle for the duration of `session_affinity_ttl` seconds or the origin
    server is unhealthy, then a new origin server is calculated and used. See
    `headers` in `session_affinity_attributes` for additional required
    configuration.
    """

    session_affinity_attributes: SessionAffinityAttributesParam
    """Configures attributes for session affinity."""

    session_affinity_ttl: float
    """Time, in seconds, until a client's session expires after being created.

    Once the expiry time has been reached, subsequent requests may get sent to a
    different origin server. The accepted ranges per `session_affinity` policy
    are: - `"cookie"` / `"ip_cookie"`: The current default of 23 hours will be used
    unless explicitly set. The accepted range of values is between [1800, 604800]. -
    `"header"`: The current default of 1800 seconds will be used unless explicitly
    set. The accepted range of values is between [30, 3600]. Note: With session
    affinity by header, sessions only expire after they haven't been used for the
    number of seconds specified.
    """

    steering_policy: SteeringPolicy
    """Steering Policy for this load balancer.

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
    """

    ttl: float
    """
    Time to live (TTL) of the DNS entry for the IP address returned by this load
    balancer. This only applies to gray-clouded (unproxied) load balancers.
    """


class PoolSetFixedResponse(TypedDict, total=False):
    """
    A collection of fields used to directly respond to the client instead of routing to a pool. When supplied on a rule, that rule stops further rule evaluation.
    """

    content_type: str
    """The http 'Content-Type' header to include in the response."""

    location: str
    """The http 'Location' header to include in the response."""

    message_body: str
    """Text to include as the http body."""

    status_code: int
    """The http status code to respond with."""


class PoolSetMatchTopology(TypedDict, total=False):
    """Matches requests by location.

    Set any combination of `pops`, `countries`, and `regions` (at least one is required); a request matches when its value appears in any populated list (e.g. `regions: ["WNAM"]` with `countries: ["US"]` matches a request in either WNAM or the US).
    """

    countries: SequenceNotStr[str]
    """A list of ISO 3166-1 alpha-2 country codes.

    Matches when the request's country is in this list.
    """

    pops: SequenceNotStr[str]
    """A list of Cloudflare PoP codes. Matches when the request's PoP is in this list."""

    regions: SequenceNotStr[str]
    """A list of Cloudflare region codes (e.g.

    `WNAM`, `ENAM`, `WEU`). Matches when the request's region is in this list.
    """


class PoolSetMatch(TypedDict, total=False):
    """Determines which requests a pool set applies to.

    Set `topology` to match by location or `default: true` to match all requests; the two are mutually exclusive. A pool set with no `match` matches all requests.
    """

    default: bool
    """When true, matches every request. Cannot be combined with `topology`."""

    topology: PoolSetMatchTopology
    """Matches requests by location.

    Set any combination of `pops`, `countries`, and `regions` (at least one is
    required); a request matches when its value appears in any populated list (e.g.
    `regions: ["WNAM"]` with `countries: ["US"]` matches a request in either WNAM or
    the US).
    """


class PoolSetOverrides(TypedDict, total=False):
    """The behavior a pool set applies when its `match` succeeds.

    A strict subset of a rule's `overrides`: a pool set replaces the topology wholesale with a flat pool list (`pools`), so only the declarative pool-routing fields plus `fallback_pool` and `steering_policy` are settable. All fields are optional.
    """

    fallback_pool: str
    """The pool ID to use when all other pools are detected as unhealthy."""

    pool_default_weight: float
    """The default weight for pools not listed in `pool_weights`.

    The declarative alternative to `random_steering.default_weight`; mutually
    exclusive with `random_steering`.
    """

    pool_weights: Dict[str, float]
    """A mapping of pool IDs to custom weights, relative to the other pools.

    The declarative alternative to `random_steering.pool_weights`; mutually
    exclusive with `random_steering`.
    """

    pools: SequenceNotStr[str]
    """A flat, ordered list of pool IDs to route the matched audience to.

    Replaces the resolved topology with exactly these pools. Mutually exclusive with
    `fixed_response`.
    """

    steering_policy: SteeringPolicy
    """Steering Policy for this load balancer.

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
    """


class PoolSet(TypedDict, total=False):
    """One entry in a load balancer's `pool_sets`.

    Pool sets are evaluated in array order; the first whose `match` succeeds applies its `overrides` (or `fixed_response`), and evaluation stops there.
    """

    disabled: bool
    """Disable this specific pool set. It will no longer be evaluated."""

    fixed_response: PoolSetFixedResponse
    """
    A collection of fields used to directly respond to the client instead of routing
    to a pool. When supplied on a rule, that rule stops further rule evaluation.
    """

    match: PoolSetMatch
    """Determines which requests a pool set applies to.

    Set `topology` to match by location or `default: true` to match all requests;
    the two are mutually exclusive. A pool set with no `match` matches all requests.
    """

    name: str
    """A human-readable name for this pool set."""

    overrides: PoolSetOverrides
    """The behavior a pool set applies when its `match` succeeds.

    A strict subset of a rule's `overrides`: a pool set replaces the topology
    wholesale with a flat pool list (`pools`), so only the declarative pool-routing
    fields plus `fallback_pool` and `steering_policy` are settable. All fields are
    optional.
    """
