# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["DiscoveryAPIShieldEndpointManagementGetAPIDiscoveryResultsForAZoneResponse"]


class DiscoveryAPIShieldEndpointManagementGetAPIDiscoveryResultsForAZoneResponse(BaseModel):
    schemas: Optional[List[object]] = None

    timestamp: Optional[datetime] = None
