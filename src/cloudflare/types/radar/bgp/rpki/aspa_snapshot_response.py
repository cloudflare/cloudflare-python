# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["ASPASnapshotResponse", "ASNInfo", "ASNInfo_13335", "ASPAObject", "Meta"]


class ASNInfo_13335(BaseModel):
    asn: int
    """ASN number."""

    country: str
    """Alpha-2 country code."""

    name: str
    """AS name."""


class ASNInfo(BaseModel):
    api_13335: ASNInfo_13335 = FieldInfo(alias="13335")


class ASPAObject(BaseModel):
    customer_asn: int = FieldInfo(alias="customerAsn")
    """The customer ASN publishing the ASPA object."""

    providers: List[int]


class Meta(BaseModel):
    data_time: datetime = FieldInfo(alias="dataTime")
    """Timestamp of the underlying data."""

    query_time: datetime = FieldInfo(alias="queryTime")
    """Timestamp when the query was executed."""

    total_count: int = FieldInfo(alias="totalCount")
    """Total number of ASPA objects."""


class ASPASnapshotResponse(BaseModel):
    asn_info: ASNInfo = FieldInfo(alias="asnInfo")

    aspa_objects: List[ASPAObject] = FieldInfo(alias="aspaObjects")

    meta: Meta
