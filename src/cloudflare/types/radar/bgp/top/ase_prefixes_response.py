# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ....._models import BaseModel
from ....unnamed_schema_ref_130 import UnnamedSchemaRef130

__all__ = ["AsePrefixesResponse", "ASN"]


class ASN(BaseModel):
    asn: int

    country: str

    name: str

    pfxs_count: int


class AsePrefixesResponse(BaseModel):
    asns: List[ASN]

    meta: UnnamedSchemaRef130
