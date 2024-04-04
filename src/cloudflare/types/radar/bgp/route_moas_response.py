# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from ...unnamed_schema_ref_c5858f1f916a921846e0b6159af470a7 import UnnamedSchemaRefC5858f1f916a921846e0b6159af470a7

__all__ = ["RouteMoasResponse", "Moa", "MoaOrigin"]


class MoaOrigin(BaseModel):
    origin: int

    peer_count: int

    rpki_validation: str


class Moa(BaseModel):
    origins: List[MoaOrigin]

    prefix: str


class RouteMoasResponse(BaseModel):
    meta: UnnamedSchemaRefC5858f1f916a921846e0b6159af470a7

    moas: List[Moa]
