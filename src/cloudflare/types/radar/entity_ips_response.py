# File generated from our OpenAPI spec by Stainless.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

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
