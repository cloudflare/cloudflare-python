# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["PathListResponse", "ASNInfo", "Meta", "Path"]


class ASNInfo(BaseModel):
    asn: int
    """ASN number."""

    country: Optional[str] = None
    """Alpha-2 country code."""

    name: Optional[str] = None
    """AS name."""


class Meta(BaseModel):
    data_time: Optional[datetime] = FieldInfo(alias="dataTime", default=None)
    """Timestamp of the underlying RIB data."""

    effective_collector: Optional[str] = FieldInfo(alias="effectiveCollector", default=None)

    query_time: Optional[datetime] = FieldInfo(alias="queryTime", default=None)
    """Timestamp when the query was executed."""

    stale: bool


class Path(BaseModel):
    collectors: List[str]

    paths_count: int = FieldInfo(alias="pathsCount")

    peers_count: int = FieldInfo(alias="peersCount")

    segment: List[int]


class PathListResponse(BaseModel):
    asn_info: Optional[Dict[str, ASNInfo]] = FieldInfo(alias="asnInfo", default=None)

    collectors: List[str]

    meta: Meta

    paths: List[Path]
