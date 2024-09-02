# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["TimeseriesGroupResponseCodesResponse", "Serie0"]


class Serie0(BaseModel):
    noerror: List[str] = FieldInfo(alias="NOERROR")

    nxdomain: List[str] = FieldInfo(alias="NXDOMAIN")


class TimeseriesGroupResponseCodesResponse(BaseModel):
    meta: object

    serie_0: Serie0
