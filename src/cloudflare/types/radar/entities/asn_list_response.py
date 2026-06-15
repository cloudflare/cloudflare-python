# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ASNListResponse", "ASN", "ASNEstimatedUsers"]


class ASNEstimatedUsers(BaseModel):
    estimated_users: Optional[int] = FieldInfo(alias="estimatedUsers", default=None)
    """Total estimated users."""


class ASN(BaseModel):
    asn: int

    country: str

    country_name: str = FieldInfo(alias="countryName")

    estimated_users: ASNEstimatedUsers = FieldInfo(alias="estimatedUsers")

    name: str

    aka: Optional[str] = None

    org_name: Optional[str] = FieldInfo(alias="orgName", default=None)

    website: Optional[str] = None


class ASNListResponse(BaseModel):
    asns: List[ASN]
