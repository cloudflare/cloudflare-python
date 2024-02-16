# File generated from our OpenAPI spec by Stainless.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["HTTPHTTPVersionsResponse", "Serie0"]


class Serie0(BaseModel):
    http_1_x: List[str] = FieldInfo(alias="HTTP/1.x")

    http_2: List[str] = FieldInfo(alias="HTTP/2")

    http_3: List[str] = FieldInfo(alias="HTTP/3")

    timestamps: List[str]


class HTTPHTTPVersionsResponse(BaseModel):
    meta: object

    serie_0: Serie0
