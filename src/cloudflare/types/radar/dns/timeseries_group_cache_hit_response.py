# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["TimeseriesGroupCacheHitResponse", "Serie0"]


class Serie0(BaseModel):
    negative: List[str] = FieldInfo(alias="NEGATIVE")

    positive: List[str] = FieldInfo(alias="POSITIVE")


class TimeseriesGroupCacheHitResponse(BaseModel):
    meta: object

    serie_0: Serie0
