# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["DiscoveryAPIShieldEndpointManagementGetAPIDiscoveryResultsForAZoneResponse"]


class DiscoveryAPIShieldEndpointManagementGetAPIDiscoveryResultsForAZoneResponse(BaseModel):
    schemas: Optional[List[object]] = None

    timestamp: Optional[datetime] = None
