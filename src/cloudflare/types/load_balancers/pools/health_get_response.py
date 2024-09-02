# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["HealthGetResponse", "PopHealth", "PopHealthOrigin", "PopHealthOriginIP"]


class PopHealthOriginIP(BaseModel):
    failure_reason: Optional[str] = None
    """Failure reason."""

    healthy: Optional[bool] = None
    """Origin health status."""

    response_code: Optional[float] = None
    """Response code from origin health check."""

    rtt: Optional[str] = None
    """Origin RTT (Round Trip Time) response."""


class PopHealthOrigin(BaseModel):
    ip: Optional[PopHealthOriginIP] = None


class PopHealth(BaseModel):
    healthy: Optional[bool] = None
    """Whether health check in region is healthy."""

    origins: Optional[List[PopHealthOrigin]] = None


class HealthGetResponse(BaseModel):
    pool_id: Optional[str] = None
    """Pool ID"""

    pop_health: Optional[PopHealth] = None
    """List of regions and associated health status."""
