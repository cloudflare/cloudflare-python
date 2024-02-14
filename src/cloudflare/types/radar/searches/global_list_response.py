# File generated from our OpenAPI spec by Stainless.

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = ["GlobalListResponse", "Search"]


class Search(BaseModel):
    code: str

    name: str

    type: str


class GlobalListResponse(BaseModel):
    search: List[Search]
