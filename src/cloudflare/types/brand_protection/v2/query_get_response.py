# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = [
    "QueryGetResponse",
    "QueryGetResponseItem",
    "QueryGetResponseItemParameters",
    "QueryGetResponseItemParametersStringMatch",
]


class QueryGetResponseItemParametersStringMatch(BaseModel):
    max_edit_distance: float

    pattern: str


class QueryGetResponseItemParameters(BaseModel):
    string_matches: List[QueryGetResponseItemParametersStringMatch]

    max_time: Optional[str] = None

    min_time: Optional[str] = None


class QueryGetResponseItem(BaseModel):
    created: str

    parameters: Optional[QueryGetResponseItemParameters] = None

    query_id: int

    query_tag: str

    scan: bool

    updated: str


QueryGetResponse: TypeAlias = List[QueryGetResponseItem]
