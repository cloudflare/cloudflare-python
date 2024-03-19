# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["TimeseriesGroupHTTPProtocolResponse", "Serie0"]


class Serie0(BaseModel):
    http: List[str]

    https: List[str]

    timestamps: List[str]


class TimeseriesGroupHTTPProtocolResponse(BaseModel):
    meta: object

    serie_0: Serie0
