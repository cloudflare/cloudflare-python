# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["HealthGetResponse", "POPHealth", "POPHealthOrigin", "POPHealthOriginIP"]


class POPHealthOriginIP(BaseModel):
    failure_reason: Optional[str] = None
    """Failure reason."""

    healthy: Optional[bool] = None
    """Origin health status."""

    response_code: Optional[float] = None
    """Response code from origin health check."""

    rtt: Optional[str] = None
    """Origin RTT (Round Trip Time) response."""


class POPHealthOrigin(BaseModel):
    ip: Optional[POPHealthOriginIP] = None


class POPHealth(BaseModel):
    healthy: Optional[bool] = None
    """Whether health check in region is healthy."""

    origins: Optional[List[POPHealthOrigin]] = None


class HealthGetResponse(BaseModel):
    pool_id: Optional[str] = None
    """Pool ID"""

    pop_health: Optional[POPHealth] = None
    """List of regions and associated health status."""
