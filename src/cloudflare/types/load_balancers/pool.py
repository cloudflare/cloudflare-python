# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .origin import Origin
from ..._models import BaseModel
from .check_region import CheckRegion
from .load_shedding import LoadShedding
from .origin_steering import OriginSteering
from .notification_filter import NotificationFilter

__all__ = ["Pool"]


class Pool(BaseModel):
    id: Optional[str] = None

    check_regions: Optional[List[CheckRegion]] = None
    """A list of regions from which to run health checks.

    Null means every Cloudflare data center.
    """

    created_on: Optional[str] = None

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

    modified_on: Optional[str] = None

    monitor: Optional[str] = None
    """
    The ID of the Monitor to use for checking the health of origins within this
    pool.
    """

    name: Optional[str] = None
    """A short name (tag) for the pool.

    Only alphanumeric characters, hyphens, and underscores are allowed.
    """

    networks: Optional[List[str]] = None
    """List of networks where Load Balancer or Pool is enabled."""

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
