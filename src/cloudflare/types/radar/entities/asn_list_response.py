# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ASNListResponse", "ASN"]


class ASN(BaseModel):
    asn: int

    country: str

    country_name: str = FieldInfo(alias="countryName")

    name: str

    aka: Optional[str] = None

    name_long: Optional[str] = FieldInfo(alias="nameLong", default=None)
    """Deprecated field. Please use 'aka'."""

    org_name: Optional[str] = FieldInfo(alias="orgName", default=None)

    website: Optional[str] = None


class ASNListResponse(BaseModel):
    asns: List[ASN]
