# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["IQITimeseriesGroupsResponse", "Serie0"]


class Serie0(BaseModel):
    p25: List[str]

    p50: List[str]

    p75: List[str]

    timestamps: List[str]


class IQITimeseriesGroupsResponse(BaseModel):
    meta: object

    serie_0: Serie0
