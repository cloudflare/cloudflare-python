# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["TimeseriesGroupMatchingAnswerResponse", "Serie0"]

class Serie0(BaseModel):
    negative: List[str] = FieldInfo(alias = "NEGATIVE")

    positive: List[str] = FieldInfo(alias = "POSITIVE")

class TimeseriesGroupMatchingAnswerResponse(BaseModel):
    meta: object

    serie_0: Serie0