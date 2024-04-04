# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from ...unnamed_schema_ref_c5858f1f916a921846e0b6159af470a7 import UnnamedSchemaRefC5858f1f916a921846e0b6159af470a7

__all__ = ["RoutePfx2asResponse", "PrefixOrigin"]


class PrefixOrigin(BaseModel):
    origin: int

    peer_count: int

    prefix: str

    rpki_validation: str


class RoutePfx2asResponse(BaseModel):
    meta: UnnamedSchemaRefC5858f1f916a921846e0b6159af470a7

    prefix_origins: List[PrefixOrigin]
