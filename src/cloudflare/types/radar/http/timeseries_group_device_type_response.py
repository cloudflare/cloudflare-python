# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["TimeseriesGroupDeviceTypeResponse", "Serie0"]


class Serie0(BaseModel):
    desktop: List[str]

    mobile: List[str]

    other: List[str]

    timestamps: List[str]


class TimeseriesGroupDeviceTypeResponse(BaseModel):
    meta: object

    serie_0: Serie0
