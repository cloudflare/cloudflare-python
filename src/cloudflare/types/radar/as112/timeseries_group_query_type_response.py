# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["TimeseriesGroupQueryTypeResponse", "Serie0"]


class Serie0(BaseModel):
    a: List[str] = FieldInfo(alias="A")

    aaaa: List[str] = FieldInfo(alias="AAAA")

    ptr: List[str] = FieldInfo(alias="PTR")

    soa: List[str] = FieldInfo(alias="SOA")

    srv: List[str] = FieldInfo(alias="SRV")


class TimeseriesGroupQueryTypeResponse(BaseModel):
    meta: object

    serie_0: Serie0
