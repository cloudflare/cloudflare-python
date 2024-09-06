# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["SearchGlobalResponse", "Search"]


class Search(BaseModel):
    code: str

    name: str

    type: str


class SearchGlobalResponse(BaseModel):
    search: List[Search]
