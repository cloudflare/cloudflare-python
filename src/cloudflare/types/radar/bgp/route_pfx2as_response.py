# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["RoutePfx2asResponse", "PrefixOrigin"]


class PrefixOrigin(BaseModel):
    origin: int

    peer_count: int

    prefix: str

    rpki_validation: str


class RoutePfx2asResponse(BaseModel):
    meta: object

    prefix_origins: List[PrefixOrigin]
