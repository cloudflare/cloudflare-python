# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["TimeseriesGroupMaliciousResponse", "Serie0"]


class Serie0(BaseModel):
    malicious: List[str] = FieldInfo(alias="MALICIOUS")

    not_malicious: List[str] = FieldInfo(alias="NOT_MALICIOUS")


class TimeseriesGroupMaliciousResponse(BaseModel):
    meta: object

    serie_0: Serie0
