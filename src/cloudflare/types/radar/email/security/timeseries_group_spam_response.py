# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["TimeseriesGroupSpamResponse", "Serie0"]


class Serie0(BaseModel):
    not_spam: List[str] = FieldInfo(alias="NOT_SPAM")

    spam: List[str] = FieldInfo(alias="SPAM")


class TimeseriesGroupSpamResponse(BaseModel):
    meta: object

    serie_0: Serie0
