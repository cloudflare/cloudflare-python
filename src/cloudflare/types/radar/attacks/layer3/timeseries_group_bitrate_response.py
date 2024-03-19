# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["TimeseriesGroupBitrateResponse", "Serie0"]


class Serie0(BaseModel):
    one_gbps_to_ten_gbps: List[str] = FieldInfo(alias="_1_GBPS_TO_10_GBPS")

    ten_gbps_to_one_hundred_gbps: List[str] = FieldInfo(alias="_10_GBPS_TO_100_GBPS")

    five_hundred_mbps_to_one_gbps: List[str] = FieldInfo(alias="_500_MBPS_TO_1_GBPS")

    over_100_gbps: List[str] = FieldInfo(alias="OVER_100_GBPS")

    timestamps: List[str]

    under_500_mbps: List[str] = FieldInfo(alias="UNDER_500_MBPS")


class TimeseriesGroupBitrateResponse(BaseModel):
    meta: object

    serie_0: Serie0
