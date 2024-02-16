# File generated from our OpenAPI spec by Stainless.

from typing import List

from ..._models import BaseModel

__all__ = ["HTTPBotClassesResponse", "Serie0"]


class Serie0(BaseModel):
    bot: List[str]

    human: List[str]

    timestamps: List[str]


class HTTPBotClassesResponse(BaseModel):
    meta: object

    serie_0: Serie0
