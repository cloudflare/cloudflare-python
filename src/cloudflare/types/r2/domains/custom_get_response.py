# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["CustomGetResponse", "Domain", "DomainStatus"]


class DomainStatus(BaseModel):
    ownership: Literal["pending", "active", "deactivated", "blocked", "error", "unknown"]
    """Ownership status of the domain"""

    ssl: Literal["initializing", "pending", "active", "deactivated", "error", "unknown"]
    """SSL certificate status"""


class Domain(BaseModel):
    domain: str
    """Domain name of the custom domain to be added"""

    enabled: bool
    """Whether this bucket is publicly accessible at the specified custom domain"""

    status: DomainStatus

    zone_id: Optional[str] = FieldInfo(alias="zoneId", default=None)
    """Zone ID of the custom domain resides in"""

    zone_name: Optional[str] = FieldInfo(alias="zoneName", default=None)
    """Zone that the custom domain resides in"""


class CustomGetResponse(BaseModel):
    domains: List[Domain]
