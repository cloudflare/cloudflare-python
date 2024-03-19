# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ....._models import BaseModel

__all__ = ["LoadBalancingAnalytics"]


class LoadBalancingAnalytics(BaseModel):
    id: Optional[int] = None

    origins: Optional[List[object]] = None

    pool: Optional[object] = None

    timestamp: Optional[datetime] = None
