# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ...._models import BaseModel

__all__ = ["StatCloudflareImagesImagesUsageStatisticsResponse", "Count"]


class Count(BaseModel):
    allowed: Optional[float] = None
    """Cloudflare Images allowed usage."""

    current: Optional[float] = None
    """Cloudflare Images current usage."""


class StatCloudflareImagesImagesUsageStatisticsResponse(BaseModel):
    count: Optional[Count] = None
