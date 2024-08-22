# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .header import Header
from ..._models import BaseModel

__all__ = ["Origin"]


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

    header: Optional[Header] = None
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
