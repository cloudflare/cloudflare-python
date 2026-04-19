# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ASNBotnetThreatFeedResponse", "Ase", "Meta"]


class Ase(BaseModel):
    asn: int

    country: str

    name: str

    rank: int

    rank_change: Optional[int] = FieldInfo(alias="rankChange", default=None)


class Meta(BaseModel):
    date: str

    total: int

    compare_date: Optional[str] = FieldInfo(alias="compareDate", default=None)


class ASNBotnetThreatFeedResponse(BaseModel):
    ases: List[Ase]

    meta: Meta
