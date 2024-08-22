# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ASNGetResponse", "ASN", "ASNEstimatedUsers", "ASNEstimatedUsersLocation", "ASNRelated"]


class ASNEstimatedUsersLocation(BaseModel):
    location_alpha2: str = FieldInfo(alias="locationAlpha2")

    location_name: str = FieldInfo(alias="locationName")

    estimated_users: Optional[int] = FieldInfo(alias="estimatedUsers", default=None)
    """Estimated users per location"""


class ASNEstimatedUsers(BaseModel):
    locations: List[ASNEstimatedUsersLocation]

    estimated_users: Optional[int] = FieldInfo(alias="estimatedUsers", default=None)
    """Total estimated users"""


class ASNRelated(BaseModel):
    asn: int

    name: str

    aka: Optional[str] = None

    estimated_users: Optional[int] = FieldInfo(alias="estimatedUsers", default=None)
    """Total estimated users"""


class ASN(BaseModel):
    asn: int

    confidence_level: int = FieldInfo(alias="confidenceLevel")

    country: str

    country_name: str = FieldInfo(alias="countryName")

    estimated_users: ASNEstimatedUsers = FieldInfo(alias="estimatedUsers")

    name: str

    org_name: str = FieldInfo(alias="orgName")

    related: List[ASNRelated]

    source: str
    """Regional Internet Registry"""

    website: str

    aka: Optional[str] = None

    name_long: Optional[str] = FieldInfo(alias="nameLong", default=None)
    """Deprecated field. Please use 'aka'."""


class ASNGetResponse(BaseModel):
    asn: ASN
