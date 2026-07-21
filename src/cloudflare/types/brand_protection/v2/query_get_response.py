# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = [
    "QueryGetResponse",
    "UnionMember0",
    "UnionMember0Parameters",
    "UnionMember0ParametersStringMatch",
    "UnionMember1",
    "UnionMember1Parameters",
    "UnionMember1ParametersStringMatch",
]


class UnionMember0ParametersStringMatch(BaseModel):
    pattern: str


class UnionMember0Parameters(BaseModel):
    string_matches: List[UnionMember0ParametersStringMatch]

    max_time: Optional[str] = None

    min_time: Optional[str] = None


class UnionMember0(BaseModel):
    created: str

    parameters: Optional[UnionMember0Parameters] = None

    query_id: int

    query_tag: str

    scan: bool

    updated: str


class UnionMember1ParametersStringMatch(BaseModel):
    pattern: str


class UnionMember1Parameters(BaseModel):
    string_matches: List[UnionMember1ParametersStringMatch]

    max_time: Optional[str] = None

    min_time: Optional[str] = None


class UnionMember1(BaseModel):
    created: str

    parameters: Optional[UnionMember1Parameters] = None

    query_id: int

    query_tag: str

    scan: bool

    updated: str


QueryGetResponse: TypeAlias = Union[List[UnionMember0], UnionMember1]
