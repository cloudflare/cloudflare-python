# File generated from our OpenAPI spec by Stainless.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["TimeseriesGroupDNSSECResponse", "Serie0"]


class Serie0(BaseModel):
    not_supported: List[str] = FieldInfo(alias="NOT_SUPPORTED")

    supported: List[str] = FieldInfo(alias="SUPPORTED")


class TimeseriesGroupDNSSECResponse(BaseModel):
    meta: object

    serie_0: Serie0
