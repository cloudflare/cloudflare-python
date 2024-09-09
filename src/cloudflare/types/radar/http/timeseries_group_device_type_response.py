# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["TimeseriesGroupDeviceTypeResponse", "Serie0"]


class Serie0(BaseModel):
    desktop: List[str]

    mobile: List[str]

    other: List[str]

    timestamps: List[str]


class TimeseriesGroupDeviceTypeResponse(BaseModel):
    meta: object

    serie_0: Serie0
