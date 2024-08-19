# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["TimeseriesGroupBotClassResponse", "Serie0"]


class Serie0(BaseModel):
    bot: List[str]

    human: List[str]

    timestamps: List[str]


class TimeseriesGroupBotClassResponse(BaseModel):
    meta: object

    serie_0: Serie0
