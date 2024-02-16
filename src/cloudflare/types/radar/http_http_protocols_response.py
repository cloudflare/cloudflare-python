# File generated from our OpenAPI spec by Stainless.

from typing import List

from ..._models import BaseModel

__all__ = ["HTTPHTTPProtocolsResponse", "Serie0"]


class Serie0(BaseModel):
    http: List[str]

    https: List[str]

    timestamps: List[str]


class HTTPHTTPProtocolsResponse(BaseModel):
    meta: object

    serie_0: Serie0
