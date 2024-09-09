# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["TimeseriesGroupMitigationProductResponse", "Serie0"]


class Serie0(BaseModel):
    ddos: List[str] = FieldInfo(alias="DDOS")

    timestamps: List[str]


class TimeseriesGroupMitigationProductResponse(BaseModel):
    meta: object

    serie_0: Serie0
