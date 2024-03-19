# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["TimeseriesGroupEncryptedResponse", "Serie0"]


class Serie0(BaseModel):
    encrypted: List[str] = FieldInfo(alias="ENCRYPTED")

    not_encrypted: List[str] = FieldInfo(alias="NOT_ENCRYPTED")


class TimeseriesGroupEncryptedResponse(BaseModel):
    meta: object

    serie_0: Serie0
