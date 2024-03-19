# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "LoadBalancer",
    "AdaptiveRouting",
    "LocationStrategy",
    "RandomSteering",
    "Rule",
    "RuleFixedResponse",
    "RuleOverrides",
    "RuleOverridesAdaptiveRouting",
    "RuleOverridesLocationStrategy",
    "RuleOverridesRandomSteering",
    "RuleOverridesSessionAffinityAttributes",
    "SessionAffinityAttributes",
]


class AdaptiveRouting(BaseModel):
    failover_across_pools: Optional[bool] = None
    """
    Extends zero-downtime failover of requests to healthy origins from alternate
    pools, when no healthy alternate exists in the same pool, according to the
    failover order defined by traffic and origin steering. When set false (the
    default) zero-downtime failover will only occur between origins within the same
    pool. See `session_affinity_attributes` for control over when sessions are
    broken or reassigned.
    """


class LocationStrategy(BaseModel):
    mode: Optional[Literal["pop", "resolver_ip"]] = None
    """
    Determines the authoritative location when ECS is not preferred, does not exist
    in the request, or its GeoIP lookup is unsuccessful.

    - `"pop"`: Use the Cloudflare PoP location.
    - `"resolver_ip"`: Use the DNS resolver GeoIP location. If the GeoIP lookup is
      unsuccessful, use the Cloudflare PoP location.
    """

    prefer_ecs: Optional[Literal["always", "never", "proximity", "geo"]] = None
    """
    Whether the EDNS Client Subnet (ECS) GeoIP should be preferred as the
    authoritative location.

    - `"always"`: Always prefer ECS.
    - `"never"`: Never prefer ECS.
    - `"proximity"`: Prefer ECS only when `steering_policy="proximity"`.
    - `"geo"`: Prefer ECS only when `steering_policy="geo"`.
    """


class RandomSteering(BaseModel):
    default_weight: Optional[float] = None
    """
    The default weight for pools in the load balancer that are not specified in the
    pool_weights map.
    """

    pool_weights: Optional[object] = None
    """A mapping of pool IDs to custom weights.

    The weight is relative to other pools in the load balancer.
    """


class RuleFixedResponse(BaseModel):
    content_type: Optional[str] = None
    """The http 'Content-Type' header to include in the response."""

    location: Optional[str] = None
    """The http 'Location' header to include in the response."""

    message_body: Optional[str] = None
    """Text to include as the http body."""

    status_code: Optional[int] = None
    """The http status code to respond with."""


class RuleOverridesAdaptiveRouting(BaseModel):
    failover_across_pools: Optional[bool] = None
    """
    Extends zero-downtime failover of requests to healthy origins from alternate
    pools, when no healthy alternate exists in the same pool, according to the
    failover order defined by traffic and origin steering. When set false (the
    default) zero-downtime failover will only occur between origins within the same
    pool. See `session_affinity_attributes` for control over when sessions are
    broken or reassigned.
    """


class RuleOverridesLocationStrategy(BaseModel):
    mode: Optional[Literal["pop", "resolver_ip"]] = None
    """
    Determines the authoritative location when ECS is not preferred, does not exist
    in the request, or its GeoIP lookup is unsuccessful.

    - `"pop"`: Use the Cloudflare PoP location.
    - `"resolver_ip"`: Use the DNS resolver GeoIP location. If the GeoIP lookup is
      unsuccessful, use the Cloudflare PoP location.
    """

    prefer_ecs: Optional[Literal["always", "never", "proximity", "geo"]] = None
    """
    Whether the EDNS Client Subnet (ECS) GeoIP should be preferred as the
    authoritative location.

    - `"always"`: Always prefer ECS.
    - `"never"`: Never prefer ECS.
    - `"proximity"`: Prefer ECS only when `steering_policy="proximity"`.
    - `"geo"`: Prefer ECS only when `steering_policy="geo"`.
    """


class RuleOverridesRandomSteering(BaseModel):
    default_weight: Optional[float] = None
    """
    The default weight for pools in the load balancer that are not specified in the
    pool_weights map.
    """

    pool_weights: Optional[object] = None
    """A mapping of pool IDs to custom weights.

    The weight is relative to other pools in the load balancer.
    """


class RuleOverridesSessionAffinityAttributes(BaseModel):
    drain_duration: Optional[float] = None
    """Configures the drain duration in seconds.

    This field is only used when session affinity is enabled on the load balancer.
    """

    headers: Optional[List[str]] = None
    """
    Configures the names of HTTP headers to base session affinity on when header
    `session_affinity` is enabled. At least one HTTP header name must be provided.
    To specify the exact cookies to be used, include an item in the following
    format: `"cookie:<cookie-name-1>,<cookie-name-2>"` (example) where everything
    after the colon is a comma-separated list of cookie names. Providing only
    `"cookie"` will result in all cookies being used. The default max number of HTTP
    header names that can be provided depends on your plan: 5 for Enterprise, 1 for
    all other plans.
    """

    require_all_headers: Optional[bool] = None
    """
    When header `session_affinity` is enabled, this option can be used to specify
    how HTTP headers on load balancing requests will be used. The supported values
    are:

    - `"true"`: Load balancing requests must contain _all_ of the HTTP headers
      specified by the `headers` session affinity attribute, otherwise sessions
      aren't created.
    - `"false"`: Load balancing requests must contain _at least one_ of the HTTP
      headers specified by the `headers` session affinity attribute, otherwise
      sessions aren't created.
    """

    samesite: Optional[Literal["Auto", "Lax", "None", "Strict"]] = None
    """Configures the SameSite attribute on session affinity cookie.

    Value "Auto" will be translated to "Lax" or "None" depending if Always Use HTTPS
    is enabled. Note: when using value "None", the secure attribute can not be set
    to "Never".
    """

    secure: Optional[Literal["Auto", "Always", "Never"]] = None
    """Configures the Secure attribute on session affinity cookie.

    Value "Always" indicates the Secure attribute will be set in the Set-Cookie
    header, "Never" indicates the Secure attribute will not be set, and "Auto" will
    set the Secure attribute depending if Always Use HTTPS is enabled.
    """

    zero_downtime_failover: Optional[Literal["none", "temporary", "sticky"]] = None
    """
    Configures the zero-downtime failover between origins within a pool when session
    affinity is enabled. This feature is currently incompatible with Argo, Tiered
    Cache, and Bandwidth Alliance. The supported values are:

    - `"none"`: No failover takes place for sessions pinned to the origin (default).
    - `"temporary"`: Traffic will be sent to another other healthy origin until the
      originally pinned origin is available; note that this can potentially result
      in heavy origin flapping.
    - `"sticky"`: The session affinity cookie is updated and subsequent requests are
      sent to the new origin. Note: Zero-downtime failover with sticky sessions is
      currently not supported for session affinity by header.
    """


class RuleOverrides(BaseModel):
    adaptive_routing: Optional[RuleOverridesAdaptiveRouting] = None
    """
    Controls features that modify the routing of requests to pools and origins in
    response to dynamic conditions, such as during the interval between active
    health monitoring requests. For example, zero-downtime failover occurs
    immediately when an origin becomes unavailable due to HTTP 521, 522, or 523
    response codes. If there is another healthy origin in the same pool, the request
    is retried once against this alternate origin.
    """

    country_pools: Optional[object] = None
    """
    A mapping of country codes to a list of pool IDs (ordered by their failover
    priority) for the given country. Any country not explicitly defined will fall
    back to using the corresponding region_pool mapping if it exists else to
    default_pools.
    """

    default_pools: Optional[List[str]] = None
    """A list of pool IDs ordered by their failover priority.

    Pools defined here are used by default, or when region_pools are not configured
    for a given region.
    """

    fallback_pool: Optional[object] = None
    """The pool ID to use when all other pools are detected as unhealthy."""

    location_strategy: Optional[RuleOverridesLocationStrategy] = None
    """Controls location-based steering for non-proxied requests.

    See `steering_policy` to learn how steering is affected.
    """

    pop_pools: Optional[object] = None
    """
    (Enterprise only): A mapping of Cloudflare PoP identifiers to a list of pool IDs
    (ordered by their failover priority) for the PoP (datacenter). Any PoPs not
    explicitly defined will fall back to using the corresponding country_pool, then
    region_pool mapping if it exists else to default_pools.
    """

    random_steering: Optional[RuleOverridesRandomSteering] = None
    """Configures pool weights.

    - `steering_policy="random"`: A random pool is selected with probability
      proportional to pool weights.
    - `steering_policy="least_outstanding_requests"`: Use pool weights to scale each
      pool's outstanding requests.
    - `steering_policy="least_connections"`: Use pool weights to scale each pool's
      open connections.
    """

    region_pools: Optional[object] = None
    """
    A mapping of region codes to a list of pool IDs (ordered by their failover
    priority) for the given region. Any regions not explicitly defined will fall
    back to using default_pools.
    """

    session_affinity: Optional[Literal["none", "cookie", "ip_cookie", "header", '""']] = None
    """
    Specifies the type of session affinity the load balancer should use unless
    specified as `"none"` or "" (default). The supported types are:

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

    session_affinity_attributes: Optional[RuleOverridesSessionAffinityAttributes] = None
    """Configures attributes for session affinity."""

    session_affinity_ttl: Optional[float] = None
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

    steering_policy: Optional[
        Literal[
            "off",
            "geo",
            "random",
            "dynamic_latency",
            "proximity",
            "least_outstanding_requests",
            "least_connections",
            '""',
        ]
    ] = None
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

    ttl: Optional[float] = None
    """
    Time to live (TTL) of the DNS entry for the IP address returned by this load
    balancer. This only applies to gray-clouded (unproxied) load balancers.
    """


class Rule(BaseModel):
    condition: Optional[str] = None
    """The condition expressions to evaluate.

    If the condition evaluates to true, the overrides or fixed_response in this rule
    will be applied. An empty condition is always true. For more details on
    condition expressions, please see
    https://developers.cloudflare.com/load-balancing/understand-basics/load-balancing-rules/expressions.
    """

    disabled: Optional[bool] = None
    """Disable this specific rule.

    It will no longer be evaluated by this load balancer.
    """

    fixed_response: Optional[RuleFixedResponse] = None
    """
    A collection of fields used to directly respond to the eyeball instead of
    routing to a pool. If a fixed_response is supplied the rule will be marked as
    terminates.
    """

    name: Optional[str] = None
    """Name of this rule. Only used for human readability."""

    overrides: Optional[RuleOverrides] = None
    """
    A collection of overrides to apply to the load balancer when this rule's
    condition is true. All fields are optional.
    """

    priority: Optional[int] = None
    """The order in which rules should be executed in relation to each other.

    Lower values are executed first. Values do not need to be sequential. If no
    value is provided for any rule the array order of the rules field will be used
    to assign a priority.
    """

    terminates: Optional[bool] = None
    """
    If this rule's condition is true, this causes rule evaluation to stop after
    processing this rule.
    """


class SessionAffinityAttributes(BaseModel):
    drain_duration: Optional[float] = None
    """Configures the drain duration in seconds.

    This field is only used when session affinity is enabled on the load balancer.
    """

    headers: Optional[List[str]] = None
    """
    Configures the names of HTTP headers to base session affinity on when header
    `session_affinity` is enabled. At least one HTTP header name must be provided.
    To specify the exact cookies to be used, include an item in the following
    format: `"cookie:<cookie-name-1>,<cookie-name-2>"` (example) where everything
    after the colon is a comma-separated list of cookie names. Providing only
    `"cookie"` will result in all cookies being used. The default max number of HTTP
    header names that can be provided depends on your plan: 5 for Enterprise, 1 for
    all other plans.
    """

    require_all_headers: Optional[bool] = None
    """
    When header `session_affinity` is enabled, this option can be used to specify
    how HTTP headers on load balancing requests will be used. The supported values
    are:

    - `"true"`: Load balancing requests must contain _all_ of the HTTP headers
      specified by the `headers` session affinity attribute, otherwise sessions
      aren't created.
    - `"false"`: Load balancing requests must contain _at least one_ of the HTTP
      headers specified by the `headers` session affinity attribute, otherwise
      sessions aren't created.
    """

    samesite: Optional[Literal["Auto", "Lax", "None", "Strict"]] = None
    """Configures the SameSite attribute on session affinity cookie.

    Value "Auto" will be translated to "Lax" or "None" depending if Always Use HTTPS
    is enabled. Note: when using value "None", the secure attribute can not be set
    to "Never".
    """

    secure: Optional[Literal["Auto", "Always", "Never"]] = None
    """Configures the Secure attribute on session affinity cookie.

    Value "Always" indicates the Secure attribute will be set in the Set-Cookie
    header, "Never" indicates the Secure attribute will not be set, and "Auto" will
    set the Secure attribute depending if Always Use HTTPS is enabled.
    """

    zero_downtime_failover: Optional[Literal["none", "temporary", "sticky"]] = None
    """
    Configures the zero-downtime failover between origins within a pool when session
    affinity is enabled. This feature is currently incompatible with Argo, Tiered
    Cache, and Bandwidth Alliance. The supported values are:

    - `"none"`: No failover takes place for sessions pinned to the origin (default).
    - `"temporary"`: Traffic will be sent to another other healthy origin until the
      originally pinned origin is available; note that this can potentially result
      in heavy origin flapping.
    - `"sticky"`: The session affinity cookie is updated and subsequent requests are
      sent to the new origin. Note: Zero-downtime failover with sticky sessions is
      currently not supported for session affinity by header.
    """


class LoadBalancer(BaseModel):
    id: Optional[str] = None

    adaptive_routing: Optional[AdaptiveRouting] = None
    """
    Controls features that modify the routing of requests to pools and origins in
    response to dynamic conditions, such as during the interval between active
    health monitoring requests. For example, zero-downtime failover occurs
    immediately when an origin becomes unavailable due to HTTP 521, 522, or 523
    response codes. If there is another healthy origin in the same pool, the request
    is retried once against this alternate origin.
    """

    country_pools: Optional[object] = None
    """
    A mapping of country codes to a list of pool IDs (ordered by their failover
    priority) for the given country. Any country not explicitly defined will fall
    back to using the corresponding region_pool mapping if it exists else to
    default_pools.
    """

    created_on: Optional[datetime] = None

    default_pools: Optional[List[str]] = None
    """A list of pool IDs ordered by their failover priority.

    Pools defined here are used by default, or when region_pools are not configured
    for a given region.
    """

    description: Optional[str] = None
    """Object description."""

    enabled: Optional[bool] = None
    """Whether to enable (the default) this load balancer."""

    fallback_pool: Optional[object] = None
    """The pool ID to use when all other pools are detected as unhealthy."""

    location_strategy: Optional[LocationStrategy] = None
    """Controls location-based steering for non-proxied requests.

    See `steering_policy` to learn how steering is affected.
    """

    modified_on: Optional[datetime] = None

    name: Optional[str] = None
    """The DNS hostname to associate with your Load Balancer.

    If this hostname already exists as a DNS record in Cloudflare's DNS, the Load
    Balancer will take precedence and the DNS record will not be used.
    """

    pop_pools: Optional[object] = None
    """
    (Enterprise only): A mapping of Cloudflare PoP identifiers to a list of pool IDs
    (ordered by their failover priority) for the PoP (datacenter). Any PoPs not
    explicitly defined will fall back to using the corresponding country_pool, then
    region_pool mapping if it exists else to default_pools.
    """

    proxied: Optional[bool] = None
    """Whether the hostname should be gray clouded (false) or orange clouded (true)."""

    random_steering: Optional[RandomSteering] = None
    """Configures pool weights.

    - `steering_policy="random"`: A random pool is selected with probability
      proportional to pool weights.
    - `steering_policy="least_outstanding_requests"`: Use pool weights to scale each
      pool's outstanding requests.
    - `steering_policy="least_connections"`: Use pool weights to scale each pool's
      open connections.
    """

    region_pools: Optional[object] = None
    """
    A mapping of region codes to a list of pool IDs (ordered by their failover
    priority) for the given region. Any regions not explicitly defined will fall
    back to using default_pools.
    """

    rules: Optional[List[Rule]] = None
    """
    BETA Field Not General Access: A list of rules for this load balancer to
    execute.
    """

    session_affinity: Optional[Literal["none", "cookie", "ip_cookie", "header", '""']] = None
    """
    Specifies the type of session affinity the load balancer should use unless
    specified as `"none"` or "" (default). The supported types are:

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

    session_affinity_attributes: Optional[SessionAffinityAttributes] = None
    """Configures attributes for session affinity."""

    session_affinity_ttl: Optional[float] = None
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

    steering_policy: Optional[
        Literal[
            "off",
            "geo",
            "random",
            "dynamic_latency",
            "proximity",
            "least_outstanding_requests",
            "least_connections",
            '""',
        ]
    ] = None
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

    ttl: Optional[float] = None
    """
    Time to live (TTL) of the DNS entry for the IP address returned by this load
    balancer. This only applies to gray-clouded (unproxied) load balancers.
    """
