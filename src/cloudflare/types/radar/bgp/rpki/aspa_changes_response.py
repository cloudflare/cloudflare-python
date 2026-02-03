# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["ASPAChangesResponse", "ASNInfo", "ASNInfo_13335", "Change", "ChangeEntry", "Meta"]


class ASNInfo_13335(BaseModel):
    asn: int
    """ASN number."""

    country: str
    """Alpha-2 country code."""

    name: str
    """AS name."""


class ASNInfo(BaseModel):
    api_13335: ASNInfo_13335 = FieldInfo(alias="13335")


class ChangeEntry(BaseModel):
    customer_asn: int = FieldInfo(alias="customerAsn")
    """The customer ASN affected."""

    providers: List[int]

    type: Literal["CustomerAdded", "CustomerRemoved", "ProvidersAdded", "ProvidersRemoved"]


class Change(BaseModel):
    customers_added: int = FieldInfo(alias="customersAdded")
    """Number of new ASPA objects created."""

    customers_removed: int = FieldInfo(alias="customersRemoved")
    """Number of ASPA objects deleted."""

    date: datetime
    """Date of the changes in ISO 8601 format."""

    entries: List[ChangeEntry]

    providers_added: int = FieldInfo(alias="providersAdded")
    """Number of providers added to existing objects."""

    providers_removed: int = FieldInfo(alias="providersRemoved")
    """Number of providers removed from existing objects."""

    total_count: int = FieldInfo(alias="totalCount")
    """Running total of active ASPA objects after this day."""


class Meta(BaseModel):
    data_time: datetime = FieldInfo(alias="dataTime")
    """Timestamp of the underlying data."""

    query_time: datetime = FieldInfo(alias="queryTime")
    """Timestamp when the query was executed."""


class ASPAChangesResponse(BaseModel):
    asn_info: ASNInfo = FieldInfo(alias="asnInfo")

    changes: List[Change]

    meta: Meta
