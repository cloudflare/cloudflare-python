# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

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
