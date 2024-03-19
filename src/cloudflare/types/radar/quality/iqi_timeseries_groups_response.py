# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["IQITimeseriesGroupsResponse", "Serie0"]


class Serie0(BaseModel):
    p25: List[str]

    p50: List[str]

    p75: List[str]

    timestamps: List[str]


class IQITimeseriesGroupsResponse(BaseModel):
    meta: object

    serie_0: Serie0
