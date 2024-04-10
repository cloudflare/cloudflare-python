# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ...._models import BaseModel

__all__ = ["Layer3TimeseriesResponse", "Serie0"]


class Serie0(BaseModel):
    timestamps: List[datetime]

    values: List[str]


class Layer3TimeseriesResponse(BaseModel):
    meta: object

    serie_0: Serie0
