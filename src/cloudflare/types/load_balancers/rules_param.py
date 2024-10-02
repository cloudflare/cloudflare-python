# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import TypedDict

from .default_pools import DefaultPools
from .steering_policy import SteeringPolicy
from .session_affinity import SessionAffinity
from .random_steering_param import RandomSteeringParam
from .adaptive_routing_param import AdaptiveRoutingParam
from .location_strategy_param import LocationStrategyParam
from .session_affinity_attributes_param import SessionAffinityAttributesParam

__all__ = ["RulesParam", "FixedResponse", "Overrides"]


class FixedResponse(TypedDict, total=False):
    content_type: str
    """The http 'Content-Type' header to include in the response."""

    location: str
    """The http 'Location' header to include in the response."""

    message_body: str
    """Text to include as the http body."""

    status_code: int
    """The http status code to respond with."""


class Overrides(TypedDict, total=False):
    adaptive_routing: AdaptiveRoutingParam
    """
    Controls features that modify the routing of requests to pools and origins in
    response to dynamic conditions, such as during the interval between active
    health monitoring requests. For example, zero-downtime failover occurs
    immediately when an origin becomes unavailable due to HTTP 521, 522, or 523
    response codes. If there is another healthy origin in the same pool, the request
    is retried once against this alternate origin.
    """

    country_pools: Dict[str, List[str]]
    """
    A mapping of country codes to a list of pool IDs (ordered by their failover
    priority) for the given country. Any country not explicitly defined will fall
    back to using the corresponding region_pool mapping if it exists else to
    default_pools.
    """

    default_pools: List[DefaultPools]
    """A list of pool IDs ordered by their failover priority.

    Pools defined here are used by default, or when region_pools are not configured
    for a given region.
    """

    fallback_pool: str
    """The pool ID to use when all other pools are detected as unhealthy."""

    location_strategy: LocationStrategyParam
    """Controls location-based steering for non-proxied requests.

    See `steering_policy` to learn how steering is affected.
    """

    pop_pools: Dict[str, List[str]]
    """
    (Enterprise only): A mapping of Cloudflare PoP identifiers to a list of pool IDs
    (ordered by their failover priority) for the PoP (datacenter). Any PoPs not
    explicitly defined will fall back to using the corresponding country_pool, then
    region_pool mapping if it exists else to default_pools.
    """

    random_steering: RandomSteeringParam
    """Configures pool weights.

    - `steering_policy="random"`: A random pool is selected with probability
      proportional to pool weights.
    - `steering_policy="least_outstanding_requests"`: Use pool weights to scale each
      pool's outstanding requests.
    - `steering_policy="least_connections"`: Use pool weights to scale each pool's
      open connections.
    """

    region_pools: Dict[str, List[str]]
    """
    A mapping of region codes to a list of pool IDs (ordered by their failover
    priority) for the given region. Any regions not explicitly defined will fall
    back to using default_pools.
    """

    session_affinity: SessionAffinity
    """
    Specifies the type of session affinity the load balancer should use unless
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
    """

    session_affinity_attributes: SessionAffinityAttributesParam
    """Configures attributes for session affinity."""

    session_affinity_ttl: float
    """Time, in seconds, until a client's session expires after being created.

    Once the expiry time has been reached, subsequent requests may get sent to a
    different origin server. The accepted ranges per `session_affinity` policy are:

    - `"cookie"` / `"ip_cookie"`: The current default of 23 hours will be used
      unless explicitly set. The accepted range of values is between [1800, 604800].
    - `"header"`: The current default of 1800 seconds will be used unless explicitly
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


class RulesParam(TypedDict, total=False):
    condition: str
    """The condition expressions to evaluate.

    If the condition evaluates to true, the overrides or fixed_response in this rule
    will be applied. An empty condition is always true. For more details on
    condition expressions, please see
    https://developers.cloudflare.com/load-balancing/understand-basics/load-balancing-rules/expressions.
    """

    disabled: bool
    """Disable this specific rule.

    It will no longer be evaluated by this load balancer.
    """

    fixed_response: FixedResponse
    """
    A collection of fields used to directly respond to the eyeball instead of
    routing to a pool. If a fixed_response is supplied the rule will be marked as
    terminates.
    """

    name: str
    """Name of this rule. Only used for human readability."""

    overrides: Overrides
    """
    A collection of overrides to apply to the load balancer when this rule's
    condition is true. All fields are optional.
    """

    priority: int
    """The order in which rules should be executed in relation to each other.

    Lower values are executed first. Values do not need to be sequential. If no
    value is provided for any rule the array order of the rules field will be used
    to assign a priority.
    """

    terminates: bool
    """
    If this rule's condition is true, this causes rule evaluation to stop after
    processing this rule.
    """
