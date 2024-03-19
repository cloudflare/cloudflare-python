# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["TimeseriesGroupSpoofResponse", "Serie0"]


class Serie0(BaseModel):
    not_spoof: List[str] = FieldInfo(alias="NOT_SPOOF")

    spoof: List[str] = FieldInfo(alias="SPOOF")


class TimeseriesGroupSpoofResponse(BaseModel):
    meta: object

    serie_0: Serie0
