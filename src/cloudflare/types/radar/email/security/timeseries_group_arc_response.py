# File generated from our OpenAPI spec by Stainless.

from typing import List

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["TimeseriesGroupARCResponse", "Serie0"]


class Serie0(BaseModel):
    fail: List[str] = FieldInfo(alias="FAIL")

    none: List[str] = FieldInfo(alias="NONE")

    pass_: List[str] = FieldInfo(alias="PASS")


class TimeseriesGroupARCResponse(BaseModel):
    meta: object

    serie_0: Serie0
