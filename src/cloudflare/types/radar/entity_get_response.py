# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["EntityGetResponse", "IP"]


class IP(BaseModel):
    asn: str

    asn_location: str = FieldInfo(alias="asnLocation")

    asn_name: str = FieldInfo(alias="asnName")

    asn_org_name: str = FieldInfo(alias="asnOrgName")

    ip: str

    ip_version: str = FieldInfo(alias="ipVersion")

    location: str

    location_name: str = FieldInfo(alias="locationName")


class EntityGetResponse(BaseModel):
    ip: IP
