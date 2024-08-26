# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["TimeseriesGroupManagedRulesResponse", "Serie0"]


class Serie0(BaseModel):
    bot: List[str] = FieldInfo(alias="Bot")

    timestamps: List[str]


class TimeseriesGroupManagedRulesResponse(BaseModel):
    meta: object

    serie_0: Serie0
