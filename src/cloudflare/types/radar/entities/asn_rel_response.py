# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from ...unnamed_schema_ref_130 import UnnamedSchemaRef130

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
    meta: UnnamedSchemaRef130

    rels: List[Rel]
