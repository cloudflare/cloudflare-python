# File generated from our OpenAPI spec by Stainless.

from typing import List

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["MaliciousListResponse", "Serie0"]


class Serie0(BaseModel):
    malicious: List[str] = FieldInfo(alias="MALICIOUS")

    not_malicious: List[str] = FieldInfo(alias="NOT_MALICIOUS")


class MaliciousListResponse(BaseModel):
    meta: object

    serie_0: Serie0
