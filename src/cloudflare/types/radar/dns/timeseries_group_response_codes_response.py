# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["TimeseriesGroupResponseCodesResponse", "Serie0"]


class Serie0(BaseModel):
    noerror: List[str] = FieldInfo(alias="NOERROR")

    notimp: List[str] = FieldInfo(alias="NOTIMP")

    nxdomain: List[str] = FieldInfo(alias="NXDOMAIN")

    refused: List[str] = FieldInfo(alias="REFUSED")

    servfail: List[str] = FieldInfo(alias="SERVFAIL")


class TimeseriesGroupResponseCodesResponse(BaseModel):
    meta: object

    serie_0: Serie0
