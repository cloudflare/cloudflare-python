# File generated from our OpenAPI spec by Stainless.

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["EntityIPsResponse", "IP"]


class IP(BaseModel):
    asn: str

    asn_location: str = FieldInfo(alias="asnLocation")

    asn_name: str = FieldInfo(alias="asnName")

    asn_org_name: str = FieldInfo(alias="asnOrgName")

    ip: str

    ip_version: str = FieldInfo(alias="ipVersion")

    location: str

    location_name: str = FieldInfo(alias="locationName")


class EntityIPsResponse(BaseModel):
    ip: IP
