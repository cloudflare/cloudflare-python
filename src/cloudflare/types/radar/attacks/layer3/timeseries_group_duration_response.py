# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["TimeseriesGroupDurationResponse", "Serie0"]


class Serie0(BaseModel):
    one_hour_to_three_hours: List[str] = FieldInfo(alias="_1_HOUR_TO_3_HOURS")

    ten_mins_to_twenty_mins: List[str] = FieldInfo(alias="_10_MINS_TO_20_MINS")

    twenty_mins_to_forty_mins: List[str] = FieldInfo(alias="_20_MINS_TO_40_MINS")

    forty_mins_to_one_hour: List[str] = FieldInfo(alias="_40_MINS_TO_1_HOUR")

    over_3_hours: List[str] = FieldInfo(alias="OVER_3_HOURS")

    timestamps: List[str]

    under_10_mins: List[str] = FieldInfo(alias="UNDER_10_MINS")


class TimeseriesGroupDurationResponse(BaseModel):
    meta: object

    serie_0: Serie0
