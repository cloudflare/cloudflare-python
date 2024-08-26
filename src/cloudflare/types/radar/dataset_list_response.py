# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

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