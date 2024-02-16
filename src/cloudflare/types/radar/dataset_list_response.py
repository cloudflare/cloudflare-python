# File generated from our OpenAPI spec by Stainless.

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["DatasetListResponse", "Dataset"]


class Dataset(BaseModel):
    id: int

    description: str

    meta: object

    tags: List[str]

    title: str

    type: str


class DatasetListResponse(BaseModel):
    datasets: List[Dataset]
