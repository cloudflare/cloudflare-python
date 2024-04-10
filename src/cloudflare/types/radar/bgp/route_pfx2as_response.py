# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["RoutePfx2asResponse", "Meta", "PrefixOrigin"]


class Meta(BaseModel):
    data_time: str

    query_time: str

    total_peers: int


class PrefixOrigin(BaseModel):
    origin: int

    peer_count: int

    prefix: str

    rpki_validation: str


class RoutePfx2asResponse(BaseModel):
    meta: Meta

    prefix_origins: List[PrefixOrigin]
