# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = [
    "PoolCreateParams",
    "Origin",
    "OriginHeader",
    "LoadShedding",
    "NotificationFilter",
    "NotificationFilterOrigin",
    "NotificationFilterPool",
    "OriginSteering",
]


class PoolCreateParams(TypedDict, total=False):
    name: Required[str]
    """A short name (tag) for the pool.

    Only alphanumeric characters, hyphens, and underscores are allowed.
    """

    origins: Required[Iterable[Origin]]
    """The list of origins within this pool.

    Traffic directed at this pool is balanced across all currently healthy origins,
    provided the pool itself is healthy.
    """

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
    """A list of regions from which to run health checks.

    Null means every Cloudflare data center.
    """

    description: str
    """A human-readable description of the pool."""

    enabled: bool
    """Whether to enable (the default) or disable this pool.

    Disabled pools will not receive traffic and are excluded from health checks.
    Disabling a pool will cause any load balancers using it to failover to the next
    pool (if any).
    """

    latitude: float
    """
    The latitude of the data center containing the origins used in this pool in
    decimal degrees. If this is set, longitude must also be set.
    """

    load_shedding: LoadShedding
    """Configures load shedding policies and percentages for the pool."""

    longitude: float
    """
    The longitude of the data center containing the origins used in this pool in
    decimal degrees. If this is set, latitude must also be set.
    """

    minimum_origins: int
    """
    The minimum number of origins that must be healthy for this pool to serve
    traffic. If the number of healthy origins falls below this number, the pool will
    be marked unhealthy and will failover to the next available pool.
    """

    monitor: object
    """
    The ID of the Monitor to use for checking the health of origins within this
    pool.
    """

    notification_email: str
    """This field is now deprecated.

    It has been moved to Cloudflare's Centralized Notification service
    https://developers.cloudflare.com/fundamentals/notifications/. The email address
    to send health status notifications to. This can be an individual mailbox or a
    mailing list. Multiple emails can be supplied as a comma delimited list.
    """

    notification_filter: Optional[NotificationFilter]
    """Filter pool and origin health notifications by resource type or health status.

    Use null to reset.
    """

    origin_steering: OriginSteering
    """Configures origin steering for the pool.

    Controls how origins are selected for new sessions and traffic without session
    affinity.
    """


class OriginHeader(TypedDict, total=False):
    host: Annotated[List[str], PropertyInfo(alias="Host")]
    """The 'Host' header allows to override the hostname set in the HTTP request.

    Current support is 1 'Host' header override per origin.
    """


class Origin(TypedDict, total=False):
    address: str
    """
    The IP address (IPv4 or IPv6) of the origin, or its publicly addressable
    hostname. Hostnames entered here should resolve directly to the origin, and not
    be a hostname proxied by Cloudflare. To set an internal/reserved address,
    virtual_network_id must also be set.
    """

    enabled: bool
    """Whether to enable (the default) this origin within the pool.

    Disabled origins will not receive traffic and are excluded from health checks.
    The origin will only be disabled for the current pool.
    """

    header: OriginHeader
    """The request header is used to pass additional information with an HTTP request.

    Currently supported header is 'Host'.
    """

    name: str
    """A human-identifiable name for the origin."""

    virtual_network_id: str
    """The virtual network subnet ID the origin belongs in.

    Virtual network must also belong to the account.
    """

    weight: float
    """The weight of this origin relative to other origins in the pool.

    Based on the configured weight the total traffic is distributed among origins
    within the pool.

    - `origin_steering.policy="least_outstanding_requests"`: Use weight to scale the
      origin's outstanding requests.
    - `origin_steering.policy="least_connections"`: Use weight to scale the origin's
      open connections.
    """


class LoadShedding(TypedDict, total=False):
    default_percent: float
    """The percent of traffic to shed from the pool, according to the default policy.

    Applies to new sessions and traffic without session affinity.
    """

    default_policy: Literal["random", "hash"]
    """The default policy to use when load shedding.

    A random policy randomly sheds a given percent of requests. A hash policy
    computes a hash over the CF-Connecting-IP address and sheds all requests
    originating from a percent of IPs.
    """

    session_percent: float
    """
    The percent of existing sessions to shed from the pool, according to the session
    policy.
    """

    session_policy: Literal["hash"]
    """
    Only the hash policy is supported for existing sessions (to avoid exponential
    decay).
    """


class NotificationFilterOrigin(TypedDict, total=False):
    disable: bool
    """If set true, disable notifications for this type of resource (pool or origin)."""

    healthy: Optional[bool]
    """If present, send notifications only for this health status (e.g.

    false for only DOWN events). Use null to reset (all events).
    """


class NotificationFilterPool(TypedDict, total=False):
    disable: bool
    """If set true, disable notifications for this type of resource (pool or origin)."""

    healthy: Optional[bool]
    """If present, send notifications only for this health status (e.g.

    false for only DOWN events). Use null to reset (all events).
    """


class NotificationFilter(TypedDict, total=False):
    origin: Optional[NotificationFilterOrigin]
    """Filter options for a particular resource type (pool or origin).

    Use null to reset.
    """

    pool: Optional[NotificationFilterPool]
    """Filter options for a particular resource type (pool or origin).

    Use null to reset.
    """


class OriginSteering(TypedDict, total=False):
    policy: Literal["random", "hash", "least_outstanding_requests", "least_connections"]
    """The type of origin steering policy to use.

    - `"random"`: Select an origin randomly.
    - `"hash"`: Select an origin by computing a hash over the CF-Connecting-IP
      address.
    - `"least_outstanding_requests"`: Select an origin by taking into consideration
      origin weights, as well as each origin's number of outstanding requests.
      Origins with more pending requests are weighted proportionately less relative
      to others.
    - `"least_connections"`: Select an origin by taking into consideration origin
      weights, as well as each origin's number of open connections. Origins with
      more open connections are weighted proportionately less relative to others.
      Supported for HTTP/1 and HTTP/2 connections.
    """
