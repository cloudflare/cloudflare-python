# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["TimeseriesGroupIPVersionResponse", "Serie0"]


class Serie0(BaseModel):
    i_pv4: List[str] = FieldInfo(alias="IPv4")

    i_pv6: List[str] = FieldInfo(alias="IPv6")


class TimeseriesGroupIPVersionResponse(BaseModel):
    meta: object

    serie_0: Serie0
