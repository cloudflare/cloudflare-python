# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["TimeseriesGroupCompromisedResponse", "Serie0"]


class Serie0(BaseModel):
    clean: List[str] = FieldInfo(alias="CLEAN")

    compromised: List[str] = FieldInfo(alias="COMPROMISED")

    timestamps: List[str]


class TimeseriesGroupCompromisedResponse(BaseModel):
    meta: object

    serie_0: Serie0
