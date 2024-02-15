# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = ["StatCloudflareImagesImagesUsageStatisticsResponse", "Count"]


class Count(BaseModel):
    allowed: Optional[float] = None
    """Cloudflare Images allowed usage."""

    current: Optional[float] = None
    """Cloudflare Images current usage."""


class StatCloudflareImagesImagesUsageStatisticsResponse(BaseModel):
    count: Optional[Count] = None
