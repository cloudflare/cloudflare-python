# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["RegionalHostnameGetResponse"]


class RegionalHostnameGetResponse(BaseModel):
    created_on: datetime
    """When the regional hostname was created"""

    hostname: str
    """DNS hostname to be regionalized, must be a subdomain of the zone.

    Wildcards are supported for one level, e.g `*.example.com`
    """

    region_key: str
    """Identifying key for the region"""
