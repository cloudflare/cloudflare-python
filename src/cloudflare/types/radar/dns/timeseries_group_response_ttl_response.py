# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["TimeseriesGroupResponseTTLResponse", "Serie0"]


class Serie0(BaseModel):
    _0m: List[str] = FieldInfo(alias="<=0m")

    _15m: List[str] = FieldInfo(alias="<=15m")

    _1d: List[str] = FieldInfo(alias="<=1d")

    _1h: List[str] = FieldInfo(alias="<=1h")

    _1m: List[str] = FieldInfo(alias="<=1m")

    _1w: List[str] = FieldInfo(alias="<=1w")

    _1y: List[str] = FieldInfo(alias="<=1y")

    _5m: List[str] = FieldInfo(alias="<=5m")

    _1y: List[str] = FieldInfo(alias=">1y")


class TimeseriesGroupResponseTTLResponse(BaseModel):
    meta: object

    serie_0: Serie0
