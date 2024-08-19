# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RankingTopResponse", "Meta", "MetaTop0", "Top0", "Top0Category"]


class MetaTop0(BaseModel):
    date: str


class Meta(BaseModel):
    top_0: MetaTop0


class Top0Category(BaseModel):
    id: float

    name: str

    super_category_id: float = FieldInfo(alias="superCategoryId")


class Top0(BaseModel):
    categories: List[Top0Category]

    domain: str

    rank: int

    pct_rank_change: Optional[float] = FieldInfo(alias="pctRankChange", default=None)
    """Only available in TRENDING rankings."""


class RankingTopResponse(BaseModel):
    meta: Meta

    top_0: List[Top0]
