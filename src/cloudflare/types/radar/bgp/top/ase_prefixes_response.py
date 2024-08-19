# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ....._models import BaseModel

__all__ = ["AsePrefixesResponse", "ASN", "Meta"]


class ASN(BaseModel):
    asn: int

    country: str

    name: str

    pfxs_count: int


class Meta(BaseModel):
    data_time: str

    query_time: str

    total_peers: int


class AsePrefixesResponse(BaseModel):
    asns: List[ASN]

    meta: Meta
