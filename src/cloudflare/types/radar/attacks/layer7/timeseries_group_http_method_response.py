# File generated from our OpenAPI spec by Stainless.

from typing import List

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["TimeseriesGroupHTTPMethodResponse", "Serie0"]


class Serie0(BaseModel):
    get: List[str] = FieldInfo(alias="GET")

    timestamps: List[str]


class TimeseriesGroupHTTPMethodResponse(BaseModel):
    meta: object

    serie_0: Serie0
