# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from ...unnamed_schema_ref_c5858f1f916a921846e0b6159af470a7 import UnnamedSchemaRefC5858f1f916a921846e0b6159af470a7

__all__ = ["ASNRelResponse", "Rel"]


class Rel(BaseModel):
    asn1: int

    asn1_country: str

    asn1_name: str

    asn2: int

    asn2_country: str

    asn2_name: str

    rel: str


class ASNRelResponse(BaseModel):
    meta: UnnamedSchemaRefC5858f1f916a921846e0b6159af470a7

    rels: List[Rel]
