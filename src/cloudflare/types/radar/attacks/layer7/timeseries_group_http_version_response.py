# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["TimeseriesGroupHTTPVersionResponse", "Serie0"]


class Serie0(BaseModel):
    http_1_x: List[str] = FieldInfo(alias="HTTP/1.x")

    timestamps: List[str]


class TimeseriesGroupHTTPVersionResponse(BaseModel):
    meta: object

    serie_0: Serie0
