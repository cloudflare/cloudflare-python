# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["TimeseriesGroupIPVersionResponse", "Serie0"]


class Serie0(BaseModel):
    i_pv4: List[str] = FieldInfo(alias="IPv4")

    i_pv6: List[str] = FieldInfo(alias="IPv6")

    timestamps: List[str]


class TimeseriesGroupIPVersionResponse(BaseModel):
    meta: object

    serie_0: Serie0
