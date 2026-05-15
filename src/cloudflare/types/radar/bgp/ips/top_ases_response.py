# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["TopAsesResponse", "ASN"]


class ASN(BaseModel):
    asn: int

    v4_24s: int

    v6_48s: int


class TopAsesResponse(BaseModel):
    anchor_ts: datetime = FieldInfo(alias="anchorTs")

    asns: List[ASN]

    country: Optional[str] = None

    metric: str
