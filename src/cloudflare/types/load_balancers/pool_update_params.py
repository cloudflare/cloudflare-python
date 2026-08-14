# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .check_region import CheckRegion
from .origin_param import OriginParam
from .load_shedding_param import LoadSheddingParam
from .origin_steering_param import OriginSteeringParam
from .notification_filter_param import NotificationFilterParam

__all__ = ["PoolUpdateParams"]


class PoolUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    name: Required[str]
    """A short name (tag) for the pool.

    Only alphanumeric characters, hyphens, and underscores are allowed.
    """

    origins: Required[Iterable[OriginParam]]
    """The list of origins within this pool.

    Traffic directed at this pool is balanced across all currently healthy origins,
    provided the pool itself is healthy.
    """

    check_regions: Optional[List[CheckRegion]]
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

    health_sources: Optional[List[Literal["local", "regional", "global"]]]
    """
    A list of health sources, ordered from highest to lowest priority, used to
    evaluate individual origin health and overall pool health. The load balancer
    uses the first source that has data and falls back to the next. Currently
    accepted values are null or the exact array ["regional", "global"]; any other
    combination is rejected. Null (the default) behaves like ["local", "global"].
    ["regional", "global"] makes each region steer on its own health, falling back
    to the global decision when a region has no fresh data. Setting regional
    requires at least one region in check_regions.
    """

    latitude: float
    """
    The latitude of the data center containing the origins used in this pool in
    decimal degrees. If this is set, longitude must also be set.
    """

    load_shedding: Optional[LoadSheddingParam]
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

    monitor: str
    """
    The ID of the Monitor to use for checking the health of origins within this
    pool.
    """

    monitor_group: str
    """
    The ID of the Monitor Group to use for checking the health of origins within
    this pool.
    """

    notification_email: str
    """This field is now deprecated.

    It has been moved to Cloudflare's Centralized Notification service
    https://developers.cloudflare.com/fundamentals/notifications/. The email address
    to send health status notifications to. This can be an individual mailbox or a
    mailing list. Multiple emails can be supplied as a comma delimited list.
    """

    notification_filter: Optional[NotificationFilterParam]
    """Filter pool and origin health notifications by resource type or health status.

    Use null to reset.
    """

    origin_steering: Optional[OriginSteeringParam]
    """Configures origin steering for the pool.

    Controls how origins are selected for new sessions and traffic without session
    affinity.
    """
