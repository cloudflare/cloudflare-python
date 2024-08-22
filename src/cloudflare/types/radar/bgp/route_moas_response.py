# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["RouteMoasResponse", "Meta", "Moa", "MoaOrigin"]

class Meta(BaseModel):
    data_time: str

    query_time: str

    total_peers: int

class MoaOrigin(BaseModel):
    origin: int

    peer_count: int

    rpki_validation: str

class Moa(BaseModel):
    origins: List[MoaOrigin]

    prefix: str

class RouteMoasResponse(BaseModel):
    meta: Meta

    moas: List[Moa]