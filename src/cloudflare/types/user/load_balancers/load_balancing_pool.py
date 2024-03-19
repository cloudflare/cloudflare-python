# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "LoadBalancingPool",
    "LoadShedding",
    "NotificationFilter",
    "NotificationFilterOrigin",
    "NotificationFilterPool",
    "OriginSteering",
    "Origin",
    "OriginHeader",
]


class LoadShedding(BaseModel):
    default_percent: Optional[float] = None
    """The percent of traffic to shed from the pool, according to the default policy.

    Applies to new sessions and traffic without session affinity.
    """

    default_policy: Optional[Literal["random", "hash"]] = None
    """The default policy to use when load shedding.

    A random policy randomly sheds a given percent of requests. A hash policy
    computes a hash over the CF-Connecting-IP address and sheds all requests
    originating from a percent of IPs.
    """

    session_percent: Optional[float] = None
    """
    The percent of existing sessions to shed from the pool, according to the session
    policy.
    """

    session_policy: Optional[Literal["hash"]] = None
    """
    Only the hash policy is supported for existing sessions (to avoid exponential
    decay).
    """


class NotificationFilterOrigin(BaseModel):
    disable: Optional[bool] = None
    """If set true, disable notifications for this type of resource (pool or origin)."""

    healthy: Optional[bool] = None
    """If present, send notifications only for this health status (e.g.

    false for only DOWN events). Use null to reset (all events).
    """


class NotificationFilterPool(BaseModel):
    disable: Optional[bool] = None
    """If set true, disable notifications for this type of resource (pool or origin)."""

    healthy: Optional[bool] = None
    """If present, send notifications only for this health status (e.g.

    false for only DOWN events). Use null to reset (all events).
    """


class NotificationFilter(BaseModel):
    origin: Optional[NotificationFilterOrigin] = None
    """Filter options for a particular resource type (pool or origin).

    Use null to reset.
    """

    pool: Optional[NotificationFilterPool] = None
    """Filter options for a particular resource type (pool or origin).

    Use null to reset.
    """


class OriginSteering(BaseModel):
    policy: Optional[Literal["random", "hash", "least_outstanding_requests", "least_connections"]] = None
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


class OriginHeader(BaseModel):
    host: Optional[List[str]] = FieldInfo(alias="Host", default=None)
    """The 'Host' header allows to override the hostname set in the HTTP request.

    Current support is 1 'Host' header override per origin.
    """


class Origin(BaseModel):
    address: Optional[str] = None
    """
    The IP address (IPv4 or IPv6) of the origin, or its publicly addressable
    hostname. Hostnames entered here should resolve directly to the origin, and not
    be a hostname proxied by Cloudflare. To set an internal/reserved address,
    virtual_network_id must also be set.
    """

    disabled_at: Optional[datetime] = None
    """This field shows up only if the origin is disabled.

    This field is set with the time the origin was disabled.
    """

    enabled: Optional[bool] = None
    """Whether to enable (the default) this origin within the pool.

    Disabled origins will not receive traffic and are excluded from health checks.
    The origin will only be disabled for the current pool.
    """

    header: Optional[OriginHeader] = None
    """The request header is used to pass additional information with an HTTP request.

    Currently supported header is 'Host'.
    """

    name: Optional[str] = None
    """A human-identifiable name for the origin."""

    virtual_network_id: Optional[str] = None
    """The virtual network subnet ID the origin belongs in.

    Virtual network must also belong to the account.
    """

    weight: Optional[float] = None
    """The weight of this origin relative to other origins in the pool.

    Based on the configured weight the total traffic is distributed among origins
    within the pool.

    - `origin_steering.policy="least_outstanding_requests"`: Use weight to scale the
      origin's outstanding requests.
    - `origin_steering.policy="least_connections"`: Use weight to scale the origin's
      open connections.
    """


class LoadBalancingPool(BaseModel):
    id: Optional[str] = None

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
    ] = None
    """A list of regions from which to run health checks.

    Null means every Cloudflare data center.
    """

    created_on: Optional[datetime] = None

    description: Optional[str] = None
    """A human-readable description of the pool."""

    disabled_at: Optional[datetime] = None
    """This field shows up only if the pool is disabled.

    This field is set with the time the pool was disabled at.
    """

    enabled: Optional[bool] = None
    """Whether to enable (the default) or disable this pool.

    Disabled pools will not receive traffic and are excluded from health checks.
    Disabling a pool will cause any load balancers using it to failover to the next
    pool (if any).
    """

    latitude: Optional[float] = None
    """
    The latitude of the data center containing the origins used in this pool in
    decimal degrees. If this is set, longitude must also be set.
    """

    load_shedding: Optional[LoadShedding] = None
    """Configures load shedding policies and percentages for the pool."""

    longitude: Optional[float] = None
    """
    The longitude of the data center containing the origins used in this pool in
    decimal degrees. If this is set, latitude must also be set.
    """

    minimum_origins: Optional[int] = None
    """
    The minimum number of origins that must be healthy for this pool to serve
    traffic. If the number of healthy origins falls below this number, the pool will
    be marked unhealthy and will failover to the next available pool.
    """

    modified_on: Optional[datetime] = None

    monitor: Optional[object] = None
    """
    The ID of the Monitor to use for checking the health of origins within this
    pool.
    """

    name: Optional[str] = None
    """A short name (tag) for the pool.

    Only alphanumeric characters, hyphens, and underscores are allowed.
    """

    notification_email: Optional[str] = None
    """This field is now deprecated.

    It has been moved to Cloudflare's Centralized Notification service
    https://developers.cloudflare.com/fundamentals/notifications/. The email address
    to send health status notifications to. This can be an individual mailbox or a
    mailing list. Multiple emails can be supplied as a comma delimited list.
    """

    notification_filter: Optional[NotificationFilter] = None
    """Filter pool and origin health notifications by resource type or health status.

    Use null to reset.
    """

    origin_steering: Optional[OriginSteering] = None
    """Configures origin steering for the pool.

    Controls how origins are selected for new sessions and traffic without session
    affinity.
    """

    origins: Optional[List[Origin]] = None
    """The list of origins within this pool.

    Traffic directed at this pool is balanced across all currently healthy origins,
    provided the pool itself is healthy.
    """
