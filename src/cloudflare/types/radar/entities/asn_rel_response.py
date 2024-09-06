# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["ASNRelResponse", "Meta", "Rel"]


class Meta(BaseModel):
    data_time: str

    query_time: str

    total_peers: int


class Rel(BaseModel):
    asn1: int

    asn1_country: str

    asn1_name: str

    asn2: int

    asn2_country: str

    asn2_name: str

    rel: str


class ASNRelResponse(BaseModel):
    meta: Meta

    rels: List[Rel]
