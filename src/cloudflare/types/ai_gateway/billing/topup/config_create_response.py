# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from ....._models import BaseModel

__all__ = ["ConfigCreateResponse", "UnionMember0", "UnionMember1", "UnionMember2"]


class UnionMember0(BaseModel):
    amount: float

    threshold: float


class UnionMember1(BaseModel):
    amount: float

    status: Literal["configured"]

    threshold: float


class UnionMember2(BaseModel):
    amount: float

    client_secret: str

    setup_intent_id: str

    status: Literal["requires_action"]

    threshold: float


ConfigCreateResponse: TypeAlias = Union[UnionMember0, UnionMember1, UnionMember2]
