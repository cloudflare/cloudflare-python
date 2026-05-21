# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["RegionListResponse"]


class RegionListResponse(BaseModel):
    id: str

    created_on: datetime

    modified_on: datetime

    name: str

    region_key: str

    version: int

    version_created_on: datetime
