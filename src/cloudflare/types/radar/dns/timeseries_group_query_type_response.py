# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["TimeseriesGroupQueryTypeResponse", "Serie0"]


class Serie0(BaseModel):
    a: List[str] = FieldInfo(alias="A")

    aaaa: List[str] = FieldInfo(alias="AAAA")

    https: List[str] = FieldInfo(alias="HTTPS")

    ns: List[str] = FieldInfo(alias="NS")

    ptr: List[str] = FieldInfo(alias="PTR")


class TimeseriesGroupQueryTypeResponse(BaseModel):
    meta: object

    serie_0: Serie0
