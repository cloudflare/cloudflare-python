# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["TimeseriesGroupResponseTTLResponse", "Serie0"]


class Serie0(BaseModel):
    _0m: List[str] = FieldInfo(alias="<=0m")

    less_than_or_equal_to_fifteen_minutes: List[str] = FieldInfo(alias="<=15m")

    less_than_or_equal_to_one_day: List[str] = FieldInfo(alias="<=1d")

    less_than_or_equal_to_one_hour: List[str] = FieldInfo(alias="<=1h")

    less_than_or_equal_to_one_minute: List[str] = FieldInfo(alias="<=1m")

    less_than_or_equal_to_one_week: List[str] = FieldInfo(alias="<=1w")

    less_than_or_equal_to_one_year: List[str] = FieldInfo(alias="<=1y")

    less_than_or_equal_to_five_minutes: List[str] = FieldInfo(alias="<=5m")

    greater_than_one_year: List[str] = FieldInfo(alias=">1y")


class TimeseriesGroupResponseTTLResponse(BaseModel):
    meta: object

    serie_0: Serie0
