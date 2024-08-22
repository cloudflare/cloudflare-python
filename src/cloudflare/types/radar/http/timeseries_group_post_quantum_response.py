# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["TimeseriesGroupPostQuantumResponse", "Serie0"]

class Serie0(BaseModel):
    not_supported: List[str] = FieldInfo(alias = "NOT_SUPPORTED")

    supported: List[str] = FieldInfo(alias = "SUPPORTED")

    timestamps: List[str]

class TimeseriesGroupPostQuantumResponse(BaseModel):
    meta: object

    serie_0: Serie0